"""Collect Pexels video candidates for screening: metadata + one preview frame each, then contact sheets with IDs.

Usage:
    python tools/pexels_collect.py queries.txt OUTDIR [--per 10] [--env "D:/0008. Key Quân sự/.env"] [--per-sheet 30]

queries.txt lines: "tag|query" (tag = section label). Candidates: landscape, width >= 1280, duration >= 6 s.
OUTDIR gets: candidates.json, thumbs/<id>.jpg, sheet_XX.jpg (6 columns, ID + duration + tag printed on every thumbnail).
Key PEXELS_API_KEY read from env or --env file, never printed. No video files are downloaded here.
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


def load_key(env_path):
    k = os.environ.get("PEXELS_API_KEY")
    if not k and env_path:
        for line in pathlib.Path(env_path).read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("PEXELS_API_KEY="):
                k = line.split("=", 1)[1].strip().strip('"')
    if not k:
        raise SystemExit("missing PEXELS_API_KEY")
    return k


def get(url, key=None):
    h = {"User-Agent": UA}
    if key:
        h["Authorization"] = key
    for a in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=40).read()
        except Exception:
            time.sleep(2 * (a + 1))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries")
    ap.add_argument("outdir")
    ap.add_argument("--per", type=int, default=10)
    ap.add_argument("--env")
    ap.add_argument("--per-sheet", type=int, default=30)
    a = ap.parse_args()
    key = load_key(a.env)
    out = pathlib.Path(a.outdir)
    (out / "thumbs").mkdir(parents=True, exist_ok=True)
    cands = {}
    for line in pathlib.Path(a.queries).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        tag, q = line.split("|", 1)
        raw = get("https://api.pexels.com/videos/search?" + urllib.parse.urlencode({"query": q, "per_page": a.per, "orientation": "landscape"}), key)
        n = 0
        for v in (json.loads(raw) if raw else {}).get("videos", []):
            if v["id"] in cands or v["duration"] < 6 or v["width"] < 1280:
                continue
            pics = v.get("video_pictures") or []
            thumb = pics[len(pics) // 2]["picture"] if pics else v.get("image")
            cands[v["id"]] = {"id": v["id"], "tag": tag, "query": q, "dur": v["duration"], "w": v["width"], "h": v["height"], "page": v["url"],
                              "by": v["user"]["name"], "by_url": v["user"]["url"], "thumb": thumb}
            n += 1
        print(f"{tag:10s} {q:34s} +{n}", flush=True)
        time.sleep(0.4)
    ids = list(cands)
    for vid in ids:
        dst = out / "thumbs" / f"{vid}.jpg"
        if not dst.exists():
            b = get(cands[vid]["thumb"])
            if b:
                dst.write_bytes(b)
    json.dump(list(cands.values()), open(out / "candidates.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    W, H, cols = 320, 180, 6
    for si in range(0, len(ids), a.per_sheet):
        chunk = ids[si:si + a.per_sheet]
        rows = (len(chunk) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * W, rows * H), (20, 20, 20))
        d = ImageDraw.Draw(sheet)
        for i, vid in enumerate(chunk):
            p = out / "thumbs" / f"{vid}.jpg"
            if p.exists():
                im = Image.open(p).convert("RGB").resize((W, H))
                sheet.paste(im, ((i % cols) * W, (i // cols) * H))
            x, y = (i % cols) * W, (i // cols) * H
            d.rectangle([x, y, x + 150, y + 14], fill=(0, 0, 0))
            d.text((x + 2, y + 1), f"{vid} {cands[vid]['dur']}s {cands[vid]['tag']}", fill=(255, 255, 0))
        sheet.save(out / f"sheet_{si // a.per_sheet + 1:02d}.jpg", quality=80)
    print("candidates", len(ids), "sheets", (len(ids) + a.per_sheet - 1) // a.per_sheet, "->", out)


if __name__ == "__main__":
    main()
