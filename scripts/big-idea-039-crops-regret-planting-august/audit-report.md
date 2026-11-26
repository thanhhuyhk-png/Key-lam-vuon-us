# Independent Script Audit — big-idea-039-crops-regret-planting-august

> Auditor: mkt-youtube-script-audit (V7 Lean) — góc nhìn thứ 2 độc lập, không có context viết.
> Script: `script.md` (1,363 từ TTS, ~9-9.5 phút @150wpm) | Đối chiếu: `outline.md`, `research-brief.md`, `retention-spine.md`

---

## 1) HEADER

```
MODE: A (Standard) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard
DNA VOICE:          Moderate  (2/8 signature bắt buộc = 0 instance: anonymous social proof, cost comparison)
NARRATOR INTEGRITY: Pass (0 flags — quét đủ fake-experience blacklist, 0 match)
HOOK:               Needs work (1 leak — xem #2 dưới)
COMPLIANCE (flag):  Clean (0 blacklist, pet/kid safety present, không YMYL)
=> VERDICT: REVISE
```

---

## 2) TOP 3 RETENTION LEAKS

**Leak #1 — Credibility/pet-safety block ngồi ngay đuôi vùng chết giây 40-55, đẩy payoff Item #1 (Spinach) trễ hơn mốc <60s mà chính Spine đặt ra.**

> **[trích]** *"Every fact today comes from real university extension offices, like the ones in South Dakota, Illinois, and Maryland, not guesswork. One quick note before we get into it: all five of these are common vegetables, safe for pets and grandkids to be around in the garden. Nothing here needs special handling."* (word 131-181, ≈ giây 52-72 @150wpm)

- Open loop giây 40-55 (word ~96-131, "the one your grandmother would've called the real prize") CÓ mặt đúng chỗ — tốt. Nhưng ngay sau đó, thay vì tiếp tục tension, script chèn 1 đoạn "housekeeping" (nguồn tin + pet-safety) dài ~50 từ đúng vào đuôi vùng chết kênh, rồi mới tới nội dung thật của Spinach (word ~196+, thực chất giá trị bắt đầu ở word ~251 = ~1:40-1:47). Retention-spine tự đặt mục tiêu "Giao mảnh lớn đầu tiên: item #1 Spinach ~ giây 60 (word idx ~150)" — script trễ hơn mốc này khoảng 30-45 giây quy đổi.
- Rule L4 (lessons-learned) nói rõ: "KHÔNG chuyển sang preview/giới thiệu tại đây" — đoạn credibility+disclaimer này về bản chất là 1 dạng "giới thiệu về video" (dù không phải tự giới thiệu narrator), vẫn có nguy cơ đọc như 1 khoảng dừng thay vì tiếp tục kéo tension.

**Fix (giữ DNA Voice):**
> *"Every fact here comes straight from real university extension research — South Dakota, Illinois, Maryland — not guesswork, and all five of these are common vegetables, safe for pets and grandkids. First up, the one you can get in the ground today: spinach."*
(gộp credibility + pet-safety + transition thành 1 hơi, cắt ~15-20 từ, kéo payoff Spinach gần mốc 55-60s hơn.)

---

**Leak #2 — Payoff của Open Loop #1 ("kale = phần thưởng thật sự") dựa trên 1 claim so sánh KHÔNG có nguồn trong research-brief.**

> **[trích]** *"Out of all five crops today, kale shows the sweetening effect the most dramatically... It happens more noticeably in kale than almost anything else you'll grow."*

- Đây là câu trả lời cho open loop đã gài 2 lần (hook + giây 40-55) — điểm cao trào nhất của toàn video. Nhưng research-brief Câu hỏi 1 chỉ nói kale/chard/collards "develop a sweeter taste" cùng cơ chế với root crops — KHÔNG có xếp hạng "kale ngọt/rõ rệt hơn 4 loại còn lại". Research-brief còn tự flag NEED DATA: "Nghiên cứu peer-reviewed định lượng riêng cho kale... không thể WebFetch... KHÔNG trích dẫn số liệu cụ thể." Superlative "most dramatically / more noticeably than almost anything else" là suy diễn thêm, không truy được nguồn — vi phạm CR4 (claim-scoping honesty) đúng tại beat quan trọng nhất video.

**Fix (giữ DNA Voice, đổi trục sang thứ ĐÃ có nguồn — độ bền lạnh, không phải "ngọt nhất"):**
> *"Here's why. Kale takes the cold further than any of the other four — extension research from South Dakota and Oregon says a light frost pulls the bitterness out and pushes the sweetness in, and kale just keeps doing that, down into real cold, especially with a little row cover."*
(giữ nguyên "phần thưởng thật sự" nhưng đổi lý-do sang "chịu lạnh lâu nhất/liên tục nhất" — điều research-brief thực sự support, thay vì so sánh mức độ ngọt.)

---

**Leak #3 — Preview 30-60s không nêu tên bất kỳ item nào trong 5 crop → chỉ 1 loop sống thay vì nhiều loop chồng (CR2, craft rule đã biết).**

> **[trích]** *"We're covering all five today. The one at the very end is the one your grandmother would've called the real prize of a fall garden."*

- CR2 (competitor-teardown rule, ACTIVE trong `lessons-learned.md`): "Listicle/checklist: nêu TÊN tất cả item ngay trong preview → nhiều open-loop cùng lúc." Script chỉ tease item cuối (kale), 4 item còn lại (spinach/beets/carrots/chard) hoàn toàn ẩn danh cho tới khi lượt tới — nghĩa là suốt phút 1-8, viewer chỉ có đúng 1 loop sống thay vì 4-5 loop xếp chồng.

**Fix:**
> *"We're covering all five today: spinach, beets, carrots, chard, and the one at the very end your grandmother would've called the real prize of a fall garden."*
(thêm ~2 giây TTS, mở thêm 4 loop cùng lúc, không cần bỏ open loop kale đã gài.)

---

## 3) HOOK CHECK — soi đặc biệt giây 40-55 (HOOK_DROPOFF_ZONE)

- [x] Đòn đau/viễn cảnh tương phản — dạng Revelation (đúng type đã confirm trong Spine): "Cold doesn't ruin your garden... it flips a switch" — myth-reversal, phù hợp hook type đã chọn.
- [x] Open Loop / Countdown anchor — "five vegetables" + "the one at the very end... your grandmother..." — có, đúng chỗ.
- [x] 5 từ đầu mạnh — "Cold doesn't ruin your garden" — declarative myth-reversal, chấp nhận được cho Revelation type.
- [x] Mini-payoff trước ~20s — cơ chế + con số "forty degrees Fahrenheit" xuất hiện ở word ~17-19 (~giây 7-8 @150wpm) — RẤT sớm, vượt yêu cầu.
- [~] Câu rơi vào HOOK_DROPOFF_ZONE (giây 40-55): loop-cue CÓ sống đúng chỗ, nhưng ngay sau đó là block credibility/disclaimer (xem Leak #1) — không hẳn "chuyển sang giới thiệu", nhưng đọc như 1 khoảng dừng thay vì tiếp tục siết tension.

→ Hook cơ bản vững (chứng minh sớm, đúng L6), nhưng cần sửa Leak #1 để giữ trọn đà qua vùng chết.

---

## 4) DNA VOICE AUDIT (đối chiếu `channel-truth.md` + `brand-voice-dna.md`)

**Có mặt (đúng tần suất quy định):**
| Element | Tần suất script | Target |
|---|---|---|
| "Here's why" / "Here's why this works" | 3x (word 251, 577, 1059) | 2-3 ✓ |
| "Don't panic" | 1x | 1 ✓ |
| "That's it" | 1x (line 71) | 1 ✓ |
| Grandmother reference (folklore) | 2x ("your grandmother", hook + kale) | 1-2 ✓ |
| Accessibility Anchors | 3x ("Just one overnight soak", "thirty seconds a row", "All you need is that layer of mulch") | 2-3 ✓ |
| Gardener idioms (≥2 khác nhau) | "dirt-cheap", "rain or shine" | ≥2 ✓ |
| Folksy marker | "most folks" | ≥1 ✓ |
| AI clichés (blacklist) | 0 match (đã grep toàn bộ) | 0 ✓ |
| Contractions | Rải đều xuyên script (doesn't/it's/that's/you're/they're/don't...) | ≥60% ✓ (qualitative) |
| Sign-off | "Happy gardening." | ✓ |
| "Your neighbors will..." | 1x (biến thể "wonder" thay vì "ask") | ✓ tinh thần đúng |

**THIẾU hoàn toàn (0 instance) — nằm trong "SIGNATURE bắt buộc/script" của channel-truth.md:**
- 🟡 **Anonymous social proof** — 0 lần "a viewer in [state]" / "a gardener I spoke with" / "master gardeners often report" trong toàn bài. Grep xác nhận 0 match cho viewer/subscriber/neighbor-of-mine.
- 🟡 **Cost comparison (DIY vs store)** — 0 số tiền, 0 so sánh chi phí trong toàn script. Grep xác nhận 0 match `$`/dollar.

→ Cả 2 đều fix được dễ dàng mà không phá cấu trúc (ví dụ chèn 1 câu social proof ở đoạn carrots/candy-carrots, hoặc 1 câu cost so sánh ở đoạn kết "a little more food, a little extra saved").

**Structure Signatures (≥2/script yêu cầu) — đạt 3/4:**
- ✅ Mantra 3-nhịp đóng bài: *"A little more food, a little extra saved, and honestly, some fun out there too!"* — đúng công thức.
- ✅ Lặp 1 con số xuyên bài: **"forty degrees"** xuất hiện 3 lần (hook, carrots, recap "Here's the number that ties it all together") — đúng chữ ký #2, thực thi tốt.
- ✅ Fragment ngắn tạo nhịp: "That's it.", "Four down.", "Two down, three to go."
- Chẩn đoán chắc nịch mở/đóng: có nhưng nhẹ hơn ("Cold doesn't ruin your garden. It flips a switch." đóng vai trò tương đương).

→ DNA Voice: **Moderate** — texture/signature phrase execution mạnh, nhưng thiếu 2 element bắt buộc (social proof, cost) kéo điểm xuống khỏi "Strong".

---

## 4.5) STORYTELLING CRAFT CHECK (Cinematic Toolkit — `brand-voice-dna.md`)

- [~] **Micro-Bridge mọi transition** — 4/5 bridge tốt (đóng ý cũ + tease mới): "Spinach gets you started. But beets are where the real efficiency kicks in." / "That's carrots... But chard is the one that keeps paying you back into next year." 2 transition có dáng "trạm dừng" nhẹ ("Two down, three to go", "Four down.") nhưng đều đi kèm tease ngay sau nên chấp nhận được — không flag cứng.
- [x] **≥1-2 scene có nguồn** — Scene "Candy Carrots" (Eliot Coleman, Harborside Maine, đầu 1980s) khớp CHÍNH XÁC với Story Bank trong research-brief (tên, thập niên, địa danh, URL EcoFarming Daily) — PASS, không có nhân chứng bịa.
- [x] **Mid-video re-hook tại MIDROLL_DIP (phút 4-6)** — *"And this one's for those of you who already got your carrots in the ground weeks ago. The mistake isn't in the planting. It's pulling them too early."* rơi đúng ~4:58-5:10 — PASS.
- [x] **Per-item intrigue (≥3-4 item, bắt buộc đầu+cuối)** — Cả 5/5 item đều có differentiation có nguồn: Spinach (thermal dormancy twist), Beets (2 harvests/1 planting), Carrots (myth-bust + scene), Chard (biennial "pays back next year"), Kale (item cuối, "phần thưởng thật sự" — nhưng xem Leak #2 về nguồn của claim cụ thể). PASS về cấu trúc, có 1 vấn đề nguồn ở item cuối.
- [x] **Climax Beat** — đỉnh rõ ràng tại scene "Candy Carrots" (phút ~5, trong đúng MIDROLL_DIP) — không phải 7 nhịp đều nhau. PASS.
- [x] **Forward-Visual Close → Identity CTA → geo-comment CTA → sign-off** — đúng thứ tự: *"you could be walking out to a garden bed still full of color... If you're the kind of gardener who'd rather plant one more round... you belong here... What's your state or USDA zone..."* → `Happy gardening.` PASS, bám sát template.
- [ ] 🟡 **CR2 (preview nêu tên tất cả item)** — KHÔNG đạt, xem Leak #3.

---

## 5) NARRATOR INTEGRITY SCAN

**0 vi phạm.** Đã quét đủ fake-experience blacklist (I've grown/tested/spent/planted, my garden, my clients, when I was, I remember, for X years, after decades, my experience, I personally, I recommend/think/believe, in my garden) — **0 match** trong toàn script.

- "your grandmother" (không phải "my grandmother") dùng như folklore hướng về viewer — an toàn hơn cả spec mặc định.
- Tên riêng duy nhất (Eliot Coleman) có nguồn URL rõ trong research-brief Story Bank, không phải nhân chứng bịa.
- Không có tông "họ giấu bạn" / industry-accusation.

→ **PASS sạch.**

---

## 6) COMPLIANCE FLAG (nhẹ — không chấm lại Risk Score, đã 9/10 ở bước khác)

- Blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal): **0 match.**
- YMYL: không áp dụng (rau củ thông thường, không phải foraging/health/nutrition claim).
- Pet/Kid safety: **có mặt rõ ràng, đúng vị trí** ("safe for pets and grandkids to be around in the garden. Nothing here needs special handling.") — cũng là 1 trong 3 comment-engagement themes của kênh, thực thi tốt.

→ **Clean, không có gì cần chuyển compliance re-check.**

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES)

| ID | Rule | Kết quả |
|----|------|---------|
| L1 | Đừng chọn cây exotic/niche | ✅ PASS — cả 5 cây đều phổ biến (kale, carrots, spinach, beets, chard) |
| L2 | Counter-intuitive phải có outcome cụ thể | ✅ PASS — carrots "backwards" claim có outcome cụ thể (forking) + Coleman scene |
| L3 | Deliver title promise trong 60s đầu | ✅ PASS — cơ chế + proof xuất hiện trong 10-15 giây đầu |
| L4 | Open loop xuyên giây 40-55 | ✅ PASS (nhưng xem Leak #1 — đuôi zone có vấn đề) |
| L5 | Tension layer phút 4-6 | ✅ PASS mạnh — Carrots + scene Coleman đúng vị trí Spine đã thiết kế |
| L6 | Bằng chứng/số trước giây 20 | ✅ PASS — "forty degrees" ở word ~17-19 |
| L7 | ≤10 phút mặc định | ✅ PASS — 1,363 từ ≈ 9-9.5 phút |
| L8 | Ergonomic stacking (nếu áp dụng) | N/A — không phải title dạng triple-pain-removal |
| CR2 | Preview nêu tên tất cả item | 🟡 KHÔNG đạt — xem Leak #3 |
| CR4 | Claim-scoping honesty | 🟡 1 vi phạm nhẹ — xem Leak #2 (superlative "most dramatically" không có nguồn) |

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Số liệu cụ thể + nguồn cite inline đúng lúc — dày đặc, đúng lúc (SDSU/UMD/Mississippi State/Illinois/WVU/USU đều được gọi tên trong prose, không chỉ liệt kê cuối bài).
- [x] **≥2 câu Consensus Synthesis** — ĐẠT 2/2 rõ ràng: (1) *"Extension services in Maryland, Mississippi, and Utah word it differently, but they all land on the same window..."* (khớp Consensus Principle #2), (2) *"Extension offices in Illinois and West Virginia don't agree on much. But they agree on this: leave your carrots in the ground through that first frost."* (khớp Consensus Principle #3). Cả 2 đều bọc folksy wrapper đúng chuẩn ("Now here's the interesting part").
- [x] Science → Action → Benefit — hook: cơ chế → "these five crops are ready to plant now" (action) → "harvesting food sweeter" (benefit). PASS.
- [~] Claim-scoping trung thực — PASS phần lớn, nhưng Leak #2 (kale superlative) và 2 con số chưa hedge đủ (xem mục 8) là ngoại lệ đáng sửa.
- [x] Góc cơ chế/research khác biệt — scene Coleman "candy carrots" là differentiator thật, 1 kênh AI-voice generic cùng niche khó có được (có tên, năm, địa danh, nguồn).
- [x] Không dính pattern slop (giả khoa học/claim thần kỳ vô nguồn/cấu trúc hoán đổi) — sạch.

→ **≥2 bằng chứng đạt, không dính slop pattern.** Anti-slop check PASS, không phải lý do REVISE.

---

## 7) ACTIONABLE FIXES (xếp theo tác động)

1. **[CAO]** Sửa Leak #1 — gộp/cắt gọn block credibility+pet-safety (word 131-181) để Item #1 Spinach vào nội dung thật gần mốc 55-60s hơn thay vì ~1:40. (bản vá ở mục 2)
2. **[CAO]** Sửa Leak #2 — đổi trục lý-do "kale = phần thưởng thật sự" từ "ngọt nhất/rõ rệt nhất" (không có nguồn so sánh) sang "chịu lạnh lâu nhất/liên tục nhất" (có nguồn SDSU/Oregon). Đây là payoff của loop chính cả video, cần đúng.
3. **[TRUNG BÌNH]** Thêm 2 signature bắt buộc đang thiếu: 1 câu anonymous social proof (vd chèn gần đoạn Coleman: *"One gardener up in Minnesota said leaving carrots in through the first snow was the best trick she ever picked up."*) + 1 câu cost-comparison ngắn ở đoạn kết (vd: *"One packet of seeds, a few dollars, versus what you'd pay for 'winter-sweetened' greens at the store."*).
4. **[TRUNG BÌNH]** Sửa Leak #3 — liệt tên 5 crop trong preview 30-60s thay vì chỉ tease kale, để mở nhiều loop cùng lúc (CR2).
5. **[THẤP]** Hedge 2 con số chưa đủ nguồn: (a) spinach "above about seventy-five degrees... simply refuse to sprout" — source thực tế là đường cong dần (spotty 75-80°F, gần như dừng hẳn ở 85°F), nên đổi sang "somewhere in the mid-to-upper seventies, germination gets spotty, and it stalls out almost completely once you're near eighty-five" HOẶC giữ đơn giản nhưng hạ độ chắc chắn; (b) kale "down into the teens for some varieties" — không có trong research-brief, cần tìm nguồn hoặc đổi thành hedge chung "real cold" không kèm số cụ thể.

---

## 8) INLINE TAGS REPORT

- `[NEED DATA]` — kale cold-tolerance "down into the teens" (không có trong research-brief); claim so sánh "kale sweetens most dramatically / more noticeably than almost anything else" (không có ranking nguồn).
- `[HEDGE]` — spinach germination-halt threshold "above about seventy-five degrees... simply refuse to sprout" nên mềm hơn so với đường cong thật của nguồn (spotty 75-80°F → halt ~85°F).
- `[PET-SAFETY]` — đã có, đúng vị trí, không cần sửa.
- `[YMYL]` — không áp dụng.
- `[COMPLIANCE]` — không có gì để chuyển, Clean.

---

## VERDICT: REVISE

**Lý do REVISE (không REJECT, không PUBLISH thẳng):**
- Không có Narrator Integrity violation, không có compliance blacklist, không có YMYL thiếu disclaimer → không đủ căn cứ REJECT.
- Nhưng có 1 retention leak cụ thể ngay tại vùng chết đã biết của kênh (Leak #1), 1 claim thiếu nguồn nằm đúng ở payoff cao trào nhất video (Leak #2), 1 cơ hội craft đã biết nhưng chưa áp dụng (Leak #3/CR2), và 2 signature element bắt buộc thiếu hoàn toàn (social proof, cost comparison) → đủ để không PUBLISH thẳng.
- Tất cả đều sửa được nhanh, giữ nguyên cấu trúc Spine đã duyệt — không cần viết lại toàn bộ.

---

**Nhắc cuối:** Bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off TRƯỚC khi export VoiceAI.
