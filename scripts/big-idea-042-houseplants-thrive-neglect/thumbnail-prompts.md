# Thumbnail Prompts — 5 Houseplants That Get Healthier When You Forget to Water Them

**Mode:** MODE 1 — Concept Test (bắt buộc: kênh đang Browse demotion, chưa đủ mẫu cho MODE 2 isolation)
**Concept-pair:** Verdict/Before→After (A, đã chốt GATE 1) × Warning/Stop-Shock (B, mới)
**Nguồn công thức:** `references/thumbnail-stats-garden-us-60k.md` §AUDIT TL;DR

> ⚠️ **Đã trim chữ so với concept chốt ở GATE 1.** Outline duyệt "THESE 5 LOVE NEGLECT / STOP WATERING
> SO MUCH" (8 từ). Rule reliability của skill này (`≤5 từ tổng, ≤3 từ/dòng hook`) buộc rút gọn còn
> **"5 LOVE NEGLECT / STOP WATERING"** (5 từ). Giữ nguyên số + ý nghĩa, ngắn hơn để AI bake chữ chính xác.

---

## Biến thể A — Before→After / Guilt-Relief (giữ nguyên concept GATE 1, chữ đã trim)

| Mục | Giá trị |
|---|---|
| Concept | Verdict — trước/sau, đảo cảm giác tội lỗi thành sự nhẹ nhõm |
| Cảm-xúc-đích (G4) | Nhẹ nhõm / được minh oan — cây trái héo vì úng (trái) ↔ cây khoẻ vì tưới ít (phải) |
| Text | VÀNG `5 LOVE NEGLECT` (3 từ) · TRẮNG `STOP WATERING` (2 từ) — tổng 5 từ |
| Layout | ① Before→After 60/40 (bên phải/payoff to hơn — G2) |
| Màu chữ | Vàng + Trắng (chuẩn kênh) |
| Số khớp script | ✅ "5" (năm cây) |
| Complementarity | Không trùng title (title không có "love neglect") |
| GURU 5G | G1 ✅ (hook 3 từ) · G2 ✅ (60/40, phải nổi bật) · G3 ✅ (chưa lộ 5 cây là gì) · G4 ✅ (nhẹ nhõm/minh oan) · G5 ✅ (đất đen úng nước vs đất nứt khô — tương phản tối/sáng mạnh) |

### MASTER PROMPT A

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred indoor plant background. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: a before-after split, NOT 50/50 — the right side dominates about 60% of the frame, bright and vivid; the left side is smaller, about 40%, dim and desaturated.
LEFT SIDE (the wrong way, ~40% width, dim): a wilted, yellowing houseplant sitting in visibly soggy, dark, waterlogged black soil in a plastic pot, water pooling at the base. A bold red dashed circle around the wet soil and a large red ❌ over the plant.
RIGHT SIDE (the fix, ~60% width, bright and dominant): the same kind of houseplant, lush, deep green and healthy, growing in dry, lightly cracked terracotta-colored soil in a clean pot on a sunny windowsill. A bright green ✅ on this side.

TEXT — render EXACTLY two short lines in very thick bold sans-serif, heavy black outline + drop shadow, centered in clean negative space, NOT covering the plants: line 1 "5 LOVE NEGLECT" in bright YELLOW, line 2 "STOP WATERING" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Biến thể B — Single Hero / Warning-Stat-Shock (concept KHÁC hẳn A)

| Mục | Giá trị |
|---|---|
| Concept | Warning/Stop — dùng đúng con số shock trong hook script (khảo sát 54%) |
| Cảm-xúc-đích (G4) | Giật mình tự soi ("có phải mình không?") — khác hẳn cảm xúc "nhẹ nhõm" của A |
| Text | VÀNG `STOP!` (1 từ) · TRẮNG `54% OVERWATER` (2 từ) — tổng 3 từ |
| Layout | ② Single hero (bình tưới đang tưới tràn) |
| Màu chữ | Vàng + Trắng |
| Số khớp script | ✅ "fifty-four percent" trong script → viết thành `54%` |
| Complementarity | 0 từ trùng A hoặc title — concept hoàn toàn khác |
| GURU 5G | G1 ✅ ("STOP!" cực dễ đọc ở 200px) · G2 ✅ (1 tiêu điểm — bình tưới) · G3 ✅ (chưa nói cây nào an toàn) · G4 ✅ (giật mình, khác A) · G5 ✅ (nước tràn tối màu + mũi tên đỏ phá nền xanh) |

### MASTER PROMPT B

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred indoor background. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — a metal watering can, held by a single hand (prop only, no face, no body), pouring a heavy stream of water onto a houseplant that is clearly drowning: dark waterlogged soil, water overflowing and pooling around the pot's base. A bold red curved arrow points at the overflowing water. Offset to one side, leaving clean negative space for text.

TEXT — render EXACTLY two short lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the watering can or plant: line 1 "STOP!" in bright YELLOW, line 2 "54% OVERWATER" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Render (chưa chạy được — thiếu API key)

```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-042-houseplants-thrive-neglect/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-042-houseplants-thrive-neglect/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```

🔴 **Đã kiểm tra: KHÔNG có `GEMINI_API_KEY` hoặc `AI33_KEY` ở đâu trong hệ thống** (giống tình trạng
BÀI 1 và 3 video A/B test cũ đang bị chặn cùng lý do). Cần bạn cung cấp key để render trực tiếp, hoặc
dán 2 prompt trên vào tool ảnh sẵn có.
