# Thumbnail prompts — big-idea-097 · Stop Buying Fruit Bushes: Grow 6 for Free From Winter Cuttings

> garden-us-thumbnail · **MODE 1 (Concept test)** · 18/11/2026 · CHỈ tạo prompt, **chưa render** (render tốn credit — chờ user duyệt).
> Packaging-first: A dùng đúng concept đã chốt ở `outline.md` (FROM A STICK, Reveal). Title giữ nguyên (Test & Compare chỉ đổi thumbnail).
> Đổi so với outline: **bỏ nhãn giá `$25 → $0`** (research-brief C48: không có nguồn giá). Thay bằng cặp «cây mua ở vườn ươm ❌ → cành trơ ✅» không có số tiền.

## Khoá chủ đề
- **Title:** `Stop Buying Fruit Bushes: Grow 6 for Free From Winter Cuttings` — lever title: Kết quả↑ (6 cây) + Công sức↓/chi phí↓ (free).
- **Lever thumbnail:** Cảm giác chắc thắng↑ bằng **cơ chế nhìn thấy được** (cành trơ → cây) (A) · Curiosity bằng **ngoại lệ trung thực** (táo hiếm ra rễ) (B) — khác lever title.
- **Số/chữ trên thumbnail = trong script:** A `3 BUDS` = «Aim for three buds» (C02) · B `NOT APPLES` = «apples don't root well» (C33).
- ⚠️ Thumbnail không mang điều kiện «cần cây mẹ / dormant / cắm khi đất mềm». Chấp nhận: script nói điều kiện ở hook (0:20) và M1; không thêm số khác.

## Bảng biến thể (MODE 1: 2 archetype KHÁC ĐÒN TÂM LÝ)
| Biến thể | Archetype | Cảm-xúc-đích | Text (vàng / trắng) | Layout | Vật mang cảm xúc | Complementarity (0 từ trùng title) |
|---|---|---|---|---|---|---|
| **A ⭐** | Reveal / Before→After | ngạc nhiên, «ồ, vậy thôi à?» | `FROM A STICK` / `3 BUDS` | ① before→after (trái ❌ cây nhà vườn ươm · phải ✅ cành trơ) | cành nho trơ cỡ bút chì cắm vào đất, 3 chồi nhìn thấy | ✅ from/a/stick/3/buds ≠ stop/buying/fruit/bushes/grow/6/free/winter/cuttings |
| **B** | Callout phủ định / Warning nhẹ | tò mò, «ủa, sao táo không?» | `NOT APPLES` / `TRY THESE` | ③ split: trái táo ❌ · phải chùm nho/lý chua ✅ | quả táo bị gạch đỏ cạnh cành cắt | ✅ not/apples/try/these ≠ title |

**Guardrails đã kiểm:** faceless (không người/mặt/tay) · không động vật (đặc biệt không chó gần nho — luật ASPCA trong script) · không chữ sợ · không «Don't» · không nhãn tuổi · không 100%/guaranteed · số khớp script · không nhãn giá · **không dùng cảnh cành cắm vào đất tuyết/đóng băng** (trái câu «plant when soil softens») → đất nâu mềm, không tuyết ở khung cắm · cây là *Vitis* (nho) thật, không dùng sung cảnh *Ficus benjamina* · không nhãn thương hiệu/nhãn PP thật.

## PROMPT A ⭐ — Reveal: `FROM A STICK` / `3 BUDS`
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–80. Vivid saturated colors, ultra high contrast. NO human face, no full person, no hands, no animals.

SCENE: a clean split composition. ONE hero object: a bare, leafless grape vine cutting about as thick as a pencil, with exactly three small plump buds clearly visible along the stem, pushed upright into soft dark-brown garden soil, bright morning light, sharp focus, macro, shallow depth of field. The cutting fills the right 55% of the frame. On the left, smaller and slightly blurred, a potted nursery grape plant with a plain blank plastic tag (no price, no brand, no readable text), with a bold red X over it. The background is a softly blurred late-winter garden with bare branches and a wooden fence, bare brown soil, no snow around the cutting.

TEXT: the ONLY text in the entire image is exactly two lines, spelled letter for letter, nothing else: line 1 "FROM A STICK" in bright YELLOW, line 2 "3 BUDS" in WHITE. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow, stacked in the clean negative space at the top left, NOT covering the cutting. Render this text exactly, do NOT translate it, do NOT add any other text, words, letters, numbers, prices or captions anywhere.

Negative: no face, no person, no hands, no animals, no dog, no price tag text, no brand logo, no snow on the cutting, no extra text, no gibberish letters, no watermark, no UI, no distorted shapes.
```

## PROMPT B — Callout phủ định: `NOT APPLES` / `TRY THESE`
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–80. Vivid saturated colors, ultra high contrast. NO human face, no full person, no hands, no animals.

SCENE: a clean split frame, dark soil table surface. LEFT 45%: one large glossy red apple with a bold red X drawn over it, a short bare apple twig lying beside it. RIGHT 55%: a small ripe cluster of dark purple grapes and a bunch of red currants on a bare dormant winter cutting stem about as thick as a pencil. Sharp focus, macro, shallow depth of field, soft cold winter light, background softly blurred bare winter garden.

TEXT: the ONLY text in the entire image is exactly two lines, spelled letter for letter, nothing else: line 1 "NOT APPLES" in bright YELLOW, line 2 "TRY THESE" in WHITE. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow, stacked in the clean negative space at the top, NOT covering the fruit. Render this text exactly, do NOT translate it, do NOT add any other text, words, letters, numbers or captions anywhere.

Negative: no face, no person, no hands, no animals, no dog, no price tag, no brand logo, no extra text, no gibberish letters, no watermark, no UI, no distorted shapes.
```

## Quy tắc chọn
- **A ⭐** nếu cần giữ lời hứa «free / from a stick» và hợp hook A. **B** hợp nếu muốn test curiosity «ngoại lệ táo» — nhưng thumbnail không có «free/6», cần title giữ gánh lời hứa.
- Render: chờ user chọn A/B → chạy `tools/glabs_thumb.py` (khoá ở workspace Quân sự — memory reference-glabs-image-server) hoặc Nano Banana Pro; **chưa render**.
