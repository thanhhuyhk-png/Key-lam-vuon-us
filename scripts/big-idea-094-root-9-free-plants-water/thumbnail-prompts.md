# Thumbnail prompts — big-idea-094 · You're Throwing Away Free Plants: Root These 9 in a Glass of Water

> Concept khoá cùng title ở GATE outline (08/11). Skill `garden-us-thumbnail` · **MODE 1 (concept test)**: kênh đang ở vùng views_5d ~600, impression thấp → A và B khác hẳn đòn tâm lý.
> **Chưa render**: render tốn tiền, chờ user chọn công cụ (`ve_thumb.py` / G-Labs / nano).

## Biến thể
| Biến thể | Concept (archetype) | Cảm xúc đích (G4) | Text (vàng / trắng) | Layout | Lever (khác title) | GURU 5G |
|---|---|---|---|---|---|---|
| **A ⭐** | Verdict / Before→After ❌/✅ | sợ mất (cây sắp bị vứt) → nhẹ nhõm | `BEFORE FROST` / `CUT 1 TIP` | split 40/60, bên phải (ly có rễ) thống trị | Thời gian (làm ngay tối nay) | G1 ✅ hook 2 từ, ly + rễ chiếm ≥40% · G2 ✅ ly bên phải là tiêu điểm · G3 ✅ "cắt chỗ nào? sao chỉ cần ly nước?" · G4 ✅ lá đen sương giá vs rễ trắng · G5 ✅ lá coleus đỏ tím + rễ trắng trên nền tối |
| B | Stat / Number shock | khao khát (cả dãy cây miễn phí) | `$0 BY SPRING` / `1 GLASS EACH` | hero: dãy ly trên kệ sáng, badge tròn vàng `$0` | Tiền | G1 ✅ `$0` to trong badge · G2 ✅ ly ở giữa nét căng, các ly còn lại blur · G3 ✅ "cây gì? ra rễ thật à?" · G4 ✅ rễ trắng nhìn thấy qua kính · G5 ✅ lá đỏ/tím/vàng chanh trên kệ gỗ ấm |

- **Có SỐ + triệu chứng (luật C3):** A: `1` + tình huống "sắp có sương giá" · B: `$0` + `1`. Số khớp script ("Tonight, one glass, one tip." · "free plant" · "costs" = không mua gì).
- **Complementarity:** title có you're/throwing/away/free/plants/root/9/glass/water. A dùng 0 từ trùng. B lặp "GLASS" (chủ thể bắt buộc của video, được phép 1 từ trùng).
- **Guardrails:** faceless (chỉ 1 bàn tay làm prop ở A) · không chữ sợ/độc · không động vật · số không bịa.
- ⚠️ **Cảnh báo dựng (từ phản biện R2):** không đặt chó/mèo cạnh ly coleus/begonia/arrowhead. Coleus phải là cây coleus lá màu thật, không lấy nhầm cây khác.

---

## MASTER PROMPT A — `BEFORE FROST` / `CUT 1 TIP`
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel. Vivid saturated colors, ultra high contrast, shallow depth of field. NO human face, no full person; a single hand as a prop is allowed only where described.

LAYOUT: a before→after split, NOT 50/50 — the left side takes about 40%, the right side about 60% and dominates.
LEFT (the wrong way, ~40%): a frost-damaged potted coleus plant, its burgundy-and-lime leaves blackened and limp with white frost crystals, tipped into a dark trash can on a cold porch at dawn. A bold red dashed circle around the blackened leaves and a large red ❌ over it.
RIGHT (the fix, ~60%): a clear drinking glass of water on a bright windowsill holding one fresh coleus stem tip with vivid burgundy-and-lime leaves above the waterline, and a bundle of crisp white roots clearly visible through the glass below. A single hand gently setting the glass down. A bright green ✅ beside the glass.

TEXT — The ONLY text in the entire image is exactly two stacked lines in very thick bold sans-serif, heavy black outline and drop shadow, placed at the top-left over the porch side, NOT covering the glass: line 1 "BEFORE FROST" in bright YELLOW, line 2 "CUT 1 TIP" in WHITE — spelled letter for letter, render exactly, do NOT translate, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no animals, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted hands, no leaves under the water.
```

## MASTER PROMPT B — `$0 BY SPRING` / `1 GLASS EACH`
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel. Vivid saturated colors, ultra high contrast, warm winter window light. NO human face, no full person, no hands.

SCENE: a row of clear drinking glasses of water lined up on a bright wooden shelf by a window, each glass holding one cutting with its leaves above the water and white roots visible through the glass: a burgundy-and-lime coleus stem, a chartreuse sweet potato vine piece, a pink-flowered wax begonia stem, and a single fuzzy African violet leaf on its stalk. The center glass (coleus) is large, sharp and in front, taking about 45% of the frame; the other glasses fade into soft blur. A big bright YELLOW circular badge in the top-left corner reading "$0". A curved yellow arrow pointing at the white roots in the center glass.

TEXT — The ONLY text in the entire image: inside the yellow badge "$0" in black; and two stacked lines in very thick bold sans-serif with heavy black outline and drop shadow on the right side negative space, NOT covering the center glass: line 1 "BY SPRING" in bright YELLOW, line 2 "1 GLASS EACH" in WHITE — spelled letter for letter, render exactly, do NOT translate, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no hands, no animals, no extra text, no gibberish letters, no watermark, no logo, no UI, no leaves under the water, no soil.
```

## Dự phòng (prediction: đổi khi views_5d < 500 hoặc CTR giờ 48 < 3%)
C `JUST 1 LEAF`: cận cảnh 1 lá African violet trong ly shot, có rễ và mầm con, khoanh đỏ quanh mầm. Viết prompt khi cần.

## Nguồn số
"1 tip / 1 glass" = câu kết script "Tonight, one glass, one tip." · "$0" = khung "free plant" của title, script không yêu cầu mua gì (không hormone, không đất ở giai đoạn ra rễ).
