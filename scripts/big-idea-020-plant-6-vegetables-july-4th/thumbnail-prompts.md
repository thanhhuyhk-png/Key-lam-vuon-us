# Thumbnail Prompts — big-idea-020 "Plant These 6 After July 4th"

**Title:** Science Says: Plant These 6 After July 4th | Old Fashioned Gardening Tips
**Title lever (Value Equation):** Kết quả↑ (6, second harvest) + Cảm giác chắc thắng↑ (Science Says) + Thời gian↓ (After July 4th)
**Nguồn công thức:** `references/thumbnail-stats-garden-us-60k.md` (data teardown 14 thumbnail thật — GHI ĐÈ skill hardcode)
**A/B mode:** MODE 1 — Concept test (kênh còn ít A/B log) → A = Curiosity/reassurance (concept gốc từ outline GATE) × B = Warning/Stop (zucchini mistake, layout mạnh nhất data: Before→After, AVD 33% winner)

---

## Variant A — "STILL GROWING?" (Curiosity/reassurance, từ outline GATE)

**Archetype:** Curiosity — câu hỏi trấn an, mở loop nhẹ ("mùa chưa hết đâu")
**Layout:** Single hero object + text negative space (TOP_LAYOUTS #2)
**Text:** Tier 1 (VÀNG, hook): `STILL GROWING?` · Tier 2 (TRẮNG, phụ): `SECOND HARVEST!`
**Complementarity check:** Title = science/says/plant/these/6/after/july/4th/old/fashioned/gardening/tips → Thumb = still/growing/second/harvest → **0 từ trùng ✅**
**Lever thumb kéo:** Cảm giác chắc thắng↑ (khác biểu hiện: trấn an thay vì "science proof") — bổ trợ, không lặp lever title.
**Số:** không có số → bỏ qua zero-hallucination check.

### Master Prompt A
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background, warm golden late-afternoon light. NO human face, no full body, no person as main subject.

SCENE: ONE single hero close-up — a weathered hand (auxiliary only, cropped at wrist, not a face or body) pushing small bean seeds into rich dark soil in a raised garden bed. Softly blurred out-of-focus American flag bunting and red-white-blue ribbon decor in the background, hinting at a July 4th setting without being the focus. Shallow depth of field, macro on the soil and seed. The hand and soil are offset to the bottom-right, leaving clean negative space in the upper-left for text.

TEXT — render EXACTLY two stacked words/phrases in very thick bold sans-serif, heavy black outline + drop shadow, positioned in the upper-left negative space, NOT covering the hand or soil: line 1 "STILL GROWING?" in bright YELLOW, line 2 "SECOND HARVEST!" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

A curved cyan arrow points from the text down toward the seed being planted.

Negative: no human face, no full body, no second person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Variant B — "ONE MISTAKE KILLS YOUR CROP" (Warning/Stop, zucchini payoff)

**Archetype:** Warning/Stop — layout Before→After, pattern mạnh nhất data (AVD 33% ⭐ "Rooting Cuttings")
**Layout:** Before→After split ❌/✅ (TOP_LAYOUTS #1)
**Text:** Tier 1 (VÀNG, hook): `ONE MISTAKE` · Tier 2 (TRẮNG, phụ): `KILLS YOUR CROP`
**Complementarity check:** Thumb = one/mistake/kills/your/crop → **0 từ trùng với title ✅**; cũng không trùng chữ Variant A (still/growing/second/harvest) ✅
**Nội dung neo script:** squash vine borer đẻ trứng cuối tháng 6–đầu tháng 7 vào cây bí đã trồng từ mùa xuân → mục 4 script ("the plant almost every gardener already has growing right now"). Số ngày/borer timing đã verified trong research-brief — không bịa.
**Lever thumb kéo:** Cảm giác chắc thắng↑ qua đòn LOSS AVERSION (khác hẳn đòn "trấn an" của A) — 2 concept khác đòn tâm lý theo yêu cầu MODE 1.

### Master Prompt B
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background, natural daylight. NO people, no human face, no hands — object-driven, faceless.

LAYOUT: a clean before-after split, two halves, divided by a thin vertical line.
LEFT HALF (the mistake): a wilting zucchini/squash plant stem at soil level with a small ragged hole and sawdust-like frass near the base (squash vine borer damage), surrounding leaves drooping and yellowing. A bold red dashed circle around the hole in the stem, and a large red "❌" symbol over this half.
RIGHT HALF (the fix): a fresh, healthy young zucchini seedling with vivid deep-green leaves growing in the same style raised garden bed, thriving. A bright green "✅" symbol over this half.

TEXT — render EXACTLY two stacked words/phrases in very thick bold sans-serif, heavy black outline + drop shadow, centered at the top, NOT covering the plants: line 1 "ONE MISTAKE" in bright YELLOW, line 2 "KILLS YOUR CROP" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Guardrail check (cả 2 biến thể)
- ✅ Faceless (A: chỉ tay phụ trợ cầm hạt giống, không mặt/thân — khớp data "tay đôi khi xuất hiện như phụ trợ"; B: hoàn toàn object-driven, không người)
- ✅ Không overclaim/conspiracy/100%/guaranteed
- ✅ Botanical shock OK (squash vine borer damage — vật thể, không phải human-fear)
- ✅ Số: không có số bịa trên cả 2 biến thể
- ✅ Complementarity: 0 từ trùng title ở cả A và B
- ✅ MODE 1: A (Curiosity/reassurance) và B (Warning/Stop) khác hẳn concept + ảnh + chữ + cảm xúc

## Ghi vào A/B RESULTS LOG sau khi publish
Sau khi có data thật (CTR/AVD), điền vào `references/thumbnail-stats-garden-us-60k.md` block `## 🔁 A/B RESULTS LOG`:
`[ngày] big-idea-020 Curiosity "STILL GROWING?/SECOND HARVEST!" vs Warning "ONE MISTAKE/KILLS YOUR CROP" → WINNER + AVD/CTR + bài học`
