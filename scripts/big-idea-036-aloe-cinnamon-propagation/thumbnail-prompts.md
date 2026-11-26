# Thumbnail Prompts — Why Most Aloe Leaf Cuttings Fail (And What Actually Fixes It)

**Nguồn concept:** outline.md GATE 1 (packaging-first) — lever gốc "quế không phải hormone" giữ nguyên, chỉ tách lại thành 2 tầng chữ theo công thức WIN thật của kênh (`thumbnail-stats-garden-us-60k.md`), thay vì "NOT A HORMONE" 1 dòng ≤3 từ (rule cũ của outline skill, đã bị data ghi đè).

**Mode đã chọn: MODE 1 — Concept Test (bắt buộc).** Kênh đang trong Browse demotion (channel-truth.md, từ ~29/04) → theo skill, KHÔNG dùng Mode 2 isolation. A và B là 2 archetype khác hẳn nhau: **Verdict/Myth-bust (Before→After ❌/✅)** vs **Curiosity/Question (single-hero)**.

**Số liệu dùng:** không có số cụ thể trên thumb (script không có con số % thành công — đúng, vì research-brief đánh dấu NEED DATA cho tỷ lệ %, không bịa lên thumbnail).

---

## Bảng biến thể

| Biến thể | Concept/Archetype | Cảm-xúc-đích (G4) | Text (vàng/trắng) | Layout | GURU 5G |
|---|---|---|---|---|---|
| **A** | Verdict / Myth-bust | Sốc nhẹ + thoả mãn (đúng-sai rõ ràng) | Vàng: `GRANDMA'S TRICK` · Trắng: `NOT A HORMONE` | Before→After ❌/✅ | ✅ G1 (vàng 2 từ/dòng, chủ thể to) · ✅ G2 (bên phải "sau" nổi hơn 60/40) · ✅ G3 (chưa nói TẠI SAO nó vẫn có tác dụng — giữ trong video) · ✅ G4 (chai hormone ❌ vs rễ trắng ✅ = trạng thái vật thể tải cảm xúc) · ✅ G5 (quế nâu cam + ❌ đỏ phá nền xanh) |
| **B** | Curiosity / Question | Tò mò, hoài nghi ("liệu có thật không?") | Trắng: `DOES CINNAMON` · Vàng: `WORK?` | Single-hero + dấu hỏi đỏ | ✅ G1 (hook 1 từ "WORK?") · ✅ G2 (1 chủ thể duy nhất, lệch khung) · ✅ G3 (không trả lời Có/Không) · ✅ G4 (ánh sáng kịch tính lên đầu lá phủ quế = "đang bị điều tra") · ✅ G5 (mũi tên vàng cong + dấu hỏi đỏ phá nền xanh) |

**Complementarity Test:** content words thumbnail (grandma, trick, hormone, cinnamon, work) — **0 trùng** với content words title (most, aloe, leaf, cuttings, fail, actually, fixes). PASS cả 2 biến thể. (Chủ động tránh "FIX/FIXES" trùng title.)

---

## MASTER PROMPT A — Verdict / Before→After ❌/✅

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background, warm natural light. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: a clean before→after split, two halves, right half slightly more dominant (about 60/40).
LEFT HALF (the wrong belief, smaller/dimmer): a dried aloe leaf tip dusted with cinnamon powder, sitting next to a small commercial rooting-hormone bottle. A bold red dashed circle around the rooting-hormone bottle and a large red ❌ over it.
RIGHT HALF (the real fix, larger/brighter): the same dried aloe leaf tip now nestled shallow in coarse sand and light soil, with thin white roots visibly emerging from its base. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, centered in the negative space, NOT covering the main objects: line 1 "GRANDMA'S TRICK" in bright YELLOW, line 2 "NOT A HORMONE" in WHITE. The ONLY text in the entire image is these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no snakes or threatening animals.
```

---

## MASTER PROMPT B — Curiosity / Single-Hero Question

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background, dramatic warm light. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — a macro close-up of a dried aloe leaf tip freshly dusted with cinnamon powder, offset to one side of the frame, leaving clean negative space on the other side. A bold red question mark drawn near the leaf tip, and a curved yellow arrow pointing at the cinnamon-dusted cut end. Shallow depth of field, dramatic spotlight on the leaf tip.

TEXT — render EXACTLY this short question in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the object: "DOES CINNAMON" in WHITE, "WORK?" in bright YELLOW. The ONLY text in the entire image is these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no second object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no snakes or threatening animals.
```

---

## Guardrail check (cả 2 biến thể)
- ✅ Faceless (no face/full person) — chỉ vật thể
- ✅ Không động vật đe doạ làm hero
- ✅ Không overclaim/conspiracy ("100%", "GUARANTEED", "SHOCKING" — không dùng)
- ✅ Không human-fear ("TOXIC/DEADLY/POISON" — không dùng; botanical/product shock OK: ❌ trên chai hormone)
- ✅ Không số bịa (script không có % cụ thể → thumbnail cũng không bịa số)
- ✅ Lever Value Equation thumbnail khác title: title kéo Cảm-giác-chắc-thắng↑+Công-sức↓; thumbnail kéo **Kết quả↑/Cảm-giác-chắc-thắng↑ qua tiết lộ chi tiết cụ thể (hormone/cinnamon)** mà title chưa nói ra

---

Bạn muốn:
1. **Render cả 2 ảnh** ngay bằng script generate.py (nano, 16:9, 2K)?
2. Chỉ render 1 biến thể (A hoặc B)?
3. Sửa text/concept trước khi render?
