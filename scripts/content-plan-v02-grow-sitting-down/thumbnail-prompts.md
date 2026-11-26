# Thumbnail Prompts — 7 Plants You Can Grow Sitting Down

**Video title:** 7 Plants You Can Grow Sitting Down | Gardening Over 60
**Title levers:** Kết quả↑ + Công sức↓ (sitting / no bending)
**Thumbnail lever (complementary):** Cảm-giác-chắc-thắng↑ (reassurance — "bad back? you can still do it") — packaging-first, chốt từ outline GATE.
**Formula source:** `references/thumbnail-stats-garden-us-60k.md` (FACELESS 100% · 2-tier YELLOW hook + WHITE sub · listicle → leading-number badge).
**A/B mode:** MODE 1 — Concept test (chưa có A/B result log cho kênh → tìm concept lever lớn). A = Number-badge abundance · B = Before→After verdict. Title GIỮ NGUYÊN.
**Number on thumb:** "7" = seven plants (khớp script ✅, zero hallucination).

---

## Complementarity Test (vs title)
Title content words: 7 · plants · grow · sitting · down · gardening · 60.
- **A text** "BAD BACK?" / "NO BENDING" → bad, back, no, bending = **0 trùng** ✅ (badge "7" = listicle anchor được phép — đúng pattern "20 Perennials" của kênh).
- **B text** "STOP KNEELING" / "DO THIS INSTEAD" → stop, kneeling, do, this, instead = **0 trùng** ✅.

Cả A & B: faceless (no people/face/hands), yellow hook + white sub, ✅/❌ markup, pass guardrails (no human-fear/conspiracy/overclaim; "BAD BACK?" = nói về chính người xem + ✅ reassurance, không fear-monger).

---

## Variant table
| Biến thể | Concept (đòn tâm lý) | Text (vàng / trắng) | Layout | Cảm xúc |
|---|---|---|---|---|
| **A** | Abundance / reassurance | `BAD BACK?` / `NO BENDING` + badge `7` | Single hero + number badge | dư dả, nhẹ nhõm |
| **B** | Verdict / problem→fix | `STOP KNEELING` / `DO THIS INSTEAD` | Before→After ❌\|✅ | dứt khoát, giải pháp |

---

## MASTER PROMPT A — Number-badge abundance (layout listicle WIN)

```
A photorealistic 16:9 YouTube thumbnail for a US senior home-gardening channel, audience 60–80. Vivid saturated colors, ultra high contrast, warm golden afternoon light, blurred green garden background. NO people, no human face, no hands.

SCENE: a waist-high raised garden planter overflowing with ripe red cherry tomatoes, lush green leaf lettuce, strawberries and herbs, brimming over the edge. An empty rustic wooden garden chair sits right beside the planter at the same comfortable height, angled as if ready to be used. Macro abundance, shallow depth of field. A bright YELLOW curved arrow points from the empty chair to the planter, showing easy seated reach.

NUMBER BADGE: a bold number "7" inside a bright YELLOW circle with heavy black outline, top-left corner.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, lower-left in the negative space, NOT covering the planter or chair: line 1 "BAD BACK?" in bright YELLOW, line 2 "NO BENDING" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## MASTER PROMPT B — Before→After verdict (❌ ground bed | ✅ raised + chair)

```
A photorealistic 16:9 YouTube thumbnail for a US senior home-gardening channel, audience 60–80. Vivid saturated colors, ultra high contrast, warm light, blurred garden background. NO people, no human face, no hands.

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the wrong way): a low vegetable garden bed flat on the ground, far down at soil level. A bold red dashed circle around the low bed and a large red ❌ over it.
RIGHT HALF (the fix): a tall waist-high raised planter bursting with ripe cherry tomatoes, leaf lettuce and strawberries, with an empty rustic wooden garden chair beside it at the same height. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered along the bottom, NOT covering the main objects: line 1 "STOP KNEELING" in bright YELLOW, line 2 "DO THIS INSTEAD" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Render command (tùy chọn)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/content-plan-v02-grow-sitting-down/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/content-plan-v02-grow-sitting-down/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
