# Thumbnail Prompts — 4 Kitchen Bug Sprays Ranked — 1 of Them Feeds the Aphids

**Mode:** MODE 1 — Concept Test *(bắt buộc: `impressions-baseline-2026-09-02.md` ghi view 5-ngày trung vị = **285**, dưới ngưỡng demotion 500 → không đủ mẫu cho MODE 2 isolation)*
**Concept-pair:** Number-ranking/curiosity (A) × Threat-reveal (B) — **khác hẳn nhau về G4**, không phải biến thể của cùng một ảnh
**Nguồn công thức:** `references/thumbnail-stats-garden-us-60k.md` §AUDIT TL;DR + §CTR ĐO THẬT

> 🔀 **Packaging-first:** `outline.md` đã chốt concept ở GATE 1: VÀNG `1 OF THESE 4` / TRẮNG `FEEDS APHIDS`.
> ⚠️ **Đã trim dòng vàng.** "1 OF THESE 4" = 4 từ, vượt luật G1 Squint *(hook vàng ≤3 từ/dòng)*.
> Rút còn **"1 OF 4"** (3 từ) — giữ nguyên số + ý nghĩa, chỉ ngắn hơn để AI bake chữ chính xác.
> Dòng trắng `FEEDS APHIDS` giữ nguyên — đã đúng luật.

---

## Biến thể A ⭐ — Number-Badge / Line-Up *(giữ concept GATE 1, chữ đã trim)*

| Mục | Giá trị |
|---|---|
| Concept | 4 vật thể xếp hàng, đánh dấu đúng 1 cái — number-badge + before/after ẩn (❌ trên 1/4) |
| Cảm-xúc-đích (G4) | Tò mò cạnh tranh — "cái nào trong 4 cái tôi đang dùng là cái sai?" |
| Text | VÀNG `1 OF 4` (3 từ, có SỐ — đúng LUẬT SỐ 15/08) · TRẮNG `FEEDS APHIDS` (2 từ, nêu triệu chứng/hệ quả) |
| Layout | Line-up 4 vật thể ngang hàng + khoanh đỏ + ❌ trên 1 vật thể |
| Màu chữ | Vàng + Trắng (chuẩn kênh) |
| Số khớp script | ✅ "4 Kitchen Bug Sprays" — đúng 4 vật thể trong ảnh |
| Complementarity | 0 từ trùng title *(title nói "1 of them", thumb nói "1 OF 4" — không trùng chữ, chỉ trùng ý số lượng, chấp nhận được vì ảnh trả lời PHẦN "cái nào" mà chữ không nói)* |
| GURU 5G | G1 ✅ (hook 3 từ, mỗi vật thể ≥ đủ lớn để nhận dạng ở 200px) · G2 ⚠️→✅ *(4 vật thể nhưng 1 tiêu điểm nhờ khoanh đỏ+❌ kéo mắt)* · G3 ✅ (chưa lộ CÁI NÀO trong tựa đề, chỉ lộ trong ảnh — vẫn giữ được "vì sao" cho video) · G4 ✅ (tò mò cạnh tranh) · G5 ✅ (khoanh đỏ + ❌ phá nền bếp trung tính) |

### MASTER PROMPT A

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, warm natural kitchen light, shallow depth of field, clean blurred kitchen counter background. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: Four kitchen items lined up in a neat row on a wooden counter, left to right: a spray bottle of soapy water, a few whole garlic cloves, a small glass jar of sugar water with a spray bottle top, and a box of baking soda. Behind the row, slightly blurred, a few real aphids visible on a green leaf. A bold red dashed circle drawn around the sugar water jar specifically, with a bold red "X" mark overlaid on it. The other three items are NOT marked, left clean.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, positioned in open space above the row of items, NOT covering any of the four objects: line 1 "1 OF 4" in bright YELLOW, line 2 "FEEDS APHIDS" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no red mark on any item except the sugar water jar.
```

---

## Biến thể B — Threat-Reveal / Invisible-Threat *(concept KHÁC hẳn A — góc "hormigas de granja")*

| Mục | Giá trị |
|---|---|
| Concept | Mối đe doạ đang diễn ra ngay lúc này — kiến "chăn" rệp, chưa ai nói cho người xem biết |
| Cảm-xúc-đích (G4) | Rùng mình khám phá / "tôi chưa từng để ý điều này" — khác hẳn cảm xúc "tò mò xếp hạng" của A |
| Text | VÀNG `THEY'RE FARMING` (2 từ — dưới 3, an toàn) · TRẮNG `NOT KILLING` (2 từ) |
| Layout | Macro/close-up 1 tiêu điểm — thân cây với hàng kiến đang bò, rệp ở giữa |
| Màu chữ | Vàng + Trắng |
| Số khớp script | ⚠️ Không có số ở dòng vàng — **vi phạm LUẬT SỐ 15/08** nếu dùng làm phương án chính. Giữ làm B vì MODE 1 đòi khác hẳn A về mặt cảm xúc; nếu B thắng ở vòng test thì bản MODE 2 sau phải thêm số |
| Complementarity | 0 từ trùng title — bổ trợ đúng (title nói "feeds", thumb nói cơ chế "farming") |
| GURU 5G | G1 ✅ (2 từ/dòng, macro rõ) · G2 ✅ (1 tiêu điểm — thân cây) · G3 ✅ (chưa nói farming CÁI GÌ) · G4 ✅ (rùng mình) · G5 ✅ (kiến + rệp tương phản mạnh với nền lá xanh) |

### MASTER PROMPT B

```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50-80. Vivid saturated colors, ultra high contrast, natural outdoor light, macro close-up framing, shallow depth of field, blurred green garden background. NO human face, no full person, no hands.

SCENE: An extreme macro close-up of a plant stem, filling most of the frame. A cluster of small green aphids on the stem, and several ants walking among them, one ant appearing to tend an aphid closely. Sharp focus on the ants and aphids, background soft green blur. A thin red dashed circle around one ant touching an aphid, to draw the eye.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline + drop shadow, positioned in the upper portion of the frame in open space, NOT covering the stem or insects: line 1 "THEY'RE FARMING" in bright YELLOW, line 2 "NOT KILLING" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted insect anatomy.
```

---

## ⚠️ Trước khi render

- [ ] Xác nhận **A** hay **B** làm ảnh chính khi upload — MODE 1 nghĩa là **cả hai** nên được render để so sánh, nhưng chỉ 1 lên video khi đăng lần đầu.
- [ ] 🔴 **B thiếu số ở dòng vàng** — nếu B thắng CTR, phải làm bản MODE 2 thêm số *(ví dụ đổi "THEY'RE FARMING" → "4 SPRAYS, 1 FEEDS THEM")* trước khi dùng lâu dài.
- [ ] Render bằng Nano Banana Pro *(theo `garden-us-thumbnail` SKILL.md)*.
- [ ] 🔴 **API key thiếu** — như `big-idea-041`, `GEMINI_API_KEY`/`AI33_KEY` không có trong hệ thống lúc soạn prompt này. Render thủ công hoặc cấp key trước khi chạy.
- [ ] Sau khi render: verify chữ đúng chính tả 100% *(ưu tiên tuyệt đối theo SKILL.md — chữ méo giết CTR mạnh hơn thiếu 1 chi tiết markup)*.
