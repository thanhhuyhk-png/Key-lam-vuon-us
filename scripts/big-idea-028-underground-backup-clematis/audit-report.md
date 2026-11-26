# Audit Report — Bury Your Clematis 3 Inches "Wrong" | Senior Gardening Tips

> Independent QA — góc nhìn thứ 2, không có context người viết. Big Idea #028.
> Auditor: Elite Gardening Script Auditor (mkt-youtube-script-audit)

---

## 1) HEADER

```
MODE: A | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard
DNA VOICE:          Moderate
NARRATOR INTEGRITY: Pass
HOOK:               Needs work
COMPLIANCE (flag):  Clean (không chấm lại Risk Score — chạy mkt-yt-compliance để có số chính thức)
=> VERDICT: REVISE
```

DATA MODE dùng: `BASELINE_AVD 25.6%`, `HOOK_DROPOFF_ZONE giây 40-55`, `MIDROLL_DIP_ZONE phút 4-6` (channel-stats-garden-us-60k.md) + `lessons-learned.md` ACTIVE RULES (L1-L8, CR1-CR11).

---

## 2) TOP 3 RETENTION LEAKS

### Leak #1 — Preview enumeration occupies the front half of HOOK_DROPOFF_ZONE (giây 40-55) before the sharp open loop lands
**[trích câu gốc]:** *"Here's the thing — this isn't some backyard trick your neighbor swears by. It sounds backwards, but stick with me, because it actually makes sense. We'll cover why the rule you learned is wrong for this one plant, the actual science behind it, and the three steps to do it right. And near the end, I'll show you the one spot on the stem to leave alone."*

→ **Lý do viewer rớt:** Ước lượng theo nhịp đọc TTS (~2.3-2.5 từ/giây), khoảng giây 40-50 của video rơi đúng vào đoạn "We'll cover why the rule... the actual science... the three steps to do it right" — đây là preview liệt kê chung chung (generic "we'll cover X, Y, Z"), đúng kiểu nội dung mà `lessons-learned.md` L4 cảnh báo tránh tại vùng chết này ("KHÔNG chuyển sang preview/giới thiệu tại đây"). Open loop cụ thể/sắc ("the one spot on the stem to leave alone... rots instead of working") chỉ thực sự landed ở khoảng giây 50-60 — tức nửa đầu vùng chết THẬT của kênh (giây 40-50, nơi 3/5 top video rớt nặng nhất) không có mỏ neo cụ thể nào giữ chân.

→ **Bản vá giữ DNA Voice:** Đảo thứ tự — đưa open loop sắc bén lên TRƯỚC danh sách preview, để nó chiếm trọn vùng giây 40-55:
> *"Here's the thing — this isn't some backyard trick your neighbor swears by. And there's one exact spot on that stem you can never bury by mistake — get it wrong, and the whole trick rots instead of working. Stick with me, because by the end you'll know exactly where that spot is, plus the actual science behind why this works, and the three steps to do it right."*

---

### Leak #2 — Pet/kid-safety caution paragraph inserted right before the promised "3 steps" payoff, breaking momentum at a high-anticipation moment
**[trích câu gốc]:** *"Quick word of caution before you grab your trowel: clematis sap can irritate skin... Wearing gloves while you work, and bagging up any trimmings to toss somewhere out of reach right away, goes a long way toward keeping everyone safe."* → ngay sau đó mới tới *"So here's how you actually do it — three simple steps..."*

→ **Lý do viewer rớt:** Bảng Retention Spine đã duyệt (GATE 2.5) đặt beat pet-safety ở mốc **7:00-7:30**, gắn liền với việc đóng Loop#2 ("mắt lá nào KHÔNG được chôn"). Script thực tế lại chèn nó ở khoảng phút 3:40-3:50 — ngay trước lúc video sắp trả lời "làm sao chôn cho đúng" (payoff mà Preview đã hứa từ giây 20). Một đoạn cảnh báo ~80 từ (găng tay, thú cưng, trẻ nhỏ) chen vào đúng lúc viewer đang chờ hành động cụ thể tạo ra 1 khúc trì hoãn không cần thiết, lệch khỏi bảng Spine đã duyệt.

→ **Bản vá giữ DNA Voice:** Rút gọn xuống 1 câu ngắn tại vị trí hiện tại (giữ an toàn tối thiểu), rồi trả bản đầy đủ về đúng vị trí đã duyệt (gần "three mistakes", ~7:00-7:30) gắn với việc đóng Loop#2:
> *(tại vị trí hiện tại, rút gọn còn)* "One quick heads-up before you grab your trowel — clematis sap isn't kind to skin, dogs, or cats, so gloves on and trimmings out of reach." 
> *(chuyển bản đầy đủ xuống ngay trước/sau "three mistakes")* giữ nguyên câu gốc, đặt cạnh mistake #1 (chôn nhầm thân non) — đúng bảng Spine.

---

### Leak #3 — Flat "trạm dừng" transitions in Step 3 and the "three mistakes" list (no micro-bridge)
**[trích câu gốc]:** *"...just make sure it's wood, not green. Step three: you'll backfill gradually."* và *"...you lose most of the protection. Three: skipping a simple wire guard around a young plant..."*

→ **Lý do viewer rớt:** Theo Cinematic Storytelling Toolkit (brand-voice-dna.md), mọi transition cần micro-bridge (đóng ý cũ + tease món nợ mới), không phải "trạm dừng" đánh số trần trụi. "Step three: you'll backfill gradually." và "Two:..." / "Three:..." trong đoạn mistakes đều là kiểu trạm dừng thuần — không có gì kéo viewer từ ý này sang ý kia. Vị trí này nằm SAU đỉnh khoa học mạnh nhất video (wilt mechanism ở phút 4-6), tức là đúng lúc năng lượng video có xu hướng chùng xuống trước khi Forward-Visual Close cứu lại ở cuối — rủi ro rớt nhẹ ở khúc 3/4 cuối.

→ **Bản vá giữ DNA Voice:** Thêm 1 câu bridge trước mỗi bước/mistake tiếp theo:
> "...just make sure it's wood, not green. Get that right, and step three is almost too easy." → "Step three: you'll backfill gradually."
> "...you lose most of the protection. Nail those two, and there's still one more sneaky way this trick fails." → "Three: skipping a simple wire guard..."

---

## 3) HOOK CHECK — soi giây 40-55 (HOOK_DROPOFF_ZONE)

- [x] Có đòn đau / viễn cảnh tương phản? — Có, dạng nghịch lý trí tuệ ("mọi guide nói X, RHS nói ngược lại"), nhưng chưa phải viewer-POV pain scene mạnh.
- [ ] Có Open Loop / Countdown anchor rõ ràng ngay đầu? — Yếu; open loop cụ thể chỉ xuất hiện cuối Preview, không phải ngay từ câu đầu.
- [ ] 5 từ đầu mạnh (verb mệnh lệnh / pain statement)? — **Fail.** "Every gardening guide tells you…" là câu dẫn trung tính, không phải mệnh lệnh hay pain statement trực diện.
- [x] Mini-payoff trước ~20s? — Có, RHS + "three inches" xuất hiện ~giây 14.
- [ ] Câu rơi vào HOOK_DROPOFF_ZONE (giây 40-55) có open loop giữ chân đủ sớm? — **Yếu**, xem Leak #1.

**Fail 2/5 tiêu chí → 2 bản hook rewrite (giữ DNA Voice):**

**Rewrite A (đảo thứ tự, sửa tối thiểu):**
> "Every gardening guide tells you to plant level with the soil — go deeper, and you rot the crown. But the Royal Horticultural Society says do the exact opposite for one plant: bury your clematis three inches deep, on purpose. That buried stem becomes a hidden backup plant, waiting underground to take over. If a mower, a hard frost, or even a rabbit wipes out the one on top, that backup is ready to step in.
>
> Here's the thing — this isn't some backyard trick your neighbor swears by. And there's one exact spot on that stem you can never bury by mistake — get it wrong, and the whole trick rots instead of working. Stick with me, because by the end you'll know exactly where that spot is, the actual science behind why this works, and the three steps to do it right."

**Rewrite B (mở bằng visual command + pain scene, sửa 5-từ-đầu):**
> "Stop. If you just planted a clematis level with the soil, like every guide tells you to — you may have already made the one mistake that kills it. The Royal Horticultural Society says bury it three inches deeper than that, on purpose. That buried stem becomes a hidden backup plant, waiting underground to take over if a mower, a hard frost, or a rabbit wipes out the one on top.
>
> Here's the thing — this isn't some backyard trick your neighbor swears by. And there's one exact spot on that stem you can never bury by mistake, or the whole trick rots instead of working. Stick with me: by the end, you'll know exactly where that spot is, the science behind why deep planting saves this one plant, and the three simple steps to do it right."

---

## 4) DNA VOICE AUDIT

| Signature element (channel-truth.md bắt buộc) | Có/Thiếu | Ghi chú |
|---|---|---|
| Grandmother-or-failure story | ✅ Có | P5: "old-timers say... 'my grandmother always buried her clematis deep'" — đúng khung folklore, không phải bằng chứng cá nhân |
| "Here's why this works" + analogy | ✅ Có | P6 "Here's why this works" + analogy "second plant hiding underground" (P8) |
| Exact numbers | ✅ Có | "2-3 inches", "4 to 8 hours" |
| 3 mistakes | ✅ Có | P20, đủ 3 mistake rõ ràng |
| Cost comparison | 🟡 Yếu | Có beat ("dirt-cheap... against the cost of replacing a dead vine") nhưng **KHÔNG có con số $ cụ thể** — lệch khỏi pattern "100% top video có specific quantity" và CR6 |
| Anonymous social proof | ✅ Có | "Gardeners on extension forums... report the same outcome" — đúng hướng dẫn research-brief (tránh case study bịa) |
| Accessibility Anchors ×2-3 | 🟡 Yếu | Chỉ thấy 1 mờ nhạt ("just a few extra minutes of digging"); thiếu dạng rõ như "Just 1 drop"/"Takes 30 seconds" |
| ≥60% contractions | ✅ Có | Mật độ contraction cao xuyên script |
| ≥2 idioms khác nhau | ✅ Có | "the proof is in the pudding", "dirt-cheap" |
| ≥1 folksy marker | 🟡 Biên | "old-timers", "your neighbor swears by" — gần đúng tinh thần nhưng không khớp đúng list ("folks"/"a neighbor of mine"/"trust me on this") |
| Sign-off `Happy gardening.` | ✅ Có | Cuối script |

→ 2/11 element yếu rõ (Accessibility Anchors, Cost $ figure) + 1 biên (folksy marker) → **DNA VOICE: Moderate** (không Weak vì phần lõi — voice, narrator framing, numbers, mistakes, social proof — vẫn vững).

---

## 4.5) STORYTELLING CRAFT CHECK

- **Transition "trạm dừng":** Step 2→3 và trong "three mistakes" là trạm dừng phẳng (xem Leak #3). Phần đầu-giữa video (Hook→Paradigm Shift→Framework) có bridge tốt hơn.
- **Scene (≥1-2):** ✅ 1 scene viewer-POV rõ: *"Picture this: you're mowing along the fence line, and the blade catches a low vine you didn't see."* — không có documented-history scene, nhưng research-brief xác nhận Story Bank trống (đã search 4+ lần, không tìm được nguồn kiểm chứng được) → KHÔNG phải lỗi, đúng quy trình zero-hallucination.
- **Mid-video re-hook tại MIDROLL_DIP (phút 4-6):** Science moment (wilt non-systemic) đặt đúng vị trí phút 4-6, đúng bảng Spine — nhưng không có câu "nói thẳng với 1 nhóm viewer đang định rời" kiểu rule 4 (optional, không bắt buộc). 🟡 nice-to-have, không chặn GATE.
- **Per-item intrigue:** N/A — không phải listicle.
- **Climax beat:** ✅ Có — cơ chế "fungus non-systemic, root luôn sống" là đỉnh khoa học của video, đặt đúng vùng MIDROLL_DIP với build-up đầy đủ từ Paradigm Shift trước đó. Không có climax nào khác cạnh tranh.
- **Forward-visual close trước Identity CTA:** ✅ Có — *"By next spring, you could be looking at a vine that shrugged off a hard frost or a mower nick without missing a beat."* → rồi mới Identity CTA *"If so, you belong here."* Đúng thứ tự rule 9→5. Timeframe "by next spring" khớp khung research-brief (không overclaim).

---

## 5) NARRATOR INTEGRITY SCAN

**PASS — 0 vi phạm.** Đã quét đủ fake-experience blacklist ("I've grown/tested/spent/planted", "my garden", "when I was", "I remember", "for X years", "after decades", "my experience", "I personally") — không xuất hiện trong script. Câu "my grandmother always buried her clematis deep" được đóng khung đúng là lời old-timers kể lại ("You'll hear old-timers say things like…"), không phải tuyên bố trải nghiệm cá nhân của narrator — hợp lệ theo quy định folklore-only.

---

## 6) COMPLIANCE FLAG (nhẹ)

**Clean.** Không thấy blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal). Pet/kid safety có mặt (sap gây kích ứng da, cảnh báo chó/mèo/trẻ nhỏ) — chỉ lệch VỊ TRÍ so với Spine (xem Leak #2), không lệch NỘI DUNG. Không phải YMYL con người (không phải ăn uống/thuốc) nên không cần disclaimer y tế — đúng đánh giá research-brief. Đây chỉ là flag nhẹ tham khảo — số Risk Score chính thức đã có ở vòng compliance riêng (9/10), audit này không chấm lại.

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES)

| ID | Rule | Kết quả |
|---|---|---|
| L1 | Đừng chọn cây exotic/niche | ✅ Pass — clematis phổ biến ở garden center Mỹ |
| L2 | Counter-intuitive claim cần outcome cụ thể | ✅ Pass — "sống sót mower/frost/rabbit, mọc lại trong vài tuần / mùa sau" |
| L3 | Deliver title promise trong 60s | ✅ Pass — RHS + "3 inches" ở ~giây 14 |
| L4 | Open loop xuyên giây 40-55 | 🟡 Yếu — xem Leak #1, có nhưng đến muộn trong vùng chết |
| L5 | Tension layer phút 4-6, Jenga Retention | ✅ Pass mạnh — science moment (wilt non-systemic) đặt đúng chỗ, đây là điểm mạnh nhất script |
| L6 | Bằng chứng claim sốc trước giây 20-33 | ✅ Pass — RHS/3in ở giây ~14, đe dọa cụ thể (mower/frost/rabbit) phủ đúng giây 20-33 |
| L7 | Không vượt 10 phút mặc định | ✅ Pass — ~1356 từ ≈ 9 phút, đúng target 8-10′ |
| L8 | Ưu tiên ergonomic stacked-benefit | N/A — không phải kiểu title "No X No Y No Z", không vi phạm |

Không có 🔴 vi phạm ACTIVE RULE nào. L4 ở mức 🟡 cần sửa (đã có patch ở Leak #1).

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Số liệu cụ thể + nguồn cite đúng lúc — "4 to 8 hours" (crown rot), "2-3 inches" (RHS/Ashridge/Ask Extension), timeline "vài tuần" vs "mùa sau" tách đúng theo research-brief.
- [x] ≥2 câu Consensus Synthesis — (1) P4 "RHS, International Clematis Society, và university extension services... all recommend it... It's the official planting guide" (Consensus Principle 1); (2) P15 "extension services and the Royal Horticultural Society have landed on the same answer today... they all agree on one thing" (Consensus Principle 2). Cả 2 đều bọc folksy, không lặp "Nguồn A nói X" trần trụi.
- [x] Science moment có chốt Action → Benefit — cơ chế nấm non-systemic → benefit "root system almost always fine, new shoots push up."
- [x] Claim-scoping trung thực — tách rõ large-flowered vs small-flowered clematis; tách "vài tuần" (tổn thương cục bộ) vs "mùa sau" (chết toàn bộ) đúng như research-brief cảnh báo tránh gộp.
- [x] KHÔNG dựng case study cá nhân bịa — script dùng "Gardeners on extension forums... report the same outcome" đúng như research-brief chỉ định (Q3 xác nhận KHÔNG có case study kiểm chứng được), KHÔNG bịa "a gardener in Ohio…".
- [x] Không dính pattern slop (cơ chế giả khoa học, claim thần kỳ, cấu trúc hoán đổi được).

**≥2 bằng chứng đạt → PASS.** Không có pattern slop.

---

## 7) ACTIONABLE FIXES (xếp theo tác động)

1. **[CAO]** Đảo thứ tự Preview — đưa open loop sắc ("the one spot you can never bury by mistake") lên TRƯỚC danh sách "we'll cover X, Y, Z", để nó chiếm trọn giây 40-55 thay vì đến muộn (xem Leak #1 + Hook Rewrite A/B).
2. **[CAO-VỪA]** Dời đoạn pet/kid-safety đầy đủ về đúng vị trí đã duyệt trong Retention Spine (~7:00-7:30, cạnh "three mistakes"/đóng Loop#2); tại vị trí hiện tại (trước 3 bước) chỉ giữ 1 câu cảnh báo ngắn (xem Leak #2).
3. **[VỪA]** Thêm micro-bridge cho Step 2→3 và giữa 3 mistake, tránh "trạm dừng" phẳng (xem Leak #3).
4. **[VỪA]** Thêm con số $ cụ thể vào beat cost-comparison cuối script (vd "$15-20 cho 1 cây clematis mới ở garden center" thay vì chỉ "dirt-cheap") — khớp signature "cost comparison" + pattern "100% top video có specific quantity".
5. **[THẤP]** Thêm 1-2 Accessibility Anchor rõ ràng ở đoạn 3-bước ("Takes just a few extra minutes", "One extra step, that's it") để đạt đủ ×2-3 theo signature yêu cầu.

---

## 8) INLINE TAGS REPORT

- `[NEED DATA]` — 0 tag còn sót trong script.md (đã resolve sạch trước khi finalize; đúng quy trình — script KHÔNG dùng số Jarvis-Lowry 50.7%/47.7% chưa verify full-text, và KHÔNG dựng case study cá nhân dù research-brief thiếu case study xác minh được).
- `[YMYL]` — Rủi ro thấp (không phải ăn uống/thuốc); không cần disclaimer y tế.
- `[PET-SAFETY]` — Có 1 block (P9, sap kích ứng da/độc với chó mèo) — nội dung đúng, chỉ cần dời vị trí (xem Leak #2).
- `[HEDGE]` — Timeline "vài tuần" vs "mùa sau" đã tách đúng, không overclaim tốc độ hồi phục.
- `[COMPLIANCE]` — Không có dấu hiệu nào cần chuyển cho mkt-yt-compliance ngoài số Risk Score đã có sẵn.

---

## VERDICT GATE

**REVISE** — không có lỗi REJECT-level (không hands-on claim, không blacklist nặng, không thiếu safety note, không case study bịa). Nhưng Hook fail 2/5 checklist + 3 retention leak sửa được (đều có patch cụ thể giữ nguyên DNA Voice) → cần sửa trước khi qua GATE publish cuối cùng, theo đúng định nghĩa REVISE trong SKILL.

**Nhắc cuối:** Bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off TRƯỚC khi export VoiceAI.
