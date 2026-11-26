# Thumbnail Prompts — 7 Perennials That Bloom All Summer With Almost No Water | Senior Gardening Tips

## ⚠️ Điều chỉnh so với outline

Outline gốc đề xuất text `SURVIVES 100°F`, nhưng **"100°F" không xuất hiện ở bất kỳ đâu trong script.md** (không loài nào trong 7 loài được nêu số độ chịu nhiệt cụ thể) — vi phạm guardrail "số trên thumb PHẢI khớp script". Đã thay bằng 2 concept dùng đúng số THẬT trong script:
- Số "7" (leading-number, đúng format Listicle theo `thumbnail-stats`)
- "$1,000 a year" (số liệu EPA WaterSense có thật trong script, đoạn cost comparison)

Cũng áp dụng công thức WIN thật của kênh (từ `thumbnail-stats-garden-us-60k.md`, ghi đè skill mặc định): **2 tầng chữ VÀNG (hook) + TRẮNG (phụ), ~4-6 từ**, KHÔNG phải ≤3 từ trắng thuần như outline gợi ý ban đầu.

**Complementarity Test:** cả 2 biến thể — 0 từ trùng nội dung với title ("Perennials/Bloom/Summer/Almost/No/Water/Senior/Gardening/Tips"). Lever thumbnail đều KHÁC lever title (title kéo Kết quả↑+Công sức↓; A kéo Cảm giác-chắc-thắng↑ qua bằng chứng khoa học; B kéo Tiền/mất mát qua so sánh chi phí).

---

## MODE 1 — Concept Test (video mới, chưa có winner riêng cho video này)

| Biến thể | Archetype | Text | Layout | Màu chữ | Cảm xúc |
|---|---|---|---|---|---|
| **A** | Stat/Number (leading-badge, mặc định cho Listicle) | "PROVEN TO SURVIVE" / "EXTREME DROUGHT" + badge "7" | Single hero + leading-number badge | Vàng (hook) + Trắng (phụ) | Cảm giác chắc thắng — bằng chứng khoa học |
| **B** | Verdict (Before→After, layout mạnh nhất data kênh) | "$1,000 A YEAR" / "DOWN THE DRAIN" | Before→After ❌ \| ✅ | Vàng (hook) + Trắng (phụ) | Mất mát/tiền — loss aversion |

---

## MASTER PROMPT A — Leading-Number Badge (Proof/Stat)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background. NO people, no human face, no hands.

SCENE: ONE single hero object only — a vivid Purple Coneflower or Black-Eyed Susan blooming brightly, offset to one side, growing directly out of bone-dry, deeply cracked, sun-baked brown soil (no grass, no other plants). Macro, shallow depth of field, warm natural light.

BADGE: a bold solid YELLOW circle in the top-left corner containing the large black number "7".

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, placed in the negative space, NOT covering the flower or the badge: line 1 "PROVEN TO SURVIVE" in bright YELLOW, line 2 "EXTREME DROUGHT" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

## MASTER PROMPT B — Before→After (Cost/Loss)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background. NO people, no human face, no hands.

LAYOUT: a clean before-after split, two halves.
LEFT HALF (the wrong way): a garden sprinkler head spraying water wastefully across a patch of thirsty green lawn and wilting annual flowers, water visibly pooling on the ground. A bold red dashed circle around the sprinkler head and a large red ❌ over this half.
RIGHT HALF (the fix): one vivid Blanket Flower or Purple Coneflower blooming brightly in bone-dry, deeply cracked soil, no sprinkler or hose anywhere in sight. A bright green ✅ on this half.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered, NOT covering the main objects: line 1 "$1,000 A YEAR" in bright YELLOW, line 2 "DOWN THE DRAIN" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Nguồn số liệu (zero-hallucination check)

- "7" — số loài liệt kê trong script (Black-Eyed Susan, Purple Coneflower, Blanket Flower, Yarrow, Russian Sage, Daylily, Threadleaf Coreopsis).
- "$1,000 A YEAR" — script.md: "The EPA estimates that outdoor watering can run a household over a thousand dollars a year in water costs."
- "PROVEN TO SURVIVE" / "university-tested" framing — script.md: "Every number here is pulled straight from university extension research... not just what looks pretty in a seed catalog."
- "EXTREME DROUGHT" — mô tả chung, khớp chủ đề chính (drought-tolerant), không phải claim số liệu cụ thể.
