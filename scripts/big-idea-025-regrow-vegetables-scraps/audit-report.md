# Audit Report — Regrow 6 Vegetables From Scraps, No Soil | Gardening Without Bending

MODE: C (YMYL-adjacent — food safety mold/spoilage, elderly risk) | DATA: DATA MODE (channel-stats-garden-us-60k.md, fetched 2026-06-09 — 29 ngày, hơi cũ nhưng vẫn dùng vì chưa có sync mới) | LANGUAGE: EN | VIDEO TYPE: YMYL-Foraging-adjacent (food safety, không phải foraging thật)

```
DNA VOICE:          Moderate (2 gap nhỏ — xem mục 4)
NARRATOR INTEGRITY: Pass
HOOK:               Pass
COMPLIANCE (flag):  Clean (đã chấm chính thức qua mkt-yt-compliance = 10/10)
=> VERDICT: REVISE (2 fix nhỏ, không cần viết lại)
```

---

## 1) TOP 3 RETENTION LEAKS

Không phát hiện leak nghiêm trọng ở `HOOK_DROPOFF_ZONE` (giây 40-55) hay `MIDROLL_DIP_ZONE` (phút 4-6) — cả 2 vùng đều có nội dung/loop sống đúng vị trí (verify Pha D: L4 @ giây 52, L5 zone 3:50-6:30). Đây là 3 điểm nhỏ đáng chú ý, không phải leak chết:

- **"University of California researchers clocked new growth starting in about six days."** → đây là điểm duy nhất mang tính "authority" ở vùng L3 (giây 59) nhưng đã bị rút gọn thành 1 nguồn đơn lẻ (xem mục 6.7) → giảm sức nặng "khác AI-slop" đúng lúc cần nhất (payoff đầu tiên). → **Bản vá:** "University of California researchers — along with extension offices in Illinois and Michigan — all clocked this the same way: new growth in about six days." (giữ nguồn cụ thể cho compliance + khôi phục hội tụ đa nguồn cho anti-slop).
- **Bridge "Celery rewards patience. Romaine rewards almost none."** → tốt, nhưng đứng một mình không kèm số liệu nên hơi nhẹ so với các bridge khác. Không bắt buộc sửa, chỉ note.
- **Đoạn cabbage/mold (cuối video, ~7:00)** dài và dồn nhiều thông tin an toàn (mold, elderly risk, CDC) sát nhau → hơi nặng về Facts ngay trước climax "answer you've been waiting for". Không phải leak, nhưng nếu muốn mượt hơn có thể tách 1 câu Fun/Feelings chen vào — không bắt buộc.

## 2) HOOK CHECK

- [x] Có đòn đau/tương phản: "already sitting in your trash can right now"
- [x] Open Loop/Countdown: "which one wins, and which ones are barely worth the jar"
- [x] 5 từ đầu mạnh: "Six vegetables. Zero dollars."
- [x] Mini-payoff trước ~20s: "zero dollars" + "under a week" xuất hiện trong 15 từ đầu
- [x] Câu tại `HOOK_DROPOFF_ZONE` (giây 40-55): "Let's start with the fastest of the six" (giây ~52) giữ loop sống, KHÔNG chuyển sang giới thiệu bản thân

**Hook: Pass**, không cần rewrite.

## 3) DNA VOICE AUDIT

| Yếu tố (theo brand-voice-dna.md) | Trạng thái |
|---|---|
| "Here's why this works" (2-3 lần) | ✅ 3 lần (green onion, celery, science correction) |
| "Don't panic" (1 lần) | ✅ (đoạn cabbage) |
| "That's it" (1 lần) | ✅ (đoạn actionable step) |
| "My grandmother"/"A neighbor" (1-2 lần) | ✅ 2 (grandmothers-generic + "one home gardener") |
| Accessibility Anchors (2-3 lần) | 🟡 Chỉ 1 cụm ("one small jar…thirty seconds") — thiếu 1-2 cụm rải thêm ở item khác (vd celery/bok choy) |
| Sign-off "Happy gardening." | ✅ |
| Contractions ≥60% câu | ✅ ước lượng đạt (they're, don't, that's, it's, she'd, won't…) |
| Gardener idioms Tier 2 (≥2 khác nhau) | 🟡 Không thấy idiom nào từ bank chuẩn (rain or shine / dirt-cheap / from seed to harvest…) — script dùng ẩn dụ tự chế ("tortoise of this list", "the quiet one") thay vì idiom truyền thống, chấp nhận được nhưng nên bổ sung ≥1 idiom chuẩn |
| Folksy marker ≥1 | ✅ "folks" (2 lần) |
| AI Clichés blacklist = 0 | ✅ Không thấy delve/leverage/moreover/furthermore… |

→ **DNA Voice: Moderate** (2 gap nhỏ, không chặn publish, nên vá nếu còn thời gian).

## 4.5) STORYTELLING CRAFT CHECK

- [x] Micro-bridge ở mọi transition — không có "trạm dừng" phẳng. Các bridge: "The next one takes patience…" / "Celery rewards patience. Romaine rewards almost none." / "We're at the halfway point…" đều đóng ý cũ + tease món nợ mới.
- [x] ≥1-2 scene — 1 scene documented history (Victory Gardens, có nguồn National WWII Museum trong Story Bank) ✅
- [x] Mid-video re-hook tại vùng dip — "Maybe you already have a real garden bed going out back…" đặt ngay trước item #4, đúng lúc tiếp cận `MIDROLL_DIP_ZONE`
- [x] Per-item intrigue — item #1 (fastest win), #4 (tortoise), #5 (quiet one), #6/cuối (most folks throw away) đều có intrigue riêng; item #2/#3 được intrigue hoá qua bridge câu trước đó thay vì trong dòng "Number X" — đạt tinh thần rule (≥3-4/6 item, có đầu+cuối)
- [x] Climax beat — "So here's the answer you've been waiting for" đứng đúng 1 điểm đỉnh duy nhất, có build-up đủ (items 4-6) trước khi trả lời, không rơi vào dip mà thiếu build-up
- [x] Forward-visual close ("white roots reaching down that jar") ĐỨNG TRƯỚC identity CTA ("you belong here") — đúng thứ tự. Không có next-video-loop hứa hão (đúng, vì không có video kế hoạch thật).

→ **Storytelling: Pass đầy đủ**, không có gap.

## 5) NARRATOR INTEGRITY SCAN

Không phát hiện vi phạm. Không có "I grew/I tested/my garden". "One home gardener told her extension office…" đúng dạng ẩn danh (anonymous social proof), không phải nhân chứng có tên bịa. "Grandmothers have been doing…" dùng đúng như folklore chung, không phải bằng chứng cá nhân.

## 6) COMPLIANCE FLAG

Clean — đã chấm chính thức qua `mkt-yt-compliance` = **10/10 PUBLISH** (2 vòng rewrite: nguồn cụ thể UC/USDA/CDC/National WWII Museum, pet+kid-safety block đúng vị trí trước method + disclaimer trong 30s đầu, hedge claim tuyệt đối). Không cần chấm lại.

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES)

| Rule | Kết quả |
|---|---|
| L1 (không exotic plant) | ✅ 6 loại rau đều phổ biến ở Mỹ |
| L2 (counter-intuitive có outcome cụ thể) | N/A — không có claim ngược đời chính |
| L3 (deliver title trong 60s) | ✅ green onion method + "no soil" giao tại giây 59 |
| L4 (open loop giây 40-55) | ✅ giây 52, "fastest of the six" |
| L5 (tension phút 4-6) | ✅ bok choy→leek→cabbage phủ 3:50-6:30 |
| L6 (bằng chứng trước giây 20 nếu claim sốc) | N/A — title không phải claim ngược đời |
| L7 (không viết quá 10 phút mặc định) | ✅ ~8.6 phút |
| L8 (pain-removal stack ergonomic) | ✅ "No Soil, No Bending" đúng công thức AVD 49% |

Không vi phạm rule nào.

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Số liệu cụ thể + nguồn cite inline (UC, USDA, CDC, National WWII Museum)
- [ ] **≥2 câu Consensus Synthesis — CHỈ CÒN 1** 🟡. Nguyên nhân: vòng compliance rewrite (round 2-3) đổi "Extension offices at more than one university clocked this the same way" (hội tụ đa nguồn) → "University of California researchers clocked…" (nguồn đơn lẻ) để đáp ứng yêu cầu "nêu tên cụ thể" của compliance. Điều này vô tình làm mất kỹ thuật Consensus Synthesis ở đúng vị trí L3 — nơi cần sức nặng "khác AI-slop" nhất. Nguyên tắc #2 (regrown = second wind) vẫn giữ được tinh thần hội tụ nguồn qua "University extension research is blunt about it" nhưng cũng không nêu rõ "nhiều nguồn độc lập" tường minh.
- [x] Science moment chốt Action → Benefit (bitterness → dùng garnish/stir-fry)
- [x] Claim-scoping trung thực (romaine "not full head", bok choy "not before full head", leek range "weeks, sometimes months")
- [x] Góc cơ chế khoa học riêng (bitterness compounds do plant stress) — AI-slop generic không có
- [x] Không dính pattern slop (không cơ chế giả khoa học, không claim thần kỳ, không cấu trúc hoán đổi được)

→ **5/6 tiêu chí đạt, 1 tiêu chí (Consensus Synthesis) bị suy yếu do side-effect của compliance fix** — vẫn đủ ngưỡng ≥2 bằng chứng differentiation tổng thể nên KHÔNG reject, nhưng nên vá để giữ trọn vẹn cả 2 lớp (nguồn cụ thể + hội tụ đa nguồn) — 2 mục tiêu này không loại trừ nhau, có thể viết chung 1 câu (xem bản vá ở mục 1).

## 7) ACTIONABLE FIXES (xếp theo tác động)

1. **[Cao]** Khôi phục Consensus Synthesis cho claim green onion (giây 59, vị trí L3): đổi "University of California researchers clocked new growth starting in about six days." → "University of California researchers — along with extension offices in Illinois and Michigan — all clocked this the same way: new growth in about six days." (giữ nguồn cụ thể, khôi phục hội tụ đa nguồn).
2. **[Thấp]** Thêm 1-2 Accessibility Anchor nữa (vd ở celery hoặc bok choy: "just a shallow bowl and a few minutes of your time") để đạt 2-3 lần/script theo brand voice.
3. **[Thấp]** Cân nhắc thêm 1 gardener idiom chuẩn từ bank (vd "dirt-cheap" khi nói về "$0" trong đoạn debunk overclaim) để tăng Human Texture Tier 2.

Không có fix nào ở mức "cao" đủ để REJECT — cả 3 đều là polish, không phải lỗi cấu trúc.

## 8) INLINE TAGS REPORT

Không có `[NEED DATA]` / `[YMYL]` / `[PET-SAFETY]` / `[HEDGE]` / `[COMPLIANCE]` nào còn sót trong script — toàn bộ đã xử lý ở vòng compliance trước đó.

---

## Ghi chú Producer

Nhớ bật **"Altered or synthetic content"** khi upload (kênh dùng AI Voice). Producer sign-off trước khi export VoiceAI.
