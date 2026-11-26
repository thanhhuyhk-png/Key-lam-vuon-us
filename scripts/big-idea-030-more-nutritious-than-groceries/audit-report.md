# Audit Report — "You're Pulling $6 Salad: 7 Yard Weeds That Beat Store Greens"

> Independent QA — mkt-youtube-script-audit (V7 Lean). Chạy như góc nhìn thứ 2, không có context viết script/spine.
> Word count TTS: **1,459** (target 1,200–1,500 ✅) · Pace mapping dùng chung convention với retention-spine (~2.5 words/sec, khớp idx↔giây do spine tự quy đổi).

---

## 1) HEADER

```
MODE: C (YMYL / Foraging) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: YMYL-Foraging (Listicle 7-item)
DNA VOICE:          Moderate
NARRATOR INTEGRITY: Pass (0 flags)
HOOK:               Needs work
COMPLIANCE (flag):  1 dấu hiệu (plantain BP caution missing) → chạy mkt-yt-compliance để chấm chính thức
=> VERDICT: REVISE
```

---

## 2) TOP 3 RETENTION LEAKS

**Leak 1 — Central claim gets ZERO hard number until ~word 163–187 (~giây 65–75), missing the spine's own <60s delivery-lock and blowing past L6's giây 20–33 window.** 🔴
- **[trích]** *"You just paid six dollars for a bag of greens... something growing free in your yard right now beats what's in that bag... by number five, you'll see one that holds more of a nutrient we normally pay for in fish oil pills."* (idx 0–58, giây 0–23) → then a 100+ word safety-note/preview stretch → the **first actual number** in the whole video doesn't land until *"one hundred three milligrams of calcium and more than a hundred percent of your daily vitamin A"* (idx ~170–187, giây ~68–75).
- **Lý do viewer rớt:** retention-spine.md tự đặt DELIVERY-LOCK target "con số cụ thể đầu tiên (vit A 112% DV) ở idx ~150 (giây 60)" — script thực tế trễ hơn ~10-15s so với chính target đó, và trễ xa hơn nữa so với L6 (bắt buộc bằng chứng/con số trước giây 20–33). Đây đúng pattern đã giết "Pulling Weeds" (-29.5%@20-30s, AVD 18.8%) và "STOP Pesticides" (-20.8%@22-33s) trong lessons-learned.md — claim ngược đời ("cỏ dại thắng rau chợ") được NÊU nhưng không được CHỨNG MINH bằng số trong cửa sổ sống còn.
- **Bản vá (giữ DNA Voice):** Kéo 1 con số ngắn lên trước giây 20 — vd chèn ngay sau câu mở: *"Here's the thing: one of these seven has more vitamin C than three whole oranges — and it's growing in your lawn right now."* (dùng số violet đã có, không cần thêm nghiên cứu) rồi mới vào safety note + preview.

**Leak 2 — Safety disclaimer bleeds into the channel's worst zone (giây 40–55).** 🟡
- **[trích]** *"One safety note first: a couple of these plants have look-alikes, so always be completely sure of a plant's identification — check a local extension office or field guide — before you pick or eat anything from the yard."* (idx 79–116, ≈ giây 32–46) chạy thẳng vào đúng `HOOK_DROPOFF_ZONE` (giây 40–55) của kênh, và phần theo sau trong chính zone đó — *"There's a reason your yard keeps outperforming the produce aisle, and we'll show you why by the end"* (idx 117–134, giây ~47–54) — chỉ là re-tease chung chung, không phải payoff mới.
- **Lý do viewer rớt:** disclaimer bắt buộc (Mode C) nhưng đúng lúc rơi vào cửa sổ tử vong nhất kênh, đọc như một khoảng dừng hành chính đúng lúc L4 yêu cầu open loop sống, không phải "giới thiệu/preview".
- **Bản vá:** Rút disclaimer còn 1 câu gọn (*"One quick note: always be sure of a plant's ID before you pick anything — more on that as we go."*), dồn chi tiết misID xuống item cụ thể (đã có sẵn ở #4 violet), để giây 40–55 dành trọn cho open-loop/tease mạnh hơn.

**Leak 3 — "Wall of caveats" ngay trước phần chốt (idx 1214–1319, ≈ giây 8:05–8:45), ngay sau đỉnh cảm xúc của item Plantain (Story Bank).** 🟡
- **[trích]** *"Before you put this together: only ever eat what you can identify with complete certainty, never pick from a lawn that's been sprayed, and if you're trying any of these for the first time, start with a small amount to check for personal sensitivity. If you've got pets or grandkids around, keep an eye on them near anything new... Rinse everything well and keep your harvest up on the counter..."* — 6 cảnh báo dồn liên tiếp trong 1 đoạn (105 từ), ngay sau climax lịch sử "Englishman's Foot".
- **Lý do viewer rớt:** năng lượng vừa lên đỉnh (scene lịch sử) rồi rơi thẳng vào một khối liability-disclaimer dày đặc trước khi tới payoff cuối (salad $6) — risk giảm nhịp đúng đoạn cuối dễ rời kênh nhất.
- **Bản vá:** Tách làm 2: 1 câu cảnh báo cốt lõi ngay đây (identification + no-spray), dời phần pet/grandkid + rinse/storage xuống ghép chung với đoạn "put it together" salad cuối (đã có sẵn khung "keep your harvest... out of paw and grandkid reach" — hợp lý nếu đặt cùng lúc mô tả salad, không phải trước nó).

---

## 3) HOOK CHECK (giây 0–30 phổ quát + soi riêng `HOOK_DROPOFF_ZONE` giây 40-55)

- [x] Đòn đau/viễn cảnh tương phản — "$6 bag" vs "free in your yard" ✓
- [x] Open Loop/Countdown anchor — "by number five... beats fish oil pills" ✓ mạnh
- [~] 5 từ đầu mạnh — "You just paid six dollars" là pain-statement khá, không phải verb mệnh lệnh, chấp nhận được
- [ ] **Mini-payoff trước ~20s — FAIL.** Không có số/dữ kiện cụ thể nào trước giây 20; chỉ có framing + open loop (xem Leak 1)
- [ ] **DATA MODE — câu rơi vào `HOOK_DROPOFF_ZONE` (giây 40-55) — yếu.** Đó là đuôi safety-note + 1 câu re-tease chung chung, không phải micro-payoff mới (xem Leak 2)

**→ HOOK: Needs work.** 2 bản rewrite (giữ DNA Voice, chèn 1 số sớm):

1. *"You just paid six dollars for a bag of greens at the grocery store. Here's the thing: one weed in your yard right now has more vitamin C than three whole oranges — and it's just one of seven that beat what's in that bag. By number five, you'll see one that holds more of a nutrient we normally pay for in fish oil pills."*
2. *"Six dollars. That's what you paid for that bag of greens — and something growing free by your back step already beats it. Not one weed. Seven. One of them out-vitamins an orange three times over. And by number five, we're talking about the one that goes head-to-head with fish oil."*

---

## 4) DNA VOICE AUDIT

Chấm theo `channel-truth.md` TL;DR + `brand-voice-dna.md`.

**Signature elements:**
| Element | Có/Thiếu |
|---|---|
| Grandmother-or-failure story | Thiếu (chấp nhận được — bảng "SIGNATURE PHRASES THEO FORMAT" cho Listicle không yêu cầu; chỉ nêu "Here's the thing / open-loop / That's it / mantra") |
| "Here's why this works" + analogy | Có cụm "Here's why..." ×2 (đúng tần suất 2-3 lần) nhưng **không kèm analogy đơn giản nào** trong cả script — mỗi lần chỉ dẫn thẳng vào số liệu, thiếu phép so sánh dễ hình dung |
| Exact numbers | Có, dày đặc và chính xác so với research-brief ✓ |
| 3 mistakes | N/A cho Listicle (không bắt buộc) |
| Cost comparison (DIY vs store) | Có, "$6 bag" là hero anchor xuyên suốt ✓ mạnh |
| **Anonymous social proof** | **THIẾU HOÀN TOÀN** — không có "a viewer in [state]" / "master gardeners often report" nào trong cả script, dù đây là signature bắt buộc trong TL;DR |
| Accessibility Anchors ×2-3 | Có 2 ("thirty seconds to spot", "All you need is a salad bowl") — đạt ngưỡng dưới |
| Sign-off | "Happy gardening." ✓ |

**Human Texture E7:** contractions dày đặc (you're/it's/here's/that's/don't/you'll...) ước lượng đạt ≥60%; idioms: "dirt-cheap", "rain or shine" (≥2 ✓); folksy marker: "folks"/"most folks" (≥1 ✓). Không phát hiện AI cliché nào (không có delve/leverage/moreover/furthermore...). ✓

**→ DNA VOICE: Moderate** — texture tốt, nhưng thiếu 1 signature bắt buộc (anonymous social proof) và "Here's why" không kèm analogy như công thức yêu cầu.

**Gợi ý vá (giữ giọng, không thêm claim mới):** chèn 1 câu social-proof ẩn danh ở đoạn kết hoặc sau item mạnh nhất, vd sau Purslane: *"Master gardeners who've caught onto this one already treat it as a free supplement, not a weed."* (khung chung, không cần nguồn cụ thể vì là social-proof ẩn danh theo đúng định dạng brand).

---

## 4.5) STORYTELLING CRAFT CHECK

- [x] **Micro-Bridge ở mọi transition** — tất cả 6 chuyển đoạn giữa item đều dùng công thức đóng-ý-cũ + tease-mới ("Dandelion's just the warm-up act...", "Purslane closes out the fish story. But the next one closes out something else...") — **KHÔNG có "trạm dừng" kiểu "Number two. [Tên]."** ✓ điểm mạnh rõ rệt
- [x] **≥1-2 scene/script** — Story Bank "Englishman's Foot" (Plantain) dùng đúng, có nguồn (Alice Morse Earle, *Old Time Gardens* 1901, trong research-brief) ✓
- [x] **Mid-video re-hook tại MIDROLL_DIP_ZONE (phút 4-6)** — Purslane (idx 604–736 ≈ giây 4:02–4:54) đóng đúng Loop #1 ngay trong vùng nguy hiểm nhất kênh — thiết kế tốt, thực thi đúng ✓
- [ ] **Per-Item Intrigue — 🟡 chỉ 1/7 item có pre-name intrigue, thiếu ở item CUỐI (bắt buộc).** Item #1 Dandelion mở đúng công thức ("the plant that's already outperforming a produce-aisle regular — the cheerful yellow dandelion"), nhưng item #7 Plantain (CUỐI, bắt buộc theo rule 7) mở bằng cách nêu tên ngay: *"This is broadleaf plantain, not the banana, the flat, ribbed weed..."* — chưa có tò mò/khác biệt đặt TRƯỚC tên. 5 item giữa (#2-6) cũng đều nêu tên trước, chỉ đạt 1/7 thay vì yêu cầu ≥3-4.
  - Gợi ý: đổi câu mở Plantain thành *"Every single day, you're stepping over one of the strangest hitchhikers in American history. This is broadleaf plantain..."*
- [x] **Climax Beat** — Purslane được dựng cao độ có chủ đích ("everything up to this point was just setting the table, because number five is the one I promised you...") + đoạn dài hơn các item khác (132 từ vs ~80-95 của item đầu) ✓
- [x] **Forward-Visual Close + Identity CTA** — "By this weekend, you could be looking at your yard as a grocery aisle instead of a to-do list" → "If you're the kind of gardener who'd rather harvest than spray, you belong here" → comment hook geo-specific → "Happy gardening." ✓ đúng thứ tự công thức

**Bổ sung CR-rules (competitor teardown, ADOPT nếu thiếu = 🟡):**
- **CR2 thiếu** — Preview (idx 59-134) không nêu TÊN bất kỳ item nào trong 7 item, chỉ tease số lượng + item #5. Rule khuyến nghị liệt tên ngay trong preview để mở nhiều open-loop cùng lúc — hiện tại chỉ có 1 loop chính. Không bắt buộc nhưng đáng cân nhắc nếu muốn siết thêm giây 30-60.

---

## 5) NARRATOR INTEGRITY SCAN

**Pass — 0 vi phạm.** Quét toàn bộ script theo fake-experience blacklist ("I've grown/tested/spent/planted", "my garden", "when I was", "I remember", "for X years", "my experience", "I personally") — **không xuất hiện lần nào.** Narrator giữ đúng vai trò "kể lại kiến thức công khai", dùng "we" (đại diện kênh) và "you" (viewer), không có claim hands-on cá nhân, không bịa nguồn/tên người không có URL, không có tông "họ giấu bạn". Sạch.

---

## 6) COMPLIANCE FLAG

- 🔴 **[YMYL/PET-SAFETY thiếu] Broadleaf plantain (item #7) thiếu cảnh báo huyết áp.** Research-brief.md ghi rõ trong YMYL Flags: *"Broadleaf plantain → large quantities can lower blood pressure; worth a brief 'everything in moderation' note given the channel's older audience, many of whom may be on blood pressure medication."* Script KHÔNG có câu này ở đoạn Plantain (idx 892–1039) — bỏ sót cả trong retention-spine.md (chỉ liệt "3 YMYL/compliance" nhưng thực tế chỉ nêu 2: violet claim + wood sorrel hedge) lẫn trong script. Đây là gap thật xuyên suốt pipeline, không phải lỗi vặt — audience kênh chính xác là nhóm rủi ro (60-80 tuổi, nhiều người dùng thuốc huyết áp).
  - **Fix cụ thể:** chèn 1 câu ngay sau số liệu plantain, vd: *"One quick note: eating a lot of plantain at once can lower blood pressure, so if you're on blood pressure medication, treat it like any new green — a modest handful, not a full meal."*
- Không phát hiện blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal) — "100 percent of your daily vitamin A" là %DV dinh dưỡng hợp lệ, không phải marketing claim.
- Wood sorrel (item #6) đã có hedge YMYL đúng chuẩn (oxalate, so sánh spinach/rhubarb, khuyến nghị hỏi bác sĩ) ✓
- Pet/grandkid safety có 2 điểm chèn đúng vị trí (item #4 violet + đoạn tổng kết cuối) ✓

---

## 6.5) LESSONS-LEARNED CHECK

| ID | Kết quả |
|---|---|
| L1 (exotic plant) | ✅ PASS — cả 7 cây đều phổ biến ở Mỹ |
| L2 (outcome cụ thể cho counter-intuitive) | ✅ PASS — mỗi item có số cụ thể |
| L3 (deliver title promise trong 60s) | 🟡 SÁT NGƯỠNG — số liệu chứng minh đầu tiên rơi vào ~giây 65-75, trễ hơn ngưỡng 60s (xem Leak 1) |
| L4 (open loop xuyên giây 40-55) | 🟡 YẾU — có câu re-tease nhưng lẫn với đuôi safety-disclaimer (xem Leak 2) |
| L5 (tension layer phút 4-6) | ✅ PASS — Purslane climax đúng vùng, đúng thiết kế |
| L6 (bằng chứng/số trước giây 20-33) | 🔴 VI PHẠM — không có số nào trước giây ~65 (xem Leak 1); đây là rule có 5 video tiền lệ trong evidence log |
| L7 (độ dài ≤10 phút mặc định) | ✅ PASS — 1,459 từ ≈ 9:44 ở pace ~2.5wps |
| L8 (ergonomic benefit stacking) | N/A — video thuộc pillar nutrition/value, không phải ergonomic pain-removal |

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Số liệu cụ thể + cite nguồn inline đúng lúc (USDA, University of Illinois Extension, "a two-thousand-one peer-reviewed nutrition study", "a twenty-fourteen peer-reviewed nutrient study", "a twenty-eighteen peer-reviewed comparison", Davis 2004, UF/IFAS Klee) — mật độ cao, đọc-được-thành-tiếng, đúng chuẩn kênh
- [x] **≥2 câu Consensus Synthesis** — đoạn kết ("Now, the research folks say it different ways, but they keep landing on the same conclusion...") tổng hợp đúng 3 nguồn độc lập (Davis 2004 + UF/IFAS tomato + PLOS ONE 2018) thành 1 nguyên tắc, bọc folksy đúng công thức ✓
- [x] Science moment → Action → Benefit (vd dandelion: "sold in stores for real money... yours already growing free") ✓
- [x] Claim-scoping trung thực — *"these numbers move with soil, season, and how the plant grew, so treat them as a solid ballpark, not a lab guarantee"* ✓
- [x] Góc cơ chế riêng (breeding/dilution-effect) mà video "liệt kê cây ăn được" thông thường không có ✓
- [ ] **1 điểm cần verify — Purslane EPA claim là claim trung tâm nhưng KHÔNG truy được nguồn trong research-brief.md hiện tại.** Brief chỉ ghi "Đã verified sẵn (không đào lại): Purslane (omega-3 **ALA**)" ở phần header — không có mục Q&A riêng cho purslane trong brief này. Script lại đưa ra claim cụ thể hơn nhiều: *"a twenty-fourteen peer-reviewed nutrient study found purslane tested higher in omega-3s than any other leafy green scientists have measured so far... It's one of the only land plants ever found to carry a trace of **EPA**..."* — ALA và EPA là 2 loại omega-3 khác nhau; claim "trace of EPA" (loại omega-3 đặc trưng của dầu cá — đúng thứ làm nên "beats fish" trong title/thumbnail) là claim khoa học có thật trong y văn (Simopoulos et al.) nhưng **không nằm trong tài liệu research-brief.md được cung cấp cho lần audit này**, nên không thể xác nhận độc lập nguồn "2014 peer-reviewed" mà script trích. Đây là claim trụ cột của cả video (title, thumbnail "MORE THAN FISH", Loop #1 payoff) — mức rủi ro cao nhất trong toàn bộ script nếu số/năm sai.
  - **Không phải lỗi bắt buộc REJECT** (vì được đánh dấu "đã verified sẵn" từ một pass trước không có trong input tôi đọc được) nhưng **cần xác nhận lại nguồn trước GATE** — nếu prior verification pass có link cụ thể, nên chèn vào research-brief.md để lần audit sau không phải flag lại.

**→ Anti-Slop: PASS có điều kiện** (đủ ≥2 bằng chứng, không dính pattern slop rõ ràng), với 1 lỗ hổng sourcing cần verify ở trên.

---

## 7) ACTIONABLE FIXES (xếp theo tác động)

1. **[Cao]** Chèn 1 số cụ thể (vd violet "3 oranges" hoặc dandelion vit A) vào trước giây 20 của hook — đóng Leak 1, sửa L6 violation, khớp lại DELIVERY-LOCK của chính retention-spine.
2. **[Cao]** Thêm câu cảnh báo huyết áp cho Plantain (item #7) — gap YMYL thật, đúng nhóm rủi ro của audience kênh (60-80 tuổi).
3. **[Trung bình]** Xác nhận lại nguồn "2014 peer-reviewed / EPA trace" cho Purslane trước khi export — claim trụ cột của cả video.
4. **[Trung bình]** Rút gọn safety-note đầu hook còn 1 câu, dồn chi tiết xuống, để giây 40-55 dành cho open-loop mạnh hơn thay vì đuôi disclaimer (Leak 2).
5. **[Thấp]** Thêm intrigue-trước-tên cho item Plantain (item cuối, bắt buộc theo Storytelling rule 7) + cân nhắc 1 câu anonymous social proof để đạt đủ DNA Voice signature.

---

## 8) INLINE TAGS REPORT

- `[YMYL]` ×2 — wood sorrel (đã có, đúng chuẩn) · plantain (thiếu, cần thêm — xem mục 6)
- `[PET-SAFETY]` ×2 — violet item + đoạn tổng kết cuối (đã có, đạt)
- `[HEDGE]` ×2 — "solid ballpark, not a lab guarantee" · "one of the only land plants ever found" (đã hedge đúng mức)
- `[NEED DATA]` ×1 — nguồn "2014 peer-reviewed / EPA trace" cho Purslane không truy được trong research-brief.md hiện tại (xem mục 6.7)
- `[COMPLIANCE]` ×1 — thiếu cảnh báo huyết áp Plantain (xem mục 6)

---

## VERDICT: REVISE

Mode C yêu cầu PUBLISH chỉ khi MỌI safety check đạt — hiện thiếu 1 (plantain BP caution), nên chưa đủ điều kiện PUBLISH. Không đạt mức REJECT vì đây không phải lỗi hệ thống (narrator integrity sạch 100%, phần lớn YMYL/pet-safety đã đúng chỗ, cấu trúc storytelling — đặc biệt micro-bridge và climax — thực thi tốt). 5 fix ở mục 7 đều cụ thể, nhỏ gọn, không cần viết lại toàn bộ script.

**Nhắc cuối:** bật "Altered or synthetic content" khi upload (AI Voice); Producer sign-off TRƯỚC khi export VoiceAI.
