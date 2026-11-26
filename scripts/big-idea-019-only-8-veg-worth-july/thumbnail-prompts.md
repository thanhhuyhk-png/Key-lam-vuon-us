# Thumbnail Prompts — big-idea-019-only-8-veg-worth-july

**Video:** The Only 8 Vegetables Worth Planting in July | Gardening Over 60
**Concept khoá tại GATE outline (packaging-first):** frost-deadline / "BEAT THE FROST" — bổ trợ title (title lo "8 rau", thumb lo "đồng hồ frost đếm ngược").
**A/B mode:** MODE 1 — Concept test (A Verdict/Before→After × B Curiosity/single-hero). Title giữ nguyên.
**Faceless:** yes (no people/face/hands). **Số bịa:** không (không bake chữ số nào → cũng tránh trùng "8" của title).

## Complementarity Test (BẮT BUỘC)
- Title content words: Only · 8 · Vegetables · Worth · Planting · July · Gardening · Over · 60.
- **A text:** BEAT · FROST · BEFORE · TOO · LATE → 0 từ trùng ✅
- **B text:** ONE · NUMBER · DECIDES · ALL → 0 từ trùng ✅
- Lever: title kéo *Kết quả↑ + Chắc-thắng↑ (đã lọc sẵn)*; thumbnail kéo lever KHÁC = *Thời gian↓ / urgency (frost clock)* ✅

| Biến thể | Concept (đòn tâm lý) | Text (hook vàng / phụ trắng) | Layout | Cảm xúc |
|---|---|---|---|---|
| **A** ⭐ | Verdict / loss | BEAT THE FROST / BEFORE IT'S TOO LATE | Before→After ❌/✅ | khẩn cấp, "kẻo mất trắng" |
| **B** | Curiosity / secret | ONE NUMBER / DECIDES IT ALL | Single-hero calendar + arrow | tò mò, "con số nào?" |

---

## MASTER PROMPT A ⭐ (Before→After — layout WIN, AVD-cao-nhất của kênh)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 60 to 80. Vivid saturated colors, ultra high contrast, warm natural light, blurred vegetable-garden background. NO people, no human face, no hands.

LAYOUT: a clean before-after split, two equal halves divided down the middle.
LEFT HALF (too slow, it fails): a single unripe green tomato and a small green pepper still hanging on the vine, dusted with white frost, leaves wilting and greyed. A bold red dashed circle around the frost-bitten fruit, and a large red cross mark X over this half.
RIGHT HALF (still in time, it wins): a vibrant freshly pulled bunch of red radishes and crisp green bush beans piled on dark rich soil, glistening, healthy, backlit. A bright green check mark on this half.

TEXT — render EXACTLY two stacked lines, very thick bold sans-serif, heavy black outline plus drop shadow, centered in the lower third, NOT covering the main objects: line 1 "BEAT THE FROST" in bright YELLOW, line 2 "BEFORE IT'S TOO LATE" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI text, no distorted shapes, no blurry text.
```

## MASTER PROMPT B (Single-hero curiosity — đổi concept để test)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 60 to 80. Vivid saturated colors, ultra high contrast, warm natural light, blurred vegetable-garden background. NO people, no human face, no hands.

SCENE: ONE single hero object — a paper wall calendar standing on dark garden soil, offset to the RIGHT, leaving clean empty negative space on the LEFT. One square on the calendar is circled thickly in red, and a big curved red arrow sweeps toward it like a countdown clock. A few fresh red radishes rest at the base for garden context. Macro, shallow depth of field, dramatic warm light.

TEXT — render EXACTLY two stacked lines, very thick bold sans-serif, heavy black outline plus drop shadow, placed in the LEFT negative space, NOT covering the calendar: line 1 "ONE NUMBER" in bright YELLOW, line 2 "DECIDES IT ALL" in WHITE.
Do NOT add any other overlay text, words, captions, labels or watermark. The calendar may show a plain blank grid with no legible words.

Negative: no people, no face, no hands, no second calendar, no legible fine print, no extra overlay text, no gibberish letters, no watermark, no logo, no distorted shapes, no blurry text.
```

---

## Render (tùy chọn)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-019-only-8-veg-worth-july/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-019-only-8-veg-worth-july/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> Chữ baked sai nét → render lại / rút gọn text (max 2–3 lần/biến thể). Sai dai dẳng → render nền KHÔNG chữ + overlay Canva thủ công.
