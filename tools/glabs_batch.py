"""Batch image generation through the G-Labs server (nano_banana_pro) from a CSV of prompts.

Usage:
    python tools/glabs_batch.py ai_needed.csv OUTDIR --env "D:/0008. Key Quân sự/.env" [--workers 3] [--only AI-ID1,AI-ID2] [--variants 1]

CSV columns: ai_id, uses, prompt. Output: OUTDIR/<ai_id>.jpg (skips existing). With --variants N > 1, also writes <ai_id>-v2.jpg ...
Key/URL read at run time from env or --env (never printed). Sends up to --workers jobs at once (images only; do not use for video).
Log: OUTDIR/log.jsonl.
"""
import argparse
import concurrent.futures as cf
import csv
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = "curl/8.5.0"


def load_env(p):
    url, key = os.environ.get("G_LABS_URL"), os.environ.get("G_LABS_API_KEY")
    if p and not (url and key):
        for l in pathlib.Path(p).read_text(encoding="utf-8", errors="ignore").splitlines():
            if "=" in l and not l.lstrip().startswith("#"):
                k, v = l.split("=", 1)
                k, v = k.strip(), v.strip().strip('"')
                if k == "G_LABS_URL":
                    url = url or v
                if k == "G_LABS_API_KEY":
                    key = key or v
    if not (url and key):
        raise SystemExit("missing G_LABS_URL / G_LABS_API_KEY")
    return url.rstrip("/"), key


def api(base, key, method, path, body=None):
    for a in range(6):
        req = urllib.request.Request(base + path, method=method, data=json.dumps(body).encode() if body else None,
                                     headers={"X-API-Key": key, "Content-Type": "application/json", "User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code < 500 or method == "POST":
                raise RuntimeError(f"HTTP {e.code}")
        except Exception as e:
            if method == "POST":
                raise RuntimeError(type(e).__name__)
        time.sleep(4 * (a + 1))
    raise RuntimeError("api retries exhausted")


def one(base, key, prompt, dst, upscale=True, model="nano_banana_pro"):
    body = {"prompt": prompt, "model": model, "aspect_ratio": "16:9"}
    if upscale:
        body["upscale"] = ["2K"]
    tid = api(base, key, "POST", "/api/image/generate", body)["task_id"]
    t0 = time.time()
    while time.time() - t0 < 700:
        time.sleep(6)
        s = api(base, key, "GET", f"/api/status/{tid}")
        if s["status"] == "completed":
            url = s["results"][0]
            url = base + url[url.index("/api/files/"):]
            dst.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300).read())
            return round(time.time() - t0)
        if s["status"] == "failed":
            raise RuntimeError(f"{s.get('error_code')} {s.get('error')}")
    raise RuntimeError("timeout")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("outdir")
    ap.add_argument("--env")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--only")
    ap.add_argument("--variants", type=int, default=1)
    ap.add_argument("--model", default="nano_banana_pro", help="Model name (e.g. nano_banana_pro, muse)")
    a = ap.parse_args()
    base, key = load_env(a.env)
    out = pathlib.Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    jobs = []
    for r in csv.DictReader(open(a.csv, encoding="utf-8-sig")):
        if a.only and r["ai_id"] not in a.only.split(","):
            continue
        for v in range(a.variants):
            dst = out / (f"{r['ai_id']}.jpg" if v == 0 else f"{r['ai_id']}-v{v + 1}.jpg")
            if not dst.exists():
                jobs.append((r["ai_id"], r["prompt"], dst))
    print("jobs", len(jobs), flush=True)

    def run(j):
        aid, prompt, dst = j
        try:
            try:
                s = one(base, key, prompt, dst, True, a.model)
            except RuntimeError as e:
                s = one(base, key, prompt, dst, False, a.model)
            return aid, dst.name, "ok", s
        except Exception as e:
            return aid, dst.name, "FAIL " + str(e)[:80], 0

    with cf.ThreadPoolExecutor(a.workers) as ex, open(out / "log.jsonl", "a", encoding="utf-8") as lg:
        for res in ex.map(run, jobs):
            print(*res, flush=True)
            lg.write(json.dumps(res, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
