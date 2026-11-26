# Thumbnail Prompts — aloe-30-years-biology

**Video title:** Why Grandmother's Aloe Lived 30 Years — It's the Biology
**Format:** Educational / counter-intuitive myth-bust (4 reasons biology)
**Formula source:** `references/thumbnail-stats-garden-us-60k.md`
**A/B MODE:** **MODE 1 — Concept test** (B khác hẳn A: ảnh + chữ + cảm xúc)
**Faceless:** ✅ no people/face/hands · **Title giữ nguyên** khi Test & Compare

## A/B = 2 CONCEPT KHÁC ĐÒN TÂM LÝ
| | 🅰️ Reveal / Reassurance (concept khoá) | 🅱️ Warning / Stat shock |
|---|---|---|
| **Đòn** | Trấn an + lật ngược ("nhăn = TỐT") | Cảnh báo/sốc ("thứ giết nó") |
| **Ảnh** | Single hero: lá aloe nhăn nhưng căng, gel trong lộ ra, bệ cửa ấm + ✅ | Bình tưới đổ nước xối xả lên aloe + ❌ đỏ |
| **Chữ** | `WRINKLED`(vàng) / `= SAVING`(trắng) | `#1 KILLER`(vàng) / `IS WATER`(trắng) |
| **Archetype** | Reveal/Reassurance (single hero) | Warning + Stat shock |

> A = concept đã khoá trong script (packaging-first) · B = góc khác để test.

## Complementarity Test (title words: why·grandmother's·aloe·lived·30·years·biology)
- A: wrinkled·saving → 0 trùng ✅
- B: 1·killer·is·water → 0 trùng ✅

## Số/claim dùng (zero hallucination — có trong script)
- `#1 KILLER IS WATER` = "overwatering is the number-one killer" ✅
- "wrinkled isn't dying, it's surviving" → concept A ✅
- (KHÔNG để "30 YEARS" lên thumb vì trùng title)

---

## 🅰️ Variant A — Reveal / Reassurance (concept khoá: WRINKLED = SAVING)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, warm cozy windowsill background. NO people, no human face, no hands.

SCENE: ONE single hero object only — an extreme close-up of a firm aloe vera leaf that is slightly wrinkled but still healthy, snapped open to reveal the thick clear water-gel inside, glistening. Set on a warm old windowsill. A bright green ✅ check mark in the lower corner. Offset to the right, leaving clean negative space on the left. Macro, shallow depth of field.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, on the left negative space, NOT covering the leaf: line 1 "WRINKLED" in bright YELLOW, line 2 "= SAVING" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

## 🅱️ Variant B — Warning / Stat Shock (#1 killer is water)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred windowsill background. NO people, no human face, no hands.

SCENE: a potted aloe vera plant being over-watered — a watering can pouring a heavy stream of water flooding the pot, water pooling and overflowing, the base of the aloe looking soft and dark. A bold red dashed circle around the soggy soil and a large red ❌ over the watering can.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, on the left, NOT covering the plant: line 1 "#1 KILLER" in bright YELLOW, line 2 "IS WATER" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Vòng lặp A/B
- **Pha 1 (file này):** A (trấn an "nhăn = tốt") vs B (cảnh báo "nước giết nó") → concept nào ăn click + giữ chân hơn.
- **Pha 2 (sau winner):** MODE 2 Isolation — đổi 1 biến (màu/1 từ). Ghi vào `references/thumbnail-stats` → A/B RESULTS LOG.

## Render (khi muốn ảnh)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/aloe-30-years-biology/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/aloe-30-years-biology/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> Chữ baked sai nét → render lại / tối đa 2–3 lần/biến thể.
