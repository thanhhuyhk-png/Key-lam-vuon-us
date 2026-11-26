# Prediction — big-idea-100-aloe-sequel

> Ghi tại GATE Script (22/11/2026). 7–14 ngày sau khi đăng, so với số thật trong `retro.md` (`tools/kiem_dinh_ky.py` tự ghi `retro-auto.md`).
> **Chấm chính:** views_5d so với trung vị 10 video gần nhất (596 ở lần đo 22/11) + giây xem/lượt + CTR Studio. ⛔ Không chấm bằng AVD% đơn lẻ.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-100-aloe-sequel |
| **Hạng** | **AN TOÀN** · Topic Gate 2/3 (① ✅ · ② ❌ · ③ ✅ mỏng) → GO có điều kiện · **TEST** (xem dưới) |
| **Loại** | **PHẦN TIẾP THEO catalog (C2)** — gốc: `AJnyTWUgKWU` «5 Secrets to Growing Aloe Vera FAST and EASY» (23.301 view / 28 ngày, CTR 6,64 %). Video đầu tiên của thử nghiệm C2 (8 video). |
| Ngày scripted | 2026-11-22 (user duyệt script sau 3R 2 vòng) |
| Target publish | **chưa chốt** — evergreen, không có hạn trend; còn thumbnail (render ảnh thật), giọng, dựng |
| Compliance score (lúc GATE) | **10/10 PUBLISH** (R2 Opus, vòng 2; vòng 1: 8/10) · Hook /35: Agy 34 · Opus 31 |
| Độ dài | **1.356 từ ≈ 8,2′** @165 wpm — dưới khung 10–12′ (user chấp nhận 22/11, không độn) |

## Title bet
- **Title chốt:** `Free Aloe Vera Plants: Separate Pups the Easy Way (5 Steps)` (user chọn Title A 22/11; vidIQ không chấm — tool không có)
- Specific quantity? **Y** («5 Steps», «Free») — kết quả người xem nhận được, không số trừu tượng (L21 ✅)
- Leading number? **N** — «Free» dẫn đầu, số ở cuối ngoặc
- Keyword-first: **một phần** — «aloe vera» ở ký tự 6; keyword đo được «aloe vera plant care» 4.031/th US (growth null); «aloe vera winter care» <750. Video browse-intent (như video gốc, Browse ~70 %).
- Độ dài: **10 từ / 59 ký tự**
- Thumbnail concept: `1 POT → 4 POTS` (+ dòng trắng `CHECK THE BASE` đề xuất bởi R3, chờ render); ảnh THẬT, không AI.

## Retention bets (3 luật cứng + L22–L27)
- **Topic familiarity:** **Y** — aloe vera là cây phổ thông nhất kênh; video gốc là video số 1.
- **Giây 40–55 (L4/L15):** Loop A «cái cắt phải khô bao lâu?» gieo 0:32 → còn sống qua 0:38–1:00 (câu 38–60 s là Bước 1 + mẹo kiểm rễ, không lộ trình) → trả một phần 3:18 → đóng 4:13 (hẹn «about four minutes», trả ~3,7′).
- **Phút 4–6 (L5):** Editorial Signature = bảng «ai nói gì» về thời gian khô (Arizona «a week or so» ↔ Illinois «re-pot right away»; lá/cành là câu hỏi khác) + Loop C «động tác nghe ngược» gieo 5:02 → đóng 6:08 · Jenga Retention: **ON**.
- **Luật mới lần đầu áp trên cả bài (22/11):** FIRST_STEP **0:18** (L24) · COMMENT_Q **2:33** (L22, TEST) · kết **13 s** (L23) · loop dài nhất **166 s** (L27) · giọng E7 **47 %** câu rút gọn.

## Engagement bets
- Themes nhắm tới: ☐ Nostalgia (không dùng — Story Bank trống, không bịa nhân vật, L11) · ☑ **Pet safety** (ASPCA: aloe độc với chó mèo, chỗ pup phơi khô, «call your vet») · ☑ **USDA zone/climate** (mùa đông, trong nhà vùng lạnh)
- Câu kích theme (L22): «How many pups did you find on yours? Tell me in the comments.» (2:33)

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views_5d | trung vị 596 · an toàn ≥894 (1,5×) · bứt ≥2.980 (5×) | **P25 ~350 · P50 ~650 · P75 ~1.300** (ước tay, chưa qua `chi_so.py`). **P(≥894) ≈ 0,30 · P(≥2.980) ≈ 0,03** |
| AVD % | 29,3 % (tuần mới nhất) · video ≤9′ từ 9/2026: 29,5 % | **~29 %** (8,2′ nhưng nhiều đoạn «ai nói gì») — phán đoán |
| CTR % (giờ 48) | video mới ≤45 ngày: trung vị 2,40 % · video cũ 4,35 % · «Root These 9» (khung Free) 3,02 % | **~3,2 %** (khoảng 2,5–4,5) — khung «Free …» + thumbnail có số nhận được; chưa có thumbnail render |
| Giây xem/lượt | watch-budget kênh ~238 s | **~140–150 s** (AVD 29 % × 8,2′) — thấp hơn video 10–12′ vì ngắn; câu hỏi retro: views_5d có bù không |

> Căn cứ: (1) ① franchise ✅ nhưng **9 video aloe sau video gốc có views_5d trung vị 291** (132–692) — franchise không tự chuyển; (2) giả thuyết: 9 video con đi theo khung cứu cây/sợ/sinh học, video này **giữ khung gói của video gốc** (Free + dễ + số bước) nên dự báo trên mức 291; (3) video ≤9′ từ 9/2026 có views_5d trung vị 538, 10–12′ là 673 (n=12 / 7); (4) ③ keyword mỏng, ② trend không có aloe → trần thấp, không dự báo bứt.

## TEST (ghi rõ để retro trả lời)
1. **TEST C2 — PHẦN TIẾP THEO catalog (đầu tiên, 1/8):** giữ khung gói của video gốc có làm franchise «chuyển» không? views_5d **≥894** → C2 hoạt động, làm tiếp phần 2 gốc khác (Avocado) · **<400** → ngay cả khi giữ khung vẫn không chuyển → hạ C2 khỏi cổng ①.
2. **TEST KHUNG GÓI vs 9 video aloe trước:** «Free … (5 Steps)» so với trung vị 291 của 9 video aloe con.
3. **TEST ĐỘ DÀI 8,2′ (dưới khung 10–12′):** giây xem/lượt và views_5d so với 094 (11:17 → 850) và nhóm ≤9′ (538). views_5d ≥ nhóm ≤9′ nhưng giây xem/lượt <150 → ngắn không thiệt.
4. **TEST BỘ LUẬT MỚI L22–L24 + L27 (video đầu tiên áp đủ):** giữ chân @0:30 (baseline ~64 %) · @1:00 (baseline ~43 %, mục tiêu ≥46 %) · bình luận/1K view (baseline ~1,5; L22 hy vọng ≥2,5) · rơi 20–35 s có nhỏ hơn −24 % của 092/093 không.
5. **TEST EDITORIAL SIGNATURE «ai nói gì»:** comment có nhắc «a week vs right away» không? đường cong 3:29–5:05 phẳng hơn 092/093 không? (không có thẻ này ở 092/093).
6. **TEST HÌNH THẬT (không AI):** bình luận có chê hình giả như video gốc (156 like) không? (chỉ đánh giá được sau khi dựng).

## Quy tắc dừng
- views_5d **<400** hoặc CTR giờ 48 **<2,5 %** → gói hỏng: đổi thumbnail trước (P2 `CROWDED ALOE?` / P3 `1 → 4`), rồi mới đổi title (giữ «aloe vera» ở đầu).
- views_5d **≥894** → đạt mức an toàn; phần tiếp gốc khác (Avocado) vào suất C2 kế tiếp.
- views_5d **≥2.980** → làm phần tiếp aloe thứ 2 ngay, giữ khung «Free … (N Steps)».
- 3 video C2 liên tiếp <400 → thôi C2 (retro đề xuất, chờ user duyệt).
