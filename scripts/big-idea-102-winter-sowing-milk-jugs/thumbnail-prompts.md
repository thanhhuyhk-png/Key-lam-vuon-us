# Thumbnail Prompts & Overlay Spec (L29 Clean Plate + Manual/Pillow) — big-idea-102

> Cập nhật 26/11/2026 (sau Phản biện kép 3R V1+V2 — quyết định **D4**):
> - **Áp dụng cứng Luật L29:** AI **CHỈ** render **ảnh nền sạch 16:9 (`STRICTLY NO TEXT`)** có chừa sẵn vùng tối/mờ (negative space); toàn bộ **chữ 2 tầng ALL CAPS (VÀNG + TRẮNG, viền đen dày 9–10px + đổ bóng) & badge ❌/✅ / mũi tên** ghép bằng **Canva / Photoshop** hoặc **Python Pillow** (`tools/garden_thumb_real.py`) để sắc nét tuyệt đối trên cả **Smart TV (2–3m)** lẫn **mobile (200px)**.
> - **Đã sửa theo 3R V1 (D4):** Gỡ `"$0"` (tránh overclaim vì vẫn cần potting mix/băng dính), giữ **LUẬT SỐ** (`6`), **LUẬT THÁNG** (`JANUARY`), **FACELESS** (không mặt người, không chữ meta L21).
> - **Khuyến nghị Test & Compare (MODE 1):** Render **A (PA1)** ưu tiên trước + **C (PA3)** hoặc **B (PA2)** để A/B test concept khác hẳn nhau.

---

## Bảng so sánh 3 phương án Clean-Plate + Overlay Spec

| Biến thể | Đòn tâm lý | Chữ dòng 1 (VÀNG `#FFD60A`) | Chữ dòng 2 (TRẮNG `#FFFFFF`) | Markup Vector | Bố cục & GURU 5G |
|---|---|---|---|---|---|
| **Thumb A ⭐ (PA1 — ưu tiên)** | Số lượng + Tháng + Bỏ thiết bị | **`6 SEEDS IN JANUARY`** | **`NO GROW LIGHTS`** | 1 mũi tên cong vàng trỏ mầm xanh trong bình | Single Hero lệch phải 55%, trái 45% nền tối mờ sạch · G1–G5 PASS |
| **Thumb B (PA2 — Test & Compare)** | Triệu chứng + Cách sửa mùa vụ | **`ROTTING SEEDS?`** | **`JANUARY JUG FIX`** | ❌ đỏ trái · ✅ xanh phải · khoanh đỏ nét đứt vào nắp bình kín | Split 40/60 Before→After · G1–G5 PASS |
| **Thumb C (PA3 — Test & Compare)** | Chia phe 6+3 sát tiêu đề | **`SOW 6 IN JANUARY`** | **`SKIP THESE 3!`** | Badge ✅ xanh ô cải · badge ❌ đỏ ô cà chua héo · mũi tên vàng | 3 vùng bất đối xứng (bình sữa trái + 2 ô đối lập phải) · G1–G5 PASS |

---

## MASTER PROMPT A ⭐ (Clean Plate — Single Hero, ưu tiên render trước)

### 1. Clean-Plate Image Prompt (100% English · STRICTLY NO TEXT)
```text
A photorealistic 16:9 YouTube thumbnail background plate for a US home-gardening channel. Crisp winter daylight, vivid natural colors, ultra high contrast, shallow depth of field. NO human face, no full person (no hands needed).

SCENE: ONE dominant hero object placed firmly on the right 55% of the frame — a translucent plastic 1-gallon American milk jug resting outdoors on a dusting of fresh white snow beside a wooden backyard fence. The plastic milk cap is COMPLETELY REMOVED (open uncapped spout visible at the top). The jug is cut horizontally around the middle with a strip of silver duct tape sealing the seam, and the top slightly hinged open to reveal lush, bright emerald-green spinach and kale seedlings growing out of rich dark damp potting mix inside. Golden winter sunlight catches frost crystals on the jug and illuminates the vibrant green sprouts.

NEGATIVE SPACE: The left 45% of the frame is softly blurred dark winter pine foliage and shadowed dark backyard soil, clean and uncluttered, reserved for bold text overlay later.

STRICTLY NO TEXT, no letters, no words, no numbers, no arrows, no icons, no checkmarks, no labels, no logos, no watermark anywhere in the image.

Negative: no text, no typography, no letters, no numbers, no milk cap on spout, no covered porch roof, no face, no full person, no watermark, no logo, no UI, no distorted plastic.
```

### 2. Overlay Spec A (Canva / Photoshop / Pillow — 1280×720)
- **Vùng chữ:** Khối trái 45% (`x = 40..560`, `y = 90..560`), thêm dải gradient đen mờ trái→phải (`opacity 0.65 → 0`) giúp chữ nổi cực gắt trên Smart TV.
- **Dòng 1 (VÀNG `#FFD60A`):** `6 SEEDS` (cỡ lớn `Impact / Anton / Montserrat Black` ~125px, viền đen `stroke 10px` + drop shadow)
- **Dòng 2 (VÀNG `#FFD60A`):** `IN JANUARY` (~98px, viền đen `stroke 9px`) *(hoặc gộp 1 dòng `6 SEEDS IN JAN` nếu muốn 2 tầng cực gọn)*
- **Dòng 3 (TRẮNG `#FFFFFF`):** `NO GROW LIGHTS` (~74px, viền đen `stroke 8px`)
- **Markup vector:** 1 mũi tên cong màu vàng `#FFD60A` (viền đen 5px) đi từ cạnh phải chữ trỏ thẳng vào cụm mầm xanh bên trong bình sữa.

---

## MASTER PROMPT B (Clean Plate — Before→After ❌/✅, MODE 1 Test & Compare)

### 1. Clean-Plate Image Prompt (100% English · STRICTLY NO TEXT)
```text
A photorealistic 16:9 YouTube thumbnail background plate for a US home-gardening channel. Ultra high contrast, crisp macro garden photography, softly blurred backyard snow background. NO human face, no full person.

LAYOUT: An asymmetrical 40/60 vertical split comparison.
LEFT 40% (cooler, dimmer, muted tones): a translucent 1-gallon plastic milk jug outdoors in winter with the plastic cap STILL SCREWED TIGHTLY ON, heavy foggy condensation droplets trapping moisture inside, and limp, yellowed, waterlogged soggy sprouts sitting in dark overly wet soil at the bottom. Upper-left area darkened and softly blurred for text overlay later.
RIGHT 60% (bright, crisp golden winter sunlight, vivid colors): a translucent 1-gallon plastic milk jug sitting on light snow with the plastic cap COMPLETELY REMOVED (wide-open spout clearly visible), hinged cut sealed with silver duct tape, filled with healthy, compact, bright green leafy seedlings thriving in rich dark soil.

STRICTLY NO TEXT, no letters, no words, no numbers, no X marks, no checkmarks, no circles, no arrows, no labels, no watermark anywhere in the image.

Negative: no text, no typography, no letters, no numbers, no face, no full person, no icons, no watermark, no logo, no UI, no distorted shapes.
```

### 2. Overlay Spec B (Canva / Photoshop / Pillow — 1280×720)
- **Đường chia dọc:** thanh trắng 10px tại `x = 512` (40% trái / 60% phải).
- **Vùng chữ (dải tối gradient trên-trái `y = 24..300`):**
  - Dòng 1 (VÀNG `#FFD60A`, ~115px, stroke đen 9px): **`ROTTING SEEDS?`**
  - Dòng 2 (TRẮNG `#FFFFFF`, ~84px, stroke đen 8px): **`JANUARY JUG FIX`**
- **Markup vector sắc nét:**
  - **Khoanh đỏ nét đứt** (màu `#E83C34`, độ dày 8px) quanh chiếc nắp nhựa đang vặn kín ở bình bên trái.
  - **Badge tròn ❌ đỏ** (`#E83C34`, viền trắng 6px) góc dưới-trái (`cx=440, cy=635`).
  - **Badge tròn ✅ xanh** (`#46C85A`, viền trắng 6px) góc dưới-phải (`cx=1200, cy=635`).

---

## MASTER PROMPT C (PA3 — Clean Plate chia phe 6 sống / 3 hỏng, tùy chọn A/B với A)

### 1. Clean-Plate Image Prompt (100% English · STRICTLY NO TEXT)
```text
A photorealistic 16:9 YouTube thumbnail background plate for a US home-gardening channel. High contrast, crisp daylight, vivid natural colors. NO human face, no full person.

LAYOUT: Left 50% shows a translucent 1-gallon American milk jug with NO CAP sitting outdoors in light snow, dark blurred winter background behind the upper-left corner reserved for bold text overlay later. Right 50% is cleanly divided into two stacked close-up botanical panels:
- TOP-RIGHT PANEL (bright, crisp): lush green hardy spinach and kale seedlings thriving in dark damp potting mix inside a snowy garden light.
- BOTTOM-RIGHT PANEL (cooler, dramatic): a frost-bitten wilted young tomato seedling drooping on dark frosty soil.

STRICTLY NO TEXT, no letters, no words, no numbers, no checkmarks, no X marks, no arrows, no labels, no watermark anywhere in the image.

Negative: no text, no typography, no letters, no numbers, no face, no full person, no milk cap, no watermark, no logo, no UI.
```

### 2. Overlay Spec C (Canva / Photoshop / Pillow — 1280×720)
- **Vùng chữ góc trên-trái (`x = 36..600`, gradient tối):**
  - Dòng 1 (VÀNG `#FFD60A`, ~104px, stroke đen 9px): **`SOW 6 IN JANUARY`**
  - Dòng 2 (TRẮNG `#FFFFFF`, ~88px, stroke đen 8px): **`SKIP THESE 3!`**
- **Markup vector:** Badge **✅ xanh** góc trên-phải ô rau xanh · Badge **❌ đỏ** góc dưới-phải ô cà chua héo lạnh · 1 mũi tên cong vàng từ bình sữa trỏ vào ô ✅.

---

## Quy trình render & kiểm tra nhanh (Bước 3–4 skill `garden-us-thumbnail`)
1. Render 2 ảnh nền sạch (`thumbnail-a-clean.png` + `thumbnail-b-clean.png` hoặc `thumbnail-c-clean.png`) bằng Goha Studio **Nano Banana Pro (0 cr trên ULTRA)** hoặc ảnh stock thật từ `_LIBRARY/`.
2. Ghép chữ 2 tầng + markup vector sắc nét bằng **Canva / Photoshop** hoặc **Python Pillow** (`tools/garden_thumb_real.py`) xuất ra `1280×720` (`thumbnail-a.png`, `thumbnail-b.png`).
3. **Kiểm mắt ở 2 cỡ:** thu nhỏ **200px** (mobile feed) + mở **toàn màn hình** (mô phỏng Smart TV 2–3m) — xác nhận **0 chữ rác AI**, chữ VÀNG đọc trong 0,5 giây, bình sữa **không có nắp**.
