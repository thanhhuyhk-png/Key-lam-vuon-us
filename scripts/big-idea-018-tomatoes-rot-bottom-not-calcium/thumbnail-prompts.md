# Thumbnail Prompts — big-idea-018 (Tomato Rot Isn't Calcium)

**Title:** Tomato Rot Isn't Calcium — The 1 Watering Fix | Senior Gardening Tips
**Lever title đã kéo:** Công sức↓ (1 fix) + Cảm-giác-chắc-thắng↑ (the real cause)
**Lever thumbnail (bổ trợ, KHÁC title):** A = Verdict/loss ("bạn đang làm SAI") · B = Curiosity ("đáy đen — tại sao?")
**Số trên thumb:** không có số → không bịa (script không có số then chốt dạng badge).

### Complementarity Test (BẮT BUỘC)
- Title content words: `tomato · rot · calcium · watering · fix`
- A text: `WRONG · DO · THIS · INSTEAD` → **0 trùng** ✅
- B text: `BLACK · BOTTOM · HERE'S · WHY` → **0 trùng** ✅
- ⚠️ Cố tình BỎ "NOT CALCIUM" (concept gốc outline) vì "CALCIUM" trùng title = lặp (title đã nói "Isn't Calcium"). Thumbnail mở góc MỚI: "bạn đang fix sai" (A) / "đáy đen, tại sao" (B).

### Bảng biến thể (A/B — MODE 1 Concept test: Verdict × Curiosity)
| Biến thể | Concept (archetype) | Text (hook vàng / phụ trắng) | Layout | Cảm xúc |
|---|---|---|---|---|
| **A** ⭐ | Verdict / Myth-bust | `WRONG!` (vàng) / `DO THIS INSTEAD` (trắng) | Before→After ❌/✅ (WIN, AVD cao nhất kênh) | "Mình đang làm sai → có cách đúng" |
| **B** | Curiosity / Question | `BLACK BOTTOM?` (vàng) / `HERE'S WHY` (trắng) | Single hero macro + khoanh đỏ + mũi tên cong | "Tò mò — sao đáy lại đen?" |

> Cả 2: FACELESS (no people/face/hands làm chủ thể), 2 tầng ALL CAPS vàng+trắng, viền đen + đổ bóng, markup chuẩn kênh, 0 overclaim/conspiracy/human-fear.

---

## MASTER PROMPT A ⭐ (Before→After ❌/✅ — layout WIN của kênh)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, warm natural light, blurred garden background. NO people, no human face, no hands.

LAYOUT: a clean before→after split into two halves with a subtle divider.
LEFT HALF (the wrong way): a small pile of crushed eggshells and a calcium spray bottle next to a ripe red tomato that has a large black, sunken, leathery blossom-end-rot patch on its bottom. A bold red dashed circle around the black rotten patch, and a large red ❌ over this half.
RIGHT HALF (the fix): a metal watering can pouring a steady stream of water onto soil covered with golden straw mulch, beside a flawless glossy red tomato with a clean, healthy bottom. A bright green ✅ on this half.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline and drop shadow, centered between the halves, NOT covering the tomatoes: line 1 "WRONG!" in bright YELLOW, line 2 "DO THIS INSTEAD" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no misspelling.
```

---

## MASTER PROMPT B (Single hero macro — Curiosity, biến thể thử nghiệm khác concept)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, warm natural light, blurred garden background. NO people, no human face, no hands.

SCENE: ONE single hero object only — a perfect glossy red tomato tilted to reveal a large black, sunken, leathery blossom-end-rot patch on its bottom. Macro close-up, shallow depth of field, the tomato offset to the right leaving clean negative space on the left. A bold red dashed circle around the black patch and a curved yellow arrow pointing at it.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline and drop shadow, placed in the left negative space, NOT covering the tomato: line 1 "BLACK BOTTOM?" in bright YELLOW, line 2 "HERE'S WHY" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no second object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no misspelling.
```

---

## Render (tùy chọn)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-018-tomatoes-rot-bottom-not-calcium/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-018-tomatoes-rot-bottom-not-calcium/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> A = layout WIN (khuyến nghị mặc định). B = thử concept curiosity khác đòn tâm lý. Test & Compare trên YouTube, giữ title nguyên.
