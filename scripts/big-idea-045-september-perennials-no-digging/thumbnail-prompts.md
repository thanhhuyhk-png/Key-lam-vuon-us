# Thumbnail Prompts — 7 No-Dig Perennials for September That Come Back Every Year

## ⚠️ 2 lần điều chỉnh so với concept chốt ở GATE outline

**Lần 1 — LUẬT SỐ.** Outline gốc chốt: vàng `BACK HURTS?` · trắng `NO MORE DIGGING`. Theo
`thumbnail-stats-garden-us-60k.md`, LUẬT SỐ (2026-08-15, CTR đo thật n=6) yêu cầu chữ trên thumbnail
phải có SỐ/$ — câu không số là pattern CTR THẤP NHẤT đo được của kênh (1.5–1.7%). `NO MORE DIGGING`
không có số → đã thay bằng dòng có số + payoff.

**Lần 2 — LUẬT THÁNG (2026-08-20, competitor scan).** Quét 13 thumbnail đối thủ cùng ngách seasonal:
**12/13 in TÊN THÁNG ngay trên ảnh** ("PLANT ONCE THIS AUGUST", "15 VEGETABLES TO PLANT IN SEPTEMBER"…).
Cả 2 biến thể cũ đều THIẾU token tháng → đã thêm `SEPTEMBER` vào dòng trắng.

> 📌 **Tháng KHÔNG tính là trùng lặp giữa các video cùng batch.** Mọi đối thủ đều dùng chung token tháng —
> nó là tín hiệu phân loại thời vụ (video còn hạn dùng hay đã cũ), không phải yếu tố khác biệt hoá.
> Khác biệt giữa 045/047/048 nằm ở **dòng vàng triệu chứng + hình ảnh**, và 3 video đó vẫn khác nhau hoàn toàn.

⚠️ **Đánh đổi đã chấp nhận:** thêm token tháng đẩy tổng chữ từ 5 lên ~6 từ, vượt nhẹ khuyến nghị
"≤5 từ" của skill (lý do: AI bake chữ dễ méo khi nhiều element). **Bù lại bằng cách đơn giản hoá markup**
— bỏ bớt khoanh đỏ nét đứt ở biến thể A, chỉ giữ ❌/✅. Ưu tiên tuyệt đối: chữ đúng chính tả > markup đẹp.

Kênh vẫn dưới KPI view-5-ngày-đầu (234 vs 500) → **MODE 1** (concept test). Cặp: Verdict × Stat/Number-shock.

---

## Biến thể

| Biến thể | Concept/Archetype | Cảm-xúc-đích (G4) | Text | Layout | Màu chữ | GURU 5G |
|---|---|---|---|---|---|---|
| **A** | Verdict (Before→After) — "mua lại mỗi xuân" vs "trồng 1 lần" | Tiếc nuối/lãng phí → nhẹ nhõm | vàng `BUYING AGAIN?` · trắng `PLANT 7 THIS SEPTEMBER` | Before→After ❌/✅, lệch 40/60 nghiêng bên ✅ | vàng+trắng | ✅ G1 (dòng vàng 2 từ) · ✅ G2 (40/60) · ✅ G3 (chưa lộ 7 cây) · ✅ G4 (khay héo ❌ vs luống hoa sung túc ✅) · ✅ G5 (đỏ/xanh chọi nền) |
| **B** | Stat/Number-shock — góc ergonomic "trồng ngồi ghế" (mục #7 sedum) | Đau nhức → thư giãn | vàng `BACK HURTS?` · trắng `7 SEPTEMBER SIT-DOWN PICKS` | Single hero (ghế làm vườn thấp + bay trồng cây) | vàng+trắng | ✅ G1 · ✅ G2 (1 chủ thể lệch, nền blur) · ✅ G3 (chưa lộ cây/kỹ thuật) · ✅ G4 (ghế + bay = trạng thái thư thái) · ✅ G5 (ghế cam/đỏ phá nền xanh) |

Complementarity: cả 2 dùng số "7" (numeral info-scent, đúng tiền lệ kênh) + token `SEPTEMBER` (trùng title
nhưng là tín hiệu thời vụ bắt buộc theo LUẬT THÁNG, không tính FAIL). Ngoài 2 thứ đó, không trùng cụm từ nào
với title `7 No-Dig Perennials for September That Come Back Every Year`. A dùng lại "Back" (khác nghĩa —
đau lưng vs "come back"), chơi chữ có chủ đích.

Số "7" khớp script (7 mục thật). Tháng khớp cửa sổ đăng (28/08–02/09, nội dung tháng 9).

---

## MASTER PROMPT A — Verdict (Before→After)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background, warm natural September light. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: an unbalanced before→after split, roughly 40/60 — the left "before" side narrower, the right "after" side dominant and brighter.
LEFT SIDE (the wrong way, ~40% of frame): a wilted, half-dead annual flower tray sitting in a shopping cart at a garden center checkout, dry fallen autumn leaves around it, dull desaturated lighting. A large red ❌ over the tray.
RIGHT SIDE (the fix, ~60% of frame, dominant): a lush, thriving perennial flower bed in September — black-eyed susans, hosta leaves, and sedum blooms together, vibrant and full, warm golden light. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, centered in clean negative space at the top, NOT covering the flowers: line 1 "BUYING AGAIN?" in bright YELLOW, line 2 "PLANT 7 THIS SEPTEMBER" in WHITE. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## MASTER PROMPT B — Stat/Number-shock (single hero, ergonomic angle)

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background, warm natural September light. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — a low wooden garden stool with a bright orange-red cushion, sitting beside a shallow flower bed, a hand trowel resting on the seat, a small tray of sedum cuttings nearby. The stool and trowel are offset to one side, leaving clean negative space above and to the other side. Macro-ish framing, shallow depth of field, the orange-red stool popping hard against the green garden background.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the stool or trowel: line 1 "BACK HURTS?" in bright YELLOW, line 2 "7 SEPTEMBER SIT-DOWN PICKS" in WHITE. The ONLY text in the entire image is exactly these two lines — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no second hero object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Render (tùy chọn)

```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-045-september-perennials-no-digging/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v

python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-045-september-perennials-no-digging/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```

Chữ baked sai dai dẳng sau 3 lần → **giữ token SEPTEMBER, rút ngắn phần còn lại** (A: `PLANT 7 IN SEPTEMBER` · B: `7 PICKS · SEPTEMBER`) + bỏ nốt ❌/✅. KHÔNG chuyển sang overlay Canva.
