# Thumbnail Prompts — You're Pulling $6 Salad: 7 Yard Weeds That Beat Store Greens

> Concept lõi khoá từ outline.md (packaging-first, GATE 1): chủ thể **Purslane vs Fish/Fish-Oil**, lever thumbnail = **Cảm giác chắc thắng↑/Reveal** (khác lever title = Tiền/Value). Đã format lại text từ "MORE THAN FISH" (1 tầng cũ) sang chuẩn 2 tầng vàng+trắng theo `thumbnail-stats-garden-us-60k.md` (data thật, ghi đè công thức cũ).
> Kênh đang **Browse demotion** (KPI view 5-ngày-đầu <500) → bắt buộc **MODE 1 (Concept Test)**: A & B khác đòn tâm lý rõ (Verdict/Reveal × Curiosity/Question), không phải chỉnh 1 biến.
> Số liệu nguồn: script.md item Purslane — "more omega-3s than any other leafy green... one of the only land plants ever found to carry a trace of EPA, the exact omega-3 usually found in fish oil capsules" (nguồn 2014 peer-reviewed, xem research-brief.md addendum).

---

## Bảng biến thể

| Biến thể | Concept/Archetype | Cảm-xúc-đích (G4) | Text (vàng/trắng) | Layout | GURU 5G |
|---|---|---|---|---|---|
| **A** | Verdict / Stat-Reveal | Kinh ngạc, không-tin (purslane tươi rực rỡ vs viên dầu cá nhàm chán, y tế) | `MORE OMEGA-3` (vàng) / `THAN FISH OIL!` (trắng) | Single-hero (layout WIN #2 — layout champion AVD 49%) + mũi tên cong vàng trỏ purslane | ✅ G1 (2+3 từ/dòng, đọc được 200px) · ✅ G2 (purslane ~65% khung, lọ dầu cá nhỏ/mờ ~35%) · ✅ G3 (nêu SO SÁNH, giấu SỐ+CƠ CHẾ — video mới trả lời) · ✅ G4 (như trên) · ✅ G5 (lọ dầu cá bạc/trắng phá vỡ tông xanh-lá toàn feed) |
| **B** | Curiosity / Question | Tò mò, hoài nghi ("thật không?") | `BEATS FISH?` (vàng) / `FOR FREE` (trắng) | Single-hero + dấu `?` đỏ lớn giữa 2 vật thể (purslane vs cá tươi thật, khác A dùng lọ dầu cá) | ✅ G1 (2+2 từ/dòng) · ✅ G2 (purslane chiếm ưu thế ~60%, cá lệch góc ~40%, mờ hơn) · ✅ G3 (câu hỏi mở, KHÔNG tự trả lời) · ✅ G4 (như trên) · ✅ G5 (da cá bạc-xám tương phản mạnh với lá xanh-đỏ purslane) |

**Complementarity check:** Content words A ("omega-3/fish oil") và B ("beats/fish/free") — **0 từ trùng lõi** với title ("pulling/salad/yard weeds/store greens/beat store greens"). Cả 2 biến thể pass, không cần đánh dấu ECHO.

---

## MASTER PROMPT A — Verdict / Stat-Reveal

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred garden background with warm natural light. NO human face, no full person.

SCENE: ONE dominant hero object — a fresh, glossy purslane sprig with reddish succulent stems and plump green leaves, filling about 65% of the frame, offset to the left, in sharp macro focus. To the right, smaller and slightly blurred, a small glass bottle of fish oil capsules (amber glass, visible golden gel capsules) sits in soft-focus negative space. A bold curved yellow arrow points from the fish oil bottle toward the purslane sprig.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, positioned in the negative space on the right side, NOT covering the purslane: line 1 "MORE OMEGA-3" in bright YELLOW, line 2 "THAN FISH OIL!" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no snake or threatening animal.
```

---

## MASTER PROMPT B — Curiosity / Question

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred kitchen-counter/garden background with natural light. NO human face, no full person.

SCENE: TWO objects in visual tension — on the left, a fresh glossy purslane sprig with reddish stems and plump green leaves, large and sharp, filling about 60% of the frame. On the right, a single small whole fresh fish (silver-scaled, on a wooden cutting board), smaller and slightly softer focus, filling about 40% of the frame. Between them, a large bold red question mark "?" drawn in thick marker style, creating visual tension between the two objects.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, positioned in the negative space above or below the objects, NOT covering either object: line 1 "BEATS FISH?" in bright YELLOW, line 2 "FOR FREE" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no snake or threatening animal.
```

---

## Ghi chú render
- Cả 2 prompt đã khoá chính tả từng dòng chữ + negative list đầy đủ theo chuẩn skill (chống AI méo chữ khi bake trong 1 lần render).
- Nếu chữ bake sai sau 3 lần thử: rút "MORE OMEGA-3" → "OMEGA-3" (1 từ) hoặc "BEATS FISH?" → "FISH?" (1 từ), giữ nguyên phần còn lại.
- Render lệnh gợi ý (dán MASTER PROMPT tương ứng vào `<...>`):
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-030-more-nutritious-than-groceries/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-030-more-nutritious-than-groceries/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
