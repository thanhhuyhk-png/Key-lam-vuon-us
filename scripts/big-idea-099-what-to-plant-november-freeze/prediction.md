# Prediction — big-idea-099-what-to-plant-november-freeze

> Ghi tại GATE Script (19/11/2026). 7–14 ngày sau khi đăng, so với số thật trong `retro.md`.
> **Chấm chính:** views_5d so với trung vị 597 (`channel.config.json` → `scoring`) + giây xem/lượt + CTR Studio. ⛔ Không chấm bằng AVD% đơn lẻ.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-099-what-to-plant-november-freeze |
| **Hạng** | **AN TOÀN** (Topic Gate 2/3 thiếu ① · GO có điều kiện · không phải cú đánh lớn) · **TEST** (xem dưới) |
| Ngày scripted | 2026-11-19 (user duyệt script sau 3R 2 vòng) |
| Target publish | **≤ 28/11/2026** theo hạn trend 10 ngày (báo cáo `do_trend.py` 18/11) — **chưa có ngày chốt**; còn các bước thumbnail, giọng, dựng. Nếu không kịp, giá trị còn lại là từ khoá «what to plant in november» (4.167/th US) nhưng nhu cầu nguội sau 3–6 tuần. Xung đột lịch: 098 đang hướng 12–19/12 |
| Compliance score (lúc GATE) | **9/10** (R2 Opus, vòng 2 — fail mục 8 hedging, đã sửa 3 câu, **chưa chấm lại**; ước 10) · Agy vòng 2: 4 lỗi CHẶN đã sửa, chưa ai đọc lại |
| Độ dài | 1.837 từ ≈ 11,1′ @165 wpm (khung 10–14′) |

## Title bet
- **Title chốt:** `What to Plant in November: 5 Crops That Shrug Off 28°F` (user chọn A′ sau research; vidIQ không chấm — tool không có)
- Specific quantity? **Y** («5», «28°F»)
- Leading number? **N** — số đứng sau dấu hai chấm; keyword «what to plant in november» ở 25 ký tự đầu (KEYWORD-FIRST, L10)
- Keyword-first: **Y** — «what to plant in november» 4.167/th US (cạnh tranh 59, không có +30%); «november gardening» 9.502/th
- Độ dài: **10 từ / 54 ký tự**
- Thumbnail concept: `STILL GREEN` (lá sương, nhiệt kế) — bổ trợ title bằng KẾT QUẢ nhìn thấy; chi tiết `thumbnail-prompts.md`.

## Retention bets (3 luật cứng)
- **Topic familiarity:** **Y** — kale, cải bắp, củ cải, cải bó xôi, tỏi, cà rốt là rau quen với người Mỹ. Rủi ro: chủ đề **rau ngoài trời theo mùa**, không phải franchise hit kênh (aloe/bơ/giâm cành); video «16 Things Grandma Always Planted in October» chỉ 737 view (~1,3× trung vị).
- **Giây 40–55:** Loop #1 «hai cây bị loại, một cây cần lạnh» (gieo ~0:15, nhắc ~1:12) + giây 38–60 là M1 định nghĩa nhóm nhưng đã gài «Keep those two missing vegetables in mind» (L4 ✅, L15 ✅).
- **Phút 4–6:** bảng số phiếu 7 cây (Editorial Signature) + Loop #2 «lạnh đổi vị» + mini-loop cải bắp yếu / cải bó xôi tranh cãi / cà rốt chia phiếu / tỏi cần lạnh (mỗi 15–45 s). Jenga Retention: **ON** (4 loop, ≤2 chồng).
- Mốc loop thực tế (R2): #1 0:15→~5:45 · #2 ~2:58→~3:59 · #3 ~6:03→~8:16 · #4 ~8:24→~9:50.

## Engagement bets
- Themes: ☐ Nostalgia (chỉ «Our grandparents' generation read the sky» — 1 câu) · ☑ Pet safety (mulch ca cao độc cho chó, ASPCA, ở M3) · ☑ USDA zone/climate (mùa đông nhẹ vs lạnh: Texas, Sacramento, Iowa; mức thấp nhất trong dự báo)
- Câu kích theme: «What's the lowest low on your forecast this week? Tell me in the comments.»

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views_5d | trung vị 597 · an toàn ≥896 · bứt ≥2.982 | **P25 ~300 · P50 ~550 · P75 ~1.100** (ước tay, chưa qua `chi_so.py`). **P(≥896) ≈ 0,25 · P(≥2.982) ≈ 0,04** |
| AVD % | 25,6% (video 7–9′: 27–35%; ≥16′: 12–15%) | **~27%** (11′, listicle 5 cây + 2 tranh cãi, nhiều số nhưng thẻ đồ hoạ mang số) — phán đoán |
| CTR % (giờ 48) | video mới 10/10–07/11 1,3–1,6% | **~2,3%** — keyword «what to plant in november» + «28°F» cụ thể; không có «Amish»/«Stop» mạnh như 098 |
| Giây xem/lượt | watch-budget kênh ~195 s | **≥165 s** |

> Căn cứ: (1) trend 10 ngày ĐA_KENH (Gardenomics ×10,2 · Plant Explainer ×2,6 · Gathering Basket ×2,2) nhưng các kênh này nhỏ — Gardenomics 2.986 view sau 2–3 ngày; (2) ① kênh mình = ❌ → dự báo thấp hơn các video bám franchise; (3) các dự báo trước đều cao hơn thực (P50 1.110/1.085/919 → thực 649/316/290) nên giữ P50 ~ trung vị; (4) nhu cầu tìm kiếm mỏng (không +30%); (5) khán giả mục tiêu bị trend «cuối tháng 11» — đăng muộn hơn 28/11 giảm giá trị.

## TEST (ghi rõ để retro trả lời)
1. **TEST ĐỀ TÀI TỪ `do_trend.py` (đầu tiên):** video đầu tiên chọn chủ đề hoàn toàn từ báo cáo trend 10 ngày, không bám franchise hay Model Link. views_5d ≥896 → đường tìm chủ đề mới hoạt động; <400 → kiểm lại cổng ② (hệ số [ƯỚC], chưa có tăng/ngày [ĐO]).
2. **TEST TRỤC ĐÃ ĐỔI — «theo mức thấp nhất trong dự báo», không theo USDA zone** (đối thủ Gardenomics làm theo zone, không có số °F nào): CTR/giữ chân có tốt hơn mốc kênh không? Đếm comment nhắc «zone» vs «forecast».
3. **TEST KEYWORD «what to plant in november» (KEYWORD-FIRST):** % lưu lượng Search của video có vượt 5% (so 1,5% của kênh) không? Có +30% không (lần đo 19/11: không).
4. **TEST EDITORIAL SIGNATURE — BẢNG SỐ PHIẾU (4:15–5:00):** đường cong phút 4–6 có phẳng hơn 098/097 không? Comment có nhắc bảng/cà rốt không?
5. **TEST TRUNG THỰC «Plant» (mùa đông nhẹ vs lạnh):** comment có phàn nàn «tôi không gieo được ở vùng tôi» hay khen vì nói thẳng giới hạn?
6. **TEST CHỦ ĐỀ NGOÀI FRANCHISE (①❌):** rau ngoài trời theo mùa giữ ≥ trung vị 597 không? Nếu <400 → bỏ nhánh này, quay lại phần tiếp 5 hit cũ.

## Quy tắc dừng
- views_5d < 400 **hoặc** CTR giờ 48 < 2% → gói hỏng: đổi thumbnail trước (biến thể B), rồi mới đổi title (giữ «what to plant in november» ở đầu).
- views_5d ≥ 896 → đạt mức an toàn; làm tiếp 1 chủ đề từ báo cáo trend kế (không chép khuôn câu).
- views_5d ≥ 2.982 → làm phần tiếp «what to plant in [tháng kế]» ngay, giữ khung số + ngưỡng nhiệt.
