"""DNA kênh — đo đặc điểm nào của tiêu đề / độ dài thật sự kéo view TRÊN CHÍNH KÊNH NÀY (thêm 2026-11-08).

Chạy mỗi Chủ Nhật sau `tools/du_bao.py dong-bo`. Không tốn credit vidIQ (YouTube Analytics OAuth của kênh).

Lệnh:
    python -X utf8 tools/dna_kenh.py do [--cua-so 90]
        1. Lấy chỉ số trọn đời từng video công khai trong research/video-5d.json: AVD %, giây xem, sub, nguồn lưu lượng
           → research/dna-kenh-data.json (lưu đệm: video đã có số và > 30 ngày tuổi không hỏi lại).
        2. Nhập mọi file export Studio đặt trong research/studio/*.csv (Studio → Analytics → Advanced mode → Content →
           Export → CSV; cần cột Content/Video, Impressions, Impressions click-through rate). API không có 2 cột này.
        3. Tính HỆ SỐ (lift) của từng đặc điểm = trung vị view video CÓ ÷ trung vị video KHÔNG CÓ, trong cùng cửa sổ:
           - cửa sổ gần (N ngày gần nhất, mặc định 90) — kênh lúc này
           - giai đoạn tham chiếu T2–T4/2026 (lúc kênh còn ra outlier) — để biết nguyên liệu outlier là gì
        4. Ghi references/dna-kenh.md (đọc cho người) + references/dna-kenh.json (cho tools/sinh_y.py và san-y-tuong).
Hệ số với n < 3 ở một phía không tính (ghi "—"). Đây là TƯƠNG QUAN, không phải nhân quả: dùng để xếp ưu tiên ý tưởng,
không dùng thay kiểm định.
"""
import csv
import datetime as dt
import json
import math
import re
import statistics as st
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
VID = ROOT / "research" / "video-5d.json"
DATA = ROOT / "research" / "dna-kenh-data.json"
STUDIO = ROOT / "research" / "studio"
OUT_MD = ROOT / "references" / "dna-kenh.md"
OUT_JSON = ROOT / "references" / "dna-kenh.json"
REF = ("2026-02-01", "2026-04-30")  # giai đoạn kênh còn ra outlier

# Đặc điểm tiêu đề — dùng chung với tools/sinh_y.py. Sửa regex ở ĐÂY, không chép sang tool khác.
FEATURES = {
    "dao_niem_tin": ("Đảo niềm tin «Stop / Never … Instead»", r"\b(stop|never)\b|instead"),
    "free_tien": ("Miễn phí / $ / never buy", r"free|\$|cheap|never buy|cost|budget|save money|¢"),
    "do_ai_cung_co": ("Thứ ai cũng có / đang vứt đi",
                      r"weed|scrap|peel|leaves|cardboard|eggshell|coffee ground|ash|water\b|kitchen|grocery|store.bought|pit\b|seed from"),
    "it_cong": ("Ít công (lazy / no soil / no dig / plant once)",
                r"lazy|no soil|no dig|no bending|without bending|zero effort|plant once|never die|just water|no pulling"),
    "danh_sach": ("Danh sách ≥ 5 món", r"^\s*([5-9]|[1-9]\d)\b|\b([5-9]|[1-9]\d)\s+(?:\w+\s){0,2}(plants|things|vegetables|herbs|perennials|weeds|houseplants|crops|flowers|vines|scraps|trees)"),
    "gia_tri_cao": ("Đổi giá trị «most valuable / gold / better than»", r"valuable|gold|better than|beat|worth|secret"),
    "mot_cay": ("Một cây cụ thể (sửa lỗi / chăm một loài)", r"^(?:(?!\b\d+\b).)*\b(your|my|a|one)\s+(\w+\s){0,2}(tree|cactus|orchid|plant|lemon|geranium|garlic|ginger|pineapple|rose|pepper|aloe|basil|snake plant|clematis|hydrangea)\b"),
    "so_hai_mat": ("Sợ / mất (toxic / dying / kill / warning / mistake)", r"toxic|poison|dying|dead|kill|warning|mistake|regret|rot|wrong"),
    "khoa_hoc": ("Khoa học / kiểm chứng / extension", r"science|study|truth|myth|ranked|extension|actually|tested"),
    "mua_thang": ("Tháng / mùa", r"january|february|march|april|may|june|july|august|september|october|november|december|winter|fall|spring|summer|frost"),
    "grandma": ("Bà / folklore", r"grandma|grandmother|old.fashioned"),
}
LEN_BANDS = [(0, 600, "< 10′"), (600, 900, "10–15′"), (900, 1200, "15–20′"), (1200, 10 ** 6, "≥ 20′")]


def has(feat, title):
    return bool(re.search(FEATURES[feat][1], title or "", re.I))


# ---------- 1. lấy số ----------
def fetch(force=False):
    import yt_analytics as ya
    vids = [v for v in json.loads(VID.read_text(encoding="utf-8"))["videos"] if v["privacy"] == "public"]
    old = {r["videoId"]: r for r in json.loads(DATA.read_text(encoding="utf-8"))} if DATA.exists() and not force else {}
    access = ya.get_access_token()
    meta = ya.video_meta(access, [v["videoId"] for v in vids])
    today = dt.date.today()

    def call(**p):
        for i in range(3):
            j = ya._analytics_safe(access, **p)
            if j is not None:
                return j
            time.sleep(2 * (i + 1))
        return None

    out, asked = [], 0
    for v in vids:
        vid = v["videoId"]
        age = (today - dt.date.fromisoformat(v["published"])).days
        o = old.get(vid)
        row = dict(v, dur=meta.get(vid, {}).get("dur"))
        if o and age > 30 and "averageViewPercentage" in o and "src" in o:
            row.update({k: o[k] for k in ("averageViewPercentage", "averageViewDuration", "subscribersGained", "src") if k in o})
            out.append(row)
            continue
        base = dict(ids="channel==MINE", startDate=v["published"], endDate=str(today), filters="video==" + vid)
        a = call(metrics="views,averageViewPercentage,averageViewDuration,subscribersGained", **base)
        t = call(metrics="views", dimensions="insightTrafficSourceType", **base)
        asked += 1
        if a and a.get("rows"):
            cols = [c["name"] for c in a["columnHeaders"]]
            d = dict(zip(cols, a["rows"][0]))
            d.pop("views", None)  # giữ view trọn đời từ Data API (cùng nguồn với sổ đề tài)
            row.update(d)
        if t and t.get("rows"):
            tot = sum(r[1] for r in t["rows"]) or 1
            row["src"] = {r[0]: round(100 * r[1] / tot, 1) for r in t["rows"]}
        out.append(row)
    DATA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"✓ {len(out)} video ({asked} hỏi API, còn lại lấy đệm) → {DATA.relative_to(ROOT)}")
    return out


# ---------- 2. Studio ----------
def num(x):
    try:
        return float(str(x).replace(",", "").replace("%", "").strip())
    except ValueError:
        return None


def studio():
    """{videoId: {impressions, ctr}} từ mọi CSV export Studio; file sau ghi đè file trước (sắp theo tên)."""
    out = {}
    if not STUDIO.exists():
        return out
    for p in sorted(STUDIO.glob("*.csv")):
        rows = list(csv.DictReader(p.read_text(encoding="utf-8-sig").splitlines()))
        if not rows:
            continue
        keys = rows[0].keys()
        kid = next((k for k in keys if k.strip().lower() in ("content", "video", "video id")), None)
        # Studio ghi "Impressions" hoặc "Thumbnail impressions" tuỳ bản; CTR là "…click-through rate (%)"
        kimp = next((k for k in keys if "impressions" in k.lower() and "click" not in k.lower()), None)
        kctr = next((k for k in keys if "click-through" in k.lower()), None)
        kpub = next((k for k in keys if "publish" in k.lower()), None)
        if not (kid and kimp):
            print(f"  · bỏ qua {p.name}: không thấy cột Content/Impressions")
            continue
        m = re.search(r"(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})", p.name)  # cửa sổ export, đặt trong tên file
        start = m.group(1) if m else None
        for r in rows:
            vid = (r.get(kid) or "").strip()
            if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
                continue
            pub = None
            try:
                pub = dt.datetime.strptime((r.get(kpub) or "").strip(), "%b %d, %Y").date().isoformat()
            except ValueError:
                pass
            out[vid] = {"impressions": num(r.get(kimp)), "ctr": num(r.get(kctr)) if kctr else None, "file": p.name,
                        # True = video đăng trong cửa sổ export → impressions ≈ trọn đời (đo được mẻ hiển thị đầu)
                        "studio_tron_doi": bool(start and pub and pub >= start)}
    return out


# ---------- 3. hệ số ----------
def lift(rows, feat, key="views"):
    y = [r[key] for r in rows if r.get(key) is not None and has(feat, r["title"])]
    n = [r[key] for r in rows if r.get(key) is not None and not has(feat, r["title"])]
    if len(y) < 3 or len(n) < 3:
        return None, len(y)
    my, mn = st.median(y), st.median(n)
    return (round(my / mn, 2) if mn else None), len(y)


def do(cua_so=90):
    rows = fetch()
    stu = studio()
    for r in rows:
        r.update(stu.get(r["videoId"], {}))
    today = dt.date.today()
    since = str(today - dt.timedelta(days=cua_so))
    recent = [r for r in rows if r["published"] >= since and not r.get("partial")]
    ref = [r for r in rows if REF[0] <= r["published"] <= REF[1]]
    five = [r["views_5d"] for r in sorted(recent, key=lambda r: r["published"], reverse=True)
            if r.get("views_5d") is not None][:10]
    med5 = st.median(five) if five else None
    res = {"ngay": str(today), "cua_so_ngay": cua_so, "n_gan": len(recent), "n_tham_chieu": len(ref),
           "trung_vi_5d_10_gan": med5,
           "nguong": {"an_toan_5d": round(1.5 * med5) if med5 else None, "but_5d": round(5 * med5) if med5 else None},
           "duoi_phai": {}, "dac_diem": {}, "do_dai": {}, "studio": {}}
    for name, L in (("gan", recent), ("tham_chieu", ref)):
        lv = [r["views"] for r in L if r.get("views") is not None]
        m = st.median(lv) if lv else 0
        res["duoi_phai"][name] = {"trung_vi_view": m, "ty_le_ge_3x": round(sum(v >= 3 * m for v in lv) / len(lv), 2) if lv else None,
                                  "so_ge_5000": sum(v >= 5000 for v in lv)}
    for f, (label, _) in FEATURES.items():
        lg, ng = lift(recent, f, "views_5d")
        lr, nr = lift(ref, f, "views")
        res["dac_diem"][f] = {"ten": label, "he_so_gan": lg, "n_gan": ng, "he_so_tham_chieu": lr, "n_tham_chieu": nr}
    for name, L, key in (("gan", recent, "views_5d"), ("tham_chieu", ref, "views")):
        for lo, hi, lab in LEN_BANDS:
            x = [r for r in L if r.get("dur") and lo <= r["dur"] < hi]
            if len(x) >= 2:
                res["do_dai"].setdefault(lab, {})[name] = {
                    "n": len(x), "trung_vi": st.median([r[key] for r in x if r.get(key) is not None] or [0]),
                    "avd": round(st.median(r.get("averageViewPercentage") or 0 for r in x), 1),
                    "giay_xem": round(st.median(r.get("averageViewDuration") or 0 for r in x))}
    si = [r for r in rows if r.get("studio_tron_doi") and r.get("impressions")]  # video mới: impressions ≈ trọn đời
    cat = [r for r in rows if r.get("impressions") and not r.get("studio_tron_doi") and r["published"] < REF[1]]
    if si:
        res["studio"] = {
            "n": len(si), "trung_vi_impressions": st.median(r["impressions"] for r in si),
            "trung_vi_ctr": st.median(r["ctr"] for r in si if r.get("ctr") is not None),
            "ctr_catalog_cu": round(st.median(r["ctr"] for r in cat if r["impressions"] >= 1000 and r.get("ctr") is not None), 2)
            if any(r["impressions"] >= 1000 for r in cat) else None,
            "video": [{"ngay": r["published"], "impressions": r["impressions"], "ctr": r["ctr"], "views": r.get("views"),
                       "avd": r.get("averageViewPercentage"), "dai_phut": round((r.get("dur") or 0) / 60), "title": r["title"]}
                      for r in sorted(si, key=lambda r: r["published"])]}
        # Hệ số đặc điểm trên CTR (video mới trong cửa sổ Studio) — gói có kéo người xem lạnh không
        for f in FEATURES:
            y = [r["ctr"] for r in si if has(f, r["title"]) and r.get("ctr") is not None]
            n = [r["ctr"] for r in si if not has(f, r["title"]) and r.get("ctr") is not None]
            res["dac_diem"][f]["he_so_ctr_moi"] = round(st.median(y) / st.median(n), 2) if len(y) >= 2 and len(n) >= 2 and st.median(n) else None
    subs = sum(r.get("subscribersGained") or 0 for r in recent)
    res["sub_tu_video_gan"] = subs
    OUT_JSON.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    write_md(res, recent)
    print(f"✓ {OUT_MD.relative_to(ROOT)} · {OUT_JSON.relative_to(ROOT)}")


def f2(x):
    return "—" if x is None else f"×{x:.2f}"


def write_md(res, recent):
    d, dp = res["dac_diem"], res["duoi_phai"]
    L = [f"# DNA kênh — {res['ngay']}", "",
         f"Máy ghi: `python -X utf8 tools/dna_kenh.py do` · cửa sổ gần {res['cua_so_ngay']} ngày ({res['n_gan']} video) · "
         f"tham chiếu T2–T4/2026 ({res['n_tham_chieu']} video, lúc kênh còn ra outlier).", "",
         "## Hai mức thắng", "",
         f"- Trung vị views_5d 10 video gần nhất: **{res['trung_vi_5d_10_gan']}**",
         f"- **An toàn** ≥ 1,5× = **{res['nguong']['an_toan_5d']}** views_5d · **Bứt** ≥ 5× = **{res['nguong']['but_5d']}** views_5d",
         "", "| | Trung vị view trọn đời | Tỉ lệ video ≥ 3× trung vị | Video ≥ 5.000 |", "|---|---|---|---|",
         f"| Gần | {dp['gan']['trung_vi_view']:.0f} | {dp['gan']['ty_le_ge_3x']} | {dp['gan']['so_ge_5000']} |",
         f"| Tham chiếu | {dp['tham_chieu']['trung_vi_view']:.0f} | {dp['tham_chieu']['ty_le_ge_3x']} | {dp['tham_chieu']['so_ge_5000']} |",
         "", f"Sub từ các video trong cửa sổ gần: **{res['sub_tu_video_gan']}**.", "",
         "## Hệ số đặc điểm tiêu đề", "",
         "Hệ số = trung vị view video có đặc điểm ÷ video không có, cùng cửa sổ (gần: views_5d · tham chiếu: view trọn đời). "
         "`—` = một phía < 3 video.", "",
         "| Đặc điểm | Gần (n có) | Tham chiếu (n có) |", "|---|---|---|"]
    for f, x in sorted(d.items(), key=lambda kv: -(kv[1]["he_so_tham_chieu"] or 0)):
        L.append(f"| {x['ten']} | {f2(x['he_so_gan'])} ({x['n_gan']}) | {f2(x['he_so_tham_chieu'])} ({x['n_tham_chieu']}) |")
    L += ["", "## Độ dài", "", "| Dải | Gần: n · trung vị 5d · AVD · giây xem | Tham chiếu: n · trung vị view · AVD · giây xem |", "|---|---|---|"]
    for lab, x in res["do_dai"].items():
        g, t = x.get("gan"), x.get("tham_chieu")
        fmt = lambda y: "—" if not y else f"{y['n']} · {y['trung_vi']:.0f} · {y['avd']}% · {y['giay_xem']}s"
        L.append(f"| {lab} | {fmt(g)} | {fmt(t)} |")
    L += ["", "## Impressions / CTR (Studio)", ""]
    if res["studio"]:
        s = res["studio"]
        L.append(f"Video đăng trong cửa sổ export ({s['n']} video, impressions ≈ trọn đời): trung vị impressions "
                 f"**{s['trung_vi_impressions']:.0f}** · CTR **{s['trung_vi_ctr']}%** · CTR catalog cũ (trước T5, ≥ 1.000 impressions) "
                 f"**{s['ctr_catalog_cu']}%**.")
        L += ["", "| Ngày | Impressions | CTR | View | AVD | Dài | Tiêu đề |", "|---|---|---|---|---|---|---|"]
        for v in s["video"]:
            L.append(f"| {v['ngay']} | {v['impressions']:.0f} | {v['ctr']}% | {v['views']} | {round(v['avd'] or 0)}% | "
                     f"{v['dai_phut']}′ | {v['title'][:60]} |")
        L += ["", "Đọc: impressions cao + CTR thấp = YouTube **đã thử mở rộng** sang người xem lạnh nhưng gói không kéo được → "
              "sửa gói (tiêu đề + thumbnail). Impressions thấp + CTR khá = chưa được thử → tín hiệu sớm (AVD, giây xem) yếu."]
        ctrs = [(x["ten"], x.get("he_so_ctr_moi")) for x in res["dac_diem"].values() if x.get("he_so_ctr_moi")]
        if ctrs:
            L += ["", "Hệ số CTR theo đặc điểm (video mới, n rất nhỏ — chỉ xem hướng): " +
                  " · ".join(f"{t} ×{v:.2f}" for t, v in sorted(ctrs, key=lambda kv: -kv[1]))]
    else:
        L.append("Chưa có. Đặt file export Studio (Content, Impressions, Impressions click-through rate) vào `research/studio/` "
                 "rồi chạy lại — đây là chỗ đo được video có ra khỏi mẻ hiển thị đầu hay không.")
    L += ["", "## Video gần đây", "", "| Ngày | views_5d | Trọn đời | Dài | AVD | Đặc điểm | Tiêu đề |", "|---|---|---|---|---|---|---|"]
    for r in sorted(recent, key=lambda r: r["published"], reverse=True)[:15]:
        tags = ",".join(k for k in FEATURES if has(k, r["title"]))
        L.append(f"| {r['published']} | {r.get('views_5d')} | {r.get('views')} | {round((r.get('dur') or 0) / 60)}′ | "
                 f"{round(r.get('averageViewPercentage') or 0)}% | {tags} | {r['title'][:55]} |")
    L += ["", "> Tương quan, không phải nhân quả. Dùng để xếp ưu tiên ý tưởng (`tools/sinh_y.py`) và làm căn cứ cho hệ số khớp "
          "của `/san-y-tuong`; không thay kiểm định."]
    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] != "do":
        raise SystemExit(__doc__)
    do(int(a[a.index("--cua-so") + 1]) if "--cua-so" in a else 90)
