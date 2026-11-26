# Phiếu kiểm định — Hạt đào/mận/anh đào (fruit pits) — 2026-10-24

**Verdict: SỬA GÓC (vòng 1/2)** — không phải GO. Vòng A: C2 Vàng · C3 Xanh · C6 Xanh · C0 Xanh. Vòng B: C1 Biên · C7 Vàng · C4 Biên · C5 Biên.
vidIQ tk3: 455 → 435 trong Vòng B (tiêu 20, trong ngân sách 30). Dữ liệu thô: `research/san-y-tuong-2026-10-24/`.

## C1 — Chỉ số cầu (mẫu `mau-c1-fruit-pits-v2.json`)
- Mẫu: 36 video long-form ≥4 phút, kênh <100K sub, 12 tháng, 3 truy vấn vidIQ (relevance + date). Dùng được 10 sau lọc (loại 14 không có OM, 11 kênh siêu nhỏ, 1 chưa đủ tuổi) → độ tin **trung bình**.
- ⚠️ **5/10 video dùng được thuộc một kênh (Expert Peaches) và OM của chúng là ƯỚC TÍNH** (view ÷ view điển hình của kênh, 3.085), vì vidIQ trả OM null. Bản chưa ước tính chỉ còn 5 video → `p_thang` bị script từ chối.
- THR (OM ≥1,5, đã làm mượt) **0,417** · breakout (OM ≥2) 0,333 · độ lặp lại **2 kênh** (Biên; cần ≥3) · biến động OM −57% (nguội) · đà tăng 6,97 (không đáng tin vì mẫu lệch).
- Dự báo (mốc 597 = views_5d trung vị kênh): P25 **405** · P50 **753** · P75 **1.339**; ngưỡng thắng ≈ 900. P(thắng) tham khảo **0,42** (độ tin thấp–trung bình, **thấp hơn geranium 0,64**).
- Điều quan trọng hơn con số: long-form "trồng cây từ hạt đào" phần lớn chỉ 1–5K view; chỉ vài ca vượt (Expert Peaches 326K tháng 6, Silas Mercer 68K, "1-hour soak" 42,7K OM 4,8). Video nổ nhất chủ đề là **Shorts time-lapse** (200K–700K), không phải long-form.

## C2 — Bão hoà (cập nhật sau Vòng B → Vàng, sát Đỏ)
Tiêu đề "Don't Throw Away Your Pits! Grow Peach, Plum, Cherry, Apricot & Almond Trees in Just 3 Steps" đã bị **≥18 kênh** đăng lại từ 7/2026 đến 10/2026; hầu hết <500 view (trung vị ~150), một vài bản 1–8,7K. Mình không dùng khuôn này, nhưng người xem/thuật toán đã thấy rất nhiều video cùng chủ đề.

## C7 — Video mồi: **Vàng**
- Từ khoá `grow peach tree from pit` (US): **<750/tháng**, mức "Very low". `vidiq_trending_videos` "peach pit": 0 kết quả.
- Video mồi long-form còn lại: Expert Peaches 326K (6/2026) và Silas Mercer 68K (8/2026), cả hai ≥2 tháng tuổi; không đo được VPH hiện tại và kênh nhỏ có cạnh chúng hay không (`[CHƯA ĐO]`).
- → chủ đề không sống bằng tìm kiếm; sống bằng đề xuất mà chưa có bằng chứng.

## C4 — Chất liệu: **Biên**
Mở đọc được **1 trang** hạng A: **Iowa State Extension "Germination of Tree Seed"**:
- Lạnh 33–41°F (nhóm *Prunus*); đào 98–105 ngày, mận châu Âu 90 ngày, anh đào chua 90–150 ngày.
- Trồng sâu 2 inch (đào, mận), 1/2 inch (anh đào chua).
- "Hạt của hầu hết anh đào, mận, đào trồng **không** giống cây mẹ" (not true to type).
- Có thể gieo ngoài trời mùa thu; nếu không thì gieo hạt đã lạnh vào mùa xuân.
Ba trang khác (Oklahoma State, UGA B818, UC) **bị chặn 403** khi mở → mới chỉ thấy tên trong kết quả tìm kiếm; không được dùng số từ chúng. Thiếu: tỷ lệ nảy, mất khả năng nảy sau ~1 năm (chỉ từ Ask Extension, chưa mở), thời gian tới khi ra quả, ghép/mắt. Chưa đủ cho deep-dive 18–24′ (cần thêm ≥2 trang mở được).

## C5 — Hình ảnh: **Biên** (ước, chưa đếm theo từng chương)
`garden_lib.py find`: **peach 0 · pit 0 · plum 0 · fridge 0**; seedling/seed/pot 40 mỗi từ · hands 29 · soil 14 · sprout 10 · cherry 9. Cảnh then chốt (hạt đào, đập vỏ, túi giấy trong tủ lạnh, cây non) phải tải mới hoặc AI POV. Chi phí 2.

## C3/C6/C0 (từ Vòng A, giữ nguyên)
C3 Xanh (khác 2 trục: không hứa kết quả · có mốc mùa). C6 Xanh (có "phần phân tích riêng": cây không giống quả mình ăn). C0 Xanh: `Plant a Peach Pit? What You Will Really Get (Do It This Fall)` 94 điểm.

## SỬA GÓC — đề xuất ≥2 góc mới (đổi trục, chạy lại Vòng A)
1. **"Không tủ lạnh": gieo hạt ngoài trời mùa thu** — đổi *phạm vi/cách kể* từ "5 loại quả, 3 bước" thành 1 việc lười (Iowa State: có thể gieo ngoài trời mùa thu). Thử tiêu đề: `Plant a Peach Pit This Fall: No Fridge, No Fuss`. Cần thêm 2 trang hạng A mở được xác nhận điều kiện (vùng lạnh, chuột, độ ẩm).
2. **"Cây từ hạt sẽ cho gì":** đổi *nghịch lý* sang kết cục thực tế (không giống quả đã ăn, bao lâu có quả, cần ghép) — kéo khán giả ưa Shorts time-lapse nhưng bằng long-form có số. Rủi ro: cần nguồn về thời gian ra quả/ghép chưa mở được.
3. (Dự phòng) Chuyển sang ý #2 trong phiếu 24/10: **khoai tây giâm hồng** (cầu hồng lớn hơn; bản hoài nghi chưa được kiểm chứng ăn view).

## Điều kiện để GO
≥2 trang hạng A bổ sung mở được (thử Texas A&M AgriLife, Penn State, Clemson HGIC, MSU) · một góc mới qua lại C2 · kiểm kênh nhỏ có cạnh Expert Peaches trong đề xuất (mở trang video trong trình duyệt).

*Chưa ghi `du-bao.csv` (chỉ ghi khi GO).*


---
## Vòng A lại — góc "gieo hạt ngoài trời mùa thu, không tủ lạnh" (24/10, vòng sửa 2/2)
vidIQ tk3: 435 → 420 (tiêu 15, chấm 3 tiêu đề). Kết quả: **Vòng A QUA, nhưng cổng cầu không đổi nên chưa đủ để làm.**

| Cổng | Mức | Ghi chú |
|---|---|---|
| C2 | **Xanh** | NexLev, 20 kết quả "plant peach pit outside in fall no fridge" (12 tháng): chưa ai làm đúng góc này. Gần nhất: Expert Peaches `-M8RHVcWmKw` (3,8K, 23′) chỉ so tủ lạnh với ngoài trời như một phần; "No Waiting…" 88 view. Khuôn "Don't Throw Away Your Pits!" không dùng. Nội bộ 0% |
| C3 | **Xanh** | "Expert Peaches nói cả hai cách trong 1 video dài. Mình chỉ nói *cách lười, và cái giá của nó* (ẩm khó theo dõi, loài gặm nhấm ăn hạt), vì hai trang extension cùng cảnh báo." |
| C6 | **Xanh** | Phần phân tích riêng: bảng "tủ lạnh vs ngoài trời" từ các trang extension, kể cả chỗ **chưa ai có số** (tỷ lệ nảy khi gieo ngoài trời, ranh giới zone). Không vùng đỏ |
| C0 | **Xanh** | 92: `No Fridge? Plant Peach Pits Outside This Fall (Here Is the Catch)` (65 ký tự) · 90: `Plant a Peach Pit This Fall: No Fridge Needed (What Happens by Spring)` (70) · 88: `Peach Pit in the Fridge or in the Ground? What Extension Says` (61) |

### Trang extension mở đọc được (C4) — đã mở thật
1. **Iowa State Extension — Germination of Tree Seed** (từ Vòng B): lạnh 33–41°F; đào 98–105 ngày, mận châu Âu 90 ngày, anh đào chua 90–150 ngày; gieo sâu 2 inch (đào, mận), 1/2 inch (anh đào chua); hạt không giống cây mẹ; **"có thể gieo ngoài trời mùa thu"**.
2. **Utah State Extension — Nanking cherry in the garden** (*Prunus tomentosa*, họ hàng anh đào; **không phải đào**): "plant the seeds outside in the fall and allow natural temperatures to achieve stratification"; ngoài trời **khó theo dõi độ ẩm** và **hạt có thể bị gặm nhấm ăn**; trong nhà 32–45°F, cần **100 ngày** lạnh.
3. **WSU / Pacific Northwest Extension — Propagating Plants from Seed** (PDF 24 trang, bảng 4): nhiệt độ ngâm lạnh **đào 41°F, mận 41°F, anh đào 35–45°F, anh đào ngọt 40°F** (+ ủ ấm 70°F 20 ngày); **số ngày không đọc được từ văn bản trích** → `[UNREADABLE]`, không dùng.
4. Illinois Extension news release "Do you know the secret…": **không** khuyến nghị gieo ngoài trời mùa thu cho cây ăn quả, chỉ nói cây con thường thành thức ăn cho thú; không đủ cho góc này.
Bị chặn khi mở: Oklahoma State (403), UGA B818 (403), UC (403), UMD (lỗi chứng chỉ).

### Khoảng trống chưa có nguồn (phải ghi `[NEED DATA]`)
Tỷ lệ nảy khi gieo ngoài trời; ranh giới zone (một blog nói vùng lạnh được, một blog nói chỉ zone 7–9; mâu thuẫn, chỉ là blog hạng D); cách chống chuột cho hạt; bao lâu có quả; mất khả năng nảy sau ~1 năm (chưa mở được trang).

### Phán quyết
- Vòng A: Xanh ×4. **Nhưng** C1 (Biên, THR 0,42, 2 kênh), C7 (Vàng: <750 tìm kiếm/tháng, không video mồi sống), C4 (Biên: 2 trang thật cho đào/mận/anh đào và 1 trang cho họ hàng) **không đổi**, vì đây vẫn là cùng chủ đề; đổi góc không tạo ra nhu cầu mới.
- Dự báo giữ nguyên: P25 405 · **P50 753 · P75 1.339** so với ngưỡng ~900 → **kỳ vọng nằm dưới ngưỡng thắng**. Chất liệu chỉ đủ khoảng 8–12′, không tới khung 20–24′ của kênh.
- **Khuyến nghị: GO có điều kiện, ưu tiên thấp** — chỉ làm nếu cần video thứ hai trong tháng 11 và chấp nhận bản ngắn (TEST độ dài); không đáng hơn geranium. Ý tiếp theo nên là **khoai tây giâm hồng** (chạy Vòng B).
