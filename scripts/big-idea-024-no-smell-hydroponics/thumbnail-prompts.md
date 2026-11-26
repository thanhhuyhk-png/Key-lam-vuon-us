# Thumbnail Prompts — Grow 7 Herbs in Water (No Soil, No Smell, No Mess)

**Nguồn công thức:** `references/thumbnail-stats-garden-us-60k.md` (AUDIT TL;DR — override skill mặc định)
**Concept A:** đã chốt tại GATE outline (packaging-first) — dùng nguyên, chỉ verify + build prompt
**Mode A/B:** MODE 1 — Concept Test (video chưa có thumbnail thắng riêng để isolation-test)

---

## Bảng biến thể

| Biến thể | Concept | Text (hook vàng / phụ trắng) | Layout | Lever | Cảm xúc |
|---|---|---|---|---|---|
| **A** | Single hero (layout #2 — khớp champion AVD 49%) — PROMISE-ECHO | `NO SMELL` (vàng) / `NO SOIL` (trắng) | Single hero object + negative space | Công sức↓ (echo title) | Yên tâm / giải pháp |
| **B** | Before→After (đánh trúng objection #1 trực diện) | `STINKY?` (vàng) / `NOT ANYMORE` (trắng) | Before→After ❌/✅ | Cảm giác chắc thắng↑ | Tò mò → nhẹ nhõm |

**Complementarity check:**
- A = `ECHO` (lặp có chủ đích 2 từ từ title "No Smell"/"No Soil" — cho phép theo `PROMISE_ECHO` rule 2026-07-04, vì mục tiêu là hút ĐÚNG audience quan tâm objection này, không phải tò mò thuần)
- B = 0 từ trùng title → pass Complementarity chuẩn

**Guardrail check (cả 2):** không 100%/conspiracy/human-fear · faceless (no face, no full person; tay-prop OK) · không động vật đe dọa · số: không có số cần bake (video không claim số cụ thể trên thumb) · chữ 2 tầng ALL CAPS ~2-4 từ/dòng ✅

---

## MASTER PROMPT A — Single Hero (Promise-Echo, khớp champion layout)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, warm natural light, blurred kitchen/windowsill background. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — a clear glass jar filled with clean, crystal-clear water, sitting on a bright windowsill, with a fresh herb cutting inside showing vivid white healthy roots clearly visible through the glass. The jar is offset to one side, leaving clean negative space on the other side for text. Optionally, a single hand is gently holding the jar as a prop (no face, no full person). Macro-ish framing, shallow depth of field, roots in sharp focus.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, centered in the negative space, NOT covering the jar or roots: line 1 "NO SMELL" in bright YELLOW, line 2 "NO SOIL" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no cloudy or murky water in this scene.
```

---

## MASTER PROMPT B — Before→After (đánh trúng objection trực diện)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred kitchen background. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: a clean before-after split, two halves, divided by a subtle vertical line.
LEFT HALF (the fear): a glass jar with cloudy, murky, algae-tinted water and a wilting plant stem inside, looking neglected and unappealing. A bold red dashed circle around the murky water and a large red ❌ over it.
RIGHT HALF (the reality): a glass jar with crystal-clear water and a healthy herb cutting showing bright white roots, on a sunny windowsill. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, centered across the top, NOT covering either jar: line 1 "STINKY?" in bright YELLOW, line 2 "NOT ANYMORE" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Ghi chú số liệu
Không có số cụ thể cần bake lên thumbnail cho video này (không claim "X ngày" hay "$X" trên thumb) — an toàn zero-hallucination.
