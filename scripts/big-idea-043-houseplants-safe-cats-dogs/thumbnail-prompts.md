# Thumbnail Prompts — 9 Houseplants That Are Safe for Cats and Dogs

**Mode:** MODE 1 — Concept Test (kênh đang Browse demotion)
**Concept-pair:** Single-hero/emotional-proxy (A, đã chốt GATE 1, có động vật phụ) × Number-badge/listicle (B, mới)
**Nguồn công thức:** `references/thumbnail-stats-garden-us-60k.md` §AUDIT TL;DR
**Guardrail đặc thù bài này:** kênh CẤM động vật đe doạ làm hero (rắn/chuột) nhưng CHO PHÉP chó/mèo NHÀ
làm phụ (không quá 30% khung, không phải chủ thể chính). Cả 2 biến thể dưới đây tuân thủ.

> ⚠️ Đã trim chữ theo rule reliability (≤5 từ tổng). Giữ nguyên số "9" + ý nghĩa.

---

## Biến thể A — Single Hero + Pet Prop (giữ nguyên concept GATE 1)

| Mục | Giá trị |
|---|---|
| Concept | Single hero (spider plant) + mèo làm phụ — cảm xúc "đây là video cho tôi" |
| Cảm-xúc-đích (G4) | Yên tâm / ấm áp — mèo đang ngửi lá mà không sao cả = trạng thái an toàn |
| Text | VÀNG `THESE 9 PASS` (3 từ) · TRẮNG `CATS & DOGS` (2 từ) — tổng 5 từ |
| Layout | ② Single hero + negative space |
| Màu chữ | Vàng + Trắng |
| Số khớp script | ✅ "9" |
| GURU 5G | G1 ✅ · G2 ✅ (1 tiêu điểm — cây, mèo chỉ phụ) · G3 ✅ (chưa lộ 9 cây là gì) · G4 ✅ (yên tâm) · G5 ✅ (mèo tạo điểm phá nền xanh tự nhiên) |

### MASTER PROMPT A

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, warm indoor light, blurred living room background. NO human face, no full person.

SCENE: ONE single hero object — a spider plant with long arching variegated leaves in a pot on a sunny windowsill, offset to one side. At the edge of the frame (not the hero, occupying less than 30% of the image), a calm house cat is gently sniffing one of the leaves. The cat is a supporting element only, not the focal point. Clean negative space on the other side for text.

TEXT — render EXACTLY two short lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the plant or the cat: line 1 "THESE 9 PASS" in bright YELLOW, line 2 "CATS & DOGS" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no human face, no full human body, no threatening animals, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Biến thể B — Number-Badge / Listicle (concept KHÁC hẳn A)

| Mục | Giá trị |
|---|---|
| Concept | Number-badge listicle — nhấn "9 cây" bằng badge tròn thay vì cảm xúc pet |
| Cảm-xúc-đích (G4) | Tin cậy/organized — cảm giác "đây là danh sách đầy đủ, đáng lưu" khác hẳn "ấm áp" của A |
| Text | VÀNG `9 SAFE PLANTS` (3 từ) · TRẮNG `ASPCA CHECKED` (2 từ) — tổng 5 từ |
| Layout | ③ Leading-number badge (số 9 trong vòng tròn vàng góc trên-trái) |
| Màu chữ | Vàng + Trắng |
| Số khớp script | ✅ "9" + "ASPCA" (nguồn thật trong script) |
| GURU 5G | G1 ✅ (badge số to, dễ đọc) · G2 ✅ (badge + hero không cạnh tranh vì badge nhỏ góc) · G3 ✅ (chưa lộ 9 cây) · G4 ✅ (tin cậy, khác A) · G5 ✅ (badge tròn vàng đậm phá nền) |

### MASTER PROMPT B

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, blurred indoor plant collection background. NO human face, no full person, no animals in this variant.

SCENE: a small grouping of three or four different common houseplants (a spider plant, a Boston fern, a calathea with striped leaves, and a small palm) arranged together on a bright windowsill shelf, offset to one side of the frame. In the top-left corner, a bold solid yellow circular badge with the large black number "9" inside it.

TEXT — render EXACTLY two short lines in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the plants or the badge: line 1 "9 SAFE PLANTS" in bright YELLOW, line 2 "ASPCA CHECKED" in WHITE. The ONLY text in the entire image, besides the single digit "9" inside the badge, is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no animals, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```

---

## Render (chưa chạy được — thiếu API key)

```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-043-houseplants-safe-cats-dogs/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "D:/0002-Team A Nam/scripts/big-idea-043-houseplants-safe-cats-dogs/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```

🔴 Vẫn không có `GEMINI_API_KEY`/`AI33_KEY` trong hệ thống (giống BÀI 1 và BÀI 2). Dán 2 prompt trên vào
tool ảnh sẵn có, hoặc cung cấp key để render trực tiếp.
