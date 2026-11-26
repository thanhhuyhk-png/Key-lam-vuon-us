# Thumbnail Prompts — big-idea-015-milk-jug-watering-safe

**Video title:** The Milk-Jug Watering Trick, Made Safe in 1 Step | Gardening Over 60
**Format:** Myth-bust / Swap (Problem-Fix)
**Formula source:** `references/thumbnail-stats-garden-us-60k.md`
**A/B MODE:** **MODE 1 — Concept test** (B khác hẳn A: ảnh + chữ + cảm xúc)
**Faceless:** ✅ no people/face/hands · **Title giữ nguyên** khi Test & Compare
> ⚠️ Override outline gốc: bỏ "senior hands" → object-only. Giữ ý text khoá "BURY THIS".

## A/B = 2 CONCEPT KHÁC ĐÒN TÂM LÝ
| | 🅰️ Versus / Swap (ý khoá) | 🅱️ Value / Stat (cheap + bền) |
|---|---|---|
| **Đòn** | Đổi cái đúng: chôn clay, bỏ nhựa | Giá trị: $5, dùng nhiều năm |
| **Ảnh** | Before→After: bình nhựa ❌ \| olla đất nung chôn ✅ | Single hero: olla đất nung cắt lớp, nước rỉ xuống rễ |
| **Chữ** | `BURY THIS`(vàng) / `NOT THIS`(trắng) | `$5 SWAP`(vàng) / `LASTS YEARS`(trắng) |
| **Archetype** | Versus/Swap (Before→After) | Stat/Value (single hero) |

## Complementarity Test (title words: the·milk-jug·watering·trick·made·safe·1·step·gardening·over·60)
- A: bury·this·not → 0 trùng ✅
- B: 5·swap·lasts·years → 0 trùng ✅ (tránh "water/watering" — trùng stem title)

## Số dùng (zero hallucination — có trong script)
- `$5 SWAP` = "about five dollars to make" / "five to twelve dollars" ✅
- `LASTS YEARS` = "a waterer you'll use for years"; clay "never breaks down" vs jug "crumbles by August" ✅
- (Không dùng angle "microplastics in your food" — script CỐ TÌNH không doạ; tránh fear-bait/clickbait penalty)

---

## 🅰️ Variant A — Versus / Swap (ý khoá: BURY THIS)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred raised-bed background. NO people, no human face, no hands.

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the old way): an old faded chalky plastic milk jug with a few punched holes, sitting in the dirt, looking brittle. A large red ❌ over it.
RIGHT HALF (the fix): a plain terracotta clay olla pot buried up to its neck in a leafy raised bed, a small stone capping the top. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered over the split, NOT covering the pots: line 1 "BURY THIS" in bright YELLOW, line 2 "NOT THIS" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

## 🅱️ Variant B — Value / Stat (single hero olla, $5 + bền)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden-bed background. NO people, no human face, no hands.

SCENE: ONE single hero object only — a terracotta clay olla pot buried in rich soil, shown as a clean cutaway cross-section so you can see water seeping out through the clay to the plant roots around it. Offset to the right, leaving clean negative space on the left. A curved yellow arrow pointing at the water seeping to the roots. Macro, shallow depth of field.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, on the left negative space, NOT covering the pot: line 1 "$5 SWAP" in bright YELLOW, line 2 "LASTS YEARS" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Vòng lặp A/B
- **Pha 1 (file này):** A (đổi cái đúng: chôn clay) vs B (giá trị: $5 dùng bao năm) → concept nào ăn click + giữ chân hơn.
- **Pha 2 (sau winner):** MODE 2 Isolation — đổi 1 biến. Ghi vào `references/thumbnail-stats` → A/B RESULTS LOG.

## Render (khi muốn ảnh)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-015-milk-jug-watering-safe/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-015-milk-jug-watering-safe/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> Chữ baked sai nét → render lại / tối đa 2–3 lần/biến thể.
