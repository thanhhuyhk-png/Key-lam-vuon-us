---
file: impressions-baseline-2026-09-02.md
role: Mốc gốc tầng ĐÓNG GÓI (impressions · CTR · view-5-ngày) để retro sau này có cái mà so
read_by: [yt-channel-health-audit, mkt-youtube-script-audit, skill-garden-us-pipeline]
đo: 2026-09-02
nguồn: YouTube Studio (CTR + impressions, nhập tay) + tools/yt_analytics.py health 12
---

# 📉 MỐC GỐC — tầng đóng gói · Senior Garden Guide · 02/09/2026

> **Vì sao có file này:** kho đang đo AVD rất kỹ và ⛔ không đo gì ở tầng trên nó.
> AVD chỉ chấm **người đã bấm vào**. Nút thắt của kênh nằm ở **trước cú bấm**, và trước hôm nay
> ⛔ không có con số nào để so.

---

## 1. Ba video mới nhất — số thật từ Studio

| Video | Đăng | Hiển thị | CTR | View | Người xem riêng biệt |
|---|---|---|---|---|---|
| Save a Dying Orchid in 5 Steps | 28/08 · 5 ngày | **3.300** | **2,7%** | 705 | 172 |
| 6 Lazy Perennials to Plant in Pots This September | 31/08 · 2 ngày | **2.800** | **2,7%** | 367 | 70 |
| 6 Houseplants to Bring Indoors Before Frost | 02/09 · vài giờ | 306 | 3,3% | 88 | — |

> ⚠️ Video 02/09 **chưa đủ tuổi để chấm** — ghi lại cho đủ bộ, ⛔ đừng dùng làm mốc.

**3.300 hiển thị / 62.100 người đăng ký = 5,3%.**

---

## 2. Nguồn kéo view — video MỚI vs catalog CŨ

| | Duyệt xem | **Video đề xuất** | Tìm kiếm |
|---|---|---|---|
| Orchid (28/08) | 86,5% | **—** | 4,1% |
| Perennials (31/08) | 79,6% | **6,5%** | 3,0% |
| Houseplants (02/09) | 87,5% | **—** | 1,1% |
| **Toàn kênh 28 ngày** | 62,8% | **22,3%** | 6,2% |

> Số toàn kênh do **catalog cũ** tạo ra — 20 video cũ giữ **97,6%** view, 15 video mới chỉ **2,4%**
> *(7.265 view / 15 video = 484 view/video)*.
>
> ## ⇒ Video cũ sống bằng ĐỀ XUẤT. Video mới chỉ được đẩy tới người đăng ký sẵn có, rồi chết ở đó.

---

## 3. Chuỗi nhân quả — chẩn đoán 02/09

```
mẻ thử nhỏ (~3.000 hiển thị)
        ↓
CTR về 2,7%  ← dưới ngưỡng mở rộng
        ↓
KHÔNG bao giờ ra khỏi mẻ thử  →  đề xuất ≈ 0  →  705 view  →  chết
```

**Giữ chân ⛔ không phải nút thắt.** Cùng cửa sổ: AVD 25,9% → **28,3%** (+2,4 điểm), đang tăng.
Đổi độ dài cũng ⛔ không phải đòn bẩy: dải 8–12′ (n=15) trung vị **628 view** vs 12–20′ (n=18) **636 view**.

---

## 4. 🎯 NGƯỠNG PHẢI VƯỢT — dùng cho retro

| Chỉ số | Mốc gốc 02/09 | Ngưỡng | Đọc ở đâu |
|---|---|---|---|
| Hiển thị / video mới | ~3.000 | **> 8.000** | Studio → Phạm vi tiếp cận |
| CTR | 2,7% | **> 4,0%** | Studio → Phạm vi tiếp cận |
| View 5 ngày đầu | 285 *(trung vị)* | **> 800** | `yt_analytics.py health` → `early_velocity.median_5d_views` |
| Đề xuất, video mới | ≈ 0 | **> 15%** | Studio → Cách người xem tìm thấy |

> ⏱️ **Đọc CTR ở giờ 48. ⛔ Đừng đợi view** — view là kết quả đến sau, CTR là nguyên nhân.

---

## 5. Hai nhánh kết luận — quyết ở phép thử tới

Sau 3 video đóng gói phổ thông *(theo `L9` + `L9b` trong `lessons-learned.md`)*:

| Kết quả | Nghĩa là | Làm gì tiếp |
|---|---|---|
| CTR **> 4%** và hiển thị **bật lên** | ✅ L9 đúng, đã sửa xong | Chuẩn hoá vào Title Engine + brief |
| CTR **> 4%** nhưng hiển thị **vẫn ~3.000** | 🔴 Người đăng ký đã nguội — 62.100 sub đến từ ~7 video phổ thông, ⛔ không phải khán giả senior | Bài toán khác: kích hoạt lại tệp sub, hoặc chấp nhận xây lại từ đề xuất |
| CTR **vẫn ~2,7%** | 🔴 Ảnh + tiêu đề còn vấn đề khác ngoài nhãn tuổi | Bóc thumbnail riêng, đừng đổ hết cho L9 |

---

## 6. ⛔ Hai chỗ trong kho đang MÂU THUẪN với L9 — phải sửa trước khi viết bài kế

| File | Câu cần sửa | Vì sao |
|---|---|---|
| `SLATE-2026-W34.md` § *"Luật riêng cho công thức trồng trong nước"* | *"Ba vế bắt buộc là **no soil · no bending · no cost** (theo L8). Đừng thay nội dung ba vế."* | Luật này **ép `no bending` quay lại title** — đúng thứ vừa thua A/B 40,3/59,7 và đúng thứ kéo cùng đề tài từ 973.416 xuống 15.891 |
| `BRIEF-5-SCRIPTS-SEPTEMBER.md` §0 | *"Ba kênh có Golden/Senior trong tên đều nằm trong nhóm outlier → thị trường trả thưởng cho senior-gardening"* | **Đúng ở cấp KÊNH, sai khi áp xuống cấp VIDEO.** Evergreen Seniors (119K, tên có "Seniors") có 0/10 top video mang chữ chỉ tuổi; bài duy nhất có = 855 view |

---

## 7. Còn thiếu

- **CTR lịch sử của 7 video triệu view** — chưa lấy. Có nó mới biết mốc CTR "thời còn ăn" là bao nhiêu, thay vì đoán ngưỡng 4%. `[CẦN SỐ: Studio → từng video giai đoạn 11/2025–04/2026]`
- **15 video đã rút khỏi công khai** (9 private + 6 đã xoá), mất **53.637 view** — chủ ý hay bị gỡ? `[CẦN XÁC NHẬN]`
