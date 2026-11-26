"""Máy kiểm trùng ĐỀ TÀI — Garden US (thêm 2026-11-08, chép cách làm của kit GohaKit P0 `kiem-de-tai.py`).

Chạy TRƯỚC mọi lệnh vidIQ của Topic Gate / san-y-tuong: không tốn credit, chặn đề tài kênh đã làm
và chỉ ra hit cũ cùng chủ thể (= tín hiệu ① FRANCHISE của Topic Gate).

Lệnh:
    python -X utf8 tools/kiem_de_tai.py lap
        Dựng references/so-de-tai.tsv từ: research/video-5d.json (mọi video long-form đã đăng, có view)
        + scripts/* chưa đăng (đang làm) + research/phieu-kiem-dinh-*.md (verdict san-y-tuong).
        Chạy lại sau `tools/du_bao.py dong-bo`, hoặc khi mở thư mục video mới.
    python -X utf8 tools/kiem_de_tai.py kiem "<đề tài / tiêu đề dự kiến>" [--goc "<góc kể>"] [--chu-the "a,b"]
        In CHẶN / CẢNH BÁO / ĐẠT kèm dòng khớp, và danh sách hit cùng chủ thể (gợi ý phần tiếp).
        Mã thoát: 0 = ĐẠT hoặc CẢNH BÁO · 1 = CHẶN · 2 = lỗi đầu vào (chưa có sổ…).

Luật:
  CHẶN     cùng chủ thể + cùng khung, và dòng đó đăng trong 180 ngày / đang làm;
           hoặc cùng chủ thể + cùng khung với một phiếu NO-GO.
  CẢNH BÁO cùng chủ thể khác khung (làm được nếu đổi góc rõ — ghi trục đổi vào Topic Gate);
           cùng chủ thể + cùng khung nhưng đã > 180 ngày (làm lại = remake nội bộ: phải đổi ≥ 1 trục);
           hoặc tiêu đề giống ≥ 0,6 dù chủ thể khác.
  ĐẠT      không có dòng nào ở trên.
Chủ thể = từ nội dung sau khi bỏ từ chung (plant, grow, garden, winter…). Khi máy tách sai, truyền --chu-the.
"""
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SO = ROOT / "references" / "so-de-tai.tsv"
VID = ROOT / "research" / "video-5d.json"
MAP = ROOT / "research" / "thu-muc-video.tsv"
COLS = ["ma", "nguon", "trang_thai", "ngay", "de_tai", "chu_the", "khung", "views_5d", "views", "lien_ket"]
RECENT_DAYS = 180

STOP = set("""the a an and or of to in on for with your you this that it is are how why what my i at by from do does
dont don't not no just now next can will be its it's into than then these those them they their our we us all any
every one ever never more most less much very really actually only even still yet before after again here there
this that s t isn won wont without keep keeps keeping alive sell profitable giant forgotten exact
watch until yet pull can't cant doesn't use using make makes made do done get gets thing things way ways
""".split())
GENERIC = set("""plant plants planting planted grow grows growing grown garden gardens gardening gardener gardeners
home house indoor indoors outdoor outside inside pot pots potted container containers yard backyard soil water watering
winter fall autumn spring summer season seasonal year years week weeks day days month months time tip tips trick tricks
secret secrets easy simple best worst free cheap cost budget fast faster quick quickly lazy guide step steps fix
mistake mistakes reason reasons truth science study tested ranked method methods hack hacks better instead stop try
over senior seniors elderly grandma grandmother grandma's old fashioned gardening60 zone zones kitchen store bought
full whole head bulb huge big small tiny new first last live lives living alive dying dead die kill kills save
bloom blooms blooming flower flowers flowering harvest harvests fruit fruits leaf leaves root roots rooting
cutting cuttings regrow regrows propagate propagating propagation clone scrap scraps seed seeds pit pits overwinter
overwintering frost freeze cold drop drops dropping hardwood softwood method rescue revive""".split())
# Từ chỉ KHUNG (cách làm) — không tính là chủ thể; dùng để đo "cùng khung" ở FRAMES.
MONTHS = "january february march april may june july august september october november december".split()

FRAMES = [  # (khung, mẫu regex) — thứ tự = ưu tiên
    ("cuu-cay", r"dying|save|rescue|revive|won'?t|isn'?t|not (?:bloom|grow|flower)|struggl|rot|yellow|brown|drop|why your|mistake|wrong"),
    ("nhan-giong", r"cutting|propagat|from (?:seed|scraps|a pit)|regrow|clone|split|divid|rooting|root (?:it|them)|seed"),
    ("qua-dong", r"overwinter|winter|frost|bring (?:it|them) inside|cold|freez"),
    ("kiem-chung", r"truth|myth|study|science|ranked|tested|really|actually work"),
    ("danh-sach", r"^\s*\d+\s|\b\d+ (?:plants|things|vegetables|herbs|perennials|crops|weeds|houseplants)"),
    ("ra-hoa", r"bloom|flower"),
    ("thu-hoach", r"harvest|grow (?:a|your|food)|yield|fruit"),
    ("tiet-kiem", r"\$|free|never buy|cheap|budget|cost"),
]


def words(t):
    return [w for w in re.findall(r"[a-z][a-z'’]+", (t or "").lower().replace("’", "'"))]


def chu_the(t):
    ws = [w.strip("'") for w in words(t)]
    out = []
    for w in ws:
        if w.endswith("oes") and len(w) > 5:
            b = w[:-2]
        elif w.endswith("ies") and len(w) > 5:
            b = w[:-3] + "y"
        elif w.endswith("s") and len(w) > 4 and not w.endswith(("ss", "us", "is")):
            b = w[:-1]
        else:
            b = w
        if b in STOP or w in STOP or b in GENERIC or w in GENERIC or b in MONTHS or len(b) < 3:
            continue
        if b not in out:
            out.append(b)
    return out


def khung(t):
    low = (t or "").lower()
    for name, pat in FRAMES:
        if re.search(pat, low):
            return name
    return "khac"


def sim(a, b):
    A, B = set(chu_the(a)) | set(words(a)) - STOP, set(chu_the(b)) | set(words(b)) - STOP
    return len(A & B) / max(1, min(len(A), len(B))) if A and B else 0.0


# ---------- lap ----------
def lap():
    if not VID.exists():
        print("⚠️ chưa có research/video-5d.json — chạy `python -X utf8 tools/du_bao.py dong-bo --so 200` trước")
        sys.exit(2)
    vids = json.loads(VID.read_text(encoding="utf-8"))["videos"]
    fmap = {}
    if MAP.exists():
        fmap = {r["thu_muc"]: r["video_id"] for r in csv.DictReader(MAP.open(encoding="utf-8"), delimiter="\t")}
    published_ids = {v["videoId"] for v in vids}
    rows = []
    for v in vids:
        if v["privacy"] != "public":
            continue
        rows.append({"ma": v["videoId"], "nguon": "video", "trang_thai": "da-dang", "ngay": v["published"],
                     "de_tai": v["title"], "chu_the": ",".join(chu_the(v["title"])), "khung": khung(v["title"]),
                     "views_5d": v["views_5d"] if not v["partial"] else "", "views": v.get("views") or "",
                     "lien_ket": next((f for f, i in fmap.items() if i == v["videoId"]), "")})
    sys.path.insert(0, str(ROOT / "tools"))
    from du_bao import folder_titles  # dùng lại cách lấy tiêu đề thư mục
    for d in sorted((ROOT / "scripts").iterdir()):
        if not d.is_dir() or not (d / "pipeline-state.md").exists():
            continue
        if fmap.get(d.name) in published_ids:
            continue
        ts = folder_titles(d)
        title = ts[0] if ts else d.name.split("-", 3)[-1].replace("-", " ")
        slug = re.sub(r"^(big-idea|remake|outline|content-plan|video)-[\dv]*-?", "", d.name).replace("-", " ")
        rows.append({"ma": d.name, "nguon": "thu-muc", "trang_thai": "dang-lam",
                     "ngay": dt.date.fromtimestamp((d / "pipeline-state.md").stat().st_mtime).isoformat(),
                     "de_tai": title, "chu_the": ",".join(chu_the(slug + " " + title)), "khung": khung(slug + " " + title),
                     "views_5d": "", "views": "", "lien_ket": d.name})
    for p in sorted((ROOT / "research").glob("phieu-kiem-dinh-*.md")):
        txt = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"verdict[^\n]{0,200}", txt, re.I)
        v = (m.group(0) if m else "").upper()
        st = "no-go" if "NO-GO" in v and "GO CÓ" not in v else ("sua-goc" if "SỬA GÓC" in v else ("go" if "GO" in v else "?"))
        mm = re.match(r"phieu-kiem-dinh-(.+)-(\d{4}-\d{2}-\d{2})\.md", p.name)
        topic = (mm.group(1) if mm else p.stem).replace("-", " ")
        h1 = re.search(r"^#\s+(.+)$", txt, re.M)
        rows.append({"ma": p.name, "nguon": "phieu", "trang_thai": st, "ngay": mm.group(2) if mm else "",
                     "de_tai": (h1.group(1) if h1 else topic)[:120], "chu_the": ",".join(chu_the(topic)),
                     "khung": khung(topic + " " + (h1.group(1) if h1 else "")), "views_5d": "", "views": "",
                     "lien_ket": "research/" + p.name})
    with SO.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, COLS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    by = {}
    for r in rows:
        by[r["nguon"]] = by.get(r["nguon"], 0) + 1
    print(f"✓ {SO.relative_to(ROOT)}: {len(rows)} dòng · " + " · ".join(f"{k} {n}" for k, n in by.items()))


# ---------- kiem ----------
_ROWS, _BODIES = None, None


def _rows():
    global _ROWS
    if _ROWS is None:
        if not SO.exists():
            print("⚠️ chưa có references/so-de-tai.tsv — chạy `kiem_de_tai.py lap`")
            sys.exit(2)
        _ROWS = list(csv.DictReader(SO.open(encoding="utf-8"), delimiter="\t"))
    return _ROWS


def _bodies():
    global _BODIES
    if _BODIES is None:
        _BODIES = {sp.parent.name: sp.read_text(encoding="utf-8", errors="replace").lower().split("## tts script", 1)[-1]
                   for sp in (ROOT / "scripts").glob("*/script.md")}
    return _BODIES


def danh_gia(de_tai, goc="", ct_arg=""):
    """Chấm 1 đề tài với sổ — trả dict (dùng lại được từ tools/sinh_y.py)."""
    rows = _rows()
    text = f"{de_tai} {goc}".strip()
    ct = [x.strip().lower() for x in ct_arg.split(",") if x.strip()] or chu_the(de_tai)
    kh = khung(text)
    today = dt.date.today()
    chan, canh, hit = [], [], []
    for r in rows:
        rct = set(r["chu_the"].split(",")) - {""}
        same_ct = len(set(ct) & rct) >= max(1, len(ct) - len(ct) // 3)  # 1→1 · 2→2 · 3→2 (sweet potato ≠ potato water; christmas tree ≠ lemon tree)
        same_kh = r["khung"] == kh and kh != "khac"
        s = sim(text, r["de_tai"])
        try:
            age = (today - dt.date.fromisoformat(r["ngay"])).days if r["ngay"] else 9999
        except ValueError:
            age = 9999
        tag = f"[{r['nguon']}·{r['trang_thai']}·{r['khung']}] {r['ngay']} {r['de_tai'][:80]}"
        if r["views"]:
            tag += f" · {int(r['views']):,} view" + (f" (5 ngày {r['views_5d']})" if r["views_5d"] else "")
        if same_ct and r["nguon"] in ("video", "thu-muc") and age <= 30:
            chan.append((s, tag + f" — cùng chủ thể, mới {age} ngày: tránh ăn view của nhau"))
        elif same_ct and same_kh and (r["trang_thai"] in ("dang-lam", "no-go") or (r["nguon"] == "video" and age <= RECENT_DAYS)):
            chan.append((s, tag))
        elif same_ct and same_kh:
            canh.append((s, tag + f" — cùng khung, đã {age} ngày: làm lại phải đổi ≥ 1 trục"))
        elif same_ct:
            canh.append((s, tag + " — cùng chủ thể, khác khung"))
        elif s >= 0.6:
            canh.append((s, tag + f" — tiêu đề giống {s:.2f}"))
        if (same_ct or (same_kh and s >= 0.4)) and r["nguon"] == "video" and r["views"] and int(r["views"]) >= 5000:
            hit.append((int(r["views"]), tag))
    sau = []
    if ct:  # chủ thể đã nằm sâu trong lời đọc (một chương của video khác) — tiêu đề không lộ ra
        for name, t in _bodies().items():
            hits = [len(re.findall(r"\b" + re.escape(c) + r"s?\b", t)) for c in ct]
            n = sum(hits)
            if n >= 5 and sum(h > 0 for h in hits) >= max(1, len(ct) - len(ct) // 3):
                sau.append((n, name))
    verdict = "CHẶN" if chan else ("CẢNH BÁO" if (canh or sau) else "ĐẠT")
    return {"chu_the": ct, "khung": kh, "so_dong": len(rows), "chan": sorted(chan, key=lambda x: -x[0]),
            "canh": sorted(canh, key=lambda x: -x[0]), "hit": sorted(hit, reverse=True),
            "sau": sorted(sau, reverse=True), "verdict": verdict}


def kiem(de_tai, goc="", ct_arg=""):
    g = danh_gia(de_tai, goc, ct_arg)
    print(f"Đề tài: {de_tai}" + (f"  · góc: {goc}" if goc else ""))
    print(f"Chủ thể: {', '.join(g['chu_the']) or '(không tách được — truyền --chu-the)'} · khung: {g['khung']} · sổ: {g['so_dong']} dòng\n")
    for name, lst in (("🔴 CHẶN", g["chan"]), ("🟡 CẢNH BÁO", g["canh"])):
        if lst:
            print(name)
            for _, t in lst[:12]:
                print("   ", t)
            print()
    if g["hit"]:
        print("⭐ HIT CÙNG CHỦ THỂ (≥ 5.000 view) — tín hiệu ① FRANCHISE, cân nhắc làm phần tiếp:")
        for v, t in g["hit"][:5]:
            print("   ", t)
        print()
    if g["sau"]:
        print("📖 CHỦ THỂ ĐÃ CÓ TRONG LỜI ĐỌC (≥ 5 lần nhắc — có thể là một chương):")
        for n, f in g["sau"][:5]:
            print(f"    {f}: {n} lần")
        print()
    print(f"KẾT QUẢ: {g['verdict']}")
    if g["chan"]:
        print("→ Đổi chủ thể, hoặc đổi KHUNG rõ ràng (cứu cây ↔ nhân giống ↔ qua đông ↔ kiểm chứng…) rồi kiểm lại. "
              "Không lách bằng từ đồng nghĩa.")
    sys.exit(1 if g["chan"] else 0)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("lap", "kiem"):
        raise SystemExit(__doc__)
    if a[0] == "lap":
        lap()
    else:
        if len(a) < 2:
            raise SystemExit(__doc__)
        opt = lambda k: a[a.index(k) + 1] if k in a else ""
        kiem(a[1], opt("--goc"), opt("--chu-the"))
