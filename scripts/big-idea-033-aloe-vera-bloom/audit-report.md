# Audit Report — "3 Signs Your Aloe Vera Is About to Bloom (Don't Miss It)"

> Audit ĐỘC LẬP (mkt-youtube-script-audit) — không giả định self-audit/Triple F/compliance trước đó đã đúng.
> Script: `script.md` · Word count TTS body ≈ **1,264 từ** (target 1,200–1,500 ✅) · Runtime ước tính ~9:10 (trong khung 8-10' ✅, dùng nhịp ~2.3 từ/giây để đối chiếu vùng chết theo giây/phút — ước tính, không phải số đo thật).

---

## 1) HEADER

```
MODE: A (Standard) | DATA: DATA MODE (channel-stats-garden-us-60k.md AUDIT TL;DR) | LANGUAGE: EN | VIDEO TYPE: Standard
DNA VOICE:          Moderate
NARRATOR INTEGRITY: Pass (0 flags)
HOOK:               Pass
COMPLIANCE (flag):  Clean trên blacklist/YMYL/pet-safety — nhưng có 1 flag ACCURACY/ANTI-SLOP (nguồn chết) → xem mục 6
=> VERDICT: REVISE
```

DATA MODE variables dùng: `BASELINE_AVD` 25.6% · `HOOK_DROPOFF_ZONE` giây 40-55 · `MIDROLL_DIP_ZONE` phút 4-6. Đối chiếu thêm với `lessons-learned.md` ACTIVE RULES (L1-L8) và `retention-spine.md` của chính video này.

---

## 2) TOP 3 RETENTION LEAKS

**Leak 1 — Sign #1 reveal trễ hơn target spine ~8-15 giây, có 1 câu đệm làm chậm nhịp**
- **[trích]** *"Here's the thing — most aloe plants kept indoors never bloom at all, so if yours is trying to, that's a pretty big deal. It takes a plant that's truly ready, mature and strong enough, to put up that tall spike of orange and yellow flowers. So here's sign number one, short version."*
- **Lý do:** `retention-spine.md` đặt target đóng Loop #1 (giao Sign #1) tại **~1:00** (word idx ~150). Đếm từ thực tế: câu reveal ("the flower stalk always rises from dead center") rơi vào khoảng **từ thứ 156-175**, tức ~1:08-1:16 theo nhịp trung bình của script — trễ hơn target ~8-15s vì câu "that's a pretty big deal" là câu đệm không mang thông tin mới.
- **Bản vá (giữ DNA voice):** *"Here's the thing — most aloe plants kept indoors never bloom at all. If yours is trying to, that's a big deal, because it takes a plant mature and strong enough to put up that tall spike of orange and yellow flowers. So here's sign number one."* (cắt ~8-10 từ, giữ nguyên giọng, kéo payoff gần target hơn).

**Leak 2 — Vùng dip phút 4-6 thiếu "mid-video re-hook" nói thẳng với nhóm sắp rời (Cinematic Toolkit rule 4)**
- **[trích]** Toàn bộ đoạn từ "So now you've checked the location, and you've checked the speed..." đến hết đoạn "First, age... Second, size... Third, timing..." (~4:00-5:40) — dựa hoàn toàn vào bridge + science moment, không có câu trực tiếp gọi tên 1 nhóm khán giả đang định bỏ đi.
- **Lý do:** `brand-voice-dna.md` mục Cinematic Toolkit #4 yêu cầu 1 câu re-hook kiểu *"and this one is for those of you who…"* đúng tại `MIDROLL_DIP_ZONE`. Script bù bằng Story Bank scene (Huntington) — tốt nhưng đó là pattern-break, không phải re-hook trực tiếp. Đây là vùng dip nặng nhất kênh (-11%), 2 lớp phòng thủ tốt hơn 1.
- **Bản vá:** chèn trước "Here's why this works" (đầu Sign #3): *"And if you've been checking the center of your aloe for weeks with nothing to show for it — hang in there, because timing might be the missing piece here, not effort."*

**Leak 3 — 1 claim dựa trên nguồn đã bị chính research-brief đánh dấu chết/không đáng tin (accuracy risk, không phải retention-timing nhưng thuộc vùng rủi ro "audience tự sửa lỗi khoa học")**
- **[trích]** *"Once that stalk is up, those tubular orange and yellow flowers start opening — usually from the bottom up over a couple of weeks."*
- **Lý do:** `outline.md` Research Notes ghi hướng nở hoa "bottom-up" dựa phần lớn vào nguồn `biologyinsights.com`. `research-brief.md` (dòng 7) đã xác nhận **2 URL biologyinsights.com này hiện 404/không còn tồn tại và domain là content-farm** ("Xếp Tier 4-5 tối đa... KHÔNG dùng nguồn này"). Brief bản mới KHÔNG có câu hỏi nào re-verify hướng nở hoa bằng nguồn khác — claim "bottom-up" trôi qua từ outline cũ mà không bị bắt lại. Đây đúng kiểu lỗi mà "khán giả faceless niche chủ động report + comment sửa lỗi khoa học" (rủi ro demotion) mà channel-truth cảnh báo.
- **Bản vá (an toàn, không mất DNA voice, không cần nguồn mới):** *"Once that stalk is up, those tubular orange and yellow flowers start opening up over the next couple of weeks. Just let it happen."* (bỏ chi tiết hướng "bottom-up" chưa re-verify, giữ nguyên phần còn lại — không mất thông tin quan trọng cho viewer).

---

## 3) HOOK CHECK — soi đặc biệt câu ở HOOK_DROPOFF_ZONE (giây 40-55)

- [x] Đòn đau/viễn cảnh tương phản — "Most aloe owners will go their entire lives without ever seeing this plant flower" (rarity contrast)
- [x] Open Loop/Countdown anchor — "three very specific ways, and most people miss every single one"
- [x] 5 từ đầu mạnh — "Most aloe owners will go" (pain/contrast statement, không phải mệnh lệnh nhưng đủ mạnh)
- [x] Mini-payoff trước ~20s — "The first sign shows up right in the center of the plant, and it's easy to mistake for something else entirely" (~giây 26, đã hé lộ vị trí Sign #1)
- [x] **[DATA MODE]** Câu rơi vào HOOK_DROPOFF_ZONE (giây 40-55, ≈ từ 92-127): nội dung là "It moves fast, and honestly, most folks just aren't watching closely enough to catch it. Here's the thing — most aloe plants kept indoors never bloom at all..." — đây là **open loop + fact-giá-trị (rarity)**, KHÔNG phải câu preview/tự giới thiệu. **PASS L4.**

Lưu ý: câu có dáng dấp "preview/giới thiệu" nhất trong toàn script — *"Today we're covering all three signs, pulled straight from what extension services and plant researchers document about aloe blooming"* — rơi ở ~giây 27-35, tức **trước** vùng chết 40-55s, nên kỹ thuật không vi phạm L4. Nhưng đây là câu credibility hơi khô, đặt sát vùng chết — nếu muốn siết chặt hơn nữa có thể rút gọn, không bắt buộc.

**HOOK: Pass — không cần rewrite.**

---

## 4) DNA VOICE AUDIT

Chấm theo `references/channel-truth.md` (TL;DR) + `references/brand-voice-dna.md`.

**Signature elements — có/thiếu:**
| Element | Trạng thái |
|---|---|
| Grandmother story / personal failure story | ❌ **Thiếu** — không có "My grandmother…" hay "a neighbor of mine…" ở đâu trong script. Đây là signature phrase "bắt buộc/script" theo TL;DR (tần suất 1-2 lần/script). |
| "Here's why this works" + analogy | 🟡 Có "Here's why this works" (đúng phrase) nhưng KHÔNG có analogy đơn giản đi kèm ngay sau nó (chỉ liệt kê age/size/timing). Analogy pup-vs-stalk ("a pup is basically the plant making a copy of itself...") nằm ở đoạn khác, không gắn với science moment này. |
| Exact numbers | ✅ Rất tốt — "3 to 4 years", "12-15+ leaves", "close to an inch a day", "2-3 feet", "10-14 days", "6 hours", "1907", "200+ species" |
| 3 mistakes | N/A — format Mystery Reveal, không phải Problem-Fix, hợp lý bỏ qua |
| Cost comparison (DIY vs store) | N/A — video quan sát-only, không có sản phẩm/DIY để so giá — hợp lý bỏ qua |
| Anonymous social proof | ✅ "Growers who track it closely report…" / "Researchers who've studied aloe vera flowers directly confirm what growers have suspected for years" |
| Accessibility Anchors ×2-3 | ✅ "Takes about ten seconds to check", "Takes about thirty seconds", "All you need is one glance" (3 anchor) |
| `Happy gardening.` | ✅ Có, đúng vị trí cuối |

**Human Texture E7:** contractions dày đặc xuyên suốt (isn't/don't/that's/here's/you're/you've/aren't...) — quan sát trực quan vượt ngưỡng 60% (không đếm chính xác số câu, không bịa số). ≥2 idioms: "Mother Nature's way", "green thumb" — đạt. ≥1 folksy marker: "folks" (nhiều lần) — đạt. **0 AI cliché** (delve/leverage/moreover/furthermore...) — sạch.

**Sentence Structure Signatures (yêu cầu ≥2/script — script đạt CẢ 4):**
1. ✅ Mantra rule-of-three đóng bài: *"Grow a little patience, skip the guesswork, and have some fun watching for it."*
2. 🟡 Lặp 1 con số làm xương sống: "three" (3 signs) được nhắc lại nhưng không drill mạnh như mẫu chuẩn (5-7 lần)
3. ✅ Chẩn đoán chắc nịch: *"Straight up, stiff as a spear? That's it, no guesswork needed. That's your first sign."*
4. ✅ Fragment ngắn: *"Not the base. Not the side. Always the center."*

**Sign-off:** đúng `Happy gardening.` ✅

**Kết luận DNA Voice = Moderate:** phần "Science-Backed Proof" của voice formula được thực thi RẤT tốt (hedge đúng chuẩn, consensus synthesis, exact numbers, structure signatures). Phần "Lazy Grandma Wisdom" (folklore cá nhân — grandmother/neighbor) hoàn toàn vắng mặt, khiến giọng nghiêng về "researcher kể chuyện" hơn là "bà nội kể chuyện". Không phải lỗi Narrator Integrity (không có gì phải xoá) — mà là CƠ HỘI THÊM, không phải VI PHẠM cần xoá.

---

## 4.5) STORYTELLING CRAFT CHECK

- [x] **Micro-bridge mọi transition** — không có "trạm dừng" trần trụi. Bridge vào Sign #2: *"But location alone isn't the whole story... it doesn't creep. It sprints."* Bridge vào Sign #3: *"there's one more piece... It costs them."* Cả 2 đều đóng ý cũ + tease ý mới đúng công thức. **Mạnh.**
- [x] **≥1-2 scene có nguồn** — 2 scene: (a) documented history Huntington Desert Garden 1907 (khớp Story Bank research-brief, tên/năm/địa danh có URL) ✅; (b) viewer-POV *"Picture it — that tall spike of orange and yellow blooms, rising right out of your own windowsill."* ✅. Không có claim mới ngoài research-brief.
- [ ] **Mid-video re-hook tại MIDROLL_DIP_ZONE** — 🟡 **thiếu** (xem Leak 2 ở mục 2). Story Bank scene đóng vai trò pattern-break nhưng không phải re-hook trực tiếp gọi tên nhóm khán giả sắp rời.
- [x] **Per-item intrigue** — cả 3/3 item (kể cả đầu+cuối) đều có câu intrigue trước khi gọi tên ("it's easy to mistake for something else", "it doesn't creep, it sprints", "it costs them") — vượt yêu cầu tối thiểu (≥3-4).
- [x] **Climax beat** — 🟡 có nhưng nhẹ: đỉnh là *"Line those three up... you're looking at the real thing"* + Huntington scene ngay sau. Không lệch vào MIDROLL_DIP thiếu build-up (climax nằm ~5:40-6:38, sau vùng dip). Chấp nhận được, không bắt buộc sửa.
- [x] **Forward-visual close trước Identity CTA** — đúng thứ tự: hình ảnh tương lai *"Picture it — that tall spike..."* → rồi mới *"If you're the kind of gardener who checks the center of the pot before anything else..."* (Identity CTA). Next-video loop: không có, hợp lệ vì đây là optional.

---

## 5) NARRATOR INTEGRITY SCAN

**0 vi phạm.** Quét toàn bộ fake-experience blacklist (I've grown/tested/spent/planted, my garden, when I was, I remember, for X years, after decades, my experience, I personally) — **không xuất hiện lần nào**. Script không dùng ngôi thứ nhất số ít ở bất kỳ đâu (chỉ "we're covering" ở phần preview, hợp lệ vì "we" = host+audience, không phải hands-on claim cá nhân). Không có tông "họ giấu bạn" / industry-accusation. Không có tên người không nguồn (William Hertrich CÓ nguồn trong Story Bank). **Sạch nhất trong các script đã audit gần đây — đáng khen.**

---

## 6) COMPLIANCE FLAG

- Blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal): **0 matches.**
- Tier C (YMYL) disclaimer: N/A — research-brief Câu hỏi 5 đã xác nhận script không chạm claim y tế/edible.
- Pet/Kid safety: N/A theo nguyên tắc (không đụng spray/fertilizer/edible) — nhưng **cơ hội bỏ lỡ**: channel-truth liệt kê pet safety là "quick win engagement" (đòn bẩy comment). Aloe là cây độc nhẹ với mèo/chó nếu nhai — 1 câu ngắn kiểu *"and if you've got a cat that likes to nibble new growth, keep an eye on that flower stalk too"* vừa an toàn vừa ăn điểm engagement. Không bắt buộc, nhưng khuyến nghị.
- **Accuracy flag (không thuộc blacklist nhưng thuộc rủi ro "audience report lỗi khoa học"):** claim "bottom-up" bloom order dựa nguồn đã bị chính research-brief đánh dấu chết/content-farm — xem Leak 3, mục 2. Đề nghị `mkt-yt-compliance` không cần chấm lại Risk Score (đây không phải blacklist/YMYL) nhưng người viết nên sửa trước publish.

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES L1-L8)

| Rule | Kết quả |
|---|---|
| L1 (exotic/niche plant) | ✅ Aloe vera — cây phổ biến nhất kênh, không vi phạm |
| L2 (counter-intuitive cần outcome cụ thể) | N/A — video không có claim ngược đời |
| L3 (deliver title promise trong 60s) | 🟡 Nhẹ — Sign #1 (mảnh đầu tiên của lời hứa "3 signs") giao ở ~1:08-1:16, hơi trễ hơn target ~1:00 của chính retention-spine (xem Leak 1). Không nghiêm trọng vì hook đã hé sign #1 từ giây 26. |
| L4 (open loop giây 40-55) | ✅ Pass — xem mục 3 |
| L5 (tension layer phút 4-6) | ✅ Pass — bridge dày đặc trong vùng dip, dù thiếu re-hook trực tiếp (Leak 2) |
| L6 (N/A — không phải shock title) | N/A, đúng như retention-spine đã ghi |
| L7 (≤10 phút mặc định) | ✅ ~9:10 ước tính, trong khung 8-10' |
| L8 (ergonomic senior stacking hook) | N/A — format Mystery Reveal/curiosity, không phải method/ergonomic-offer |

**0 vi phạm 🔴.** 2 flag 🟡 nhẹ (L3 timing drift, đã nêu ở Leak 1).

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

Câu hỏi: *"Script này có gì mà một kênh AI-voice generic cùng niche KHÔNG THỂ có?"*

- [x] Số liệu cụ thể có nguồn (research-brief): tuổi/số lá/tốc độ đều đúng hedge như research-brief yêu cầu
- [x] **≥2 câu Consensus Synthesis:** (1) *"Nearly every trusted growing guide agrees on this — the flower stalk always rises from dead center of the rosette."* (Consensus Principle #1, đúng công thức hội tụ-nguồn); (2) *"Researchers who've studied aloe vera flowers directly confirm what growers have suspected for years"* (hội tụ giới nghiên cứu + giới trồng trọt cho Principle #2). Đặc biệt tốt: Consensus Principle #3 (tốc độ) — nguồn YẾU nhất theo brief — được script **KHÔNG** đóng khung là consensus, mà hedge đúng thành quan sát cá nhân người trồng ("Growers who track it closely report... not one big formal study"). Đây là xử lý tinh tế, đúng chuẩn zero-hallucination.
- [🟡] Science → Action → Benefit: science moment (energy cost) giải thích tốt WHY nhưng không chốt ngay 1 action cụ thể cho viewer ngay sau đó (age/size/timing đọc hơi liệt kê hơn là "đi làm gì tiếp"). Nhẹ, không bắt buộc sửa.
- [x] Claim-scoping trung thực: hedge tốt ở tuổi ("3-4 years, sometimes longer"), tốc độ ("strong pattern, not a guarantee"), năng lượng ("Plant physiologists... expensive" thay vì khẳng định cơ chế tinh bột mùa đông chưa có nguồn Aloe-specific)
- [x] Góc research/lịch sử mà kênh AI generic không có: Huntington Desert Garden 1907 (documented, có nguồn) + peer-reviewed MDPI/Foods energy-cost finding
- [🔴→đã sửa ở Leak 3] 1 claim (bottom-up bloom order) trôi từ nguồn đã bị chính brief đánh dấu chết — đây chính là kiểu lỗi khiến "audience chủ động report/sửa lỗi khoa học" mà phần Faceless Wedge của channel-truth cảnh báo là rủi ro demotion

**Đánh giá:** ≥2 bằng chứng consensus synthesis đạt, xử lý hedge tinh tế vượt kỳ vọng — nhưng có đúng 1 lỗ hổng cụ thể (Leak 3) làm giảm điểm "toàn bộ script đã re-verify nguồn". Không đủ nghiêm trọng để REJECT (chỉ 1 câu, dễ sửa, không phải core claim của video), nhưng đủ để REVISE trước publish.

---

## 7) ACTIONABLE FIXES (ưu tiên cao → thấp)

1. **[HIGH]** Sửa claim "bottom-up" bloom order (Leak 3) — bỏ chi tiết hướng nở chưa re-verify, dùng bản vá đã đưa. Không cần tìm nguồn mới nếu muốn xuất bản nhanh; nếu muốn giữ chi tiết "bottom-up" thì cần 1 nguồn sống mới trước publish.
2. **[MED]** Thêm 1 câu mid-video re-hook trước "Here's why this works" ở đầu Sign #3 (Leak 2) — vá đúng lỗ hổng duy nhất còn thiếu trong Cinematic Toolkit checklist, đúng tại MIDROLL_DIP_ZONE.
3. **[MED]** Thêm 1 câu folklore cá nhân ("a neighbor of mine…" hoặc "My grandmother…") ở đâu đó tự nhiên (gợi ý: đoạn "Maximizing the Bloom" — "A neighbor of mine calls the hands-off wait the hardest part of the whole thing") để phục hồi vế "Lazy Grandma Wisdom" đang nhạt hơn vế "Science-Backed Proof".
4. **[LOW]** Cắt ~8-10 từ đệm ở đoạn dẫn vào Sign #1 (Leak 1) để payoff về gần target ~1:00 của retention-spine hơn.
5. **[LOW, optional]** Thêm 1 câu pet-safety ngắn (mèo gặm cuống hoa mới) — quick-win engagement theo channel-truth, không bắt buộc.

---

## 8) INLINE TAGS REPORT

- `[COMPLIANCE]` — claim "bottom-up" bloom order dựa nguồn dead-link (mục 2 Leak 3, mục 6, mục 6.7)
- `[NEED DATA]` — claim "a stressed aloe's more likely to drop its blooms early" không có citation trực tiếp trong research-brief.md (kiến thức làm vườn phổ thông, rủi ro thấp, không bắt buộc sửa nhưng nên gắn cờ cho lần research tiếp theo)
- `[HEDGE]` — 2 chỗ hedge ĐÚNG chuẩn, đáng khen chứ không phải lỗi: tốc độ vươn cao ("strong pattern, not a guarantee") và tuổi ra hoa ("3 to 4 years, sometimes longer")
- `[YMYL]` — không áp dụng, video sạch YMYL
- `[PET-SAFETY]` — không bắt buộc, cơ hội bổ sung (mục 6)

---

## VERDICT: REVISE

**Không phải REJECT** — Narrator Integrity sạch tuyệt đối (hiếm gặp), Hook pass, 0 blacklist, 0 vi phạm ACTIVE RULES nghiêm trọng, Anti-Slop đạt ngưỡng. **Không PUBLISH thẳng** vì có 1 lỗi accuracy cụ thể dễ sửa (nguồn chết — Leak 3) và DNA Voice thiếu 1 signature bắt buộc (folklore cá nhân) — cả hai sửa nhanh (<10 phút), không cần viết lại script.

**Việc cần làm trước khi publish:** áp fix #1 (bắt buộc — accuracy) + fix #2 và #3 (khuyến nghị mạnh — retention + DNA voice) từ mục 7. Fix #4, #5 tuỳ chọn.

---

*Nhắc cuối: bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off TRƯỚC khi export VoiceAI.*
