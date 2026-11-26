"""Generate AI videos through the G-Labs webhook server (model: muse).

Usage:
    python tools/glabs_video.py "prompt here" out.mp4 [--env "D:/0008. Key Quân sự/.env"] [--model muse]
"""
import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = "curl/8.5.0"


def load_env(env_path):
    url, key = os.environ.get("G_LABS_URL"), os.environ.get("G_LABS_API_KEY")
    if env_path and not (url and key):
        for line in pathlib.Path(env_path).read_text(encoding="utf-8", errors="ignore").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip('"')
                if k == "G_LABS_URL":
                    url = url or v
                if k == "G_LABS_API_KEY":
                    key = key or v
    if not (url and key):
        raise SystemExit("missing G_LABS_URL / G_LABS_API_KEY (use --env <file>)")
    return url.rstrip("/"), key


def api(base, key, method, path, body=None):
    for attempt in range(6):
        req = urllib.request.Request(
            base + path, method=method, data=json.dumps(body).encode() if body else None,
            headers={"X-API-Key": key, "Content-Type": "application/json", "User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code < 500 or method == "POST":
                raise RuntimeError(f"HTTP {e.code} on {path}")
        except Exception as e:
            if method == "POST":
                raise RuntimeError(f"{type(e).__name__} on {path}")
        time.sleep(4 * (attempt + 1))
    raise RuntimeError("api retries exhausted")


def generate_video(base, key, prompt, dst, model="muse", limit=600):
    body = {"prompt": prompt, "model": model}
    print(f"Submitting video task with model '{model}'...", flush=True)
    res = api(base, key, "POST", "/api/video/generate", body)
    tid = res["task_id"]
    print(f"Task queued. ID: {tid}. Polling status...", flush=True)
    
    t0 = time.time()
    while time.time() - t0 < limit:
        time.sleep(6)
        s = api(base, key, "GET", f"/api/status/{tid}")
        status = s.get("status")
        print(f"Status: {status} ({int(time.time() - t0)}s)", flush=True)
        if status == "completed":
            url = s["results"][0]
            url = base + url[url.index("/api/files/"):]
            print(f"Downloading video from {url}...", flush=True)
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r:
                pathlib.Path(dst).write_bytes(r.read())
            print(f"Saved to {dst} ({round(time.time() - t0)}s)")
            return
        if status == "failed":
            raise RuntimeError(f"{s.get('error_code')} {s.get('error')}")
    raise RuntimeError("Video generation timed out")


def main():
    ap = argparse.ArgumentParser(description="Generate AI video using G-Labs muse model")
    ap.add_argument("prompt", help="Text prompt for video generation")
    ap.add_argument("output", help="Output file path (e.g. out.mp4)")
    ap.add_argument("--env", default="D:/0008. Key Quân sự/.env")
    ap.add_argument("--model", default="muse")
    a = ap.parse_args()

    base, key = load_env(a.env)
    generate_video(base, key, a.prompt, a.output, model=a.model)


if __name__ == "__main__":
    main()
