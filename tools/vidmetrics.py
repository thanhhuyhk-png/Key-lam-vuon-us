"""vidmetrics.py — do cac chi so hinh/tieng cua MOT video bat ky (video mau cua kenh khac hoac ban dung cua ta).
Dung chung cho tools/look_check.py va tools/ref_bench.py. Can ffmpeg; whisper (faster-whisper) chi khi do loi doc.
"""
import json, re, statistics as st, subprocess

def _ff(args, **kw):
    return subprocess.run(["ffmpeg", "-hide_banner", "-v", "info"] + args, capture_output=True, **kw)

def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout
    return float(out.strip() or 0)

def look(path, fps=1):
    """do sang trung binh / trung vi (0-255), ti le khung toi (< 40), bao hoa — 1 khung moi giay"""
    r = _ff(["-i", path, "-vf", f"fps={fps},scale=320:-2,signalstats,metadata=print:file=-", "-an", "-f", "null", "-"], text=True, encoding="utf-8", errors="ignore")
    y = [float(m) for m in re.findall(r"YAVG=([\d.]+)", r.stdout)]; s = [float(m) for m in re.findall(r"SATAVG=([\d.]+)", r.stdout)]
    if not y: return {}
    return {"mean": round(st.mean(y), 1), "median": round(st.median(y), 1), "dark": round(sum(v < 40 for v in y) / len(y), 3), "sat": round(st.mean(s), 1) if s else 0}

def cuts(path, th=0.15, merge=0.4, fps=10):
    """lan cat canh theo diem doi canh (scene score > th, lay mau 10 khung/giay cho moi video nhu nhau), gop cac lan cat sat nhau"""
    r = _ff(["-i", path, "-vf", f"fps={fps},scale=320:-2,select='gte(scene,0)',metadata=print:file=-", "-an", "-f", "null", "-"], text=True, encoding="utf-8", errors="ignore")
    pts = [(float(a), float(b)) for a, b in re.findall(r"pts_time:([\d.]+)\s+lavfi\.scene_score=([\d.]+)", r.stdout)]
    if not pts: pts = [(float(a), float(b)) for a, b in re.findall(r"pts_time:([\d.]+)[^\n]*\n[^\n]*scene_score=([\d.]+)", r.stdout)]
    out = []
    for t, s_ in pts:
        if s_ > th and (not out or t - out[-1] > merge): out.append(t)
    return out

def loud(path):
    r = _ff(["-i", path, "-af", "ebur128", "-f", "null", "-"], text=True, encoding="utf-8", errors="ignore")
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    return float(m[-1]) if m else None

def novelty(path, fps=1, back=10, thr=14):
    """do MOI: khung (1/giay) duoc tinh la 'lap lai' neu giong mot khung cach > back giay truoc do (anh xam 32x18, sai khac TB < thr).
    looks = so 'kieu hinh' khac nhau (gom nhom tham lam)"""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale=32:18,format=gray", "-f", "rawvideo", "-"], capture_output=True)
    import numpy as np
    n = len(r.stdout) // 576
    F = np.frombuffer(r.stdout[:n * 576], dtype=np.uint8).reshape(n, 576).astype(np.int16)
    rep = 0
    for i in range(back * fps, n):
        rep += bool((np.abs(F[:i - back * fps] - F[i]).mean(axis=1) < thr).any())
    cents = []
    for f in F[::2]:
        if not cents or not (np.abs(np.array(cents) - f).mean(axis=1) < thr).any(): cents.append(f)
    return {"repeat": round(rep / max(1, n), 3), "looks_per_min": round(len(cents) / max(1, n / fps / 60), 1)}

NUMW = r"\d|^(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|percent|half|double)\W*$"
def speech(words, title_at=None, text=None):
    """words: [{'w','t'}] — toc do doc, cau hoi, so lieu, so tu truoc tieu de. text: loi day du co dau cau (neu words da bo dau)"""
    if not words: return {}
    dur = words[-1]["t"] - words[0]["t"]; txt = text or " ".join(w["w"] for w in words)
    out = {"wpm": round(len(words) / max(1, dur) * 60), "q_per_1000": round(txt.count("?") / len(words) * 1000, 1),
           "num_per_min": round(sum(bool(re.search(NUMW, w["w"].lower().strip())) for w in words) / max(1, dur) * 60, 1),
           "you_share": round(sum(re.sub(r"[^a-z]", "", w["w"].lower()) in ("you", "your", "youre", "yourself") for w in words) / len(words), 3)}
    if title_at is not None: out["words_before_title"] = sum(w["t"] < title_at for w in words)
    return out

def whisper_words(path, model="small"):
    from faster_whisper import WhisperModel
    m = WhisperModel(model, device="cpu", compute_type="int8"); segs, _ = m.transcribe(path, language="en", word_timestamps=True)
    return [{"w": w.word.strip(), "t": round(w.start, 2), "e": round(w.end, 2)} for s in segs for w in s.words]

def find_title(words, text):
    """thoi diem cau tieu de duoc doc (khop 4 chu dau cua text)"""
    key = [re.sub(r"[^a-z0-9]", "", x.lower()) for x in text.split()][:4]; ws = [re.sub(r"[^a-z0-9]", "", w["w"].lower()) for w in words]
    for i in range(len(ws) - len(key) + 1):
        if ws[i:i + len(key)] == key: return words[i]["t"]
    return None

def cut_stats(c, dur):
    sh = [b - a for a, b in zip([0] + c, c + [dur])]
    return {"cuts_per_min": round(len(c) / dur * 60, 1), "median_shot": round(st.median(sh), 2), "longest_shot": round(max(sh), 1),
            "cuts_30s": sum(t < 30 for t in c), "cuts_60s": sum(t < 60 for t in c)}
