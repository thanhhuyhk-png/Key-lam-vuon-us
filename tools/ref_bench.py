"""ref_bench.py — do mot video MAU (hoac ban dung cua ta) theo cung bo chi so, ghi vao so DNA cua kenh de so sanh.
  python tools/ref_bench.py --video "<mau.mp4>" --name "Awaken 8B city" --title-text "Could all of humanity" --root "<goc kenh>"
  python tools/ref_bench.py --video "projects/<ten>/out/<video>.mp4" --project projects/<ten> --name "Tap 03" --root "<goc kenh>"
Ket qua: <root>/research/bench/<name>.json + bang so sanh trong <root>/research/bench/BENCH.md (giua 2 dong <!--BENCH-->).
Chi so: cat canh/phut, canh trung vi, do sang, khung toi, bao hoa, LUFS, do lap hinh (repeat), kieu hinh/phut,
        toc do doc, cau hoi/1000 tu, so lieu/phut, so tu truoc tieu de.  Loi doc: --project (words.json) hoac faster-whisper (mac dinh, ~2 phut).
"""
import argparse, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vidmetrics as VM
def read_json(p, d=None):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else d
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")

ap = argparse.ArgumentParser()
ap.add_argument("--video"); ap.add_argument("--table-only", action="store_true", help="chi ve lai bang tu series/bench/*.json"); ap.add_argument("--name", required=True); ap.add_argument("--root", required=True)
ap.add_argument("--project"); ap.add_argument("--title-text"); ap.add_argument("--title-at", type=float); ap.add_argument("--no-speech", action="store_true"); ap.add_argument("--words", help="transcript co san (words.json hoac danh sach doan whisper co truong w)")
a = ap.parse_args()
bdir = os.path.join(a.root, "research", "bench"); os.makedirs(bdir, exist_ok=True)
if not a.table_only:
    dur = VM.duration(a.video); print(f"Do {a.name} ({dur:.0f} s)…")
    m = {"name": a.name, "file": os.path.basename(a.video), "duration": round(dur, 1)}
    m.update(VM.cut_stats(VM.cuts(a.video), dur)); m.update(VM.look(a.video)); m["lufs"] = VM.loud(a.video); m.update(VM.novelty(a.video))
    words, tt = [], a.title_at
    if a.project:
        words = read_json(os.path.join(a.project, "timeline", "words.json"), [])
        story = read_json(os.path.join(a.project, "story", "shots.json"), {})
        if tt is None: tt = next((s["start"] for s in story.get("shots", []) if "TITLE" in (s.get("notes") or "")), None)
    elif a.words:
        raw = json.load(open(a.words, encoding="utf-8"))
        words = [{"w": w[0].strip(), "t": w[1]} for sg in raw for w in sg["w"]] if raw and "w" in raw[0] and isinstance(raw[0]["w"], list) else raw
    elif not a.no_speech:
        try: words = VM.whisper_words(a.video)
        except Exception as e: print("Bo qua loi doc (khong co faster-whisper?):", e)
    if words and tt is None and a.title_text: tt = VM.find_title(words, a.title_text)
    full = " ".join(l.get("text", "") for l in read_json(os.path.join(a.project, "timeline", "lines.json"), [])) if a.project else None
    m.update(VM.speech(words, tt, full)); m["title_at"] = tt
    slug = re.sub(r"[^a-z0-9]+", "-", a.name.lower()).strip("-")
    json.dump(m, open(os.path.join(bdir, slug + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- bang so sanh trong DNA-THANG.md
rows = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(bdir, "*.json")))]
COLS = [("Video", "name", "{}"), ("Dài", "duration", "{:.0f}s"), ("Cắt/phút", "cuts_per_min", "{}"), ("Cảnh TV", "median_shot", "{}s"), ("Sáng", "mean", "{:.0f}"),
        ("Khung tối", "dark", "{:.0%}"), ("Bão hòa", "sat", "{:.0f}"), ("Lặp hình", "repeat", "{:.0%}"), ("Kiểu hình/phút", "looks_per_min", "{}"),
        ("Từ/phút", "wpm", "{}"), ("Hỏi/1000 từ", "q_per_1000", "{}"), ("Số liệu/phút", "num_per_min", "{}"), ("Tiêu đề lúc", "title_at", "{:.0f}s"), ("Từ trước tiêu đề", "words_before_title", "{}"), ("LUFS", "lufs", "{}")]
def cell(r, k, f):
    v = r.get(k)
    try: return "–" if v is None else f.format(v)
    except Exception: return str(v)
tbl = ["| " + " | ".join(c for c, _, _ in COLS) + " |", "|" + "---|" * len(COLS)] + ["| " + " | ".join(cell(r, k, f) for _, k, f in COLS) + " |" for r in rows]
dna = os.path.join(a.root, "research", "bench", "BENCH.md")
txt = open(dna, encoding="utf-8").read() if os.path.exists(dna) else "# DNA THẮNG\n\n## Bảng đo video mẫu\n<!--BENCH-->\n<!--BENCH-->\n"
parts = txt.split("<!--BENCH-->")
if len(parts) >= 3: txt = parts[0] + "<!--BENCH-->\n" + "\n".join(tbl) + "\n<!--BENCH-->" + "<!--BENCH-->".join(parts[2:])
else: txt += "\n<!--BENCH-->\n" + "\n".join(tbl) + "\n<!--BENCH-->\n"
open(dna, "w", encoding="utf-8").write(txt)
print("\n".join(tbl)); print("->", dna)
