# Thumbnail Prompts — Save a Dying Snake Plant in 5 Steps

**Title:** Save a Dying Snake Plant in 5 Steps (Even Soft, Yellow Leaves) | Senior Gardening Tips
**Title lever kéo:** Kết quả↑ (5 steps to save) + Cảm giác chắc thắng↑ ("even soft, yellow leaves")
**MODE:** MODE 1 — Concept Test (bắt buộc, kênh đang Browse demotion từ 29/04, impression thấp → không dùng isolation test)
**Nguồn số/claim:** không có con số cần bake lên thumb (không phải listicle) — chỉ trạng thái cây, khớp script.

---

## Bảng biến thể

| Biến thể | Concept (archetype) | Cảm-xúc-đích (G4) | Text | Layout | Màu chữ | Lever thumb (khác title) | GURU 5G |
|---|---|---|---|---|---|---|---|
| **A** | Verdict / Myth-bust (Before→After) | Thất vọng (❌ rễ đen mềm) → mãn nguyện (✅ rễ trắng khỏe) | "NOT THIRSTY" (vàng) / "IT'S DROWNING" (trắng) | Before→After ❌ | ✅ | Vàng+trắng | Cảm giác chắc thắng↑ qua reveal cơ chế (promise-echo có chủ đích với hook script, không trùng từ với TITLE) | ✅ Pass cả 5 (xem ghi chú dưới) |
| **B** | Curiosity / Question (single-hero) | Lo lắng/tò mò — chưa biết cây còn cứu được không | "IS IT" (vàng) / "STILL ALIVE?" (trắng) | Single hero + mũi tên | Vàng+trắng | Cảm giác chắc thắng↑ qua câu hỏi tình trạng (khác hẳn A — A trả lời reveal, B giữ câu hỏi mở) | ✅ Pass cả 5 (xem ghi chú dưới) |

**Complementarity Test (vs title):** 0 từ trùng với title ở cả A và B ("not thirsty/drowning" và "is it/still alive" đều không xuất hiện trong title). Không cần đánh dấu ECHO với title; A có echo nhẹ với câu mở hook trong script (chủ đích, chấp nhận được theo guardrail promise-echo).

**Ghi chú 5 GURU-gate:**
- **A:** G1 (2 từ/dòng, đọc được ở 200px) ✅ · G2 (before/after lệch 60/40, "after" to & sáng hơn) ✅ · G3 (thumb trả lời 1 phần câu hỏi "vì sao rơi" nhưng KHÔNG trả lời "còn cứu được không" — vẫn còn gap) ✅ · G4 (trạng thái rễ = biểu cảm khuôn mặt faceless) ✅ · G5 (đỏ/xanh chọi nền xanh lá) ✅
- **B:** G1 (2 từ/dòng) ✅ · G2 (1 hero object lệch 1 bên, nền blur) ✅ · G3 (câu hỏi mở hoàn toàn, đáp án nằm trong video) ✅ · G4 (lá mềm úa vàng = trạng thái lo lắng) ✅ · G5 (khoanh đỏ + mũi tên trên nền đất tối tương phản xanh) ✅

---

## MASTER PROMPT A — Verdict / Before→After

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: a clean before-after split, two halves, NOT 50/50 — the right half is visually dominant (about 60% of the frame), brighter and larger than the left.
LEFT HALF (smaller, ~40%, the wrong state): a snake plant pulled out of its pot, roots visibly mushy and black, sitting in dark waterlogged soil. A bold red dashed circle around the blackened root mass and a large red X mark over it.
RIGHT HALF (larger, ~60%, the fix): a healthy snake plant repotted in bright, well-draining soil, roots visibly white and firm, vivid green leaves standing upright. A bright green checkmark on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline and drop shadow, centered in the negative space between the two halves, NOT covering either plant: line 1 "NOT THIRSTY" in bright YELLOW, line 2 "IT'S DROWNING" in WHITE — spelled letter for letter, nothing else.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## MASTER PROMPT B — Curiosity / Single-Hero

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — an extreme close-up of a single hand gently squeezing the soft, yellowed base of a snake plant leaf, dark contrasting soil visible behind it. The hand and leaf are offset to one side of the frame, leaving clean negative space on the other side. A bold red dashed circle around the soft yellowed spot on the leaf base, with a curved yellow arrow pointing at it. Macro shot, shallow depth of field.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline and drop shadow, placed in the negative space, NOT covering the hand or leaf: line 1 "IS IT" in bright YELLOW, line 2 "STILL ALIVE?" in WHITE — spelled letter for letter, nothing else.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no face, no full person, no second object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Ghi chú A/B test

Kênh đang trong Browse demotion (từ 29/04) → theo `thumbnail-stats-garden-us-60k.md`, đây là **MODE 1 bắt buộc** (concept test, không phải isolation): A và B khác hẳn đòn tâm lý (Verdict vs Curiosity), khác ảnh, khác chữ, khác cảm-xúc-đích — đúng cặp mặc định "Verdict × Curiosity" mà file data đề xuất bắt đầu áp dụng. Title giữ nguyên khi chạy YouTube Test & Compare (chỉ đổi thumbnail).

Sau khi có kết quả Test & Compare, ghi lại vào `references/thumbnail-stats-garden-us-60k.md` block `## 🔁 A/B RESULTS LOG` theo format: `[ngày] [slug] [A archetype] vs [B archetype] → WINNER + lý do`.
