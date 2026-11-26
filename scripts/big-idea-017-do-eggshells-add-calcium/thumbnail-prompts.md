# Thumbnail Prompts — big-idea-017-do-eggshells-add-calcium

**Video title:** Do Eggshells Really Add Calcium? What Science Found | Gardening Over 60
**Formula source:** `references/thumbnail-stats-garden-us-60k.md`
**A/B MODE:** **MODE 1 — Concept test** (kênh còn non → tìm concept lever lớn; B khác hẳn A về ảnh+chữ+cảm xúc, cả hai on-formula)
**Faceless:** ✅ no people/face/hands · **Title giữ nguyên** (YouTube Test & Compare chỉ đổi thumbnail)

## A/B = 2 CONCEPT KHÁC HẲN
| | 🅰️ Verdict / Before→After | 🅱️ Curiosity / Question |
|---|---|---|
| **Cảm xúc** | Phán quyết (loss/warning) | Tò mò (mở vòng lặp) |
| **Ảnh** | Split: vỏ trứng ❌ \| tưới ✅ | Single hero: 1 hũ vỏ trứng + dấu **?** |
| **Chữ** | `MYTH` (vàng) / `BUSTED` (trắng) | `DOES IT` (trắng) `WORK?` (vàng) |
| **Layout WIN** | ① Before→After (AVD top kênh) | ② Single hero + markup |

## Complementarity Test (cả 2)
- Title words: eggshells·really·add·calcium·science·found·gardening
- A: myth·busted = 0 trùng ✅ · B: does·it·work = 0 trùng ✅ (tránh "really" vì title đã có)

---

## 🅰️ Variant A — Before→After Verdict (layout WIN, vàng+trắng)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background. NO people, no human face, no hands.

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the wrong way): a pile of crushed white eggshells on dark soil and a ripe red tomato with an ugly sunken black blossom-end-rot patch. A bold red dashed circle around the eggshells and a large red ❌ over them.
RIGHT HALF (the fix): a watering can pouring a steady stream of water onto a healthy tomato plant with straw mulch over the soil, and a flawless ripe red tomato. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, centered, NOT covering the tomatoes: line 1 "MYTH" in bright YELLOW, line 2 "BUSTED" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

## 🅱️ Variant B — Curiosity / Question (concept KHÁC: single hero + dấu hỏi)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background. NO people, no human face, no hands.

SCENE: ONE single hero object only — a clear glass jar full of crushed white eggshells resting on dark rich garden soil, offset to the right, leaving clean dark negative space on the left. A bold bright red question-mark drawn large next to the jar. Macro, shallow depth of field.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, on the left negative space, NOT covering the jar: line 1 "DOES IT" in WHITE, line 2 "WORK?" in bright YELLOW.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no second object, no tomato, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Vòng lặp A/B (2 pha)
- **Pha 1 (file này):** test A (verdict) vs B (curiosity) → concept nào ăn click hơn cho kênh.
- **Pha 2 (sau khi có winner):** chuyển MODE 2 Isolation — giữ concept thắng, đổi 1 biến (vàng vs trắng, 1 từ) để tinh chỉnh.

## Render
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-017-do-eggshells-add-calcium/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-017-do-eggshells-add-calcium/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> Chữ baked sai nét → render lại / tối đa 2–3 lần/biến thể. Sai dai dẳng → render nền KHÔNG chữ + overlay chữ thủ công (Canva).
