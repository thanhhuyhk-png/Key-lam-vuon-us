"""Footage feasibility check across Pexels, Pixabay and Coverr (search only, no downloads).

Usage:
    python tools/footage_search.py queries.txt --out scripts/big-idea-062-.../footage-candidates.md [--env "D:/0008. Key Quân sự/.env"]

queries.txt: one query per line, optional "ID|query" (e.g. "16|microgreens tray").
Keys (names): PEXELS_API_KEY, PIXABAY_API_KEY, COVERR_API_KEY. Read from env, then ./.env, then --env file. Never printed.
A clip counts as usable if duration >= 8 s and width >= 1280 (landscape). Counts only; check content and license before use.
Coverr results flagged AI when the API says is_ai_generated. Coverr asks for its logo as a clickable credit when its API is used in an app, and its
download counter (PATCH /videos/:id/stats/downloads) is required when an app downloads files — this tool does not download.
"""
import argparse
import json
import os
import pathlib
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = "curl/8.5.0"
MIN_DUR, MIN_W = 8.0, 1280


def load_env(extra):
    env = dict(os.environ)
    for p in [pathlib.Path(".env")] + ([pathlib.Path(extra)] if extra else []):
        if p.exists():
            for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.split("=", 1)
                    env.setdefault(k.strip(), v.strip().strip('"'))
    return env


def get(url, headers=None):
    h = {"User-Agent": UA}
    h.update(headers or {})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=40) as r:
                return json.loads(r.read())
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def pexels(q, key):
    d = get("https://api.pexels.com/videos/search?" + urllib.parse.urlencode({"query": q, "per_page": 20, "orientation": "landscape"}), {"Authorization": key})
    out = []
    for v in (d or {}).get("videos", []):
        out.append({"src": "pexels", "title": (v.get("url") or "").rstrip("/").split("/")[-1].replace("-", " "), "dur": f(v.get("duration")),
                    "w": v.get("width") or 0, "url": v.get("url"), "by": (v.get("user") or {}).get("name", "")})
    return out


def pixabay(q, key):
    d = get("https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": key, "q": q, "per_page": 20}))
    out = []
    for v in (d or {}).get("hits", []):
        w = max((vv.get("width") or 0 for vv in (v.get("videos") or {}).values()), default=0)
        out.append({"src": "pixabay", "title": (v.get("tags") or "")[:60], "dur": f(v.get("duration")), "w": w, "url": v.get("pageURL"), "by": v.get("user", "")})
    return out


def coverr(q, key):
    d = get("https://api.coverr.co/videos?" + urllib.parse.urlencode({"query": q, "page_size": 20, "urls": "false"}), {"Authorization": "Bearer " + key})
    out = []
    hits = (d or {}).get("hits")
    for v in hits if isinstance(hits, list) else []:
        out.append({"src": "coverr", "title": (v.get("title") or "").strip() + (" [AI]" if v.get("is_ai_generated") else ""), "dur": f(v.get("duration")),
                    "w": f(v.get("max_width")) or 1920, "url": "https://coverr.co/videos/" + str(v.get("slug") or v.get("id")), "by": "Coverr"})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries")
    ap.add_argument("--out", required=True)
    ap.add_argument("--env")
    a = ap.parse_args()
    env = load_env(a.env)
    sources = [("pexels", pexels, env.get("PEXELS_API_KEY")), ("pixabay", pixabay, env.get("PIXABAY_API_KEY")), ("coverr", coverr, env.get("COVERR_API_KEY"))]
    sources = [s for s in sources if s[2]]
    print("sources:", [s[0] for s in sources])
    lines = ["# Footage candidates (search only)", "", f"Usable = duration >= {MIN_DUR:.0f} s and width >= {MIN_W}. Counts are search hits that pass the filter, not a content check.", "",
             "| Shot | Query | " + " | ".join(s[0] for s in sources) + " | Top candidates |", "|---|---|" + "---|" * len(sources) + "---|"]
    for raw in pathlib.Path(a.queries).read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        sid, q = raw.split("|", 1) if "|" in raw else ("", raw)
        counts, tops = [], []
        for name, fn, key in sources:
            res = [c for c in fn(q, key) if c["dur"] >= MIN_DUR and c["w"] >= MIN_W]
            counts.append(str(len(res)))
            tops += [f"[{c['src']}] {c['title'][:40]} ({c['dur']:.0f}s) {c['url']}" for c in res[:2]]
            time.sleep(0.4)
        lines.append(f"| {sid} | {q} | " + " | ".join(counts) + " | " + "<br>".join(tops[:4]) + " |")
        print(sid, q, counts, flush=True)
    pathlib.Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("saved", a.out)


if __name__ == "__main__":
    main()
