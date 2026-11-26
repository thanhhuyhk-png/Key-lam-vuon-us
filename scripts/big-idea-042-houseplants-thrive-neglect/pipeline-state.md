# Pipeline State — big-idea-042-houseplants-thrive-neglect

> Auto-tracked. ✅ xong · ⬜ chưa làm. Cập nhật ở mỗi GATE.
> Source: BRIEF-4-SCRIPTS-2026-W34.md → BÀI 2
> Last sync: 2026-08-19

**Title chốt:** `5 Houseplants That Get Healthier When You Forget to Water Them` (63 ký tự)
**Thumb chốt:** VÀNG `THESE 5 LOVE NEGLECT` / TRẮNG `STOP WATERING SO MUCH` — Before→After layout

| # | Bước | Skill | Output | Trạng thái |
|---|------|-------|--------|-----------|
| 1 | Outline | mkt-youtube-outline | outline.md | ✅ |
| 1.5 | Deep Research | mkt-youtube-deep-research | research-brief.md | ✅ |
| 2 | Hook (GATE) | mkt-hook-kallaway | (in script) | ✅ |
| 2.5 | Retention Spine | playbook P2S (Pha A+B) | retention-spine.md | ✅ |
| 3 | Script EN | youtube-garden-us | script.md | ✅ (1,203 từ · 8.0′) |
| 3.2 | Audit độc lập | mkt-youtube-script-audit | audit-report.md | ✅ (REVISE → vá 3/3 → PUBLISH) |
| 3.5 | Prediction | templates/prediction.template.md | prediction.md | ✅ |
| 4a | SEO EN | mkt-yt-seo-description | seo-en.md | ✅ |
| 4b | Translate ES | mkt-yt-translate-es | script-es.md | ✅ (23/23 đoạn khớp) |
| 4c | SEO ES | mkt-yt-seo-description | seo-es.md | ✅ |
| 5 | Thumbnail prompts | garden-us-thumbnail | thumbnail-prompts.md | ✅ prompt A/B xong — 🔴 render ảnh CHỜ API key (GEMINI_API_KEY / AI33_KEY không có trong hệ thống) |
| 6 | Retro | yt_analytics.py retro | retro.md | ⬜ (7–14 ngày sau publish) |

**Tiến độ:** 8/8 bước pipeline ✅ **HOÀN TẤT** (thumbnail + retro tính riêng)

---

## Danh sách 5 cây (đã chốt sau research)

① ZZ plant · ② Jade plant · ③ **Ponytail palm** (mốc "silent killer" của open loop) · ④ Cast iron plant · ⑤ Dracaena

Cả 5 cây đều có nguồn Clemson HGIC hoặc NYBG — mạnh hơn dự kiến ban đầu (outline lo ngại chỉ có nguồn
blog thương mại). Đã né aloe/snake plant (bão hoà) và pothos (trùng cây chính BÀI 1 cùng tuần).

---

## ⚠️ Sửa quan trọng sau audit độc lập (2026-08-19)

Script viết inline rồi tự audit độc lập ngay sau đó (chạy auto theo yêu cầu "duyệt và tự động làm tới
cuối" — không có GATE trung gian với user), phát hiện **3 lỗi** trước khi hoàn tất:

1. 🔴 **Pet-safety oversimplification** — "chỉ đau bụng, không gì nghiêm trọng hơn" hạ thấp phổ triệu
   chứng ASPCA thật (nôn ra máu, giãn đồng tử, khó nuốt tuỳ cây). Đã vá thành khoanh vùng đúng mức.
2. 🔴 **Misquote NYBG** — script gán chữ "water tank" cho NYBG trong khi nguồn dùng "water storage".
   Đã sửa thành diễn giải đúng, không gán sai từ.
3. 🔴 **Timeline claim sai** — "Last week we covered seven plants..." nhưng brief xác nhận cả 4 video
   cùng tuần W34 (4 video/tuần), không cách nhau 1 tuần. Đã bỏ, thay bằng forward-visual close +
   identity CTA + câu hỏi comment + tease BÀI 3 (bridge tự nhiên vì pet-safety vừa nói xong).

Chi tiết đầy đủ: [audit-report.md](audit-report.md).

## ⚠️ Lưu ý bắt buộc trước khi đăng

1. **Bật "Altered or synthetic content"** khi upload.
2. **Chapters là ước tính** — chỉnh lại theo bản dựng cuối. Bản ES dài hơn EN ~12%, timestamps khác nhau.
3. **CTR nhập tay** từ Studio để điền `retro.md`.
4. **Cặp thử nghiệm tự nhiên với BÀI 1:** cùng tuần, khác độ dài (8.0′ vs 10.0′) và khác loại title
   (claim ngược đời vs pain-removal). So sánh AVD/CTR hai bài khi có số thật — xem `prediction.md` §giả thuyết.
