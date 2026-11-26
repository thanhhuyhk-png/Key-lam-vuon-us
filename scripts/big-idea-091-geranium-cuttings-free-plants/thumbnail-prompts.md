# Thumbnail prompts — big-idea-091 · Take Geranium Cuttings Now - Free Plants Next Spring (The 3-Inch Rule)

> Tạo 24/10/2026 bằng skill `garden-us-thumbnail`. **MODE 1 — CONCEPT TEST** (A và B khác hẳn đòn tâm lý; kênh đang trong giai đoạn demotion, nên không dùng MODE 2). Title GIỮ NGUYÊN (Test & Compare chỉ đổi thumbnail). Cặp mặc định theo skill: **Stat/Number shock × Verdict**. Chưa render — prompt 100% English, dán vào tool ảnh bất kỳ, hoặc nhờ tôi render bằng `tools/glabs_thumb.py`.

## Đầu vào đã kiểm
| Mục | Giá trị | Nguồn |
|---|---|---|
| Title | `Take Geranium Cuttings Now - Free Plants Next Spring (The 3-Inch Rule)` | outline.md |
| Lever title kéo | Kết quả↑ (free plants) + Công sức↓ (3-inch) + Thời gian↓ (now) | outline.md |
| Concept chốt từ outline | `$0 NURSERY BILL` (lever **chi phí**) — user duyệt 24/10 | outline.md `## Thumbnail` |
| Số có thật trong script | "three to four inches" (3–4 inch) · `$0` = cây mới không tốn tiền (M4 có câu scoping, `PROMISE_OK: free`) | script.md |
| Công thức kênh | FACELESS (tay-prop OK) · 2 tầng ALL CAPS · hook VÀNG + phụ TRẮNG · viền đen + bóng · markup đỏ nét đứt + ❌/✅ | thumbnail-stats (override) |

## Bảng biến thể
| | **A — Stat/Number shock** | **B — Verdict (Before→After ❌/✅)** |
|---|---|---|
| Concept | Bàn tay cầm đoạn ngọn phong lữ vừa cắt, thước (không số) bên cạnh, hàng chậu phong lữ nở rực mờ phía sau | Trái: lá phong lữ đóng sương, rìa đen (cách SAI: để ngoài trời) ❌ · Phải: đoạn ngọn xanh sạch trên tay + thước ✅ (cách ĐÚNG) |
| Đòn tâm lý | khao khát / giá trị (không mất tiền cây) | sợ mất cây → hành động ngay |
| Cảm-xúc-đích (G4) | **thoả mãn / khao khát** — vật tải: cành xanh khỏe + chậu hoa đỏ nở | **sợ-mất → nhẹ nhõm** — vật tải: lá bị sương cháy đen vs ngọn xanh |
| Text | hook **VÀNG** `$0` · phụ **TRẮNG** `NURSERY BILL` | hook **VÀNG** `FROST TONIGHT?` · phụ **TRẮNG** `SNIP 3-4 IN` |
| Số | `$0` (khớp M4) | `3-4` (khớp C01, script nói "three to four inches") |
| Triệu chứng (cổng #3 của kênh) | ⚠️ **chưa có bằng chữ** (chỉ có ảnh lá sương ở nền? không — A không có). Giữ nguyên chữ user đã duyệt; B bù | ✅ `FROST TONIGHT?` — thứ người xem đang lo |
| Complementarity với title | 0 từ trùng ✅ (`Free`≈`$0` cùng nghĩa khác chữ) | `3-4 IN` **ECHO có chủ đích** với "3-Inch Rule" (số, không phải từ); `FROST/TONIGHT/SNIP` không có trong title ✅ |
| Layout | ③ hero + badge `$0` · focal: bàn tay + ngọn ở **60%** trái | ① Before→After, **phải thống trị 60/40** |
| **GURU 5G** | G1 ✅ `$0` vàng cực to (1 token) · G2 ✅ 1 tiêu điểm (ngọn trên tay, ~60%) · G3 ✅ tự hỏi "ngọn cây nhỏ mà $0 là sao?" (đáp án trong video) · G4 ✅ (cành khỏe + hoa) · G5 ✅ nền tối ấm + đỏ hoa + vàng, không chìm trong biển xanh | G1 ✅ ≤3 từ/dòng · G2 ✅ phải 60% · G3 ✅ tự hỏi "snip chỗ nào, sao 3–4?" · G4 ✅ lá cháy vs ngọn xanh · G5 ✅ tông lạnh xanh-trắng (sương) vs ấm — phá nền xanh lá |
| Rủi ro render | bàn tay AI méo ngón; thước **không số** (tránh AI chế chữ) | nhiều element (❌ + ✅ + khoanh + thước) → chữ dễ méo; đã rút hook còn 2 từ |

> **Biến chính test:** A không có triệu chứng bằng chữ, B có. Câu hỏi retro: **số + triệu chứng (B) có thắng "$ + lợi ích" (A) không?** — khớp bài học kênh (mẫu `TURNING MUSHY? 5 FIXES INSIDE` 2,7% vs câu hỏi trống 1,5%). Nếu B thắng, bài sau bỏ concept "chi phí" trần.

---

## MASTER PROMPT A — Stat/Number shock
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–70. Vivid saturated colors, ultra high contrast, warm porch-light bokeh background. NO human face, no full person (a single hand as a prop is allowed only as described below).

SCENE: LEFT 60% of the frame is ONE single hero: a close-up of a single hand holding upright a freshly cut red-geranium stem tip — bright green leaves clustered at the top, a bare green stem below, a clean cut at the bottom end. A plain wooden ruler stands beside the stem to show its length; the ruler has NO numbers, NO letters and NO printed marks that look like text. A bold red dashed circle is drawn around the clean cut end. RIGHT 40% of the frame: a softly blurred (out-of-focus) porch rail with a row of terracotta pots of red geraniums in full bloom. Dark warm background, macro look, shallow depth of field.

TEXT — render EXACTLY these two stacked lines in very thick bold sans-serif, heavy black outline and drop shadow, placed in the upper-right negative space, NOT covering the hand or the stem: line 1 "$0" in very large bright YELLOW; line 2 "NURSERY BILL" in WHITE. The ONLY text in the entire image is exactly these: "$0" in yellow and "NURSERY BILL" in white, spelled letter for letter. Do NOT translate. Do NOT add any other text, letters, numbers, words, captions, labels or watermark anywhere.

Negative: no face, no full person, no second hero object, no extra text, no gibberish letters, no numbers on the ruler, no watermark, no logo, no UI, no distorted or extra fingers.
```

## MASTER PROMPT B — Verdict (Before→After ❌/✅)
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 35–70. Vivid saturated colors, ultra high contrast, blurred garden background. NO human face, no full person (a single hand as a prop is allowed only as described below).

LAYOUT: a clean before→after split. The RIGHT side is dominant, about 60% of the frame; the LEFT side about 40%.
LEFT (the wrong way, cold blue-white tone): a cluster of red-geranium leaves covered in white frost crystals, leaf edges blackened by the cold. A bold red dashed circle around the frozen leaf edge and a large red ❌ over it.
RIGHT (the fix, warm light): a single hand holding upright a clean, freshly cut green geranium stem tip with a few green leaves at the top. A plain wooden ruler stands beside it; the ruler has NO numbers, NO letters and NO marks that look like text. A bright green ✅ on this side.

TEXT — render EXACTLY these two stacked lines in very thick bold sans-serif, heavy black outline and drop shadow, in the negative space at the top, NOT covering the leaves, the hand or the stem: line 1 "FROST TONIGHT?" in bright YELLOW; line 2 "SNIP 3-4 IN" in WHITE. The ONLY text in the entire image is exactly these: "FROST TONIGHT?" in yellow and "SNIP 3-4 IN" in white, spelled letter for letter. Do NOT translate. Do NOT add any other text, letters, numbers, words, captions, labels or watermark anywhere.

Negative: no face, no full person, no extra text, no gibberish letters, no numbers on the ruler, no watermark, no logo, no UI, no distorted or extra fingers, no animals.
```
> Nếu chữ bị méo sau 3 lần render: rút B còn `FROST?` / `SNIP 3-4 IN`, bỏ khoanh đỏ trước, giữ ❌ ✅ (skill: chữ đúng chính tả > markup đẹp). KHÔNG chuyển sang overlay Canva; giữ ảnh hoàn chỉnh từ prompt.

## Guardrail đã kiểm
- ✅ Số khớp script (`3-4` = "three to four inches", C01; `$0` = cây mới, M4 có câu scoping) · ✅ không "100%/GUARANTEED/SHOCKING" · ✅ không human-fear (sương làm cháy lá là botanical) · ✅ faceless (tay-prop) · ✅ không động vật · ✅ không nhãn tuổi trên thumbnail (L9).
- ⚠️ "FROST TONIGHT?" ngầm nói "đêm nay"; video đăng tuần đầu tháng 11 nên vùng lạnh khớp, vùng ấm (Zone 9–10) không có sương → thumbnail B kém liên quan với họ. Ghi vào retro nếu B thắng ở vùng lạnh nhưng thua ở vùng ấm (xem Demographics theo địa lý).
- Mô tả/pinned comment không lặp chữ thumbnail.

## GATE
Chọn **A** hay **B** để render, hoặc **cả hai** để dùng Test & Compare của YouTube (đề xuất, vì MODE 1 sinh ra để thử concept). Chưa render để khỏi tiêu credit trước khi bạn chọn.
