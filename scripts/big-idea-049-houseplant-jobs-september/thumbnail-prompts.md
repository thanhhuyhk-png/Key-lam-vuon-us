# Thumbnail Prompts — 7 Houseplant Jobs to Do Before You Turn the Heat On

## ⚠️ Điều chỉnh: LUẬT THÁNG + tránh trùng 3 bài trước

Concept gốc outline: vàng `HEAT COMING ON?` · trắng `7 JOBS FIRST` — đã tự nhiên đạt LUẬT SỐ (câu hỏi
triệu chứng + số + payoff), chỉ cần thêm token `SEPTEMBER` theo LUẬT THÁNG (2026-08-20).

Đã tránh trùng chữ với 3 bài trước: 045 dùng "BACK HURTS?"/"BUYING AGAIN?", 048 dùng "EMPTY AGAIN?"/
"KNEES HURT?", 047 dùng "FROST TONIGHT?"/"MOVED IT WRONG?" — video này khai thác góc RIÊNG: job #7
myth-bust ("đừng thay chậu bây giờ") là khác biệt lớn nhất của video, dùng làm biến thể B.

Kênh vẫn dưới KPI → MODE 1. Cặp: Verdict × Curiosity-gap (thay Stat/Number-shock lần này vì myth-bust
tự nhiên tạo curiosity mạnh hơn góc ergonomic).

---

## Biến thể

| Biến thể | Concept/Archetype | Cảm-xúc-đích (G4) | Text | Layout | Màu chữ | GURU 5G |
|---|---|---|---|---|---|---|
| **A** | Verdict (Before→After) — lá cháy mép do miệng gió sưởi vs cây khoẻ cạnh máy tạo ẩm | Lo lắng → an tâm | vàng `HEAT COMING ON?` · trắng `7 JOBS · SEPTEMBER` | Before→After ❌/✅, lệch 40/60 | vàng+trắng | ✅ G1 · ✅ G2 (40/60) · ✅ G3 (chưa lộ 7 việc) · ✅ G4 (lá cháy nâu ❌ vs cây tươi ẩm ✅) · ✅ G5 (nâu/xanh chọi nền) |
| **B** | Curiosity-gap — myth-bust job #7 (đừng thay chậu) | Nghi ngờ bản thân vừa làm sai → tò mò | vàng `REPOTTING NOW?` · trắng `7 JOBS, 1 SEPTEMBER MYTH` | Single hero: chậu cây + xẻng nhỏ đặt cạnh, chưa động vào đất | vàng+trắng | ✅ G1 · ✅ G2 (1 chủ thể, nền blur) · ✅ G3 (giấu đáp án "myth" là gì — gap mạnh nhất trong 4 video) · ✅ G4 (chậu+xẻng chưa dùng = trạng thái lưỡng lự) · ✅ G5 (ánh đèn ấm trong nhà chọi nền xanh cây) |

Complementarity: số "7" khớp script + token `SEPTEMBER` (bắt buộc LUẬT THÁNG). "REPOTTING" không xuất
hiện trong title (`7 Houseplant Jobs to Do Before You Turn the Heat On`) — 0 trùng ngoài numeral.

Số "7" khớp script (7 job thật). "1 MYTH" khớp job #7 thật (repot bust).

---

## MASTER PROMPT A — Verdict (Before→After)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: an unbalanced before→after split, roughly 40/60 — the left "before" side narrower, the right "after" side dominant and warmer.
LEFT SIDE (~40% of frame): a potted houseplant sitting right next to a wall heating vent, its leaf edges scorched brown and curling, dry stale-warm lighting. A large red ❌ over it.
RIGHT SIDE (~60% of frame, dominant): the same kind of plant healthy and glossy across the room, a small humidifier releasing visible mist beside it, warm cozy indoor lamp light. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered in clean negative space at the top, NOT covering the plants: line 1 "HEAT COMING ON?" in bright YELLOW, line 2 "7 JOBS · SEPTEMBER" in WHITE. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## MASTER PROMPT B — Curiosity-gap (repotting myth)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — a houseplant still in its old pot, sitting next to an empty new terracotta pot and a small hand trowel resting untouched beside it, as if paused mid-decision. A single hand rests near the trowel but is not gripping it. Warm indoor lamp light, soft green blurred living-room background. The plant and pots are offset to one side, leaving clean negative space above.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the plant or pots: line 1 "REPOTTING NOW?" in bright YELLOW, line 2 "7 JOBS, 1 SEPTEMBER MYTH" in WHITE. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no second hero object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Render (tùy chọn)

```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-049-houseplant-jobs-september/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v

python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-049-houseplant-jobs-september/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```

Chữ baked sai dai dẳng sau 3 lần → **giữ token SEPTEMBER, rút ngắn phần còn lại** (A: `7 JOBS` bỏ tháng ra badge riêng · B: `7 JOBS · 1 MYTH`) + bỏ ❌/✅. KHÔNG chuyển sang overlay Canva.
