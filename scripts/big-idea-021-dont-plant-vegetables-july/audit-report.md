# Audit Report — Don't Plant These 7 Vegetables in July (Here's Why)

MODE: A (Standard) | DATA: DATA MODE (channel-truth.md + channel-stats-garden-us-60k.md, fetched 2026-06-09/06-25) | LANGUAGE: EN | VIDEO TYPE: Standard
DNA VOICE: **Moderate** (2 signature elements bắt buộc bị thiếu — xem mục 4)
NARRATOR INTEGRITY: **Pass** (0 flags)
HOOK: **Needs work** (1 fail hard — xem Leak #1)
COMPLIANCE (flag): Clean (đã chấm chính thức 10/10 bởi mkt-yt-compliance)
=> **VERDICT: REVISE** (1 fix quan trọng ở hook + 2 bổ sung nhẹ, không cần viết lại toàn bộ)

---

## TOP 3 RETENTION LEAKS

**1. 🔴 Hook không đưa số liệu/bằng chứng trước giây 20-33 (vi phạm L6 — ACTIVE RULE)**
> **[trích]** "There's one number university researchers found that decides whether those seeds ever sprout, and it's not what you'd guess."

Đây chỉ TEASE có 1 con số, KHÔNG nói con số đó là gì. Con số thật (75°F / 82°F→43%) không xuất hiện cho tới tận item Lettuce, khoảng **word ~200, ~minute 1.3** — trễ hơn nhiều so với giây 20-33 mà `lessons-learned.md` L6 yêu cầu ("LUÔN đặt bằng chứng/con số chứng minh claim counter-intuitive TRƯỚC giây 20"). Đây chính xác là pattern đã giết 2 video tệ nhất kênh ("Pulling Weeds" -29.5%@20-30s, "Pesticides" -20.8%@22-33s) — claim sốc mà không chứng minh kịp.

> **Bản vá (giữ DNA Voice):**
> "Still got that packet of lettuce or spinach seeds on the counter, ready to go in the ground this week? Here's something most people don't know: once soil hits seventy-five degrees, those seeds shut down and simply refuse to sprout. Lettuce isn't the only one. Seven common vegetables fail in July soil, and every single one fails for its own exact, provable reason."

Con số "seventy-five degrees" giờ rơi vào khoảng word ~30 (~giây 12) — pass L6, vẫn giữ nguyên open-loop "7 vegetables" cho phần preview sau.

**2. 🟡 Tension reinforcement lệch khỏi vùng dip thật của kênh (phút 4-6)**
> **[trích]** "Now, before we move on, keep in mind we've still got the two biggest surprises coming up."

Câu này rơi vào khoảng **word ~990-1020 (~minute 6.6-6.8)** — ngay SAU khi vùng `MIDROLL_DIP_ZONE` (phút 4-6, word 600-900) đã kết thúc. Loop "radish/tomato surprise" mở từ preview vẫn còn sống xuyên vùng dip (nên L5 không fail hẳn), nhưng phần TÁI KHẲNG ĐỊNH rõ ràng lại đến hơi trễ để bắc cầu đúng lúc viewer dễ rời nhất.

> **Bản vá:** chèn 1 câu ngắn NGAY sau "...cauliflower is the most sensitive of the bunch" (rơi đúng ~word 850, ~phút 5.6 — giữa vùng dip thật):
> "...and trust me, there's an even trickier vegetable still coming up on this list."

**3. 🟡 Thiếu Anonymous Social Proof (signature bắt buộc theo brand-voice-dna.md)**
Script chỉ trích nguồn định chế (Clemson, Missouri, Maryland, Utah State) — không có câu nào kiểu "a viewer in [state]" / "master gardeners often report", vốn là 1 trong các **Signature Elements (phải có)** theo `brand-voice-dna.md` (mục AI Quick Start). Đây là lớp ấm áp/relatable khác với "science-backed", và kênh dùng nó để cân bằng giọng "bà nội" với giọng "khoa học".

> **Bản vá:** chèn vào FAQ section:
> "A viewer in Texas asked me almost this exact question last July — turns out her spinach was doing exactly what the research predicts."

---

## HOOK CHECK

- [x] Đòn đau / viễn cảnh tương phản — cảnh cầm gói hạt giống, quen thuộc với audience
- [x] Open Loop / Countdown anchor — "number six... number seven too"
- [~] 5 từ đầu mạnh — mở bằng câu hỏi trực tiếp (soft opener), không phải command-style, nhưng phù hợp với type Story/Revelation đã chọn ở Bước Hook — chấp nhận được
- [ ] **Mini-payoff trước ~20s — FAIL** (xem Leak #1)
- [x] **[DATA MODE]** Câu rơi vào `HOOK_DROPOFF_ZONE` (giây 40-55) — PASS, open loop "#6/#7" đang sống đúng vùng này

**→ 2 bản hook rewrite (đã có ở Leak #1, thêm bản 2 dưới đây):**

**Rewrite A (đã dùng ở Leak #1 — Revelation, số liệu ngay đầu)**

**Rewrite B (Story mở rộng, số liệu lồng vào hình ảnh cụ thể hơn):**
> "Picture this: a whole row of lettuce or spinach seeds, sitting in warm soil, doing absolutely nothing for weeks. It's not bad seed. Once soil crosses seventy-five degrees, the seed builds a chemical stop sign and simply refuses to wake up. That's just one of seven vegetables that fail in July soil — and each one fails for its own provable reason."

---

## DNA VOICE AUDIT

| Signature Element (brand-voice-dna.md) | Có/Thiếu |
|---|---|
| Grandmother story / personal failure story | ✅ ("your grandmother probably knew...") |
| "Here's why this works" + analogy | ✅ 3 biến thể (lettuce/brassica/radish) — hơi trên target 2-3, chấp nhận được |
| Exact measurements/numbers | ✅ dày đặc, đúng DNA |
| 3 mistakes / 3 problems | N/A — format Problem-Fix 7 items do outline quyết định, không phải lỗi |
| Cost comparison (DIY vs store) | ❌ **THIẾU** — không có so sánh $ nào trong script |
| Anonymous social proof | ❌ **THIẾU** — xem Leak #3 |
| Neighbor payoff scenario | 🟡 Có dùng phrase "Your neighbors will ask…" nhưng đảo hướng (neighbor THẤT BẠI, không phải viewer được khen) — hợp lý về nội dung (topic không có "kết quả đẹp để khoe"), nhưng không đúng tinh thần "payoff" gốc |
| "Happy gardening." sign-off | ✅ |
| Accessibility Anchors (2-3 lần) | ✅ ~5 lần (ten/twenty/under a minute/fifteen/five minutes) — hơi nhiều, có thể cắt 1-2 câu cho gọn |
| Human Texture E7 — contractions ≥60% | ✅ cao |
| Human Texture E7 — ≥2 gardener idioms (đúng list: rain or shine/green thumb/dirt-cheap/proof is in the pudding...) | ❌ **KHÔNG dùng đúng list** — script dùng "better safe than sorry" / "no harm done" (idiom chung, không phải gardener-specific) |
| Human Texture E7 — ≥1 folksy marker | ✅ "folks" (2 lần) |
| Sentence Structure — mantra rule-of-three đóng bài | ✅ "Grow smart, save your seeds, and skip the wasted summer." |
| Sentence Structure — lặp 1 con số làm xương sống (4-6 lần) | 🟡 Biến thể sáng tạo: dùng "thang số" leo dần (75°F/80°F/90°F) thay vì lặp ĐÚNG 1 con số — hợp lý về nội dung (7 ngưỡng khác nhau) nhưng lệch khỏi signature gốc |
| Sentence Structure — chẩn đoán chắc nịch | ✅ "This isn't disease. It isn't bad seed." / "This isn't a seed problem at all." |
| Sentence Structure — fragment ngắn | ✅ "That's it." ×3 (hơi lặp — xem dưới) |

**Frequency check lệch chuẩn:**
- "That's it" dùng **3 lần** (lettuce, radish, tomato) vs target 1 lần trong brand-voice-dna.md — hơi lặp, làm giảm sức nặng của signature. Gợi ý: đổi 1-2 chỗ sang biến thể khác ("And that's the whole trick." / "Simple as that.").
- "Don't panic" dùng 2 lần (lettuce, tomato) vs target 1 lần — chấp nhận được (đã giảm từ 3 xuống 2 ở vòng self-audit), có thể giữ nguyên.

---

## NARRATOR INTEGRITY SCAN

Không phát hiện vi phạm. Không có "I grew/I tested/in my garden". "Quick question I hear a lot" là khung host/MC hợp lệ (không phải claim hands-on làm vườn). "Your grandmother" dùng đúng như folklore, không phải bằng chứng cá nhân của narrator.

---

## COMPLIANCE FLAG

Không phát hiện dấu hiệu mới ngoài báo cáo `mkt-yt-compliance` đã chấm 10/10. Không cần chạy lại.

---

## LESSONS-LEARNED CHECK (ACTIVE RULES)

| Rule | Kết quả |
|---|---|
| L1 — không cây exotic | ✅ Pass |
| L2 — counter-intuitive có outcome cụ thể | ✅ Pass |
| L3 — deliver title promise trong 60s | 🟡 Tên đủ 7 loại rau xuất hiện ~giây 40-60 (preview), nhưng "why" đầu tiên (item Lettuce) chỉ tới ~giây 80 — liên quan trực tiếp tới Leak #1, fix hook sẽ cải thiện luôn mục này |
| L4 — open loop giây 40-55 | ✅ Pass |
| L5 — tension layer phút 4-6 | 🟡 Loop sống xuyên vùng nhưng reinforcement lệch trễ ~40s — xem Leak #2 |
| L6 — bằng chứng trước giây 20-33 | 🔴 **FAIL** — xem Leak #1 |

CR-series (competitor teardown, 2026-06-25): CR2 (name all items trong preview) ✅, CR7 (hero anchor) ✅ dạng biến thể, CR10 (FAQ objection-handling) ✅. Không phát hiện vi phạm nhóm AVOID X1-X5.

---

## ACTIONABLE FIXES (xếp theo tác động)

1. **[Cao]** Sửa hook theo Rewrite A hoặc B — đưa số "75°F" vào trước giây 20 (fix L6 + cải thiện L3 luôn thể).
2. **[Trung bình]** Chèn 1 câu tension nudge giữa đoạn brassica (~word 850) để bắc cầu đúng phút 4-6 (fix L5 timing).
3. **[Trung bình]** Thêm 1 câu anonymous social proof ở FAQ (fix signature thiếu).
4. **[Thấp]** Thêm 1 câu cost-angle ngắn (vd "a wasted seed packet is only a couple dollars, but a wasted month of garden space costs a lot more") — không bắt buộc nhưng khớp signature "cost comparison".
5. **[Thấp]** Đổi 1-2 trong 3 lần "That's it" sang biến thể khác để tránh lặp.

---

## INLINE TAGS REPORT

Không có `[NEED DATA]` / `[YMYL]` / `[PET-SAFETY]` mới cần gắn. `[HEDGE]`: không cần — script đã hedge nhất quán (usually/often/typically).

---

⚠️ Nhắc: bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off trước khi export VoiceAI.
