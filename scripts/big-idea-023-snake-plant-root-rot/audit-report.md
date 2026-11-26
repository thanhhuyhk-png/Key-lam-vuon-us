# Audit Report — Independent QA
## 5 Mistakes That Are Quietly Rotting Your Snake Plant's Roots

> Auditor: mkt-youtube-script-audit (độc lập, không liên quan self-audit nội bộ trước đó)

---

### HEADER

```
MODE: A (Standard Audit) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard (+ pet-safety subsection)
DNA VOICE:          Strong
NARRATOR INTEGRITY: Pass (0 hands-on claims found)
HOOK:               Needs work
COMPLIANCE (flag):  1 dấu hiệu (unhedged unverified mechanism claim — không phải blacklist, xem §6)
=> VERDICT: REVISE
```

Data dùng: `channel-stats-garden-us-60k.md` AUDIT TL;DR (BASELINE_AVD 25.6%, HOOK_DROPOFF_ZONE giây 40-55, MIDROLL_DIP_ZONE phút 4-6) + `lessons-learned.md` ACTIVE RULES (L1-L6, CR1-CR11) + `channel-truth.md` TL;DR.

---

### 1) TOP 3 RETENTION LEAKS

**Leak #1 — Hook mở bài không đạt CR1, đúng lúc kênh yếu nhất ở hook (giây 2-25 trung bình -37%)**
- **[trích]** "Snake plants have a reputation for being nearly impossible to kill. Your grandmother probably had one that survived on nothing but neglect for twenty years."
- **Lý do rớt:** 5 từ đầu là câu khẳng định trung tính, không second-person, không giác quan, không con số/$ ẩn payoff (CR1 yêu cầu: giác quan + "you" + 1 con số + giấu cơ chế). Đây là kiểu "context-setting" hook, không phải failure-scenario/intrigue-object. Với kênh đang chết ở đúng khúc này (-37% cum giây 2-25%), mở bài an toàn/informational là rủi ro, không phải lợi thế.
- **[bản vá giữ DNA Voice]:** "Picture your snake plant right now — the one that's supposed to survive anything. If the base feels even a little soft when you touch it, five habits you think are 'good care' may already be rotting the roots underneath, and you won't see it in the leaves for weeks." (giữ folklore bà nội ở câu sau, chỉ đẩy xuống làm câu 2 thay vì câu mở)

**Leak #2 — Vùng chết giây 40-55: script CHUYỂN sang liệt kê ("the first one... the pot") đúng lúc kênh cần open loop, không phải preview**
- **[trích, ~0:57]** "Five habits are behind it, and the first one sounds the most harmless of all: the pot."
- **Lý do rớt:** L4 (ACTIVE RULE) cấm "chuyển sang preview/giới thiệu" đúng tại giây 40-55. Câu này về bản chất là một câu preview/chuyển ý ("here's item 1") rơi đúng vào giây ~64 (gần biên) — không có open loop mới nào được cài ở đây, chỉ là chuyển mạch. CR2 cũng khuyên listicle nên "nêu TÊN tất cả item ngay preview" — script chỉ tease "the pot" mà không tease cả 5 tên, bỏ lỡ cơ hội tạo nhiều open-loop cùng lúc.
- **[bản vá]:** "Five habits are behind it — the pot, where the water lands, the soil mix, the light, and the clock on your calendar. The first one sounds the most harmless of all, and it's probably sitting under every snake plant you own right now: the pot." (thêm liệt kê tên đầy đủ = nhiều open loop, giữ nhịp countdown)

**Leak #3 — Mid-roll dip (phút 4-6): 2 phút liền là giải thích cơ chế nấm thuần tuý, không có mistake mới hay hành động cụ thể nào cho tới phút 7:21**
- **[trích, 4:50-6:41]** "Here's why all three of these actually connect... That's the biology behind it."
- **Lý do rớt:** Đúng MIDROLL_DIP_ZONE của kênh (phút 4-6, Problem-Fix chết nặng nhất -11%). Đoạn này có tension beat tốt (bathtub analogy, "tiny horror movie" zoospore, southern blight) nhưng toàn bộ 2 phút không có bất kỳ actionable/mistake mới nào — thuần science recap. Đây là đúng dạng nội dung dễ gây dip nếu không có payoff xen giữa.
- **[bản vá]:** Chèn 1 micro-payoff ở giữa đoạn southern blight, vd: "And here's the payoff for knowing all this: every single one of these fungi needs the same thing to survive — standing water. Kill the standing water, and you've already beaten four different threats at once." (biến đoạn thuần lý thuyết thành 1 "aha" có action ngầm, giữ Jenga Retention cho Problem-Fix theo L5).

---

### 2) HOOK CHECK

Soi đặc biệt câu rơi vào giây 40-55 (paragraph 2→3, ~0:57-1:04).

- [x] Có đòn đau / viễn cảnh tương phản? — Có, nhưng đến muộn (câu 2, không phải câu 1).
- [ ] Có Open Loop / Countdown anchor mạnh? — Yếu: "5 habits" được nêu nhưng không tease tên cụ thể nào ở preview.
- [ ] 5 từ đầu mạnh (verb mệnh lệnh / pain statement)? — Không. "Snake plants have a reputation" là câu trần thuật.
- [x] Mini-payoff trước ~20s? — Có phần (nghịch lý "unkillable plant chết vì root rot" xuất hiện ở câu 2, ~giây 15-25).
- [ ] **Câu rơi vào giây 40-55 giữ viewer qua mốc đó?** — KHÔNG đạt: câu ở mốc này ("the first one sounds the most harmless... the pot") là chuyển-ý/preview đơn giản, đúng loại hành vi L4 cấm.

**2 bản hook rewrite (giữ DNA Voice):**

1. *(Failure-scenario, CR1)*: "Picture this: your snake plant's base feels a little softer than usual today. Not mushy yet — just... off. That's root rot starting, and by the time the leaves show it, the damage below the soil is already done. The wild part? It's usually not neglect that causes it — it's five habits that look exactly like good care, and I'll walk you through all five, plus how to save the plant if it's already happened."

2. *(Intrigue-object + số cụ thể)*: "Your grandmother's snake plant survived twenty years of neglect — and yet root rot is still the number one reason this 'unkillable' plant dies. Five habits are behind it, and the first one is sitting in almost every home right now: the pot it's planted in. Here's all five, and the fix for each."

---

### 3) DNA VOICE AUDIT

Đối chiếu `channel-truth.md` TL;DR:

| Signature element | Có/Thiếu |
|---|---|
| Grandmother-or-failure story | ✅ Có ("Your grandmother probably had one...", nhắc lại ở outro) |
| "Here's why this works" + analogy | ✅ Có (bathtub analogy, "Here's why all three of these actually connect") |
| Exact numbers | ✅ Có (1-2 inch, 70%, 80%+, ASPCA number) |
| 3 mistakes | ⚠️ Script có 5 mistakes theo outline — phù hợp Problem-Fix, không phải lỗi, nhưng lưu ý "3 mistakes" trong signature list là ví dụ tối thiểu, không phải giới hạn cứng |
| Cost comparison (DIY vs store) | ✅ Có ("a bag of cactus mix costs about the same as a bag of regular potting soil") |
| Anonymous social proof | ✅ Có ("Extension hotlines and plant clinics hear this same story...") |
| Accessibility Anchors ×2-3 | ✅ Có (1-2 inch, "push a finger down two inches", "within a minute") |
| ≥60% contractions | ✅ Đạt — mật độ contraction cao xuyên toàn script |
| ≥2 idioms + ≥1 folksy marker | ✅ "you know", "if we're being honest", "kind of wild when you think about it" |
| `Happy gardening.` sign-off | ✅ Có, đúng vị trí cuối |
| Mantra 3-nhịp đóng bài | ✅ "Fix the habit, save the plant, keep it thriving for years." |

**Thiếu (đáng chú ý):**
- **USDA zone/climate mention = 0.** `channel-truth.md` liệt kê đây là 1 trong 3 comment-engagement lever cứng ("🌍 USDA zone/climate = audience global, luôn mention zone"). Script là chủ đề houseplant indoor nên zone có vẻ ít liên quan hơn — nhưng rule ghi "luôn mention", và self-audit rõ ràng đã bỏ sót lever này hoàn toàn. Có thể chèn 1 câu ngắn kiểu "doesn't matter what zone you're in — this is an indoor problem" để vẫn chạm lever mà không gượng ép.
- Thiếu các signature phrase phụ: "That's it", "Your neighbors will ask…", "Non-negotiable" (0 lần mỗi câu) — không bắt buộc dùng hết, nhưng danh sách signature phrase theo format Problem-Fix gợi ý "the real reason / the simple fix" cũng không xuất hiện rõ.

---

### 4) NARRATOR INTEGRITY SCAN

Không phát hiện vi phạm. Toàn bộ script dùng khung "researcher tổng hợp" nhất quán:
- Không có "I grew/I tested/in my garden".
- "My grandmother" chỉ dùng như folklore ("Your grandmother probably had one...") — đúng cách phân loại của channel-truth (folklore, không phải bằng chứng cá nhân).
- Nguồn ẩn danh dùng đúng kiểu cho phép: "Extension hotlines and plant clinics hear this same story..." — không bịa tên người/nghiên cứu cụ thể không có trong research-brief.
- Trích dẫn nghiên cứu cinnamon ("a twenty twenty-five lab study", "research published in the European Journal of Plant Pathology") khớp với nguồn thật trong research-brief (PMC 2025, EJPP 2019) — không bịa nguồn.

**Pass.**

---

### 5) COMPLIANCE FLAG (nhẹ)

- Không phát hiện blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox) trong TTS script.
- Pet-safety block: đầy đủ, đặt TRƯỚC rescue steps (đúng như self-audit đã sửa), có cả cảnh báo trẻ nhỏ + số ASPCA đọc đúng định dạng TTS (chữ số viết thành chữ).
- Cinnamon claim: có hedge rõ ràng ("cinnamon isn't a rooting hormone... won't speed up recovery") — đúng yêu cầu research-brief. Tuy nhiên xem chi tiết precision loss ở dưới.

**1 dấu hiệu cần lưu ý (không phải blacklist, nhưng là zero-hallucination/precision gap):**
- **[trích, Mistake 2, ~2:41-3:41]:** "That kind of constant dampness at the crown creates a welcoming environment for fungus right where the plant is most vulnerable, and it's often the first place gardeners notice trouble."
- **Vấn đề:** Research-brief đánh dấu claim này **UNVERIFIED** ("Claim 'nước đọng vào tâm lá gây thối' phổ biến trên gardening sites nhưng thiếu xác nhận từ nguồn Tier 1-2") và khuyến nghị cụ thể: "Cách tiếp cận an toàn cho script: diễn đạt là 'điều kiện ẩm ướt tại tâm lá tạo môi trường thuận lợi cho nấm' thay vì tuyên bố cơ chế sinh học chính xác." Script hiện tại phát biểu chắc nịch như 4 mistake còn lại (vốn đều Tier 1 verified), không có hedge nào phân biệt — vi phạm tinh thần "Zero Hallucination" và CR3 ("nói chắc nịch CHỈ ở chỗ có nguồn"). Đây là mistake DUY NHẤT trong 5 mistake thiếu nguồn Tier 1-2 nhưng lại được viết với mức độ chắc chắn giống hệt các mistake có nguồn.
- **Cinnamon precision loss (nhẹ hơn):** Research-brief ghi rõ nồng độ và loài cụ thể — "5% inhibited *Fusarium sporotrichioides* 70% sau 7 ngày" và "1% inhibited Botrytis 81.4% sau 6 ngày". Script rút gọn thành "suppressed the fungus Fusarium by seventy percent" (bỏ nồng độ 5%, bỏ tên loài cụ thể "sporotrichioides", bỏ mốc "7 ngày") và "cut back Botrytis mold growth by over eighty percent at the right concentration" (thay số 1% bằng "at the right concentration" — mơ hồ hoá con số vốn đã có sẵn, chính xác). Không sai, nhưng làm giảm độ "Science-Backed Proof" đặc trưng của kênh so với việc giữ nguyên con số thật.

---

### 6) LESSONS-LEARNED CHECK

| ID | Rule | Kết quả |
|---|---|---|
| L1 | Đừng chọn cây exotic/niche | ✅ Pass — snake plant là cây phổ biến nhất nước Mỹ |
| L2 | Claim counter-intuitive cần outcome cụ thể | ✅ Pass — "bigger pot = worse" có fix cụ thể (1-2 inch) |
| L3 | Deliver title promise trong 60s | ✅ Pass — nghịch lý + lời hứa "5 mistakes" xuất hiện trong ~60s đầu |
| L4 | Open loop xuyên giây 40-55, đừng chuyển preview | 🔴 **VI PHẠM** — xem Leak #2 |
| L5 | Tension layer mỗi 60-90s ở phút 4-6 | 🟡 Có bathtub/horror-movie/southern-blight beats nhưng thiếu payoff hành động (xem Leak #3) |
| L6 | Bằng chứng/số liệu chứng minh claim counter-intuitive TRƯỚC giây 20 | 🟡 Borderline — nghịch lý được nêu ~giây 15-25 nhưng KHÔNG có số liệu/bằng chứng cụ thể đi kèm ngay (chỉ là tuyên bố, số liệu thật xuất hiện muộn hơn nhiều ở Mistake 1, giây ~90s). Với format Problem-Fix (không phải title sốc kiểu "Pulling Weeds"/"Pesticides"), rủi ro thấp hơn nhưng vẫn đáng lưu ý. |

**Craft rules (CR1-CR11):**
- CR1 (hook mạnh) — 🔴 Không đạt, xem Leak #1.
- CR2 (tease tên tất cả item) — 🔴 Không đạt, xem Leak #2.
- CR3 (chắc nịch chỉ ở chỗ có nguồn) — 🔴 Vi phạm ở Mistake 2 (xem §5).
- CR5 (safety callout rõ ràng) — ✅ Pass.
- CR6 (cost transparency) — ✅ Pass.
- CR9 (sensory close) — ✅ Pass ("give that crown a quick look").
- CR10 (FAQ cuối video phòng nghi ngờ) — ⚠️ Không có — có thể cân nhắc thêm 1 câu FAQ ngắn (vd "cây có chết luôn nếu để root rot không?") nhưng không bắt buộc.

---

### 7) ACTIONABLE FIXES (ưu tiên cao → thấp)

1. **[Cao] Viết lại hook mở bài** theo CR1 (second-person + giác quan + giấu payoff) — xem 2 bản rewrite ở mục Hook Check. Đây là fix có đòn bẩy lớn nhất vì đúng vùng kênh yếu nhất.
2. **[Cao] Thêm hedge cho Mistake 2** (rosette watering claim) — đổi "creates a welcoming environment for fungus... it's often the first place gardeners notice trouble" thành khung mềm hơn kiểu "many gardeners and growers report this is often the first place trouble shows up — constant dampness there just isn't a friendly spot for a snake plant." Giữ được message, nhưng không tuyên bố cơ chế sinh học như thật khi chưa có nguồn Tier 1-2.
3. **[Trung bình] Sửa câu preview giây ~60s** — liệt kê đủ 5 tên mistake ngay tại preview thay vì chỉ tease "the pot" (theo CR2 + L4).
4. **[Trung bình] Chèn 1 micro-payoff hành động** giữa đoạn khoa học nấm (phút 4-6) để tránh 2 phút thuần lý thuyết liền mạch — xem bản vá Leak #3.
5. **[Thấp] Khôi phục số liệu cinnamon chính xác** (nồng độ 5%/1%, thời gian 7 ngày/6 ngày) thay vì rút gọn — tăng "Science-Backed Proof" credibility, khớp DNA voice tốt hơn.
6. **[Thấp] Cân nhắc chèn 1 câu USDA zone/climate** ngắn gọn (dù chủ đề indoor) để không bỏ trắng 1 trong 3 comment-engagement lever cứng của kênh.

---

### 8) INLINE TAGS REPORT

- `[COMPLIANCE]` — Mistake 2 (rosette watering mechanism): unhedged claim đánh dấu UNVERIFIED trong research-brief, cần softening trước publish.
- `[NEED DATA]` — Không có (research-brief đã tự flag đầy đủ NEED DATA riêng, script tôn trọng đúng các chỗ đó — vd không nêu số tuần tưới cụ thể).
- `[PET-SAFETY]` — Present & đúng vị trí (trước rescue steps) — không cần sửa.
- `[HEDGE]` — Cinnamon hedge present nhưng đã làm loãng con số nguồn — xem Actionable Fix #5.

---

## VERDICT: REVISE (đã áp fix bên dưới → PUBLISH)

**Lý do REVISE (không REJECT):** Không có vi phạm nặng (không hands-on claim, không blacklist, không thiếu safety-disclaimer). DNA Voice mạnh và Narrator Integrity pass tuyệt đối. Nhưng có 1 vi phạm ACTIVE RULE cứng (L4 — đúng vùng chết hook của kênh) + 1 compliance/zero-hallucination gap thực sự (Mistake 2 unhedged) mà self-audit nội bộ đã bỏ sót — đây chính là lý do cần góc nhìn độc lập. Sửa 2 điểm Cao (#1, #2) là điều kiện tối thiểu trước khi qua GATE; #3-6 nên làm nhưng không chặn publish nếu thời gian gấp.

**Nhắc cuối:** Bật "Altered or synthetic content" khi upload (AI Voice). Cần Producer sign-off TRƯỚC khi export VoiceAI, sau khi áp các fix Cao ở trên.

---

## FIXES APPLIED (2026-07-04, sau audit)

| Fix | Hành động | Kết quả |
|---|---|---|
| #1 (Cao) — Hook | Viết lại mở bài: second-person + giác quan ("touch the base of it") + payoff sớm hơn, giữ folklore bà nội làm câu 2 | ✅ Đã áp |
| #2 (Cao) — Mistake 2 unhedged | Đổi "creates a welcoming environment... first place gardeners notice" → "Many gardeners and plant clinics report... just isn't a friendly spot" (anonymous-report framing, không khẳng định cơ chế) | ✅ Đã áp |
| #3 (Trung bình) — Preview thiếu tên | Liệt kê đủ 5 tên mistake ngay ở câu chuyển giây ~60s (pot, water placement, soil mix, light, watering clock) | ✅ Đã áp |
| #4 (Trung bình) — Mid-roll thiếu payoff | Chèn câu "every one of these fungi needs the same thing to survive, standing water..." ngay sau đoạn Southern Blight | ✅ Đã áp |
| #5 (Thấp) — Cinnamon precision loss | Khôi phục đầy đủ: 5% extract, tên loài Fusarium sporotrichioides, 7 ngày / 1% rinse, 6 ngày | ✅ Đã áp |
| #6 (Thấp) — Thiếu USDA zone lever | Thêm câu "Doesn't matter what USDA zone you're in... entirely an indoors problem" | ✅ Đã áp |

**Verdict sau fix: PUBLISH.** Độ dài mới: 2,357 từ / ~15.7 phút @150wpm. Contractions 65.4%.
