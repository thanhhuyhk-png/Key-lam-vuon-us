# Prediction — remake-002-rose-bloom-spoon-trick

> Điền tại GATE Script (Bước 3), ngay khi approve script.

| Trường | Giá trị |
|--------|---------|
| Video | remake-002-rose-bloom-spoon-trick |
| Ngày scripted | 2026-09-09 |
| Target publish | (chưa chốt) |
| Compliance score (lúc GATE) | 10/10 (vòng 2, sau khi fix Pet/Kid Safety + nguồn số liệu) |

## Title bet
- **Title chốt:** `Just 1 Spoon Makes Your Roses Bloom 10x Faster (Florist's Secret)`
- Specific quantity? **Y** ("1 Spoon", "10x Faster")
- Leading number? **N** (title không mở bằng chữ số — "Just" đứng đầu)
- Độ dài: **11 từ / ~67 ký tự** (target ~12 từ / 65 ký tự — sát chuẩn)

## Retention bets (3 luật cứng)
- **Topic familiarity:** roses — rất phổ biến với người Mỹ 60–80. **Y**
- **Giây 40–55:** open loop "the mistake I mentioned — probably not the one you're picturing, happens before the rose touches the ground" (root-bound tease, đo được ở giây ~41)
- **Phút 4–6:** Beat 4 climax — "florist's trick" reveal (vỏ trứng nghiền + bã cà phê), đo được ở giây ~273 (4:33). Jenga Retention: **ON** — cộng thêm 1 loop MỚI (science-correction) dời tới giây ~395 (6:35), vắt qua cả mid-roll dip lẫn đoạn ánh sáng/phân bón để giữ chân tới gần cuối video.

## Engagement bets
- Themes nhắm tới: ☑ Nostalgia/đa thế hệ (Peace Rose scene 1935/1945 + "My grandmother") ☑ Pet safety (+ trẻ em, đã fix ở compliance vòng 2) ☐ USDA zone/climate *(gap đã biết — không có data zone cho roses trong research-brief, không bịa)*
- Câu/đoạn cụ thể kích theme: "My grandmother always buried eggshells by her rosebushes, whole or barely crushed."

## ⚠️ Quy tắc chấm — LANE REMAKE (không dùng AVD làm verdict chính)

Theo CLAUDE.md: Lane B chấm bằng `views_5d` vs `median_5d_views` (285) + tổng giờ xem, **KHÔNG** chấm bằng AVD dù format video này là single-topic (đã dùng Retention Spine để tối ưu AVD như một kỹ thuật sản xuất, nhưng verdict cuối cùng ở retro vẫn theo chuẩn Lane B).

| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views 5 ngày đầu | median 285 (toàn kênh) | **≥285** (mục tiêu tối thiểu để PASS theo chuẩn Lane B) |
| AVD % *(diagnostic phụ, không phải verdict)* | 25.6% baseline / 28.3% W35 gần nhất | **30–33%** — kỳ vọng cao hơn baseline nhờ 2 loop giữ chân bắc qua drop zone + mid-roll dip |
| CTR % *(không phải nút thắt hiện tại của kênh)* | 5.5% | **5.5–6%** |

## 🟡 TEST KHUÔN — Archetype A3 (Single-Technique Hack)

Theo `references/remake-archetypes-en.md` §5: archetype A3 đang ở mức bằng chứng 🟡 (suy ra, chưa có số liệu — video này CHÍNH LÀ ca thử nghiệm đầu tiên). Câu hỏi retro bắt buộc phải trả lời sau 7–14 ngày:

> **Khuôn A3 (tài sản = cặp tỷ lệ định lượng · trục đổi = cây nền · lời hứa thứ hai dời sang sau payoff chính) có mang lời hứa qua được không?**

Cụ thể cần đối chiếu ở `retro.md`:
1. Retention/watch-time có thật sự giữ được qua đoạn 6:00–7:00 (nơi đặt loop "lời hứa thứ hai" — science correction vỏ trứng) hay viewer vẫn rời ngay sau climax phút 4:33 như thể loop thứ hai không có tác dụng?
2. views_5d có vượt median 285 không — nếu KHÔNG, cần phân biệt: lỗi ở archetype A3 (khuôn) hay lỗi ở seed cụ thể này (seed <60 ngày, override ở GATE 0 — xem seed-brief.md §1)?
