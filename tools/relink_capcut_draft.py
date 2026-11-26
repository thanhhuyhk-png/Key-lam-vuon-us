"""Liên kết lại media của một draft CapCut sang _LIBRARY (khi tệp gốc đã dời). CapCut phải ĐÓNG. Sao lưu draft trước.

Usage: python -X utf8 -I tools/relink_capcut_draft.py <tên draft> [--dry]
       vd: python -X utf8 -I tools/relink_capcut_draft.py G062_auto
Tìm theo TÊN TỆP gốc trong _LIBRARY (id__tên). Cập nhật draft_content.json, bản Timelines/*/draft_content.json và draft_meta_info.json.
"""
import glob
import json
import os
import shutil
import sys

BASE = r"D:\Capcut draft\CapCut Drafts"
LIB = r"D:\0002-Team A Nam\_LIBRARY"
BS = chr(92)
name = sys.argv[1]
DRY = "--dry" in sys.argv
D = os.path.join(BASE, name)
B = D + "_bak_before_relink"
cache = {}


def find(p):
    n = os.path.basename(p)
    if n not in cache:
        r = None
        for pat in (LIB + BS + "**" + BS + "*__" + n, LIB + BS + "**" + BS + n):
            g = glob.glob(pat, recursive=True)
            if g:
                r = g[0].replace(BS, "/")
                break
        cache[n] = r
    return cache[n]


tl = [x for x in os.listdir(os.path.join(D, "Timelines")) if os.path.isdir(os.path.join(D, "Timelines", x))][0]
files = [os.path.join(D, "draft_content.json"), os.path.join(D, "Timelines", tl, "draft_content.json")]
if not DRY:
    if os.path.exists(B):
        raise SystemExit("đã có sao lưu " + B)
    shutil.copytree(D, B)
fixed, missing = 0, set()
for f in files:
    d = json.load(open(f, encoding="utf-8"))
    for k in ("videos", "audios"):
        for m in d["materials"][k]:
            if not os.path.exists(m["path"]):
                q = find(m["path"])
                if q:
                    m["path"] = q
                    fixed += 1
                else:
                    missing.add(os.path.basename(m["path"]))
    if not DRY:
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
mf = os.path.join(D, "draft_meta_info.json")
meta = json.load(open(mf, encoding="utf-8"))
mfix = 0
for x in meta.get("draft_materials", []):
    for e in x.get("value", []):
        if not os.path.exists(e["file_Path"]):
            q = find(e["file_Path"])
            if q:
                e["file_Path"] = q
                mfix += 1
if not DRY:
    json.dump(meta, open(mf, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"liên kết lại {fixed} media (2 bản draft) + {mfix} mục meta | không thấy: {sorted(missing)} {'(dry)' if DRY else ''}")
