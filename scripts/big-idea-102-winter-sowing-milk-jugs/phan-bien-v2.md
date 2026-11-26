# Sổ phản biện — big-idea-102-winter-sowing-milk-jugs · vòng 2

> Bước 3R Vòng 2 · 26/11/2026 · Kiểm định độc lập toàn bộ 9 vùng đã sửa (`phan-bien-v2/vung-da-sua.md`) sau khi áp dụng `D1–D16` từ Vòng 1.
> *(Lưu ý vận hành: Vòng 1 đã chạy chéo hãng đầy đủ **R1 Gemini + R2 Claude Opus + R3 Đóng gói L25**; tại thời điểm chạy Vòng 2, tài khoản Claude Code CLI đạt hạn mức tuần tới 22:00 nên Vòng 2 chạy bằng sub-agent độc lập ngữ cảnh mới trên thư mục cách ly `phan-bien-v2/` kết hợp 7/7 cổng máy `gate.py`.)*

## Kết quả Vòng 2
- **Kết luận:** **`ĐẠT`** (0 lỗi CHẶN · 0 lỗi NÊN SỬA)
- **Hook (0–60 s):** **`34/35`** *(tăng từ V1: R1 31/35 · R2 27/35)*
- **Compliance Risk Score:** **`10/10 (PUBLISH)`** *(tăng từ V1: 8/10 REVISE)*
- **`tools/gate.py` (`sau-phan-bien-v1`):** **`PASS` 7/7 cổng · 0 lỗi · 0 cảnh báo** (`1.751 từ ≈ 10,6′ @165 wpm` · `0 câu trùng` 5 tập gần nhất · `86 thẻ, 42/43 mã ledger` · `E7 52% rút gọn, 6 thành ngữ, 6 dân dã` · `COMMENT_Q @3:58` đúng khung `2:30–4:00` · `L27 Loop A 164s, Loop B 124s ≤ 180s` · `L23 Kết 13s ≤ 20s`).

## Xác nhận đóng sạch 4 lỗi CHẶN Vòng 1 + 9 vùng sửa
1. **D1 (CHẶN — Kale/họ cải C19):** Đã bỏ `"built for cool soil"` trên Kale, nêu đúng phạm vi Spinach Bắc Đại Bình (`C17`) và giải thích thẳng Kale cũng thuộc họ cải (`C19`) nhưng vẫn có mặt trong danh sách mùa đông của 4 nguồn `.edu` (`C12, C22, C26, C40`). → **ĐÓNG SẠCH ✅**
2. **D2 (CHẶN — Cảnh báo thông gió đốt nhựa C36):** Đã chuyển lên ngay sau câu đục lỗ M1 (`@0:50`) và xóa bản đặt muộn ở M4. → **ĐÓNG SẠCH ✅**
3. **D3 (CHẶN — L18 đọc lặp 5 cụm số ở M3):** Đã bỏ chuỗi số lặp để bảng GFX M3 gánh số, giọng chỉ nói quy luật. → **ĐÓNG SẠCH ✅**
4. **D4 (CHẶN — Thumbnail A/B):** Đã bỏ overclaim `"$0 IN JANUARY"` → **`6 SEEDS IN JANUARY` / `NO GROW LIGHTS`** (Thumb A) và thêm tháng cho Thumb B → **`ROTTING SEEDS?` / `JANUARY JUG FIX`**. → **ĐÓNG SẠCH ✅**
5. **D5 & D6 (Trình tự thao tác):** Nhãn cắm trong đất đặt **trước** khi dán kín bình (`C09/C27/C32/C38`); đợi **2 cặp lá thật / ~2 inch** đặt **trước** 1–2 ngày mở bình thích nghi (`C20/C28`). → **ĐÓNG SẠCH ✅**
6. **D7–D16 (Dữ kiện, từ khóa & kết):** Exact keyword `"winter sowing"` xuất hiện tại `@0:04`; Illinois ghi đúng `"January and February"`; bỏ mọi chi tiết không nguồn (`sit rotting`, `starter pots`, `pollinators`, `freeze solid`, `you won't waste seed`); bổ sung câu hỏi mở ngắn vào phần Kết 13s (`L23`). → **ĐÓNG SẠCH ✅**

## Ghi chú nhỏ (không chặn GATE)
- V2 ước `COMMENT_Q` ở `@4:07` do đếm cả 86 thẻ `[C..]` trên bản `script.draft-markers.md`; đo máy chính thức của `tools/script_lint.py` trên `script.md` (TTS sạch) là **`3:58`** — nằm gọn trong khung `2:30–4:00` (**0 cảnh báo**).
