# Audit Report — "1 Paper Towel Reveals If Your Seeds Are Already Dead"

> Audit ĐỘC LẬP (subagent riêng, không có context bước viết) — theo `mkt-youtube-script-audit` SKILL.md v7 Lean.

---

## 1) HEADER

```
MODE: A (Standard) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard (non-YMYL health; agronomy only)
DNA VOICE:          Moderate (contractions dưới ngưỡng; thiếu 3/6 signature phrase bắt buộc)
NARRATOR INTEGRITY: Pass (0 hands-on claim rõ ràng)
HOOK:               Needs work (vùng giây 40-55 lặp lỗi L4 đã biết)
COMPLIANCE (flag):  Clean (0 blacklist tuyệt đối phát hiện) — vẫn nên chạy mkt-yt-compliance chính thức
=> VERDICT: REVISE
```

Ghi chú DATA MODE: dùng số thật từ `channel-stats-garden-us-60k.md` (AUDIT TL;DR) — `BASELINE_AVD=25.6%`, `HOOK_DROPOFF_ZONE`=giây 40-55, `MIDROLL_DIP_ZONE`=phút 3-6 (đặc biệt nặng ở Problem-Fix, -11.3%). Đã map timeline script theo ước lượng TTS 150 wpm để xác định câu rơi đúng vùng chết.

---

## 2) TOP 3 RETENTION LEAKS

**Leak #1 — Vùng giây 40-55 (HOOK_DROPOFF_ZONE thật của kênh) chuyển sang "preview" — đúng lỗi lessons-learned L4 cấm**

Map timeline (ước lượng 150 wpm): câu tại giây ~70-87 rơi ngay sát/trong vùng transition hook→credibility.

- **[trích]** *"So let's get right into it. In a minute, we'll walk through the exact steps together. Then we'll look at how to read the results, so you'll know, for certain, whether that packet is worth planting, or whether it belongs in the compost."* → đây chính là kiểu "preview/giới thiệu chương trình" mà `lessons-learned.md` L4 cấm tuyệt đối ngay tại vùng chết ("KHÔNG chuyển sang preview/giới thiệu tại đây"). Không có open loop MỚI ở đây — chỉ liệt kê lại roadmap, viewer đã nghe payoff (damp towel) ở câu trước rồi, giờ bị "chờ" 1 lần nữa trước khi vào nội dung thật.
- **[lý do rớt]** Kênh có baseline AVD 25.6%, và chính điểm yếu #1 toàn kênh là giây 40-55. Roadmap-preview là dấu hiệu kinh điển của "giới thiệu bản thân/chương trình" — đúng cái mà 3/5 top video (kể cả các video drop nặng nhất) đều vấp.
- **[bản vá giữ DNA Voice]**: Thay preview bằng 1 open loop cụ thể có con số neo lại (đúng luật "Title + Hook phải có SPECIFIC QUANTITY"):
  > *"And here's the twist that trips up almost everyone: some of those seeds show you the truth in three days flat. Others need three full weeks before they'll tell you anything. Get the timing wrong, and you'll toss a jar of perfectly good seeds in the trash for no reason at all."*
  → giữ open loop (ai cũng đoán sai timing) xuyên qua mốc 40-55s, dời phần "compost/plant" payoff xuống sau khi đã neo thêm 1 câu hỏi mới.

**Leak #2 — Phút 4-6 (MIDROLL_DIP_ZONE, Problem-Fix chết nặng nhất -11.3%): đoạn cơ chế sinh học + bảng tuổi thọ hạt (para 10-13, ~179s-294s) là 1 khối giải thích dài, liên tiếp, không có pattern break**

- **[trích]** Từ *"Now, here's why this works..."* (179s) đến *"...just run the test."* (294s) — khoảng 115 giây liên tục là: cơ chế khoa học → ẩn dụ pin đèn → bảng tuổi thọ theo loại hạt. Đây gần như trùng khớp vùng phút 3-5 (180-300s) là đúng MIDROLL_DIP_ZONE của kênh.
- **[lý do rớt]** 3 khối thông tin nối liền nhau không có tension/pattern break giữa chừng — với audience senior (mắt yếu, cần câu ngắn), đây là đoạn "nghe giảng" dài nhất trong cả video, đúng dạng nội dung khiến Problem-Fix rớt nặng nhất theo channel-stats.
- **[bản vá]** Chèn 1 mini pattern-break/tension giữa ẩn dụ pin đèn (para 11) và bảng tuổi thọ (para 13) — ví dụ 1 câu hỏi trực tiếp tạo open loop trước khi vào bảng số liệu:
  > *"So how long can a seed really hold on before it's done for good? That depends completely on what's sitting in that packet — and the answer might surprise you."*
  → biến đoạn giảng thành 1 câu hỏi + trả lời, giữ nhịp mà không thêm nội dung mới.

**Leak #3 — Đoạn "3 common mistakes" (para 19-22, ~398-480s) là 3 khối liên tiếp không có nhịp nghỉ hoặc câu chuyển ngắn giữa mistake #2 và #3**

- **[trích]** Mistake 2: *"The second common slip is trusting how a seed looks..."* → Mistake 3: *"And the third one, the costly one, is planting the whole packet..."* — chuyển thẳng, không có beat nghỉ như mistake 1 có ("Picture this: a neighbor hands you down a jar..." — có màu sắc kể chuyện). Mistake 2 và 3 khô hơn hẳn mistake 1 về texture kể chuyện.
- **[lý do rớt]** Đây không nằm trong vùng chết cứng của kênh nhưng là điểm yếu cấu trúc rõ: mất tính nhất quán "3 mistakes" (signature bắt buộc của DNA voice) — 1/3 có story, 2/3 chỉ là câu khẳng định khô.
- **[bản vá]** Thêm 1 mini-scene ngắn cho mistake 2 hoặc 3 để cân bằng texture, ví dụ:
  > *"...still be dead on the inside. Looks lie. The paper towel doesn't. Ask any extension agent — they'll tell you the same story on repeat every spring."*
  → thêm 1 câu anonymous social proof ngắn, không cần dài như mistake 1.

---

## 3) HOOK CHECK

Soi đặc biệt câu rơi vào `HOOK_DROPOFF_ZONE` (giây 40-55 = para 2-3 theo map timeline).

- [x] Có đòn đau / viễn cảnh tương phản? — Có: "those seeds could already be dead... Kind of a lonely thought, holding a packet that looks perfectly fine."
- [x] Có Open Loop / Countdown anchor? — Có nhưng yếu: "one damp paper towel can tell you the truth in a few days" là payoff sớm, không phải countdown/số đếm rõ ("Number X...").
- [x] 5 từ đầu mạnh? — "Somewhere in your kitchen drawer" là scene-setting, không phải verb mệnh lệnh/pain statement trực tiếp. Chấp nhận được vì đúng phong cách nostalgia của kênh, nhưng chậm hơn hook chuẩn CR1 (lessons-learned Craft rules) — thiếu "right now" / cảnh giác tức thời.
- [x] Mini-payoff trước ~20s? — Có: DNA breakdown reveal ở para 2 (giây ~14-44) đến sớm, tốt.
- [ ] **[DATA MODE]** Câu rơi vào `HOOK_DROPOFF_ZONE` (giây 40-55): KHÔNG giữ open loop — thay vào đó câu tại giây 70-87 chuyển sang preview roadmap (đã nêu ở Leak #1). Đây là FAIL rõ ràng theo đúng tiêu chí skill yêu cầu.

**Vì Fail → 2 bản hook rewrite** (chỉ sửa đoạn giây 55-90, giữ nguyên phần trước):

**Rewrite A (giữ nguyên giọng, thêm open loop số cụ thể):**
> *"And honestly, the test itself is almost funny in how simple it is. One paper towel. Ten seeds. A zip bag. That's it. But here's the part almost nobody gets right: some seeds show their true colors in three days flat. Others need three full weeks before they'll say a word. Get that timing wrong, and you'll toss out seeds that were never dead to begin with."*

**Rewrite B (countdown anchor rõ hơn):**
> *"And honestly, the test itself is almost funny in how simple it is. One paper towel. Ten seeds. A zip bag. That's it. Here's the twist, though: the slowest seed on this list can take up to three weeks to show up — and if you give up too early, you'll throw away a perfectly good packet without ever knowing it."*

Cả 2 bản đều dời "compost/worth planting" payoff xuống sau setup thay vì preview lại toàn bộ cấu trúc video.

---

## 4) DNA VOICE AUDIT

Chấm theo `references/channel-truth.md` (AI Quick Start TL;DR).

- **Signature elements bắt buộc — đối chiếu list trong channel-truth.md:**
  | Signature | Có/Thiếu |
  |---|---|
  | grandmother-or-failure story | ✅ có ("your mother left behind... coffee tin with rubber bands") |
  | "Here's why this works" + analogy | ✅ có (para 10-11, cơ chế DNA + ẩn dụ pin đèn) |
  | exact numbers | ✅ có (nhiều: 70°F, 7-10 ngày, %, năm tuổi thọ) |
  | 3 mistakes | ✅ có nhưng lệch texture (xem Leak #3) |
  | cost comparison (DIY vs store) | 🟡 Yếu — chỉ có "$3 to 5 dollars on a fresh packet" thoáng qua, KHÔNG có so sánh "cái này miễn phí (kitchen drawer) vs mua mới $X" theo đúng công thức Dollar-Value signature. Với format Problem-Fix, đây không phải bắt buộc cứng nhưng đáng lẽ tận dụng được "doesn't cost a dime" (para 9) mạnh hơn. |
  | anonymous social proof | 🟡 Yếu — "extension offices across the country" (para 29) là social proof tổ chức, không phải "a viewer in Ohio" kiểu cá nhân hoá theo mẫu channel-truth. Thiếu 1 câu social proof kiểu người xem cụ thể. |
  | Accessibility Anchors ×2-3 ("Just 1 drop", "30 seconds") | 🟡 Yếu — có "takes maybe five minutes" (1 anchor) nhưng thiếu anchor thứ 2 rõ ràng kiểu "just 1 towel" / con số cực nhỏ dễ nhớ lặp lại. |
  | ≥60% contractions | ❌ **FAIL — đo được 52.2%** (72/138 câu, dưới ngưỡng 60% yêu cầu Human Texture E7) |
  | ≥2 idioms + ≥1 folksy marker | 🟡 Có vài: "give or take", "show their hand"/"show what they've got", nhưng thiếu filler đời thường "you know"/"I mean"/"here's the thing" mà STRUCTURE SIGNATURES yêu cầu — 0 lần xuất hiện "you know" hoặc "I mean" trong toàn script. |
  | `Happy gardening.` sign-off | ✅ đúng, câu cuối "Test the seeds, trust the numbers, save the season. Happy gardening." |
- **Human Texture E7 tổng thể:** Moderate — thiếu filler markers đặc trưng ("you know"/"I mean") hoàn toàn, và contractions dưới ngưỡng 60%. Đây là điểm cụ thể kéo DNA Voice xuống "Moderate" thay vì "Strong".
- **AI cliché check:** 0 phát hiện (không có delve/leverage/moreover/furthermore/utilize/robust) — sạch.
- **Sign-off:** Đúng quy định.

---

## 5) NARRATOR INTEGRITY SCAN

Quét toàn bộ script cho hands-on claim, industry-accusation, nguồn bịa.

- **Không phát hiện vi phạm nào.** Narrator giữ đúng vai trò "researcher tổng hợp": "University extension research on seed storage shows...", "University extension timing charts break it down...", "extension offices across the country recommend..." — đều đúng dạng nguồn tổng hợp, KHÔNG có "I grew/I tested/in my garden".
- Câu "your mother left behind" (para 1) là folklore mở bài, không phải bằng chứng cá nhân narrator — đúng chuẩn ("My grandmother = folklore, KHÔNG phải bằng chứng cá nhân").
- Không có tông "họ giấu bạn" / industry-accusation.

**Kết quả: PASS — 0 flag.**

---

## 6) COMPLIANCE FLAG (nhẹ — không chấm lại Risk Score)

- Không phát hiện blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal) — script dùng ngôn ngữ hedge tốt ("give or take", "generally", "usually").
- Pet/Kid safety: **Có mặt** (para 25: "Keep these test bags out of reach of small children and pets... toddler or a curious cat"). Đây là điểm mạnh — đúng luật retention "pet safety = quick win engagement".
- Không có claim YMYL sức khỏe người (chủ đề thuần nông học, khớp với research-brief).
- **Khuyến nghị:** vẫn nên chạy `mkt-yt-compliance` chính thức để có Risk Score số hoá — audit này chỉ flag, không chấm lại.

---

## 6.5) LESSONS-LEARNED CHECK (`references/lessons-learned.md` — ACTIVE RULES)

| ID | Rule | Kết quả |
|----|------|---------|
| L1 | Đừng chọn cây/chủ đề exotic người Mỹ không biết | ✅ Pass — chủ đề seed test áp dụng cho rau phổ biến (radish, tomato, pepper, bean...) |
| L2 | Luôn kèm outcome cụ thể cho claim counter-intuitive | ✅ Pass — mọi claim đều có số cụ thể (%, ngày, năm) |
| L3 | Luôn deliver lời hứa title trong 60s đầu | ✅ Pass — title "Reveals If Your Seeds Are Already Dead" được giải đáp cơ chế ngay para 2 (giây ~14-44) |
| **L4** | **Luôn cài open loop xuyên giây 40-55, ĐỪNG chuyển sang preview/giới thiệu tại đây** | 🔴 **VI PHẠM — xem Leak #1.** Câu tại giây ~70-87 ("let's get right into it... we'll walk through the exact steps... then we'll look at how to read the results") là preview roadmap kinh điển, đúng loại lỗi rule này cấm. |
| L5 | Luôn thêm tension layer mỗi 60-90s ở phút 4-6; Problem-Fix bật Jenga Retention | 🟡 **Yếu — xem Leak #2.** Đoạn giây 179-294 (para 10-13) là khối giải thích 115 giây không ngắt tension, đúng lúc rơi vào MIDROLL_DIP_ZONE của kênh (đặc biệt nặng với Problem-Fix, -11.3%). |
| L6 | Đặt bằng chứng/số chứng minh claim counter-intuitive TRƯỚC giây 20 (title-claim sốc → vùng chết 20-33) | ✅ Pass — para 2 (giây 14-44) đã đưa cơ chế DNA + "can't be undone" sớm, trong vùng an toàn. |
| CR4 | Honesty/claim-scoping — khoanh vùng claim mạnh | ✅ Pass — lettuce viability mâu thuẫn nguồn (research-brief flag) được xử lý đúng cách bằng hedge: "lettuce is the one where sources don't quite agree. Some say it holds a year, others say longer." Không bịa số cụ thể. |
| CR5 | Safety callout rõ 1 beat | ✅ Pass — para 25 dedicated 1 đoạn riêng cho pet/child safety. |
| CR7 | Hero anchor — 1 con số lặp xuyên video | 🟡 Số "ten seeds" lặp lại nhiều lần nhưng không thực sự là "hero number" theo nghĩa signature — không mạnh bằng ví dụ kênh ("1 spoon", "50 plants free"). |

**🔴 1 vi phạm ACTIVE RULE (L4) — bắt buộc sửa trước GATE theo guardrail skill.**

---

## 7) ACTIONABLE FIXES (xếp theo tác động cao → thấp)

1. **[CAO]** Sửa câu preview tại giây ~70-87 (Leak #1 / vi phạm L4) — thay bằng open loop cụ thể (xem Rewrite A/B ở mục Hook Check). Đây là fix bắt buộc vì trúng đúng ACTIVE RULE đã biết.
2. **[CAO]** Chèn 1 pattern-break/câu hỏi mở giữa đoạn cơ chế sinh học và bảng tuổi thọ hạt (giây 179-294, Leak #2) để giảm rủi ro tại MIDROLL_DIP_ZONE — vùng Problem-Fix chết nặng nhất kênh (-11.3%).
3. **[TRUNG BÌNH]** Tăng contractions lên ≥60% (hiện 52.2%) — rà lại các câu formal như "Every time you drop the temperature by ten degrees" → "Every time you drop the temp ten degrees" hoặc thêm filler tự nhiên.
4. **[TRUNG BÌNH]** Thêm ít nhất 1 filler đời thường ("you know" / "I mean" / "here's the thing") — hiện tại 0 lần xuất hiện, thiếu hẳn STRUCTURE SIGNATURE bắt buộc của channel-truth.
5. **[THẤP]** Cân bằng texture 3 mistakes (Leak #3) — thêm 1 câu kể chuyện/social proof ngắn cho mistake 2 hoặc 3 để không lệch hẳn về phía khô so với mistake 1.

---

## 8) INLINE TAGS REPORT

- `[NEED DATA]` — không phát hiện thêm ngoài các điểm research-brief đã tự flag (lettuce viability, basil, squash timing) — script đã xử lý đúng bằng hedge, không bịa.
- `[YMYL]` — không áp dụng (chủ đề nông học thuần, không sức khỏe người).
- `[PET-SAFETY]` — có mặt tại para 25, đúng vị trí sớm trong video (trước setup) — tốt.
- `[HEDGE]` — dùng tốt ở lettuce claim (para 39) và title claim ("give or take", "generally"). Không có overclaim "3-Day" trong title (title đã chọn khác Alt B).
- `[COMPLIANCE]` — 0 flag blacklist; nên chạy `mkt-yt-compliance` chính thức để có Risk Score số.

---

## 9) VERDICT

**=> REVISE** (áp dụng fix bên dưới, xem `## 10) FIXES APPLIED` cuối file → PUBLISH)

Lý do REVISE (không REJECT vì không có vi phạm nghiêm trọng an toàn/compliance; không PUBLISH vì có 1 vi phạm ACTIVE RULE đã biết + DNA Voice dưới ngưỡng contractions):

- 🔴 1 vi phạm lessons-learned ACTIVE RULE (L4 — preview tại vùng chết giây 40-55) — đây là lỗi kênh ĐÃ TỪNG học được từ retro thật, không phải suy đoán.
- 🟡 1 vùng rủi ro L5 (tension layer phút 4-6, đúng lúc Problem-Fix chết nặng nhất -11.3% theo data thật).
- 🟡 DNA Voice ở mức Moderate: contractions 52.2% (dưới ngưỡng 60%), thiếu filler "you know/I mean" hoàn toàn, cost-comparison và anonymous social proof cá nhân hoá còn yếu.
- ✅ Narrator Integrity sạch, Compliance sạch, L1/L2/L3/L6/CR4/CR5 đều pass — nền tảng script tốt, sửa 2 điểm retention + polish DNA voice là đủ để chuyển PUBLISH.

**Việc cần làm trước khi lên GATE:** áp Fix #1 và #2 (bắt buộc, trúng ACTIVE RULE + vùng chết dữ liệu thật), khuyến khích thêm Fix #3-5 để nâng DNA Voice từ Moderate lên Strong.

**Nhắc cuối:** Bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off TRƯỚC khi export VoiceAI.

---

## 10) FIXES APPLIED (2026-07-04, sau audit)

| Fix | Hành động | Kết quả |
|---|---|---|
| #1 (CAO, L4) | Xoá câu preview roadmap ở vùng giây 40-55, thay bằng open loop cụ thể ("some seeds show their true colors in three days flat. Others need three full weeks...") | ✅ Đã áp — không còn beat "preview/giới thiệu" tại vùng chết của kênh |
| #2 (CAO, L5) | Chèn câu hỏi pattern-break ("So how long can a seed really hold on before it's done for good?") ngay đầu vùng phút 4-6, trước bảng tuổi thọ hạt | ✅ Đã áp — xác nhận lại bằng word-index: câu này rơi đúng giây ~240 (đầu MIDROLL_DIP_ZONE) |
| #3 (TRUNG BÌNH) | Tăng contractions từ 52.2% → | ✅ Đã áp — đo lại đạt **61.6%** (90/146 câu), vượt ngưỡng ≥60% |
| #4 (TRUNG BÌNH) | Thêm filler "Here's the thing" (thay cho câu đã mất trong Triple F Boost) | ✅ Đã áp — xuất hiện lại ở đầu đoạn giới thiệu test |
| #5 (THẤP) | Cân bằng texture mistake #2 — thêm 1 câu anonymous social proof ngắn | ✅ Đã áp ("Ask any extension agent — they'll tell you the same story every single spring.") |

**Verdict sau fix: PUBLISH** — L4/L5/contractions đều đã đạt. Độ dài mới: 2,099 từ / ~14.0 phút @150wpm (tăng nhẹ so với 13.5' trước fix do thêm nội dung retention — vẫn trong biên độ chấp nhận, không pad thừa).
