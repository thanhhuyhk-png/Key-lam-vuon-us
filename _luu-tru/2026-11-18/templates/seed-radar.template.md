---
file: seed-radar-YYYY-Www.md
role: Kho seed remake của TUẦN. Sinh bởi R0 (radar tuần), tiêu thụ bởi R1 khi bắt đầu 1 video.
lane: REMAKE
cadence: 1 lần/tuần — KHÔNG chạy lại mỗi lần viết kịch bản
source: references/remake-playbook-en.md §R0
fetched_at: YYYY-MM-DD HH:MM
---

# Seed Radar — Tuần YYYY-Www

> ⚠️ Kho này là **chuỗi quan sát**, không phải lát cắt. Cột `clone_prev` lấy từ file tuần trước —
> đó là thứ cho biết cửa sổ đang mở hay đang đóng. Đừng xoá file tuần cũ.

## Tham số quét đã dùng

| | |
|---|---|
| **R0-A** săn seed *(0–1/tuần)* | `vidiq_similar_videos` seed từ video thắng đã biết — `matchOn:"both"` · `publishedWithin:"sixMonths"` · `minEngagementRate:0.015` · `maxSubscribers:60000` · `excludeSeedChannel:true` · `limit:45` |
| **R0-B** săn khuôn *(1–2/tuần)* | `vidiq_outliers` ngách **liền kề** — `publishedWithin:"threeMonths"` · `sort:"vph"` · `maxSubscribers:60000` · keyword hẹp (`appalachian cooking tricks` · `forgotten farmhouse skills` · `grandma kitchen tricks`) |
| Lượt bổ sung | `vidiq_outliers` ngách chính, **bắt buộc** `requireAllTitleTerms:true`, keyword là cụm hẹp, `publishedWithin:"sixMonths"` · `minVph:50` *(chỉ để cắt rác — ⛔ KHÔNG phải ngưỡng chấm đậu)* |
| Lượt đếm clone | `vidiq_similar_videos` mỗi ứng viên → đếm clone 14 ngày gần nhất (`minEngagementRate:0.02`) |
| 🔴 Lượt 3 **BẮT BUỘC** | `vidiq_video_stats granularity:daily` cho top 3 → tự tính `monthly_growth_pct`. ⛔ Không seed nào vào kho nếu chưa chạy lượt này |

> ⛔ **Hai lỗi đã sửa 04/09 — đừng lặp lại:** (1) `vph` từ `outliers`/`similar_videos` sai tới **100 lần**
> (`vrvLNbIL7tk`: báo 409,97 · thật 4,09) → chỉ dùng để XẾP HẠNG, không chấm đậu. (2) `publishedWithin:"thisMonth"`
> đá nhau với cổng tuổi 60–150 ngày của R1 → video ≤30 ngày không bao giờ qua nổi R1.

---

## Bảng seed — xếp theo `vph`, KHÔNG xếp theo view

| # | videoId | Title | Kênh / sub | View | **growth 30d %** | breakout | view/sub | Tuổi | clone_now | clone_prev | Đường cong | **Archetype** | Verdict |
|---|---------|-------|-----------|------|------------------|----------|----------|------|-----------|------------|-----------|---------------|---------|
| 1 | `` | | / | | % | | × | d | | | | A_ | ✅ NHẬN / ⏳ THEO DÕI / ❌ BỎ |
| 2 | `` | | / | | % | | × | d | | | | A_ | |
| 3 | `` | | / | | % | | × | d | | | | A_ | |

**Ngưỡng verdict** *(fail 1 = ❌)*
- `monthly_growth_pct` **≥ 5%** *(1–5% ⏳ theo dõi · <1% ❌ đuôi dài — remake một cái xác)*
- `breakoutScore` ≥ 15 · `view/sub` ≥ 5× · kênh gốc < 50K sub
- Tuổi **60–150 ngày** · `clone_now` **≤ 2**
- Đường cong = **NỞ** hoặc vừa qua đỉnh. CHÁY NHANH / CHẾT → ❌
- ⛔ Trượt bộ lọc **SEED PHẢI BỎ** (`remake-archetypes-en.md` §4: X1 conspiracy · X3 health-fear · X5 self-test persona · L9 tuổi người xem · X4 nguy hiểm) → ❌ bất kể số đẹp cỡ nào

**Cột Archetype:** phân loại nhanh bằng Q1 của `remake-archetypes-en.md` §2 —
`A1` cảm giác · `A2` hạn chót · `A3` tỷ lệ · `A4` lệnh cấm · `A5` phán quyết · `A6` port ngách khác.
Kho seed nên **đa dạng archetype**: 3 seed cùng A1 = 3 lần đặt cược vào một khuôn.

---

## Chi tiết seed #1 *(chỉ điền cho seed ✅ NHẬN)*

**Giải phẫu lời hứa (R2)** — chuẩn bị sẵn cho bước viết:

| Mảnh | Nội dung trong title gốc | Xử lý |
|---|---|---|
| 🔒 Sensory *(tài sản — khoá cứng)* | | giữ nguyên chữ, cả title lẫn thumbnail |
| Condition | | được mutate |
| Open question | | được mutate |

**Vật chủ gốc:** … → **có exotic không?** ☐ Có ☐ Không
*(Nếu Có → R3 bắt buộc: tìm cây bản địa/di sản Mỹ cho cùng lời hứa cảm giác này)*

**Đường cong 13 ngày đầu của seed:** ngày 1 … → ngày 13 … · đỉnh VPH … ở ngày …

**Ai đã remake seed này rồi:** *(liệt kê clone + view của chúng — đây là bản đồ chỗ trống)*

---

## Ghi chú tuần

- Seed nào tuần trước ⏳ THEO DÕI nay đổi trạng thái:
- Cửa sổ nào vừa đóng (clone nhảy lên ≥3):
- Keyword nào tuần này không ra gì → cân nhắc đổi:
