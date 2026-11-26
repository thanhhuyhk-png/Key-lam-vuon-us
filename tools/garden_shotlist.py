"""Garden US shot list from voice.srt, built to the rhythm contract (adapted from the military channel's contract).

Usage:
    python tools/garden_shotlist.py scripts/big-idea-062-.../voice/voice.srt scripts/big-idea-062-.../footage/shotlist_cfg_062.py

The config file defines SECTIONS (name, anchor phrase), POOLS (which assets), RECIPES (pool weights per section),
KEYWORDS (cue text -> pool override), AI_PROMPTS (pool -> AI image prompts used when a pool is thin), OVERLAYS (triggers).
Writes <OUT>/shotlist.csv and <OUT>/ai_needed.csv and prints contract checks. No network, no credits.

Contract (design thresholds):
  0:00-1:00  avg <= 2.2 s, max 3.0 s    |  1:00-3:00  avg <= 3.0 s, max 4.0 s   |  after 3:00  avg <= 3.5 s, max 4.0 s
  every stock shot < 4 s; each source <= 3 uses and not repeated within 60 s; real footage share of non-graphic shots > 70 %.
"""
import csv
import importlib.util
import json
import pathlib
import random
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def load_cfg(path):
    spec = importlib.util.spec_from_file_location("cfg", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def ts(x):
    h, m, r = x.split(":")
    s, ms = r.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(path):
    rows = []
    for b in re.split(r"\n\s*\n", pathlib.Path(path).read_text(encoding="utf-8-sig").strip()):
        ls = b.splitlines()
        t = [l for l in ls if "-->" in l]
        if not t:
            continue
        a, c = [ts(x.strip()) for x in t[0].split("-->")]
        rows.append((a, c, " ".join(l for l in ls if "-->" not in l and not l.strip().isdigit()).strip()))
    return rows


def find_time(cues, phrase):
    low = phrase.lower().replace("’", "'")
    for a, c, t in cues:
        if low in t.lower().replace("’", "'"):
            return a
    return None


def target(t):
    if t < 60:
        return [1.8, 2.0, 2.2, 2.4, 2.6, 2.0, 2.2, 2.8], 3.0
    if t < 180:
        return [2.6, 3.0, 3.4, 3.0, 2.8, 3.6, 3.0, 3.2], 4.0
    return [3.0, 3.5, 3.9, 3.2, 3.8, 3.5, 3.0, 3.9], 4.0


def main():
    srt, cfgp = sys.argv[1], sys.argv[2]
    cfg = load_cfg(cfgp)
    cues = parse_srt(srt)
    total = cues[-1][1]
    rnd = random.Random(62)
    # sections
    secs = []
    for name, phrase in cfg.SECTIONS:
        t = 0.0 if phrase is None else find_time(cues, phrase)
        if t is None:
            raise SystemExit(f"anchor not found: {name}: {phrase}")
        secs.append([name, t, None])
    for i in range(len(secs)):
        secs[i][2] = secs[i + 1][1] if i + 1 < len(secs) else total

    def section_at(t):
        for n, a, b in secs:
            if a - 1e-6 <= t < b:
                return n
        return secs[-1][0]

    # cut points
    cuts, t, i = [0.0], 0.0, 0
    ends = sorted({round(c[1], 2) for c in cues} | {round(a, 2) for a, _, _ in cues} | {round(s[1], 2) for s in secs})
    while t < total - 0.05:
        pat, mx = target(t)
        d = pat[i % len(pat)]
        i += 1
        nxt = t + d
        near = [e for e in ends if abs(e - nxt) <= 0.5 and e > t + 1.2 and e - t <= mx]
        if near:
            nxt = min(near, key=lambda e: abs(e - nxt))
        # never cross a section boundary
        for _, a, _b in secs:
            if t < a < nxt - 0.3:
                nxt = a
                break
        nxt = min(nxt, total)
        if total - nxt < 1.2 and total - t <= mx:
            nxt = total
        cuts.append(round(nxt, 2))
        t = nxt
    shots = [{"start": cuts[k], "end": cuts[k + 1]} for k in range(len(cuts) - 1)]

    # --- trigger-based graphic cards (cfg.GRAPHIC_TRIGGERS = [(phrase, asset_key, min_dur_s)]) ---
    # a card starts at the spoken phrase (or at the shot start if that is <=1.5 s earlier) and swallows following shots until min_dur,
    # so cards stay on screen long enough to read and are tied to the narration, never back-to-back.
    for phrase, gkey, min_dur in getattr(cfg, "GRAPHIC_TRIGGERS", []):
        t0 = find_time(cues, phrase)
        if t0 is None:
            raise SystemExit(f"graphic trigger not found: {phrase}")
        i = next((j for j, x in enumerate(shots) if x["start"] - 1e-6 <= t0 < x["end"]), None)
        if i is None:
            continue
        if t0 - shots[i]["start"] > 1.5:
            cut = round(t0 - 0.2, 2)
            shots[i:i + 1] = [{"start": shots[i]["start"], "end": cut}, {"start": cut, "end": shots[i]["end"]}]
            i += 1
        shots[i]["forced"] = gkey
        while shots[i]["end"] - shots[i]["start"] < min_dur and i + 1 < len(shots) and not shots[i + 1].get("forced"):
            shots[i]["end"] = shots[i + 1]["end"]
            del shots[i + 1]

    def text_of(s):
        out = []
        for a, c, tx in cues:
            if c > s["start"] + 0.15 and a < s["end"] - 0.15:
                out.append(tx)
        return " ".join(out)

    pools = cfg.POOLS
    use = {}
    last_used = {}
    ai_needed = {}
    motions = ["zoom_in", "pan_left", "zoom_out", "pan_right", "push_diag"]
    n_still = 0
    last_label = {}
    for k, s in enumerate(shots):
        s["id"] = f"S{k + 1:03d}"
        s["dur"] = round(s["end"] - s["start"], 2)
        s["section"] = section_at(s["start"] + 0.01)
        s["text"] = text_of(s)
        low = s["text"].lower().replace("’", "'")
        recipe = cfg.RECIPES.get(s["section"], {"gen": 1.0})
        # forced pure graphic
        forced = s.get("forced")
        for sec, (g_every, gkey) in getattr(cfg, "GRAPHIC_SECTIONS", {}).items():
            if s["section"] == sec and (k % g_every == 0):
                forced = gkey
        pool = None
        for pat, p in cfg.KEYWORDS:
            if re.search(pat, low):
                pool = p
                break
        if pool is None or pool not in pools:
            names, weights = zip(*recipe.items())
            pool = rnd.choices(names, weights=weights)[0]
        s["pool"] = pool
        s["overlay"] = ""
        s["kind"] = ""
        gaps = getattr(cfg, "OVERLAY_GAP", {})
        if forced:
            s["type"], s["asset"], s["in"], s["crop"], s["motion"] = "G", forced, 0, "", "build"
            continue
        dgap = getattr(cfg, "OVERLAY_GAP_DEFAULT", 0)
        for pat, kind, txt in cfg.OVERLAYS:
            m = re.search(pat, low)
            if m:
                label = txt if txt else m.group(0).upper()
                if s["start"] - last_label.get(label, -9999) < gaps.get(label, dgap):
                    continue
                last_label[label] = s["start"]
                s["overlay"], s["kind"] = label, kind
                break
        if forced:
            s["type"], s["asset"], s["in"], s["crop"], s["motion"] = "G", forced, 0, "", "build"
            continue
        if pool == "AI" or not pools.get(pool):
            plist = cfg.AI_PROMPTS.get(s["section"]) or cfg.AI_PROMPTS["default"]
            key = plist[len([1 for x in shots[:k] if x.get("type") == "A" and x["section"] == s["section"]]) % len(plist)]
            s["type"], s["asset"], s["in"], s["crop"], s["motion"] = "A", key[0], 0, "", motions[k % 5]
            ai_needed.setdefault(key[0], [key[1], 0])[1] += 1
            continue
        # choose least-used asset not used in last 60 s
        cands = [a for a in pools[pool] if use.get(a["id"], 0) < 3 and s["start"] - last_used.get(a["id"], -999) >= 60]
        if not cands:
            cands = [a for a in pools[pool] if use.get(a["id"], 0) < 3]
        if not cands:
            plist = cfg.AI_PROMPTS.get(s["section"]) or cfg.AI_PROMPTS["default"]
            key = plist[k % len(plist)]
            s["type"], s["asset"], s["in"], s["crop"], s["motion"] = "A", key[0], 0, "", motions[k % 5]
            ai_needed.setdefault(key[0], [key[1], 0])[1] += 1
            continue
        a = min(cands, key=lambda x: (use.get(x["id"], 0), last_used.get(x["id"], -999)))
        u = use.get(a["id"], 0)
        use[a["id"]] = u + 1
        last_used[a["id"]] = s["start"]
        D = a.get("dur") or 8
        room = max(D - s["dur"] - 0.1, 0)
        s["type"] = a["type"]
        s["asset"] = a["id"]
        s["in"] = round(room * [0.0, 0.5, 1.0][u % 3] if room else 0, 1)
        s["crop"] = ["full", "zoom_L", "zoom_R"][u % 3]
        s["motion"] = motions[(k + u) % 5]
    # text events: ensure >= MIN_EVENTS per minute (first minute: MIN_EVENTS_FIRST) with short 'pop' captions from the voice text
    stop = set("the a an and or but to of in on at for with from is are was were be been it its it's that this these those you your yours i we they them he she his her as by if so than then not no do does did can will would should could just very really also more most some any one two three four five six seven eight nine ten there here what which who whom how when where why about into over under again once only own same too out up down off".split())

    def caption(txt):
        words = [w for w in re.findall(r"[A-Za-z0-9'-]+", txt) if w.lower() not in stop and len(w) > 3]
        if not words:
            return ""
        words = sorted(words, key=lambda w: -len(w))[:2]
        return " ".join(words).upper()

    for m in range(int(total // 60) + 1):
        a, b = m * 60, (m + 1) * 60
        need = (cfg.MIN_EVENTS_FIRST if m == 0 else cfg.MIN_EVENTS) - len([s for s in shots if a <= s["start"] < b and s["kind"]])
        free = [s for s in shots if a <= s["start"] < b and not s["kind"] and s["type"] != "G"]
        if need > 0 and free:
            step = max(len(free) // need, 1)
            for s in free[::step][:need]:
                c = caption(s["text"])
                if c:
                    s["kind"], s["overlay"] = "pop", c
    # pattern break marker: every <= 45 s something big (graphic shot or overlay kind slam/stamp)
    big = [s["start"] for s in shots if s["type"] == "G" or s["kind"] in ("slam", "stamp")]
    lastb = 0.0
    for s in shots:
        if s["type"] == "G" or s["kind"] in ("slam", "stamp"):
            lastb = s["start"]
        elif getattr(cfg, "BREAK_FILL", True) and s["start"] - lastb > 40 and s["type"] != "A":
            s["kind"], s["overlay"] = "slam", s["overlay"] or "BREAK"
            lastb = s["start"]
    outdir = pathlib.Path(cfgp).parent
    with open(outdir / "shotlist.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "start", "end", "dur", "section", "type", "asset", "in_s", "crop", "motion", "overlay_kind", "overlay_text", "pool", "voice_text"])
        for s in shots:
            w.writerow([s["id"], s["start"], s["end"], s["dur"], s["section"], s["type"], s["asset"], s["in"], s["crop"], s["motion"], s["kind"], s["overlay"], s["pool"], s["text"]])
    with open(outdir / "ai_needed.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ai_id", "uses", "prompt"])
        for k, (p, n) in ai_needed.items():
            w.writerow([k, n, p])
    # checks
    def stats(a, b):
        xs = [s["dur"] for s in shots if a <= s["start"] < b]
        return (len(xs), round(sum(xs) / len(xs), 2) if xs else 0, max(xs) if xs else 0)
    print("total", round(total, 1), "s | shots", len(shots))
    for lab, a, b in (("0:00-1:00", 0, 60), ("1:00-3:00", 60, 180), ("3:00-end", 180, 1e9)):
        n, avg, mx = stats(a, b)
        print(f"{lab:10s} shots {n:3d} avg {avg:.2f}s max {mx:.1f}s")
    nonG = [s for s in shots if s["type"] != "G"]
    real = [s for s in nonG if s["type"] in ("V", "P")]
    print("graphic shots", len(shots) - len(nonG), "| non-graphic", len(nonG), "| real", len(real), f"({len(real) / len(nonG) * 100:.0f}%)", "| AI", len(nonG) - len(real))
    srcs = {s["asset"] for s in nonG}
    print("distinct sources", len(srcs), "| need >= ", round(len(nonG) / 3))
    over = [s["id"] for s in shots if s["type"] in ("V", "P") and s["dur"] >= 4.0]
    print("stock shots >= 4.0 s:", over)
    ev = {}
    for s in shots:
        if s["kind"]:
            ev[int(s["start"] // 60)] = ev.get(int(s["start"] // 60), 0) + 1
    print("overlay events per minute:", dict(sorted(ev.items())))
    print("AI needed:", {k: v[1] for k, v in ai_needed.items()})


if __name__ == "__main__":
    main()
