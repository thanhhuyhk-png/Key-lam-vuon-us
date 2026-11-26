# Prediction — remake-001-october-planting

> Ghi tại **GATE Script**, 2026-09-04, ngay khi approve script. Đây là **cược**, không phải kỳ vọng.
> 7–14 ngày sau publish → diff với số thật trong `retro.md`. Không có file này thì không diff được.

| Trường | Giá trị |
|---|---|
| Video | `remake-001-october-planting` |
| **Lane** | **B — REMAKE** *(video lane B đầu tiên của kênh)* |
| Ngày scripted | 2026-09-04 |
| Target publish | **16–20/09/2026** *(trước tháng 10 khoảng 11–15 ngày)* |
| Compliance score lúc GATE | **10/10** *(ngưỡng edible-adjacent ≥10)* |
| Độ dài | 3.345 từ · **22,3 phút** |

---

## Title bet

- **Title chốt:** `16 Things Grandma Always Planted in October (Before the First Frost)`
- **Á quân (swap giờ 48 nếu CTR < 4%):** `16 Things to Plant in October - The Last Window Before Frost`
- Specific quantity? **Y** — `16` · `7` · `October` · `first frost`
- Leading number? **Y** — `16`
- Độ dài: **11 từ / 67 ký tự** *(target ~12 từ / 65 ký tự)*
- Neo pipe? **KHÔNG** — browse-intent, theo `ANCHOR-INTENT RULE`. Keyword đẩy xuống description + tags.
- vidIQ CTR score: **93/100** *(bản á quân 89/100)*

---

## Retention bets (3 luật cứng)

- **Topic familiarity** — cây phổ biến với người Mỹ? **Y**. Cả 16 mục đều là cây quen (tỏi, spinach, kale, collard, radish…). ⛔ 0 cây exotic. Đây là `L1`, luật đã giết video Tamarillo (AVD 11,7%).
- **Giây 40–55 (`L4`)** — open loop giữ người xem qua vùng chết:
  → *"One of them has a leaf you should never eat, and I will flag it when we get there."* — mở **giây 39,2**, đóng **phút 4:14** (mục rhubarb).
  → Loop thứ hai chồng lên: câu tự-xác-định *"Did your first frost come before November, or after?"* tại **giây 63,6**.
- **Phút 4–6 (`L5`)** — tension layer: loop #1 (*"bảy cái nào là của tôi?"*) mở **giây 49**, đóng **phút 10,4** → bắc trọn vùng dip. Cộng **PATTERN BREAK #1** tại phút 5:10 (nguyên tắc mulch sau khi đất đóng băng). Jenga Retention: **ON**.

---

## Engagement bets

Themes nhắm tới: ☑ **Nostalgia/đa thế hệ** ☑ **USDA zone/climate** ☑ **Pet safety** — **trúng cả ba**.

| Theme | Câu kích |
|---|---|
| Nostalgia *(gold)* | *"John Bartram was growing it in Philadelphia in the seventeen thirties… That plant was in colonial dirt before this country had a name."* |
| USDA zone | *"Did your first frost come before November, or after? Hold that answer."* — 15 lần chữ `zone` trong script |
| Pet safety | *"Say that out loud once if there are grandchildren in the yard. Or a dog or a cat that chews on things."* |

---

## Dự đoán số (so baseline kênh)

| Chỉ số | Baseline kênh | **DỰ ĐOÁN video này** | Cơ sở |
|---|---|---|---|
| **views 5 ngày đầu** | median **285** | **600 – 900** | Packaging mạnh hơn hẳn (CTR score 93) + thời vụ + đăng trước tháng đích. Nhưng kênh vẫn trong browse demotion → không dám đoán 4 chữ số |
| **AVD %** | 28,3% (W35) | **18 – 22%** | ⚠️ **Dự đoán THẤP HƠN baseline, có chủ đích.** Video dài gấp 2,2 lần. Watch-budget kênh ~211s; nếu budget đứng yên thì AVD = 211/1338 = **15,8%** |
| **Tổng giờ xem** | video 9′ điển hình ≈ **12 giờ** *(285 × 9′ × 29%)* | **45 – 70 giờ** | 750 × 22,3′ × 20% ≈ 56 giờ. **Đây mới là thước đo thật** |
| **CTR %** | video mới median **2,0%** | **2,5 – 3,5%** | Title có số + cụm khẩn cấp; thumbnail có số + hệ quả cụ thể (pattern 2,7% của kênh) |
| Comment/1K | 3,0 | **4 – 7** | Comment bait hỏi zone — trúng theme #2, và câu hỏi dễ trả lời |

> ⚠️ **AVD sẽ tệ hơn baseline và đó là điều đã lường trước.** Nếu retro chấm bằng AVD thì video này
> "thất bại" gần như chắc chắn. **Chấm bằng `views_5d` vs 285 và TỔNG GIỜ XEM.**
> Đây đúng là bài học đã ghi trong `lessons-learned` 02/09: *"đừng chấm title bằng AVD"* —
> ở đó AVD 49% thua AVD 24,6% tới **20,7 lần** về tổng giờ xem.

---

## Ba giả thuyết có thể bác bỏ

| # | Giả thuyết | Đúng nếu | SAI nếu |
|---|---|---|---|
| **H1** | Listicle dài nạp lại watch-budget — mỗi mục là một open loop mới | Tổng giờ xem > **25 giờ** *(gấp đôi video 9′ điển hình)* | Tổng giờ xem < 15 giờ ⇒ **budget 211s là trần cứng, độ dài không phá được** ⇒ rollback `L7` |
| **H2** | Title có cụm khẩn cấp + tuổi của NGUỒN thắng nhãn tuổi người xem | CTR > **2,0%** | CTR ≤ 2,0% ⇒ packaging không phải nút thắt như `health-log` W33 kết luận |
| **H3** | Kiến trúc chia zone khiến người xem tự phân loại → tăng tương tác | ≥ **30%** comment có nhắc zone/bang/frost | < 10% ⇒ kiến trúc zone chỉ phục vụ compliance, không phục vụ retention |

---

## Điều kiện rollback lane B

Ghi trong `channel.config.json → lanes.remake._warn`. Nhắc lại ở đây để retro không phải đi tìm:

> Sau **3 video lane B**: nếu median `views_5d` **≤ 285** → **rollback về 10 phút**.
> Giữ lại R2 (khoá mảnh sensory) · R3 (đổi vật chủ) · R5 (ảnh mới, giữ chữ) — ba cái này **không phụ thuộc độ dài**.

---

## Rủi ro đã biết, không che

1. **`L7` đang bị vi phạm có chủ đích.** 22,3 phút vs target 8–10. Bằng chứng ủng hộ đến từ **Plant Explainer**, không phải từ kênh này. Dải 20–40′ của kênh chỉ có **n = 2**.
2. **Nhóm 3 chiếm 6 phút cuối và chỉ dành cho zone 8b–9.** Khán giả miền Bắc — có thể là phần đông — ngồi qua đoạn đó không dùng được gì. Đã đặt gác cổng để họ biết trước, nhưng đuôi vẫn mỏng.
3. **Thời vụ = cửa sổ hẹp.** Trễ hạn 20/09 thì giá trị rơi rất nhanh. Bằng chứng: Earthly Gardening (43,1K sub) đăng muộn 12 ngày → **4.237 view**, so với Plant Explainer (6,16K sub) đăng sớm 10 ngày → **103.211 view**.
4. **Đây là video lane B đầu tiên.** Không có tiền lệ nội bộ để so. Mọi con số dự đoán ở trên đều suy từ kênh ngoài.
