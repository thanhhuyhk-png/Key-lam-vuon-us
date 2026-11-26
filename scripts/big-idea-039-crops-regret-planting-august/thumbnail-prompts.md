# Thumbnail Prompts — big-idea-039-crops-regret-planting-august

**Title:** 5 Crops You'll Deeply Regret Not Planting in August!
**MODE:** 1 — Concept Test (kênh đang Browse demotion → bắt buộc MODE 1 theo thumbnail-stats)
**Nguồn số:** không dùng số trên thumb (title đã có leading number "5" → thumb tránh lặp, đúng Complementarity Test)

---

## Bảng biến thể

| Biến thể | Concept / Archetype | Cảm-xúc-đích (G4) | Text (vàng/trắng) | Layout | Markup | GURU 5G |
|---|---|---|---|---|---|---|
| **A (từ outline — concept đã khoá tại GATE)** | Curiosity/Reveal — single hero | Tò mò/ngạc nhiên | "SWEETER" (vàng) / "COLD" (trắng) | Single hero object (Layout WIN #2 — layout của champion AVD 49%) | mũi tên cong vàng trỏ giọt sương trên lá | ✅ cả 5 gate (xem dưới) |
| **B (MODE 1 — archetype khác hẳn)** | Verdict/Myth-bust — Before→After | Tiếc nuối → thoả mãn | "TOO SOON" (vàng) / "= BLAND" (trắng) | Before→After split ❌/✅ (Layout WIN #1) | khoanh đỏ nét đứt + ❌ đỏ (trái) · ✅ xanh (phải) | ✅ cả 5 gate (xem dưới) |

**Complementarity Test:** content words thumb A ("sweeter", "cold") và thumb B ("too soon", "bland") — 0 trùng với content words title ("crops", "deeply", "regret", "planting", "august"). PASS cả 2.

**5 GURU-LAYER gate:**
- A: G1 Squint ✅ (2 từ ngắn, chủ thể lá phủ sương chiếm ≥40% khung) · G2 One-Focal ✅ (1 chủ thể duy nhất) · G3 Curiosity-Gap ✅ (gợi cơ chế, không giải thích) · G4 Emotional-Proxy ✅ (giọt sương lấp lánh trên lá xanh = trạng thái "ngạc nhiên") · G5 Pattern-Interrupt ✅ (ánh sương trắng phá vỡ nền xanh đồng nhất của feed làm vườn)
- B: G1 Squint ✅ (2-3 từ/dòng, phía ✅ chiếm ~60% khung) · G2 One-Focal ✅ (không chia 50/50 — phía "after" carrots tươi chiếm phần lớn) · G3 Curiosity-Gap ✅ (không lộ lý do khoa học, chỉ gợi có sai lầm) · G4 Emotional-Proxy ✅ (cà rốt nhổ sớm nhạt màu/héo vs cà rốt phủ sương cam rực) · G5 Pattern-Interrupt ✅ (cam rực tương phản nền xanh)

---

## MASTER PROMPT A

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background with soft golden morning light. NO human face, no full person.

SCENE: ONE single hero object only — an extreme macro close-up of a dark green kale leaf covered in glistening frost crystals and dew droplets, offset to the left side of the frame leaving clean negative space on the right. A bold curved yellow arrow points at the frostiest, most crystalline part of the leaf. Shallow depth of field, background softly blurred dark green and brown garden tones.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline and drop shadow, positioned in the negative space on the right, NOT covering the leaf: line 1 "SWEETER" in bright YELLOW, line 2 "COLD" in WHITE. The ONLY text in the entire image is exactly these two words, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## MASTER PROMPT B

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: a clean before-after split, two halves, RIGHT half visually larger and more dominant than the left (roughly 60/40).
LEFT HALF, smaller (the mistake): a handful of small, pale, dull-orange carrots just pulled from dry summer soil, lying limp on a wooden garden table. A bold red dashed circle around the carrots and a large red X mark over them.
RIGHT HALF, larger and dominant (the payoff): the same type of carrots still in the ground, now vividly deep-orange and glossy, dusted with sparkling frost crystals, a single gloved hand reaching in as a prop to touch one. A bright green checkmark on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline and drop shadow, centered over the left half, NOT covering the carrots: line 1 "TOO SOON" in bright YELLOW, line 2 "= BLAND" in WHITE. The ONLY text in the entire image is exactly these words, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Gate

Bạn muốn:
1. **Render cả 2 ảnh** (tôi chạy script generate.py, xuất `thumbnail-a.png` + `thumbnail-b.png`)
2. Dán 1 trong 2 prompt trên vào tool ảnh khác tự render
3. Đổi concept A hoặc B trước khi render
