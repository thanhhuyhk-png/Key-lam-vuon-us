# Thumbnail Prompts — big-idea-014-no-bend-raised-bed-build

**Video title:** Build a No-Bend Raised Bed for Under $50
**Format:** Dollar-Value / Build (Problem-Fix)
**Formula source:** `references/thumbnail-stats-garden-us-60k.md`
**A/B MODE:** **MODE 1 — Concept test** (B khác hẳn A: ảnh + chữ + cảm xúc)
**Faceless:** ✅ no people/face/hands · **Title giữ nguyên** khi Test & Compare
> ⚠️ Override outline gốc: bỏ "senior đứng thẳng" → object-only theo formula WIN. Giữ ý "WAIST-HIGH" (chiều cao title không nói).

## A/B = 2 CONCEPT KHÁC ĐÒN TÂM LÝ
| | 🅰️ Ergonomic / Benefit (ý khoá) | 🅱️ Money / Versus ($ shock) |
|---|---|---|
| **Đòn** | Thoải mái: đứng thẳng, hết cúi | Tiền: đừng trả $300 |
| **Ảnh** | Luống cao ngang hông đầy rau xanh, bệ cao = counter + ✅ | Before→After: luống store $300 ❌ \| luống DIY ✅ |
| **Chữ** | `WAIST-HIGH`(vàng) / `STAND UP`(trắng) | `$300?`(vàng) / `OR DIY`(trắng) |
| **Archetype** | Reveal/Benefit (single hero) | Versus/Value (Before→After) |

## Complementarity Test (title words: build·no-bend·raised·bed·under·$50·50)
- A: waist·high·stand·up → 0 trùng ✅
- B: 300·or·diy → 0 trùng ✅ (KHÔNG để "$50" lên thumb — trùng title)

## Số dùng (zero hallucination — có trong script)
- `$300` = "two, even three hundred dollars" (giá store) ✅
- `OR DIY` / DIY bed = build under $50 với gỗ tái chế + false bottom ✅
- Chiều cao 30–36 inch ("kitchen counter height") → cue WAIST-HIGH ✅

---

## 🅰️ Variant A — Ergonomic / Benefit (ý khoá: WAIST-HIGH)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, sunny backyard background. NO people, no human face, no hands.

SCENE: a tall waist-high wooden raised garden bed on sturdy legs, the top at about kitchen-counter height, overflowing with lush green lettuce and herbs. Shot from a low angle to emphasize how TALL it stands, so you would not have to bend to reach it. A bright green ✅ in a lower corner. Clean negative space on the left.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, on the left, NOT covering the bed: line 1 "WAIST-HIGH" in bright YELLOW, line 2 "STAND UP" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

## 🅱️ Variant B — Money / Versus ($300 vs DIY, Before→After)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred backyard background. NO people, no human face, no hands.

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the expensive way): a shiny brand-new store-bought elevated garden bed with a price-tag look, dull and pricey. A large red ❌ over it.
RIGHT HALF (the smart way): a rustic DIY waist-high raised bed built from reclaimed fence boards, full of healthy green vegetables. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered over the split, NOT covering the beds: line 1 "$300?" in bright YELLOW, line 2 "OR DIY" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Vòng lặp A/B
- **Pha 1 (file này):** A (đứng thẳng, hết cúi) vs B (đừng trả $300) → đòn nào ăn click + giữ chân hơn (comfort vs money).
- **Pha 2 (sau winner):** MODE 2 Isolation — đổi 1 biến. Ghi vào `references/thumbnail-stats` → A/B RESULTS LOG.

## Render (khi muốn ảnh)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-014-no-bend-raised-bed-build/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-014-no-bend-raised-bed-build/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> Chữ baked sai nét → render lại / tối đa 2–3 lần/biến thể.
