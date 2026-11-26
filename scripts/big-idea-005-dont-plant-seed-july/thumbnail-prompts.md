# Thumbnail Prompts — "1 Paper Towel Reveals If Your Seeds Are Already Dead"

**Mode:** MODE 1 — Concept Test (video mới, chưa có data thumbnail riêng để tinh chỉnh)
**Nguồn công thức:** `references/thumbnail-stats-garden-us-60k.md` (AUDIT TL;DR — data thật, ghi đè giả định cũ)

> ⚠️ Điều chỉnh so với concept gốc ở GATE outline: bỏ "tay người lớn tuổi chỉ vào" — vi phạm luật FACELESS của kênh (tay chỉ = tay làm chủ thể, không phải "phụ trợ cầm dụng cụ"). Thay bằng markup (khoanh đỏ / mũi tên cong) đúng chuẩn kênh. Text giữ tinh thần "còn sống hay đã chết?" nhưng đổi từ ngữ để 0 từ trùng title (title đã có sẵn "Dead", "Seeds", "Paper Towel").

## Lever Value Equation
- **Title đã kéo:** Cảm giác chắc thắng↑ (1 tờ khăn giấy, đơn giản) + Kết quả↑ (biết chắc trước khi mất mùa)
- **Thumbnail kéo lever khác:** tension/nghi ngờ (câu hỏi mở "còn sống không?") — cảm xúc bất định thay vì phát biểu chắc nịch của title

---

## Biến thể A — Verdict / Before→After ❌✅ (layout WIN mạnh nhất kênh)

| | |
|---|---|
| **Archetype** | Verdict / Myth-bust (phán quyết) |
| **Layout** | Before→After split |
| **Text** | Dòng 1 (VÀNG): `STILL ALIVE?` · Dòng 2 (TRẮNG): `HERE'S PROOF` |
| **Cảm xúc** | Nghi ngờ → xác quyết (khoa học) |
| **Complementarity** | 0 từ trùng title ✅ |

**MASTER PROMPT A:**
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden/kitchen background. NO people, no human face, no hands.

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the trap): a handful of ordinary vegetable seeds spilled out of an old, worn seed packet on a wooden kitchen counter — they look completely normal and healthy. A bold red dashed circle around the seeds and a large red ❌ overlay, implying "looks fine" is misleading.
RIGHT HALF (the proof): a single seed resting on a damp paper towel with one tiny white sprouting root visible, macro close-up, shallow depth of field. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, centered in the negative space, NOT covering the main objects: line 1 "STILL ALIVE?" in bright YELLOW, line 2 "HERE'S PROOF" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Biến thể B — Curiosity / Single-hero (đòn tâm lý khác hẳn A)

| | |
|---|---|
| **Archetype** | Curiosity / Question |
| **Layout** | Single hero object + text ở negative space |
| **Text** | Dòng 1 (VÀNG): `ALIVE OR NOT?` · Dòng 2 (TRẮNG): `ONE TEST KNOWS` |
| **Cảm xúc** | Tò mò, hồi hộp |
| **Complementarity** | 0 từ trùng title ✅ |

**MASTER PROMPT B:**
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred kitchen background. NO people, no human face, no hands.

SCENE: ONE single hero object only — a single vegetable seed resting on a damp folded paper towel, macro close-up, offset to one side leaving clean negative space on the other side. A bold red question mark drawn in the air next to the seed, and a curved yellow arrow pointing directly at the seed.

TEXT — render EXACTLY two stacked phrases in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the seed: line 1 "ALIVE OR NOT?" in bright YELLOW, line 2 "ONE TEST KNOWS" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no people, no face, no hands, no second object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Ghi chú số liệu
Không có số cụ thể trên cả 2 thumbnail (không dùng leading-number badge) — layout Before→After và Single-hero không yêu cầu số, tránh rủi ro số bịa.

## Bước tiếp theo
Dán 1 trong 2 prompt vào tool tạo ảnh (Nano Banana Pro / Gemini Flash Image khuyến nghị vì render chữ tốt), xuất 16:9. Hoặc gõ "render A" / "render B" / "render cả 2" để tôi chạy generate.py.
