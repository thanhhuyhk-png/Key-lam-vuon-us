"""Lấy ứng viên footage cho các cảnh S trong video-map.json và dựng ảnh tổng hợp để người/Claude nhìn chọn đúng nghĩa.
Số kết quả tìm kiếm không nói gì về nội dung ("pepper" có thể ra rắn), nên không tự chọn theo số.

Usage:
    python tools/footage_pick.py search scripts/<video>/video-map.json --sheets <thư mục ảnh> [--env <file .env>] [--exclude 091,061,062]
    python tools/footage_pick.py fetch  scripts/<video>/video-map.json [--env <file .env>]

search: ghi footage/candidates.json + ảnh tổng hợp. Thư viện _LIBRARY trước (bỏ clip dùng trong --exclude), rồi Pexels, Pixabay. Không tải clip.
fetch : đọc "pick" trong footage/picks.json ({"093-01": ["pexels:123", ...]}), tải clip vào _LIBRARY/_inbox/<mã>/pexels|pixabay và ghi footage/picks-resolved.csv.
Keys đọc từ env, ./.env, --env; không in ra.
"""
import argparse
import csv
import io
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.parse
import urllib.request

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB = ROOT / "_LIBRARY"
UA = "curl/8.5.0"
MIN_DUR, MIN_W, THUMB_W, THUMB_H, COLS, ROWS = 5.0, 1280, 240, 135, 6, 8


def load_env(extra):
    env = dict(os.environ)
    for p in [pathlib.Path(".env")] + ([pathlib.Path(extra)] if extra else []):
        if p.exists():
            for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.split("=", 1)
                    env.setdefault(k.strip(), v.strip().strip('"'))
    return env


def get(url, headers=None, raw=False):
    h = {"User-Agent": UA}
    h.update(headers or {})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60) as r:
                b = r.read()
                return b if raw else json.loads(b)
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def pexels(q, key, n):
    d = get("https://api.pexels.com/videos/search?" + urllib.parse.urlencode({"query": q, "per_page": 15, "orientation": "landscape"}), {"Authorization": key})
    out = []
    for v in (d or {}).get("videos", []):
        if v.get("duration", 0) < MIN_DUR or v.get("width", 0) < MIN_W:
            continue
        files = sorted([f for f in v.get("video_files", []) if f.get("width") and f.get("file_type") == "video/mp4" and f["width"] <= 1920], key=lambda f: -f["width"])
        if files:
            out.append({"key": f"pexels:{v['id']}", "src": "pexels", "dur": v["duration"], "thumb": v.get("image"), "page": v.get("url"), "by": (v.get("user") or {}).get("name", ""), "dl": files[0]["link"]})
    return out[:n]


def pixabay(q, key, n):
    d = get("https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": key, "q": q, "per_page": 15}))
    out = []
    for v in (d or {}).get("hits", []):
        vs = v.get("videos") or {}
        best = next((vs[k] for k in ("large", "medium") if vs.get(k, {}).get("url") and vs[k].get("width", 0) >= MIN_W), None)
        if best and v.get("duration", 0) >= MIN_DUR:
            out.append({"key": f"pixabay:{v['id']}", "src": "pixabay", "dur": v["duration"], "thumb": best.get("thumbnail") or vs.get("medium", {}).get("thumbnail"), "page": v.get("pageURL"), "by": v.get("user", ""), "dl": best["url"]})
    return out[:n]


def library(words, exclude, n):
    rows = list(csv.DictReader(open(LIB / "catalog.csv", encoding="utf-8-sig")))
    out = []
    for r in rows:
        if r["kind"] != "vid" or any(x in r["used_in"] for x in exclude):
            continue
        hay = (r["tags"] + " " + r["desc"].lower() + " " + r["pool"])
        score = sum(w in hay for w in words)
        if score >= 2:
            out.append((score, {"key": "lib:" + r["id"], "src": "lib", "dur": float(r["duration"] or 0), "path": str(LIB / r["path"]), "desc": r["desc"]}))
    return [x[1] for x in sorted(out, key=lambda x: -x[0])[:n]]


def thumb_of(c):
    try:
        if c["src"] == "lib":
            b = subprocess.run(["ffmpeg", "-v", "error", "-ss", "1", "-i", c["path"], "-frames:v", "1", "-vf", f"scale={THUMB_W}:-2", "-f", "image2pipe", "-c:v", "mjpeg", "-"], capture_output=True).stdout
        else:
            b = get(c["thumb"], raw=True)
        return Image.open(io.BytesIO(b)).convert("RGB").resize((THUMB_W, THUMB_H))
    except Exception:
        return Image.new("RGB", (THUMB_W, THUMB_H), (60, 60, 60))


def cmd_search(a):
    env = load_env(a.env)
    p = pathlib.Path(a.map)
    m = json.loads(p.read_text(encoding="utf-8"))
    exclude = [x for x in (a.exclude or "").split(",") if x]
    scenes = [s for s in m["scenes"] if s["t"] == "S"]
    res, seen = {}, set()
    for s in scenes:
        cs = library(" ".join(s["q"]).lower().split(), exclude, 1)
        cs += pexels(s["q"][0], env["PEXELS_API_KEY"], 4)
        for q in s["q"][:2]:
            cs += pixabay(q, env["PIXABAY_API_KEY"], 2)
            time.sleep(0.3)
        uniq = []
        for c in cs:
            if c["key"] not in seen or len(uniq) < 2:
                if c["key"] not in [u["key"] for u in uniq]:
                    uniq.append(c)
        for c in uniq[:COLS]:
            seen.add(c["key"])
        res[s["id"]] = uniq[:COLS]
        print(s["id"], len(uniq[:COLS]), flush=True)
    (p.parent / "footage" / "candidates.json").write_text(json.dumps(res, ensure_ascii=False, indent=0), encoding="utf-8")
    out = pathlib.Path(a.sheets)
    out.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
    for k in range(0, len(scenes), ROWS):
        batch = scenes[k:k + ROWS]
        sh = Image.new("RGB", (COLS * THUMB_W, len(batch) * (THUMB_H + 22)), (20, 20, 20))
        d = ImageDraw.Draw(sh)
        for r, s in enumerate(batch):
            y = r * (THUMB_H + 22)
            d.text((4, y + 2), f"{s['id']}  {s['show']}", font=font, fill=(255, 220, 80))
            for c_i, c in enumerate(res[s["id"]]):
                sh.paste(thumb_of(c), (c_i * THUMB_W, y + 22))
                d.text((c_i * THUMB_W + 4, y + 26), f"{'abcdef'[c_i]} {c['src'][:3]} {c['dur']:.0f}s", font=font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
        sh.save(out / f"sheet_{k // ROWS + 1:02d}.jpg", quality=85)
    print("sheets ->", out)


def cmd_fetch(a):
    p = pathlib.Path(a.map)
    fdir = p.parent / "footage"
    cand = json.loads((fdir / "candidates.json").read_text(encoding="utf-8"))
    picks = json.loads((fdir / "picks.json").read_text(encoding="utf-8"))
    code = json.loads(p.read_text(encoding="utf-8"))["video"].split("-")[2]
    rows = []
    for sid, keys in picks.items():
        for key in keys:
            c = next((x for x in cand.get(sid, []) if x["key"] == key), None)
            if not c:
                print("không thấy", sid, key)
                continue
            if c["src"] == "lib":
                rows.append([sid, key, c["path"], "", "library", c.get("desc", "")])
                continue
            dest = LIB / "_inbox" / code / c["src"] / (key.replace(":", "_") + ".mp4")
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                b = get(c["dl"], raw=True)
                if not b:
                    print("tải lỗi", sid, key)
                    continue
                dest.write_bytes(b)
            rows.append([sid, key, str(dest), c["page"], c["src"] + " license", c["by"]])
            print(sid, key, dest.stat().st_size // 1024 // 1024, "MB", flush=True)
    with open(fdir / "picks-resolved.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["scene", "key", "file", "source_url", "license", "credit"])
        w.writerows(rows)
    print(len(rows), "clip ->", fdir / "picks-resolved.csv")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["search", "fetch"])
    ap.add_argument("map")
    ap.add_argument("--sheets")
    ap.add_argument("--env")
    ap.add_argument("--exclude")
    a = ap.parse_args()
    {"search": cmd_search, "fetch": cmd_fetch}[a.cmd](a)
