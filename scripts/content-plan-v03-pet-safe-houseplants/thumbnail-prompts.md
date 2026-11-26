# Thumbnail Prompts — 9 Houseplants That Won't Hurt Your Cat or Dog

**Video title:** If Your Cat Chews Houseplants, Grow These 9 Instead | Pet Safe Houseplants
**Title levers:** Cảm-giác-chắc-thắng↑ (safe) + Kết quả↑ (9 cây)
**Thumbnail lever (complementary):** A = **loss-aversion/warning** (sago kills) · B = **relief/reassurance** — cả hai KHÁC lever "safe list" của title.
**Formula source:** `references/thumbnail-stats-garden-us-60k.md` (FACELESS = no human face; **thú cưng OK** · 2-tier YELLOW hook + WHITE sub · listicle → leading-number badge · Before→After ❌/✅ = layout AVD cao nhất).
**A/B mode:** MODE 1 — Concept test (A/B log kênh còn trống). A = Warning/Verdict × B = Relief/Curiosity → khác đòn tâm lý rõ. Title GIỮ NGUYÊN.
**⚠️ Correction:** KHÔNG dùng "VET-CHECKED / VET-APPROVED" (research: ASPCA không "approve", chỉ list toxic/non-toxic → overclaim). Đã thay bằng concept dưới.
**Number on thumb:** badge "9" = khớp "9 houseplants" trong script (zero hallucination). Sago = accurate (ASPCA 50% fatal).

---

## Complementarity Test (vs title)
Title content words: if · cat · chews · houseplants · grow · 9 · instead · pet · safe.
- **A** "THIS KILLS" / "THESE DON'T" → this, kills, these, don't = **0 trùng** ✅ (badge "9" = listicle anchor).
- **B** "GO AHEAD" / "LET THEM NIBBLE" → go, ahead, let, them, nibble = **0 trùng** ✅ ("nibble" ≠ "chews"). Badge "9" anchor.

Cả A & B: faceless (no human face/hands — thú cưng được phép), yellow+white 2-tier, guardrails OK ("THIS KILLS" = về CÂY độc giết THÚ, botanical/pet context có nguồn ASPCA — KHÔNG human-fear; và script DELIVER beat sago nên không phải bait).

---

## Variant table
| Biến thể | Concept (đòn tâm lý) | Text (vàng / trắng) | Layout |
|---|---|---|---|
| **A** ⭐ | Warning / loss-aversion (sago) | `THIS KILLS` / `THESE DON'T` + badge `9` | Before→After ❌ sago \| ✅ cat + safe plant |
| **B** | Relief / reassurance (playful) | `GO AHEAD` / `LET THEM NIBBLE` + badge `9` | Single hero: cat + lush safe plant + ✅ |

---

## MASTER PROMPT A — Before→After warning (layout AVD cao nhất kênh)

```
A photorealistic 16:9 YouTube thumbnail for a US senior home-gardening channel, audience 60–80. Vivid saturated colors, ultra high contrast, warm indoor light, blurred living-room background. NO human face, no hands. A pet is allowed.

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the danger): a single sago palm houseplant in a pot — stiff, spiky fern-like fronds. A bold red dashed circle around it and a large red ❌ over it.
RIGHT HALF (safe): a relaxed house cat sitting calmly beside a lush green spider plant in a pot, healthy and full. A bright green ✅ on this side.

NUMBER BADGE: a bold number "9" inside a bright YELLOW circle with heavy black outline, top-right corner (on the safe side).

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered along the bottom, NOT covering the cat or the plants: line 1 "THIS KILLS" in bright YELLOW, line 2 "THESE DON'T" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no human face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no distorted animal anatomy.
```

---

## MASTER PROMPT B — Single-hero relief (playful reassurance)

```
A photorealistic 16:9 YouTube thumbnail for a US senior home-gardening channel, audience 60–80. Vivid saturated colors, ultra high contrast, warm cozy light, blurred home background. NO human face, no hands. A pet is allowed.

SCENE: a happy house cat curled up right next to a lush, leafy green houseplant (a spider plant or a Boston fern) in a nice pot, offset to one side leaving clean negative space. The cat looks relaxed and content. A large bright green ✅ near the plant. Shallow depth of field, inviting and warm.

NUMBER BADGE: a bold number "9" inside a bright YELLOW circle with heavy black outline, top-left corner.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the cat or the plant: line 1 "GO AHEAD" in bright YELLOW, line 2 "LET THEM NIBBLE" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no human face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no distorted animal anatomy.
```

---

## Render command (tùy chọn)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/content-plan-v03-pet-safe-houseplants/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/content-plan-v03-pet-safe-houseplants/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```

---
## Note
> ⚠️ A ("THIS KILLS") = loss-aversion mạnh, CTR cao, NHƯNG lệch tông reassurance của video — chỉ dùng vì script DELIVER beat sago rõ (không bait). Nếu muốn giữ tông ấm/an tâm thuần → ưu tiên B. Đây đúng là câu hỏi MODE 1 cần test.
