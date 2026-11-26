# Audit Report — 1 August Mistake Kills Every Hydrangea Bloom Next Year
## (VÒNG AUDIT LẦN 2 — độc lập, đè lên báo cáo vòng 1)

MODE: A | DATA: DATA MODE (garden-us-60k, fetched 2026-06-09/07-04) | LANGUAGE: EN | VIDEO TYPE: Standard (+ pet-safety YMYL beat)
DNA VOICE:          Moderate
NARRATOR INTEGRITY: 1 flag (factual accuracy — xem mục 5)
HOOK:               Needs work
COMPLIANCE (flag):  Clean (0 blacklist — Risk Score đã chấm riêng 10/10, KHÔNG chấm lại; 1 lưu ý nhẹ ngoài phạm vi compliance, xem mục 3)
=> VERDICT: **REVISE**

**Word count thật (đếm lại độc lập):** 1,296 từ (phần TTS SCRIPT) — trong khung 1,200–1,500, PASS L7.

---

## 0) KIỂM TRA 4 BẢN VÁ VÒNG 1 — đã sửa đủ chưa?

| # | Vấn đề vòng 1 | Trạng thái | Ghi chú độc lập |
|---|---|---|---|
| 1 | Câu credibility đứng riêng ở giây 40-55 | 🟡 **SỬA MỘT PHẦN** | Câu *"Every fact today comes from university extension offices…"* đã biến mất, gộp đúng vào câu open-loop (dòng 19: *"Today: the one deadline extension offices actually agree on, straight from their own guidance, plus what to do if you've already crossed it. Then three things worth doing…plus one safety note that's easy to miss. By the end, you'll know exactly where you stand."*). Tốt hơn hẳn bản cũ — không còn "trust statement" trơ trọi. NHƯNG cả đoạn vẫn về bản chất là 1 **preview/TOC liệt kê** (đúng loại nội dung mà `channel-stats` mô tả là nguyên nhân rớt ở vùng 40-55s: *"transition hook→credibility/preview"*), không phải open loop tạo tension thật (không có câu tạo tò mò kiểu "và việc thứ 4 khiến ngay cả người cẩn thận nhất cũng sai" như outline gốc từng định). Xem Leak #1 mới bên dưới. |
| 2 | Thiếu cost comparison | 🟡 **ĐÃ THÊM, có tì vết mới** | Dòng 25: *"…rain or shine, and it's a cheap fix, usually less than a fancy bottle of root stimulator that does far less."* Có so sánh chi phí định tính (đúng yêu cầu, không bịa số $). Nhưng cụm *"that does far less"* là claim **hiệu quả** (không phải chi phí) không có nguồn trong research-brief — vượt phạm vi "cost comparison" ban đầu, chạm nhẹ zero-hallucination. Xem mục 3. |
| 3 | Lệch "three things" vs "four things" | 🟡 **SỬA Ở 2 ĐẦU, chưa sửa ở giữa** | Preview (dòng 19) và recap (dòng 63) nay đều nói "three things…plus one safety note" — khớp nhau. NHƯNG câu bridge giữa bài (dòng 45): *"Water, mulch, pet safety. Now the one that decides everything else: the shears."* lại nhóm "water, mulch, pet safety" thành 1 cụm đã xong và tách "the shears" riêng — tức NGẦM đếm theo kiểu 4 hạng mục song song, mâu thuẫn với cách đếm "3 things (water/mulch/shears) + 1 safety note" mà preview/recap vừa thống nhất. Audience senior dễ bị rối nhẹ ở đúng điểm giữa bài. |
| 4 | Thiếu idiom thứ 2 | ✅ **ĐÃ THÊM, nhưng hơi gượng** | "rain or shine" thêm ở dòng 25. Đạt đủ số lượng (2 idiom: "dirt-cheap" + "rain or shine"), nhưng dùng sai ngữ cảnh nhẹ: "rain or shine" nghĩa gốc là "bất kể trời thế nào, việc vẫn diễn ra" — gắn vào ống tưới nhỏ giọt hơi lệch nghĩa (tưới tự động thường NÊN dừng khi trời mưa, không phải điểm mạnh khi nó chạy "rain or shine"). Không sai nghiêm trọng, nhưng là chỗ có thể chọn idiom khớp hơn. |

**Kết luận Bước 0:** Cả 4 điểm đều được động chạm và có cải thiện thật, nhưng **không có điểm nào sửa dứt điểm 100%** — 3/4 để lại dư chấn nhỏ (giữa preview vẫn TOC-shape, bridge giữa bài lệch cách đếm, idiom hơi gượng, 1 claim hiệu quả sản phẩm không nguồn). Không đủ nghiêm trọng để REJECT nhưng đủ để giữ **REVISE**, cộng thêm 1 phát hiện mới ở mục 5 (không liên quan 4 điểm vòng 1).

---

## 1) TOP 3 RETENTION LEAKS (độc lập, đối chiếu Retention Spine + channel-stats thật)

**Leak #1 — Zone giây 40-55 đã bớt "trust statement" nhưng vẫn là preview/TOC, chưa phải open loop thật (🟡, cải thiện từ 🔴 vòng 1)**
Đoạn (word ~76-139, ≈ giây 28-70 tuỳ pace 2.16-2.7 wps) hiện đọc: *"Today: the one deadline extension offices actually agree on, straight from their own guidance, plus what to do if you've already crossed it. Then three things worth doing for the rest of this month, plus one safety note that's easy to miss. By the end, you'll know exactly where you stand."* Đây thực chất là 1 bản liệt kê nội dung ("what's coming"), không có tension/tò mò mới — chính là pattern mà `channel-truth.md`/`channel-stats` gọi tên là nguyên nhân rớt hình ở vùng này ("vùng chết hook→credibility/preview"). Bản retention-spine gốc (PHA B, hàng 0:40-0:55) đề xuất re-tease dạng "…and by the end you'll know **which mistake is yours**" — có yếu tố cá nhân hoá/tò mò rõ hơn. Bản hiện tại ("you'll know exactly where you stand") mềm hơn, ít kéo tension hơn bản Spine đã duyệt.
→ **Bản vá:** thêm lại 1 mảnh tò mò cụ thể, ví dụ đổi câu chốt thành: *"By the end, you'll know exactly which of those four is the one that's already tripping you up."* — giữ nguyên phần liệt kê nhưng đóng bằng 1 câu hỏi ngầm thay vì câu khẳng định trung tính.

**Leak #2 — Climax pruning (word ~798-828, "That's the trap…") có nguy cơ trôi RA NGOÀI `MIDROLL_DIP_ZONE` (phút 4-6) ở pace chậm — rủi ro do chính các bản vá vòng 1 gây ra (🔴 mới, chưa từng bị flag ở vòng 1)**
Tổng từ đã tăng từ ~1,254 (vòng 1) lên 1,296 (vòng 2) — tăng ~42 từ do gộp câu credibility + thêm cost-comparison + "rain or shine", tất cả đều nằm TRƯỚC đoạn climax. Điều này đẩy climax muộn hơn ~15-20s so với bản trước.
- Ở pace nhanh (2.7 wps ≈ video 8 phút): climax rơi vào giây 296-307 (4:56-5:07) — **trong vùng** 240-360s. OK.
- Ở pace chậm (2.16 wps ≈ video 10 phút, tức đầu KIA của chính target `video_length` 8-10' trong config): climax rơi vào giây 369-383 (**6:09-6:23**) — **NGOÀI** vùng `MIDROLL_DIP_ZONE` (240-360s), trễ 9-23 giây so với mốc đóng zone.
Đây không phải biên cực đoan giả định — 10 phút là chính đầu trên của `target_minutes: "8-10"` trong `channel.config.json`, và ghi chú `_why` trong chính config đó nói rõ **video 9-10' đạt AVD 33-36% (mục tiêu ưu tiên)**, tức nhóm sản xuất nhiều khả năng nhắm tới đầu dài hơn của khung — chính là đầu mà climax bị trôi khỏi vùng dip. Vì đây là loop lớn DUY NHẤT của video (theo Spine: "Số loop: 1 loop chính xuyên suốt"), lỡ mốc phút 4-6 = vi phạm L5 (Jenga Retention bắt buộc đúng vùng) ở đúng điểm quyết định nhất.
→ **Bản vá:** cắt ~30-40 từ ở đoạn trước climax (ứng viên: đoạn mulch P8-P10, hoặc rút gọn câu cost-comparison mới thêm) để kéo climax về lại trong 360s ở mọi pace hợp lý; hoặc xác nhận runtime thật sau khi TTS render và điều chỉnh nếu cần.

**Leak #3 — Bridge giữa bài ngầm mâu thuẫn với cách đếm "3+1" vừa được đồng bộ (🟡, xem thêm mục 0.3)**
Dòng 45: *"Water, mulch, pet safety. Now the one that decides everything else: the shears."* — câu này đóng vai trò bridge tốt về nhịp điệu (được vòng 1 khen), nhưng về logic đếm số, nó gộp "pet safety" vào nhóm đã-xong cùng nước/mulch rồi tách "shears" ra riêng — ngược với cấu trúc "3 things (nước, mulch, shears) + 1 safety note (pet)" mà preview/recap thống nhất. Vì DNA Structure Signature #2 của kênh dựa vào "lặp 1 con số xuyên bài" để dễ theo dõi với audience 60-80 tuổi, sự lệch pha này (dù nhỏ) làm giảm hiệu quả chính bản vá #3 của vòng 1.
→ **Bản vá:** đổi câu bridge thành *"Water and mulch, handled. One safety note along the way. Now the one that decides everything else: the shears."* — tách rõ "safety note" khỏi cụm 2 "things" đã xong, khớp đúng cách đếm 3+1.

---

## 2) HOOK CHECK

- [~] Đòn đau/viễn cảnh tương phản — có, dạng revelation (đúng khai báo retention-spine.md)
- [x] Open Loop/Countdown anchor — có ("the one deadline extension offices actually agree on")
- [ ] **5 từ đầu mạnh** — *"That healthy hydrangea by your…"* — KHÔNG có verb mệnh lệnh/pain statement, vẫn mềm cho 1 video "mistake/kills" (giống hệt vòng 1, KHÔNG nằm trong 4 điểm được yêu cầu sửa, nên vẫn tồn tại — ghi nhận lại vì đây là audit độc lập đầy đủ)
- [x] Mini-payoff trước ~20s — "August first" ở word 20-21 (≈7-9s), rất tốt, không đổi so với vòng 1
- [~] **Zone giây 40-55** — đã hết câu trust-statement trơ trọi, nhưng vẫn preview-shape thay vì open loop thật — xem Leak #1

**2 bản hook rewrite (giữ nguyên đề xuất vòng 1, vẫn còn giá trị vì chưa được áp dụng):**
1. *"Right now, hidden inside your hydrangea's stems, next year's flowers are already being decided. Extension research points to one hard date: August first."*
2. *"Look at your hydrangea today — it's already writing next June's flower count. And Extension research says there's exactly one hard date that decides it: August first."*

---

## 3) DNA VOICE AUDIT (theo channel-truth.md + brand-voice-dna.md)

| Signature bắt buộc | Có/Thiếu | Ghi chú |
|---|---|---|
| Grandmother-or-failure story | 🟡 Nhẹ | Không có story cá nhân — có documented-history scene (Siebold/Dejima 1823) thay thế hợp lệ, NHƯNG xem lỗi kiện tính ở mục 5 |
| "Here's why this works" + analogy (Problem-Fix, target 2-3) | 🟡 Vẫn dưới target | Chỉ 1 lần rõ ("Here's why depth matters more than frequency…") — không đổi so với vòng 1, không nằm trong 4 điểm yêu cầu sửa |
| "Don't panic" (×1, Voice & Narrator) | ✅ | *"So don't panic if you missed a watering or two"* — có, đúng vị trí trấn an sau đoạn hedge khoa học |
| "That's it" (×1) | ✅ | *"That's it for the rest of the year."* |
| Exact numbers | ✅ | August 1, 1"/2", 6", 2-3" mulch, 20 min (×2, lặp số hợp DNA structure), 1823/eighteen-twenties, hotline đọc chữ đúng chuẩn TTS |
| 3 mistakes | N/A hợp lý | Big Idea cố tình xây quanh đúng 1 mistake (đúng chủ đích Promise Engine) |
| **Cost comparison (DIY vs store)** | 🟡 Đã thêm, có tì vết | Xem mục 0.2 — thêm đúng yêu cầu (định tính, không bịa số $), nhưng câu *"that does far less"* là claim hiệu quả sản phẩm KHÔNG có nguồn trong research-brief — nên đổi thành thuần cost, VD: *"and it's a cheap fix, usually a fraction of what a fancy bottle of root stimulator runs."* (bỏ phần "does far less") |
| Anonymous social proof | ✅ | "One gardener in coastal Georgia says…" — đúng pattern |
| Accessibility Anchors ×2-3 | ✅ | "no daily trip out with a hose needed", "easy on the back. No bending, no standing…", "Twenty minutes with a wheelbarrow" |
| ≥2 gardener idioms khác nhau | ✅ (số lượng đạt, chất lượng 🟡) | "dirt-cheap" + "rain or shine" — đủ số nhưng "rain or shine" hơi lệch ngữ cảnh, xem mục 0.4 |
| ≥1 folksy marker | ✅ | "Folks do it with good intentions…" |
| Sign-off "Happy gardening." | ✅ | Đúng vị trí cuối |

**Kết luận:** DNA Voice = **Moderate** — không tệ hơn vòng 1 (vẫn không phải Weak), nhưng chưa đủ sạch để lên Strong vì 3 tì vết nhỏ mới phát sinh từ chính các bản vá (efficacy claim không nguồn, idiom lệch ngữ cảnh, bridge lệch cách đếm) cộng 1 gap cũ chưa đụng tới (Here's-why-this-works count).

---

## 4) STORYTELLING CRAFT CHECK

- Micro-bridge: đa số OK; bridge P16 ("Water, mulch, pet safety. Now the one that decides everything else: the shears.") về NHỊP ĐIỆU vẫn tốt nhưng về LOGIC ĐẾM SỐ mâu thuẫn với fix #3 — xem Leak #3.
- Scene ≥1-2: Đạt 2 — viewer-POV ("Picture the stem itself for a second…") + documented history (Siebold/Dejima, có nguồn URL trong research-brief) — NHƯNG chi tiết trong scene lịch sử bị sai (xem mục 5), nên về mặt "có nguồn" thì đạt, về mặt "trung thực với nguồn" thì KHÔNG đạt.
- Mid-video re-hook tại dip zone: ✅ vị trí đúng ("And this one's for anyone who already trimmed back a hydrangea…") — nhưng cần re-verify lại timing thật sau khi sửa Leak #2, vì cả cụm quanh climax đã trôi muộn hơn.
- Climax beat: có build-up rõ, nhưng **vị trí thời gian là rủi ro chính của vòng audit này** — xem Leak #2.
- Kết video: ✅ Forward-visual close → Identity CTA → câu hỏi geo-specific (USDA zone) → sign-off. Đúng thứ tự chuẩn, không đổi so với vòng 1, vẫn tốt.

---

## 5) NARRATOR INTEGRITY SCAN

**Fake-experience blacklist ("I've grown/tested/spent/planted", "my garden", "when I was", "for X years", "my experience", "I personally"):** quét lại toàn bộ script — **0 vi phạm**, xác nhận độc lập giống vòng 1. Điểm mạnh rõ rệt, không đổi.

**1 flag MỚI — sai lệch dữ kiện lịch sử so với chính nguồn research-brief đã trích (🔴):**
> **[trích script, dòng 27]** *"Back in the eighteen-twenties, **a Dutch physician** worked on a small trading island off Japan… He named a hydrangea species after the woman he loved there…"*

Research-brief (Story Bank #1) ghi rõ nguồn: *"bác sĩ kiêm nhà tự nhiên học **người Đức** Philipp Franz von Siebold"* — Siebold là người **Đức**, làm việc CHO trạm buôn của Hà Lan (VOC) trên đảo Dejima — ông không phải "a Dutch physician" (một bác sĩ người Hà Lan). Script đã lẫn quốc tịch cá nhân với quốc tịch của trạm thương mại nơi ông làm việc. Đây là lỗi kiện tính (fact distortion) đối với chính nguồn đã được duyệt trong Story Bank, không phải "không có nguồn" mà là "có nguồn nhưng trích sai" — nghiêm trọng hơn việc thiếu nguồn, vì khán giả nào tra cứu thêm (hoặc đã biết lịch sử Nhật Bản/Siebold) có thể bắt lỗi và để lại comment sửa sai — đúng rủi ro mà `channel-truth.md` cảnh báo ("khán giả chủ động report + comment sửa lỗi").
→ **Bản vá:** đổi thành *"a German physician stationed at Japan's only Dutch trading post"* hoặc đơn giản *"a young German doctor working at Japan's only outpost for Westerners"* — giữ nguyên phần còn lại của câu chuyện, chỉ sửa đúng quốc tịch.

---

## 6) COMPLIANCE FLAG (nhẹ — không chấm lại Risk Score)

Sạch — quét lại độc lập không thấy blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal), không có claim tuyệt đối mới phát sinh từ các bản vá. 1 lưu ý CHUYỂN CHO Ý THỨC BIÊN TẬP (không phải blacklist, không cần chấm lại Risk Score): câu *"a fancy bottle of root stimulator that does far less"* là 1 dạng disparagement nhẹ với 1 nhóm sản phẩm thương mại không có nguồn — rủi ro thấp nhưng nên xem cùng lúc sửa mục 3.

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES)

| Rule | Kết quả |
|---|---|
| L1 exotic plant | ✅ PASS |
| L2 outcome cụ thể | ✅ PASS — "zero flowers next spring" |
| L3 deliver trong 60s | ✅ PASS mạnh — mechanism ở giây ~8 |
| L4 open loop giây 40-55, không chuyển credibility | 🟡 **CẢI THIỆN, chưa PASS hoàn toàn** — hết trust-statement trơ trọi nhưng vẫn preview-shape (Leak #1) |
| L5 tension layer phút 4-6, Jenga bật | 🔴 **RỦI RO MỚI** — climax có thể trôi ra ngoài zone ở pace chậm (Leak #2), do chính việc thêm từ ở các bản vá khác |
| L6 bằng chứng trước giây 20 | ✅ PASS mạnh |
| L7 độ dài ≤10′ trừ earned | ✅ PASS — 1,296 từ, trong khung 1,200-1,500 (nhưng gần đầu trên hơn vòng 1, góp phần gây Leak #2) |
| L8 ergonomic stacking | ✅ Có trong body |
| CR6 cost transparency | 🟡 PASS có tì vết — xem mục 3 |
| CR4 claim-scoping | ✅ PASS mạnh — đoạn panicle/smooth "in safer territory" |
| CR5 safety callout 1 beat rõ | ✅ PASS |
| CR7 hero anchor số lặp | ✅ PASS — "August first" lặp 3 lần; "twenty minutes" lặp 2 lần (bonus, không có ở vòng 1) |

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

≥2 bằng chứng vẫn đạt, không đổi so với vòng 1: (1) 2 câu Consensus Synthesis rõ (watering + pruning date). (2) Claim-scoping trung thực (panicle/smooth exception). (3) Science → Action → Benefit rõ (soaker hose → dễ với lưng). → **PASS**, không dính pattern slop. (Lỗi Dutch/German ở mục 5 là lỗi kiện tính lịch sử, không phải "cơ chế giả khoa học" — không đổi verdict mục này, nhưng vẫn phải sửa vì thuộc phạm trù Narrator Integrity/zero-hallucination.)

---

## 7) ACTIONABLE FIXES (ưu tiên cao → thấp)

1. **[Cao]** Sửa lỗi kiện tính "a Dutch physician" → "a German physician" (mục 5) — dễ sửa, 2 từ, nhưng là lỗi thật đối chiếu ngược nguồn đã duyệt.
2. **[Cao]** Kiểm tra/kéo climax pruning về lại trong `MIDROLL_DIP_ZONE` (phút 4-6) — cắt ~30-40 từ trước climax hoặc xác nhận runtime thật sau TTS (Leak #2). Đây là rủi ro trực tiếp tới L5, ảnh hưởng AVD.
3. **[Trung]** Làm mạnh lại câu chốt zone 40-55s thành open loop thật thay vì preview thuần (Leak #1) — thêm 1 mảnh tò mò cụ thể.
4. **[Trung]** Sửa bridge P16 để khớp đúng cách đếm "3 things + 1 safety note" đã đồng bộ ở preview/recap (Leak #3).
5. **[Thấp]** Bỏ cụm "that does far less" (claim hiệu quả không nguồn) khỏi câu cost-comparison, giữ thuần phần chi phí.
6. **[Thấp]** Cân nhắc đổi "rain or shine" sang idiom khớp ngữ cảnh tưới nước hơn (vd "come drought or downpour" hoặc bỏ, giữ "dirt-cheap" là đủ số lượng tối thiểu).

---

## 8) INLINE TAGS REPORT

`[NEED DATA]` — cụm "that does far less" (hiệu quả root stimulator) không có nguồn trong research-brief.
`[HEDGE]` — đoạn "Extension experts also warn that a hot, dry summer isn't good for bud development" vẫn đúng mức hedge theo research-brief Câu hỏi 2 (xác nhận lại độc lập, không đổi so với vòng 1).
`[YMYL]` — beat pet-safety (P12-16): disclaimer đầy đủ, cân bằng overclaim/underclaim, đúng số hotline người (1-800-222-1222) tách biệt đúng khỏi ASPCA Poison Control cho thú cưng — xác nhận chính xác, không cần sửa.
`[COMPLIANCE]` — không có dấu hiệu blacklist mới; 1 lưu ý nhẹ về disparagement sản phẩm không nguồn (mục 6), không đủ nghiêm trọng để yêu cầu chấm lại Risk Score.

---

## Ghi chú cuối

- Bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off TRƯỚC khi VoiceAI export.
- **Verdict REVISE** (không REJECT, không PUBLISH): Narrator Integrity vẫn sạch ở phần hands-on-claim (0 vi phạm), nhưng có 1 lỗi kiện tính lịch sử thật cần sửa (mục 5) + 1 rủi ro timing thật đối với L5/MIDROLL_DIP_ZONE mà chính việc cộng dồn từ từ 4 bản vá vòng 1 gây ra (mục 1, Leak #2) — đây là phát hiện KHÔNG nằm trong phạm vi 4 điểm vòng 1 yêu cầu kiểm tra, nhưng là hệ quả trực tiếp của việc áp các bản vá đó. Tất cả đều là sửa câu/cắt từ, không cần viết lại cấu trúc — phù hợp REVISE, không REJECT.
- Cả 4 điểm vòng 1 đều được động chạm thật (không phải bỏ qua), nhưng nên coi là "cải thiện có điều kiện" chứ không phải "đóng hẳn" — audit vòng sau (nếu có) nên kiểm tra lại đúng các điểm 🟡 ở mục 0 trước khi PUBLISH.
