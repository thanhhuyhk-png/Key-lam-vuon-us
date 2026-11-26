"""Chia shot theo SRT thật và ghép video Garden US từ video-map.json, không cần CapCut.

Usage:
    python tools/garden_cut.py plan   scripts/<video>/video-map.json --ai-dir <thư mục clip AI>
    python tools/garden_cut.py render scripts/<video>/video-map.json --from 0 --to 60      -> build/preview.mp4
    python tools/garden_cut.py render scripts/<video>/video-map.json                       -> build/final.mp4

plan: khớp câu mở với voice.srt, chia shot theo hợp đồng nhịp, gán clip của chính cảnh trước, ghi footage/shotlist.csv.
Hết clip của cảnh thì mượn theo nhóm chủ đề; cột fallback: 0 đúng cảnh · 1 cùng chủ đề · 2 chủ đề gần · 3 chưa có hình.
Hợp đồng: 0–1′ shot ≤3,0s (TB ≤2,2) · 1–3′ ≤4,0s (TB ≤3,0) · sau 3′ ≤4,0s (TB ≤3,5); một file ≤3 lần, không lặp trong 60s.
Chữ: Impact vàng (từ khóa), thẻ nguồn nền tối ở trên giữa, mỗi chữ có woosh. Giọng chuẩn -14 LUFS. Nhạc nền trộn sau bằng tools/garden_music.py.
"""
import argparse
import csv
import difflib
import json
import pathlib
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import garden_cards

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent.parent
W, H, FPS = 1920, 1080, 30
FONT = "C:/Windows/Fonts/"
YEL, WHITE = (255, 194, 26), (247, 245, 239)
# Nhóm chủ đề: hết clip của cảnh thì mượn clip cùng nhóm để hình vẫn đúng nghĩa; nhóm "pots" và "pepper" là lớp cuối.
TOPICS = {"pepper": "01 02 13 15 25 27 43 55 57 92 94 96 98 20 22", "frost": "03 83 84 87 60 40 06", "door": "07 36 54 67 73 04",
          "pest": "08 71 75 74 82 79 78 76 80", "roots": "09 23 68 69 70 34 81 11", "pots": "21 35 42 05 10 66 95 24 25 29 85 30 12",
          "prune": "33 37 44 45 48 53 65 47 46", "rest": "26 39 41 49 31 38", "light": "28 56 59 72 16 58 61 17",
          "water": "50 51", "seedling": "18 19 86 52 90 91", "flower": "62 64 63 97"}
TOPIC_OF = {sid: k for k, v in TOPICS.items() for sid in v.split()}
FALLBACK_ORDER = {"rest": ["light", "pots"], "water": ["pots", "rest"], "flower": ["pepper", "light"], "door": ["pots", "rest"], "frost": ["light", "pepper"]}
GCARD_MAX = 7.0
WOOSH = ROOT / "_LIBRARY" / "sfx" / "woosh.mp3"


def norm(s):
    return re.findall(r"[a-z0-9']+", s.lower().replace("’", "'"))


def ts(x):
    h, m, r = x.split(":")
    s, ms = r.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(path):
    cues = []
    for b in re.split(r"\n\s*\n", pathlib.Path(path).read_text(encoding="utf-8-sig").strip()):
        ls = b.splitlines()
        i = next((k for k, l in enumerate(ls) if "-->" in l), None)
        if i is None:
            continue
        a, e = [ts(x.strip()) for x in ls[i].split("-->")]
        cues.append((a, e, " ".join(ls[i + 1:])))
    return cues


def word_times(cues):
    out = []
    for a, e, t in cues:
        ws = norm(t)
        for k, w in enumerate(ws):
            out.append((w, a + (e - a) * k / max(len(ws), 1)))
    return out


def probe(f):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout.strip()
    return float(o or 0)


def limits(t):
    return (2.2, 3.0) if t < 60 else (3.0, 4.0) if t < 180 else (3.5, 4.0)


def scene_times(m, tts, cues):
    wt = word_times(cues)
    src, dst = norm(tts), [w for w, _ in wt]
    mapping = {}
    for tag, a, b, c, d in difflib.SequenceMatcher(None, src, dst, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(b - a):
                mapping[a + k] = c + k
    low = tts
    for s in m["scenes"]:
        i = low.find(s["a"])
        idx = len(norm(low[:i]))
        while idx not in mapping and idx < len(src):
            idx += 1
        s["start"] = wt[mapping[idx]][1] if idx in mapping else None
    end = cues[-1][1]
    for a, b in zip(m["scenes"], m["scenes"][1:] + [None]):
        a["end"] = b["start"] if b else end
    m["scenes"][0]["start"] = 0.0


def cmd_plan(a):
    p = pathlib.Path(a.map)
    m = json.loads(p.read_text(encoding="utf-8"))
    tts = (p.parent / m["script"]).read_text(encoding="utf-8").split("## TTS SCRIPT", 1)[1].strip()
    cues = parse_srt(p.parent / "voice" / "voice.srt")
    scene_times(m, tts, cues)
    res = {}
    for r in csv.DictReader(open(p.parent / "footage" / "picks-resolved.csv", encoding="utf-8-sig")):
        res.setdefault(r["scene"], []).append(r["file"])
    ai = pathlib.Path(a.ai_dir)
    durs, uses, last, pos = {}, {}, {}, {}
    pool = {}
    for s in m["scenes"]:
        if s["t"] == "S":
            pool[s["id"]] = res.get(s["id"], [])
        elif s["t"] == "V":
            pool[s["id"]] = [str(ai / (s.get("file") or s["id"] + ".mp4"))]
    src_scene = {s["id"]: s for s in m["scenes"]}
    trim = {}
    for s in m["scenes"]:
        if s.get("trim"):
            trim[str(ai / (s.get("file") or s["id"] + ".mp4"))] = s["trim"]
    # clip_trim trong map: đoạn dùng được của clip stock, theo tên file (bỏ đoạn lộ mặt, lộ logo).
    for fl in {f for v in pool.values() for f in v}:
        if pathlib.Path(fl).name in m.get("clip_trim", {}):
            trim[fl] = m["clip_trim"][pathlib.Path(fl).name]
    by_topic = {k: [f for sid in v.split() for f in pool.get("093-" + sid, [])] for k, v in TOPICS.items()}
    cuts = sorted({c[0] for c in cues})
    shots, missing, need = [], 0, {}

    def take(f, t, d):
        if f not in durs:
            durs[f] = probe(f)
        lo, hi = trim.get(f, (0.0, durs[f]))
        off = pos.get(f, lo + 0.2)
        if off + d > hi:
            off = lo + 0.1
        pos[f] = off + d + 0.3
        uses[f] = uses.get(f, 0) + 1
        last[f] = t
        return round(off, 2)

    def ok(f, t):
        return uses.get(f, 0) < 3 and t - last.get(f, -999) >= 60

    # Clip mượn không được dùng trước cảnh của chính nó dưới 60 giây; clip AI chỉ mượn sau cảnh của nó (tránh lộ hình trước lời đọc).
    home = {}
    for s_ in m["scenes"]:
        for f_ in pool.get(s_["id"], []):
            home.setdefault(f_, (s_["start"], s_["t"]))

    # no_borrow trong map: clip chỉ đúng nghĩa ở cảnh của nó (vd. hoa khác loài, phòng có thùng đồ), không cho mượn sang cảnh khác.
    no_borrow = m.get("no_borrow", [])

    def borrow_ok(f, t):
        st, kind = home[f]
        return ok(f, t) and (t >= st or (kind != "V" and st - t >= 60)) and not any(k in f for k in no_borrow)

    for s in m["scenes"]:
        t = s["start"]
        if s["t"] == "G":
            ge = t + s["hold"] if s.get("hold") else s["end"] if s.get("full") or s["end"] - t <= GCARD_MAX + 2 else t + GCARD_MAX
            shots.append({"scene": s["id"], "start": t, "end": ge, "type": "G", "file": "", "in": 0, "fallback": 0})
            t = ge
        inner = [c for c in cuts if s["start"] + 1.2 < c < s["end"] - 1.0]
        while t < s["end"] - 0.01:
            avg, mx = limits(t)
            cand = [c for c in inner if t + 1.2 <= c <= t + mx and abs(c - t - avg) <= 0.8]
            e = max(cand, key=lambda c: -abs(c - t - avg)) if cand else min(t + avg, s["end"])
            if s["end"] - e < 1.0:
                e = s["end"] if s["end"] - t <= mx else (t + s["end"]) / 2
            own = [f for f in pool.get(s["id"], []) if ok(f, t)]
            fb = 0
            if own:
                f = own[0]
                if f in trim:
                    e = min(e, t + trim[f][1] - trim[f][0] - 0.2)
            else:
                f, fb = "", 3
                tp = s.get("topic") or TOPIC_OF.get(s["id"][-2:], "pots")
                for lvl, k in enumerate([tp] + FALLBACK_ORDER.get(tp, []) + ["pots", "pepper"]):
                    # Clip đã trim chỉ nhận shot ngắn hơn đoạn dùng được, để không chạy lố sang đoạn đã bỏ.
                    nb = sorted([x for x in by_topic[k] if borrow_ok(x, t) and (x not in trim or trim[x][1] - trim[x][0] - 0.2 >= e - t)], key=lambda x: uses.get(x, 0))
                    if nb:
                        f, fb = nb[0], 1 if lvl == 0 else 2
                        break
                need[tp] = need.get(tp, 0) + (0 if f else 1)
                missing += 0 if f else 1
            # Loại shot tính theo file thật đang dùng, không theo loại của cảnh, để tỉ lệ stock/AI đúng hợp đồng.
            kind = "V" if f.startswith(str(ai)) else "S"
            shots.append({"scene": s["id"], "start": round(t, 2), "end": round(e, 2), "type": kind, "file": f, "in": take(f, t, e - t) if f else 0, "fallback": fb})
            t = e
    with open(p.parent / "footage" / "shotlist.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["scene", "start", "end", "type", "file", "in", "fallback"])
        w.writeheader()
        w.writerows(shots)
    json.dump({s["id"]: {"start": s["start"], "end": s["end"], "text": s.get("text", ""), "t": s["t"], "show": s["show"], "card": s.get("card")} for s in m["scenes"]},
              open(p.parent / "footage" / "scenes-timed.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    total = cues[-1][1]
    secs = {k: sum(x["end"] - x["start"] for x in shots if x["type"] == k) for k in "SVG"}
    print(f"{len(shots)} shot · {total:.0f}s · stock {secs['S'] / total:.0%} · AI {secs['V'] / total:.0%} · đồ họa {secs['G'] / total:.0%}")
    for lo, hi in ((0, 60), (60, 180), (180, total)):
        d = [x["end"] - x["start"] for x in shots if lo <= x["start"] < hi and x["type"] != "G"]
        print(f"  {lo}-{hi:.0f}s: {len(d)} shot, TB {sum(d) / max(len(d), 1):.2f}s, dài nhất {max(d, default=0):.2f}s")
    print(f"  file dùng: {len(uses)}/{len({f for v in pool.values() for f in v})} · đúng cảnh {sum(x['fallback'] == 0 and x['type'] != 'G' for x in shots)} · cùng chủ đề {sum(x['fallback'] == 1 for x in shots)} · chủ đề gần {sum(x['fallback'] == 2 for x in shots)} · chưa có hình {missing} {need}")
    print("  đồ họa dài nhất: " + ", ".join(f"{x['scene']} {x['end'] - x['start']:.0f}s" for x in sorted([x for x in shots if x['type'] == 'G'], key=lambda x: x['start'] - x['end'])[:4]))


def fit(draw, text, font_path, size, maxw):
    while size > 28:
        f = ImageFont.truetype(font_path, size)
        if draw.textlength(text, font=f) <= maxw:
            return f
        size -= 4
    return ImageFont.truetype(font_path, size)


def text_png(text, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if "·" in text and re.search(r"[a-z]", text):
        parts = [x.strip() for x in text.split("·")]
        lines = [parts[0], " · ".join(parts[1:])]
        fs = [ImageFont.truetype(FONT + "arialbd.ttf", 60), ImageFont.truetype(FONT + "arialbd.ttf", 44)]
        bw = max(d.textlength(l, font=f) for l, f in zip(lines, fs)) + 70
        d.rounded_rectangle([(W - bw) / 2, 50, (W + bw) / 2, 220], 14, fill=(14, 14, 12, 224))
        d.text((W / 2, 100), lines[0], font=fs[0], fill=YEL, anchor="mm")
        d.text((W / 2, 175), lines[1], font=fs[1], fill=WHITE, anchor="mm")
    else:
        f = fit(d, text, FONT + "impact.ttf", 112, W - 300)
        d.text((120, 950), text, font=f, fill=YEL, anchor="lb", stroke_width=7, stroke_fill=(0, 0, 0))
    im.save(path)


def card_clip(card, d, out):
    """Dựng thẻ đồ họa thành clip; thẻ nhiều PNG hiện dần theo card.at. Trả các giây có đổi hình (để gắn woosh)."""
    pngs = garden_cards.render(card, str(out.with_suffix("")))
    at = card.get("at") or [i / len(pngs) for i in range(len(pngs))]
    marks = [x * d for x in at]
    durs = [b - a for a, b in zip(marks, marks[1:] + [d])]
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for png, t in zip(pngs, durs):
        cmd += ["-loop", "1", "-framerate", str(FPS), "-t", f"{t:.3f}", "-i", png]
    fc = "".join(f"[{i}:v]" for i in range(len(pngs))) + f"concat=n={len(pngs)}:v=1:a=0,fps={FPS},format=yuv420p[v]"
    run(cmd + ["-filter_complex", fc, "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-t", f"{d:.3f}", str(out)])
    return marks


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    if r.returncode:
        sys.exit("ffmpeg lỗi: " + r.stderr[-600:])


def cmd_render(a):
    p = pathlib.Path(a.map).resolve()
    fdir = p.parent / "footage"
    shots = list(csv.DictReader(open(fdir / "shotlist.csv", encoding="utf-8-sig")))
    scenes = json.load(open(fdir / "scenes-timed.json", encoding="utf-8"))
    total = max(float(s["end"]) for s in shots)
    t0, t1 = a.start, min(a.to if a.to else total, total)
    build = p.parent / "build"
    (build / "parts").mkdir(parents=True, exist_ok=True)
    sel = [s for s in shots if float(s["end"]) > t0 and float(s["start"]) < t1]
    missing = [s["scene"] for s in sel if s["type"] != "G" and not s["file"]]
    if missing:
        sys.exit(f"còn shot chưa có hình: {missing}")
    # crop trong map: [x, y, w, h] theo tỉ lệ khung, áp cho mọi lượt dùng clip đó (cắt chữ, logo lọt vào hình).
    crops = {s.get("file") or s["id"] + ".mp4": s["crop"] for s in json.loads(p.read_text(encoding="utf-8"))["scenes"] if s.get("crop")}
    parts, woosh_at, spans = [], [], []
    for i, s in enumerate(sel):
        st, en = max(float(s["start"]), t0), min(float(s["end"]), t1)
        # Làm tròn theo mốc tuyệt đối để sai số từng shot không cộng dồn thành lệch tiếng.
        frames = round((en - t0) * FPS) - round((st - t0) * FPS)
        d = frames / FPS
        out = build / "parts" / f"{i:04d}.mp4"
        spans.append((round((st - t0) * FPS) / FPS, round((en - t0) * FPS) / FPS))
        if s["type"] == "G":
            marks = card_clip(scenes[s["scene"]]["card"], d, out)
            woosh_at += [st - t0 + x for x in marks]
        else:
            dirx = "(iw-ow)*t/%.3f" % d if i % 2 else "(iw-ow)*(1-t/%.3f)" % d
            cr = crops.get(pathlib.Path(s["file"]).name)
            pre = f"crop=iw*{cr[2]}:ih*{cr[3]}:iw*{cr[0]}:ih*{cr[1]}," if cr else ""
            vf = (f"{pre}scale={int(W * 1.06)}:{int(H * 1.06)}:force_original_aspect_ratio=increase,crop={int(W * 1.06)}:{int(H * 1.06)},"
                  f"tpad=stop_mode=clone:stop_duration=5,crop={W}:{H}:'{dirx}':'(ih-oh)/2',fps={FPS},format=yuv420p")
            run(["ffmpeg", "-y", "-v", "error", "-ss", s["in"], "-i", s["file"], "-frames:v", str(frames), "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-an", str(out)])
        parts.append(out)
    texts = []
    for k, sc in scenes.items():
        if sc["text"] and sc["t"] != "G" and t0 <= sc["start"] < t1:
            png = build / "parts" / f"text_{k}.png"
            text_png(sc["text"], png)
            texts.append((sc["start"] - t0, min(sc["start"] - t0 + max(2.5, min(4.0, sc["end"] - sc["start"])), t1 - t0), png))
    # Chữ đốt thẳng vào từng shot nó đè lên: một lệnh overlay gộp cả video từng làm mất chữ, rồi treo giữa chừng ở bản dài.
    for i, (st, en) in enumerate(spans):
        hit = [x for x in texts if x[0] < en and x[1] > st]
        if not hit:
            continue
        cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(parts[i])]
        fc, cur = [], "[0:v]"
        for k, (a_, b_, png) in enumerate(hit):
            cmd += ["-framerate", str(FPS), "-loop", "1", "-i", str(png)]
            fc.append(f"{cur}[{k + 1}:v]overlay=enable='between(t,{a_ - st:.3f},{b_ - st:.3f})':shortest=1[v{k}]")
            cur = f"[v{k}]"
        out = parts[i].with_name(parts[i].stem + "_t.mp4")
        run(cmd + ["-filter_complex", ";".join(fc) + f";{cur}format=yuv420p[vout]", "-map", "[vout]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-an", str(out)])
        parts[i] = out
    lst = build / "parts" / "list.txt"
    lst.write_text("\n".join(f"file '{x.as_posix()}'" for x in parts), encoding="utf-8")
    woosh_at += [x[0] for x in texts]
    aud = build / "parts" / "audio.m4a"
    cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{t0:.3f}", "-t", f"{t1 - t0:.3f}", "-i", str(p.parent / "voice" / "voice.mp3")]
    for _ in woosh_at:
        cmd += ["-i", str(WOOSH)]
    amix = ["[0:a]loudnorm=I=-14:TP=-1.5:LRA=11[voice]"]
    labels = "[voice]"
    for k, a_ in enumerate(woosh_at):
        ms = int(a_ * 1000)
        amix.append(f"[{1 + k}:a]volume=0.5,adelay={ms}|{ms}[s{k}]")
        labels += f"[s{k}]"
    amix.append(f"{labels}amix=inputs={len(woosh_at) + 1}:duration=first:normalize=0[a]")
    run(cmd + ["-filter_complex", ";".join(amix), "-map", "[a]", "-c:a", "aac", "-b:a", "192k", str(aud)])
    out = build / ("preview.mp4" if a.to or a.start else "final.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(aud), "-map", "0:v", "-map", "1:a", "-c", "copy", "-movflags", "+faststart", str(out)])
    print(f"{len(parts)} shot · {len(texts)} chữ -> {out} ({probe(out):.1f}s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["plan", "render"])
    ap.add_argument("map")
    ap.add_argument("--ai-dir")
    ap.add_argument("--from", dest="start", type=float, default=0.0)
    ap.add_argument("--to", type=float)
    a = ap.parse_args()
    {"plan": cmd_plan, "render": cmd_render}[a.cmd](a)
