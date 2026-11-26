"""Thư viện footage trung tâm Garden US (kiểu _LIBRARY của kênh Quân sự).

  python tools/garden_lib.py index              # gom footage các video vào _LIBRARY + lập catalog.csv (chạy lại an toàn)
  python tools/garden_lib.py find lamp tomato [--kind vid|img] [--class stock|ai|gfx] [--pool lamp] [--video 062]
  python tools/garden_lib.py stats
  python tools/garden_lib.py ingest             # = index + consolidate: nhận media từ _inbox/<mã> vào thư viện, dọn inbox
  python tools/garden_lib.py consolidate        # video xuất xong: xóa bản gốc, chỉ giữ thư viện
  python tools/garden_lib.py wiki               # dựng trang mục lục wiki (_LIBRARY wiki, ảnh thu nhỏ _thumbs) từ catalog.csv

Nguyên tắc:
- Thư viện: D:\\0002-Team A Nam\\_LIBRARY ; mục lục: _LIBRARY\\catalog.csv.
- Cùng ổ D: dùng hardlink (không tốn thêm dung lượng, đường dẫn cũ trong draft CapCut vẫn chạy). Khác ổ: sao chép.
- Trùng nội dung (sha256) chỉ lưu một bản; mọi video đã dùng ghi ở cột used_in.
- Không xóa, không di chuyển tệp nguồn. Giấy phép/tác giả/URL ghi đủ ở từng dòng.
Thêm video mới: khai báo thêm một mục trong SOURCES (hoặc chạy index sau khi video có manifest.json cùng cấu trúc).
"""
import argparse, csv, hashlib, json, os, re, shutil, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
WS = Path(r"D:\0002-Team A Nam")
LIB = WS / "_LIBRARY"
CATALOG = LIB / "catalog.csv"
FIELDS = ["id", "path", "class", "kind", "origin", "pool", "topic", "desc", "license", "credit", "author_url", "source_url",
          "width", "height", "duration", "bytes", "sha256", "prompt", "tags", "used_in", "original_paths"]

# (mã video, thư mục footage)
def _v(code, slug):
    meta = WS / "scripts" / f"big-idea-{code}-{slug}" / "footage"
    inbox = LIB / "_inbox" / code      # TẢI THẲNG VÀO ĐÂY: _inbox/<mã>/{pexels,photos,ai,gfx}
    return (code, inbox, meta)


# (mã video, thư mục media tải về = _LIBRARY\_inbox\<mã>, thư mục footage của video giữ shotlist.csv / ai_needed.csv)
SOURCES = [_v("062", "sunny-window-winter-veggies")]

VIDEO_NAMES = {"062": "sunny-window-winter-veggies"}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def load():
    if not CATALOG.exists():
        return []
    with open(CATALOG, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def save(rows):
    LIB.mkdir(exist_ok=True)
    with open(CATALOG, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, FIELDS)
        w.writeheader()
        w.writerows(rows)


def place(src, sub, new_id):
    """Đưa tệp vào _LIBRARY\\sub bằng hardlink (fallback copy). Trả về đường dẫn tương đối."""
    dst_dir = LIB / sub
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / f"{new_id}__{src.name}"
    if not dst.exists():
        try:
            os.link(src, dst)
        except OSError:
            shutil.copy2(src, dst)
    return str(dst.relative_to(LIB))


def tags_of(*parts):
    words = re.findall(r"[a-z0-9]+", " ".join(p for p in parts if p).lower())
    return " ".join(sorted(set(w for w in words if len(w) > 2)))


def used_map(video, fdir):
    """asset id -> số lần dùng trong shotlist.csv của video."""
    p = fdir / "shotlist.csv"
    out = {}
    if p.exists():
        for r in csv.DictReader(open(p, encoding="utf-8-sig")):
            out[r["asset"]] = out.get(r["asset"], 0) + 1
    return out


def cmd_index():
    rows = load()
    by_sha = {r["sha256"]: r for r in rows if r["sha256"]}
    counters = {"V": 0, "P": 0, "A": 0, "G": 0}
    for r in rows:
        k = r["id"][:3]
        n = int(r["id"][4:])
        key = {"STK": "V", "PHO": "P", "AIM": "A", "GFX": "G"}.get(k)
        if key:
            counters[key] = max(counters[key], n)
    prefix = {"V": "STK", "P": "PHO", "A": "AIM", "G": "GFX"}
    added = merged = 0
    for video, fdir, meta in SOURCES:
        used = used_map(video, meta)
        items = []   # (path, class, kind, sub, origin, meta)
        mf = fdir / "pexels" / "manifest.json"
        if mf.exists():
            for m in json.load(open(mf, encoding="utf-8")):
                items.append((fdir / "pexels" / m["file"], "stock", "vid", "stock/pexels", "pexels", f"pexels-{m['id']}", {
                    "pool": m["pool"], "desc": m.get("desc", ""), "license": m.get("license", "Pexels License"),
                    "credit": m.get("by", ""), "author_url": m.get("by_url", ""), "source_url": m.get("page", ""),
                    "width": m.get("w", ""), "height": m.get("h", ""), "duration": m.get("dur", ""), "prompt": ""}))
        mf = fdir / "photos" / "manifest.json"
        if mf.exists():
            for m in json.load(open(mf, encoding="utf-8")):
                items.append((fdir / "photos" / m["file"], "stock", "img", "stock/pexels-photo", "pexels", m["id"], {
                    "pool": m["pool"], "desc": m.get("alt", ""), "license": m.get("license", "Pexels License"),
                    "credit": m.get("by", ""), "author_url": m.get("by_url", ""), "source_url": m.get("page", ""),
                    "width": "", "height": "", "duration": "", "prompt": ""}))
        prompts = {}
        pa = meta / "ai_needed.csv"
        if pa.exists():
            for r in csv.DictReader(open(pa, encoding="utf-8-sig")):
                prompts[r["ai_id"]] = r["prompt"]
        for p in sorted((fdir / "ai").glob("AI-*.jpg")) if (fdir / "ai").exists() else []:
            aid = p.stem
            items.append((p, "ai", "img", "ai/img-glabs", "glabs-nano-banana-pro", aid, {
                "pool": "ai", "desc": aid.replace("AI-", "").replace("-", " ").lower(), "license": "AI-generated (own account)",
                "credit": "G-Labs nano_banana_pro", "author_url": "", "source_url": "", "width": "", "height": "", "duration": "",
                "prompt": prompts.get(re.sub(r"-v\d+$", "", aid), "")}))
        for p in sorted((fdir / "gfx").glob("*.png")) if (fdir / "gfx").exists() else []:
            items.append((p, "gfx", "img", "gfx", "code-pil", p.stem, {
                "pool": "gfx", "desc": "thẻ đồ họa " + p.stem, "license": "own", "credit": "tools/garden_gfx.py",
                "author_url": "", "source_url": "", "width": "", "height": "", "duration": "", "prompt": ""}))
        for p, cls, kind, sub, origin, aid, meta in items:
            if not p.exists():
                continue
            h = sha(p)
            uses = used.get(aid) or used.get(aid.replace("pexels-photo-", "pexels-photo-"), 0)
            tag = f"{video}x{uses}" if uses else f"{video}x0"
            if h in by_sha:
                row = by_sha[h]
                if tag not in row["used_in"].split(";"):
                    row["used_in"] = ";".join(filter(None, row["used_in"].split(";") + [tag]))
                if str(p) not in row["original_paths"].split(" | "):
                    row["original_paths"] += " | " + str(p)
                merged += 1
                continue
            key = {"vid": "V", "img": "P"}[kind] if cls == "stock" else {"ai": "A", "gfx": "G"}[cls]
            counters[key] += 1
            nid = f"{prefix[key]}-{counters[key]:06d}"
            rel = place(p, sub, nid)
            row = {"id": nid, "path": rel, "class": cls, "kind": kind, "origin": origin, "pool": meta["pool"],
                   "topic": meta["pool"], "desc": meta["desc"], "license": meta["license"], "credit": meta["credit"],
                   "author_url": meta["author_url"], "source_url": meta["source_url"], "width": meta["width"],
                   "height": meta["height"], "duration": meta["duration"], "bytes": p.stat().st_size, "sha256": h,
                   "prompt": meta["prompt"], "tags": tags_of(meta["pool"], meta["desc"], aid, meta["credit"]),
                   "used_in": tag, "original_paths": str(p)}
            rows.append(row)
            by_sha[h] = row
            added += 1
    save(rows)
    print(f"đã thêm {added}, gộp trùng/cập nhật {merged}, tổng {len(rows)} dòng -> {CATALOG}")
    cmd_stats()


def cmd_stats():
    rows = load()
    tot = sum(int(r["bytes"] or 0) for r in rows)
    print(f"tổng {len(rows)} tệp · {tot / 1e9:.2f} GB (hardlink: không tốn thêm nếu cùng ổ)")
    c = {}
    for r in rows:
        c[(r["class"], r["kind"])] = c.get((r["class"], r["kind"]), 0) + 1
    for k, v in sorted(c.items()):
        print(" ", k, v)
    pools = {}
    for r in rows:
        pools[r["pool"]] = pools.get(r["pool"], 0) + 1
    print("theo chủ đề:", dict(sorted(pools.items(), key=lambda x: -x[1])))


def cmd_find(a):
    rows = load()
    kws = [k.lower() for k in a.words]
    out = []
    for r in rows:
        if a.kind and r["kind"] != a.kind:
            continue
        if a.cls and r["class"] != a.cls:
            continue
        if a.pool and r["pool"] != a.pool:
            continue
        if a.video and a.video not in r["used_in"]:
            continue
        hay = (r["tags"] + " " + r["desc"].lower() + " " + r["pool"])
        if all(k in hay for k in kws):
            out.append(r)
    for r in out[:a.limit]:
        d = f"{r['duration']}s" if r["duration"] else ""
        print(f"{r['id']} [{r['kind']}/{r['pool']}] {d} {r['desc'][:70]} · dùng: {r['used_in']} · {LIB / r['path']}")
    print(f"-- {len(out)} kết quả")


def cmd_consolidate():
    """Sau khi video xuất xong: xóa bản gốc trong folder video (chỉ khi thư viện đã có bản trùng sha256), giữ manifest vào _LIBRARY/_manifests."""
    rows = load()
    by_sha = {r["sha256"]: r for r in rows}
    freed = removed = 0
    for video, fdir, meta in SOURCES:
        mdir = LIB / "_manifests" / video
        mdir.mkdir(parents=True, exist_ok=True)
        for sub in ("pexels", "photos"):
            m = fdir / sub / "manifest.json"
            if not m.exists():
                m = meta / sub / "manifest.json"
            if m.exists():
                shutil.copy2(m, mdir / f"{sub}-manifest.json")
        for sub, pat in (("pexels", "*.mp4"), ("photos", "*.jpg"), ("ai", "AI-*.jpg"), ("gfx", "*.png")):
            for p in sorted((fdir / sub).glob(pat)) if (fdir / sub).exists() else []:
                r = by_sha.get(sha(p))
                if r and (LIB / r["path"]).exists():
                    freed += p.stat().st_size
                    p.unlink()
                    removed += 1
                else:
                    print("GIỮ (chưa có trong thư viện):", p)
        for sub in ("pexels", "photos", "ai", "gfx", "screen", "screen_photos", "frames", "unsplash"):
            d = fdir / sub
            if d.exists():
                if sub in ("screen", "screen_photos", "frames", "unsplash"):
                    shutil.rmtree(d)
                else:
                    for x in d.iterdir():
                        if x.is_file() and x.name in ("manifest.json", "_sheet.jpg", "log.jsonl"):
                            x.unlink()
                    if not any(d.iterdir()):
                        d.rmdir()
    for r in rows:
        r["original_paths"] = "(đã gom về thư viện)"
    save(rows)
    print(f"đã xóa {removed} bản gốc ({freed / 1e9:.2f} GB nhìn từ folder video); thư viện giữ bản duy nhất")


def thumb(r, tdir):
    out = tdir / f"{r['id']}.jpg"
    if out.exists():
        return
    src = LIB / r["path"]
    if r["kind"] == "vid":
        import subprocess
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "1", "-i", str(src), "-frames:v", "1",
                        "-vf", "scale=320:-2", "-q:v", "4", str(out)], check=False)
    else:
        from PIL import Image
        im = Image.open(src).convert("RGB")
        im.thumbnail((320, 320))
        im.save(out, quality=82)


def cmd_wiki():
    rows = load()
    W = LIB / "wiki"
    T = W / "_thumbs"
    T.mkdir(parents=True, exist_ok=True)
    for r in rows:
        thumb(r, T)
    pools = {}
    for r in rows:
        pools.setdefault(r["pool"], []).append(r)
    idx = ["# Thư viện footage Garden US — mục lục", "",
           f"{len(rows)} tệp · cập nhật từ `catalog.csv` (không sửa tay; chạy `python tools/garden_lib.py wiki`).",
           "Tìm nhanh: `python tools/garden_lib.py find <từ khóa> [--kind vid] [--pool lamp]`.", "",
           "| Chủ đề | Clip | Ảnh | Tổng |", "|---|---:|---:|---:|"]
    for pool, rs in sorted(pools.items(), key=lambda x: -len(x[1])):
        v = sum(1 for r in rs if r["kind"] == "vid")
        idx.append(f"| [[{pool}]] | {v} | {len(rs) - v} | {len(rs)} |")
    idx += ["", "## Video đã dùng footage", ""]
    vids = {}
    for r in rows:
        for t in filter(None, r["used_in"].split(";")):
            vids.setdefault(t.split("x")[0], 0)
            vids[t.split("x")[0]] += 1
    for v, n in sorted(vids.items()):
        idx.append(f"- {v} ({VIDEO_NAMES.get(v, '')}): {n} tệp")
    (W / "00-Library-INDEX.md").write_text(chr(10).join(idx) + chr(10), encoding="utf-8")
    for pool, rs in pools.items():
        L = [f"# {pool}", "", f"{len(rs)} tệp · cập nhật từ `catalog.csv` (không sửa tay).", ""]
        for r in sorted(rs, key=lambda r: r["id"]):
            d = f" · {r['duration']}s" if r["duration"] else ""
            L += [f"### {r['id']} — {r['kind']}{d} · dùng: {r['used_in']}", f"![[_thumbs/{r['id']}.jpg|240]]", r["desc"] or "",
                  f"- nguồn: {r['origin']} · license: {r['license']} · credit: {r['credit']}"
                  + (f" · [trang gốc]({r['source_url']})" if r["source_url"] else ""),
                  ]
            if r["prompt"]:
                L.append(f"- prompt: {r['prompt']}")
            tp = (LIB / r["path"]).as_posix().replace(" ", "%20")
            L += [f"- tệp: [{Path(r['path']).name}](file:///{tp})", ""]
        (W / f"{pool}.md").write_text(chr(10).join(L), encoding="utf-8")
    print(f"wiki: {len(pools)} trang chủ đề + INDEX -> {W}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("index")
    sp.add_parser("stats")
    sp.add_parser("wiki")
    sp.add_parser("consolidate")
    sp.add_parser("ingest")
    f = sp.add_parser("find")
    f.add_argument("words", nargs="*")
    f.add_argument("--kind")
    f.add_argument("--class", dest="cls")
    f.add_argument("--pool")
    f.add_argument("--video")
    f.add_argument("--limit", type=int, default=40)
    a = ap.parse_args()
    {"index": cmd_index, "stats": cmd_stats, "wiki": cmd_wiki, "consolidate": cmd_consolidate, "ingest": lambda: (cmd_index(), cmd_consolidate(), cmd_wiki())}.get(a.cmd, lambda: cmd_find(a))()
