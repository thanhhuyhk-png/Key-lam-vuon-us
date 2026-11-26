"""Originality / anti-template check for Garden US scripts (Pha D, lessons-learned L12).

Usage:
    python tools/originality_check.py scripts/big-idea-060-pineapple-top/script.md [--last 5]
    python tools/originality_check.py scripts/remake-003-x/script.md --against seed-transcript.txt [--allow "tastes like apple and honey"]

Compares the TTS SCRIPT section of the given script against the N most recent other
scripts (by folder modification time) and reports:
  - identical sentences (>= 4 words) shared with each script, excluding a short whitelist
    of channel signature lines (allowed like "same intro and outro")
  - 6-word n-gram overlap %
  - shared skeleton cues (hook / step-reveal / closing patterns)
Exit code 1 if any comparison has more than MAX_IDENTICAL identical sentences.

LANE B (2026-10-23): --against compares with the SEED transcript (txt / md / srt; timestamps stripped).
If omitted, a file named seed-transcript*.txt|.md|.srt in the script's folder is picked up automatically.
Stricter limits: > MAX_IDENTICAL_SEED identical sentences or > MAX_SEED_OVERLAP % of OUR 6-grams found
in the seed = FAIL. Shared runs of >= 8 words are listed so they can be rewritten.
--allow removes the locked paid-asset phrase (R2 — must stay verbatim) from both texts before comparing.

ĐỐI THỦ (2026-11-08): --competitor <file|folder> (repeatable) compares with transcripts of other channels'
videos on the SAME topic (the outliers found at Topic Gate). If omitted, every .txt/.md/.srt/.vtt in
`competitor-transcripts/` inside the script's folder is used. All competitor files are pooled:
  FAIL if > MAX_COMP_OVERLAP % of OUR 6-grams appear anywhere in the pool,
  or if any shared word run is >= MAX_COMP_RUN words (copied sentence).
Thresholds are a first guess borrowed from the Vietnamese kit (≤1 %, 0 sentence ≥10 words): calibrate by
running two independent channels on the same topic against each other and note the numbers in BENCH.md.
--no-competitor "<lý do>" silences the 'no competitor transcripts' warning.
"""
import argparse
import os
import re
import sys
from pathlib import Path

MAX_IDENTICAL = 3
MAX_IDENTICAL_SEED = 1
MAX_SEED_OVERLAP = 2.0   # % of our 6-grams; different-topic scripts of the channel sit at ~0.0-0.1%
MIN_RUN = 8              # shared runs of this many words or more are printed
MAX_COMP_OVERLAP = 1.0   # % of our 6-grams found in the pooled competitor transcripts
MAX_COMP_RUN = 10        # a shared run this long = a copied sentence
COMP_EXT = (".txt", ".md", ".srt", ".vtt")

# Short channel signature lines that may repeat (equivalent to a recurring intro/outro).
WHITELIST = {
    "happy gardening.",
    "here's why this works.",
    "here's the thing.",
    "don't panic.",
    "that's it.",
    "tell me in the comments.",
}

SKELETON_CUES = [
    "here's the catch",
    "i'll show you at step",
    "step one.",
    "step five.",
    "that makes you someone",
    "up next on your screen",
    "your neighbors will ask",
    "slow and steady",
    "trust me on this",
]


def tts_text(path: Path) -> str:
    s = path.read_text(encoding="utf-8")
    m = re.search(r"## TTS SCRIPT\s*(.*)", s, re.DOTALL)
    return m.group(1) if m else s


def sentences(t: str):
    out = []
    for x in re.split(r"(?<=[.?!])\s+", t):
        x = " ".join(x.split()).strip()
        if len(x.split()) >= 4 and x.lower() not in WHITELIST:
            out.append(x)
    return out


def grams(t: str, n: int = 6):
    w = re.findall(r"[a-z']+", t.lower())
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def seed_text(path: Path) -> str:
    s = tts_text(path) if path.suffix.lower() == ".md" else path.read_text(encoding="utf-8", errors="replace")
    lines = []
    for ln in s.splitlines():
        if re.fullmatch(r"\s*\d+\s*", ln) or "-->" in ln:   # SRT index / timing lines
            continue
        ln = re.sub(r"\[?\(?\b\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?\b\)?\]?", " ", ln)
        lines.append(ln)
    return " ".join(" ".join(lines).split())


def strip_allowed(t: str, allowed) -> str:
    for phrase in allowed:
        t = re.sub(re.escape(phrase), " ", t, flags=re.IGNORECASE)
    return t


def shared_runs(t: str, o: str, n: int = 6):
    """Longest word runs of our script that also appear in o (built from shared n-grams)."""
    w = re.findall(r"[a-z']+", t.lower())
    og = grams(o, n)
    hit = [tuple(w[i:i + n]) in og for i in range(len(w) - n + 1)]
    runs, i = [], 0
    while i < len(hit):
        if hit[i]:
            j = i
            while j + 1 < len(hit) and hit[j + 1]:
                j += 1
            runs.append(" ".join(w[i:j + n]))
            i = j + 1
        else:
            i += 1
    return sorted((r for r in runs if len(r.split()) >= MIN_RUN), key=lambda r: -len(r.split()))


def check_seed(t: str, seed_path: Path, allowed) -> bool:
    o = strip_allowed(seed_text(seed_path), allowed)
    t = strip_allowed(t, allowed)
    os_ = {s.lower() for s in sentences(o)}
    same = [s for s in sentences(t) if s.lower() in os_]
    tg, og = grams(t), grams(o)
    overlap = 100 * len(tg & og) / max(1, len(tg))
    ok = len(same) <= MAX_IDENTICAL_SEED and overlap <= MAX_SEED_OVERLAP
    print(f"[{'ok' if ok else 'FAIL'}] vs SEED {seed_path.name} ({len(o.split())} words): "
          f"identical sentences {len(same)} (limit {MAX_IDENTICAL_SEED}) · "
          f"6-gram overlap {overlap:.1f}% of ours (limit {MAX_SEED_OVERLAP}%)")
    for x in same:
        print(f"      = {x}")
    runs = shared_runs(t, o)
    for r in runs[:15]:
        print(f"      ~ [{len(r.split())}w] {r}")
    if len(runs) > 15:
        print(f"      … {len(runs) - 15} more shared runs >= {MIN_RUN} words")
    return ok


def competitor_files(args, folder: Path):
    paths = []
    for p in (args or [str(folder / "competitor-transcripts")]):
        p = Path(p).resolve()
        if p.is_dir():
            paths += sorted(x for x in p.rglob("*") if x.suffix.lower() in COMP_EXT)
        elif p.exists():
            paths.append(p)
        elif args:
            print(f"[FAIL] competitor path not found: {p}")
            return None
    return paths


def check_competitors(t: str, files, allowed) -> bool:
    t = strip_allowed(t, allowed)
    tg = grams(t)
    pool, ok = [], True
    for f in files:
        o = strip_allowed(seed_text(f), allowed)
        pool.append(o)
        ov = 100 * len(tg & grams(o)) / max(1, len(tg))
        print(f"      {f.name}: {len(o.split())} words · {ov:.2f}% of our 6-grams")
    allo = " ".join(pool)
    overlap = 100 * len(tg & grams(allo)) / max(1, len(tg))
    runs = []
    for o in pool:
        runs += [r for r in shared_runs(t, o) if len(r.split()) >= MAX_COMP_RUN]
    runs = sorted(set(runs), key=lambda r: -len(r.split()))
    ok = overlap <= MAX_COMP_OVERLAP and not runs
    print(f"[{'ok' if ok else 'FAIL'}] vs {len(files)} competitor transcript(s): 6-gram overlap {overlap:.2f}% of ours "
          f"(limit {MAX_COMP_OVERLAP}%) · copied runs >= {MAX_COMP_RUN} words: {len(runs)} (limit 0)")
    for r in runs[:15]:
        print(f"      ~ [{len(r.split())}w] {r}")
    if not ok:
        print("      → rewrite these in the channel's own words; if a run is an official name/quote, pass --allow \"<phrase>\"")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--last", type=int, default=5)
    ap.add_argument("--against", action="append", default=[],
                    help="seed transcript (txt/md/srt); repeatable. Default: seed-transcript* in the script's folder")
    ap.add_argument("--allow", action="append", default=[],
                    help="locked paid-asset phrase allowed verbatim (R2); repeatable")
    ap.add_argument("--no-seed", default="",
                    help="remake folder without a seed transcript: give the reason (e.g. entry C, source not found)")
    ap.add_argument("--competitor", action="append", default=[],
                    help="competitor transcript file or folder (same topic); repeatable. "
                         "Default: competitor-transcripts/ in the script's folder")
    ap.add_argument("--no-competitor", default="",
                    help="no competitor transcripts for this video: give the reason")
    a = ap.parse_args()

    target = Path(a.script).resolve()
    seeds = [Path(p).resolve() for p in a.against]
    if not seeds:
        seeds = sorted(p for p in target.parent.glob("seed-transcript*")
                       if p.suffix.lower() in (".txt", ".md", ".srt"))
    scripts_dir = target.parent.parent
    others = [p for p in scripts_dir.glob("*/script.md") if p.resolve() != target]
    others.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    others = others[: a.last]

    t = tts_text(target)
    ts = {s.lower(): s for s in sentences(t)}
    tg = grams(t)
    worst = 0
    print(f"Target: {target.parent.name}  ({len(t.split())} words)\n")
    for p in others:
        o = tts_text(p)
        os_ = {s.lower() for s in sentences(o)}
        same = [ts[k] for k in ts if k in os_]
        og = grams(o)
        overlap = 100 * len(tg & og) / max(1, min(len(tg), len(og)))
        cues = [c for c in SKELETON_CUES if c in t.lower() and c in o.lower()]
        worst = max(worst, len(same))
        flag = "FAIL" if len(same) > MAX_IDENTICAL else "ok"
        print(f"[{flag}] vs {p.parent.name}: identical sentences {len(same)} · 6-gram overlap {overlap:.1f}% · shared skeleton cues {len(cues)}")
        for x in same:
            print(f"      = {x}")
        if cues:
            print(f"      skeleton: {', '.join(cues)}")
    print(f"\nMax identical sentences vs any recent script: {worst} (limit {MAX_IDENTICAL})")

    seed_ok = True
    if seeds:
        print("\n— LANE B: so với transcript seed —")
        for sp in seeds:
            if not sp.exists():
                print(f"[FAIL] seed file not found: {sp}")
                seed_ok = False
                continue
            seed_ok = check_seed(t, sp, a.allow) and seed_ok
    elif target.parent.name.startswith("remake-"):
        if a.no_seed:
            print(f"\n⚠️ remake folder, seed check skipped: {a.no_seed}")
        else:
            print("\n[FAIL] remake folder but no seed transcript — add seed-transcript.txt, "
                  "pass --against, or --no-seed \"<lý do>\"")
            seed_ok = False

    comp_ok = True
    files = competitor_files(a.competitor, target.parent)
    print("\n— ĐỐI THỦ: so với transcript video cùng chủ đề —")
    if files is None:
        comp_ok = False
    elif files:
        comp_ok = check_competitors(t, files, a.allow)
    elif a.no_competitor:
        print(f"⚠️ bỏ qua: {a.no_competitor}")
    else:
        print("⚠️ chưa có transcript đối thủ — đặt vào competitor-transcripts/ (video outlier cùng chủ đề ở Topic Gate), "
              "hoặc --no-competitor \"<lý do>\"")
    sys.exit(1 if worst > MAX_IDENTICAL or not seed_ok or not comp_ok else 0)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
