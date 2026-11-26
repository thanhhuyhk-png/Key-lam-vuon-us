# Thumbnail Prompts — big-idea-093 · Don't Pull Your Pepper Plants Yet. They Can Live for Years

> ✅ **USER CHỌN 27/10: DÙNG CẢ A VÀ B (Test & Compare)** — render khi G-Labs bật.
>
> garden-us-thumbnail · 27/10/2026 · **MODE 1 (concept test)** — kênh vẫn dưới KPI views_5d ổn định → A và B khác hẳn concept. Chưa render (user chỉ yêu cầu prompt).
> Nguồn công thức: `references/thumbnail-stats-garden-us-60k.md` (TL;DR: faceless · 2 tầng vàng/trắng · BẮT BUỘC số + triệu chứng · luật tên tháng cho video theo mùa — chưa có CTR đo trên kênh → B dùng tên tháng để kiểm chứng).

## Packaging (khoá từ outline GATE [1], điều chỉnh theo luật số + triệu chứng)
- **Title (lever):** Kết quả↑ (cây sống nhiều năm) + Thời gian↓ ("Yet" = ngay trước sương giá)
- **Thumbnail (lever khác):** Công sức↓ (chỉ giữ 3 cành) · B: Chắc-thắng↑ (không cần nắng)
- Concept outline `KEEP 3 STEMS` (có số, thiếu triệu chứng) + `FROST TONIGHT?` (triệu chứng, thiếu số) → **ghép thành A 2 tầng** để có đủ cả hai.
- **Số trên thumb khớp script:** "3 stems" (M3: "Find the three strongest main branches… Three stems, and that's the whole plan") · "50–60°F" (M2/M3: "around fifty to sixty degrees") · "no sun" (M3: "a resting plant barely needs light… No lamp, no sunny sill").
- **Complementarity Test:** title có Don't/Pull/Pepper/Plants/Yet/Live/Years → A `FROST TONIGHT? / KEEP 3 STEMS` **0 từ trùng** ✅ · B `NOVEMBER FROST? / 50–60°F, NO SUN` **0 từ trùng** ✅

## Bảng biến thể
| Biến thể | Concept (archetype) | Cảm xúc đích (G4) | Text (vàng / trắng) | Layout | Màu chữ | GURU 5G |
|---|---|---|---|---|---|---|
| **A** ⭐ | Verdict — nhổ bỏ vs giữ lại | sợ mất → nhẹ nhõm | `FROST TONIGHT?` / `KEEP 3 STEMS` | ① Before→After 40/60 ❌/✅ | vàng + trắng | G1 ✅ hook 2 từ, cây chiếm ≥40% · G2 ✅ bên phải thống trị 60% · G3 ✅ "giữ 3 cành thế nào? sống được à?" — đáp án trong video · G4 ✅ cây đen rũ vì sương (trái) vs cây gọn gàng chữ Y trong chậu sạch (phải) · G5 ✅ quả ớt đỏ + sương trắng-xanh lạnh phá nền xanh lá |
| **B** | Curiosity + số + tên tháng — chỗ tối mát | tò mò / bất ngờ | `NOVEMBER FROST?` / `50–60°F, NO SUN` | ② Single hero lệch phải + nhiệt kế | vàng + trắng | G1 ✅ hook 2 từ, cây ≥40% · G2 ✅ 1 chủ thể duy nhất · G3 ✅ "không cần nắng thật à?" (Loop #2 của video) · G4 ✅ cây ớt trơ cành yên tĩnh trong góc tối = "đang ngủ" · G5 ✅ tông nâu–xám ấm + ánh vàng nhiệt kế, không nền xanh lá |

Guardrails: không mặt người (tay cầm kéo là prop) · không 100%/overclaim · không động vật · không nói "sống mãi" · số đều có trong script.
**Test & Compare:** A vs B. Biến chính đang test: *Verdict loss + số* (A) vs *Curiosity + số + tên tháng* (B). Đọc sau giờ 48; nếu CTR cả hai <4% → kích hoạt quy tắc dừng trong `prediction.md`.

---

## MASTER PROMPT A — Verdict / Before→After
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–80. Vivid saturated colors, ultra high contrast, softly blurred autumn backyard background. NO human face, no full person. A single hand holding pruning shears as a prop is allowed on the right side only.

LAYOUT: a before→after split, NOT 50/50 — the right side is dominant (about 60 percent of the frame), the left side smaller (about 40 percent).
LEFT SIDE (the wrong way): a pepper plant in a garden bed, blackened and limp from frost, leaves wilted and coated with white frost crystals, two shriveled red peppers hanging. A large bold red ❌ over it.
RIGHT SIDE (the fix, dominant, sharp and bright): the same kind of pepper plant cut back to a short bare letter-Y shape with exactly three short main stems and no leaves, standing in a clean terracotta pot filled with fresh dark potting mix. Three bold red dashed circles mark the three cut stem tips. A hand holding red-handled pruning shears beside the pot. A bright green ✅ on this side.

TEXT — The ONLY text in the entire image is exactly these two stacked lines, spelled letter for letter, in very thick bold sans-serif with heavy black outline and drop shadow, placed in the upper area, NOT covering the plants: line 1 "FROST TONIGHT?" in bright YELLOW, line 2 "KEEP 3 STEMS" in WHITE. Render exactly, do NOT translate, do NOT add any other text, letters, numbers, captions, labels or watermark anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no extra numbers, no watermark, no logo, no UI, no distorted plants, no more than three stems on the right plant.
```

## MASTER PROMPT B — Curiosity + number + month / Single hero
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–80. Ultra high contrast, warm moody indoor light. NO human face, no person, no hands.

SCENE: ONE single hero object only — a pepper plant cut back to a short bare letter-Y shape with three short stems and no leaves, in a clean terracotta pot, sitting on a wooden shelf in a dim, cool corner of a house (a basement-style corner with soft shadows, no window, no sunlight). Placed on the right third of the frame, large and sharp, filling at least 40 percent of the frame. Beside the pot, a simple round analog thermometer with a needle pointing near 55 degrees. A curved bright yellow arrow points from the text area to the plant. Shallow depth of field, everything else softly blurred.

TEXT — The ONLY text in the entire image is exactly these two stacked lines, spelled letter for letter, in very thick bold sans-serif with heavy black outline and drop shadow, in the empty left side, NOT covering the plant: line 1 "NOVEMBER FROST?" in bright YELLOW, line 2 "50–60°F, NO SUN" in WHITE. Render exactly, do NOT translate, do NOT add any other text, letters, numbers, captions, labels or watermark anywhere. The thermometer has no readable printed words.

Negative: no face, no person, no hands, no window, no sunlight beams, no green leaves on the pepper plant, no second plant, no extra text, no gibberish letters, no watermark, no logo, no UI.
```

## Render (khi user bật G-Labs / tool ảnh)
- G-Labs: `tools/glabs_thumb.py` (memory: tạo thumbnail từ Garden bằng khóa ở workspace Quân sự).
- Kiểm sau render: chữ đúng chính tả từng chữ (đặc biệt "°F" và dấu "–" ở B — nếu AI làm méo, đổi thành `50-60°F, NO SUN` hoặc `55°F, NO SUN`) · A đúng 3 cành · không mặt người · file >50KB, 16:9.
