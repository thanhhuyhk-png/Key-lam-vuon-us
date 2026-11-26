"""Dò trend kênh Garden US: video dài đang lên trong ngách (10 ngày), trend mùa (cùng kỳ năm ngoái), đà view kênh.

Một đường tìm chủ đề duy nhất của kênh (thay R0 radar seed vidIQ `vph` và trend-radar chạy tay, đã cất 18/11/2026).
Kết quả dùng cho TOPIC GATE ② (references/topic-gate-en.md) và từ khoá tiêu đề (references/title-keyword-strategy-en.md).

Dùng:
  python -X utf8 tools/do_trend.py --out-dir research/trend-us/<YYYYMMDD> \
      --ds research/trend-us/kenh-ngach.txt --video-dir research/top20-<ngày>/thu-video \
      [--tim "christmas cactus,fall leaves"] [--ngay 10] [--so-moi 12] [--hom-nay YYYY-MM-DD] [--offline]
  --ds        mỗi dòng '<kênh>' hoặc '<tên><TAB><kênh>' (UC…, @handle, URL); dòng '#' bị bỏ. Chỉ để kênh LÕI làm vườn.
  --tim       cụm tìm (dấu phẩy): video đăng tháng này theo cụm, để bắt cả kênh ngoài danh sách.
  --video-dir TSV của thu_video.py (lần đo top 20): nền view của kênh + kho cho lớp trend mùa.
  --offline   không gọi yt-dlp, chỉ chấm từ --video-dir (thử trên số cũ, kèm --hom-nay).

1) Trend 10 ngày (nhãn [ƯỚC] khi chỉ có một lần chụp):
   he_so_tre = view ÷ (nền kênh × f(tuổi)),  f(t) = clamp((t/30)^0,4; 0,25; 1)
   nền kênh  = trung vị view video dài 30–365 ngày tuổi (cần ≥ 5; thiếu thì sub × 0,8, nguồn «sub» — đọc kèm view tuyệt đối).
   Có ảnh chụp lần trước (≥ 2 ngày) thì có cột view_tang_moi_ngay [ĐO] thật — ưu tiên cột này.
   Mức: ≥ 5 rất nóng · 3–5 nóng · 2–3 lên · < 2 thường.
2) Trend mùa (cùng kỳ năm ngoái): video dài đăng từ (hôm nay − 365 − 14) đến (hôm nay − 365 + 42) ngày,
   he_so_mua = view ÷ trung vị view video dài 180–730 ngày tuổi của cùng kênh. Cửa sổ lệch về phía trước để kịp
   đăng trước đỉnh mùa 2–4 tuần.
Từ khoá: cụm 1–3 từ nội dung trong tiêu đề (bỏ từ dừng, từ câu view, nhãn tuổi — chỉ giữ CHỦ THỂ: cây, vật, việc làm).
   Trend khi có trong video hệ số ≥ 2 của ≥ 2 kênh; ≥ 3 kênh = cờ ĐA_KENH. «Độ nổi» = tỉ lệ ở video nóng ÷ tỉ lệ ở mọi video.
   ĐA_KENH chưa chắc là cơ hội: xem «so_video_nong / so_video_tat_ca» — nhiều kênh làm mà phần lớn bản không nóng
   = bão hoà (cổng ⓑ).
Đà kênh: da_view_60 = trung vị (view ÷ f(tuổi)) video 7–60 ngày ÷ nền kênh. Không có video dài 60 ngày: cờ NGUNG.

Nâng cấp 22/11/2026 (chép từ skill GohaKit rieng-tu-duy-top-20-ytb, references/do-trend-ngach-moi.md; chỉnh cho vườn):
   - Nền «sub» (kênh lạ thiếu video): trần hệ số TRAN_SUB = 10, dưới VIEW_MIN_SUB = 5.000 view thì không được ≥ 2.
   - Video trẻ < TRE_GIO = 48 giờ: dưới TRE_VIEW_MIN = 500 view thì không được ≥ 2 (Prepare Pantry 32 view ra 2,5).
   - Bỏ tiêu đề không phải tiếng Anh (RE_KHONG_ANH); lọc lạc ngách thêm đồ khô / mất điện / dự trữ.
   - Từ đơn mùa, vật chung (winter, cold, food, vegetable…) chỉ được nằm trong cụm (TU_DON): «winter sowing» được.
   - Gộp tên gọi: thanksgiving / holiday cactus → christmas cactus; usda zone → zone.
   - vph_tb = view ÷ giờ từ lúc đăng (bỏ video < 6 giờ); vph_do = tăng view ÷ giờ giữa hai lần chụp (≥ 12 giờ).
     Đọc cặp: vph_do ≫ vph_tb là tăng tốc; vph_do ≪ vph_tb là qua đỉnh. VPH tuyệt đối thiên kênh lớn: đọc cùng hệ số.
   - --goi-y: gợi ý tìm kiếm YouTube US (miễn phí) cho từ khoá trend + trend mùa; chỉ đếm gợi ý có ngữ cảnh vườn.
   - --lich research/trend-us/lich-vuon-us.tsv: mốc mùa vụ US trong --lich-ngay (45) ngày tới; làm phim dài khi còn 21–45 ngày.
   - Cờ YMYL (chữa bệnh, detox…) → chỉ theo dõi, đi luật YMYL của pipeline; OFF_NICHE (đồ khô, dự trữ).
   - --nap-meta <out-dir cũ>/meta-video.jsonl: chấm lại không tải lại (để chỉnh bộ lọc); không ghi ảnh chụp.

Đầu ra --out-dir: bao-cao-trend.md, trend-video.tsv, trend-tu-khoa.tsv, trend-mua.tsv, trend-mua-tu-khoa.tsv,
trend-kenh.tsv, meta-video.jsonl; ảnh chụp <out-dir>/../anh-chup/<ngày>.json. Thư viện chuẩn + yt-dlp. Không cookie, 0 credit.
Gốc: bản kênh JP (GohaKit-JP rieng-tu-duy-top-20-ytb/scripts/do_trend.py), đổi bộ tách từ sang tiếng Anh, thêm trend mùa.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import statistics as st
import subprocess
import sys
import time
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

HE_MU = 0.4
SAN_F = 0.25
TUOI_NEN = (30, 365)
TUOI_NEN_MUA = (180, 730)
MUA_TRUOC, MUA_SAU = 14, 42
MUA_VIEW_TOI_THIEU = 1000   # video mùa dưới 1.000 view là nhiễu (nền kênh nhỏ làm hệ số ảo)
NEN_TOI_THIEU = 5
HE_SO_SUB = 0.8
TRAN_SUB = 10.0          # trần hệ số khi nền lấy theo sub
VIEW_MIN_SUB = 5000      # nền sub: dưới mức này không được tính là video đang lên (kênh vườn nhỏ hơn kênh quân sự)
TRE_GIO = 48             # video trẻ hơn số giờ này…
TRE_VIEW_MIN = 500       # …mà dưới số view này thì không được tính là video đang lên
VIEW_MIN_LEN = 300       # mọi video: dưới số view này không được tính là đang lên (kênh nền vài chục view là nhiễu)
VPH_TUOI_TOI_THIEU = 6   # giờ: video trẻ hơn thì vph_tb quá nhiễu, để trống
VPH_GIO_TOI_THIEU = 12   # giờ: hai lần chụp cách nhau ít hơn thì không tính vph_do
LO = 25
TIMEOUT = 1500
MUC = [(5, "rat_nong"), (3, "nong"), (2, "len"), (0, "thuong")]
DUMP = "%(.{id,timestamp,upload_date,duration,view_count,like_count,comment_count,title,channel_id,channel,uploader,channel_follower_count})j"
SP_THANG_NAY = "EgQIBBAB"

TU_DUNG = set("""a an the and or but of to in on at for from with by as is are was were be been it its this that these those
you your yours we our us i my me they them their he she his her do does did done can could will would should must may might
not no nor so if then than too very just only also more most less much many any all some every each own same other such
what which who whom whose why how when where here there now ever again still even about into over under up down out off
after before during while until because since without within upon via vs one two three four five six seven eight nine ten
make makes made making get gets got getting use uses using used put puts let lets keep keeps go goes going went know knew
want need needs try tried see seen look looks like work works way ways thing things stuff lot lots really actually
best better good great big small new old first last next right wrong real easy easiest simple fast faster quick quickly
year years day days week weeks month months time times ever never always forever overnight instantly
have has had having am being till top bottom text""".split())
TU_CHUNG = set("""garden gardens gardening gardener gardeners plant plants planting planted grow grows growing grown grower
tip tips trick tricks hack hacks secret secrets idea ideas guide method methods mistake mistakes reason reasons
nobody everyone anyone people why stop instead free cheap money dollar dollars save saving home house yard backyard
grandma grandpa grandmother grandfather grandparents senior seniors elderly over 60 65 70 old-timers
miracle magic shocking insane amazing incredible unbelievable crazy wow happened happens believed believe nobody
video watch must-see ultimate complete full beginner beginners expert experts harvest harvests harvesting
result results huge massive tons bigger more less life explode explodes exploding double doubles triple triples
growth ingredient proven technique supercharge supercharges boost boosts hidden swear love hate shock stronger richer
engineer engineers scientist scientists farmer farmers gold black""".split())
NGOAI_LE_SO_IT = {"leaves": "leaf", "tomatoes": "tomato", "potatoes": "potato", "knives": "knife", "cacti": "cactus",
                  "berries": "berry", "cherries": "cherry", "strawberries": "strawberry", "blueberries": "blueberry",
                  "raspberries": "raspberry", "lilies": "lily", "peonies": "peony", "daisies": "daisy"}
# Từ thường: được nằm trong cụm («winter sowing», «cold frame», «fruit tree») nhưng không đứng làm từ khoá một mình.
TU_DON = set("""winter fall autumn spring summer season seasonal january february march april may june july august
september october november december cold hot warm frost freeze freezing snow rain heat sun shade
food foods vegetable veggie fruit tree shrub bush flower bloom blooming seed soil indoor indoors outdoor outdoors
container pot water watering bed beds space room window kitchen budget winter-proof extreme
amish ancient forgotten native nature natural organic""".split())
LOAI_MAC_DINH = (r"(?i)\b(recipe|recipes|cooking|prepper|prepping|stockpil\w*|power grid|power outage|blackout|"
                 r"pantry|buy in bulk|bulk foods?|survival food|emergency food|canning|heat-retention|"
                 r"live ?stream|asmr|minecraft|roblox|grow a garden game|sptw|twau|stand out|opal seeds|fortnite|"
                 r"gardeners'? world|full episode|podcast|unboxing)\b")
# Tiêu đề không phải tiếng Anh (thị trường US): chữ Việt / Romania, chữ không La-tinh, từ nối Tây Ban Nha / Bồ / Pháp / Đức / Hà Lan.
RE_KHONG_ANH = re.compile(
    r"[ăâđêôơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹșțî]"
    r"|[^\u0000-ɏ -⁯₠-⃏︀-️\U0001F000-\U0001FAFF]"
    r"|\b(que|los|las|del|una|como|para|plantas|jardín|jardin|uma|não|une|les|des|pour|plantes|der|die|das|und|"
    r"nicht|pflanzen|het|een|voor|tuin|pentru|grădin\w*)\b", re.I)
# Ngữ cảnh vườn: một gợi ý tìm kiếm chỉ được đếm khi có cụm kèm một trong các từ này
# («christmas cactus care» được, «christmas cactus meme» không).
RE_NGU_CANH = re.compile(r"(?i)\b(grow\w*|plant\w*|garden\w*|seeds?|soil|prun\w*|propagat\w*|overwinter\w*|indoors?|"
                         r"zone|frost|compost\w*|fertiliz\w*|bloom\w*|flower\w*|harvest\w*|repot\w*|cuttings?|"
                         r"care|water\w*|sow\w*|transplant\w*|winter|spring|fall|mulch\w*|raised bed|containers?|pots?)\b")
# Cờ trên từ khoá: YMYL = sức khoẻ / chữa bệnh (chỉ theo dõi, đi luật YMYL của pipeline); OFF_NICHE = ngoài vườn.
RE_YMYL = re.compile(r"(?i)\b(cure\w*|cancer|diabet\w*|blood\s+(pressure|sugar)|detox\w*|medicin\w*|heal\w*|doctors?|"
                     r"arthritis|inflammation|cholesterol|liver|kidney|immune|remed\w*|toxins?)\b")
RE_OFF_NICHE = re.compile(r"(?i)\b(pantry|prepp\w*|stockpil\w*|blackout|outage|bulk|survival|canning|grocery)\b")
# Gộp tên gọi trước khi tách từ
GOP = [
    (re.compile(r"\b(thanksgiving|holiday|xmas)\s+cact(us|i)\b", re.I), " christmas cactus "),
    (re.compile(r"\busda\s+(hardiness\s+)?zones?\b", re.I), " zone "),
    (re.compile(r"\bhouse\s+plants?\b", re.I), " houseplant "),
]


def f_tuoi(t: float) -> float:
    return min(1.0, max(SAN_F, (max(t, 0.5) / 30) ** HE_MU))


def muc(h):
    if h is None:
        return ""
    return next(m for nguong, m in MUC if h >= nguong)


# ---------- yt-dlp ----------

def ytdlp(args: list[str]) -> list[str]:
    cmd = ["yt-dlp", "--ignore-config", "--no-warnings", "--no-update", "--encoding", "utf-8",
           "--extractor-args", "youtube:lang=en", *args]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        print(f"  ! yt-dlp quá {TIMEOUT} s: {' '.join(args[-1:])}", file=sys.stderr)
        return []
    return [d for d in r.stdout.splitlines() if d.strip()]


def url_kenh(k: str) -> str:
    k = k.strip()
    if k.startswith("http"):
        return k.rstrip("/").removesuffix("/videos") + "/videos"
    if k.startswith("UC"):
        return f"https://www.youtube.com/channel/{k}/videos"
    return f"https://www.youtube.com/{k if k.startswith('@') else '@' + k}/videos"


def doc_meta(ids: list[str], nghi: float) -> list[dict]:
    ra = []
    for i in range(0, len(ids), LO):
        lo = ids[i:i + LO]
        for d in ytdlp(["--skip-download", "--ignore-errors", "--sleep-requests", "1", "-O", DUMP,
                        *[f"https://www.youtube.com/watch?v={x}" for x in lo]]):
            try:
                ra.append(json.loads(d))
            except json.JSONDecodeError:
                pass
        time.sleep(nghi)
    return ra


def ngay_dang(m: dict) -> datetime | None:
    if m.get("timestamp"):
        return datetime.fromtimestamp(m["timestamp"], tz=timezone.utc).replace(tzinfo=None)
    if m.get("upload_date"):
        return datetime.strptime(m["upload_date"], "%Y%m%d")
    return None


# ---------- dữ liệu ----------

def doc_ds(p: str | None) -> list[tuple[str, str]]:
    if not p:
        return []
    ra = []
    for d in Path(p).read_text(encoding="utf-8").splitlines():
        d = d.strip()
        if not d or d.startswith("#"):
            continue
        ten, _, k = d.rpartition("\t")
        ra.append((ten or k, k))
    return ra


def doc_tsv_cu(video_dir: str | None, chi_kenh: set[str] | None = None) -> dict[str, dict]:
    """TSV của thu_video.py → {channel_id: {ten, video}} (chỉ video dài). chi_kenh: chỉ đọc các kênh này."""
    ra: dict[str, dict] = {}
    if not video_dir:
        return ra
    for f in Path(video_dir).glob("*.tsv"):
        if chi_kenh is not None and f.stem not in chi_kenh:
            continue
        vs = []
        with open(f, encoding="utf-8") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                if r.get("is_short") == "1" or not r.get("view") or not r.get("ngay_dang"):
                    continue
                try:
                    vs.append({"id": r["id"], "ngay": datetime.fromisoformat(r["ngay_dang"][:19]),
                               "view": int(r["view"]), "like": int(r["like"] or 0), "tieu_de": r["tieu_de"],
                               "thoi_luong": float(r["thoi_luong_s"] or 0)})
                except ValueError:
                    continue
        ten = None
        meta = f.with_suffix(".meta.json")
        if meta.exists():
            try:
                ten = json.loads(meta.read_text(encoding="utf-8")).get("ten")
            except (json.JSONDecodeError, OSError):
                pass
        ra[f.stem] = {"ten": ten or f.stem, "video": vs}
    return ra


def la_dai(m: dict) -> bool:
    return (m.get("duration") or 0) > 180


# ---------- từ khoá (tiếng Anh, chỉ chủ thể) ----------
RE_TU = re.compile(r"[a-z][a-z'\-]*[a-z]|[a-z]")


def so_it(w: str) -> str:
    if w in NGOAI_LE_SO_IT:
        return NGOAI_LE_SO_IT[w]
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is", "as")):
        return w[:-1]
    return w


def tu_khoa(tieu_de: str) -> set[str]:
    """Cụm 1–3 từ nội dung liền nhau. Từ đơn chỉ giữ khi ≥ 4 chữ và không chung chung."""
    ra = set()
    s = " " + tieu_de + " "
    for re_, thay in GOP:
        s = re_.sub(thay, s)
    for doan in re.split(r"[^a-z' \-]+", s.lower().replace("’", "'")):
        tu = [so_it(w.strip("'-")) for w in RE_TU.findall(doan)]
        cum: list[str] = []
        for w in tu + [""]:
            if w and w not in TU_DUNG and not w.isdigit():
                cum.append(w)
                continue
            for n in (1, 2, 3):
                for i in range(len(cum) - n + 1):
                    g = cum[i:i + n]
                    if n == 1 and (len(g[0]) < 4 or g[0] in TU_CHUNG or g[0] in TU_DON):
                        continue
                    if all(x in TU_CHUNG for x in g):
                        continue
                    if g[0] in TU_CHUNG and n > 1:   # bỏ đuôi/đầu chung chung: "grow garlic" → giữ "garlic"
                        continue
                    if g[-1] in TU_CHUNG and n > 1:
                        continue
                    ra.add(" ".join(g))
            cum = []
    return ra


# ---------- chấm ----------

def nen_kenh(vs, hom_nay, tuoi):
    ds = [v["view"] for v in vs if tuoi[0] <= (hom_nay - v["ngay"]).days <= tuoi[1]]
    return (st.median(ds), len(ds)) if len(ds) >= NEN_TOI_THIEU else (None, len(ds))


def he_so(view: int, nen: float, t: float, nguon: str) -> float:
    """Hệ số trẻ, có trần cho nền «sub» và sàn view cho video trẻ (dưới sàn thì giữ < 2)."""
    h = view / (nen * f_tuoi(t))
    if nguon == "sub":
        h = min(h, TRAN_SUB)
        if view < VIEW_MIN_SUB:
            h = min(h, 1.99)
    if view < VIEW_MIN_LEN or (t * 24 < TRE_GIO and view < TRE_VIEW_MIN):
        h = min(h, 1.99)
    return h


def cham(kenh: dict[str, dict], hom_nay: datetime, ngay: int, truoc: dict | None, loai: str = LOAI_MAC_DINH):
    video_ra, kenh_ra = [], []
    re_loai = re.compile(loai) if loai else None
    for cid, k in kenh.items():
        vs = [v for v in k["video"] if v["ngay"] <= hom_nay]
        nen, n_nen = nen_kenh(vs, hom_nay, TUOI_NEN)
        nguon = "kenh" if nen else ""
        if not nen and k.get("subs"):
            nen, nguon = max(k["subs"], 1000) * HE_SO_SUB, "sub"
        moi = sorted(vs, key=lambda v: v["ngay"], reverse=True)
        cuoi = moi[0]["ngay"] if moi else None
        da = [v["view"] / f_tuoi((hom_nay - v["ngay"]).days) for v in vs if 7 <= (hom_nay - v["ngay"]).days <= 60]
        da_view = round(st.median(da) / nen, 2) if (da and nen and nguon == "kenh") else None
        co = []
        if cuoi is None or (hom_nay - cuoi).days > 60:
            co.append("NGUNG")
        if nguon == "sub":
            co.append("NEN_THEO_SUB")
        kenh_ra.append({"kenh": cid, "ten": k["ten"], "subs": k.get("subs") or "", "nen": round(nen) if nen else "",
                        "nguon_nen": nguon, "n_nen": n_nen,
                        "video_60_ngay": sum(1 for v in vs if (hom_nay - v["ngay"]).days <= 60),
                        "ngay_video_cuoi": cuoi.date().isoformat() if cuoi else "",
                        "da_view_60": da_view if da_view is not None else "", "co": ",".join(co)})
        if not nen:
            continue
        for v in vs:
            t = (hom_nay - v["ngay"]).total_seconds() / 86400
            if t > ngay or t < 0.5 or (re_loai and re_loai.search(v["tieu_de"])) or RE_KHONG_ANH.search(v["tieu_de"]):
                continue
            h = he_so(v["view"], nen, t, nguon)
            tang, vph_do = "", ""
            if truoc and v["id"] in truoc["video"]:
                cu = truoc["video"][v["id"]]
                moc_cu = datetime.fromisoformat(truoc.get("gio") or truoc["ngay"])
                gio_cach = (hom_nay - moc_cu).total_seconds() / 3600
                ds = (hom_nay - datetime.fromisoformat(truoc["ngay"])).days
                if ds >= 2:
                    tang = round((v["view"] - cu) / ds)
                if gio_cach >= VPH_GIO_TOI_THIEU:
                    vph_do = round((v["view"] - cu) / gio_cach)
            gio_tuoi = t * 24
            vph_tb = round(v["view"] / gio_tuoi) if gio_tuoi >= VPH_TUOI_TOI_THIEU else ""
            video_ra.append({"he_so_tre": round(h, 2), "muc": muc(h), "nguon_nen": nguon, "view": v["view"],
                             "tuoi_ngay": round(t, 1), "vph_tb": vph_tb, "vph_do": vph_do, "view_tang_moi_ngay": tang,
                             "ty_le_like": round(v["like"] / v["view"], 4) if v["view"] else "",
                             "ten_kenh": k["ten"], "kenh": cid, "tieu_de": v["tieu_de"],
                             "link": f"https://www.youtube.com/watch?v={v['id']}"})
    video_ra.sort(key=lambda r: (r["he_so_tre"], r["view"]), reverse=True)
    return video_ra, kenh_ra


def cham_mua(kenh: dict[str, dict], hom_nay: datetime, loai: str = LOAI_MAC_DINH):
    """Video dài đăng quanh cùng kỳ năm ngoái (−14 … +42 ngày), so với nền 180–730 ngày của cùng kênh."""
    re_loai = re.compile(loai) if loai else None
    tu, den = hom_nay - timedelta(days=365 + MUA_TRUOC), hom_nay - timedelta(days=365 - MUA_SAU)
    ra = []
    for cid, k in kenh.items():
        nen, _ = nen_kenh(k["video"], hom_nay, TUOI_NEN_MUA)
        if not nen:
            continue
        cuoi = max((v["ngay"] for v in k["video"]), default=None)
        if cuoi is None or (hom_nay - cuoi).days > 60:   # kênh đã ngừng: nền nhỏ, hệ số bị thổi phồng
            continue
        for v in k["video"]:
            if not (tu <= v["ngay"] <= den) or v["view"] < MUA_VIEW_TOI_THIEU or (re_loai and re_loai.search(v["tieu_de"])) or RE_KHONG_ANH.search(v["tieu_de"]):
                continue
            h = v["view"] / nen
            ra.append({"he_so_tre": round(h, 2), "muc": muc(h), "view": v["view"],
                       "ngay_dang": v["ngay"].date().isoformat(),
                       "ngay_tuong_ung_nam_nay": (v["ngay"] + timedelta(days=365)).date().isoformat(),
                       "ten_kenh": k["ten"], "kenh": cid, "tieu_de": v["tieu_de"],
                       "link": f"https://www.youtube.com/watch?v={v['id']}"})
    ra.sort(key=lambda r: r["he_so_tre"], reverse=True)
    return ra


def co_tu_khoa(w: str, tieu_de: list[str], so_kenh: int) -> str:
    """DA_KENH (≥ 3 kênh) · YMYL (sức khoẻ, chữa bệnh: chỉ theo dõi) · OFF_NICHE (ngoài vườn). YMYL/OFF_NICHE bật khi
    từ khoá chứa từ đó hoặc quá nửa tiêu đề nóng có từ đó."""
    co = ["DA_KENH"] if so_kenh >= 3 else []
    for ten, re_ in (("YMYL", RE_YMYL), ("OFF_NICHE", RE_OFF_NICHE)):
        if re_.search(w) or sum(bool(re_.search(t)) for t in tieu_de) * 2 > len(tieu_de):
            co.append(ten)
    return ",".join(co)


def goi_y_yt(cum: str) -> list[str]:
    """Gợi ý tìm kiếm YouTube, thị trường US, tiếng Anh (miễn phí, không khoá)."""
    url = "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=en&gl=US&q=" + quote(cum)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (trend-check)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.loads(r.read().decode("utf-8", "replace"))
        return [x for x in d[1] if isinstance(x, str)]
    except Exception as e:   # mạng lỗi thì để trống, không chặn cả báo cáo
        print(f"  ! gợi ý lỗi «{cum}»: {e}", file=sys.stderr)
        return []


def them_goi_y(kw: list[dict], so: int, nghi: float, ham=goi_y_yt) -> int:
    """Điền goi_y_us (số gợi ý chứa cụm và có ngữ cảnh vườn) + goi_y_dau (3 gợi ý đầu), tối đa `so` từ khoá."""
    chon = sorted(kw, key=lambda r: ("DA_KENH" not in r["co"], -r["so_kenh"], -r["do_noi"]))[:so]
    for r in chon:
        gy = ham(r["tu_khoa"])
        r["goi_y_us"] = sum(1 for g in gy if r["tu_khoa"] in g.lower()
                            and (RE_NGU_CANH.search(g.lower().replace(r["tu_khoa"], " ")) or RE_NGU_CANH.search(r["tu_khoa"])))
        r["goi_y_dau"] = " / ".join(gy[:3])
        time.sleep(nghi)
    return len(chon)


# ---------- lịch mốc vườn ----------

def goi_y_moc(moc: list[dict], nghi: float, ham=goi_y_yt) -> None:
    """Mỗi mốc: đếm gợi ý US có ngữ cảnh vườn cho từng cụm ở cột tu_khoa (tối đa 3 cụm)."""
    for m in moc:
        ra = []
        for cum in [c.strip() for c in m["tu_khoa"].split(",") if c.strip()][:3]:
            gy = ham(cum)
            n = sum(1 for g in gy if cum in g.lower()
                    and (RE_NGU_CANH.search(g.lower().replace(cum, " ")) or RE_NGU_CANH.search(cum)))
            ra.append(f"{cum}: {n}")
            time.sleep(nghi)
        m["goi_y_us"] = " · ".join(ra)


def thu_thu_n(nam: int, thang: int, thu: int, n: int) -> date:
    """Ngày thứ `thu` (0 = thứ Hai) thứ n trong tháng; n = -1 là lần cuối."""
    if n > 0:
        d = date(nam, thang, 1)
        return d + timedelta(days=(thu - d.weekday()) % 7 + 7 * (n - 1))
    d = (date(nam, thang + 1, 1) if thang < 12 else date(nam + 1, 1, 1)) - timedelta(days=1)
    return d - timedelta(days=(d.weekday() - thu) % 7)


NGAY_LE = {"thanksgiving": lambda y: thu_thu_n(y, 11, 3, 4), "mothers": lambda y: thu_thu_n(y, 5, 6, 2),
           "fathers": lambda y: thu_thu_n(y, 6, 6, 3), "memorial": lambda y: thu_thu_n(y, 5, 0, -1),
           "labor": lambda y: thu_thu_n(y, 9, 0, 1)}


def ngay_le(ma: str, nam: int) -> date | None:
    """MM-DD hoặc mã ngày lễ biến động (thanksgiving, mothers, fathers, memorial, labor)."""
    if ma in NGAY_LE:
        return NGAY_LE[ma](nam)
    try:
        th, ng = (int(x) for x in ma.split("-"))
        return date(nam, th, ng)
    except ValueError:
        return None


def moc_sap_toi(p: str | None, hom_nay: date, so_ngay: int) -> list[dict]:
    """TSV cột: ngay (MM-DD | mã lễ), su_kien, tu_khoa, ghi_chu. Trả mốc trong `so_ngay` ngày tới."""
    if not p:
        return []
    ra = []
    with open(p, encoding="utf-8") as fh:
        for r in csv.DictReader((d for d in fh if not d.startswith("#")), delimiter="	"):
            for nam in (hom_nay.year, hom_nay.year + 1):
                d = ngay_le((r.get("ngay") or "").strip(), nam)
                if not d or not (0 <= (d - hom_nay).days <= so_ngay):
                    continue
                con = (d - hom_nay).days
                ra.append({"ngay": d.isoformat(), "con_ngay": con, "su_kien": r["su_kien"],
                           "kip": "PHIM_DAI" if con >= 21 else "GAP", "tu_khoa": r.get("tu_khoa") or "",
                           "ghi_chu": r.get("ghi_chu") or ""})
                break
    return sorted(ra, key=lambda r: r["con_ngay"])


def gom_tu_khoa(video_ra: list[dict]):
    tat_ca = defaultdict(int)
    nong = defaultdict(lambda: {"kenh": set(), "view": 0, "he_so": [], "vi_du": [], "tieu_de": []})
    for v in video_ra:
        kw = tu_khoa(v["tieu_de"])
        for w in kw:
            tat_ca[w] += 1
        if v["he_so_tre"] >= 2:
            for w in kw:
                n = nong[w]
                n["kenh"].add(v["kenh"])
                n["view"] += v["view"]
                n["he_so"].append(v["he_so_tre"])
                n["tieu_de"].append(v["tieu_de"])
                if len(n["vi_du"]) < 3:
                    n["vi_du"].append(v["tieu_de"][:60])
    n_tat, n_nong = max(len(video_ra), 1), max(sum(1 for v in video_ra if v["he_so_tre"] >= 2), 1)
    ra = []
    for w, n in nong.items():
        if len(n["kenh"]) < 2:
            continue
        do_noi = (len(n["he_so"]) / n_nong) / (tat_ca[w] / n_tat)
        ra.append({"tu_khoa": w, "so_kenh": len(n["kenh"]), "so_video_nong": len(n["he_so"]),
                   "so_video_tat_ca": tat_ca[w], "do_noi": round(do_noi, 2),
                   "he_so_trung_vi": round(st.median(n["he_so"]), 2), "tong_view": n["view"],
                   "co": co_tu_khoa(w, n["tieu_de"], len(n["kenh"])), "goi_y_us": "", "goi_y_dau": "",
                   "vi_du": " | ".join(n["vi_du"])})
    ra.sort(key=lambda r: (r["so_kenh"], r["do_noi"], r["tong_view"]), reverse=True)
    giu = []
    for r in ra:   # bỏ cụm nằm trong cụm dài hơn có cùng số kênh, cùng số video nóng
        if any(re.search(rf"\b{re.escape(r['tu_khoa'])}\b", g["tu_khoa"]) and g["so_kenh"] == r["so_kenh"]
               and g["so_video_nong"] == r["so_video_nong"] for g in giu):
            continue
        giu = [g for g in giu if not (re.search(rf"\b{re.escape(g['tu_khoa'])}\b", r["tu_khoa"])
                                      and g["so_kenh"] == r["so_kenh"] and g["so_video_nong"] == r["so_video_nong"])]
        giu.append(r)
    giu.sort(key=lambda r: (r["so_kenh"], r["do_noi"], r["tong_view"]), reverse=True)
    return giu


# ---------- ghi ----------

def ghi_tsv(p: Path, rows: list[dict]):
    if not rows:
        p.write_text("", encoding="utf-8")
        return
    with open(p, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)


def bang_tu_khoa(kw, n=30):
    L = ["| từ khoá | kênh | video nóng / tất cả | độ nổi | hệ số trung vị | tổng view | cờ | gợi ý US | gợi ý đầu | ví dụ |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in kw[:n]:
        L.append(f"| {r['tu_khoa']} | {r['so_kenh']} | {r['so_video_nong']}/{r['so_video_tat_ca']} | {r['do_noi']} | "
                 f"{r['he_so_trung_vi']} | {r['tong_view']:,} | {r['co']} | {r['goi_y_us']} | "
                 f"{r['goi_y_dau'].replace('|', '/')} | {r['vi_du'].replace('|', '/')} |")
    if not kw:
        L.append("| (không có cụm nào đủ ≥ 2 kênh) | | | | | | | | | |")
    return L


def bao_cao(p: Path, hom_nay, ngay, video_ra, kw, mua_ra, kw_mua, kenh_ra, nguon_ghi, moc=None, co_goi_y=False):
    L = [f"# Dò trend Garden US — {hom_nay.date().isoformat()}", "",
         f"Nguồn: {nguon_ghi}. Hệ số trẻ là [ƯỚC] (một lần chụp); cột tăng/ngày là [ĐO] khi có ảnh chụp trước. 0 credit.",
         f"Video dài ≤ {ngay} ngày: {len(video_ra)} · rất nóng (≥5): {sum(v['muc']=='rat_nong' for v in video_ra)} · "
         f"nóng (3–5): {sum(v['muc']=='nong' for v in video_ra)} · lên (2–3): {sum(v['muc']=='len' for v in video_ra)}", "",
         "Cờ: DA_KENH = ≥ 3 kênh · YMYL = sức khoẻ, chữa bệnh (chỉ theo dõi, đi luật YMYL) · OFF_NICHE = ngoài vườn (bỏ). "
         + ("Gợi ý US = số gợi ý tìm kiếm YouTube (Mỹ) chứa cụm và có ngữ cảnh vườn; 0 = người xem chưa gõ cụm này, "
            "đừng dựa tiêu đề vào cụm đó." if co_goi_y else "Gợi ý US: chưa hỏi (chạy lại với --goi-y)."), ""]
    if moc is not None:
        L += ["## 0. Mốc mùa vụ sắp tới (trend đoán trước được)", "",
              "PHIM_DAI = còn ≥ 21 ngày, kịp làm phim dài và đăng trước đỉnh 2–4 tuần · GAP = < 21 ngày, chỉ làm khi bỏ "
              "qua tập khác. Ngày trong lịch là mốc lên lịch, không phải số liệu cho lời đọc.", "",
              "| ngày | còn (ngày) | kịp | mốc | từ khoá gợi ý | gợi ý US (số gợi ý có ngữ cảnh vườn) | ghi chú |",
              "|---|---|---|---|---|---|---|"]
        for m in moc:
            L.append(f"| {m['ngay']} | {m['con_ngay']} | {m['kip']} | {m['su_kien']} | {m['tu_khoa']} | "
                     f"{m.get('goi_y_us', '')} | {m['ghi_chu']} |")
        if not moc:
            L.append("| | | | (không có mốc trong khoảng này) | | | |")
        L.append("")
    L += [f"## 1. Từ khoá trend {ngay} ngày (≥ 2 kênh; ĐA_KENH = ≥ 3 kênh)", "", *bang_tu_khoa(kw), "",
         "## 2. Trend mùa — cùng kỳ năm ngoái (đăng trước đỉnh 2–4 tuần)", "",
         f"Video đăng {(hom_nay - timedelta(days=365 + MUA_TRUOC)).date()} … {(hom_nay - timedelta(days=365 - MUA_SAU)).date()}, "
         f"hệ số = view ÷ trung vị kênh (video 180–730 ngày). Cột «ngày năm nay» = hạn tham khảo; đăng trước ngày đó.", "",
         *bang_tu_khoa(kw_mua, 25), "",
         "| hệ số | view | đăng | ngày năm nay | kênh | tiêu đề |", "|---|---|---|---|---|---|"]
    for v in [v for v in mua_ra if v["he_so_tre"] >= 2][:30]:
        L.append(f"| {v['he_so_tre']} | {v['view']:,} | {v['ngay_dang']} | {v['ngay_tuong_ung_nam_nay']} | "
                 f"{str(v['ten_kenh'])[:18]} | [{v['tieu_de'][:70].replace('|', '/')}]({v['link']}) |")
    L += ["", f"## 3. Video đang lên ≤ {ngay} ngày (hệ số trẻ ≥ 2)", "",
          "VPH tb = view ÷ giờ từ lúc đăng · VPH đo = tăng view ÷ giờ giữa hai lần chụp [ĐO]. VPH đo ≫ tb: đang tăng tốc; "
          "≪ tb: đã qua đỉnh, đừng chạy theo. VPH tuyệt đối thiên kênh lớn, đọc cùng hệ số.", "",
          "| hệ số | mức | nền | view | tuổi (ngày) | VPH tb | VPH đo | tăng/ngày | kênh | tiêu đề |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for v in [v for v in video_ra if v["he_so_tre"] >= 2][:60]:
        L.append(f"| {v['he_so_tre']} | {v['muc']} | {v['nguon_nen']} | {v['view']:,} | {v['tuoi_ngay']} | {v['vph_tb']} | "
                 f"{v['vph_do']} | {v['view_tang_moi_ngay']} | "
                 f"{str(v['ten_kenh'])[:18]} | [{v['tieu_de'][:70].replace('|', '/')}]({v['link']}) |")
    L += ["", "## 4. Đà kênh", "", "| kênh | đà view 60 ngày | video 60 ngày | video cuối | cờ |", "|---|---|---|---|---|"]
    for k in sorted(kenh_ra, key=lambda k: (k["da_view_60"] if k["da_view_60"] != "" else -1), reverse=True):
        L.append(f"| {str(k['ten'])[:22]} | {k['da_view_60']} | {k['video_60_ngay']} | {k['ngay_video_cuoi']} | {k['co']} |")
    L += ["", "## Cách dùng (references/topic-gate-en.md ②, title-keyword-strategy-en.md)", "",
          "- Thứ tự tin tín hiệu (ngách vườn đi theo mùa và theo tìm kiếm): ① trend mùa ≥ 2 kênh + gợi ý US ≥ 1 · "
          "② mốc mùa vụ PHIM_DAI + gợi ý US ≥ 1 · ③ ĐA_KENH 10 ngày (hiếm, làm gấp) · ④ một kênh, hoặc gợi ý US = 0: chỉ theo dõi.",
          "- Cổng ② ĐẠT khi chủ thể có cờ ĐA_KENH, hoặc 2 kênh và có video tăng/ngày [ĐO] thật; hoặc ≥ 2 kênh ở bảng trend mùa.",
          "- Cờ YMYL: không tự đề xuất; nếu làm thì qua luật YMYL/compliance của pipeline. OFF_NICHE: bỏ.",
          "- «video nóng / tất cả» thấp (nhiều kênh làm, ít bản nóng) = bão hoà → cổng ⓑ, bắt buộc đổi góc.",
          "- Hạn: trend 10 ngày → đăng ≤ 10 ngày từ ngày báo cáo; trend mùa → đăng trước «ngày năm nay» 2–4 tuần.",
          "- Tiêu đề A/B/C đều chứa ≥ 1 từ khoá trend trong ~25 ký tự đầu, CHỈ khi video nói đúng về nó; lấy chủ thể, không chép khuôn câu.",
          "- Từ khoá vẫn qua chặn cứng X1–X5, L9 của topic-gate (máy chỉ bỏ từ câu view/nhãn tuổi khỏi danh sách, không thay cổng đó)."]
    p.write_text("\n".join(L) + "\n", encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--ds")
    ap.add_argument("--tim", default="")
    ap.add_argument("--so-tim", type=int, default=30)
    ap.add_argument("--ngay", type=int, default=10)
    ap.add_argument("--so-moi", type=int, default=12)
    ap.add_argument("--video-dir")
    ap.add_argument("--anh-chup-dir")
    ap.add_argument("--hom-nay")
    ap.add_argument("--nghi", type=float, default=2.0)
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--loai", default=LOAI_MAC_DINH, help="regex tiêu đề lạc ngách bị bỏ; '' = không lọc")
    ap.add_argument("--nap-meta", help="meta-video.jsonl của lần chạy trước: chấm lại không gọi yt-dlp (không ghi ảnh chụp)")
    ap.add_argument("--goi-y", action="store_true", help="hỏi gợi ý tìm kiếm YouTube US cho từ khoá trend + mùa (miễn phí)")
    ap.add_argument("--so-goi-y", type=int, default=30)
    ap.add_argument("--lich", help="TSV mốc mùa vụ (ngay MM-DD|thanksgiving|mothers|fathers|memorial|labor, su_kien, tu_khoa, ghi_chu)")
    ap.add_argument("--lich-ngay", type=int, default=45)
    ns = ap.parse_args(argv)

    out = Path(ns.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    hom_nay = datetime.fromisoformat(ns.hom_nay) if ns.hom_nay else datetime.now(timezone.utc).replace(tzinfo=None)
    ds = doc_ds(ns.ds)
    ids_ds = {k for _, k in ds if k.startswith("UC")}
    kenh = doc_tsv_cu(ns.video_dir, ids_ds or None)
    nguon = [f"TSV {ns.video_dir} ({len(kenh)} kênh)"] if ns.video_dir else []
    for ten, k in ds:
        if k in kenh and ten != k:
            kenh[k]["ten"] = ten
    mua_ra = cham_mua(kenh, hom_nay, ns.loai)   # kho cũ đủ cho lớp mùa, không cần yt-dlp

    metas = None
    if ns.nap_meta:   # chấm lại từ metadata đã tải lần trước, không gọi yt-dlp
        metas = [json.loads(d) for d in Path(ns.nap_meta).read_text(encoding="utf-8").splitlines() if d.strip()]
        nguon.append(f"metadata đã tải {ns.nap_meta} ({len(metas)} video)")
    elif not ns.offline:
        ids_moi: list[str] = []
        for i, (ten, k) in enumerate(ds, 1):
            ids = ytdlp(["--flat-playlist", "--print", "%(id)s", "--playlist-end", str(ns.so_moi), url_kenh(k)])
            print(f"[{i}/{len(ds)}] {ten}: {len(ids)} id", flush=True)
            ids_moi += ids
            time.sleep(ns.nghi)
        for cum in [c.strip() for c in ns.tim.split(",") if c.strip()]:
            url = f"https://www.youtube.com/results?search_query={quote(cum)}&sp={SP_THANG_NAY}"
            ids = ytdlp(["--flat-playlist", "--print", "%(id)s", "--playlist-end", str(ns.so_tim), url])
            print(f"[tìm] {cum}: {len(ids)} id", flush=True)
            ids_moi += ids
            time.sleep(ns.nghi)
        ids_moi = list(dict.fromkeys(ids_moi))
        print(f"Đọc metadata {len(ids_moi)} video…", flush=True)
        metas = doc_meta(ids_moi, ns.nghi)
        with open(out / "meta-video.jsonl", "w", encoding="utf-8") as fh:
            fh.writelines(json.dumps(m, ensure_ascii=False) + "\n" for m in metas)
        nguon.append(f"yt-dlp {len(metas)}/{len(ids_moi)} video ({len(ds)} kênh, cụm tìm: {ns.tim or 'không'})")
    if metas is not None:
        for m in metas:
            nd = ngay_dang(m)
            if not nd or not la_dai(m) or m.get("view_count") is None or not m.get("channel_id"):
                continue
            ten_m = m.get("channel") or m.get("uploader")
            k = kenh.setdefault(m["channel_id"], {"ten": ten_m or m["channel_id"], "video": []})
            k["moi"] = True
            if ten_m and k["ten"].startswith("UC"):
                k["ten"] = ten_m
            if m.get("channel_follower_count"):
                k["subs"] = m["channel_follower_count"]
            k["video"] = [v for v in k["video"] if v["id"] != m["id"]]
            k["video"].append({"id": m["id"], "ngay": nd, "view": m["view_count"], "like": m.get("like_count") or 0,
                               "tieu_de": m.get("title") or "", "thoi_luong": m.get("duration") or 0})

    chup_dir = Path(ns.anh_chup_dir) if ns.anh_chup_dir else out.parent / "anh-chup"
    truoc = None
    if chup_dir.exists():
        cu = sorted(p for p in chup_dir.glob("*.json") if p.stem < hom_nay.date().isoformat())
        if cu:
            truoc = json.loads(cu[-1].read_text(encoding="utf-8"))

    if metas is not None:   # chỉ báo kênh có số mới
        kenh = {c: k for c, k in kenh.items() if k.get("moi")}
    video_ra, kenh_ra = cham(kenh, hom_nay, ns.ngay, truoc, ns.loai)
    kw, kw_mua = gom_tu_khoa(video_ra), gom_tu_khoa(mua_ra)
    co_goi_y = ns.goi_y and not ns.offline
    if co_goi_y:
        n = them_goi_y(kw, ns.so_goi_y, min(ns.nghi, 1.0)) + them_goi_y(kw_mua, ns.so_goi_y, min(ns.nghi, 1.0))
        nguon.append(f"gợi ý YouTube US cho {n} từ khoá")
    moc = moc_sap_toi(ns.lich, hom_nay.date(), ns.lich_ngay) if ns.lich else None
    if moc and co_goi_y:
        goi_y_moc(moc, min(ns.nghi, 1.0))
    ghi_tsv(out / "trend-video.tsv", video_ra)
    ghi_tsv(out / "trend-tu-khoa.tsv", kw)
    ghi_tsv(out / "trend-mua.tsv", mua_ra)
    ghi_tsv(out / "trend-mua-tu-khoa.tsv", kw_mua)
    ghi_tsv(out / "trend-kenh.tsv", kenh_ra)
    bao_cao(out / "bao-cao-trend.md", hom_nay, ns.ngay, video_ra, kw, mua_ra, kw_mua, kenh_ra, "; ".join(nguon) or "không",
            moc, co_goi_y)
    if not ns.offline and not ns.nap_meta:
        chup_dir.mkdir(parents=True, exist_ok=True)
        anh = {"ngay": hom_nay.date().isoformat(), "gio": hom_nay.isoformat(timespec="minutes"),
               "video": {v["id"]: v["view"] for k in kenh.values() for v in k["video"] if (hom_nay - v["ngay"]).days <= 90}}
        (chup_dir / f"{hom_nay.date().isoformat()}.json").write_text(json.dumps(anh, ensure_ascii=False), encoding="utf-8")
    print(f"Xong: {len(video_ra)} video ≤ {ns.ngay} ngày ({sum(v['he_so_tre'] >= 2 for v in video_ra)} ≥ 2), "
          f"{len(kw)} từ khoá trend ({sum(1 for r in kw if 'DA_KENH' in r['co'])} ĐA_KENH); mùa: {len(mua_ra)} video, "
          f"{len(kw_mua)} từ khoá. Báo cáo: {out / 'bao-cao-trend.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
