"""Collect Pexels PHOTO candidates (landscape, >= 1920 px wide) with contact sheets for screening.

Usage: python tools/pexels_photos_collect.py queries.txt OUTDIR [--per 8] [--env FILE]
queries.txt lines: "tag|query". Output: candidates.json, thumbs/<id>.jpg, sheet_XX.jpg. Key from env or --env, never printed.
"""
import argparse
import json
import os
import pathlib
import sys
import time
import urllib.parse
import urllib.request

from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8")
UA = "curl/8.5.0"


def key(env):
    k = os.environ.get("PEXELS_API_KEY")
    if not k and env:
        for l in pathlib.Path(env).read_text(encoding="utf-8", errors="ignore").splitlines():
            if l.startswith("PEXELS_API_KEY="):
                k = l.split("=", 1)[1].strip().strip('"')
    if not k:
        raise SystemExit("missing PEXELS_API_KEY")
    return k


def get(u, k=None):
    h = {"User-Agent": UA}
    if k:
        h["Authorization"] = k
    for a in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=40).read()
        except Exception:
            time.sleep(2 * (a + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries")
    ap.add_argument("outdir")
    ap.add_argument("--per", type=int, default=8)
    ap.add_argument("--env")
    a = ap.parse_args()
    k = key(a.env)
    out = pathlib.Path(a.outdir)
    (out / "thumbs").mkdir(parents=True, exist_ok=True)
    c = {}
    for line in pathlib.Path(a.queries).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        tag, q = line.strip().split("|", 1)
        raw = get("https://api.pexels.com/v1/search?" + urllib.parse.urlencode({"query": q, "per_page": a.per, "orientation": "landscape"}), k)
        n = 0
        for p in (json.loads(raw) if raw else {}).get("photos", []):
            if p["id"] in c or p["width"] < 1920:
                continue
            c[p["id"]] = {"id": p["id"], "tag": tag, "query": q, "w": p["width"], "h": p["height"], "page": p["url"], "by": p["photographer"],
                          "by_url": p["photographer_url"], "alt": p.get("alt", ""), "src": p["src"]["large2x"], "thumb": p["src"]["small"]}
            n += 1
        print(f"{tag:8s} {q:32s} +{n}", flush=True)
        time.sleep(0.4)
    for pid, v in c.items():
        d = out / "thumbs" / f"{pid}.jpg"
        if not d.exists():
            b = get(v["thumb"])
            if b:
                d.write_bytes(b)
    json.dump(list(c.values()), open(out / "candidates.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ids = list(c)
    W, H, cols, per = 320, 200, 6, 30
    for si in range(0, len(ids), per):
        chunk = ids[si:si + per]
        rows = (len(chunk) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * W, rows * H), (20, 20, 20))
        d = ImageDraw.Draw(sheet)
        for i, pid in enumerate(chunk):
            p = out / "thumbs" / f"{pid}.jpg"
            if p.exists():
                sheet.paste(Image.open(p).convert("RGB").resize((W, H)), ((i % cols) * W, (i // cols) * H))
            x, y = (i % cols) * W, (i // cols) * H
            d.rectangle([x, y, x + 140, y + 14], fill=(0, 0, 0))
            d.text((x + 2, y + 1), f"{pid} {c[pid]['tag']}", fill=(255, 255, 0))
        sheet.save(out / f"sheet_{si // per + 1:02d}.jpg", quality=80)
    print("photos", len(ids), "sheets", (len(ids) + per - 1) // per)


if __name__ == "__main__":
    main()
