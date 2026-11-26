# Pipeline State — big-idea-041-plants-cant-kill-water

> Auto-tracked. ✅ xong · ⬜ chưa làm. Cập nhật ở mỗi GATE.
> Source: BRIEF-4-SCRIPTS-2026-W34.md → BÀI 1 (ưu tiên cao nhất)
> Last sync: 2026-08-19

**Title chốt (đổi 02/09/2026 — L9):** `7 Plants You Can't Kill — They Grow in Just Water, No Soil` (57 ký tự · nguyên Title B)
**Title á quân (swap giờ 48 nếu CTR <4%):** `7 Indoor Plants That Grow in Just Water (No Soil Needed)`
**Thumb chốt:** VÀNG `THESE 7 CAN'T DIE` / TRẮNG `NO SOIL · NO COST` (P2 — số lên dòng vàng) — ✅ sạch L9, **KHÔNG đổi**

> ### 🔴 Title A đã bị RÚT 02/09/2026 — `7 Plants You Can't Kill — No Soil, No Bending, No Cost`
>
> Title A được chọn ở GATE 1 (19/08) vì *"khớp chính xác công thức L8"*. **L8 đã bị thu hẹp 02/09 và
> phần đó bị `L9` ghi đè** — `No Bending` là chữ chỉ tuổi người xem, cấm trong title + chữ thumbnail.
> Title B từng bị loại vì *"bỏ 2/3 vế"* theo luật ba-vế của brief — **luật đó đã huỷ** (`SLATE-2026-W34.md`).
>
> Bốn bằng chứng: 3 bản cùng đề tài (973.416 / 15.891 / 363) · cặp nha đam (83.703 / 209) ·
> A/B 31/08 (`NO BENDING` 40,3% thua `PLANT ONCE` 59,7%) · Evergreen Seniors 119K sub, top-10 view 0/10 mang chữ chỉ tuổi.
> Xem `references/lessons-learned.md` L9/L9b + `references/impressions-baseline-2026-09-02.md`.
>
> **ES cũng đã đổi:** ~~`Sin Tierra, Sin Agacharse, Sin Gastar`~~ → `Crecen Solo en Agua, Sin Tierra`.
> **Thân kịch bản ⛔ KHÔNG đổi** — L9 chỉ cấm nhãn tuổi trên *title/thumbnail*, nội dung ergonomic
> (beat "no bending" ở 0:45–0:55 và 5:10 trong `retention-spine.md`) **giữ nguyên, vẫn phục vụ đúng khán giả**.

| # | Bước | Skill | Output | Trạng thái |
|---|------|-------|--------|-----------|
| 1 | Outline | mkt-youtube-outline | outline.md | ✅ |
| 1.5 | Deep Research | mkt-youtube-deep-research | research-brief.md | ✅ |
| 2 | Hook (GATE) | mkt-hook-kallaway | (in script) | ✅ |
| 2.5 | Retention Spine | playbook P2S (Pha A+B) | retention-spine.md | ✅ |
| 3 | Script EN | youtube-garden-us | script.md | ✅ (1,500 từ · 10.0′ · Compliance 10/10) |
| 3.2 | Audit độc lập | mkt-youtube-script-audit | audit-report.md | ✅ (REVISE → vá 5/5 → PUBLISH) |
| 3.5 | Prediction | templates/prediction.template.md | prediction.md | ✅ |
| 4a | SEO EN | mkt-yt-seo-description | seo-en.md | ✅ |
| 4b | Translate ES | mkt-yt-translate-es | script-es.md | ✅ (62/62 đoạn khớp) |
| 4c | SEO ES | mkt-yt-seo-description | seo-es.md | ✅ |
| 5 | Thumbnail prompts | garden-us-thumbnail | thumbnail-prompts.md | ✅ prompt A/B xong — 🔴 render ảnh CHỜ API key (GEMINI_API_KEY / AI33_KEY không có trong hệ thống) |
| 6 | Retro | yt_analytics.py retro | retro.md | ⬜ (7–14 ngày sau publish) |

**Tiến độ:** 8/8 bước pipeline ✅ **HOÀN TẤT** (thumbnail + retro tính riêng)

---

## Danh sách 7 cây (đã chốt sau research)

① Pothos · ② Lucky bamboo · ③ Heartleaf philodendron · ④ **Wandering dude** (mốc open loop) ·
⑤ English ivy · ⑥ Coleus · ⑦ Spider plant

🔴 **Chinese evergreen bị LOẠI ở Bước 1.5** — không nguồn extension/đại học nào xác nhận sống trong
nước thuần dài hạn. Thay bằng **coleus** (UW Miller Library: hàng tuần–hàng tháng, rễ 7–12 ngày).

---

## ⚠️ Lưu ý bắt buộc trước khi đăng

1. **Bật "Altered or synthetic content"** khi upload (kênh dùng AI voice).
2. **Chapters là ước tính** từ word-index của script — chỉnh lại theo bản dựng cuối. Mốc `0:00` phải giữ.
   Bản ES dài hơn EN ~12% → **timestamps ES khác EN**, đừng copy sang.
3. **CTR phải nhập tay** từ Studio (API không expose) để điền `retro.md`.
4. **POST-PUBLISH TITLE PROTOCOL:** giờ thứ 48, nếu CTR < 4% → swap sang title á quân
   (`7 Indoor Plants That Grow in Just Water (No Soil Needed)`), **giữ nguyên thumbnail**,
   ghi lại CTR trước/sau. Không đổi title + thumbnail cùng lúc.
   ⛔ **Á quân TUYỆT ĐỐI không được là bản có `No Bending` / `No Back Pain`** — đó là biến đang test.
   Đổi ngược lại nó là phá hỏng phép thử.

5. 🔴 **VIDEO ĐÃ LÊN LỊCH TRƯỚC KHI ĐỔI TITLE (02/09).** Phải vào YouTube Studio sửa **title EN + ES**
   trên bản đã lên lịch. File trong repo ⛔ không tự đồng bộ sang Studio.

## 📌 Trùng lặp cần xử lý (không thuộc pipeline này)

Tồn tại script gần trùng **chưa đăng**: `scripts/content-plan-v01-grow-7-in-water/`
(title = `If You Keep Killing Plants, Grow These 7 in Water`, 9.9′, Compliance 10/10, rewrite 2026-07-04).
Trùng chủ đề và 5/7 cây với bài 041. **Quyết định cần user:** bỏ hẳn bản cũ, hay đăng cách bài 041 vài tuần
với title/góc khác hẳn. Đăng gần nhau = tự cạnh tranh + rủi ro tín hiệu lặp nội dung.

## 🔬 Giả thuyết video này đang test (xem `prediction.md`)

1. Đóng gói là nút thắt (không phải nội dung) — test bằng thumbnail có số ở dòng vàng. ✅ giữ
2. ~~Triple pain-removal stack tái lập được sau thất bại bản 22/07 ("no smell, no mess" → 324 view).~~
   🔴 **GIẢ THUYẾT ĐÃ CHẾT 02/09** — bản 22/07 chết vì đuôi `| Gardening for Elderly`, ⛔ không phải
   vì đổi "smell/mess". Và bản "đúng ba vế" (20/03) cũng đã thua bản không-nhãn **20,7 lần** ở tổng giờ xem.
   **→ THAY BẰNG:** *Title bỏ hết chữ chỉ tuổi người xem sẽ kéo **hiển thị + CTR** lên, trong khi
   AVD giữ nguyên hoặc giảm nhẹ.* Đây là **phép thử chính thức của `L9`** — cùng đề tài đã có 3 mốc
   so (973.416 / 15.891 / 363), nên đọc kết quả rất sạch.
3. Honesty layer (dám nói 5/7 cây chỉ sống vài tháng + nêu nguồn khuyến cáo ngược) **không** giết retention. ✅ giữ

> ⚠️ **Đây là video thứ 5 cùng đề tài "cây trồng trong nước" của kênh.** Đăng để **đọc L9**,
> ⛔ không phải để mở lại loạt bài. Kết quả thế nào cũng **dừng loạt này sau đó** — rủi ro tín hiệu
> nội dung lặp (đã được cảnh báo trong `SLATE-2026-W34.md` cho khuôn "Save a Dying [cây]").
