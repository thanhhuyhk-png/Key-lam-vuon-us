# Hiệu chỉnh cổng chọn đề tài — 2026-11-25

Nguồn: `tools/du_bao.py cong` · số liệu YouTube Analytics lúc 2026-11-25T20:32:10.
Mốc: trung vị views_5d 10 video gần nhất = **596** → ngưỡng thắng 1,5× = **894**.

## Topic Gate (pipeline-state.md) ↔ kết quả thật

| Thư mục | Tín hiệu | Phán quyết | views_5d | So ngưỡng | Video |
|---|---|---|---|---|---|
| big-idea-058-garlic-in-pot | 3/3 | ƯU TIÊN | 544 | 🔴 dưới trung vị | Plant ONE Garlic Clove in a Pot Harvest a Full Head Next Sum |
| big-idea-059-ginger-store-bought | 3/3 | ƯU TIÊN | 779 | 🟡 ≥ trung vị | Why Your Grocery Store Ginger Won't Grow (And How to Fix It) |
| big-idea-060-pineapple-top | 3/3 | ƯU TIÊN | — | — | (chưa đăng / chưa ghép) |
| big-idea-061-potted-lemon-bloom | 2/3 | GO | 543 | 🔴 dưới trung vị | No Flowers on Your Lemon Tree? Count This 1 Number Tomorrow |
| big-idea-062-sunny-window-winter-veggies | 2/3 | GO-TEST | — | — | (chưa đăng / chưa ghép) |
| big-idea-093-pepper-overwinter | 3/3 | ƯU TIÊN | 289 | 🔴 dưới trung vị | Don’t Pull Your Pepper Plants Yet. They Can Live for Years |
| big-idea-095-root-cellar-humidity-zones | 3/3 | ƯU TIÊN | — | — | Root Cellar Without a Cellar 3 Zones That Keep Veggies All W |
| big-idea-096-winter-no-greenhouse | 2/3 | ƯU TIÊN CÓ ĐIỀU KIỆN | — | — | No Greenhouse Needed 5 Ways to Grow Food All Winter |
| big-idea-097-hardwood-cuttings-fruit-bushes | 2/3 | GO-TEST | — | — | (chưa đăng / chưa ghép) |
| big-idea-098-amish-no-till-fall | 2/3 | GO-TEST | — | — | (chưa đăng / chưa ghép) |
| big-idea-099-what-to-plant-november-freeze | 2/3 | GO có điều kiện | — | — | What to Plant in November 5 Crops That Shrug Off 28°F |
| big-idea-100-aloe-sequel | 2/3 | GO có điều kiện | — | — | (chưa đăng / chưa ghép) |

### Gộp theo số tín hiệu

| Tín hiệu | n có kết quả | Thắng | Trung vị views_5d |
|---|---|---|---|
| 3/3 | 3 | 0 | 544 |
| 2/3 | 1 | 0 | 543 |

## Danh mục 3 an toàn : 1 cú đánh lớn — 8 video gần nhất (bứt ≥ 5× = 2980)

| Ngày | Hạng | views_5d | Mức | Tiêu đề |
|---|---|---|---|---|
| 2026-11-25 | an toàn | — | — | No Greenhouse Needed 5 Ways to Grow Food All Winter |
| 2026-11-22 | an toàn | — | — | What to Plant in November 5 Crops That Shrug Off 28°F |
| 2026-11-20 | an toàn | — | — | Root Cellar Without a Cellar 3 Zones That Keep Veggies All W |
| 2026-11-11 | CÚ ĐÁNH LỚN | 850 | 🔴 dưới | You’re Throwing Away Free Plants: Root These 9 in a Glass of |
| 2026-11-06 | an toàn | 289 | 🔴 dưới | Don’t Pull Your Pepper Plants Yet. They Can Live for Years |
| 2026-11-03 | an toàn | 316 | 🔴 dưới | Rose Cuttings in a Potato One Small Study Found No Roots |
| 2026-10-28 | an toàn | 649 | 🔴 dưới | Geraniums Will Explode With Flowers If You Do This Now |
| 2026-10-26 | an toàn | 543 | 🔴 dưới | No Flowers on Your Lemon Tree? Count This 1 Number Tomorrow |

Cú đánh lớn trong 8 video: **1** (mục tiêu 2). Ghi `HẠNG: CÚ ĐÁNH LỚN` trong pipeline-state.md khi chọn đề tài.

## Sổ dự báo san-y-tuong (research/du-bao.csv)

Dòng cột `hang` = `cu-danh-lon` thì `nguong_thang_view` là ngưỡng BỨT (P(thắng) = P(≥ 5× trung vị)).

| Ý tưởng | Verdict | P(thắng) | P25–P75 | views_5d | Kết quả |
|---|---|---|---|---|---|
| Winter sowing bang binh sua (6-7 hat chiu lanh) | GO co dieu kien | 0.60 | 649–1612 | — | chờ |
| Giam canh phong lu (geranium cuttings) -> cay mien phi  | GO co dieu kien | 0.64 | 873–9571 | 649 | 🔴 |
| Rose cuttings in a potato? One small study found no roo | GO co dieu kien | 0.43 | 622–2863 | 316 | 🔴 |
| Giu cay ot qua dong trong nha (phan 2 Infinite Bell Pep | GO co dieu kien | 0.56 | 762–1122 | 289 | 🔴 |
| Hoa hong trong chau qua dong (goi y YouTube; goc re che | GO co dieu kien | 0.56 | 685–3791 | — | chờ |
| Dont Buy a Greenhouse: 5 Free Ways to Grow Food Through | GO co dieu kien | 0.30 | 400–950 | — | chờ |
| Stop Buying Fruit Bushes: Grow 6 for Free From Winter C | GO-TEST | 0.30 | 350–1300 | — | chờ |

Sổ có **3** dòng có kết quả.
Brier chạy khi đủ 5 dòng (còn thiếu 2).

> Cách đọc: cỡ mẫu nhỏ thì chỉ xem hướng, không đổi ngưỡng. Đề xuất đổi ngưỡng Topic Gate / san-y-tuong
> chỉ khi ≥ 8 video có kết quả, và chờ user duyệt (topic-gate-en.md mục HIỆU CHỈNH).
