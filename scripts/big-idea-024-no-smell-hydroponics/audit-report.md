# Independent Script Audit — Grow 7 Herbs in Water (No Soil, No Smell, No Mess)

MODE: A (Standard) | DATA: DATA MODE (channel-stats-garden-us-60k.md fetched 2026-06-09, ≤14 ngày cảnh báo — xem note) | LANGUAGE: EN | VIDEO TYPE: Standard

DNA VOICE:          Strong
NARRATOR INTEGRITY: Pass (0 flags)
HOOK:               Pass (minor timing note)
COMPLIANCE (flag):  Clean (mkt-yt-compliance đã chấm chính thức 10/10 PUBLISH, 2 vòng sửa)

=> **VERDICT: REVISE** (2 fix cheap, high-leverage — không cần viết lại, không chặn compliance)

> ⚠️ Note: `channel-stats-garden-us-60k.md` fetched 2026-06-09 — tại thời điểm audit (2026-07-07) đã hơn 14 ngày. Số liệu AVD 25.6% / drop zones vẫn dùng vì không có bản mới hơn, nhưng khuyến nghị chạy lại benchmark sync định kỳ.

---

## TOP 3 RETENTION LEAKS

1. **[Preview không nêu tên cả 7 herb]** → "Today I'm walking you through seven herbs that root and grow in nothing but water" — chỉ có con số "seven", không tên. Theo CR2 (competitor teardown): listicle nên nêu TÊN tất cả item ngay preview để mở NHIỀU open-loop cùng lúc ("mint, basil, thyme, chives, oregano, parsley, and even lemon balm — the slowest one on this list") — hiện tại chỉ có 1 loop chung ("7 herbs"), bỏ lỡ cơ hội giữ chân bằng nhiều mini-curiosity song song.
   → **Bản vá:** đổi câu preview thành: *"Today I'm walking you through seven herbs — mint, basil, thyme, chives, oregano, parsley, and the one that takes patience — that root and grow in nothing but water."* (giữ đúng giọng, không thêm claim mới)

2. **[Herb đầu tiên (Mint) reveal ở ~giây 80, hơi trễ so với L3 <60s]** → đoạn "3 mistakes" (giây ~52-70) đã giao value sớm (đúng tinh thần L4/hook drop-off), nhưng "value LỚN" đầu tiên của lời hứa title (herb cụ thể #1) chỉ tới ở giây ~80. Không nghiêm trọng (mistakes-beat đã lấp khoảng trống), nhưng nếu muốn siết chặt L3, có thể rút ngắn đoạn mistakes 1-2 câu.
   → **Bản vá (tùy chọn):** gộp mistake 2+3 thành 1 câu để đẩy Mint lên sớm hơn ~10-15 từ.

3. **[Chỉ có 1 câu Consensus Synthesis rõ ràng, thiếu câu thứ 2]** → Research-brief có 2 Consensus Principles (mosquito+water-change VÀ soft-stem-herb-vs-rosemary), nhưng script chỉ thể hiện rõ nguyên tắc #1 ("Nearly every extension guide says the same thing..."). Nguyên tắc #2 (tại sao rosemary bị loại) không xuất hiện — script chỉ lặng lẽ không đưa rosemary vào danh sách, mất cơ hội anti-slop differentiation (điều 1 kênh AI-slop generic không biết để nói).
   → **Bản vá (tùy chọn, không bắt buộc):** thêm 1 câu ngắn trong đoạn giới thiệu 3-mistakes hoặc gần cuối: *"One quick note — you won't see rosemary on this list. It roots in water, but nearly every grower guide agrees it doesn't thrive there long-term; it wants soil eventually."*

---

## HOOK CHECK

- [x] Có đòn đau / viễn cảnh tương phản? ("cloudy jar, a bad smell, mosquitoes" vs "never smells")
- [x] Có Open Loop / Countdown anchor? ("Seven herbs" + "one simple twice-a-week habit" chưa giải thích)
- [x] 5 từ đầu mạnh? ("This is what everyone's afraid of") — pain statement rõ
- [x] Mini-payoff trước ~20s? "CDC's own mosquito numbers" xuất hiện ở cuối hook (~giây 18-20) — mini-proof sớm, đúng L6 tinh thần dù title không phải dạng "STOP/Never" (pain-removal stack, không bắt buộc L6 nghiêm ngặt)
- [x] **[DATA MODE]** Câu rơi vào `HOOK_DROPOFF_ZONE` (giây 40-55): đoạn "3 mistakes" (giây ~52-70) giữ open loop sống, KHÔNG chuyển sang preview/giới thiệu tại đây — đúng yêu cầu L4

**Kết luận Hook: Pass.**

---

## DNA VOICE AUDIT (theo channel-truth.md)

| Signature required | Có trong script? |
|---|---|
| grandmother-or-failure story | ✅ "Chances are your own grandmother had a jar like this..." (folklore, không phải personal claim) |
| "Here's why this works" + analogy | ✅ "here's why this works: think of that stem like a battery that's already half-charged" |
| exact numbers | ✅ 7-10 ngày, 2 tuần, 4 tuần, $3-4, twice-a-week |
| 3 mistakes | ✅ đúng 3 mistake, đầu video |
| cost comparison DIY vs store | ✅ "$3-4 at the store... wilts within a week" vs "keep producing for months, for free" |
| anonymous social proof | ✅ "folks in our comments section say this is the one that surprises them most" |
| Accessibility Anchors ×2-3 | ✅ "just thirty seconds of your Sunday" (×2), "just one capful" |
| ≥60% contractions + ≥2 idioms + ≥1 folksy marker | ✅ contractions dày đặc ("it's", "don't", "you're"); folksy "folks", "Here's the thing" |
| `Happy gardening.` | ✅ đúng sign-off cuối |

**Human Texture E7:** 0 AI cliché phát hiện (không có delve/leverage/moreover/furthermore/robust/utilize).

**Kết luận DNA Voice: Strong.**

---

## STORYTELLING CRAFT CHECK

- [x] Không có transition "trạm dừng" thuần túy — mọi chuyển đoạn đều có micro-bridge ("That's four down. Number five wants a little more consistency, but it rewards you for it.")
- [x] ≥1 scene documented history: Nathaniel Ward / Wardian Case 1830s — có trong `Story Bank` của research-brief.md (nguồn History.com) → không phải fake witness, PASS
- [x] Mid-video re-hook tại dip zone: "And if you're someone who's forgotten to water a plant more times than you'd like to admit — no judgment here" — đúng vị trí trước NO SMELL SYSTEM (~phút 3.5-4)
- [x] Kết video: identity CTA "you're exactly who this channel is for" (không xin subscribe) + câu hỏi comment geo-specific ("what zone are you gardening in"). Không có next-video loop hứa hão — đúng nguyên tắc (không có kế hoạch thật thì không tease).

**Kết luận: Pass.**

---

## NARRATOR INTEGRITY SCAN

Quét đủ fake-experience blacklist (I've grown/tested/spent/planted/my garden/when I/I remember/for X years/my experience/I personally): **0 vi phạm tìm thấy.** Các câu "I get why...", "I find that oddly comforting", "I'd love to see how it goes for you" là phản ứng/cảm xúc của narrator (Triple F Boost thêm vào), KHÔNG phải hands-on claim — đúng ranh giới cho phép.

**Kết luận: Pass, 0 flags.**

---

## COMPLIANCE FLAG (nhẹ, tham khảo — đã chấm chính thức 10/10 ở bước riêng)

Không phát hiện thêm dấu hiệu nào ngoài những gì `mkt-yt-compliance` đã xử lý (hedge "helping with both problems", "does matter", Pet/Child Safety block 2 tầng plain-water/fertilizer-week). Clean.

---

## LESSONS-LEARNED CHECK (ACTIVE RULES + CR1-CR11)

| Rule | Trạng thái |
|---|---|
| L1 (không exotic plant) | ✅ Pass — 7 herb đều phổ biến ở Mỹ |
| L2 (outcome cụ thể cho counter-intuitive) | ✅ Pass — CDC 7-10 ngày, đổi nước 2x/tuần |
| L3 (deliver title promise <60s) | 🟡 Minor — herb đầu tiên ở ~giây 80 (xem Leak #2) |
| L4 (open loop giây 40-55) | ✅ Pass — "3 mistakes" giữ loop sống đúng vùng |
| L5 (tension mỗi 60-90s ở phút 4-6) | ✅ Pass — NO SMELL SYSTEM đúng phút 4.2-4.8 |
| L6 (bằng chứng trước giây 20 cho claim sốc) | ✅ Pass — "CDC" xuất hiện ~giây 18-20 trong hook |
| L7 (≤10 phút mặc định) | ✅ Pass — ~9.4 phút |
| L8 (pain-removal stack title) | ✅ Pass — "No Soil, No Smell, No Mess" đúng công thức L8 |
| CR2 (nêu tên tất cả item trong preview) | 🔴 Fail — xem Leak #1 |
| CR4 (claim-scoping trung thực) | ✅ Pass — fertilizer/mosquito đều hedge đúng |
| CR5 (safety callout rõ, không chôn vùi) | ✅ Pass — Pet/Child Safety là 1 đoạn riêng, rõ ràng |
| CR6 (cost transparency + value-ratio) | ✅ Pass — $3-4 store vs free |
| CR7 (hero anchor lặp lại) | ✅ Pass — "seven herbs" + hình ảnh lọ xuyên suốt |
| CR9 (sensory close) | 🟡 Nhẹ — kết bài chưa có ẩn dụ giác quan mạnh, chỉ có mantra 3-nhịp (chấp nhận được) |
| AVOID X1-X5 | ✅ Không dính pattern nào |

---

## ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Số liệu cụ thể + cite inline đúng lúc (CDC, extension guide)
- [🟡] Consensus Synthesis: chỉ 1/2 nguyên tắc từ research-brief xuất hiện rõ ràng trong script (xem Leak #3) — chưa đủ 2 câu như khuyến nghị, nhưng không dính pattern slop
- [x] Science moment chốt Action → Benefit (CDC math → lịch đổi nước → không hôi không muỗi)
- [x] Claim-scoping trung thực (fertilizer hedge, mosquito hedge)
- [x] Góc cơ chế độc quyền: kết hợp CDC mosquito life-cycle + extension water-change guidance — 1 kênh AI-slop generic khó tự nghĩ ra phép tính này
- [x] Không dính pattern slop (không có cơ chế giả khoa học, không claim thần kỳ vô căn cứ)

**Kết luận: 5/6 — đủ ngưỡng PUBLISH cho mục này (không 🔴), nhưng Leak #3 là cơ hội cải thiện rẻ.**

---

## ACTIONABLE FIXES (xếp theo tác động)

1. **[Cao]** Sửa câu preview để nêu tên cả 7 herb → mở nhiều open-loop song song (Leak #1, CR2)
2. **[Trung bình]** Thêm 1 câu giải thích ngắn tại sao rosemary bị loại, dùng đúng Consensus Principle #2 từ research-brief (Leak #3)
3. **[Thấp, tùy chọn]** Rút gọn đoạn "3 mistakes" 1 câu để đẩy Mint-reveal lên sớm hơn (Leak #2)
4. **[Thấp, tùy chọn]** Thêm 1 câu ẩn dụ giác quan ở đoạn kết (CR9) thay vì chỉ mantra liệt kê

---

## INLINE TAGS REPORT

Không có `[NEED DATA]` / `[YMYL]` / `[PET-SAFETY]` / `[HEDGE]` / `[COMPLIANCE]` mới phát sinh ngoài những gì đã xử lý ở bước compliance riêng.

---

**Nhắc cuối:** Bật "Altered or synthetic content" khi upload (kênh dùng AI Voice). Producer sign-off trước khi export VoiceAI.
