"""Render Garden US thumbnails through the G-Labs webhook server (nano_banana_pro).

Usage:
    python tools/glabs_thumb.py scripts/big-idea-062-.../thumbnail-prompts.md --env "D:/0008. Key Quân sự/.env"

- Reads the first two fenced code blocks under "MASTER PROMPT A" and "MASTER PROMPT B".
- URL and API key are read at run time from the env vars G_LABS_URL / G_LABS_API_KEY, or from the --env file.
  The key is never printed, logged, or copied into this workspace.
- Output: thumbnail-a.jpg / thumbnail-b.jpg next to the prompts file (skips files that already exist; pass --force to redo).
- Flow: POST /api/image/generate -> task_id -> poll /api/status/{id} -> download. Sends A and B one after the other.
"""
import argparse
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = "curl/8.5.0"  # Cloudflare in front of the server rejects urllib's default UA


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


def run_image(base, key, prompt, upscale=True, limit=600):
    body = {"prompt": prompt, "model": "nano_banana_pro", "aspect_ratio": "16:9"}
    if upscale:
        body["upscale"] = ["2K"]
    tid = api(base, key, "POST", "/api/image/generate", body)["task_id"]
    t0 = time.time()
    while time.time() - t0 < limit:
        time.sleep(6)
        s = api(base, key, "GET", f"/api/status/{tid}")
        if s["status"] == "completed":
            return s["results"][0]
        if s["status"] == "failed":
            raise RuntimeError(f"{s.get('error_code')} {s.get('error')}")
    raise RuntimeError("timeout")


def download(base, url, dst):
    url = base + url[url.index("/api/files/"):]
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r:
        pathlib.Path(dst).write_bytes(r.read())


def prompts_from(md_path):
    text = pathlib.Path(md_path).read_text(encoding="utf-8")
    out = {}
    for tag in ("A", "B"):
        m = re.search(r"MASTER PROMPT " + tag + r"\b.*?```\n(.*?)```", text, re.S)
        if not m:
            raise SystemExit(f"MASTER PROMPT {tag} not found")
        out[tag.lower()] = m.group(1).strip()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompts_md")
    ap.add_argument("--env")
    ap.add_argument("--only", choices=["a", "b"])
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    base, key = load_env(a.env)
    folder = pathlib.Path(a.prompts_md).parent
    for name, prompt in prompts_from(a.prompts_md).items():
        if a.only and name != a.only:
            continue
        dst = folder / f"thumbnail-{name}.jpg"
        if dst.exists() and not a.force:
            print(name, "cached")
            continue
        t0 = time.time()
        try:
            try:
                res = run_image(base, key, prompt, upscale=True)
            except RuntimeError as e:
                print(name, "2K failed, retry without upscale:", str(e)[:100], flush=True)
                res = run_image(base, key, prompt, upscale=False)
            download(base, res, dst)
            print(name, "ok", round(time.time() - t0), "s", dst.name, dst.stat().st_size, "bytes", flush=True)
        except Exception as e:
            print(name, "FAIL", str(e)[:200], flush=True)


if __name__ == "__main__":
    main()
