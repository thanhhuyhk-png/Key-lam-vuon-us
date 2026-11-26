"""Garden US voice via ai33.pro (POST /v3/text-to-speech), poll /v3/task/<id>, download audio, save transcript/SRT if returned.

Usage:
    python tools/ai33_voice.py --env "D:/0008. Key Quân sự/.env" --voice clone_2697441 \
        --text-file scripts/big-idea-062-.../voice-text.txt --out scripts/big-idea-062-.../voice.mp3 [--speed 1.0] [--max-credits 30000]

- Key is read at run time from env AI33_API_KEY or from --env (never printed, never copied into this workspace).
- Prints characters and an estimate (about 1.3 credits per character for cloned voices, measured 2026-10-15 in the military workspace)
  and refuses to run if the estimate is above --max-credits.
- Saves <out>.task.json (task metadata without the text body) and, when the server returns transcript data, <out>.srt.
- Sends one request at a time. User-Agent curl/8.5.0 (Cloudflare rejects urllib's default).
"""
import argparse
import json
import os
import pathlib
import sys
import time
import urllib.request
import uuid

sys.stdout.reconfigure(encoding="utf-8")
BASE = "https://api.ai33.pro"
UA = "curl/8.5.0"


def load_key(env_path):
    k = os.environ.get("AI33_API_KEY")
    if not k and env_path:
        for line in pathlib.Path(env_path).read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("AI33_API_KEY="):
                k = line.split("=", 1)[1].strip().strip('"')
    if not k:
        raise SystemExit("missing AI33_API_KEY (use --env <file>)")
    return k


def request(key, method, path, data=None, headers=None, timeout=90):
    h = {"xi-api-key": key, "User-Agent": UA}
    h.update(headers or {})
    req = urllib.request.Request(BASE + path, data=data, headers=h, method=method)
    return json.loads(urllib.request.urlopen(req, timeout=timeout).read())


def multipart(fields):
    boundary = uuid.uuid4().hex
    out = b""
    for k, v in fields.items():
        out += (f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n').encode() + str(v).encode("utf-8") + b"\r\n"
    out += f"--{boundary}--\r\n".encode()
    return out, {"Content-Type": f"multipart/form-data; boundary={boundary}"}


def fmt(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def find_segments(obj):
    """Return a list of (start_s, end_s, text) if the task JSON contains word/segment timing in a recognizable shape."""
    out = []

    def walk(x):
        if isinstance(x, dict):
            keys = {k.lower(): k for k in x}
            txt = x.get(keys.get("text")) if "text" in keys else (x.get(keys.get("word")) if "word" in keys else None)
            st = next((x[keys[k]] for k in ("start", "start_time", "begin", "from") if k in keys), None)
            en = next((x[keys[k]] for k in ("end", "end_time", "to") if k in keys), None)
            if isinstance(txt, str) and isinstance(st, (int, float)) and isinstance(en, (int, float)):
                out.append((float(st), float(en), txt))
            else:
                for v in x.values():
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)

    walk(obj)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env")
    ap.add_argument("--voice", required=True)
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--max-credits", type=int, default=30000)
    ap.add_argument("--no-transcript", action="store_true")
    a = ap.parse_args()
    key = load_key(a.env)
    text = pathlib.Path(a.text_file).read_text(encoding="utf-8").strip()
    est = int(len(text) * 1.3)
    print("chars", len(text), "| estimated credits ~", est, "| voice", a.voice, "| speed", a.speed, flush=True)
    if est > a.max_credits:
        raise SystemExit(f"estimate {est} > --max-credits {a.max_credits}; raise it explicitly to proceed")
    out = pathlib.Path(a.out)
    fields = {"text": text, "voice_id": a.voice, "speed": a.speed, "file_name": out.stem}
    if not a.no_transcript:
        fields["with_transcript"] = "true"
    body, h = multipart(fields)
    d = request(key, "POST", "/v3/text-to-speech", body, h)
    if not d.get("success"):
        raise SystemExit("submit failed: " + json.dumps(d)[:300])
    tid = d["task_id"]
    print("task", tid, flush=True)
    for _ in range(200):
        t = request(key, "GET", "/v3/task/" + tid)["data"]
        if t["status"] == "done":
            break
        if t["status"] in ("error", "failed"):
            raise SystemExit("task failed: " + json.dumps({k: v for k, v in t.items() if k != "text"})[:400])
        time.sleep(6)
    else:
        raise SystemExit("timeout waiting for task " + tid)
    meta = t.get("metadata", {})
    print("metadata keys:", sorted(meta.keys()), "| task keys:", sorted(k for k in t.keys() if k != "metadata"), flush=True)
    req = urllib.request.Request(meta["audio_url"], headers={"User-Agent": UA})
    out.write_bytes(urllib.request.urlopen(req, timeout=300).read())
    print("saved", out, out.stat().st_size, "bytes | credit_cost", t.get("credit_cost"), flush=True)
    light = {k: v for k, v in t.items() if k != "text"}
    pathlib.Path(str(out) + ".task.json").write_text(json.dumps(light, ensure_ascii=False, indent=1), encoding="utf-8")
    # try to pull an SRT URL or build one from timing data
    srt_url = next((meta[k] for k in meta if "srt" in k.lower() and isinstance(meta[k], str) and meta[k].startswith("http")), None)
    if srt_url:
        req = urllib.request.Request(srt_url, headers={"User-Agent": UA})
        out.with_suffix(".srt").write_bytes(urllib.request.urlopen(req, timeout=120).read())
        print("srt saved (server file)", out.with_suffix(".srt"))
    else:
        segs = find_segments(light)
        if segs:
            lines = []
            for i, (s, e, txt) in enumerate(segs, 1):
                lines += [str(i), f"{fmt(s)} --> {fmt(e)}", txt.strip(), ""]
            out.with_suffix(".srt").write_text("\n".join(lines), encoding="utf-8")
            print("srt built from", len(segs), "timed segments", out.with_suffix(".srt"))
        else:
            print("no transcript/SRT in the response; see .task.json")


if __name__ == "__main__":
    main()
