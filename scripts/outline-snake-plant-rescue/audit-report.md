# Audit Report — Save a Dying Snake Plant in 5 Steps (Even Soft, Yellow Leaves)

> Independent QA — second-opinion audit, no context from the writing/self-audit process. Ref: `mkt-youtube-script-audit` SKILL.md v7-lean.

---

## 1) HEADER

```
MODE: A (Standard) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard (Problem-Fix/Rescue)
DNA VOICE:          Moderate
NARRATOR INTEGRITY: Pass
HOOK:               Needs work (fails the DATA-MODE dropoff-zone sub-check)
COMPLIANCE (flag):  Clean (0 signs — mkt-yt-compliance already scored 9/10 PUBLISH separately)
=> VERDICT: REVISE
```

Word count (TTS body only): **1,315 words** ≈ 8:45 at 150 wpm — inside the 8-10 min / 1,200-1,500 word target (channel.config.json). ✅ No L7 (length) issue.

---

## 2) TOP 3 RETENTION LEAKS

**Leak #1 — 🔴 `HOOK_DROPOFF_ZONE` (giây 40-55) bị chiếm bởi Story Bank scene + câu preview, đúng loại nội dung L4 cấm**

- **[trích câu gốc, ~giây 30-56s]**: *"Here's a strange bit of history first, and it's kind of a fun one. Back in nineteen-oh-three, a botanist named David Prain classified this plant as Dracaena, not Sansevieria... This plant's been misunderstood for over a century! **Watering it wrong is an easy habit to fall into. Next, we'll break that habit together**, even if your roots already look rough."*
- **Lý do viewer rớt**: Tôi đo được câu "Watering it wrong is an easy habit to fall into. Next, we'll break that habit together" rơi đúng vào giây ~52-56 — chính giữa `HOOK_DROPOFF_ZONE` (40-55s) mà channel-stats gọi là "transition hook→credibility/preview". Đây chính xác là hành vi L4 cấm: chuyển sang preview/giới thiệu tại vùng chết thay vì giữ open loop. Retention Spine đã duyệt (GATE 2.5) đặt Diagnosis beat (2 nguồn Extension, tease "the one mistake most people make") vào đúng ô 40-55s — nhưng script thực tế đưa Story Bank scene + câu bridge preview-style vào đó, đẩy Diagnosis beat lùi ra sau (~giây 72+). Đây là lệch so với bảng Spine đã duyệt, không phải lỗi ngẫu nhiên.
- **Bản vá giữ DNA Voice**: Đảo thứ tự — đưa Diagnosis beat ("There are really only two things going on when a snake plant looks bad...") lên ngay sau hook (trước giây 40), rồi mới chèn Story Bank (David Prain) SAU khi qua khỏi giây 55, làm cầu nối sang Step 1. Ví dụ: *"...Your finger, two inches deep, tells you the truth every time. And here's a strange bit of history while we get moving — [Prain scene] — so this plant's been misunderstood for over a century. Turns out watering habits get misunderstood just as easily. Step one starts with your hands..."*

**Leak #2 — 🟡 `MIDROLL_DIP_ZONE` (phút 4-6): science-moment climax thiếu analogy — đúng lúc retention yếu nhất, thiếu chính signature bắt buộc**

- **[trích câu gốc, ~5:28]**: *"Here's why this actually works, and it's kind of satisfying once it clicks. Extension offices across the country word this differently, but they all land on the same point. It's not really the water that kills the plant. It's the oxygen. Waterlogged soil pushes air out of the root zone, and that's exactly the environment root-rot fungus needs to take over."*
- **Lý do viewer rớt**: `channel-truth.md` yêu cầu signature bắt buộc "Here's why this works" **+ analogy** — nhưng đoạn science moment (Consensus Principle 1, đúng climax của video, đặt đúng vị trí phút 4-6 theo Spine) chỉ giải thích cơ chế trừu tượng (oxy/đất úng) mà không có 1 hình ảnh cụ thể, dễ hình dung cho audience 60-80 tuổi (vd so sánh với "giữ hơi thở dưới nước", hay "cái ống hút bị bịt"). Đây là đúng điểm video dễ rớt nhất theo data (`MIDROLL_DIP_ZONE` -11% cho Problem-Fix) — thiếu analogy ở chính điểm này làm giảm sức bám tại vùng nguy hiểm nhất.
- **Bản vá giữ DNA Voice**: Thêm 1 câu analogy ngay sau "It's the oxygen": *"Think of it like holding your head underwater — roots need to breathe too, and waterlogged soil is like a plastic bag over their face."* (giữ tông folksy, không đổi nội dung khoa học).

**Leak #3 — 🟡 Step 1 (hành động cụ thể đầu tiên) trễ ~1 phút so với bảng Spine đã duyệt**

- **[trích câu gốc]**: *"Step one starts with your hands, not a tool, and it feels almost too simple."* — đo được ở **word 293 (~1:57)**, trong khi bảng Retention Spine (GATE 2.5, đã duyệt) đặt Step 1 tại mốc word-idx ~150 (~1:00).
- **Lý do viewer rớt**: Kết hợp với Leak #1, gần 2 phút đầu bị chiếm bởi hook + Story Bank + Diagnosis walkthrough trước khi lời hứa "5 Steps" của title thực sự bắt đầu giao hàng. Đây liên quan L3 (deliver title promise sớm) — phần "insight" (drowning-not-thirsty) đã giao <20s, nhưng cấu trúc "5 Steps" chính — thứ được bán trong title — chỉ bắt đầu ở gần phút 2. Rủi ro: viewer đã có đủ thông tin chẩn đoán, thấy video "chưa vào việc", rời trước khi thấy Step 1.
- **Bản vá giữ DNA Voice**: Cắt gọn đoạn Diagnosis (hiện ~72-117s) xuống 1-2 câu súc tích, dồn Step 1 lên gần mốc ~75-90s. Có thể gộp câu chẩn đoán "bone-dry vs drowning" ngắn hơn, bỏ câu "A Master Gardener with Minnesota's extension office put it even more plainly..." (trùng lặp ý với dòng ngay sau, có thể rút gọn 1 trong 2).

---

## 3) HOOK CHECK

- [x] Có đòn đau / viễn cảnh tương phản? — "soft and yellow at the base... it's not thirsty, it's drowning" ✅
- [x] Open Loop / Countdown anchor? — "5 steps to save it, even if some roots have already turned black" ✅
- [x] 5 từ đầu mạnh? — "If your snake plant's leaves..." — pain-statement kiểu "if your X looks Y", đúng bucket cho phép ✅
- [x] Mini-payoff trước ~20s? — "Still moist down there? Watering again could kill it within days" đo được ~14-19s ✅ (thoả cả L6 — bằng chứng số "two inches" rơi ~giây 13, trước vùng chết 20-33s)
- [ ] **[DATA MODE]** Câu rơi vào `HOOK_DROPOFF_ZONE` (40-55s): **FAIL** — xem Leak #1. Nội dung tại đó là Story Bank + câu preview-style, không phải open loop/micro-payoff.

**HOOK: Needs work** — 4/5 sub-checks pass, nhưng sub-check quan trọng nhất (đúng vùng chết thật của kênh) fail. Không cần rewrite toàn bộ hook (câu mở đầu rất tốt, bám sát Spine) — chỉ cần sửa cấu trúc đoạn *sau* hook (xem bản vá Leak #1).

---

## 4) DNA VOICE AUDIT

Chấm theo `channel-truth.md` (TL;DR block):

| Signature bắt buộc | Có/Thiếu | Ghi chú |
|---|---|---|
| Grandmother-or-failure story | ✅ | "My grandmother swore these things were nearly impossible to kill." — đúng khung folklore, không phải personal-experience claim |
| "Here's why this works" + analogy | 🟡 Thiếu nửa | Có câu "Here's why this actually works" nhưng KHÔNG có analogy đi kèm (xem Leak #2) |
| Exact numbers | ✅ | "two inches", "eight dollars", "fifteen to twenty-five", "3-4 inch sections", "two months" |
| 3 mistakes | ✅ | "Three mistakes trip people up more than anything else" |
| Cost comparison (DIY vs store) | ✅ | "$8 perlite... cheaper than replacing a snake plant ($15-25)" |
| Anonymous social proof | ✅ | "A Master Gardener with Minnesota's extension office...", "Old-timers in the gardening world..." |
| Accessibility Anchors ×2-3 | ✅ | "the two-second check", "This takes about ten minutes, no fancy tools", "one light dusting is plenty" |
| ≥60% contractions | 🟡 Borderline | ~59 contraction instances / ~106 câu (~56%) — hơi dưới ngưỡng, không nghiêm trọng |
| ≥2 idioms/folksy markers | 🟡 Thiếu filler đặc trưng | Có "Here's the thing", "That's it" ×2, "Don't panic" — nhưng **0 lần "you know"/"I mean"** (filler đời thường channel-truth liệt kê cụ thể) |
| Sign-off "Happy gardening." | ✅ | Đúng, ở cuối |
| Problem-Fix format-specific: "the real reason / the simple fix" | ❌ Thiếu | Channel-truth liệt kê đây là signature phrase riêng cho format Problem-Fix — không xuất hiện trong script |

**Structure Signatures (≥2 yêu cầu, có 4/4):**
- ✅ Mantra 3-nhịp đóng bài: "Grow a little more, save a little money, and have some fun doing it."
- ✅ Lặp 1 con số xuyên bài: "two inches" lặp lại ở hook / diagnosis / Step 5
- ✅ Chẩn đoán chắc nịch: "It's not thirsty. It's drowning."
- ✅ Fragment ngắn: "That's it.", "No guessing required."

**Verdict DNA Voice: Moderate** — nền tảng signature rất chắc (grandmother story, exact numbers, cost comparison, mantra, số lặp) nhưng thiếu 2 mảnh cụ thể mà brand voice liệt kê là bắt buộc cho đúng format này (analogy đi kèm "Here's why this works"; filler "you know/I mean"; framing "the real reason/simple fix" của Problem-Fix).

---

## 4.5) STORYTELLING CRAFT CHECK

- [x] **Transition "trạm dừng"** — KHÔNG có, mọi chuyển Step đều có micro-bridge đúng như Spine đã thiết kế: "Once you can see the damage, the next tool you pick up decides..." / "Cutting the rot out is only half the job..." / "But before repotting this thing, there's one spot..." / "Getting the soil right only works if the watering habit changes too." Bám sát bảng Spine gần như nguyên văn — craft tốt.
- [x] **Scene có nguồn** — David Prain/Kew scene có nguồn trong research-brief Story Bank (hobby-tier, đã gắn nhãn thận trọng cả 2 file) → không phải fake-witness, chỉ có vấn đề VỊ TRÍ (xem Leak #1), không phải vấn đề nguồn.
- [x] **Mid-video re-hook tại MIDROLL_DIP** — Có: "But before you repot — there's one spot on this plant that decides everything. The crown." (~4:39) đúng mở đầu vùng dip, đúng kỹ thuật pattern-break.
- N/A **Per-item intrigue (listicle)** — không áp dụng, đây là Problem-Fix 5-step, không phải listicle thuần.
- [x] **Climax beat** — Có 1 đỉnh rõ: Step 4 (đất thoát nước + Consensus Principle 1 oxy) đặt đúng vùng dip, không phải 5 nhịp đều nhau — nhưng thiếu analogy làm đỉnh chưa "chạm" hết mức (xem Leak #2).
- [ ] 🟡 **Kết video / Identity CTA** — Theo `brand-voice-dna.md` §Cinematic Toolkit rule 5, Identity CTA phải "trao danh tính" trực tiếp kiểu *"If you're the kind of gardener who'd rather fix it with what's under the sink — you belong here."* Câu thực tế trong script — *"Checking the soil before reaching for the watering can puts someone ahead of most snake plant owners. That's genuinely worth feeling good about."* — dùng ngôi thứ ba ("someone") thay vì trao danh tính trực tiếp cho "you", nên yếu hơn công thức chuẩn. Forward-Visual Close ("2 months new growth") cũng bị đẩy vào giữa đoạn Bonus (~7:45) thay vì đặt ngay trước Identity CTA ở cuối như Spine dự tính — ending dùng hình ảnh khác ("outlast your neighbor's windowsill") thay thế, chấp nhận được nhưng là 1 lệch nhỏ so với bảng đã duyệt. 🟡 nhẹ, không chặn publish nhưng đáng sửa để tối đa hoá ending.

---

## 5) NARRATOR INTEGRITY SCAN

**Pass — 0 vi phạm.** Đã quét toàn bộ fake-experience blacklist ("I've grown/tested/spent/planted", "my garden", "my clients", "when I was", "I remember", "for X years", "after decades", "my experience", "I personally") — không có instance nào. "My grandmother swore..." đúng khung folklore cho phép (không phải bằng chứng cá nhân của narrator). Không có tông "họ giấu bạn"/industry-accusation. Mọi claim khoa học đều gắn nguồn (extension, NYBG, Iowa State, CT Agricultural Experiment Station) hoặc hedge rõ ("Plenty of growers use...", "To be fair, cinnamon isn't a cure").

---

## 6) COMPLIANCE FLAG (nhẹ — không chấm lại Risk Score)

**Clean — 0 dấu hiệu rõ.** Không thấy blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal — chỉ có "cinnamon isn't a cure" dùng đúng nghĩa phủ định, không phải claim). Peroxide/cinnamon đã hedge đúng tier ("Plenty of growers use...", "roughly one part... to a few parts"), khớp với `[Tier 4/5]` trong research-brief — không overclaim thành extension-verified. Pet/kid safety có 1 beat rõ ràng (rubbing alcohol/peroxide/rooting hormone warning + "call your vet") + callout thứ 2 cuối video (cat digging trong đất mới). Không có claim sức khoẻ con người (YMYL N/A theo research-brief). Compliance risk score chính thức đã chấm riêng 9/10 PUBLISH — audit này không thấy gì mâu thuẫn với điểm đó.

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES)

| ID | Rule | Kết quả |
|----|------|---------|
| L1 | Không cây exotic | ✅ Pass — snake plant rất phổ biến |
| L2 | Counter-intuitive claim có outcome cụ thể | ✅ Pass — "it's not thirsty, it's drowning" + finger-test cụ thể |
| L3 | Deliver title promise trong 60s | 🟡 Partial — insight chẩn đoán giao <20s, nhưng cấu trúc "5 Steps" (lời hứa chính của title) chỉ bắt đầu ~117s. Xem Leak #3 |
| L4 | Open loop xuyên giây 40-55, không chuyển preview | 🔴 FAIL — xem Leak #1 |
| L5 | Tension layer mỗi 60-90s ở phút 4-6, Problem-Fix bật Jenga | ✅ Pass — crown loop + step bridges đúng nhịp |
| L6 | Bằng chứng claim counter-intuitive trước giây 20 | ✅ Pass — "two inches" ~giây 13, xác nhận ~giây 14-19 |
| L7 | Không >10 phút mặc định | ✅ Pass — ~8:45 |
| L8 | Ưu tiên ergonomic/triple pain-removal cho seniors | ✅ Pass — đúng niche quen thuộc, không off-niche fear |
| CR1-CR11 (competitor teardown, tuỳ chọn ADOPT) | — | CR5 (safety callout rõ) ✅, CR6 (cost transparency) ✅, CR7 (hero anchor "two inches") ✅, CR9 (sensory close) 🟡 chưa rõ, CR8/CR10 (sequel tease / FAQ cuối) không có — đều optional, không bắt buộc |
| X1-X5 (AVOID list) | — | Không dính conspiracy, absolute claim, health-fear, hoặc persona tự-trồng |

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Số liệu cụ thể + nguồn cite inline đúng lúc — University of Maryland Extension, NYBG Mertz Library, Iowa State Extension, UW-Madison Extension, CT Agricultural Experiment Station — tất cả đều có trong research-brief, không bịa.
- [x] **≥2 câu Consensus Synthesis** — Có: (1) "Extension offices across the country word this differently, but they all land on the same point. It's not really the water that kills the plant. It's the oxygen" (Consensus Principle 1, 3 nguồn hội tụ trong brief) — (2) diagnosis beat dùng 2 nguồn Extension hội tụ (Maryland + Minnesota Ask Extension) cho finger-test. Đủ ≥2, không phải citation đơn lẻ lặp lại.
- [x] Science moment có chốt Action → Benefit — "Once the drainage's fixed, the proof shows up on its own: fewer black roots, more new white ones."
- [x] Claim-scoping trung thực — "cinnamon isn't a cure. It's a helper, not a fix"; "extension-recommended... roughly" hedge cho tỷ lệ đất.
- [x] Góc cơ chế mà video cùng chủ đề (đa số chỉ nói "đừng tưới nhiều") không có — cơ chế oxy + Pythium/Rhizoctonia, crown-check threshold có 2 nguồn độc lập xác nhận.
- [x] Không dính pattern slop (không cơ chế giả khoa học, không claim thần kỳ, không cấu trúc hoán đổi được).

**Kết quả: ≥2 bằng chứng đạt → PASS anti-slop.** Đây là điểm mạnh nhất của script — differentiation khoa học rất vững, đúng chiến lược FACELESS WEDGE của kênh.

---

## 7) ACTIONABLE FIXES (xếp theo tác động cao → thấp)

1. **[Cao]** Đảo trình tự đoạn 30-75s: đưa Diagnosis beat (2-nguồn Extension) lên chiếm đúng giây 40-55, đẩy Story Bank (David Prain) ra sau hoặc rút ngắn còn 1-2 câu trước giây 40. Sửa trực tiếp Leak #1.
2. **[Cao]** Thêm 1 câu analogy ngay sau "It's the oxygen" ở climax (~5:28, giữa MIDROLL_DIP_ZONE) để hoàn thiện signature "Here's why this works + analogy". Sửa Leak #2.
3. **[Trung bình]** Rút gọn đoạn Diagnosis walkthrough (hiện ~72-117s) để Step 1 rơi gần mốc ~75-90s thay vì ~117s, khớp sát hơn với bảng Spine đã duyệt (~60s). Sửa Leak #3.
4. **[Trung bình]** Viết lại câu Identity CTA cuối theo đúng công thức trao-danh-tính ngôi "you" (brand-voice-dna.md rule 5), ví dụ: *"If you're the kind of gardener who checks the soil before reaching for the can — you're already ahead of most folks growing this plant."* Đặt forward-visual (2 tháng chồi mới HOẶC "neighbor's windowsill") ngay TRƯỚC câu này, không lẫn trong đoạn Bonus.
5. **[Thấp]** Cân nhắc thêm 1-2 lần filler "you know"/"I mean" và câu framing "the real reason / the simple fix" (Problem-Fix signature) ở đâu đó giữa video để nâng DNA Voice từ Moderate lên Strong.

---

## 8) INLINE TAGS REPORT

`[NEED DATA]` — 0 chỗ mới phát sinh (research-brief đã hedge đầy đủ 3 mục Tier 4/5: peroxide ratio, cinnamon efficacy, perlite ratio — script tôn trọng đúng hedge, không claim quá tay).
`[YMYL]` — N/A (houseplant care, không phải sức khoẻ con người).
`[PET-SAFETY]` — có 2 điểm, đủ (rubbing alcohol/peroxide/rooting hormone warning + cat-digging tip cuối video).
`[HEDGE]` — đúng chỗ: "roughly one part peroxide...", "extension-recommended amendment, roughly half-and-half"-style language cho perlite.
`[COMPLIANCE]` — 0 dấu hiệu.

---

## VERDICT: REVISE

**Lý do không REJECT:** Không có hands-on claim, không thiếu safety, không blacklist — nền tảng Narrator Integrity và Compliance sạch, Anti-Slop mạnh.

**Lý do không PUBLISH thẳng:** Leak #1 (🔴 vi phạm L4 — content sai loại đúng tại vùng chết thật của kênh, giây 40-55) là lỗi sửa-được nhưng cụ thể và có bằng chứng đo lường rõ ràng, đáng sửa trước khi xuất bản vì đây chính là vùng kênh đang chết nặng nhất (AVD 25.6%, mục tiêu 40%). Kết hợp Leak #2 (thiếu analogy tại climax/MIDROLL_DIP) và Leak #3 (Step 1 trễ), 3 vấn đề này đều tập trung đúng vào 2 vùng chết dữ liệu thật của kênh — ưu tiên sửa trước GATE.

**Nhắc cuối:** Bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off TRƯỚC khi export VoiceAI.
