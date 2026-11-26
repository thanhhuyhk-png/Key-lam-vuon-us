"""Test do_trend.py bằng tiêu đề thật của 2 lần quét 18/11 và 22/11/2026.
Chạy: python -X utf8 -m pytest -q tools/tests/test_do_trend.py -p no:cacheprovider
"""
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import do_trend as d  # noqa: E402

HOM_NAY = datetime(2026, 11, 22, 12)


# ---------- tách từ ----------

def test_tu_don_khong_dung_mot_minh():
    kw = d.tu_khoa("How Amish Grow Fresh Food All Winter With No Greenhouse")
    assert "winter" not in kw and "food" not in kw
    assert "greenhouse" in kw


def test_tu_don_van_nam_trong_cum():
    kw = d.tu_khoa("Elderly Homesteader Plants Cold Frame For Winter Vegetables")
    assert "cold" not in kw and "vegetable" not in kw
    assert "cold frame" in kw


def test_cum_cay_giu_duoc():
    kw = d.tu_khoa("15 Container Dwarf Fruit Trees That Thrive In Extreme Cold")
    assert "dwarf fruit tree" in kw
    assert "cold" not in kw


def test_gop_christmas_cactus():
    assert "christmas cactus" in d.tu_khoa("Thanksgiving Cactus Not Blooming? Do This Now")
    assert "christmas cactus" in d.tu_khoa("Holiday Cacti Care Secrets")


def test_gop_zone():
    kw = d.tu_khoa("9 Vegetables to Plant Before December Arrives (By USDA Zone)")
    assert "usda" not in kw


def test_thang_khong_dung_mot_minh():
    assert "november" not in d.tu_khoa("The 7 Perennial Seed You Must Start in November")


# ---------- bộ lọc ----------

def test_loai_do_kho_mat_dien():
    import re
    r = re.compile(d.LOAI_MAC_DINH)
    for t in ["15 Pantry Foods You're Overpaying For or Throwing Away (Save Money Fast)",
              "Stop Wasting Money! 15 Best Foods to Buy in Bulk and 7 That Go Bad Fast",
              "12 Budget Heat-Retention Hacks for a Winter Blackout: Seal Drafts"]:
        assert r.search(t), t
    assert not r.search("How Amish Grow Fresh Food All Winter With No Greenhouse")


def test_loc_khong_phai_tieng_anh():
    assert d.RE_KHONG_ANH.search("Cum să plantezi usturoi toamna")
    assert d.RE_KHONG_ANH.search("Plantas que crecen en invierno para el jardín")
    assert d.RE_KHONG_ANH.search("Zo snoei je een appelboom in de tuin")
    assert not d.RE_KHONG_ANH.search("20 Forgotten Vegetables That Grow Like Weeds - The Lazy Gardener's Gold")
    assert not d.RE_KHONG_ANH.search("This Native SUPERFRUIT Is WAY BETTER THAN Blueberries 🍇")


def test_co_ymyl_va_off_niche():
    assert "YMYL" in d.co_tu_khoa("turmeric", ["Grow Turmeric to Heal Arthritis Naturally"] * 2, 2)
    assert "OFF_NICHE" in d.co_tu_khoa("pantry", ["15 Pantry Foods"], 2)
    assert d.co_tu_khoa("garlic", ["Plant Garlic in November"], 3) == "DA_KENH"


# ---------- hệ số ----------

def test_san_view_video_tre():
    # Prepare Pantry: 32 view, 0,7 ngày, nền nhỏ → không được ≥ 2
    assert d.he_so(32, 20, 0.7, "kenh") < 2


def test_san_view_chung():
    assert d.he_so(53, 10, 3.6, "kenh") < 2


def test_tran_nen_sub():
    assert d.he_so(1_000_000, 1000, 5, "sub") <= d.TRAN_SUB
    assert d.he_so(4000, 100, 5, "sub") < 2   # dưới VIEW_MIN_SUB


def test_he_so_binh_thuong_khong_doi():
    # Frugal Solutions 22/11: 6.762 view, 8,7 ngày → vẫn «nóng»
    h = d.he_so(6762, 3000, 8.7, "kenh")
    assert abs(h - 6762 / (3000 * d.f_tuoi(8.7))) < 1e-9


def _kenh(view, gio_tuoi, cid="UC1", nen_view=1000):
    vs = [{"id": f"n{i}", "ngay": HOM_NAY - timedelta(days=40 + i * 10), "view": nen_view, "like": 0,
           "tieu_de": "old garlic video", "thoi_luong": 600} for i in range(6)]
    vs.append({"id": "moi", "ngay": HOM_NAY - timedelta(hours=gio_tuoi), "view": view, "like": 10,
               "tieu_de": "Plant Garlic in November", "thoi_luong": 600})
    return {cid: {"ten": "K", "video": vs}}


def test_vph_tb_va_vph_do():
    truoc = {"ngay": "2026-11-21", "gio": "2026-11-21T00:00", "video": {"moi": 1000}}
    video, _ = d.cham(_kenh(4000, 60), HOM_NAY, 10, truoc)
    v = next(x for x in video if x["link"].endswith("moi"))
    assert v["vph_tb"] == round(4000 / 60)
    assert v["vph_do"] == round(3000 / 36)


def test_vph_tb_trong_khi_qua_tre():
    video, _ = d.cham(_kenh(4000, 13), HOM_NAY, 10, None)
    v = next(x for x in video if x["link"].endswith("moi"))
    assert v["vph_tb"] != ""
    video, _ = d.cham(_kenh(4000, 5), HOM_NAY, 10, None)
    assert not any(x["link"].endswith("moi") for x in video)   # < 12 giờ: bỏ hẳn


# ---------- gợi ý ----------

def test_goi_y_chi_dem_ngu_canh_vuon():
    kw = [{"tu_khoa": "christmas cactus", "co": "", "so_kenh": 2, "do_noi": 1, "goi_y_us": "", "goi_y_dau": ""}]
    gia = lambda c: ["christmas cactus care", "christmas cactus meme", "christmas cactus not blooming",
                     "christmas cactus propagation"]
    d.them_goi_y(kw, 5, 0, gia)
    assert kw[0]["goi_y_us"] == 3   # «meme» không tính; «not blooming» có «bloom»


# ---------- lịch ----------

def test_ngay_le_bien_dong():
    assert d.ngay_le("thanksgiving", 2026) == date(2026, 11, 26)
    assert d.ngay_le("mothers", 2027) == date(2027, 5, 9)
    assert d.ngay_le("memorial", 2027) == date(2027, 5, 31)
    assert d.ngay_le("12-25", 2026) == date(2026, 12, 25)


def test_moc_sap_toi(tmp_path):
    p = tmp_path / "l.tsv"
    p.write_text("# chú thích\nngay\tsu_kien\ttu_khoa\tghi_chu\n12-25\tChristmas\tpoinsettia\t\n"
                 "11-26\tTG\t\t\n03-01\tXa\t\t\n", encoding="utf-8")
    m = d.moc_sap_toi(str(p), date(2026, 11, 22), 45)
    assert [x["su_kien"] for x in m] == ["TG", "Christmas"]
    assert m[0]["kip"] == "GAP" and m[1]["kip"] == "PHIM_DAI"


def test_lich_vuon_that_doc_duoc():
    p = Path(__file__).resolve().parents[2] / "research" / "trend-us" / "lich-vuon-us.tsv"
    m = d.moc_sap_toi(str(p), date(2026, 11, 22), 400)
    assert len(m) >= 15


def test_loai_game_va_tv():
    import re
    r = re.compile(d.LOAI_MAC_DINH)
    assert r.search("How To Find Opal Seeds For Sptw & Twau In Stand Out!!")
    assert r.search("Gardeners' World Winter Specials 2026/27 Ep1 / Monty's Winter Gardening")
    assert not r.search("Christmas Cactus Not Blooming? Do This Now")


def test_goi_y_moc():
    moc = [{"tu_khoa": "christmas cactus, poinsettia care"}]
    d.goi_y_moc(moc, 0, lambda c: [c + " care", c + " meme"])
    assert moc[0]["goi_y_us"] == "christmas cactus: 1 · poinsettia care: 2"
