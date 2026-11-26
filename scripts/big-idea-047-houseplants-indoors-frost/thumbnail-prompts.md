# Thumbnail Prompts — 6 Houseplants to Bring Indoors Before Frost (The 1 Step Most Skip)

## ⚠️ 2 điều chỉnh so với concept ở GATE outline

**LUẬT SỐ.** Outline gốc chốt: vàng `FROST COMING?` · trắng `MOVE THESE 6`. Dòng trắng có số nhưng thiếu
payoff cụ thể, và dòng vàng là câu hỏi chung — gần với pattern CTR thấp của kênh
(`CAN THIS COME BACK?` = 1.5%). Đã siết lại cả hai dòng.

**LUẬT THÁNG (2026-08-20, competitor scan).** 12/13 thumbnail đối thủ ngách seasonal in TÊN THÁNG trên ảnh
→ đã thêm `SEPTEMBER` vào dòng trắng.

> 📌 Tháng là tín hiệu thời vụ dùng chung toàn ngách, KHÔNG tính trùng lặp giữa 045/047/048. Khác biệt của
> video này: dòng vàng nói về **cú sốc khi di chuyển cây** (không phải đau lưng/chậu trống như 2 video kia),
> và hình ảnh là **trong nhà/ngưỡng cửa lúc chạng vạng**, khác hẳn luống đất (045) và hiên nhà ban ngày (048).

⚠️ **Đánh đổi:** tổng chữ ~6 từ → bù bằng markup tối giản (chỉ ❌/✅ ở A, không khoanh đỏ nét đứt).

Kênh vẫn dưới KPI view-5-ngày-đầu → **MODE 1**. Cặp: Verdict × Stat/Number-shock.

---

## Biến thể

| Biến thể | Concept/Archetype | Cảm-xúc-đích (G4) | Text | Layout | Màu chữ | GURU 5G |
|---|---|---|---|---|---|---|
| **A** | Verdict/Warning (Before→After) — cây chết cóng ngoài hiên vs cây khoẻ trong nhà | Lo sợ mất mát → an tâm | vàng `FROST TONIGHT?` · trắng `MOVE 6 THIS SEPTEMBER` | Before→After ❌/✅, lệch 40/60 nghiêng bên ✅ | vàng+trắng | ✅ G1 (2 từ vàng) · ✅ G2 (40/60) · ✅ G3 (chưa lộ 6 cây nào) · ✅ G4 (lá đen cóng ❌ vs cây xanh ấm trong nhà ✅) · ✅ G5 (xanh lạnh/cam ấm chọi nhau) |
| **B** | Stat/Number-shock — góc "1 bước bị bỏ qua" (tie thẳng vào title) | Nghi ngờ bản thân làm sai → tò mò | vàng `MOVED IT WRONG?` · trắng `6 PLANTS, 1 SEPTEMBER STEP` | Single hero: cây trong chậu ngay ngưỡng cửa, kính lúp đặt cạnh | vàng+trắng | ✅ G1 · ✅ G2 (1 chủ thể, nền blur) · ✅ G3 (giấu "bước" là gì — gap mạnh nhất trong 3 video) · ✅ G4 (kính lúp + lá = trạng thái đang kiểm tra, hồi hộp) · ✅ G5 (ánh đèn ấm trong nhà chọi bóng tối lạnh ngoài cửa) |

Complementarity: số "6" khớp script (6 cây thật); "1" ở biến thể B khớp lời hứa title ("The 1 Step Most Skip")
và khớp payoff mục #6 trong script (christmas cactus cần giai đoạn lạnh trước). Token `SEPTEMBER` bắt buộc
theo LUẬT THÁNG. Ngoài đó không trùng cụm từ nào với title.

⚠️ Compliance: KHÔNG dùng chữ về độc tính thú cưng trên thumbnail (jade/pothos/snake plant) dù đó là nội dung
mạnh trong script — human/pet-fear trên thumbnail vi phạm guardrail kênh. Giữ nội dung đó trong video + description.

---

## MASTER PROMPT A — Verdict/Warning (Before→After)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: an unbalanced before→after split, roughly 40/60 — the left "before" side narrower and cold-toned, the right "after" side dominant and warm.
LEFT SIDE (~40% of frame): a potted houseplant left outside on a porch at dusk, leaves blackened and drooping from cold, a faint frost sheen on the pot rim, blue-grey cold lighting. A large red ❌ over it.
RIGHT SIDE (~60% of frame, dominant): the same kind of plant now healthy indoors on a windowsill, glossy green leaves, warm golden indoor lamp light, cozy blurred living-room background. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered in clean negative space at the top, NOT covering the plants: line 1 "FROST TONIGHT?" in bright YELLOW, line 2 "MOVE 6 THIS SEPTEMBER" in WHITE. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## MASTER PROMPT B — Stat/Number-shock (single hero, "the missed step")

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — a healthy potted pothos sitting on the floor right at an open doorway threshold, half in warm indoor lamp light and half in cool blue evening light from outside. A magnifying glass rests against the pot, and a single hand holds one leaf turned upward as if inspecting its underside. The plant is offset to one side, leaving clean negative space above. Shallow depth of field, warm-versus-cool light contrast across the frame.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the plant or hand: line 1 "MOVED IT WRONG?" in bright YELLOW, line 2 "6 PLANTS, 1 SEPTEMBER STEP" in WHITE. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no second hero object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Render (tùy chọn)

```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-047-houseplants-indoors-frost/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v

python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-047-houseplants-indoors-frost/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```

Chữ baked sai dai dẳng sau 3 lần → **giữ token SEPTEMBER, rút ngắn phần còn lại** (A: `MOVE 6 · SEPTEMBER` · B: `6 PLANTS · 1 STEP`) + bỏ ❌/✅. KHÔNG chuyển sang overlay Canva.
