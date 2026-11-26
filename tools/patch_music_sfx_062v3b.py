"""Vá G062v3b_auto (CapCut phải ĐÓNG; sao lưu trước): nhạc dạo đầu 0:00-1:00 + đổi SFX chữ phụ/thẻ đếm sang mẫu người dùng mới thêm.
 - nhạc: 'Warm Morning Acoustic' (63,4s), âm lượng 0,09, fade vào 0,5s / ra 3s, cắt đúng 60s;
 - chữ phụ B -> 'Soft touch sound' (0,3), thẻ đếm -> 'Soft and clear button sound' (0,35); chữ lớn A giữ Woosh; nhãn nguồn giữ 'swing';
 - gỡ các đoạn mẫu người dùng kéo xuống cuối timeline (vật liệu giữ lại).
Chạy: python -X utf8 -I tools/patch_music_sfx_062v3b.py [--dry]"""
import copy
import json
import os
import shutil
import sys
import uuid

DRY = "--dry" in sys.argv
D = r"D:\Capcut draft\CapCut Drafts\G062v3b_auto"
BAK = D + "_bak_before_music"
TPL = r"D:\0008. Key Quân sự\Video\Video 002\_capcut\ccdraft\templates.json"
US = 1_000_000
uid = lambda: str(uuid.uuid4()).upper()
us = lambda x: int(round(x * US))

if os.path.exists(os.path.join(D, ".locked")):
    raise SystemExit("CapCut đang mở (.locked)")
tl = [x for x in os.listdir(os.path.join(D, "Timelines")) if os.path.isdir(os.path.join(D, "Timelines", x))][0]
files = [os.path.join(D, "draft_content.json"), os.path.join(D, "Timelines", tl, "draft_content.json")]
T = json.load(open(TPL, encoding="utf-8"))


def patch(d):
    mats = {}
    for ln, arr in d["materials"].items():
        if isinstance(arr, list):
            for m in arr:
                if isinstance(m, dict) and "id" in m:
                    mats[m["id"]] = (ln, m)
    aud = {m["id"]: m for m in d["materials"]["audios"]}
    tracks = d["tracks"]
    tails, base = [], {}
    for t in list(tracks):
        if t["type"] == "audio" and not t.get("name") and t["segments"] and min(s["target_timerange"]["start"] for s in t["segments"]) / US > 1000:
            for s in t["segments"]:
                base[aud[s["material_id"]]["name"]] = s
            tails.append(t)
    need = {"music": "Warm Morning Acoustic", "touch": "Soft touch sound", "button": "Soft and clear button sound"}
    ref = {}
    for k, n in need.items():
        seg = next((s for nm, s in base.items() if nm.startswith(n)), None)
        if seg is None:
            raise SystemExit("không thấy mẫu: " + n)
        ref[k] = seg

    def clone(seg, st, dur, vol, fade=None):
        c = copy.deepcopy(seg)
        refs = []
        for rid in seg.get("extra_material_refs", []):
            ln, m = mats[rid]
            m2 = copy.deepcopy(m)
            m2["id"] = uid()
            d["materials"][ln].append(m2)
            refs.append(m2["id"])
        if fade:
            f = copy.deepcopy(T["audio_refs"]["audio_fades"])
            f["id"] = uid()
            f["fade_in_duration"] = us(fade[0])
            f["fade_out_duration"] = us(fade[1])
            d["materials"].setdefault("audio_fades", []).append(f)
            refs.append(f["id"])
        c.update({"id": uid(), "extra_material_refs": refs, "volume": vol,
                  "source_timerange": {"start": 0, "duration": us(dur)}, "target_timerange": {"start": us(st), "duration": us(dur)},
                  "common_keyframes": [], "keyframe_refs": []})
        return c

    text_starts = {}
    for t in tracks:
        if t["type"] == "text" and t.get("name") in ("TEXT A", "TEXT B", "TEXT SRC"):
            text_starts[t["name"]] = [s["target_timerange"]["start"] / US for s in t["segments"]]
    vids = [t for t in tracks if t["type"] == "video"]
    counters = [s["target_timerange"]["start"] / US for s in vids[1]["segments"]] if len(vids) > 1 else []
    near = lambda x, arr: any(abs(x - a - 0.1) < 0.2 or abs(x - a) < 0.2 for a in arr)

    sfx = next(t for t in tracks if t.get("name") == "SFX TEXT")
    stats = {"touch": 0, "button": 0, "kept": 0}
    new = []
    for s in sfx["segments"]:
        st = s["target_timerange"]["start"] / US
        nm = aud[s["material_id"]]["name"]
        if nm.startswith("swing") and near(st, text_starts.get("TEXT B", [])) and not near(st, text_starts.get("TEXT SRC", [])):
            c = clone(ref["touch"], st, 0.6, 0.3)
            c["material_id"] = ref["touch"]["material_id"]
            new.append(c)
            stats["touch"] += 1
        elif nm.startswith("woosh") and near(st + 0.05, counters) and not near(st, text_starts.get("TEXT A", [])):
            c = clone(ref["button"], st, 1.0, 0.35)
            new.append(c)
            stats["button"] += 1
        else:
            new.append(s)
            stats["kept"] += 1
    sfx["segments"] = sorted(new, key=lambda g: g["target_timerange"]["start"])
    # không chồng nhau trong cùng track
    segs, over, end = [], [], -1
    for g in sfx["segments"]:
        st_ = g["target_timerange"]["start"]
        if st_ >= end:
            segs.append(g)
            end = st_ + g["target_timerange"]["duration"]
        else:
            over.append(g)
    sfx["segments"] = segs
    if over:
        t2 = copy.deepcopy(sfx)
        t2["id"] = uid()
        t2["name"] = "SFX TEXT 2"
        t2["segments"] = over
        tracks.append(t2)
    mus = clone(ref["music"], 0.0, 60.0, 0.09, fade=(0.5, 3.0))
    mt = copy.deepcopy(tails[0])
    mt["id"] = uid()
    mt["name"] = "MUSIC"
    mt["segments"] = [mus]
    for t in tails:
        tracks.remove(t)
    tracks.append(mt)
    end = max(s["target_timerange"]["start"] + s["target_timerange"]["duration"] for t in tracks if t["type"] in ("video", "audio", "text") for s in t["segments"])
    d["duration"] = end
    return stats, end, len(over)


docs = [json.load(open(f, encoding="utf-8")) for f in files]
res = [patch(d) for d in docs]
print("SFX:", res[0][0], "| tách track phụ:", res[0][2], "| nhạc 0:00-1:00 | độ dài %.2fs" % (res[0][1] / US))
if DRY:
    print("dry run: chưa ghi")
    sys.exit(0)
if os.path.exists(BAK):
    raise SystemExit("đã có sao lưu " + BAK)
shutil.copytree(D, BAK)
for f, d in zip(files, docs):
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
mp = os.path.join(D, "draft_meta_info.json")
meta = json.load(open(mp, encoding="utf-8"))
meta["tm_duration"] = res[0][1]
json.dump(meta, open(mp, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("ĐÃ VÁ", D, "| sao lưu:", BAK)
