# Audit Report — The 8-Inch Fix for a Dying Clematis (Dead Zone Watering)

> Audit độc lập (góc nhìn thứ 2) — không có context viết script. Chạy theo `mkt-youtube-script-audit` V7 Lean.

---

## 1) HEADER

```
MODE: A (Standard) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard
DNA VOICE:          Moderate
NARRATOR INTEGRITY: 1 flag
HOOK:               Pass (1 minor leak flagged — see #2 below)
COMPLIANCE (flag):  Clean (0 blacklist / pet-safety present / no YMYL)
=> VERDICT: REVISE
```

Word count: ~1,273 words (target 1,200–1,500 ✅). Runtime ≈ 8:30–9:05 (đúng khung 8–10 phút, L7 pass).

---

## 2) TOP 3 RETENTION LEAKS

### Leak #1 — Claim định lượng không có nguồn, nằm đúng MIDROLL_DIP_ZONE (phút 4–6)

> **"And one of them accidentally created half the clematis vines climbing over American porches today."**

→ Research-brief (Story Bank, George Jackman) **không có** con số "half the clematis vines… today" ở bất kỳ đâu — chỉ nói Jackmanii "tạo ra làn sóng Clematis Mania" và "vẫn là một trong những giống được trồng nhiều nhất". Câu này là số liệu bịa, rơi đúng vào MIDROLL_DIP_ZONE (giây 240–360, nơi kênh rớt nặng thứ 2). Đây chính xác là kiểu claim mà audience senior hay soi ra và sửa lỗi khoa học (đúng điểm yếu mà FACELESS WEDGE trong `channel-truth.md` cảnh báo) — hỏng đúng lúc retention yếu nhất, đúng lúc đang cần Story Bank gánh vai trò pattern-break đáng tin.

→ **Bản vá (giữ DNA Voice, bám đúng research-brief):**
*"And one of them created a clematis so popular, it's still one of the most planted varieties climbing over American porches today."* (câu ngay sau đó — "the big-flowered clematis that's still one of the most planted vines in the country" — đã có sẵn trong script, chỉ cần gộp lại, bỏ hẳn con số "half…today" bịa.)

### Leak #2 — Beat preview đè lên 5 giây đầu của HOOK_DROPOFF_ZONE (giây 40–55)

> **"…I'll also share two signs that tell you you've been getting it wrong for years. Two signs, and one habit to break for good."** (word idx ~90–112, ≈ giây 36–45)

→ L4 (ACTIVE RULE) cấm rõ: "KHÔNG chuyển sang preview/giới thiệu" tại giây 40–55 — đây là vùng chết #1 toàn kênh (cumulative loss trung bình -37% giây 2→25%). Câu trên là đuôi của beat preview ("Coming up, I'll show you the exact spot…") kéo dài đến tận ~giây 45, đè lên đúng 5 giây đầu của vùng rớt nặng nhất kênh, trước khi mới pivot sang nội dung khoa học ("Now, here's why this works…").

→ **Bản vá:** nén beat preview để dứt trước giây ~35, đẩy loop khoa học lên sớm hơn:
*"Here's the thing — this isn't some rare mistake. Almost every clematis grower does it, because it feels like the caring thing to do. Coming up, I'll show you the exact spot — plus two signs you've been getting it wrong. Now, here's why this works…"* (cắt câu lặp "for years. Two signs, and one habit to break for good" — vào thẳng khoa học sớm hơn ~8-10 từ, đủ để cả vùng 40-55s nằm trong nội dung mở loop chứ không phải đuôi preview).

### Leak #3 — Trích dẫn "extension guides" không khớp nguồn, đúng khoảnh khắc payoff cốt lõi (~2:27–3:00)

> **"Extension guides say to keep mulch six to eight inches off a clematis stem so the crown can breathe."**

→ Research-brief ghi rõ: Illinois Extension PDF nói mulch **8 inch**; cùng Illinois Extension (trang web) lại nói **4–6 inch**; American Meadows nói 6–12 inch — **không nguồn nào hội tụ đúng "6-8 inch"**. Research-brief đã cảnh báo sẵn: *"Tránh nói 'extension guides' như thể đây là con số đã hội tụ."* Câu này rơi đúng vào khoảnh khắc trả lời lời hứa cốt lõi của title ("8-Inch Fix") — nếu bị soi sai, hỏng đúng khoảnh khắc quan trọng nhất của toàn bộ chiến lược "Science-Backed Proof".

→ **Bản vá (đúng hedge research-brief đã đề xuất):**
*"Extension guides don't all agree on the exact number — some say six inches, some say eight — but every one of them agrees on this: give that crown room to breathe."*

---

## 3) HOOK CHECK (0–60s, soi đặc biệt giây 40–55)

- [x] Đòn đau / viễn cảnh tương phản — "you might actually be drowning it" (đảo ngược thói quen tưởng chăm cây thành sai lầm)
- [x] Open Loop / Countdown anchor — "So where should the water actually go? That's what I'm showing you next."
- [~] 5 từ đầu mạnh — "If you're watering your clematis" là khung điều kiện (second-person), ổn nhưng chưa phải pain-statement/verb mệnh lệnh mạnh nhất có thể theo Hook Stack (CR1)
- [x] Mini-payoff trước ~20s — "root rot in as little as four hours" ở ~giây 13.6 (đúng L6, bằng chứng trước giây 20)
- [ ] **HOOK_DROPOFF_ZONE (giây 40-55):** đuôi preview lấn ~5 giây đầu vùng chết trước khi pivot sang khoa học — xem Leak #2

**Ghi chú thêm (Hook Stack, CR1):** hook thiếu 1 mỏ neo giá tiền/con số cụ thể cực sớm (yếu tố "Giá trị/giá tiền cụ thể" trong Hook Stack 6-beat) — giá "$15-20" chỉ xuất hiện ở ~phút 6:30. Không bắt buộc phải sửa (hook vẫn Pass nhờ pain + open loop + bằng chứng sớm), nhưng là cơ hội siết thêm nếu muốn.

Verdict: **Pass** (không cần rewrite toàn bộ hook, chỉ cần patch Leak #2).

---

## 4) DNA VOICE AUDIT

**Signature elements (theo `channel-truth.md` + `brand-voice-dna.md`):**

| Element | Có/Thiếu | Ghi chú |
|---|---|---|
| "Here's why this works" + analogy | ✅ | ×2 ("Now, here's why this works" + "plumbing setup" analogy) |
| "Don't panic" | ✅ | ×1 đúng vị trí (trước khi vào con số cụ thể) |
| "the real reason / the simple fix" | ✅ | "Here's the simple fix" |
| "That's it" | ✅ | ×1 |
| Exact numbers | ✅ | "four hours", "six to eight inches", "two to four inches", "fifteen to twenty dollars" |
| 2 signs (thay "3 mistakes" — đúng theo outline/spine đã duyệt) | ✅ | Sign 1 + Sign 2 rõ ràng |
| Cost comparison | ✅ (nhẹ) | "$15-20" ring vs "losing a vine you've grown for years" — value-ratio, không phải DIY-vs-store cổ điển nhưng đúng tinh thần CR6 |
| Anonymous social proof | ✅ | "A viewer in Ohio" (đúng 1 lần, trong khung 1-2 cho phép) |
| Accessibility Anchors ×2-3 | ✅ (2) | "thirty seconds", "All you need is the hose you already own" — đạt tối thiểu, có thể thêm 1 anchor nữa |
| Grandmother-or-failure story | ➡️ **thay bằng Story Bank** | Đúng chủ trương Storytelling Upgrade 07/2026 (documented history thay fake family story) — không phải lỗi |
| Sign-off "Happy gardening." | ✅ | Đúng vị trí cuối cùng |

**Human Texture E7:**
- Contractions: **~49.5%** câu (đo tự động) — **dưới mục tiêu ≥60%** 🟡. Tập trung thiếu nhất ở đoạn Framework khoa học (giải phẫu rễ, Phytophthora) — đúng đoạn dễ ngả sang giọng "giảng bài" nhất.
- Gardener idioms: ✅ ≥2 — "green thumb", "dirt-cheap"
- Folksy marker: ✅ ≥1 — "the culprit" ("That right there? That's the culprit.")
- AI clichés: ✅ 0 matches (delve/leverage/utilize/robust/moreover/furthermore… — sạch)

**Kết luận DNA Voice: Moderate** — cấu trúc tín hiệu bản sắc (mantra 3-nhịp cuối bài "saves your knees, spares the roots, and lets that vine finally thrive", chẩn đoán chắc nịch "That right there? That's the culprit.", fragment ngắn "That's it.") đều có mặt, nhưng contraction-rate dưới ngưỡng + 2 câu trích dẫn không khớp nguồn (Leak #1, #3) kéo xuống từ Strong.

---

## 4.5) STORYTELLING CRAFT CHECK

- [x] **Không có "trạm dừng" đáng kể.** 1 transition hơi phẳng ("One quick safety note for the household…") nhưng đây là safety beat theo đúng CR5 (phải là beat rõ, không chôn vùi) — chấp nhận được, không cần bridge.
- [x] **Scene ≥1** — George Jackman, Woking 1858, có nguồn (The Daily Gardener) trong Story Bank. Chi tiết khớp brief (21 tuổi, 6 tháng, nhà kính nhỏ). **Ngoại lệ:** câu dẫn vào scene ("half the clematis vines… today") là số liệu bịa — xem Leak #1. Cần sửa TRƯỚC scene, không phải bỏ cả scene.
- [x] **Mid-video re-hook tại MIDROLL_DIP_ZONE (phút 4-6)** — "And this one's especially for those of you with an established clematis… since a mature plant's roots reach further than you'd think." (~4:23-4:39) — đúng vị trí, đúng công thức (nói thẳng với 1 nhóm viewer).
- [N/A] Per-item intrigue — không áp dụng (Problem-Fix, không phải listicle).
- [x] **Climax beat** — "That right there? That's the culprit… the deadest of dead zones" + "one-two punch" (oxy mất + Phytophthora 4-8h) tại ~3:00-3:54, ngay trước MIDROLL_DIP_ZONE, có build-up đầy đủ (không rơi vào giữa dip mà thiếu setup).
- [x] **Forward-visual close TRƯỚC identity CTA** — "your next good rain will already be watering exactly where this vine wants it" → rồi mới "If you're the kind of gardener who'd rather fix the spot than fight the plant — you belong here." Đúng thứ tự Cinematic Toolkit rule #9 → #5.

---

## 5) NARRATOR INTEGRITY SCAN

Quét đủ fake-experience blacklist (I've grown/tested/spent/planted, my garden, when I was, for X years, my experience, I personally) — **0 vi phạm dạng hands-on claim.** Narrator giữ đúng vai trò educator/storyteller xuyên suốt.

**1 flag — bịa số liệu/nguồn (không phải hands-on claim, nhưng vi phạm "CẤM bịa nguồn"):**

- **Câu gốc:** "one of them accidentally created half the clematis vines climbing over American porches today"
- **Rewrite an toàn (giữ DNA Voice):** "one of them created a clematis so popular, it's still one of the most planted varieties climbing over American porches today" (bám đúng câu research-brief đã có sẵn ngay sau đó trong script, không cần thêm nguồn mới)

---

## 6) COMPLIANCE FLAG (nhẹ)

- Blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox/heal): **0 matches** — Clean
- Tier C (YMYL): N/A — chủ đề chăm cây, research-brief đã xác nhận không có YMYL claim trực tiếp
- Pet/Kid safety: ✅ có mặt — "clematis can irritate skin or a curious pet's stomach if it's chewed on. New cuttings are best kept away from paws and little hands." (đúng Theme 3 comment driver)

**→ Compliance flag: Clean.** Chạy `mkt-yt-compliance` để chấm Risk Score chính thức nếu cần trước export.

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES)

| Rule | Kết quả | Ghi chú |
|---|---|---|
| L1 (đừng chọn cây exotic) | ✅ Pass | Clematis phổ biến với US gardeners |
| L2 (outcome cụ thể cho counter-intuitive) | ✅ Pass | "root rot trong 4 giờ" + "6-8 inch" + 2 signs cụ thể |
| L3 (deliver lời hứa title trong 60s) | ✅ Pass (theo thiết kế Spine đã duyệt GATE 2.5) | Hướng trả lời chung giao ở ~55-60s; con số cụ thể giao ở ~2:27 — đã được lý giải rõ ở DELIVERY-LOCK check của retention-spine.md, không phải lỗi mới |
| L4 (open loop xuyên giây 40-55, không preview) | 🟡 Partial | Xem Leak #2 — đuôi preview lấn ~5s đầu vùng |
| L5 (tension layer phút 4-6) | ✅ Pass | Re-hook + testimonial + Story Bank đúng vị trí |
| L6 (bằng chứng trước giây 20) | ✅ Pass | "four hours" ở ~giây 13.6 |
| L7 (không vượt 10 phút mặc định) | ✅ Pass | ~8:30-9:05 |
| L8 (title/angle ergonomic triple-pain-removal) | 🟡 Note (không blocking) | Title "8-Inch Fix" không front-load ergonomic claim như công thức AVD 49% ("No Soil, No Back Pain, No Cost") — script có nội dung ergonomic ("no kneeling, no bending", "saves your knees") nhưng title/outline đã qua GATE 1, không đề xuất đổi lại ở audit này, chỉ ghi nhận cơ hội cho video sau |

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Số liệu cụ thể + nguồn cite inline — phần lớn tốt (4 giờ, feeder roots cluster, oxy mất tức thời); **2 ngoại lệ bị flag ở Leak #1 và #3**
- [x] ≥2 câu Consensus Synthesis — đạt: *"Nearly every university extension office agrees on this same point…"* + *"Plant pathologists at university extension offices keep landing on the same two-part answer."* (đúng Research Authority word bank, không lặp citation đơn lẻ)
- [x] Science → Action → Benefit — mỗi đoạn khoa học đều chốt hành động cụ thể (tưới vành ngoài, dùng soaker ring)
- [~] Claim-scoping trung thực — phần lớn tốt, nhưng Leak #1 và #3 là 2 chỗ claim-scoping bị lỏng (trình bày như đã hội tụ/xác nhận trong khi thực tế chưa)
- [x] Góc cơ chế/research độc đáo — "dead zone" framing + feeder-root science là góc chưa thấy ở kênh cùng niche (đúng research-brief câu hỏi 4)
- [x] Không dính pattern slop kiểu giả khoa học (stick-X-inside-Y) — sạch

**Kết luận:** 2 bằng chứng đạt chuẩn trở lên, KHÔNG dính pattern slop hệ thống — nhưng 2 claim cụ thể (Leak #1, #3) đủ nghiêm trọng để giữ verdict ở REVISE thay vì PUBLISH thẳng, vì chúng nằm đúng 2 khoảnh khắc rủi ro cao nhất video (MIDROLL_DIP payoff + core title-payoff).

---

## 7) ACTIONABLE FIXES (xếp theo tác động)

1. **[CAO]** Xoá/sửa "half the clematis vines climbing over American porches today" (Leak #1) — không có nguồn, rơi đúng MIDROLL_DIP_ZONE.
2. **[CAO]** Sửa "Extension guides say to keep mulch six to eight inches" (Leak #3) — dùng hedge "some say six, some say eight" thay vì trình bày như con số đã hội tụ.
3. **[TB]** Nén đuôi beat preview (giây 36-45) để không đè lên đầu HOOK_DROPOFF_ZONE (Leak #2).
4. **[TB]** Tăng mật độ contraction (hiện ~49.5%, mục tiêu ≥60%), đặc biệt ở đoạn Framework khoa học — thêm "you know / I mean / that's" tự nhiên để giữ giọng "bà nội Ohio" khi giải thích khoa học.
5. **[THẤP]** "The very first book written on clematis" → research-brief ghi rõ là "cuốn sách chuyên đề đầu tiên **bằng tiếng Anh**" — thêm hedge "in English" để tránh overclaim phạm vi.

---

## 8) INLINE TAGS REPORT

- `[NEED DATA]` — "half the clematis vines climbing over American porches today" (không có nguồn trong research-brief)
- `[NEED DATA]` — "fifteen to twenty dollars at any hardware store" (giá không xuất hiện trong research-brief; hedge "give or take" nếu giữ)
- `[HEDGE]` — "Extension guides say to keep mulch six to eight inches off a clematis stem" (nguồn không hội tụ đúng range này)
- `[HEDGE]` — "The very first book written on clematis" (thiếu qualifier "in English" so với research-brief)
- `[PET-SAFETY]` — ✅ đã có, đạt chuẩn, không cần sửa
- `[COMPLIANCE]` — không có flag blacklist

---

## VERDICT: REVISE

Không REJECT vì: không có hands-on claim xuyên suốt, không YMYL thiếu disclaimer, không blacklist compliance nặng. Cần REVISE vì: 2 claim định lượng không khớp nguồn (Leak #1, #3) rơi đúng 2 khoảnh khắc rủi ro cao nhất video (MIDROLL_DIP payoff + core title-payoff) + 1 chỗ preview lấn HOOK_DROPOFF_ZONE + contraction-rate dưới ngưỡng. Cả 4 đều sửa được bằng patch cục bộ, không cần viết lại script.

**Nhắc trước export:** bật "Altered or synthetic content" khi upload (AI Voice) · Producer sign-off TRƯỚC khi đưa vào VoiceAI.
