# Prediction — big-idea-095-root-cellar-humidity-zones

> Ghi tại GATE Script (16/11/2026). 7–14 ngày sau khi đăng, so với số thật trong `retro.md`.
> **Chấm chính:** views_5d so với trung vị 597 (`channel.config.json` → `scoring`) + giây xem/lượt + CTR Studio. ⛔ Không chấm bằng AVD% đơn lẻ.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-095-root-cellar-humidity-zones |
| **Hạng** | **AN TOÀN** (Topic Gate 3/3 · không phải cú đánh lớn) · **TEST** (xem dưới) |
| Ngày scripted | 2026-11-16 |
| Target publish | trước ~25/11/2026 *(phán đoán: đề tài trữ rau theo mùa; đăng càng gần đầu mùa đông càng hợp, sau T1 mất tính «làm ngay»)* |
| Compliance score (lúc GATE) | **9/10** (R2 Opus, vòng 2). Hai câu mục 8 đã sửa theo đề xuất để lên 10/10 nhưng **chưa được chấm lại độc lập**. Agy chấm thang riêng ~10/100 sau vá. gate.py PASS |
| Độ dài | 1.830 từ ≈ 11,1′ @165 wpm (khung config 10–14′) |

## Title bet
- **Title chốt:** `Root Cellar Without a Cellar: 3 Zones That Keep Veggies All Winter` (vidIQ 85; user chọn 16/11)
- Specific quantity? **Y** ("3 Zones", "All Winter")
- Leading number? **N**. «Root Cellar» đứng đầu để theo KEYWORD-FIRST (cụm rộng 16.893/tháng US). Số «3» nằm giữa title.
- Độ dài: **11 từ / 61 ký tự**
- Thumbnail test: A `98% vs 65%` (⭐, bổ trợ title bằng số đo, 0 từ trùng) vs B `NEVER TOGETHER` (tuyệt đối hơn nguồn «best not to» — chỉ dùng nếu cần test).

## Retention bets (3 luật cứng)
- **Topic familiarity:** **Y**. Cà rốt, khoai, hành, táo; «root cellar» quen với người Mỹ. Nối hit root cellar cũ (6.446 view, hạng 6/50).
- **Giây 40–55:** Loop #1 «the fruit people store right beside it» (mở 0:43) → nhắc ở ~3:30, ~4:55, 5:54 → đóng khi trả ethylene ở ~6:28.
- **Phút 4–6:** Loop #1 + Loop #2 («a warm, dark start», mở ~3:32 → đóng ~5:35) còn mở; Editorial Signature = bảng Zone Incompatibility Matrix; nhịp căng mỗi 15–40 s (tỏi/hành mềm, khoai ngọt, solanine, cảnh báo thú cưng). Jenga Retention: **ON**.

## Engagement bets
- Themes: ☑ Nostalgia (chỉ dạng chung, «a dug cellar») · ☑ Pet safety (ASPCA hành/tỏi + khoai xanh; nắp thùng) · ☑ USDA zone/climate (nhiệt kế sau đợt rét đầu, thùng chôn ở vùng lạnh)
- Câu kích theme: «Tell me in the comments where your coldest spot is, garage, porch or shed, and which zone it's going to be.» · «Keep those onion and garlic racks out of reach of pets.»

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views_5d | trung vị 597 · an toàn ≥896 · bứt ≥2.982 | **P50 ~700 · P25 ~400 · P75 ~1.500**. Cược: ngang trung vị; xác suất chạm mức an toàn ~35%, mức bứt ~5% |
| AVD % | 25,6% (video 7–9′: 27–35%; ≥16′: 12–15%) | **~28%** (11′, đề tài cơ chế + 2 loop) |
| CTR % (giờ 48) | 28d 5,5% · video mới 10/10–07/11 1,3–1,6% | **≥2,5%** (keyword «root cellar» có cầu tìm kiếm; thumbnail số đối lập) |
| Giây xem/lượt | watch-budget kênh ~195 s | **≥185 s** |

> Các số P25/P50/P75 là phán đoán, không do mô hình tính, và thận trọng hơn video 094 vì: (1) đề tài **ngoài thông số vàng W41** (trữ sau thu hoạch, không phải nhân giống); (2) cổng Topic Gate chưa tách được video thắng/thường (hiệu chỉnh 08/11: 3/3 → 0/3 thắng, n nhỏ). Chưa chạy phiếu san-y-tuong vòng B (còn ~20 credit trần) → chưa có dòng p_thang trong `research/du-bao.csv`.

## TEST (ghi rõ để retro trả lời)
1. **TEST ĐỀ TÀI NGOÀI KHUNG VÀNG:** trữ rau theo mùa (franchise «root cellar») có giữ được views_5d ≥ trung vị như video nhân giống không? Nếu có → khung vàng cần thêm mục «trữ».
2. **TEST BÁM MODEL LINK (Frugal Solutions):** đề tài + khuôn tiêu đề «Without… / 3 …» lấy từ Frugal Solutions — views_5d có vượt trung vị không? Trả lời cho quyết định tiếp tục bám hay thôi bám (mốc: 3 video bám mà không video nào ≥896 → thôi bám).
3. **TEST CƠ CHẾ «3 VÙNG ĐỘ ẨM» thay cho danh sách:** đường cong giữ chân có rơi ở ranh giới giữa các vùng hay giữ qua phút 4–6?
4. **TEST ĐỘ DÀI 11′:** giây xem/lượt và tổng giờ xem có ≥ video 8–9′ (125–178 s) không (lần thứ hai dùng khung 10–14′)?
5. **TEST THÔNG ĐIỆP TRUNG THỰC «không phải cả năm»:** câu bác lời hứa «full year» có làm CTR/bình luận khác không (comment có nhắc?).

## Quy tắc dừng
- views_5d < 450 **hoặc** CTR giờ 48 < 2% → gói hỏng: đổi thumbnail trước (B `NEVER TOGETHER` hoặc biến thể 1 củ cụ thể), rồi mới đổi title.
- views_5d ≥ 896 → đạt mức an toàn; làm tiếp phần 2 «ủ hành / ủ khoai» hoặc «thùng chôn ở vùng lạnh» nếu comment hỏi.
- views_5d ≥ 2.982 → làm phần tiếp ngay (3 vùng ở vùng khí hậu lạnh/nóng), giữ nguyên khung gói.
