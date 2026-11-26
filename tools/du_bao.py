"""Khép vòng dự báo chọn đề tài — Garden US (thêm 2026-11-08).

Vì sao: sổ dự báo research/du-bao.csv có verdict + P(thắng) nhưng chưa dòng nào có kết quả thật,
nên không biết Topic Gate / san-y-tuong có chọn đúng hay không. Tool này lấy views_5d thật từ
YouTube Analytics của chính kênh (OAuth sẵn có của tools/yt_analytics.py — không tốn credit vidIQ).

Lệnh:
    python -X utf8 tools/du_bao.py dong-bo [--so 200]
        Lấy N video long-form mới nhất của kênh + views_5d (ngày đăng .. +4, giống `yt_analytics health`)
        → research/video-5d.json. Ghép thư mục scripts/* ↔ video theo tiêu đề
        → research/thu-muc-video.tsv (dòng nguon=tay được giữ nguyên; sửa tay khi ghép sai).
    python -X utf8 tools/du_bao.py dien
        Điền ngay_dang, views_5d, thang_thua vào research/du-bao.csv cho mọi dòng đã đủ 5 ngày
        (theo link_video, hoặc cột thu_muc qua bảng ghép). Sao lưu .bak-<ngày> trước khi ghi.
    python -X utf8 tools/du_bao.py cong
        Bảng hiệu chỉnh: phán quyết Topic Gate (pipeline-state.md) và verdict san-y-tuong ↔ views_5d thật
        → research/hieu-chinh-cong.md. Đủ ≥5 dòng sổ có kết quả thì chạy luôn Brier của san-y-tuong.
    python -X utf8 tools/du_bao.py tat-ca      (= dong-bo → dien → cong)

Ngưỡng thắng: cột nguong_thang_view của từng dòng; thiếu thì 1,5 × trung vị views_5d 10 video gần nhất.
"""
import csv
import datetime as dt
import json
import re
import shutil
import statistics
import time
import subprocess
import sys
import urllib.parse
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
RES = ROOT / "research"
LEDGER = RES / "du-bao.csv"
VID_JSON = RES / "video-5d.json"
MAP_TSV = RES / "thu-muc-video.tsv"
REPORT = RES / "hieu-chinh-cong.md"
BRIER = Path.home() / ".claude" / "skills" / "san-y-tuong" / "scripts" / "chi_so.py"
SHORT_MAX_S = 180
STOP = set("the a an and or of to in on for with your you this that it is are how why what my i at by from "
           "do does dont don't not no just now next can will be its it's into than then".split())


def words(t):
    return {w for w in re.findall(r"[a-z0-9]+", (t or "").lower()) if w not in STOP and len(w) > 1}


def sim(a, b):
    A, B = words(a), words(b)
    return len(A & B) / max(1, min(len(A), len(B))) if A and B else 0.0


# ---------- dong-bo ----------
def dong_bo(n=60):
    import yt_analytics as ya  # tự nạp token của kênh; không in giá trị
    access = ya.get_access_token()
    hdr = {"Authorization": "Bearer " + access}
    ch = ya._get(ya.DATA + "/channels?" + urllib.parse.urlencode({"part": "contentDetails", "mine": "true"}), hdr)
    uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, tok = [], None
    while len(ids) < n:
        q = {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}
        if tok:
            q["pageToken"] = tok
        j = ya._get(ya.DATA + "/playlistItems?" + urllib.parse.urlencode(q), hdr)
        ids += [it["contentDetails"]["videoId"] for it in j.get("items", [])]
        tok = j.get("nextPageToken")
        if not tok:
            break
    meta = ya.video_meta(access, ids[:n])
    life = {}
    for i in range(0, len(ids[:n]), 50):
        j = ya._get(ya.DATA + "/videos?" + urllib.parse.urlencode(
            {"part": "statistics", "id": ",".join(ids[i:i + 50])}), hdr)
        life.update({it["id"]: int(it["statistics"].get("viewCount", 0)) for it in j.get("items", [])})
    today = dt.date.today()
    out, loi = [], []
    prev = {}
    if VID_JSON.exists():
        prev = {x["videoId"]: x.get("views_5d") for x in json.loads(VID_JSON.read_text(encoding="utf-8"))["videos"]
                if not x.get("partial")}
    for vid, m in meta.items():
        if m["dur"] <= SHORT_MAX_S:
            continue
        pub = dt.date.fromisoformat(m["published"])
        end = pub + dt.timedelta(days=4)
        partial = end >= today  # Analytics trễ ~1-2 ngày: chỉ chốt khi đã qua hẳn cửa sổ
        j = None
        for lan in range(3):  # Analytics hay trả lỗi im lặng khi gọi dồn: thử lại, giãn dần
            j = ya._analytics_safe(access, ids="channel==MINE", startDate=str(pub), endDate=str(min(end, today)),
                                   dimensions="day", filters="video==" + vid, metrics="views")
            if j is not None:
                break
            time.sleep(2 * (lan + 1))
        v5 = sum(int(r[1]) for r in j.get("rows", [])) if j is not None else None
        if j is None:
            v5 = prev.get(vid)  # API lỗi: giữ số lần trước (views_5d của video đã qua cửa sổ không đổi)
            if v5 is None:
                loi.append(m["title"][:50])
        out.append({"videoId": vid, "title": m["title"], "published": m["published"], "privacy": m["privacy"],
                    "views_5d": v5, "views": life.get(vid), "partial": partial or (today - end).days < 2})
    out.sort(key=lambda x: x["published"], reverse=True)
    pubs = [x for x in out if x["privacy"] == "public" and not x["partial"]]
    full = [x["views_5d"] for x in pubs[:10] if x["views_5d"] is not None]
    med = int(statistics.median(full)) if full else None
    if loi:
        print(f"⚠️ {len(loi)} video không lấy được views_5d sau 3 lần thử: {loi[:5]}")
    if len(full) < 10:
        print(f"⚠️ trung vị chỉ tính trên {len(full)}/10 video gần nhất (thiếu số) — chạy lại `dong-bo`")
    VID_JSON.write_text(json.dumps({"fetched_at": dt.datetime.now().isoformat(timespec="seconds"),
                                    "median_5d_last10": med, "videos": out}, ensure_ascii=False, indent=2),
                        encoding="utf-8")
    print(f"✓ {len(out)} video long-form · trung vị views_5d 10 video gần nhất (đã chốt): {med} → {VID_JSON.name}")
    ghep(out)


def folder_titles(d: Path):
    """Các tiêu đề ứng viên của một thư mục: H1 seo-en, dòng title trong pipeline-state/prediction."""
    ts = []
    for name in ("seo-en.md", "pipeline-state.md", "prediction.md", "outline.md"):
        p = d / name
        if not p.exists():
            continue
        for ln in p.read_text(encoding="utf-8", errors="replace").splitlines()[:400]:
            if (name == "seo-en.md" and ln.startswith("# ")) or re.search(r"title", ln, re.I):
                t = re.sub(r"^#+\s*(SEO Description\s*[—-]\s*)?", "", ln)
                t = re.sub(r"[*`|>]", " ", t)
                if 4 <= len(words(t)) <= 25:
                    ts.append(t.strip())
    return ts


def read_map():
    rows = {}
    if MAP_TSV.exists():
        for r in csv.DictReader(MAP_TSV.open(encoding="utf-8"), delimiter="\t"):
            rows[r["thu_muc"]] = r
    return rows


def ghep(videos):
    old = read_map()
    pub = [v for v in videos if v["privacy"] == "public"]
    cand = []
    for d in sorted((ROOT / "scripts").iterdir()):
        if not d.is_dir() or not (d / "script.md").exists():
            continue
        if old.get(d.name, {}).get("nguon") == "tay":
            continue
        ts = folder_titles(d)
        # Thêm 22/11/2026: video phải đăng SAU khi thư mục ra đời (mtime sớm nhất − 1 ngày).
        # Lỗi cũ: 096 (chưa đăng) bị ghép với video 16/02 → sổ dự báo ghi "thắng" 18K giả.
        born = min((f.stat().st_mtime for f in d.iterdir() if f.is_file()), default=0)
        born_d = (dt.date.fromtimestamp(born) - dt.timedelta(days=1)).isoformat() if born else ""
        for v in pub:
            if born_d and (v.get("published") or "") < born_d:
                continue
            s = max((sim(t, v["title"]) for t in ts), default=0)
            if s >= 0.5:
                cand.append((s, d.name, v))
    cand.sort(key=lambda x: -x[0])
    used_f, used_v = {k for k, r in old.items() if r.get("nguon") == "tay"}, \
        {r["video_id"] for r in old.values() if r.get("nguon") == "tay"}
    new = {k: r for k, r in old.items() if r.get("nguon") == "tay"}
    for s, f, v in cand:
        if f in used_f or v["videoId"] in used_v:
            continue
        used_f.add(f)
        used_v.add(v["videoId"])
        new[f] = {"thu_muc": f, "video_id": v["videoId"], "tieu_de": v["title"], "do_khop": f"{s:.2f}",
                  "nguon": "tu-dong"}
    with MAP_TSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, ["thu_muc", "video_id", "tieu_de", "do_khop", "nguon"], delimiter="\t")
        w.writeheader()
        for k in sorted(new):
            w.writerow(new[k])
    weak = [r for r in new.values() if r["nguon"] == "tu-dong" and float(r["do_khop"]) < 0.7]
    print(f"✓ ghép {len(new)} thư mục ↔ video → {MAP_TSV.name} "
          f"({len(weak)} cặp độ khớp < 0,7 — xem lại; sửa tay thì đổi nguon=tay)")


# ---------- dien ----------
def load_videos():
    if not VID_JSON.exists():
        raise SystemExit("chưa có research/video-5d.json — chạy `dong-bo` trước")
    return json.loads(VID_JSON.read_text(encoding="utf-8"))


def vid_from_link(link):
    m = re.search(r"(?:youtu\.be/|v=|shorts/)([A-Za-z0-9_-]{11})", link or "")
    return m.group(1) if m else None


def dien():
    data = load_videos()
    byid = {v["videoId"]: v for v in data["videos"]}
    fmap = {k: r["video_id"] for k, r in read_map().items()}
    raw = LEDGER.read_text(encoding="utf-8-sig")
    rows = list(csv.DictReader(raw.splitlines()))
    cols = list(rows[0].keys()) if rows else []
    if "thu_muc" not in cols:
        cols.append("thu_muc")
    changed = 0
    for r in rows:
        r.setdefault("thu_muc", "")
        vid = vid_from_link(r.get("link_video")) or fmap.get(r.get("thu_muc", "").strip())
        if not vid:
            print(f"  · chưa có link/thư mục: {r['y_tuong'][:60]}")
            continue
        v = byid.get(vid)
        if not v:
            print(f"  · {vid} không có trong {VID_JSON.name} (tăng --so khi dong-bo)")
            continue
        ngay_dubao = (r.get("ngay") or "").strip()
        if ngay_dubao and (v.get("published") or "") < ngay_dubao:
            # Thêm 22/11/2026: video đăng trước ngày dự báo = ghép nhầm, không chấm.
            print(f"  ⚠️ {r['y_tuong'][:50]}: {vid} đăng {v.get('published')} < ngày dự báo {ngay_dubao} — ghép nhầm, bỏ qua")
            if vid_from_link(r.get("link_video")) == vid and not r.get("_link_tay"):
                for k in ("link_video", "ngay_dang", "views_5d", "thang_thua"):
                    r[k] = ""
            continue
        if not r.get("link_video"):
            r["link_video"] = "https://youtu.be/" + vid
        r["ngay_dang"] = v["published"]
        if v["partial"] or v["views_5d"] is None:
            print(f"  · {r['y_tuong'][:50]}: chưa đủ 5 ngày (tạm {v['views_5d']})")
            continue
        try:
            nguong = float(r.get("nguong_thang_view") or 0) or 1.5 * data["median_5d_last10"]
        except TypeError:
            continue
        r["views_5d"] = str(v["views_5d"])
        try:
            float(r.get("p_thang") or "")
        except ValueError:  # Brier cần P(thắng): dòng không có thì chỉ ghi view, không chấm
            print(f"  · {r['y_tuong'][:50]}: views_5d {v['views_5d']} — không có p_thang, không chấm thắng/thua")
            continue
        r["thang_thua"] = "1" if v["views_5d"] >= nguong else "0"
        changed += 1
        print(f"  ✓ {r['y_tuong'][:50]}: views_5d {v['views_5d']} vs ngưỡng {nguong:.0f} → "
              f"{'THẮNG' if r['thang_thua'] == '1' else 'thua'}")
    bak = LEDGER.with_suffix(f".csv.bak-{dt.date.today()}")
    if not bak.exists():
        shutil.copy2(LEDGER, bak)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, cols)
        w.writeheader()
        w.writerows(rows)
    print(f"✓ cập nhật {changed} dòng có kết quả trong {LEDGER.name}")


# ---------- cong ----------
GATE_RE = re.compile(r"TOPIC GATE\s*[—-]\s*([0-3])/3[^→\n]*→\s*([^(,\n]+)")


def cong():
    data = load_videos()
    byid = {v["videoId"]: v for v in data["videos"]}
    fmap = read_map()
    med = data["median_5d_last10"]
    nguong = round(1.5 * med) if med else None
    rows = []
    for d in sorted((ROOT / "scripts").iterdir()):
        ps = d / "pipeline-state.md"
        if not ps.exists():
            continue
        m = GATE_RE.search(ps.read_text(encoding="utf-8", errors="replace"))
        if not m:
            continue
        v = byid.get(fmap.get(d.name, {}).get("video_id", ""))
        rows.append({"thu_muc": d.name, "so_tin_hieu": m.group(1), "phan_quyet": m.group(2).strip(),
                     "views_5d": None if not v or v["partial"] else v["views_5d"],
                     "tieu_de": v["title"] if v else "(chưa đăng / chưa ghép)"})
    led = list(csv.DictReader(LEDGER.read_text(encoding="utf-8-sig").splitlines())) if LEDGER.exists() else []

    L = [f"# Hiệu chỉnh cổng chọn đề tài — {dt.date.today()}",
         "",
         f"Nguồn: `tools/du_bao.py cong` · số liệu YouTube Analytics lúc {data['fetched_at']}.",
         f"Mốc: trung vị views_5d 10 video gần nhất = **{med}** → ngưỡng thắng 1,5× = **{nguong}**.",
         "",
         "## Topic Gate (pipeline-state.md) ↔ kết quả thật",
         "",
         "| Thư mục | Tín hiệu | Phán quyết | views_5d | So ngưỡng | Video |",
         "|---|---|---|---|---|---|"]
    for r in rows:
        v = r["views_5d"]
        kq = "—" if v is None else ("✅ thắng" if nguong and v >= nguong else ("🟡 ≥ trung vị" if v >= med else "🔴 dưới trung vị"))
        L.append(f"| {r['thu_muc']} | {r['so_tin_hieu']}/3 | {r['phan_quyet']} | {v if v is not None else '—'} | {kq} | {r['tieu_de'][:60]} |")
    L += ["", "### Gộp theo số tín hiệu", "", "| Tín hiệu | n có kết quả | Thắng | Trung vị views_5d |", "|---|---|---|---|"]
    for k in ("3", "2", "1"):
        vs = [r["views_5d"] for r in rows if r["so_tin_hieu"] == k and r["views_5d"] is not None]
        if vs:
            L.append(f"| {k}/3 | {len(vs)} | {sum(nguong is not None and x >= nguong for x in vs)} | {int(statistics.median(vs))} |")
    # Danh mục 3:1 — video đăng gần nhất có thư mục, đọc dòng "HẠNG: CÚ ĐÁNH LỚN" trong pipeline-state.md
    but = round(5 * med) if med else None
    inv = {r["video_id"]: k for k, r in fmap.items()}
    recent = [v for v in data["videos"] if v["privacy"] == "public" and v["videoId"] in inv][:8]
    L += ["", f"## Danh mục 3 an toàn : 1 cú đánh lớn — 8 video gần nhất (bứt ≥ 5× = {but})", "",
          "| Ngày | Hạng | views_5d | Mức | Tiêu đề |", "|---|---|---|---|---|"]
    n_lon = 0
    for v in recent:
        ps = ROOT / "scripts" / inv[v["videoId"]] / "pipeline-state.md"
        txt = ps.read_text(encoding="utf-8", errors="replace") if ps.exists() else ""
        lon = bool(re.search(r"HẠNG:\s*\**\s*CÚ ĐÁNH LỚN", txt, re.I))
        n_lon += lon
        x = None if v["partial"] else v["views_5d"]
        muc = "—" if x is None else ("🚀 bứt" if but and x >= but else ("✅ an toàn" if nguong and x >= nguong else "🔴 dưới"))
        L.append(f"| {v['published']} | {'CÚ ĐÁNH LỚN' if lon else 'an toàn'} | {x if x is not None else '—'} | {muc} | {v['title'][:60]} |")
    L.append(f"\nCú đánh lớn trong 8 video: **{n_lon}** (mục tiêu 2). Ghi `HẠNG: CÚ ĐÁNH LỚN` trong pipeline-state.md khi chọn đề tài.")
    L += ["", "## Sổ dự báo san-y-tuong (research/du-bao.csv)", "",
          "Dòng cột `hang` = `cu-danh-lon` thì `nguong_thang_view` là ngưỡng BỨT (P(thắng) = P(≥ 5× trung vị)).", "",
          "| Ý tưởng | Verdict | P(thắng) | P25–P75 | views_5d | Kết quả |", "|---|---|---|---|---|---|"]
    for r in led:
        tt = r.get("thang_thua", "").strip()
        L.append(f"| {r['y_tuong'][:55]} | {r['verdict']} | {r['p_thang']} | {r['p25']}–{r['p75']} | "
                 f"{r.get('views_5d') or '—'} | {'✅' if tt == '1' else ('🔴' if tt == '0' else 'chờ')} |")
    xong = [r for r in led if r.get("thang_thua", "").strip() in ("0", "1")]
    L += ["", f"Sổ có **{len(xong)}** dòng có kết quả."]
    if len(xong) >= 5 and BRIER.exists():
        p = subprocess.run([sys.executable, "-X", "utf8", str(BRIER), "brier", str(LEDGER)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        L += ["", "## Brier", "", "```", (p.stdout + p.stderr).strip(), "```"]
    else:
        L.append(f"Brier chạy khi đủ 5 dòng (còn thiếu {max(0, 5 - len(xong))}).")
    L += ["", "> Cách đọc: cỡ mẫu nhỏ thì chỉ xem hướng, không đổi ngưỡng. Đề xuất đổi ngưỡng Topic Gate / san-y-tuong",
          "> chỉ khi ≥ 8 video có kết quả, và chờ user duyệt (topic-gate-en.md mục HIỆU CHỈNH)."]
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("dong-bo", "dien", "cong", "tat-ca"):
        raise SystemExit(__doc__)
    n = int(a[a.index("--so") + 1]) if "--so" in a else 200
    if a[0] in ("dong-bo", "tat-ca"):
        dong_bo(n)
    if a[0] in ("dien", "tat-ca"):
        dien()
    if a[0] in ("cong", "tat-ca"):
        cong()
