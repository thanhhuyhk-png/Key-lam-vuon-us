# Thumbnail Prompts — 7 Plants You Can't Kill — They Grow in Just Water, No Soil

**Mode:** MODE 1 — Concept Test (bắt buộc: kênh đang Browse demotion, chưa đủ mẫu cho MODE 2 isolation)
**Concept-pair:** Verdict/promise-echo (A, đã chốt GATE 1) × Stat/Number-shock (B, mới)
**Nguồn công thức:** `references/thumbnail-stats-garden-us-60k.md` §AUDIT TL;DR

> ⚠️ **Đã trim chữ so với concept chốt ở GATE 1.** Outline duyệt "THESE 7 CAN'T DIE / NO SOIL · NO COST"
> (8 từ). Rule reliability của skill này (`≤5 từ tổng, ≤3 từ/dòng hook` — để AI bake chữ chính xác) buộc
> rút gọn còn **"7 CAN'T DIE / ZERO COST"** (5 từ). Giữ nguyên ý nghĩa + số + promise-echo với title,
> chỉ ngắn hơn. Nếu bạn muốn giữ đúng bản dài, cần cảnh báo trước: AI dễ bake sai chính tả hơn với 8 từ.

---

## Biến thể A — Single Hero / Promise-Echo (giữ nguyên concept GATE 1, chữ đã trim)

| Mục | Giá trị |
|---|---|
| Concept | Verdict + Promise-Echo — lặp lời hứa title lên thumb (hợp lệ theo data champion AVD 49%) |
| Cảm-xúc-đích (G4) | Thoả mãn / tự tin — bộ rễ trắng dày = trạng thái "sống khoẻ" |
| Text | VÀNG `7 CAN'T DIE` (3 từ) · TRẮNG `ZERO COST` (2 từ) — tổng 5 từ |
| Layout | ② Single hero + negative space |
| Màu chữ | Vàng + Trắng (chuẩn kênh) |
| Số khớp script | ✅ "7" (bảy cây) |
| Complementarity | `ECHO` — cố ý lặp lời hứa title, đúng ngoại lệ champion |
| GURU 5G | G1 ✅ (hook 3 từ, chủ thể ≥40% khung) · G2 ✅ (1 tiêu điểm — lọ) · G3 ✅ (chưa lộ 7 cây là gì) · G4 ✅ (thoả mãn) · G5 ✅ (khoanh đỏ + rễ trắng phá nền xanh) |

### MASTER PROMPT A

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, warm golden window light, blurred kitchen background. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — a clear glass jar sitting on a sunlit windowsill, filled with water and a dense mass of thick white plant roots fanned out inside it, with a leafy green vine trailing up out of the jar. The jar is offset to one side, leaving clean negative space on the other side for text. A bold red dashed circle drawn around the white root mass to highlight it. Macro-ish framing, shallow depth of field on the blurred kitchen background.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the jar or roots: line 1 "7 CAN'T DIE" in bright YELLOW, line 2 "ZERO COST" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Biến thể B — Before→After / Stat-Shock (concept KHÁC hẳn A — góc chi phí)

| Mục | Giá trị |
|---|---|
| Concept | Stat/Number-shock — vế "no cost" của title CHƯA được thumb A khai thác thị giác |
| Cảm-xúc-đích (G4) | Vui vì tiết kiệm / cảm giác "hớ" khi mua — khác hẳn cảm xúc "thoả mãn sống khoẻ" của A |
| Text | VÀNG `$10-$30?` · TRẮNG `FREE INSTEAD` — tổng 4 từ |
| Layout | ① Before→After 60/40 (bên phải/payoff to hơn — G2) |
| Màu chữ | Vàng + Trắng |
| Số khớp script | ✅ "ten to thirty dollars" trong script → viết thành `$10-$30` |
| Complementarity | 0 từ trùng với A hoặc title — concept hoàn toàn khác |
| GURU 5G | G1 ✅ · G2 ✅ (60/40, phải nổi bật hơn) · G3 ✅ (chưa lộ cây cụ thể) · G4 ✅ (frugal-vindication, khác A) · G5 ✅ (biên lai trắng + ❌ đỏ tương phản mạnh với xanh) |

### MASTER PROMPT B

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred kitchen/garden background. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: a before-after split, but NOT 50/50 — the right side dominates about 60% of the frame, brighter and more saturated; the left side is smaller, about 40%, dimmer and slightly desaturated.
LEFT SIDE (the wrong way, ~40% width, dim): a small printed price tag reading "$10-$30" resting next to a droopy, sad-looking store-bought houseplant in a plastic nursery pot. A bold red dashed circle around the price tag and a large red ❌ over the wilting plant.
RIGHT SIDE (the fix, ~60% width, bright and dominant): a single hand (prop only, no face, no body) setting a lush green plant cutting into a clear glass jar of water on a sunny windowsill. A bright green ✅ on this side.

TEXT — render EXACTLY two short lines in very thick bold sans-serif, heavy black outline + drop shadow, centered in clean negative space, NOT covering the objects: line 1 "$10-$30?" in bright YELLOW, line 2 "FREE INSTEAD" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Render (chưa chạy được — thiếu API key)

```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-041-plants-cant-kill-water/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-041-plants-cant-kill-water/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```

🔴 **Đã kiểm tra: KHÔNG có `GEMINI_API_KEY` (mode `nano`) hoặc `AI33_KEY` (mode ElevenLabs-image) ở đâu
trong hệ thống** — không trong `.env` workspace, không trong biến môi trường, không trong `.secrets/`.
Đây là lý do 3 video A/B test thumbnail cũ (`scripts/ab-test-thumbnails-2026-W34/`) cũng đang bị chặn.
Cần bạn cung cấp 1 trong 2 key này thì tôi mới render được ảnh thật.

**Việc cần làm:** dán 2 master prompt trên vào bất kỳ tool ảnh nào bạn có sẵn (Nano Banana Pro, Midjourney,
ChatGPT image, v.v.), hoặc cung cấp API key để tôi render trực tiếp.
