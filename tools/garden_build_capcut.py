"""Write a NEW CapCut draft for Garden US big-idea-062 from shotlist.csv (CapCut must be CLOSED). Adapted from the military channel's build_v004.py.

Usage:
    python -X utf8 -I tools/garden_build_capcut.py [--dry]

Reads: <VID>/footage/shotlist.csv, pexels/ + photos/ + ai/ + gfx/ assets, <VID>/voice/voice.mp3.
Base skeleton and element templates are READ from the military workspace's Video 002 draft (read-only); nothing there is modified.
Writes: D:/Capcut draft/CapCut Drafts/G062_auto (refuses to overwrite) and adds one entry to CapCut's root_meta_info.json
(a .bak_g062 copy is made first). --dry only measures and prints the report.
Text rows: A (slam/stamp: key number), B (pop: short caption), SRC (source lower-third). Counters (1/7..7/7) are PNG overlays.
With --v3: SFX (Woosh/swing from _LIBRARY/sfx) are placed on every text/counter event. No music. Native text stays editable.
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
VID = r"D:\0002-Team A Nam\scripts\big-idea-062-sunny-window-winter-veggies"
V3 = "--v3" in sys.argv   # dựng bản viết lại: footage/v3/shotlist.csv + voice/v3/voice.mp3 + draft G062v3_auto
BS = chr(92)
FOOT = VID + (BS + "footage" + BS + "v3" if V3 else BS + "footage")
V2 = r"D:\0008. Key Quân sự\Video\Video 002\_capcut\ccdraft"
SRC_DRAFT = os.path.join(V2, "backup_V002_auto")
NAME = ("G062v3_auto" if V3 else "G062_auto") if "--name" not in sys.argv else sys.argv[sys.argv.index("--name") + 1]
DRAFT = r"D:\Capcut draft\CapCut Drafts" + "\\" + NAME
ROOT_META = r"C:\Users\admin\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft\root_meta_info.json"
VOICE = VID + (BS + "voice" + BS + "v3" + BS + "voice.mp3" if V3 else BS + "voice" + BS + "voice.mp3")
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
    s = next((x for x in j.get("streams", []) if x["codec_type"] == "video"), {})
    return int(s.get("width", 0) or 0), int(s.get("height", 0) or 0), float(j["format"].get("duration", 0) or 0)


# ---------------- assets ----------------
shots = list(csv.DictReader(open(FOOT + r"\shotlist.csv", encoding="utf-8-sig")))
shots.sort(key=lambda r: float(r["start"]))
total = float(shots[-1]["end"])
ai_use = {}
dis_state = None
table_n = 0


BS = chr(92)
LIBDIR = r"D:\0002-Team A Nam\_LIBRARY"


def lib_find(name):
    """Tìm tệp theo tên gốc (vd pexels-123.mp4) trong _LIBRARY (id__tên) hoặc _inbox; None nếu chưa có."""
    import glob
    for pat in (LIBDIR + BS + "**" + BS + "*__" + name, LIBDIR + BS + "**" + BS + name):
        g = glob.glob(pat, recursive=True)
        if g:
            return g[0]
    return None


def asset_path(sh):
    p, mt = _asset_path(sh)
    if not os.path.exists(p):
        q = lib_find(os.path.basename(p))
        if q:
            return q, mt
    return p, mt


def _asset_path(sh):
    global dis_state, table_n
    t, a = sh["type"], sh["asset"]
    _v = sh["voice_text"].lower()
    if re.search(r"first\. how many hours|how many hours of light", _v):
        dis_state = "HOURS"
    elif re.search(r"second\. how far|how far should the lamp", _v):
        dis_state = "DIST"
    elif re.search(r"third\. should you wash|wash microgreens", _v):
        dis_state = "WASH"
    elif re.search(r"that's the table|now, lamps", _v):
        dis_state = None
    if t == "V":
        return FOOT + rf"\pexels\{a}.mp4", "video"
    if t == "P":
        return FOOT + rf"\photos\{a}.jpg", "photo"
    if t == "A":
        n = ai_use.get(a, 0)
        ai_use[a] = n + 1
        v = FOOT + rf"\ai\{a}-v2.jpg"
        p = FOOT + rf"\ai\{a}.jpg"
        return (v if (n % 2 == 1 and os.path.exists(v)) else p), "photo"
    if t == "G":
        key = a
        if a == "GFX-TABLE":
            if dis_state:
                key = "GFX-DIS-" + dis_state
            else:
                key = ["GFX-TABLE-1", "GFX-TABLE-2", "GFX-TABLE-3"][min(table_n, 2)]
                table_n += 1
        return FOOT + rf"\gfx\{key}.png", "photo"
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


# motion -> (z0, z1, (px0, px1), (py0, py1)) ; photos move more than clips
CAM = {"zoom_in": (1.00, 1.10, (0, 0), (0, 0)), "zoom_out": (1.10, 1.00, (0, 0), (0, 0)),
       "pan_left": (1.08, 1.08, (0.03, -0.03), (0, 0)), "pan_right": (1.08, 1.08, (-0.03, 0.03), (0, 0)),
       "push_diag": (1.04, 1.10, (0.02, -0.02), (0.015, -0.015))}

main_track = {**T["video_track"], "id": uid(), "segments": []}
over_track = {**T["video_track"], "id": uid(), "segments": []}
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
            z0, z1, px0, px1, py0, py1 = 1.0, 1.04, 0.0, 0.0, 0.0, 0.0
            src_start = us(max(0.0, min(float(sh["in_s"] or 0), dur - (en - st) - 0.05)))
        crop = sh.get("crop") or ""
        extra, offx = (1.12, 0.05) if crop == "zoom_L" else ((1.12, -0.05) if crop == "zoom_R" else (1.0, 0.0))
        px0 += offx
        px1 = px1 + offx if mtype != "video" else px0
        kfs = [kf("KFTypeScaleX", [(0, base * extra * z0), (seg_dur, base * extra * z1)]), kf("KFTypeScaleY", [(0, base * extra * z0), (seg_dur, base * extra * z1)])]
        if px0 != px1:
            kfs.append(kf("KFTypePositionX", [(0, px0), (seg_dur, px1)]))
        if py0 != py1:
            kfs.append(kf("KFTypePositionY", [(0, py0), (seg_dur, py1)]))
        base = base * extra
    main_track["segments"].append(video_segment(mat, st, en, base * z0, px0, py0, kfs, src_start))
    meta_media.append((path, mtype, w, h, dur))
    report.append((sid, f"{st:.2f}", f"{en:.2f}", sh["type"], os.path.basename(path), sh["overlay_kind"], sh["overlay_text"]))
    if sh["overlay_kind"] == "count":
        n = sh["overlay_text"].split("/")[0]
        op = (lib_find(f"CHALK-COUNT-{n}.png") if V3 else None) or lib_find(f"COUNT-{n}.png") or FOOT + rf"\gfx\COUNT-{n}.png"
        om = video_material(op, "photo", 1920, 1080, 0)
        over_track["segments"].append(video_segment(om, st, en, 1.0, 0.0, 0.0, []))
        meta_media.append((op, "photo", 1920, 1080, 0))

tracks = [main_track]
if over_track["segments"]:
    tracks.append(over_track)

# ---------------- voice ----------------
vw, vh, vdur = probe(VOICE)
voice_mat = copy.deepcopy(T["audio_material"])
voice_mat.update({"id": uid(), "type": "extract_music", "name": os.path.basename(VOICE), "path": VOICE.replace("\\", "/"), "duration": us(vdur),
                  "category_name": "local", "wave_points": []})
add_mat("audios", voice_mat)
vseg = copy.deepcopy(T["audio_segment"])
vseg.update({"id": uid(), "material_id": voice_mat["id"], "extra_material_refs": clone_refs(T["audio_refs"]), "volume": 1.0,
             "source_timerange": {"start": 0, "duration": us(min(total, vdur))}, "target_timerange": {"start": 0, "duration": us(min(total, vdur))},
             "common_keyframes": [], "keyframe_refs": []})
tracks.append({**T["audio_track"], "id": uid(), "name": "Voice", "is_default_name": False, "segments": [vseg]})

# ---------------- text ----------------
# row -> (font, text color RGB 0-1, size, x, y, bg hex)
STYLE = {"A": ("C:/Windows/Fonts/impact.ttf", [1.0, 0.84, 0.04], 15.0, 0.0, -0.52, "#12372A"),
         "B": ("C:/Windows/Fonts/arialbd.ttf", [1.0, 1.0, 1.0], 8.5, -0.55, -0.80, "#12372A"),
         "SRC": ("C:/Windows/Fonts/arialbd.ttf", [1.0, 1.0, 1.0], 7.5, 0.0, -0.88, "#12372A"),
         "ILL": ("C:/Windows/Fonts/arial.ttf", [1.0, 1.0, 1.0], 6.0, 0.78, -0.92, "#000000")}
ROW_OF = {"slam": "A", "stamp": "A", "pop": "B", "source": "SRC"}
TEXT_TRACKS = {k: {**T["text_track"], "id": uid(), "name": f"TEXT {k}", "is_default_name": False, "segments": []} for k in STYLE}


def add_label(row, text, t0, t1):
    font, color, size, x, y, bg = STYLE[row]
    tm = copy.deepcopy(T["text_material"])
    content = {"text": text, "styles": [{"fill": {"content": {"render_type": "solid", "solid": {"color": color}}},
                                         "font": {"path": font, "id": ""}, "size": size, "range": [0, len(text)]}]}
    tm.update({"id": uid(), "content": json.dumps(content, ensure_ascii=False, separators=(",", ":")), "font_path": font, "font_size": size,
               "text_color": "#%02X%02X%02X" % tuple(int(c * 255) for c in color), "background_color": bg, "background_alpha": 0.92,
               "background_style": 1, "background_round_radius": 0.0, "background_fill": bg, "background_width": 0.14,
               "background_height": 0.12, "alignment": 1, "text_alpha": 1.0, "global_alpha": 1.0})
    add_mat("texts", tm)
    anim = copy.deepcopy(T["text_refs"]["material_animations"])
    anim["id"] = uid()
    for a_ in anim.get("animations", []):
        a_["duration"] = 300000
    add_mat("material_animations", anim)
    seg = copy.deepcopy(T["text_segment"])
    seg.update({"id": uid(), "material_id": tm["id"], "extra_material_refs": [anim["id"]], "source_timerange": None,
                "target_timerange": {"start": us(t0), "duration": us(t1 - t0)}, "render_timerange": {"start": 0, "duration": 0},
                "common_keyframes": [], "keyframe_refs": []})
    if row == "B":   # keep long captions inside the frame: half-width (normalized) ~ 0.033 per character at size 8.5
        x = -min(0.55, max(0.0, 0.93 - 0.033 * len(text)))
    seg["clip"] = {"scale": {"x": 1.0, "y": 1.0}, "rotation": 0.0, "transform": {"x": x, "y": y},
                   "flip": {"vertical": False, "horizontal": False}, "alpha": 1.0}
    TEXT_TRACKS[row]["segments"].append(seg)


n_text = 0
for sh in shots:
    k = sh["overlay_kind"]
    if sh["type"] == "G" or k not in ROW_OF or not sh["overlay_text"]:
        continue
    st, en = float(sh["start"]), float(sh["end"])
    t0 = st + 0.10
    t1 = min(en, t0 + (2.6 if k in ("slam", "stamp", "source") else 2.0))
    if t1 - t0 < 0.5:
        continue
    add_label(ROW_OF[k], sh["overlay_text"], t0, t1)
    n_text += 1
for row in STYLE:
    segs = TEXT_TRACKS[row]["segments"]
    segs.sort(key=lambda g: g["target_timerange"]["start"])
    for g1, g2 in zip(segs, segs[1:]):
        end1 = g1["target_timerange"]["start"] + g1["target_timerange"]["duration"]
        if end1 > g2["target_timerange"]["start"]:
            g1["target_timerange"]["duration"] = max(300000, g2["target_timerange"]["start"] - g1["target_timerange"]["start"])
    if segs:
        tracks.append(TEXT_TRACKS[row])

# ---------------- SFX cho chữ (mẫu của người dùng trong _LIBRARY\sfx) ----------------
SFX_FILES = {"woosh": LIBDIR + r"\sfx\woosh.mp3", "swing": LIBDIR + r"\sfx\swing.mp3"}
SFX_PLAN = {"slam": ("woosh", 0.55, -0.05), "stamp": ("woosh", 0.55, -0.05), "count": ("woosh", 0.5, -0.05),
            "source": ("swing", 0.35, 0.0), "pop": ("swing", 0.2, 0.0)}
sfx_segs = []
if V3 and all(os.path.exists(p) for p in SFX_FILES.values()):
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
        if sh["type"] == "G" and k != "count":
            continue
        if k in SFX_PLAN and sh["overlay_text"]:
            ev_.append((float(sh["start"]) + (0.10 if k in ROW_OF else 0.0), k))
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
    print(f"SFX segments {len(sfx_segs)} in {len(lanes)} track(s)")

# ---------------- sticker (sóng nhạc) user thêm tay trong G062v3b_auto; lưu ở templates/capcut_sticker_equalizer.json ----------------
STK = os.path.join(os.path.dirname(HERE), "templates", "capcut_sticker_equalizer.json")
if V3 and os.path.exists(STK):
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
    print("sticker: Equalize EN Music Tone V4 (cả video)")

d["tracks"] = tracks
d["duration"] = us(total)
d["name"] = NAME
d["update_time"] = 0

nseg = sum(len(t["segments"]) for t in tracks)
by_type = {}
for s in shots:
    by_type[s["type"]] = by_type.get(s["type"], 0) + 1
print(f"shots {len(shots)} {by_type} | text events {n_text} (A/B/SRC: " + "/".join(str(len(TEXT_TRACKS[r]["segments"])) for r in STYLE) +
      f"/ILL) | counter overlays {len(over_track['segments'])} | tracks {len(tracks)} | segments {nseg} | length {total:.2f}s | voice {vdur:.2f}s")
with open(os.path.join(FOOT, "build_report.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w_ = csv.writer(f)
    w_.writerow(["shot", "start", "end", "type", "file", "overlay_kind", "overlay_text"])
    w_.writerows(report)
if DRY:
    print("dry run: nothing written")
    sys.exit(0)

# ---------------- write the new draft (never overwrite) ----------------
if os.path.exists(DRAFT):
    raise SystemExit(f"{DRAFT} already exists - not overwriting. Rename/delete it manually to rebuild.")
if os.path.exists(os.path.join(os.path.dirname(DRAFT), "V002_auto", ".locked")):
    raise SystemExit("CapCut seems to be open (.locked) - close CapCut and rerun")
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
shutil.copy2(ROOT_META, ROOT_META + (".bak_g062v3" if V3 else ".bak_g062"))
store = rm["all_draft_store"]
store[:] = [e for e in store if e.get("draft_name") != NAME]
src_entry = next(e for e in store if e.get("draft_name") == "V002_auto")
e = copy.deepcopy(src_entry)
e.update({"draft_id": new_id, "draft_name": NAME, "draft_fold_path": DRAFT.replace("\\", "/"),
          "draft_json_file": DRAFT.replace("\\", "/") + "\\draft_content.json", "draft_cover": DRAFT.replace("\\", "/") + "\\draft_cover.jpg",
          "tm_duration": us(total)})
store.insert(0, e)
json.dump(rm, open(ROOT_META, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("WROTE", DRAFT)
