# Hồ sơ ngách — Garden US
Cập nhật: 2026-10-17 · Dùng cho bộ skill chung `/pipeline-video` và `/san-y-tuong`
Hồ sơ này **chỉ trỏ** tới hệ thống Garden đang có; không thay `CLAUDE.md`, `channel.config.json`, `PIPELINE-GARDEN-US.md` hay các skill garden. Khi mâu thuẫn, file gốc của Garden thắng.

## Kênh
- Ngôn ngữ / thị trường: tiếng Anh, US (có bản ES qua `mkt-yt-translate-es`)
- Khán giả: người làm vườn Mỹ **35–60+** (lõi hiện tại 60–80), xem trên điện thoại (`channel.config.json` → `target_viewer`, cập nhật 23/10/2026)
- Kênh mình: `garden-us-60k` · số liệu: `references/channel-stats-garden-us-60k.md` (khối AUDIT TL;DR)

## Định nghĩa thắng
- Chỉ số kênh đang dùng: **views_5d so với trung vị kênh + giây xem/lượt + CTR Studio** (`channel.config.json` → `scoring`). Trung vị views_5d: **597**, ngưỡng thắng **896** (= 1,5×). Số 285 cũ chỉ còn là lịch sử.
- Cửa sổ chấm: 5 ngày (không phải 30 ngày như mặc định của `/san-y-tuong`). Sổ dự báo ghi ở cột `views_5d`.

## Key kênh
- Làm: mẹo làm vườn thực tế, sửa lỗi cây, theo mùa, tiết kiệm tiền; giọng educator, hạ áp lực
- Không làm: thuyết âm mưu, gây sợ sức khỏe, cơ chế nguy hiểm, persona "tôi tự thử", tiêu đề nhắc tuổi người xem (bộ lọc X1–X5, L9 trong `channel.config.json`)

## Định dạng
- Lane A Big Idea: một chủ đề, **10–14 phút (1.650–2.300 từ)** theo `channel.config.json` → `video_length` (user quyết 10/11/2026 sau 5 video 17–20′: giây xem/lượt không tăng, views_5d giảm; bản 20–24′ của 23/10 đã thôi). Vượt 14′ chỉ khi bảng Spine chứng minh payoff đủ dày.
- Lane B Remake: archetype A1–A10 (`references/remake-archetypes-en.md`); chỉ A1/A2/A5 được vượt 10 phút (đang test có kiểm soát).
- Mô-đun lõi tương ứng: Big Idea ≈ **C sửa lỗi/hướng dẫn**; A1/A2/A5 ≈ **A danh mục**.

## Thang nguồn
| Hạng | Nguồn |
|---|---|
| A | Extension .edu (land-grant), USDA, EPA, ASPCA (độc tính thú cưng), peer-reviewed |
| B | RHS, vườn thực vật lớn, sách nhà xuất bản chuyên ngành |
| C | Báo làm vườn uy tín, nhà sản xuất (chỉ cho thông số sản phẩm) |
| D | Blog, forum, Pinterest, wiki — chỉ dẫn đường |

## Vùng đỏ chính sách
YMYL: liều thuốc/hóa chất, an toàn thú cưng/trẻ em, cây ăn được/độc, chữa bệnh người · thuyết âm mưu · gây sợ. Chi tiết: `mkt-yt-compliance` và `references/lessons-learned.md`.

## Đường dẫn
- Ý tưởng: lane A `mkt-big-idea` (Notion Big Ideas) · lane B `research/seed-radar-YYYY-Www.md`
- Cổng chủ đề: `references/topic-gate-en.md`
- Lessons: `references/lessons-learned.md` · vòng phản hồi: `references/feedback-loop.md`
- Dự đoán từng video: `prediction.md` trong thư mục video · Sổ dự báo chung: `research/du-bao.csv` (cột `thu_muc` bắt buộc) · kết quả điền bằng `tools/du_bao.py`
- Danh mục đã dùng: `references/so-de-tai.tsv` (máy dựng: `tools/kiem_de_tai.py lap`)

## Luật riêng ngách (thắng mặc định của `/san-y-tuong`, thêm 2026-11-08)
1. **Phễu gộp:** chạy theo `references/topic-gate-en.md` mục PHỄU GỘP. Topic Gate = bậc 1; Vòng A / Vòng B của skill = bậc 2 / bậc 3. ⛔ Không gọi lại `vidiq_outliers` / `vidiq_keyword_research` cho cùng chủ đề — C2 và từ khoá C0 dùng lại dữ liệu bậc 1.
2. **Tầng 2 câu 2 (trùng danh mục) do máy làm:** `python -X utf8 tools/kiem_de_tai.py kiem "<tiêu đề>" --goc "<góc>"`. CHẶN → loại hoặc đổi khung; CẢNH BÁO → ghi vào phiếu C2 (trùng nội bộ). Dòng ⭐ HIT = nguồn (f) "video thắng của chính kênh".
3. **Ngân sách:** trần 60 credit/ý (bậc 1+2 ≤ 30, Vòng B ≤ 30). Vòng B chỉ chạy khi chọn giữa ≥ 2 ý hoặc ý thăm dò / GO-TEST. Vượt trần → hỏi user.
4. **Hai mức thắng + danh mục 3 : 1** (user duyệt 08/11): an toàn ≥ 1,5× trung vị views_5d, bứt ≥ 5×. Tỷ lệ khai thác/thăm dò của skill thay bằng 3 an toàn : 1 cú đánh lớn. Tầng 1 nguồn (b) "ma trận Khung × Đối tượng" = `tools/sinh_y.py`; hệ số khớp lấy hướng từ `references/dna-kenh.json` thay cho ước đoán. Cổng riêng của cú đánh lớn: `references/topic-gate-en.md` mục CÚ ĐÁNH LỚN.
5. **Tầng 4 (hiệu chỉnh):** `python -X utf8 tools/du_bao.py tat-ca` mỗi Chủ Nhật — điền `views_5d`, `thang_thua` (theo `nguong_thang_view` của dòng), ghi `research/hieu-chinh-cong.md`; tự chạy Brier khi đủ 5 dòng. Đổi ngưỡng chỉ khi ≥ 8 video có kết quả và user duyệt.

## Pipeline
- Ngôn ngữ kịch bản: en · Thị trường: US
- Độ dài: 20–24 phút (lane A, theo config) · Tốc độ đọc: **165 từ/phút** (giọng Key gardent đo thật, `tools/script_lint.py`)
- Thư mục video: `scripts/big-idea-NNN-slug/` hoặc `scripts/remake-NNN-slug/` · File trạng thái: `pipeline-state.md` (Garden đã dùng — giữ định dạng của Garden)
- Tên file: `outline.md` · `research-brief.md` · `retention-spine.md` · `script.md` (lời đọc dưới `## TTS SCRIPT`) · `seo-en.md` · `script-es.md` · `seo-es.md` · `prediction.md`
- Thứ tự bước của Garden: 0-T Topic Gate → [1] outline (kèm 3 tiêu đề + thumbnail) → [1.5] deep research → [2] hook → [2.5] retention spine → [3] script → [3.5] prediction → [4a/b/c] SEO + ES → [6] retro
- File giọng văn: `references/channel-truth.md` (thắng) · `references/brand-voice-dna.md`
- Thẻ cần xác minh: `[NEED DATA: …]`, `[HEDGE]`, `[YMYL]`
- Mô-đun tuân thủ: YMYL làm vườn/thú cưng

| Bước lõi | Bước Garden | Skill riêng | Chế độ |
|---|---|---|---|
| 1 Kiểm định | 0-T + R0–R3 | `references/topic-gate-en.md`, `mkt-big-idea`, seed-brief | riêng |
| 2 Research | [1.5] | `mkt-youtube-deep-research` (subagent `garden-deep-researcher`) | riêng → lõi kiểm 2 nguồn |
| 3 Gói hứa | [1] tiêu đề + [2] hook | `mkt-youtube-outline`, `mkt-hook-kallaway` | riêng → lõi chạy 6 phép thử + kiểm lời hứa |
| 4 Dàn ý | [1] + [2.5] spine | `mkt-youtube-outline`, `templates/retention-spine-*.template.md` | riêng → lõi kiểm sổ vòng mở |
| 5 Kịch bản | [3] | `youtube-garden-us` | riêng → lõi chạy lint + bản đồ sự thật |
| 6 Tuân thủ | [3] Phase 2.2 | `mkt-yt-compliance` (điểm 0–10) | riêng |
| 10 SEO | [4a/4c] | `mkt-yt-seo-description` (subagent `garden-seo`) | riêng → lõi kiểm chương/khớp kịch bản |
| 11 Hậu kiểm | [3.5] + [6] retro | `prediction.md`, `references/feedback-loop.md` | riêng → lõi thêm sổ dự báo + Brier |

```json lint
{
  "language": "en",
  "wpm": 165,
  "target_words": [1650, 2300],
  "body_start": "^## TTS SCRIPT",
  "section_label": "^\\s*\\[\\[NEVER\\]\\]$",
  "skip_line": "^\\s*(```|#|>)",
  "sentence_avg": [8, 15],
  "signatures": {
    "Here's why this works": [0, 3],
    "Don't panic": [0, 1],
    "That's it": [0, 1],
    "Happy gardening.": [1, 1]
  },
  "second_person_every": 150,
  "verify_tags": ["\\[NEED DATA[^\\]]*\\]", "\\[HEDGE\\]", "\\[YMYL\\]", "\\[VERIFY\\]"],
  "credit_per_char": 0
}
```
Ghi chú ngưỡng: `sentence_avg` [8, 15] và ngôi thứ hai mỗi ~150 từ là **ước đoán ban đầu** cho khán giả lớn tuổi, chưa có bằng chứng; câu chữ ký lấy từ `channel-truth.md` dòng 60. Câu chữ ký Garden đổi theo định dạng (listicle: "Here's the thing", "That's it"; problem-fix: "Here's why this works", "Don't panic" — `channel-truth.md` dòng 43–44) nên mức tối thiểu để 0; muốn ép theo định dạng thì chạy lint với `--profile` riêng. Video dài (A1/A2/A5, bản long-form) chạy lint với `--target <số từ>`. Chỉnh sau `/hau-kiem`.

## Lịch sử thay đổi
- 2026-10-17: tạo hồ sơ để thử bộ skill chung `/pipeline-video` trên Garden; chỉ ánh xạ, không sửa hệ thống Garden.
- 2026-11-01: khớp lại với config: mốc 597/896, độ dài 20–24 phút, 165 từ/phút.
- 2026-11-08: thêm mục Luật riêng ngách (phễu gộp, máy kiểm trùng đề tài, trần credit, khép vòng dự báo bằng `tools/du_bao.py`).

## Liên quan
`CLAUDE.md` · `PIPELINE-GARDEN-US.md` · `channel.config.json` · `references/channel-truth.md` · `references/lessons-learned.md`
