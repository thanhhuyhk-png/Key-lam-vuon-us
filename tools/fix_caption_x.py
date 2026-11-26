"""Đặt lại vị trí ngang của chữ phụ (TEXT B) trong draft để chữ dài không bị cắt khỏi khung. CapCut phải ĐÓNG; sao lưu trước.

Usage: python -X utf8 -I tools/fix_caption_x.py <tên draft>
Quy tắc: nửa bề rộng chữ ~0.033 mỗi ký tự (size 8.5) -> x = -min(0.55, 0.93 - 0.033*len).
"""
import json
import os
import shutil
import sys

BASE = r"D:\Capcut draft\CapCut Drafts"
name = sys.argv[1]
D = os.path.join(BASE, name)
B = D + "_bak_before_captionx"
if os.path.exists(os.path.join(D, ".locked")):
    raise SystemExit("CapCut đang mở (.locked)")
if os.path.exists(B):
    raise SystemExit("đã có sao lưu " + B)
shutil.copytree(D, B)
tl = [x for x in os.listdir(os.path.join(D, "Timelines")) if os.path.isdir(os.path.join(D, "Timelines", x))][0]
n = 0
for f in (os.path.join(D, "draft_content.json"), os.path.join(D, "Timelines", tl, "draft_content.json")):
    d = json.load(open(f, encoding="utf-8"))
    texts = {m["id"]: m for m in d["materials"]["texts"]}
    for t in d["tracks"]:
        if t.get("name") != "TEXT B":
            continue
        for s in t["segments"]:
            txt = json.loads(texts[s["material_id"]]["content"])["text"]
            s["clip"]["transform"]["x"] = -min(0.55, max(0.0, 0.93 - 0.033 * len(txt)))
            n += 1
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("đã chỉnh", n, "segment chữ phụ (2 bản draft); sao lưu:", B)
