"""Kiểm định kỳ kênh Garden US — khép vòng phản hồi tự động (thêm 2026-11-22). 0 credit vidIQ.

Vì sao: tới 22/11/2026 có 47 thư mục có prediction.md nhưng chỉ 1 retro.md; task định kỳ duy nhất
đã tắt từ 09/06; 25 luật ACTIVE phần lớn ghi «chưa có retro». Kênh viết luật nhanh hơn đo luật.
Tool này đo mọi video đã đăng ≥7 ngày, ghi retro-auto.md cho từng thư mục, và chấm từng luật
bằng số thật của chính kênh (nhóm CÓ áp luật vs KHÔNG áp).

Lệnh:
    python -X utf8 tools/kiem_dinh_ky.py                 # đầy đủ: làm mới health + du_bao, đo, báo cáo
    python -X utf8 tools/kiem_dinh_ky.py --khong-lam-moi # chỉ đọc số đã có + đo retention video mới

Đầu ra:
    research/kiem-dinh-ky/<YYYYMMDD>.md + latest.md   báo cáo (sức khoẻ · cờ đỏ · chấm luật · việc phải làm)
    research/kiem-dinh-ky/video-ledger.tsv            mỗi video 1 dòng: views_5d, AVD, giữ chân 0:30/1:00/2:00, bình luận/1K, CTR Studio, cờ luật
    research/kiem-dinh-ky/ctr-studio.tsv              CTR + lượt hiển thị từng video, đọc từ file export Studio
    scripts/<thư mục>/retro-auto.md                   số thật của video (không ghi đè retro.md của người)

CTR: YouTube Analytics API không trả CTR (đã thử 22/11/2026). Thả file export Studio
(Studio → Analytics → Nội dung → Xuất, dạng .zip hoặc .csv) vào research/ hoặc research/studio-export/ — tool tự đọc.
"""
import argparse
import csv
import datetime as dt
import io
import json
import re
import statistics
import subprocess
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import yt_analytics as yta  # noqa: E402

OUT = ROOT / "research" / "kiem-dinh-ky"
CACHE = OUT / "retro-cache.json"
LEDGER = OUT / "video-ledger.tsv"
CTR_TSV = OUT / "ctr-studio.tsv"
MAP_TSV = ROOT / "research" / "thu-muc-video.tsv"
VID_JSON = ROOT / "research" / "video-5d.json"
HEALTH = ROOT / "references" / "channel-health-latest.json"
DC_TSV = ROOT / "references" / "cach-noi-da-chot.tsv"
WPM = 165.0
TODAY = dt.date.today()


def run(label, args):
    print(f"→ {label}")
    p = subprocess.run([sys.executable, "-X", "utf8", *map(str, args)], cwd=ROOT, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=900)
    tail = (p.stdout or "").strip().splitlines()[-3:]
    for ln in tail:
        print("   ", ln)
    if p.returncode:
        print("   ⚠️ lỗi:", (p.stderr or "").strip()[-300:])
    return p.returncode


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def f1(x, nd=1):
    return "—" if x is None else (f"{x:.{nd}f}" if isinstance(x, float) else str(x))


# ---------- CTR từ export Studio ----------
WIN_RE = re.compile(r"(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})")


def studio_tables():
    """Mọi bảng 'theo video' trong export Studio (.zip/.csv) ở research/ và research/studio-export/."""
    srcs = list((ROOT / "research").glob("*.zip")) + list((ROOT / "research" / "studio-export").glob("*.*"))
    for src in srcs:
        m = WIN_RE.search(src.name)
        win_end = m.group(2) if m else dt.date.fromtimestamp(src.stat().st_mtime).isoformat()
        win_start = m.group(1) if m else ""
        try:
            if src.suffix.lower() == ".zip":
                with zipfile.ZipFile(src) as z:
                    for n in z.namelist():
                        if n.lower().endswith(".csv"):
                            yield win_start, win_end, src.name, z.read(n).decode("utf-8-sig", errors="replace")
            elif src.suffix.lower() == ".csv":
                yield win_start, win_end, src.name, src.read_text(encoding="utf-8-sig", errors="replace")
        except (zipfile.BadZipFile, OSError) as e:
            print(f"   ⚠️ không đọc được {src.name}: {e}")


def ingest_ctr():
    best = {}
    for ws, we, name, txt in studio_tables():
        rows = list(csv.DictReader(io.StringIO(txt)))
        if not rows or "Thumbnail click-through rate (%)" not in rows[0] or "Content" not in rows[0]:
            continue
        for r in rows:
            vid = (r.get("Content") or "").strip()
            if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
                continue
            try:
                ctr = float(r["Thumbnail click-through rate (%)"] or 0)
                imp = int(float(r.get("Thumbnail impressions") or 0))
                vw = int(float(r.get("Views") or 0))
            except ValueError:
                continue
            old = best.get(vid)
            if old is None or we > old["win_end"]:
                best[vid] = {"video_id": vid, "ctr_pct": ctr, "impressions": imp, "views_win": vw, "title": (r.get("Video title") or "").strip(), "pub": (r.get("Video publish time") or "").strip(),
                             "avd_pct": r.get("Average percentage viewed (%)"), "win_start": ws, "win_end": we,
                             "nguon": name}
    OUT.mkdir(parents=True, exist_ok=True)
    with CTR_TSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, ["video_id", "ctr_pct", "impressions", "views_win", "title", "pub", "avd_pct", "win_start", "win_end", "nguon"], delimiter="\t")
        w.writeheader()
        w.writerows(sorted(best.values(), key=lambda r: r["video_id"]))
    latest = max((r["win_end"] for r in best.values()), default=None)
    print(f"→ CTR Studio: {len(best)} video · export mới nhất kết thúc {latest or '—'}")
    return best, latest


# ---------- retention ----------
def retention(access, vid, dur):
    end = TODAY
    start = end - dt.timedelta(days=365)
    base = yta.analytics(access, ids="channel==MINE", startDate=str(start), endDate=str(end), dimensions="video",
                         filters="video==" + vid, metrics="views,averageViewPercentage,averageViewDuration,comments")
    bc = [c["name"] for c in base["columnHeaders"]]
    br = dict(zip(bc, base["rows"][0])) if base.get("rows") else {}
    ret = yta.analytics(access, ids="channel==MINE", startDate=str(start), endDate=str(end),
                        dimensions="elapsedVideoTimeRatio", filters="video==" + vid, metrics="audienceWatchRatio")
    curve = [(float(r[0]), float(r[1])) for r in ret.get("rows", [])]

    def at(sec):
        if not curve or not dur:
            return None
        x = sec / dur
        if x > 1:
            return None
        prev = curve[0]
        for c in curve:
            if c[0] >= x:
                if c[0] == prev[0]:
                    return round(c[1] * 100, 1)
                t = (x - prev[0]) / (c[0] - prev[0])
                return round((prev[1] + t * (c[1] - prev[1])) * 100, 1)
            prev = c
        return round(curve[-1][1] * 100, 1)

    def biggest(lo, hi):
        best = None
        for i in range(1, len(curve)):
            s0, s1 = curve[i - 1][0] * dur, curve[i][0] * dur
            if s0 < lo or s1 > hi:
                continue
            d = curve[i][1] - curve[i - 1][1]
            if best is None or d < best[2]:
                best = (s0, s1, d)
        return None if best is None else f"{int(best[0])}→{int(best[1])}s {best[2] * 100:+.1f}%"

    views = int(br.get("views", 0) or 0)
    com = int(br.get("comments", 0) or 0)
    return {"views": views, "avd_pct": round(float(br.get("averageViewPercentage", 0) or 0), 1),
            "avd_s": int(br.get("averageViewDuration", 0) or 0), "comments": com,
            "com_per_1k": round(com * 1000 / views, 2) if views else None,
            "ret_30": at(30), "ret_60": at(60), "ret_120": at(120), "ret_240": at(240),
            "drop_0_60": biggest(0, 60), "drop_60_end": biggest(60, dur or 1), "curve_n": len(curve),
            "do_luc": TODAY.isoformat()}


# ---------- đặc điểm thư mục ----------
def dc010():
    if not DC_TSV.exists():
        return None
    for ln in DC_TSV.read_text(encoding="utf-8").splitlines():
        c = ln.split("\t")
        if c[0] == "DC010":
            return re.compile(c[2], re.I)
    return None


def folder_flags(d: Path):
    p = d / "script.md"
    out = {"words": None, "phut": None, "nhanh": 0, "tiep_theo": 0, "FIRST_STEP": 0, "ENDING_FROM": 0, "COMMENT_Q": 0, "lane": "B" if d.name.startswith("remake") else "A",
           "hang": ""}
    if p.exists():
        raw = p.read_text(encoding="utf-8", errors="replace")
        head, _, tts = raw.partition("## TTS SCRIPT")
        if tts:
            n = len(re.sub(r"<#[\d.]+#>", " ", tts).split())
            out["words"] = n
            out["phut"] = round(n / WPM, 1)
        for k in ("FIRST_STEP", "ENDING_FROM", "COMMENT_Q"):
            out[k] = 1 if re.search(rf"^\s*[-*]?\s*\**{k}\**:", head, re.M) else 0
    ps = d / "pipeline-state.md"
    if ps.exists():
        pst = ps.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"HẠNG:\s*([^\n·|]+)", pst)
        out["hang"] = m.group(1).strip() if m else ""
        out["nhanh"] = 1 if re.search(r"3R:\s*ĐƯỜNG NHANH", pst) else 0
        out["tiep_theo"] = 1 if re.search(r"PHẦN TIẾP THEO:\s*[A-Za-z0-9_-]{11}", pst) else 0
    return out


def write_retro_auto(d: Path, v, r, ctr, med5):
    p = d / "retro-auto.md"
    lines = [f"# RETRO-AUTO — {v['title']}",
             "",
             f"> Do `tools/kiem_dinh_ky.py` ghi lúc {r['do_luc']} (0 credit). Số thật, không diễn giải — người hoặc phiên kiểm định "
             f"viết phần học được vào `retro.md`. File này được ghi lại mỗi lần đo.",
             "",
             f"Video: https://youtu.be/{v['videoId']} · đăng {v['published']} · thời lượng {yta.fmt_mmss(v.get('dur') or 0)}",
             "",
             "| Chỉ số | Thật | Mốc kênh |",
             "|---|---|---|",
             f"| views_5d | {v.get('views_5d')} | trung vị 10 video gần nhất {f1(med5, 0)} |",
             f"| Views (tới nay) | {r['views']} | — |",
             f"| AVD | {r['avd_pct']}% · {r['avd_s']}s | — |",
             f"| Còn lại @0:30 / 1:00 / 2:00 / 4:00 | {f1(r['ret_30'])} / {f1(r['ret_60'])} / {f1(r['ret_120'])} / {f1(r['ret_240'])} % | — |",
             f"| Rơi mạnh nhất 0–60s | {r['drop_0_60'] or '—'} | — |",
             f"| Rơi mạnh nhất sau 60s | {r['drop_60_end'] or '—'} | — |",
             f"| Bình luận | {r['comments']} ({f1(r['com_per_1k'], 2)}/1K view) | — |",
             f"| CTR (Studio) | {f1(ctr.get('ctr_pct')) + '% · ' + str(ctr.get('impressions')) + ' lượt hiển thị · kỳ ' + ctr.get('win_start', '') + '→' + ctr.get('win_end', '') if ctr else 'chưa có — thả export Studio vào research/'} | — |",
             ""]
    p.write_text("\n".join(lines), encoding="utf-8")


# ---------- chấm luật ----------
def cohort(rows, key, metric, flag_fn):
    a = [r[metric] for r in rows if flag_fn(r) and r.get(metric) is not None]
    b = [r[metric] for r in rows if not flag_fn(r) and r.get(metric) is not None]
    return len(a), med(a), len(b), med(b)


def verdict(na, ma, nb, mb, higher_better=True, min_n=3):
    if na < min_n or nb < min_n or ma is None or mb is None:
        return f"⏳ chưa đủ mẫu (cần ≥{min_n} mỗi bên)"
    better = ma > mb if higher_better else ma < mb
    ratio = (ma / mb) if mb else None
    tag = "✅ số ủng hộ luật" if better else "🔴 số NGƯỢC luật"
    return f"{tag} ({'×' + format(ratio, '.2f') if ratio else ''})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--khong-lam-moi", action="store_true", help="không chạy lại health / du_bao")
    ap.add_argument("--do-lai", action="store_true", help="đo lại retention mọi video (bỏ cache)")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    if not a.khong_lam_moi:
        run("health 8 tuần", [TOOLS / "yt_analytics.py", "health"])
        run("du_bao dong-bo → dien → cong", [TOOLS / "du_bao.py", "tat-ca"])

    ctr, ctr_latest = ingest_ctr()
    vids = json.loads(VID_JSON.read_text(encoding="utf-8")) if VID_JSON.exists() else {"videos": []}
    med5 = vids.get("median_5d_last10")
    byid = {v["videoId"]: v for v in vids["videos"]}
    fmap = {}
    if MAP_TSV.exists():
        for r in csv.DictReader(MAP_TSV.open(encoding="utf-8"), delimiter="\t"):
            fmap[r["video_id"]] = r["thu_muc"]
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() and not a.do_lai else {}

    access = None
    pub = [v for v in vids["videos"] if v.get("privacy") == "public"]
    meta = {}
    try:
        access = yta.get_access_token()
        meta = yta.video_meta(access, [v["videoId"] for v in pub])
    except SystemExit as e:
        print("   ⚠️ không lấy được token / meta:", e)
    dc = dc010()
    rows = []
    new_measured = 0
    for v in pub:
        pd_ = dt.date.fromisoformat(v["published"])
        age = (TODAY - pd_).days
        v["dur"] = meta.get(v["videoId"], {}).get("dur") or 0
        if v["dur"] and v["dur"] <= 180:
            continue  # Shorts
        r = cache.get(v["videoId"])
        # đo khi ≥7 ngày; đo lại một lần ở ≥28 ngày để có số ổn định
        need = age >= 7 and access and (r is None or (age >= 28 and r.get("age_do", 0) < 28))
        if need:
            try:
                r = retention(access, v["videoId"], v["dur"])
                r["age_do"] = age
                cache[v["videoId"]] = r
                new_measured += 1
            except SystemExit as e:
                print(f"   ⚠️ {v['videoId']}: {e}")
        folder = fmap.get(v["videoId"], "")
        fl = folder_flags(ROOT / "scripts" / folder) if folder else {}
        c = ctr.get(v["videoId"], {})
        row = {"video_id": v["videoId"], "dang": v["published"], "tuoi": age, "thu_muc": folder, "tieu_de": v["title"],
               "phut_thuc": round(v["dur"] / 60, 1) if v["dur"] else None, "views_5d": v.get("views_5d") if not v.get("partial") else None,
               "views": (r or {}).get("views"), "avd_pct": (r or {}).get("avd_pct"), "ret_30": (r or {}).get("ret_30"),
               "ret_60": (r or {}).get("ret_60"), "ret_120": (r or {}).get("ret_120"), "com_per_1k": (r or {}).get("com_per_1k"),
               "ctr_pct": c.get("ctr_pct"), "impressions": c.get("impressions"), "views_win": c.get("views_win"),
               "title_meta": (1 if dc and dc.search(v["title"]) else 0),
               **{k: fl.get(k) for k in ("lane", "hang", "nhanh", "tiep_theo", "words", "FIRST_STEP", "ENDING_FROM", "COMMENT_Q")}}
        rows.append(row)
        if folder and r and (ROOT / "scripts" / folder).is_dir():
            write_retro_auto(ROOT / "scripts" / folder, v, r, c, med5)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    rows.sort(key=lambda r: r["dang"], reverse=True)
    cols = list(rows[0].keys()) if rows else []
    with LEDGER.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"→ đo retention mới: {new_measured} video · ledger {len(rows)} dòng")

    report(rows, med5, ctr_latest, ctr)


def report(rows, med5, ctr_latest, ctr=None):
    H = json.loads(HEALTH.read_text(encoding="utf-8")) if HEALTH.exists() else {}
    wk = [w for w in H.get("weekly_trend", []) if w.get("views")]
    full = wk[1:-1] if len(wk) > 3 else wk  # bỏ tuần đầu/cuối cắt dở
    flags, todo = [], []

    # sức khoẻ
    last, prior = (full[-1]["views"] if full else None), med([w["views"] for w in full[-5:-1]])
    if last and prior and last < 0.85 * prior:
        flags.append(f"🔴 View tuần {full[-1]['week']} = {last:,} < 85 % trung vị 4 tuần trước ({prior:,.0f}).")
    rec = [r for r in rows if r["views_5d"] is not None and r["tuoi"] >= 5]
    m5_new, m5_old = med([r["views_5d"] for r in rec[:5]]), med([r["views_5d"] for r in rec[5:10]])
    if m5_new is not None and m5_old and m5_new < m5_old:
        flags.append(f"🟡 Trung vị views_5d 5 video mới nhất {m5_new:.0f} < 5 video trước đó {m5_old:.0f}.")
    cat = H.get("catalog_split", {})
    if cat.get("old_share_pct", 0) >= 85:
        flags.append(f"🔴 Video cũ giữ {cat['old_share_pct']} % view; {cat.get('new_videos')} video mới chỉ góp "
                     f"{100 - cat['old_share_pct']:.1f} %. Kênh đang sống bằng catalog đang nguội dần.")
    last14 = [r for r in rows if r["tuoi"] <= 14]
    if len(last14) < 4:
        flags.append(f"🟡 Nhịp đăng: {len(last14)} video trong 14 ngày (mục tiêu ≥4).")
    # C6 (22/11/2026): ~1/3 video là Lane B remake — TEST 6 video
    since = [r for r in rows if r["dang"] >= "2026-11-22" and r["thu_muc"]]
    if since:
        nb = sum(1 for r in since if r["lane"] == "B")
        msg = f"Tỷ lệ lane từ 22/11: {nb}/{len(since)} remake (mục tiêu ~1/3, TEST 6 video)"
        if len(since) >= 3 and nb == 0:
            flags.append(f"🟡 {msg} — video kế tiếp nên là remake.")
        elif len(since) >= 6:
            todo.append(f"{msg} — đủ 6 video: chấm dòng «Lane B remake» ở mục 4 rồi trình user giữ hay bỏ tỷ lệ.")
        else:
            todo.append(msg)
        nt = sum(1 for r in since if r.get("tiep_theo") == 1)
        msg2 = f"Phần tiếp theo catalog từ 22/11: {nt}/{len(since)} (mục tiêu ~1/4, TEST 8 video)"
        if len(since) >= 4 and nt == 0:
            flags.append(f"🟡 {msg2} — video kế tiếp nên là phần tiếp theo của 1 video catalog top-5.")
        elif len(since) >= 8:
            todo.append(f"{msg2} — đủ 8 video: chấm dòng «C2 phần tiếp theo» ở mục 4 rồi trình user.")
    ctr_new = [r for r in rows if r["ctr_pct"] is not None and r["tuoi"] <= 45]
    if ctr_new:
        mc = med([r["ctr_pct"] for r in ctr_new])
        mc_old = med([r["ctr_pct"] for r in rows if r["ctr_pct"] is not None and r["tuoi"] > 45 and (r["impressions"] or 0) >= 1000])
        if mc_old and mc < 0.7 * mc_old:
            flags.append(f"🔴 CTR video ≤45 ngày (trung vị {mc:.2f} %) < 70 % CTR video cũ có ≥1K lượt hiển thị ({mc_old:.2f} %). Trục yếu nhất = ĐÓNG GÓI.")
    if not ctr_latest or (TODAY - dt.date.fromisoformat(ctr_latest)).days > 8:
        todo.append(f"Tải export Studio mới (Analytics → Nội dung → Xuất) vào `research/` — bản mới nhất kết thúc {ctr_latest or 'chưa có'}.")
    trend_dirs = sorted([p for p in (ROOT / "research" / "trend-us").glob("2026*") if p.is_dir()]) if (ROOT / "research" / "trend-us").exists() else []
    if trend_dirs:
        age = (TODAY - dt.datetime.strptime(trend_dirs[-1].name[:8], "%Y%m%d").date()).days
        if age > 3:
            todo.append(f"Báo cáo trend {trend_dirs[-1].name} đã {age} ngày (>3) — chạy lại `tools/do_trend.py` trước khi chọn đề tài.")
    no_retro = [r for r in rows if r["thu_muc"] and r["tuoi"] >= 7 and not (ROOT / "scripts" / r["thu_muc"] / "retro.md").exists()]
    if no_retro:
        todo.append(f"{len(no_retro)} video ≥7 ngày có retro-auto.md nhưng chưa có bài học trong retro.md — phiên kiểm định viết 3 dòng «học được» cho 3 video mới nhất: "
                    + ", ".join(r["thu_muc"] for r in no_retro[:3]))

    # chấm luật
    L = []
    def add(name, metric, flag_fn, label, higher=True, scope=None):
        rr = [r for r in rows if (scope is None or scope(r))]
        na, ma, nb, mb = cohort(rr, None, metric, flag_fn)
        L.append(f"| {name} | {label} | {na} · {f1(ma)} | {nb} · {f1(mb)} | {verdict(na, ma, nb, mb, higher)} |")
    recent = lambda r: r["tuoi"] <= 180
    add("L21 tiêu đề meta/số trừu tượng", "ctr_pct", lambda r: r["title_meta"] == 0, "CTR % (nhóm KHÔNG meta vs CÓ meta)", scope=recent)
    add("L22 câu hỏi bình luận giữa video", "com_per_1k", lambda r: r["COMMENT_Q"] == 1, "bình luận/1K view", scope=lambda r: r["thu_muc"])
    add("L23 kết ≤20s", "avd_pct", lambda r: r["ENDING_FROM"] == 1, "AVD %", scope=lambda r: r["thu_muc"])
    add("L24 bước đầu ≤45s", "ret_60", lambda r: r["FIRST_STEP"] == 1, "% còn lại @1:00", scope=lambda r: r["thu_muc"])
    add("Độ dài ≤12′", "views_5d", lambda r: (r["phut_thuc"] or 99) <= 12, "views_5d", scope=recent)
    add("Độ dài ≤12′", "ret_60", lambda r: (r["phut_thuc"] or 99) <= 12, "% còn lại @1:00", scope=recent)
    add("Lane B remake", "views_5d", lambda r: r["lane"] == "B", "views_5d (remake vs big-idea)", scope=lambda r: r["thu_muc"])
    add("Lane B remake — cùng kỳ 90 ngày", "views_5d", lambda r: r["lane"] == "B", "views_5d", scope=lambda r: r["thu_muc"] and r["tuoi"] <= 90)
    add("C2 phần tiếp theo catalog", "views_5d", lambda r: r.get("tiep_theo") == 1, "views_5d (tiếp theo vs thường)", scope=lambda r: r["thu_muc"] and r["dang"] >= "2026-11-22")
    add("C3 đường nhanh 1 vòng", "views_5d", lambda r: r.get("nhanh") == 1, "views_5d (1 vòng vs 2 vòng)", scope=lambda r: r["thu_muc"] and r["dang"] >= "2026-11-22")

    md = [f"# Kiểm định kỳ kênh Garden US — {TODAY.isoformat()}",
          "",
          "> `tools/kiem_dinh_ky.py` · 0 credit · số thật YouTube Analytics + export Studio. Đề xuất đổi luật chỉ khi đủ mẫu, và chờ user duyệt.",
          "",
          "## 1. Sức khoẻ (self-baseline)",
          "",
          "| Tuần | Views | AVD % |", "|---|---|---|"]
    md += [f"| {w['week']} | {w['views']:,} | {w['avd_pct']} |" for w in full[-8:]]
    md += ["",
           f"- Trung vị views_5d 10 video gần nhất: **{f1(med5, 0)}** · 5 mới nhất {f1(m5_new, 0)} · 5 trước đó {f1(m5_old, 0)}",
           f"- Traffic 28 ngày: {H.get('traffic_mix', {}).get('current_28d', {})}",
           f"- Catalog: video cũ giữ {cat.get('old_share_pct', '—')} % view",
           "",
           "", "### Catalog đang kéo view (gốc cho phần tiếp theo — C2)", ""]
    def _age(pub):
        try:
            return (TODAY - dt.datetime.strptime(pub, "%b %d, %Y").date()).days
        except ValueError:
            return 0
    cat_rows = sorted([c for c in (ctr or {}).values() if c.get("views_win") and _age(c.get("pub", "")) > 45],
                      key=lambda c: -c["views_win"])[:5]
    md += [f"- {c['title']} · {c['views_win']:,} view trong kỳ export (tới {ctr_latest}) · AVD {c.get('avd_pct')} % · CTR {c['ctr_pct']} % · đăng {c['pub']} · `{c['video_id']}`"
           for c in cat_rows]
    md += ["",
           "## 2. Cờ đỏ", ""] + ([f"- {x}" for x in flags] or ["- Không có."]) + [
           "", "## 3. Video gần nhất", "",
           "| Đăng | Tiêu đề | Phút | views_5d | AVD % | @0:30 | @1:00 | @2:00 | BL/1K | CTR % | Hiển thị |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows[:12]:
        md.append(f"| {r['dang']} | {r['tieu_de'][:48]} | {f1(r['phut_thuc'])} | {f1(r['views_5d'])} | {f1(r['avd_pct'])} | {f1(r['ret_30'])} | "
                  f"{f1(r['ret_60'])} | {f1(r['ret_120'])} | {f1(r['com_per_1k'], 2)} | {f1(r['ctr_pct'], 2)} | {f1(r['impressions'])} |")
    md += ["", "## 4. Chấm luật bằng số của kênh", "",
           "| Luật | Thước | Nhóm áp luật: n · trung vị | Nhóm không: n · trung vị | Kết luận |", "|---|---|---|---|---|"] + L + [
           "",
           "> Luật mới (L22–L24) mới áp từ 22/11/2026 nên nhóm «áp luật» sẽ trống vài tuần. Thăng / hạ cấp luật theo `lessons-learned.md`: ≥3 video cùng hướng.",
           "", "## 5. Việc phải làm tuần này", ""] + ([f"- [ ] {x}" for x in todo] or ["- Không có."]) + [""]
    txt = "\n".join(md)
    (OUT / f"{TODAY:%Y%m%d}.md").write_text(txt, encoding="utf-8")
    (OUT / "latest.md").write_text(txt, encoding="utf-8")
    print(f"✓ báo cáo → research/kiem-dinh-ky/{TODAY:%Y%m%d}.md ({len(flags)} cờ, {len(todo)} việc)")


if __name__ == "__main__":
    main()
