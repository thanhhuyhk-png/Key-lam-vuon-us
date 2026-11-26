# Phân tích toàn diện quy trình Garden US — 22/11/2026

> Số liệu: `tools/yt_analytics.py health` (27/09–22/11), `tools/kiem_dinh_ky.py` (188 video, retention từng video),
> export Studio 10/10–21/11, `research/hieu-chinh-cong.md`. Mọi số dưới đây đo hôm nay, không ước đoán.

## A. Chẩn đoán — 6 điểm gãy

| # | Điểm gãy | Bằng chứng | Mức |
|---|---|---|---|
| 1 | **Kênh sống bằng catalog cũ đang nguội** | Video cũ giữ **93,4 %** view; 13 video mới chỉ góp 6,6 %. View tuần 22.307 (W41) → 18.395 (W46), −18 % | 🔴 |
| 2 | **Đóng gói là trục yếu nhất** | CTR video ≤45 ngày trung vị **2,40 %** so với 4,35 % của video cũ. Browse chiếm **70,6 %** traffic, nên CTR quyết định lượt hiển thị. AVD ổn định 29–30 % | 🔴 |
| 3 | **Vòng phản hồi chưa từng chạy** | 47 thư mục có `prediction.md`, chỉ **1** có `retro.md`. Task định kỳ duy nhất đã **tắt từ 09/06**. `du_bao.py` ghép nhầm 096 với video tháng 2 → sổ ghi một «thắng» 18K giả (đã sửa 22/11) | 🔴 |
| 4 | **Cổng chọn đề tài chưa dự đoán được** | Topic Gate 3/3 «ƯU TIÊN»: 0/3 thắng (544 · 779 · 290). `san-y-tuong` cho P(thắng) 0,43–0,64 nhưng 0/3 thắng → quá tự tin. Mẫu nhỏ, chưa đổi ngưỡng (luật ≥8 video) | 🟡 |
| 5 | **Luật tăng nhanh hơn luật được đo** | 25 luật ACTIVE, phần lớn ghi «chưa có retro». ~5.400 dòng quy tắc + 8 GATE + 3R 2 vòng mỗi video. Nhịp đăng **3 video / 14 ngày** | 🟡 |
| 6 | **Video tốt nhất 2 tháng qua nằm ngoài pipeline** | «Nobody Believed Dragon Fruit Could Survive on Desert Sand — Until This Happened»: CTR **4,41 %**, views_5d **1.182** (gấp 2 trung vị). Không có thư mục nào trong `scripts/` | 🟡 |

**Tín hiệu tốt:**
- Video ≤12′ có views_5d gấp **1,54** lần video >12′ (n = 43 so với 42, 180 ngày gần nhất).
- Lane B remake tháng 9: trung vị 763 so với Lane A cùng tháng 531 (**×1,4**, n = 3).
- Hai video 10–11′ sau 10/11 đạt views_5d 850 và 1.182, cao nhất kể từ tháng 9.

## B. Đã làm hôm nay

1. `tools/kiem_dinh_ky.py`, 0 credit:
   - đo retention mọi video ≥7 ngày (còn lại @0:30, 1:00, 2:00, 4:00; giây rơi mạnh nhất);
   - đo bình luận trên 1K view;
   - đọc CTR từ export Studio (API không trả CTR, đã thử);
   - ghi `retro-auto.md` vào 48 thư mục;
   - chấm từng luật bằng nhóm áp luật so với nhóm không áp;
   - ghi báo cáo `research/kiem-dinh-ky/latest.md`.
2. Task `garden-us-kiem-dinh-ky` chạy CN + T4 lúc 20:00:
   - đo và dò trend;
   - CN tự viết `retro.md` cho 3 video mới nhất và nối vào Evidence log;
   - đề xuất hiệu chỉnh luật **chờ duyệt**, không tự sửa ACTIVE RULES.
3. Vá `du_bao.py`: không còn ghép thư mục với video đăng trước khi ý tưởng ra đời.
4. CLAUDE.md: bỏ dòng sai «routine weekly vẫn chạy».

## C. Đề xuất nâng cấp, xếp theo đòn bẩy

### C1. Đóng gói trước, viết sau (đòn bẩy #1, áp ngay)
- **Sửa gói 3 video có nhiều lượt hiển thị nhưng CTR thấp.** Mỗi lần sửa chỉ đổi tiêu đề **hoặc** thumbnail, rồi so CTR 7 ngày:

  | Video | Lượt hiển thị (28 ngày) | CTR | Hướng sửa |
  |---|---|---|---|
  | No Flowers on Your Lemon Tree? Count This 1 Number Tomorrow | 15.569 | 1,35 % | bỏ số trừu tượng (L21), hứa kết quả: «No Flowers on Your Lemon Tree? Fix It With This Free Trick» |
  | Geraniums Will Explode With Flowers If You Do This Now | 7.590 | 2,58 % | thumbnail Before → After hoa nở, chữ «2× FLOWERS» |
  | Rose Cuttings in a Potato One Small Study Found No Roots | 2.836 | 2,22 % | bỏ «Study» (L21), đảo niềm tin: «Stop Rooting Roses in Potatoes — Do This Instead» |
- **Mỗi video mới dùng «Test & Compare» của YouTube Studio với 3 thumbnail.** Người phản biện R3 đề xuất 3 phương án, nên thumbnail không còn là bước làm sau cùng.
- Đo bằng `kiem_dinh_ky.py`, cột CTR.

### C2. Khai thác catalog đang kéo view (tuần này)
- Aloe (23K view / 28 ngày), Avocado (16K), Rooting cuttings (7K) vẫn là nguồn browse chính.
- **Cứ 4 video thì 1 video là phần tiếp theo trực tiếp của một video top-5**, cùng chủ thể nhưng góc mới. Đây là cổng ① của Topic Gate.
- Gắn end screen và thẻ từ video mới về video gốc, và ngược lại.

### C3. Nhịp đăng: đường nhanh cho đề tài an toàn (✅ user duyệt và đã áp 22/11/2026)
- Đề tài evergreen không YMYL chỉ cần 3R **1 vòng** + R3 đóng gói. Giữ 2 vòng khi đề tài có thú cưng, ăn được hoặc hoá chất.
- Mục tiêu **≥4 video / 14 ngày** (hiện là 3).

### C4. Vệ sinh luật (✅ user duyệt và đã áp 22/11/2026)
- Luật mới vào **TESTING**, trừ khi có số của chính kênh.
- Luật nào 60 ngày chưa đo được thì phiên kiểm định đề xuất hạ cấp.
- Trần ≤20 luật ACTIVE: gộp các luật trùng (L4 ⊂ L15, L3 ⊂ L24, L14 ⊂ L19).

### C5. Độ dài 10–12′ (✅ user duyệt và đã áp 22/11/2026)
- Đổi `video_length` từ 10–14′ (1.650–2.300 từ) sang **10–12′ (1.650–2.000 từ)**.
- Căn cứ: views_5d ×1,54 cho video ≤12′, và 3 video 10–12′ sau 10/11 đều hơn các video 17–20′.

### C6. Tăng Lane B remake lên ~1/3 số video (✅ user duyệt và đã áp 22/11/2026)
- Cùng tháng 9, remake ×1,4 so với Lane A. Mẫu nhỏ (n = 3), nên áp làm TEST trong 6 video rồi phiên kiểm định chấm lại.

### C7. Hiệu chỉnh dự báo (tự động, chờ đủ mẫu)
- Sổ có 0/3 dự báo thắng. Khi đủ 8 video, phiên kiểm định đề xuất co P(thắng) và đổi ngưỡng Topic Gate.

## D. Việc user phải tự làm
- **Mỗi tuần thả 1 file export Studio** (Analytics → Nội dung → Xuất, 28 ngày) vào `research/`. Đây là nguồn CTR duy nhất.
- Cho biết video Dragon Fruit được làm bằng cách nào, để đưa cách đó vào pipeline nếu nó lặp lại được.
- ~~Duyệt C3–C6~~ — đã duyệt và áp 22/11/2026.
