# Thumbnail prompts — big-idea-098 · 4 Amish Fall Garden Habits That Beat a Rototiller

> MODE 1 (Concept test) · 18/11/2026 · CHỈ tạo prompt, **chưa render** (render tốn credit — chờ user duyệt).
> Packaging-first: A dùng concept đã chốt ở `outline.md` (`LEAVES ✅` vs máy xới ❌). Title giữ nguyên; Test & Compare chỉ đổi thumbnail.

## Khoá chủ đề
- **Title:** `4 Amish Fall Garden Habits That Beat a Rototiller` — lever title: Kết quả↑ (đất tốt hơn) + Công sức↓ (không máy).
- **Lever thumbnail:** A = chi phí↓ / dễ làm (thứ thay máy là **lá rụng miễn phí**) · B = Cảm giác chắc thắng↑ bằng **cơ chế nhìn thấy được** (đất tơi như bọt biển vs bột).
- **Chữ trên thumbnail = có trong script:** A `LEAVES` = «a blanket of leaves» (H3) · `FREE` = «Those bags are free mulch» · B `SPONGE` / `NOT FLOUR` = ẩn dụ M1 «Healthy soil is the sponge… Tilling turns it into flour».
- ⛔ Không dùng hình người Amish (mặt, trang phục nhận diện được) — tôn trọng cộng đồng và tránh hình AI giả tư liệu. Không «Amish» trên thumbnail (title đã mang keyword; 0 từ trùng).

## Bảng biến thể (MODE 1: 2 archetype KHÁC ĐÒN TÂM LÝ)
| Biến thể | Archetype | Cảm-xúc-đích | Text (vàng / trắng) | Layout | Vật mang cảm xúc | Complementarity (0 từ trùng title) |
|---|---|---|---|---|---|---|
| **A ⭐** | Before→After / Callout | nhẹ nhõm, «khỏi mua máy» | `LEAVES ✅` / `FREE` | ① split: trái máy xới trên đất bột xám ❌ · phải luống phủ lá nâu băm dày ✅ | đống lá băm dày trên luống, góc lộ đất đen tơi | ✅ leaves/free ≠ 4/amish/fall/garden/habits/beat/rototiller |
| **B** | Reveal / So sánh cơ chế | tò mò, «đất mình là loại nào?» | `SPONGE` / `NOT FLOUR` | ③ hai nắm đất cận cảnh: trái đất tơi có lỗ, sợi nấm trắng, giun ✅ · phải đất bột mịn khô ❌ | hai cục đất đặt cạnh nhau | ✅ 0 từ trùng |

**Guardrails đã kiểm:** faceless (không người/mặt/tay) · không động vật ngoài giun · không chữ sợ · không «Don't/Never» · không nhãn tuổi · không 100%/guaranteed · không nhãn giá · không người Amish.

## PROMPT A ⭐ — `LEAVES ✅` / `FREE`
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–80. Vivid saturated colors, ultra high contrast. NO human face, no person, no hands, no animals.

SCENE: a clean split composition of one backyard vegetable bed in late fall. LEFT 40%: a gas-powered rototiller standing on flat, pale gray, powdery dry soil, slightly desaturated, with a bold red X drawn over the tiller. RIGHT 60%: the same bed covered in a thick, fluffy layer of shredded brown and orange autumn leaves about eight inches deep, a small corner pulled back to reveal dark, crumbly, moist soil, warm golden late-afternoon light, sharp focus. A small bold green check mark near the leaves.

TEXT: the ONLY text in the entire image is exactly two lines, spelled letter for letter, nothing else: line 1 "LEAVES" in bright YELLOW, line 2 "FREE" in WHITE. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow, stacked in clean negative space at the top right above the leaves, NOT covering the soil corner.

Negative: no face, no person, no hands, no animals, no Amish people, no buggy, no horse, no brand logo on the tiller, no price tag, no extra text, no gibberish letters, no watermark, no UI, no distorted machinery.
```

## PROMPT B — `SPONGE` / `NOT FLOUR`
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–80. Vivid saturated colors, ultra high contrast. NO human face, no person, no hands.

SCENE: two clumps of garden soil side by side on a rustic wooden board, macro, shallow depth of field. LEFT 55%: a dark, moist, crumbly soil clump full of small air pockets and root channels, fine white fungal threads visible, one earthworm partly emerging, a green check mark. RIGHT 45%: a pile of pale, dry, fine powdery soil like flour, a little dust in the air, a bold red X. Soft natural daylight.

TEXT: the ONLY text in the entire image is exactly two lines, spelled letter for letter, nothing else: line 1 "SPONGE" in bright YELLOW above the left clump, line 2 "NOT FLOUR" in WHITE above the right pile. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow, NOT covering the soil.

Negative: no face, no person, no hands, no Amish people, no bread, no kitchen flour bag, no extra text, no gibberish letters, no watermark, no UI.
```

## Quy tắc chọn
- **A ⭐** khớp concept đã chốt ở GATE [1] và lời hứa «không máy». **B** test curiosity cơ chế — hợp hook A′ (đất bột) nhưng không nói «thay máy bằng gì».
- Render: chờ user chọn A/B → `tools/glabs_thumb.py` (khoá ở workspace Quân sự — memory reference-glabs-image-server) hoặc Nano Banana Pro; **chưa render**.
