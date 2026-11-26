# Pipeline State — remake-001-october-planting

**Lane:** B — REMAKE *(video lane B đầu tiên của kênh)* · **Ngày dựng:** 2026-09-04
**Title:** `16 Things Grandma Always Planted in October (Before the First Frost)`
**Target publish:** **16–20/09/2026** ⏰ *(cửa sổ hẹp — trễ 20/09 thì giá trị rơi rất nhanh)*

---

## Tiến độ

| Bước | Trạng thái | Output | GATE |
|---|---|---|---|
| **R0** radar tuần | ✅ | `research/seed-radar-2026-W36.md` | không gate |
| **R1** tái thẩm seed | ✅ | seed `dOYKEdmPXWY` — 103.211 view / 6.160 sub · breakout 349 · đường cong NỞ | — |
| **R2** giải phẫu lời hứa | ✅ | mảnh khẩn cấp khoá cứng | — |
| **R3** đổi vật chủ | ✅ | tháng 9 → **tháng 10** | ✅ GATE 0 |
| **[1]** outline | ✅ | `outline.md` | ✅ GATE 1 *(đổi title B→C)* |
| **[1.5]** deep-research | ✅ | `research-brief.md` + `research-lo1..lo5.md` · **5 lô** · 38 flag `[NEED DATA]` | ✅ GATE 2 *(chốt 16 mục)* |
| **[2]** hook | ✅ | `hook.md` | ✅ GATE Hook |
| **[2.5]** retention spine | ✅ | `retention-spine.md` | ✅ GATE 2.5 |
| **[3]** script | ✅ | `script.md` — 3.345 từ · 22,3′ · **Pha D 8/8** · **Compliance 10/10** | ✅ GATE Script |
| **[4a]** SEO EN | ✅ | `seo-en.md` — 2.400 ký tự · pinned 270 ký tự | không gate |
| **[4b]** dịch ES | ✅ | `script-es.md` — 3.520 từ · 23,5′ · 16 mục · 0 câu >20 từ | không gate |
| **[4c]** SEO ES | ✅ | `seo-es.md` — 2.897 ký tự *(xem ghi chú ngưỡng)* · pinned 265 ký tự | không gate |
| **[5]** prediction | ✅ | `prediction.md` — ghi tại GATE Script | — |
| **thumbnail** | ⬜ | chạy `garden-us-thumbnail` — concept đã chốt ở `outline.md` | — |
| **[6]** retro | ⬜ | 7–14 ngày sau publish → diff với `prediction.md` → `lessons-learned.md` | — |

---

## Packaging đã khoá

| | |
|---|---|
| Title chính | `16 Things Grandma Always Planted in October (Before the First Frost)` · 67 ký tự · vidIQ **93/100** |
| Title á quân *(swap giờ 48 nếu CTR <4%)* | `16 Things to Plant in October - The Last Window Before Frost` · vidIQ 89/100 |
| Thumbnail | `ONLY 7 WORK COLD` · **FACELESS** *(luật kênh 14/14)* · ⛔ cấm tái dùng ảnh của seed |
| Cấu trúc | 16 mục · nhóm **7 / 3 / 6** theo "ai làm được" |

⛔ **KHÔNG đổi title + thumbnail cùng lúc** sau khi đăng — mất khả năng đọc biến nào có tác dụng.

---

## ⚠️ Ngưỡng SEO description: luật hiệu chuẩn trên tiếng Anh

Skill `mkt-yt-seo-description` quy định **1.200–2.500 ký tự**. Bản EN đạt **2.400** ✅.
Bản ES đạt **2.897** — thừa 397, và **đã cắt 2 vòng** rồi.

Chênh lệch EN→ES là **21%**, đúng mức nở tự nhiên của tiếng Tây Ban Nha (20–25%).
Ép ES xuống 2.500 nghĩa là **cắt bớt nội dung mà bản EN vẫn giữ** → khán giả ES nhận ít hơn.
Trần cứng của YouTube là 5.000 ký tự, nên 2.897 **không gãy gì**.

🔧 **Đề xuất sửa skill:** ngưỡng nên theo ngôn ngữ — EN 1.200–2.500 · ES 1.400–3.000.
Chưa sửa vì đó là thay đổi luật cấp skill, cần user quyết.

---

## Ghi chú vận hành

**File `script.md` là bản cuối** — đã qua Triple F Boost + 2 vòng compliance.
`script-pre-triplef.md.bak` giữ bản trước Triple F để đối chiếu nếu cần.

**Luật đang vi phạm có chủ đích:** `L7` — 22,3 phút vs target kênh 8–10.
Đã duyệt tại GATE 2 như **TEST CÓ KIỂM SOÁT**. Điều kiện rollback ở `channel.config.json → lanes.remake._warn`.

**⚠️ Thước chấm cho video này:** `views_5d` vs `median_5d_views` (**285**) + **tổng giờ xem**.
⛔ **KHÔNG chấm bằng AVD** — `prediction.md` đã dự đoán AVD *thấp hơn* baseline một cách có chủ đích.

---

## Việc còn lại trước khi đăng

- [ ] Render thumbnail bằng `garden-us-thumbnail` *(concept + 5 asset đã mô tả trong `hook.md`)*
- [ ] **Ghi CTR baseline từ Studio** cho 5 video đang sửa title *(xem `research/title-fix-L9-2026-09-04.md`)* — việc riêng, không thuộc video này
- [ ] Đăng **16–20/09**
- [ ] Giờ 48 sau đăng: nếu CTR < 4% → swap sang title á quân, **giữ nguyên thumbnail**
- [ ] 7–14 ngày sau: điền `retro.md` từ `templates/retro.template.md`, diff với `prediction.md`
