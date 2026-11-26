"""Write a NEW CapCut draft for Garden US big-idea-091 from shotlist.csv (CapCut must be CLOSED).
Adapted from garden_build_capcut.py.

Usage:
    python -X utf8 -I tools/garden_build_capcut_091.py [--dry]
"""
import copy
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
VID = r"D:\0002-Team A Nam\scripts\big-idea-091-geranium-cuttings-free-plants"
BS = chr(92)
FOOT = VID + BS + "footage"
V2 = r"D:\0008. Key Quân sự\Video\Video 002\_capcut\ccdraft"
SRC_DRAFT = os.path.join(V2, "backup_V002_auto")
NAME = "G091_auto" if "--name" not in sys.argv else sys.argv[sys.argv.index("--name") + 1]
DRAFT = r"D:\Capcut draft\CapCut Drafts" + "\\" + NAME
ROOT_META = r"C:\Users\admin\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft\root_meta_info.json"
VOICE = VID + BS + "voice" + BS + "voice.mp3"
DRY = "--dry" in sys.argv
US = 1_000_000
T = json.load(open(os.path.join(V2, "templates.json"), encoding="utf-8"))
T["audio_refs"] = {k: v for k, v in T["audio_refs"].items() if k not in ("realtime_denoises", "vocal_separations", "audio_fades")}


def uid():
    return str(uuid.uuid4()).upper()


def us(sec):
    return int(round(sec * US))


def probe(p):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height,codec_type", "-show_entries", "format=duration",
                                   "-of", "json", p], capture_output=True, text=True).stdout)
    st = next((s for s in j.get("streams", []) if s.get("codec_type") == "video"), None)
    if st:
        w, h = int(st["width"]), int(st["height"])
    else:
        w, h = 1920, 1080
    dur = float(j.get("format", {}).get("duration", 0.0))
    return w, h, dur


shots = list(csv.DictReader(open(os.path.join(FOOT, "shotlist.csv"), encoding="utf-8-sig")))

LIBDIR = r"D:\0002-Team A Nam\_LIBRARY"


def lib_find(name):
    """Tìm tệp theo tên gốc trong _LIBRARY hoặc inbox."""
    import glob
    for pat in (LIBDIR + BS + "**" + BS + "*__" + name, LIBDIR + BS + "**" + BS + name):
        g = glob.glob(pat, recursive=True)
        if g:
            return g[0]
    return None


def asset_path(sh):
    t, a = sh["type"], sh["asset"]
    # Check if a is directly found in local folders
    if t == "V":
        p1 = os.path.join(FOOT, "pexels", a)
        if os.path.exists(p1):
            return p1, "video"
        p2 = lib_find(a)
        if p2 and os.path.exists(p2):
            return p2, "video"
        return p1, "video"
    elif t == "A":
        p = os.path.join(FOOT, "ai", a)
        return p, "photo"
    elif t == "G":
        p = os.path.join(FOOT, "gfx", a)
        if os.path.exists(p):
            return p, "photo"
        p2 = lib_find(a)
        if p2:
            return p2, "photo"
        return p, "photo"
    elif t == "P":
        p = os.path.join(FOOT, "photos", a)
        if os.path.exists(p):
            return p, "photo"
        p2 = lib_find(a)
        if p2:
            return p2, "photo"
        return p, "photo"
    raise SystemExit("unknown type " + t)


missing = []
for sh in shots:
    p, mt = asset_path(sh)
    sh["_path"], sh["_mtype"] = p, mt
    if not os.path.exists(p):
        missing.append((sh["id"], p))
if missing:
    for m in missing[:15]:
        print("MISSING", *m)
    raise SystemExit(f"{len(missing)} files missing")

print(f"All {len(shots)} assets verified!")

d = copy.deepcopy(json.load(open(os.path.join(SRC_DRAFT, "draft_content.json"), encoding="utf-8")))
M = d["materials"]
for k in M:
    if isinstance(M[k], list):
        M[k] = []


def add_mat(listname, obj):
    M.setdefault(listname, []).append(obj)
    return obj["id"]


def clone_refs(refs_by_list):
    ids = []
    for ln, m in refs_by_list.items():
        c = copy.deepcopy(m)
        c["id"] = uid()
        ids.append(add_mat(ln, c))
    return ids


def kf(prop, pairs):
    return {"id": uid(), "material_id": "", "property_type": prop, "keyframe_list": [
        {"id": uid(), "curveType": "Line", "time_offset": t, "left_control": {"x": 0.0, "y": 0.0}, "right_control": {"x": 0.0, "y": 0.0},
         "values": [v], "string_value": "", "graphID": ""} for t, v in pairs]}


def video_material(path, mtype, w, h, dur):
    mat = copy.deepcopy(T["video_material"])
    mat.update({"id": uid(), "type": mtype, "path": path.replace("\\", "/"), "material_name": os.path.basename(path), "width": w, "height": h,
                "duration": 10800000000 if mtype == "photo" else us(dur), "has_audio": False, "category_name": "local"})
    add_mat("videos", mat)
    return mat


def video_segment(mat, st, en, scale, tx, ty, kfs, src_start=0):
    refs = clone_refs(T["video_refs"])
    seg = copy.deepcopy(T["video_segment"])
    seg_dur = us(en) - us(st)
    seg.update({"id": uid(), "material_id": mat["id"], "extra_material_refs": refs, "volume": 0.0,
                "source_timerange": {"start": src_start, "duration": seg_dur},
                "target_timerange": {"start": us(st), "duration": seg_dur}, "render_timerange": {"start": 0, "duration": 0},
                "keyframe_refs": [], "render_index": 0, "track_render_index": 0})
    seg["clip"] = {"scale": {"x": scale, "y": scale}, "rotation": 0.0, "transform": {"x": tx, "y": ty},
                   "flip": {"vertical": False, "horizontal": False}, "alpha": 1.0}
    seg["common_keyframes"] = kfs
    return seg


CAM = {"zoom_in": (1.00, 1.08, (0, 0), (0, 0)), "zoom_out": (1.08, 1.00, (0, 0), (0, 0)),
       "pan_left": (1.06, 1.06, (0.02, -0.02), (0, 0)), "pan_right": (1.06, 1.06, (-0.02, 0.02), (0, 0)),
       "push_diag": (1.04, 1.08, (0.015, -0.015), (0.01, -0.01))}

main_track = {**T["video_track"], "id": uid(), "segments": []}
meta_media, report = [], []
for sh in shots:
    sid, st, en = sh["id"], float(sh["start"]), float(sh["end"])
    path, mtype = sh["_path"], sh["_mtype"]
    w, h, dur = probe(path)
    seg_dur = us(en) - us(st)
    mat = video_material(path, mtype, w, h, dur)
    ar = w / h if h else 16 / 9
    base = 1.0 if abs(ar - 16 / 9) < 0.03 else max(ar / (16 / 9), (16 / 9) / ar)
    src_start = 0
    if sh["type"] == "G":
        kfs, z0, px0, py0 = [], 1.0, 0.0, 0.0
    else:
        z0, z1, (px0, px1), (py0, py1) = CAM.get(sh["motion"], CAM["zoom_in"])
        if mtype == "video":
            z0, z1, px0, px1, py0, py1 = 1.0, 1.03, 0.0, 0.0, 0.0, 0.0
            src_start = us(max(0.0, min(float(sh["in_s"] or 0), dur - (en - st) - 0.05)))
        kfs = [kf("KFTypeScaleX", [(0, base * z0), (seg_dur, base * z1)]), kf("KFTypeScaleY", [(0, base * z0), (seg_dur, base * z1)])]
        if px0 != px1:
            kfs.append(kf("KFTypePositionX", [(0, px0), (seg_dur, px1)]))
        if py0 != py1:
            kfs.append(kf("KFTypePositionY", [(0, py0), (seg_dur, py1)]))
    main_track["segments"].append(video_segment(mat, st, en, base * z0, px0, py0, kfs, src_start))
    meta_media.append((path, mtype, w, h, dur))
    report.append((sid, f"{st:.2f}", f"{en:.2f}", sh["type"], os.path.basename(path), sh["overlay_kind"], sh["overlay_text"]))

tracks = [main_track]

# ---------------- voice ----------------
vw, vh, vdur = probe(VOICE)
vmat = copy.deepcopy(T["audio_material"])
vmat.update({"id": uid(), "type": "extract_music", "name": os.path.basename(VOICE), "path": VOICE.replace("\\", "/"),
             "duration": us(vdur), "category_name": "local", "wave_points": []})
add_mat("audios", vmat)
vseg = copy.deepcopy(T["audio_segment"])
vseg.update({"id": uid(), "material_id": vmat["id"], "extra_material_refs": clone_refs(T["audio_refs"]), "volume": 1.0,
             "source_timerange": {"start": 0, "duration": us(vdur)}, "target_timerange": {"start": 0, "duration": us(vdur)},
             "common_keyframes": [], "keyframe_refs": []})
vtrack = {**T["audio_track"], "id": uid(), "name": "VOICE", "is_default_name": False, "segments": [vseg]}
tracks.append(vtrack)
meta_media.append((VOICE, "audio", 0, 0, vdur))

# ---------------- text tracks ----------------
STYLE = {"A": "stamp", "B": "pop", "SRC": "source"}
ROW_OF = {"slam": "A", "stamp": "A", "pop": "B", "source": "SRC"}
TEXT_TRACKS = {r: {**T["text_track"], "id": uid(), "name": f"TEXT {r}", "is_default_name": False, "segments": []} for r in STYLE}

font_title_path = r"C:\Windows\Fonts\impact.ttf"
if not os.path.exists(font_title_path):
    font_title_path = r"C:\Windows\Fonts\arialbd.ttf"
font_title = font_title_path.replace("\\", "/")

def text_material(txt, style_key):
    m = copy.deepcopy(T["text_material"])
    mid = uid()
    color = [1.0, 0.816, 0.251] if style_key == "A" else ([1.0, 1.0, 1.0] if style_key == "B" else [0.95, 0.95, 0.95])
    m.update({"id": mid, "content": json.dumps({"text": txt, "styles": [{"fill": {"alpha": 1.0, "content": {"render_type": "solid", "color": color}},
                                                                           "font": {"id": "", "path": font_title}, "size": 9.0 if style_key=="SRC" else (14.0 if style_key=="B" else 22.0),
                                                                           "range": [0, len(txt)]}]})})
    add_mat("texts", m)
    return m

def text_segment(mat, st, en, tx, ty):
    seg = copy.deepcopy(T["text_segment"])
    seg_dur = us(en) - us(st)
    seg.update({"id": uid(), "material_id": mat["id"], "extra_material_refs": clone_refs(T["text_refs"]),
                "source_timerange": {"start": 0, "duration": seg_dur}, "target_timerange": {"start": us(st), "duration": us(en) - us(st)},
                "render_timerange": {"start": 0, "duration": 0}, "keyframe_refs": []})
    seg["clip"] = {"scale": {"x": 1.0, "y": 1.0}, "rotation": 0.0, "transform": {"x": tx, "y": ty},
                   "flip": {"vertical": False, "horizontal": False}, "alpha": 1.0}
    return seg

n_text = 0
for sh in shots:
    k = sh["overlay_kind"]
    txt = sh["overlay_text"]
    if not txt or k not in ROW_OF:
        continue
    row = ROW_OF[k]
    t0 = float(sh["start"]) + (0.10 if row == "A" else 0.05)
    t1 = float(sh["end"])
    tm = text_material(txt, row)
    ty = -0.72 if row == "A" else (-0.84 if row == "B" else 0.82)
    tx = 0.0 if row != "SRC" else -0.45
    tseg = text_segment(tm, t0, t1, tx, ty)
    TEXT_TRACKS[row]["segments"].append(tseg)
    n_text += 1

for r in ["SRC", "B", "A"]:
    if TEXT_TRACKS[r]["segments"]:
        tracks.append(TEXT_TRACKS[r])

# ---------------- SFX ----------------
SFX_FILES = {"woosh": LIBDIR + r"\sfx\woosh.mp3", "swing": LIBDIR + r"\sfx\swing.mp3"}
SFX_PLAN = {"slam": ("woosh", 0.55, -0.05), "stamp": ("woosh", 0.55, -0.05), "source": ("swing", 0.35, 0.0), "pop": ("swing", 0.2, 0.0)}
sfx_segs = []
if all(os.path.exists(p) for p in SFX_FILES.values()):
    sfx_mats = {}
    for k_, p_ in SFX_FILES.items():
        _, _, sd = probe(p_)
        m_ = copy.deepcopy(T["audio_material"])
        m_.update({"id": uid(), "type": "extract_music", "name": os.path.basename(p_), "path": p_.replace("\\", "/"), "duration": us(sd),
                   "category_name": "local", "wave_points": []})
        add_mat("audios", m_)
        sfx_mats[k_] = (m_, sd)
    ev_ = []
    for sh in shots:
        k = sh["overlay_kind"]
        if k in SFX_PLAN and sh["overlay_text"]:
            ev_.append((float(sh["start"]), k))
    for t0, k in sorted(ev_):
        key, vol, off = SFX_PLAN[k]
        m_, sd = sfx_mats[key]
        seg = copy.deepcopy(T["audio_segment"])
        seg.update({"id": uid(), "material_id": m_["id"], "extra_material_refs": clone_refs(T["audio_refs"]), "volume": vol,
                    "source_timerange": {"start": 0, "duration": us(sd)}, "target_timerange": {"start": us(max(t0 + off, 0)), "duration": us(sd)},
                    "common_keyframes": [], "keyframe_refs": []})
        sfx_segs.append(seg)
    sfx_segs.sort(key=lambda g: g["target_timerange"]["start"])
    lanes = []
    for g in sfx_segs:
        st_ = g["target_timerange"]["start"]
        for ln_ in lanes:
            last = ln_[-1]["target_timerange"]
            if last["start"] + last["duration"] <= st_:
                ln_.append(g)
                break
        else:
            lanes.append([g])
    for n_, ln_ in enumerate(lanes):
        tracks.append({**T["audio_track"], "id": uid(), "name": "SFX TEXT" + (f" {n_ + 1}" if n_ else ""), "is_default_name": False, "segments": ln_})
    print(f"SFX placed: {len(sfx_segs)} events in {len(lanes)} track(s)")

# ---------------- sticker (Music Equalizer) ----------------
STK = os.path.join(os.path.dirname(HERE), "templates", "capcut_sticker_equalizer.json")
total = float(shots[-1]["end"])
if os.path.exists(STK):
    sj = json.load(open(STK, encoding="utf-8"))
    sm = copy.deepcopy(sj["material"])
    sm["id"] = uid()
    add_mat("stickers", sm)
    st_track = copy.deepcopy(sj["track"])
    st_track["id"] = uid()
    for g in st_track["segments"]:
        g.update({"id": uid(), "material_id": sm["id"]})
        g["target_timerange"] = {"start": 0, "duration": us(total)}
    tracks.append(st_track)
    print("Sticker: Equalizer tone overlay active")

d["tracks"] = tracks
d["duration"] = us(total)
d["name"] = NAME
d["update_time"] = 0

print(f"Total duration: {total:.2f}s | Voice: {vdur:.2f}s | Shots: {len(shots)} | Text events: {n_text}")

with open(os.path.join(FOOT, "build_report.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w_ = csv.writer(f)
    w_.writerow(["shot", "start", "end", "type", "file", "overlay_kind", "overlay_text"])
    w_.writerows(report)

if DRY:
    print("Dry run completed: verified successfully.")
    sys.exit(0)

# Write draft
if os.path.exists(DRAFT):
    print(f"Removing previous draft {DRAFT}...")
    shutil.rmtree(DRAFT)

shutil.copytree(SRC_DRAFT, DRAFT)
tl_dir = os.path.join(DRAFT, "Timelines")
tl = [x for x in os.listdir(tl_dir) if os.path.isdir(os.path.join(tl_dir, x))][0]
for p in (os.path.join(DRAFT, "draft_content.json"), os.path.join(tl_dir, tl, "draft_content.json")):
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

new_id = str(uuid.uuid4()).upper()
mp = os.path.join(DRAFT, "draft_meta_info.json")
meta = json.load(open(mp, encoding="utf-8"))
vals, seen = [], set()
for path, mtype, w, h, dur in meta_media:
    key = path.lower()
    if key in seen:
        continue
    seen.add(key)
    vals.append({"ai_group_type": "", "create_time": 0, "duration": us(dur) if mtype != "photo" else 5000000, "enter_from": 0,
                 "extra_info": os.path.basename(path), "file_Path": path.replace("\\", "/"), "height": h, "id": str(uuid.uuid4()),
                 "import_time": 0, "import_time_ms": 0, "item_source": 1, "material_color_tag": "", "md5": "", "metetype": mtype,
                 "roughcut_time_range": {"duration": us(dur) if mtype != "photo" else 5000000, "start": 0},
                 "sub_time_range": {"duration": -1, "start": -1}, "type": 0, "width": w})
for e in meta.get("draft_materials", []):
    if e.get("type") == 0:
        e["value"] = vals
meta["tm_duration"] = us(total)
meta["draft_id"] = new_id
meta["draft_name"] = NAME
meta["draft_fold_path"] = DRAFT.replace("\\", "/")
json.dump(meta, open(mp, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

rm = json.load(open(ROOT_META, encoding="utf-8"))
shutil.copy2(ROOT_META, ROOT_META + ".bak_g091")
store = rm["all_draft_store"]
store[:] = [e for e in store if e.get("draft_name") != NAME]
src_entry = next(e for e in store if e.get("draft_name") == "V002_auto")
e = copy.deepcopy(src_entry)
e.update({"draft_id": new_id, "draft_name": NAME, "draft_fold_path": DRAFT.replace("\\", "/"),
          "draft_json_file": DRAFT.replace("\\", "/") + "\\draft_content.json", "draft_cover": DRAFT.replace("\\", "/") + "\\draft_cover.jpg",
          "tm_duration": us(total)})
store.insert(0, e)
json.dump(rm, open(ROOT_META, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

print(f"\nSUCCESSFULLY WROTE CAPCUT DRAFT: {DRAFT}")
