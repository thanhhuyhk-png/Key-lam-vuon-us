---
file: seed-radar-2026-W36.md
role: Kho seed remake tuần W36. Sinh bởi R0 (radar tuần). Tiêu thụ bởi R1 khi bắt đầu 1 video.
lane: REMAKE
cadence: 1 lần/tuần — KHÔNG chạy lại mỗi lần viết kịch bản
source: references/remake-playbook-en.md §R0-A + §R0-B
fetched_at: 2026-09-04
scanned: 85 kết quả (2 lượt vidiq_outliers + 1 lượt vidiq_similar_videos)
---

# Seed Radar — Tuần 2026-W36

> ⚠️ Đây là **tuần đầu tiên** → cột `clone_prev` trống. Từ W37 trở đi mới đọc được xu hướng cửa sổ.
> **Đừng xoá file này.**

## Bối cảnh kênh khi quét

| | |
|---|---|
| View tuần | W25 đỉnh **59.558** → W33 đáy **20.650** → W35 **27.172** *(-54% từ đỉnh, nhích lên 2 tuần gần nhất)* |
| AVD | 25,9% → **28,3%** *(+2,4 điểm — đang **tăng**)* |
| Catalog | 20 video cũ giữ **97,6%** view · 15 video mới chỉ **2,4%** = **484 view/video** |
| `median_5d_views` | **285** |

> 🔴 **Chẩn đoán:** AVD tăng trong khi view giảm ⇒ nút thắt là **impressions**, không phải giữ chân.
> Lane remake nhắm đúng nút thắt (packaging), nhưng tỷ lệ trúng ~1/50 ⇒ **không phải thuốc cấp cứu**.

---

## R0-A — SĂN SEED · kết quả: **0 seed đạt**

> ⚠️ **Bảng này đã sửa 04/09 sau khi chạy lượt 3.** Bản đầu tiên nhận `vrvLNbIL7tk` dựa trên
> `vph` do `similar_videos` trả về — **con số đó sai 100 lần**. Xem khối lỗi trong `remake-playbook-en.md §R0`.
> Chấm lại bằng **tốc độ tích luỹ tháng** (`monthly_growth_pct`), ngưỡng rút từ chính seed đã thắng.

| # | videoId | Title | Kênh / sub | View | `vph` **báo** | `vph` **THẬT** | Tăng/tháng | Tuổi | Verdict |
|---|---------|-------|-----------|------|-----------|------------|-----------|------|---------|
| 1 | `vrvLNbIL7tk` | Why Grandma Boiled Dish Rags | Tales From the Mutiny / 7,62K | 844.171 | ~~410~~ | **4,09** | +8.652 = **1,0%** | 87d | ❌ **BỎ** — đuôi dài |
| 2 | `VAOj6_hkXeQ` | The Forgotten Homemade Mosquito Trap… | Home Tips US / 2,10K | 321.667 | ~~163~~ | **4,9** | +2.922 = **0,9%** | 83d | ❌ **BỎ** — đuôi dài |
| 3 | `X_61ggFkBA4` | This Plant Is Poisonous… So Why Did Appalachians Eat It? \| Pokeweed | Kayla Jacquelyn / 3,29K | **73.443** | 112 | **27–246** | 33.826 → 73.443 trong **15 ngày** = **+117%** | **23d** | ⏳ **THEO DÕI** — sống thật, đang tăng tốc, nhưng **quá non** |
| 4 | `BvIO-IfExRQ` | Do These 7 Things to Your Tomatoes THIS WEEK | Easy Gardening for Seniors / 4,29K | 31.154 | 24 | *(chưa đo)* | — | 56d | ⏳ đo lại W37 |
| 5 | `ThxKrq0XxuI` | There's a Tree That Feeds 100,000 Bees… | Dale's Hive / 3,42K | 26.743 | 0 | — | — | 28d | ❌ vph = 0 |
| 6 | `L-vA5TrXemY` | 25 Genius British Grandma Cooking Tricks | Britain As It Was / 17K | 97.914 | 23 | — | — | **177d** | ❌ quá cửa sổ |
| 7 | `iX-3LzU6Zro` | More Nutritious Than Carrots. Plant It Once… | **Botanical Vault** / 24,3K | 5.010 | 2 | — | — | 105d | ❌ chết *(chính họ làm skirret và flop → cây không phải tài sản)* |

### ⏳ `X_61ggFkBA4` — ứng viên duy nhất còn sống, nhưng chưa nhận

Kéo theo ngày: **33.826 (20/08) → 73.443 (04/09)** = **+117% trong 15 ngày**, vph dao động 27–246 và
có ngày **tăng tốc trở lại** (Aug 31: 246). Đây là video **thật sự đang được đẩy**, khác hẳn hai cái trên.

**Vì sao vẫn chưa nhận:** mới **23 ngày**. Toàn bộ bằng chứng về thời điểm nhảy vào của tôi chỉ có
**n = 2** (Silas D+118, No Longer Here D+127). Nhảy vào lúc bản gốc còn đang leo là **chưa từng được kiểm chứng**
trong bộ dữ liệu này — và tôi vừa mắc lỗi vì bịa ngưỡng, nên lần này không bịa thêm cái nữa.

⚠️ Ngoài ra `pokeweed` là cây **có độc** — nếu làm phải khoanh vùng theo `CR5` rất chặt.

> **Kết luận R0-A tuần W36: KHÔNG có seed.** Đúng như dự báo cung 0–2/tuần — tuần này rơi vào **0**.
> ⛔ Không hạ chuẩn để lấp chỗ trống. Lane B1 tuần này **trống**, đôn lane A lên bù.

---

## R0-B — SĂN KHUÔN · mỏ không cạn

> 🔑 **Khác biệt then chốt so với R0-A:** săn khuôn **KHÔNG cần seed còn sống**.
> R0-A remake *cùng một video* → phải cạnh tranh cùng truy vấn → seed chết thì cửa sổ chết theo.
> R0-B chỉ mượn **cấu trúc** đem sang ngách khác → video nguồn tắt hay không **không liên quan**.
> ⇒ Vì vậy tuần nào R0-A trắng, **R0-B vẫn chạy được bình thường**. Đây là lane chống hụt cung.

Khuôn `số đếm + Forgotten/Grandma + thủ phạm kinh tế mềm` đang chiếm mọi ngách liền kề:

| Video nguồn khuôn | Kênh / sub | View | breakout | Port sang vườn |
|---|---|---|---|---|
| *25 Forgotten Diner Sandwiches America Used to Order Every Day* | Retro State / 9,19K | 673.367 | **863** | `25 Forgotten Vegetables America Used to Grow in Every Backyard` |
| *NEVER Grill Your Steak Again — 80-Year-Old Grandma Butcher's Method* | Margret Miller / 13,1K | 445.341 | **3.470** | `NEVER Prune Tomatoes Again — Try This 80-Year-Old Grandma Gardener's Method` |
| *25 FORGOTTEN Farmhouse Skills Every American Family Knew 100 Years Ago* | Forgotten American Skills / 28,3K | 137.992 | 28 | `25 Forgotten Garden Skills Every American Family Knew 100 Years Ago` |
| *20 Old-House Drainage Tricks Modern Builders Quietly Abandoned* | Forgotten Home Engineering / 6,04K | 55.215 | 8,1 | `20 Old Garden Drainage Tricks Modern Landscapers Quietly Abandoned` |
| *STOP Boiling & Frying Eggs The OLD WAY! 45 Appalachian Tricks* | Opal Rowe / 23,7K | 151.554 | 16,9 | `STOP Watering The Old Way! 25 Appalachian Garden Tricks` |

⛔ **Đã loại khỏi danh sách port:**
- `oFq7llORY0k` *"Ancient Herb Triggers Skin-Tightening Collagen… Why Doctors Never Mention It"* — YMYL + conspiracy y tế (`X3`, `X1`)
- `ZI5Ty2sFGng` *"OVER 60? Top 4 Vegetables That Save Your Kidneys…"* — nhãn tuổi người xem (`L9`) + YMYL, dù nó đang có 146K view

---

## Ghi chú tuần W36

- **Thời vụ:** `pRlNAhqUHXc` (9 Perennials September, breakout 56) quá non để remake nhưng **đúng mùa ngay bây giờ**
  → đây là bài của **lane A**, không phải lane B. Đề xuất đưa vào slate tuần này.
- **Cửa sổ sẽ mở:** `BvIO-IfExRQ` vào cửa sổ **W37**, `X_61ggFkBA4` vào **~W41**. Tuần sau kiểm lại `vph`.
- 🔴 **Việc phải sửa ngoài lane remake:** video *"Kill Weeds With Cardboard — No Bending, No Pain"*
  (**207 view/5 ngày**) vẫn đang mang nhãn `No Bending` trên title — **vi phạm `L9`**, luật đã chốt 02/09.
  Đổi title video này trước khi làm bất kỳ việc gì khác — nó là sửa 1 dòng chữ.
