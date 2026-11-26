# Prediction — big-idea-030-more-nutritious-than-groceries

> Điền tại GATE Script (Bước 3) ngay khi approve script. Ghi lại "cược" của video
> để 7–14 ngày sau diff với số thật trong `retro.md`. Không có prediction → không diff được.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-030-more-nutritious-than-groceries |
| Ngày scripted | 2026-07-15 |
| Target publish | TBD — chưa lên lịch |
| Compliance score (lúc GATE) | ~10/10 (round 3 subagent: 9/10 + 1 fix thủ công "storage" line, không chạy lại subagent vì fix rõ ràng an toàn) |

## Title bet
- **Title chốt:** `You're Pulling $6 Salad: 7 Yard Weeds That Beat Store Greens`
- Specific quantity? **Y** ($6, "seven") — 100% top videos có; bắt buộc
- Leading number? **N** — tradeoff có chủ đích tại GATE 1 (Title Engine v2 kill funnel chọn driver Fear/Regret "You're Pulling" thay vì leading number; xem outline.md)
- Độ dài: **11 từ / 62 ký tự** (target ~12 từ / 65 ký tự — trong ngưỡng)

## Retention bets (3 luật cứng)
- **Topic familiarity:** cây/chủ đề ≥ phổ biến với người Mỹ? **Y** — cả 7 cây (dandelion, lamb's quarters, chickweed, violet, purslane, wood sorrel, plantain) đều là cỏ dại phổ biến toàn nước Mỹ, không exotic
- **Giây 40–55:** open loop gì giữ người xem qua vùng chết? → Loop #1 (mở ở hook: "cây #5 thắng cả cá") sống qua tái-tease "There's a reason your yard keeps outperforming the produce aisle, and we'll show you why by the end" — cue thật tại giây 46.8s (đã sửa sau audit độc lập; bản đầu tiên cue này lẫn với đuôi safety-disclaimer, bị flag Leak 2, đã fix)
- **Phút 4–6:** tension layer gì (open loop / payoff / pattern break)? → Climax Purslane (omega-3 vs cá) đóng Loop #1 tại giây 271.6 (4:32) — payoff mạnh nhất video, đúng giữa mid-roll dip zone của kênh · Jenga Retention: **ON** (2 loop chồng: Loop#1 hook→purslane, Loop#2 science-moment preview→conclusion)

## Engagement bets
- Themes nhắm tới: ☑ Nostalgia/đa thế hệ  ☑ Pet safety  ☑ USDA zone/climate
- Câu/đoạn cụ thể kích theme:
  - Nostalgia: "Old-timers in the gardening community have long said the best greens are the ones nobody planted" + scene lịch sử "The Englishman's Foot" (plantain theo chân thực dân Mayflower)
  - Pet safety: "if you've got grandkids or pets running around the yard" (item violet) + block an toàn mở rộng trước đoạn ráp salad cuối
  - USDA zone: "no matter what USDA zone you're in" (preview)

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| AVD % | 25.6% | **32%** — cược retention engineering (L6 proof giây 11.6, climax đúng dip zone, 2-loop Jenga đã audit-fix) đủ kéo qua target 32%, nhưng KHÔNG đạt mức "L8 formula" 49% vì đây là angle nutrition-value chứ không phải ergonomic pain-stack đã chứng minh thắng nhất kênh |
| CTR % | 5.5% | **5.5%** — cược giữ nguyên baseline, không kỳ vọng tăng vì title cố ý hy sinh leading-number (driver Fear/Regret thay thế) và kênh đang ưu tiên tuyệt đối AVD, không phải CTR (đã khỏe, xem channel-truth 2026-07-04) |
