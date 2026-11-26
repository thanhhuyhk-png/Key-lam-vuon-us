# Thumbnail Prompts — video-101-avocado-from-seed

**Video title:** 5 Things Nobody Tells You About Growing Avocado From Seed
**Format:** Listicle / myth-bust hybrid
**Formula source:** `references/thumbnail-stats-garden-us-60k.md`
**A/B MODE:** **MODE 1 — Concept test** (B khác hẳn A: ảnh + chữ + cảm xúc)
**Faceless:** ✅ no people/face/hands · **Title giữ nguyên** khi Test & Compare
> ⚠️ Override outline gốc: bỏ "senior hands" → object-only theo formula WIN.

## A/B = 2 CONCEPT KHÁC ĐÒN TÂM LÝ
| | 🅰️ Value / Transformation | 🅱️ Stat / Time Shock |
|---|---|---|
| **Đòn** | Tiếc của → cây miễn phí | Sốc/khó tin |
| **Ảnh** | Before→After: hạt sắp vứt ❌ \| chậu avocado xanh tốt ✅ | Single hero: 1 hạt nảy mầm thành cây non bên cửa sổ |
| **Chữ** | `TRASH?`(vàng) / `OR FREE PLANT`(trắng) | `13 YEARS?!`(vàng) / `NO FRUIT`(trắng) |
| **Archetype** | Versus/Value (Before→After) | Stat/Number shock (single hero) |

## Complementarity Test (title words: 5·things·nobody·tells·growing·avocado·seed)
- A: trash·or·free·plant → 0 trùng ✅
- B: 13·years·no·fruit → 0 trùng ✅

## Số dùng (zero hallucination — đều có trong script)
- `13 YEARS?!` = "five to thirteen years before it even flowers" ✅
- `NO FRUIT` = "may never, ever fruit"; gardener 15 năm không quả ✅
- `FREE PLANT` = houseplant store $15–30 vs "costs you the price of the lunch" ✅

---

## 🅰️ Variant A — Value / Transformation (Before→After)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred kitchen-and-windowsill background. NO people, no human face, no hands.

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the waste): a brown avocado pit and scooped-out avocado skins sitting in a kitchen scrap bowl over a trash can, dull and about to be thrown away. A large red ❌ over the trash.
RIGHT HALF (the payoff): a lush, glossy, deep-green potted avocado houseplant thriving on a bright sunny windowsill. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, centered over the split, NOT covering the plant: line 1 "TRASH?" in bright YELLOW, line 2 "OR FREE PLANT" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

## 🅱️ Variant B — Stat / Time Shock (single hero)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred bright-window background. NO people, no human face, no hands.

SCENE: ONE single hero object only — a sprouted avocado pit that has grown into a tall thin young seedling with a few glossy green leaves, planted in a small pot (or glass) on a sunny windowsill, offset to the right, leaving clean negative space on the left. A bold curved yellow arrow pointing up the skinny single stalk. Macro, shallow depth of field.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, on the left negative space, NOT covering the seedling: line 1 "13 YEARS?!" in bright YELLOW, line 2 "NO FRUIT" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Vòng lặp A/B
- **Pha 1 (file này):** A (value/transformation) vs B (stat shock) → concept nào ăn click + giữ chân hơn.
- **Pha 2 (sau khi có winner):** MODE 2 Isolation — giữ concept thắng, đổi 1 biến (màu/1 từ). Ghi kết quả vào `references/thumbnail-stats` → A/B RESULTS LOG.

## Render (khi muốn ảnh)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/video-101-avocado-from-seed/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/video-101-avocado-from-seed/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> Chữ baked sai nét → render lại / tối đa 2–3 lần/biến thể.
