# Thumbnail prompts — big-idea-062 · Grow Vegetables Indoors This Winter (5 Easy, 2 Need a Light)

> MODE 1 (Concept test) — bắt buộc vì kênh đang trong giai đoạn Browse demotion / impression thấp (KPI view 5 ngày < 500). A và B khác concept, khác cảm xúc, đều on-formula (faceless, vàng + trắng, markup đỏ).
> Cặp mặc định theo công thức hiện hành: **Stat/Number shock × Verdict**, cả hai có SỐ + TRIỆU CHỨNG.
> Concept ở `outline.md` (`WINDOW or LAMP?`) **được giữ làm ý tưởng hình** (cửa sổ vs đèn), nhưng chữ đã đổi sang số + triệu chứng để qua gate §C.3 của skill (câu hỏi trống không số từng cho CTR thấp nhất kênh).
> Prompt chỉ để xuất ảnh. **Chưa render.**

## Bảng biến thể
| | Concept | Cảm-xúc-đích (G4) | Text | Layout | Màu chữ | Lever kéo | GURU 5G |
|---|---|---|---|---|---|---|---|
| **A** | Verdict / Before→After | lo → nhẹ nhõm (cây gầy vươn kính → cây khỏe dưới đèn) | `LEGGY?` / `6-8 HOURS` | Before→After ❌/✅ (60/40, bên đèn to hơn) | Vàng + Trắng | Chắc-thắng↑ (biết dấu hiệu + mức sáng) | ✅ |
| **B** | Curiosity + số (Stat) | tò mò (vì sao cần tối?) | `NO FRUIT?` / `6 HOURS DARK` | Single hero lệch phải + chữ ở negative space | Vàng + Trắng | Kết quả↑ + tò mò (đáp án nằm trong video) | ✅ |

### Complementarity Test (title ↔ thumbnail)
Title (v3, 18/10): *Grow, Vegetables, Indoors, This, Winter, 5, Can, Use, a, Window, 2, Need, a, Lamp.* (title cũ: 5 Easy, 2 Need a Light — thumbnail A/B không đổi, vẫn 0 từ trùng)
- A: LEGGY · 6-8 · HOURS → **0 từ trùng** ✅
- B: NO · FRUIT · 6 · HOURS · DARK → **0 từ trùng** ✅ (số 6 khác số 5 và 2 ở title)
Title lo SEO + lời hứa "5 + 2"; thumbnail lo dấu hiệu (A) và câu hỏi về bóng tối (B).

### Số trên ảnh = số trong script (zero hallucination)
| Số | Script | Mã claim |
|---|---|---|
| `6-8 HOURS` (A) | "lettuce and herbs usually need six to eight hours of bright light every day" | CL-001 (Illinois Extension 2017) |
| `6 HOURS DARK` (B) | "tomatoes actually need about six hours of dark to fruit" | CL-011 (UNH Extension Q&A 2021) |
⚠️ B chỉ đúng cho **cà chua**; ớt thì không cần (script nói rõ). Hình B vẽ cà chua.

### 5 GURU gate
| Gate | A | B |
|---|---|---|
| G1 Squint (200px: đọc được chữ vàng + thấy chủ thể) | ✅ `LEGGY?` 1 từ, cây gầy to | ✅ `NO FRUIT?` ≤3 từ; cà chua con ≥40% khung |
| G2 One focal point (60/40) | ✅ bên đèn thống trị | ✅ một hero, nền mờ |
| G3 Curiosity gap (câu hỏi gieo, đáp án giấu) | ✅ "mình dính kiểu gầy này không, và mấy giờ sáng đủ?" | ✅ "vì sao cà chua cần tối mà không có quả?" (đáp án ở video) |
| G4 Emotional proxy (trạng thái vật thể gánh cảm xúc) | ✅ cây nhợt vươn kính vs cây dày xanh | ✅ hoa vàng nhỏ chưa đậu quả dưới ánh đèn vs đêm xanh thẫm |
| G5 Pattern-interrupt (chống chìm trong biển xanh lá) | ✅ trái xám lạnh + phải tím-hồng ấm từ đèn + khoanh đỏ | ✅ nền xanh navy đêm + ánh đèn ấm + hoa vàng |

## MASTER PROMPT A — Verdict / Before→After (layout WIN)
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred kitchen background. NO human face, no full person, no hands.

LAYOUT: a before→after split, two halves, the RIGHT half slightly larger and brighter (about 60/40).
LEFT HALF (the problem): a kitchen windowsill in cold gray winter light with a small tray of pale, thin, stretched seedlings all bending toward the glass. A bold red dashed circle around the thin bending stems and a large red ❌ over the tray.
RIGHT HALF (the fix): the same kind of tray on a shelf under a small shop lamp a few inches above, giving a warm pink-purple glow, with short, sturdy, deep-green seedlings standing straight. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline and drop shadow, in the negative space, NOT covering the trays: line 1 "LEGGY?" in bright YELLOW, line 2 "6-8 HOURS" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no hands, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no brand names, no extra objects.
```

## MASTER PROMPT B — Curiosity + số (single hero)
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred background. NO human face, no full person, no hands.

SCENE: ONE single hero object only — a small potted tomato plant with a few tiny yellow flowers and no fruit, placed on the right side under a small shop lamp with a warm glow. Behind it, a dark navy-blue night window with a crescent moon. Macro, shallow depth of field, clean negative space on the left. A curved yellow arrow pointing from the lamp to the flowers.

TEXT — render EXACTLY two stacked lines in very thick bold sans-serif, heavy black outline and drop shadow, in the negative space on the left, NOT covering the plant: line 1 "NO FRUIT?" in bright YELLOW, line 2 "6 HOURS DARK" in WHITE. The ONLY text in the entire image is exactly these two lines, spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.

Negative: no face, no full person, no hands, no second plant, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes, no brand names.
```

## Kết quả render (17/10, G-Labs · nano_banana_pro 16:9, 2752×1536)
`thumbnail-a.jpg` · `thumbnail-b.jpg` — chạy bằng `tools/glabs_thumb.py` (lần đầu cho cả hai, không phải render lại).
- **Chữ:** cả hai đúng chính tả, đúng hai dòng, không chữ thừa; vàng + trắng, viền đen dày. ✅
- **A:** ❌/✅ rõ, khoanh đỏ nét đứt đúng chỗ; tỉ lệ gần 50/50 (ít hơn 60/40 yêu cầu). ⚠️ `6-8 HOURS` đứng cạnh hình đèn nên có thể bị đọc là "đèn chạy 6–8 giờ"; thực ra số này là giờ sáng mạnh cho rau lá/thảo mộc (CL-001). Nếu muốn tránh nhầm: `6-8 HRS SUN`? (6 ký tự thêm, kiểm lại G1) hoặc bỏ đèn khỏi nửa phải.
- **B:** cà chua, hoa vàng, trăng, mũi tên đều đúng prompt. ⚠️ đèn đang **bật** trong đêm trong khi chữ nói "6 HOURS DARK"; có thể hiểu là "đèn bật cả đêm làm cây không quả" (khớp câu hỏi), nhưng nếu muốn thẳng nghĩa hơn hãy tắt đèn và chỉ giữ ánh trăng.
- Cả hai là ảnh AI dựng, không phải kết quả thật của kênh.

## Render (đã chạy; lệnh gốc để tham khảo)
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" -o "D:/0002-Team A Nam/scripts/big-idea-062-sunny-window-winter-veggies/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" -o "D:/0002-Team A Nam/scripts/big-idea-062-sunny-window-winter-veggies/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
Nếu chữ baked sai sau 3 lần: rút A còn `LEGGY?` + `6-8 HRS`, hoặc B còn `NO FRUIT?` một dòng; đừng chuyển sang overlay.

## Ghi chú
- Thumbnail là hình minh họa dựng; không phải kết quả thực hiện thật của kênh. Trong video, cảnh minh họa dùng nhãn `illustration` (xem `shot-plan.md`).
- A/B theo MODE 1 trong Test & Compare của YouTube; đọc kết quả sau ≥ vài nghìn impression, tránh kết luận từ mẫu nhỏ (kênh đang impression thấp).
- Đọc cùng chủ đề: bài 061 (lemon) dùng cặp A `NO BUDS? / 6–8 HRS`, B `BUDS DROPPING? / 55–65°F NIGHTS` — khung giống nhau (câu hỏi triệu chứng + số). Khác hình và chủ đề, nhưng cùng khuôn chữ → cân nhắc đổi cấu trúc chữ ở bài sau để tránh khuôn.
