# Chẩn đoán kênh Garden US — vì sao video mới kẹt ở vài trăm đến 1–2K view (2026-11-08)

Nguồn: YouTube Analytics OAuth của kênh (188 video long-form công khai, view trọn đời, views_5d, AVD, giây xem, sub, nguồn lưu lượng) + `references/health-log-garden-us-60k.md` (impressions/CTR nhập tay từ Studio — API không có). Không tốn credit vidIQ. Số thô: `research/video-5d.json`; script đo nằm ở scratchpad phiên 08/11.

## 1. Kênh theo tháng
| Tháng | View kênh | Sub + | Video đăng | Trung vị view trọn đời / video | Video ≥ 5K |
|---|---|---|---|---|---|
| 01 | 1.155.547 | 15.276 | — | — | — |
| 02 | 722.219 | 8.212 | 21 | 1.269 | 4 |
| 03 | 1.118.969 | 13.954 | 31 | 795 | 3 |
| 04 | 1.568.112 | 13.107 | 29 | 1.393 | 5 |
| 05 | 395.414 | 4.074 | 31 | 501 | 1 |
| 06 | 226.103 | 1.764 | 20 | 361 | 0 |
| 07 | 120.206 | 1.085 | 15 | 366 | 0 |
| 08 | 104.197 | 930 | 17 | 298 | 0 |
| 09 | 112.509 | 595 | 14 | 658 | 0 |
| 10 | 87.507 | 497 | 8 | 669 | 0 |

- Tỉ lệ video đạt ≥ 3× trung vị cùng giai đoạn: T2–4 **20 %** · T5–8 **5 %** · T9–11 **0 %**.
- 91 % view hiện nay đến từ catalog cũ. Video mới nhận 2–7K impressions, CTR 2,4–2,9 % (catalog cũ 6,2 %).
- 24 video từ T9 đến nay đem về tổng cộng **9 sub** (theo số từng video).

## 2. Nguyên nhân, xếp theo độ chắc
1. **Video mới không bao giờ ra khỏi mẻ hiển thị đầu** (chắc). Mọi hit của kênh đều 88–96 % từ Browse — khác biệt nằm ở chỗ YouTube có mở rộng sang khán giả lạnh hay không. Mẻ đầu 2–7K impressions × CTR ~2,5 % ≈ 100–200 click Browse → ~600 view, rồi dừng.
2. **Tệp 50K sub được "mua" bằng 3–4 video viral rộng** (khá chắc). 7 cây trồng trong nước 985K, 6 cỏ dại quý 937K, Stop rooting in water 182K, Bug-free 104K. Người xem đến vì lời hứa rộng (đồ ai cũng có, miễn phí, đảo niềm tin), không vì "sửa lỗi một cây". Mẻ thử đầu đi vào tệp này → CTR thấp → không mở rộng.
3. **Bộ luật + cách chọn đề tài đã cắt hết nguyên liệu tạo outlier** (khá chắc, tương quan). Hệ số view so với video không có đặc điểm, trong T2–4:
   | Đặc điểm tiêu đề | T2–4 | T5–8 | T9–11 (đang dùng) |
   |---|---|---|---|
   | free / $ / never buy | **×3,86** (15/81) | ×1,24 | gần như bỏ (2/22) |
   | Đảo niềm tin "Stop / Never … Instead" | **×1,43** (40/81) | ×1,01 | **0/22** |
   | Danh sách ≥ 5 món | ×1,63 | ×0,78 | ×0,82 |
   | Khoa học / kiểm chứng / extension | — | ×0,75 | ×0,85 |
   | Tháng / mùa | — | ×0,66 | ×0,91 |
   Cổng hiện tại tối ưu cho **không trượt** (trung vị ~600 rất đều) chứ không cho **bứt**. Luật SLATE W40 ③ "MỘT cây" và lệnh cấm khung "Don't" (rút từ n = 13, gộp chung đảo niềm tin với sợ/mất) chặn đúng khung thắng của kênh.
4. **Bị hạ hạng Browse từ ~29/04** (đã ghi ở `channel-truth.md`): sau viral 926K có AVD 23,9 %, kèm nhịp 31 video/tháng nhiều biến thể na ná. Chưa rõ còn dư âm không.
5. **Độ dài** — số chưa rõ ràng: video 15–20′ ở T9–11 có AVD 12 % và giây xem 124 s (thấp hơn video < 10′: 148 s), nhưng n = 2–4. Không phải nguyên nhân chính; nên xét lại quy định 20–24′.

## 3. Sequel của hit cũ — không còn tự ra view
Sau T5, gần như mọi phần tiếp của các dòng hit chỉ được 150–1.500 view (vd Grow Herbs in Water 427, Stop Pulling 12 Weeds 234, Aloe rooting 335–453). Hit đến từ **gói lời hứa cụ thể**, không từ chủ đề. ⇒ Franchise (tín hiệu ①) là điều kiện cần, không đủ.

## 4. Bổ sung từ export Studio 10/10–07/11 (user gửi 08/11)
File: `research/studio/noi-dung-2026-10-10_2026-11-07.csv` (bản gốc ở `research/studio/_raw-2026-10-10_2026-11-07/`). Cửa sổ 29 ngày: 74.489 view · 420.358 impressions · CTR 5,95 % · 196 sub · $357.
- **8 video mới chỉ chiếm 13,5 % impressions và $14 / $357 doanh thu.** Catalog cũ (Aloe 123K impressions CTR 6,4 % · Avocado 95K 7,0 % · Stop Rooting 30K 7,9 %) nuôi kênh.
- **Sửa chẩn đoán mục 2.1:** YouTube **có** thử mở rộng một số video mới — Pineapple 14.232 impressions, Lemon 15.206 — nhưng CTR với người xem lạnh rơi còn **1,62 % và 1,33 %** (catalog cũ trung vị 5,4 %). Video có CTR khá (Christmas Cactus 3,14 %) lại chỉ được 3,8K impressions. ⇒ Nút thắt hiện tại là **gói (tiêu đề + thumbnail) không kéo được người lạ**, không chỉ "không được thử".
- Tiêu đề hai video bị mở rộng rồi tắt đều tự làm yếu lời hứa: "(It Takes 2 Years!)" báo trước là lâu; "Light Hours Extension Guides Actually Recommend" là khung khoa học (hệ số CTR ×0,68 ở 8 video mới; mẫu rất nhỏ).
- Video ≥ 16′: AVD 12–15 %; video 7–9′: 27–35 %.
