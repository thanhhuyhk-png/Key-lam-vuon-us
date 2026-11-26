---
file: topic-gate-en.md
role: 🚦 TOPIC GATE — cổng chọn chủ đề BẮT BUỘC cho MỌI video (lane A + lane B), chạy ở Bước 0-T, TRƯỚC outline / GATE 0
read_by: [skill-garden-us-pipeline (Bước 0-T), yt-channel-health-audit (Bước 7 chọn bài), mkt-youtube-outline (đọc kết quả trong pipeline-state)]
channel: Garden US (garden-us-60k)
created: 2026-10-05
derived_from: health audit W41 + kiểm chứng 49 video (research/keyword-title-test-2026-10-05.json) + bài học big-idea-058 garlic
---

# 🚦 TOPIC GATE — 3 tín hiệu, cần ≥2/3

## 🔗 PHỄU GỘP Topic Gate + san-y-tuong (từ 2026-11-08) — đọc mục này trước
Trước đây hai cổng chạy song song, gọi lại cùng lệnh vidIQ (cổng này 10–20 credit + san-y-tuong 40–60 credit/ý; lượt 01/11 tiêu 135 credit cho 3 ý). Nay là **một phễu 4 bậc**, dữ liệu bậc trước dùng lại ở bậc sau, ⛔ không gọi lại `vidiq_outliers` / `vidiq_keyword_research` cho cùng chủ đề.

| Bậc | Việc | Tốn | Dừng khi |
|---|---|---|---|
| **0 · Máy** | `python -X utf8 tools/kiem_de_tai.py kiem "<tiêu đề dự kiến>" --goc "<góc>"` → CHẶN / CẢNH BÁO / ĐẠT. Dòng ⭐ HIT CÙNG CHỦ THỂ = **tín hiệu ① chấm sẵn** (nối hit cũ). Cùng lúc: soát chặn cứng (mục dưới) bằng mắt. | 0 credit | CHẶN → đổi chủ thể hoặc đổi KHUNG rồi kiểm lại; không lách bằng từ đồng nghĩa |
| **1 · Topic Gate** | ② đọc báo cáo `tools/do_trend.py` (0 credit) + ③ 1–2 lệnh `vidiq_keyword_research` → phán quyết ≥2/3 như bảng PHÁN QUYẾT. ⓑ ⓒ như cũ. | ≤ 10 | BACKLOG / BỎ |
| **2 · Vòng A san-y-tuong** | C2 bão hoà **dùng lại** kết quả ② · C3 góc · C6 chính sách · mổ comment · C0 gói (`score_title`). | ≤ 15 | Đỏ ở cổng nào thì dừng ý đó |
| **3 · Vòng B san-y-tuong** | C1 chỉ số (THR, P(thắng), P25–P75) · C7 video mồi · C4 · C5. **Chỉ chạy** khi chọn giữa ≥ 2 ý, hoặc ý là GO-TEST / thăm dò. | ≤ 30 | — |

- **Trần mỗi ý: 60 credit** (bậc 1+2 ≤ 30, bậc 3 ≤ 30). Xem số dư trước và sau (`python ~/.claude/tools/vidiq_call.py balance`, hoặc `vidiq_balance`), báo dùng tài khoản nào; vượt trần thì hỏi user trước, không tự chạy tiếp.
- Ý vào sản xuất có phiếu san-y-tuong → 1 dòng `research/du-bao.csv`, **bắt buộc điền cột `thu_muc`** (tên thư mục `scripts/…`) để máy ghép kết quả.
- **Khép vòng:** mỗi Chủ Nhật (cùng lần dò trend) chạy `python -X utf8 tools/du_bao.py tat-ca` → điền views_5d + thắng/thua vào sổ, ghi `research/hieu-chinh-cong.md` (Topic Gate ↔ kết quả thật, Brier khi đủ 5 dòng). Sau đó `python -X utf8 tools/kiem_de_tai.py lap` để sổ đề tài có video mới.
- Thứ tự trình user: bảng bậc 0 (kết quả máy) → bảng Topic Gate → phiếu san-y-tuong (nếu có) → 1 lựa chọn đề xuất → ⏸ DỪNG chờ duyệt.

## 🔀 TỶ LỆ LANE — ~1/3 remake (C6, user duyệt 22/11/2026 · TEST 6 video)

- Cứ **3 video thì 1 video Lane B remake** (seed lấy từ báo cáo trend `do_trend.py` hoặc link user đưa; vẫn qua bậc 0 + TOPIC GATE như mọi lane). Hai video còn lại là Lane A; suất «cú đánh lớn» 1/4 vẫn giữ và có thể rơi vào lane nào cũng được.
- Căn cứ: cùng tháng 9/2026, 3 remake trung vị views_5d **763** so với Lane A **531** (×1,4) — mẫu nhỏ, nên là TEST.
- Khi chọn đề tài: đếm 2 video gần nhất trong `research/kiem-dinh-ky/video-ledger.tsv` (cột `lane`); cả hai đều A → đề xuất 1 seed remake trước.
- Chấm lại sau 6 video từ 22/11 (≈ 2 remake): `tools/kiem_dinh_ky.py` mục «Chấm luật» dòng «Lane B remake». Remake thua Lane A cùng kỳ → trình user hạ về tỷ lệ cũ.

## 🔁 PHẦN TIẾP THEO CỦA VIDEO CATALOG — 1/4 video (C2, user duyệt 22/11/2026 · TEST 8 video)

- Cứ **4 video thì 1 video là phần tiếp theo trực tiếp** của một video catalog đang kéo view: cùng chủ thể (cây/vật), **góc mới**, không lặp nội dung. Đây là cổng ① (franchise) của Topic Gate — tự đạt ① khi video gốc nằm trong top-5.
- Lấy danh sách video gốc ở `research/kiem-dinh-ky/latest.md` → mục «Catalog đang kéo view» (top-5 theo view 28 ngày). Ví dụ 22/11: Aloe (23K view / 28 ngày) · Avocado (16K) · Rooting cuttings in water (7K) · I Stopped Watering My Lemon Tree (5K) · 7 Cheap Root Cellar Ideas (3K).
- Góc mới lấy từ **câu hỏi trong bình luận** của video gốc (`youtube_video_comments` / `vidiq_video_comments`) hoặc từ bước tiếp theo của người xem (vd «avocado đã nảy mầm → giờ làm gì»). Vẫn qua bậc 0 `kiem_de_tai.py` (CẢNH BÁO trùng với chính video gốc là bình thường — chỉ CHẶN mới dừng).
- Đóng gói gợi nhắc video gốc (cùng vật chính trên thumbnail, tiêu đề có chữ hứa giống), và gắn **end screen + thẻ 2 chiều** giữa video mới và video gốc sau khi đăng.
- Ghi `PHẦN TIẾP THEO: <videoId gốc> — <tiêu đề gốc>` vào `pipeline-state.md` để `kiem_dinh_ky.py` đếm tỷ lệ và chấm kết quả (views_5d phần tiếp theo vs video thường, cùng kỳ). Chấm lại sau 8 video từ 22/11.

## 🚀 CÚ ĐÁNH LỚN — hạng thứ hai của danh mục (từ 2026-11-08, user duyệt)
Vì sao: từ T9/2026 kênh có 0 % video đạt ≥ 3× trung vị (T2–T4: 20 %). Cổng ①②③ chọn tốt video **không trượt**, nhưng phạt đúng những ý có thể bứt (`research/chan-doan-kenh-2026-11-08.md`).
- **Hai mức thắng** (`channel.config.json` → `scoring`, đọc lại từ `references/dna-kenh.json` mỗi CN): **an toàn** ≥ 1,5× trung vị views_5d · **bứt** ≥ 5× trung vị.
- **Danh mục 3 : 1:** cứ 4 video có 1 cú đánh lớn. Ghi `HẠNG: CÚ ĐÁNH LỚN` ngay dưới block TOPIC GATE trong `pipeline-state.md`; `tools/du_bao.py cong` đếm 8 video gần nhất (mục tiêu 2).
- **Nguồn ý:** `python -X utf8 tools/sinh_y.py` → `research/sinh-y-<năm>-W<tuần>.md` (hạt ý ở `references/dna-but.tsv`, xếp theo hệ số DNA kênh). Chọn 2–3 ý.
- **Cổng riêng (thay ①②③ cho hạng này):**
  | Cổng | Đạt khi | Nguồn |
  |---|---|---|
  | Bậc 0 | kiểm trùng không CHẶN | `kiem_de_tai.py` (sinh_y đã chạy sẵn) |
  | DNA | điểm ưu tiên `sinh_y` ≥ 1,0 **hoặc** có hit cùng chủ thể ≥ 10K | `sinh-y-*.md` |
  | Độ rộng tệp | cụm từ khoá RỘNG (không phải cụm cụ thể) ≥ 10.000/tháng US, **hoặc** ≥ 1 video cùng CHỦ THỂ (góc nào cũng được) ≥ 100K view trong 2 năm | 1 `vidiq_keyword_research` + 1 `vidiq_outliers` (bậc 1, ≤ 15 credit) |
  | Gói | 3 tiêu đề, ≥ 1 cái `score_title` ≥ 80, ≤ 70 ký tự; 3 ý thumbnail có vật cụ thể + biến đổi thấy được | san-y-tuong C0 |
  | Lời hứa giữ được | claim chính chứng minh được trong 20 s đầu (L6) bằng nguồn hạng A/B; cột `ghi_chu` của hạt ý có nguồn | ⓒ chất liệu |
  | Chặn cứng | như mục CHẶN CỨNG dưới — **không nới** | — |
  Không phạt vì "chưa có outlier cùng góc" (②) hay "không nối franchise" (①). Vòng B của san-y-tuong chạy khi có credit, `nguong_thang_view` = ngưỡng BỨT, cột `hang` = `cu-danh-lon`.
- **Khung "Stop … Instead"** (đảo niềm tin, ×1,39 thời kênh còn ra hit): **được dùng từ 08/11 theo L20** (`lessons-learned.md`) — vế sau là thứ được thêm, không chữ sợ, có nguồn A/B, chứng minh ≤ 20 s, tối đa 1 video/4.
- **Nhịp Chủ Nhật** (0 credit): `do_trend.py` (dò trend, chạy nền) → `du_bao.py dong-bo` → `dna_kenh.py do` → `du_bao.py dien` → `du_bao.py cong` → `kiem_de_tai.py lap` → `sinh_y.py`. Có file export Studio thì đặt vào `research/studio/` trước khi chạy `dna_kenh.py`.

> **Vì sao có cổng này.** "Thấy video đang nổ → làm theo" KHÔNG đủ. Dữ liệu chính kênh:
>
> | Cách chọn chủ đề | Ví dụ | View |
> |---|---|---|
> | Chỉ CÙNG CHỦ ĐỀ với outlier người khác | *7 Plants That Thrive in the Darkest Room* (gốc *20 Beautiful Plants…* 89K) | **427** |
> | Phần tiếp hit CŨ của kênh mình | *The Truth About Long-Term Water Culture* (nối *7 plants in water*) | **1,456** — tốt nhất 8 tuần |
> | Remake outlier + đổi MỘT trục + nguồn khoa học | *Just 1 Spoon…* (remake-002) | **1,011** (154% median) |
>
> Remake thuần: tỷ lệ trúng ~1/50, title stem dùng lần 2 suy giảm 8–118× (`remake-playbook-en.md`).
> ⇒ Outlier người khác cho biết **thị trường muốn gì**; nó KHÔNG cho biết **khán giả của MÌNH** có bấm bản của mình không.

---

## 3 TÍN HIỆU

### ① Kênh mình — FRANCHISE (tín hiệu mạnh nhất)
Chủ đề có nối được với **hit cũ** hoặc **video mới tốt nhất** của kênh không?
- Nguồn: `references/channel-health-latest.json` → `outliers.top` + `early_velocity` (video mới tốt nhất).
- Đạt khi: **cùng cây/vật** với hit, HOẶC **cùng khung lời hứa** của hit (vd hit Avocado = "đồ trong bếp → cây mới, cách lười" → garlic, chanh từ hạt, tái trồng gốc rau đều đạt).
- Hit hiện tại (05/10): Aloe 53K · Avocado từ hạt 45K · 7 cây trồng trong nước 23K · Lemon 15K · Giâm cành 13K. Video mới tốt nhất: Water Culture 1,456 · 1 Spoon 1,011 · October 906.
- Lý do mạnh nhất: thuật toán đã biết tệp khán giả của chủ đề này trên kênh mình → mẻ thử đầu đi đúng người.

### ② Ngách — TREND ĐANG LÊN (máy `tools/do_trend.py`, 0 credit — thay `vidiq_outliers` từ 18/11/2026)
- Nguồn: báo cáo **≤ 3 ngày tuổi** `research/trend-us/<YYYYMMDD>/bao-cao-trend.md`. Cũ hơn thì chạy lại:
  `python -X utf8 tools/do_trend.py --ds research/trend-us/kenh-ngach.txt --video-dir research/top20-<ngày>/thu-video --tim "<2–4 cụm mùa>" --out-dir research/trend-us/<YYYYMMDD>` (~20 phút, chạy nền).
- Đạt khi MỘT trong:
  - **Trend 10 ngày:** chủ thể có cờ `DA_KENH` (≥ 3 kênh có video hệ số trẻ ≥ 2), hoặc 2 kênh và có video tăng view/ngày **[ĐO]** thật (lần chụp thứ hai trở đi).
  - **Trend mùa:** chủ thể có trong video hệ số ≥ 2 của **≥ 2 kênh** ở bảng «cùng kỳ năm ngoái».
- Một kênh đơn lẻ = chỉ ghi «theo dõi», chưa đạt ② — **kể cả khi đó là Model Link** (Model Link chỉ là mẫu cách làm, không phải nguồn đề tài; user duyệt 18/11).
- **Hạn đăng:** trend 10 ngày → đăng ≤ 10 ngày tính từ ngày báo cáo; quá hạn thì chạy lại máy xem còn lên không. Trend mùa → đăng trước cột «ngày năm nay» 2–4 tuần.
- Cột «video nóng / tất cả» thấp (nhiều kênh làm, ít bản nóng) = bão hoà → cổng ⓑ, bắt buộc đổi góc.
- Ghi vào `pipeline-state.md`: ngày báo cáo, từ khoá, hệ số, loại (10 ngày / mùa). Ghi lại **pattern title** của video nóng → Title Engine, ⛔ không chép stem.
- ⛔ Không dùng `vph` của vidIQ (đã sai 100 lần) và không chạy `vidiq_outliers` cho cổng này nữa.
- **LUẬT TIÊU ĐỀ CÓ TỪ KHOÁ TREND (18/11/2026, user chốt; ghi đè bước 2 «soi outlier» của KEYWORD-FIRST GATE):** cả 3 phương án title **A/B/C đều chứa ≥ 1 từ khoá trend** của báo cáo trong ~25 ký tự đầu, **chỉ khi video nói đúng về nó** (không gắn từ khoá để câu view — chính sách metadata gây hiểu lầm). Lấy **chủ thể** (cây · vật · việc làm), ⛔ không chép khuôn câu của video nóng (stem dùng lần 2 suy giảm 8–118×). Có cụm search ③ ≥ 3,000/th US thì cụm đó đứng đầu. Không có từ khoá trend nào hợp video = chưa qua ②, quay lại chọn đề tài. Vẫn giữ L9, X1–X5, ≤ 65 ký tự.

### ③ Keyword — NHU CẦU TÌM KIẾM
- Lệnh: `vidiq_keyword_research` · `country:"US"` cho 2–3 cụm (chung + cụ thể đúng ý định video).
- Đạt khi: cụm chính **≥3,000/tháng US** HOẶC `searchDemandGrowthPct` **≥ +30%** so nền 30 ngày.
- ⚠️ Cụm chung ≠ cụm cụ thể (vd "how to plant garlic" 15,990 vs "grow garlic in pots" <750) — ghi cả hai.
- Đạt ③ → title theo **KEYWORD-FIRST GATE** (`title-keyword-strategy-en.md`, lesson L10).
- Kỳ vọng thực tế (kiểm chứng 49 video): title có cụm chủ thể → Search ~2.0% vs 0.5% (×4), Suggested 9% vs 6%. Search là phần CỘNG THÊM; ~86–90% view vẫn từ Browse.

---

## 2 KIỂM TRA PHỤ — không cộng tín hiệu, nhưng HẠ được phán quyết
> Thêm 12/10/2026, lấy từ quy trình kiểm định ý tưởng ngách quân sự (`D:\0008. Key Quân sự\Quy-trinh-tim-va-kiem-dinh-y-tuong.md`). Chạy ngay sau khi đếm ①②③, dùng lại data đã lấy, ⛔ không tốn thêm lệnh vidIQ.

### ⓑ Bão hoà GÓC
- Câu hỏi: trong **3–4 tháng gần đây**, **≥3 kênh** đã làm **đúng góc này** (cùng chủ thể + cùng khung lời hứa) mà phần lớn chỉ đạt mức trung bình của chính họ?
- Cách kiểm: đọc lại báo cáo `do_trend.py` của ② (cột «video nóng / tất cả», bảng video đang lên và trend mùa). Kênh nào chỉ có 1 video nổ, các bản cùng góc còn lại lẹt đẹt → tính là bão hoà.
- Bằng chứng kênh: nhánh listicle faceless cho người cao tuổi (Backyard Buddy · Verdant · SereneGreen 2–7K view/video, `health-log` W41). Mình làm *7 Plants … Darkest Room* = **427** trong khi gốc *20 Plants…* = 89K.
- Trúng → **bắt buộc đổi GÓC** (theo mùa · theo vùng khí hậu US · theo lỗi phổ biến · sang video QUY TRÌNH thấy được), không chỉ đổi 1 trục nhỏ. Không tìm ra góc mới thì hạ 1 bậc phán quyết.

### ⓒ Chất liệu
- Câu hỏi: liệt kê nhanh được **≥5 chi tiết cụ thể, ít người biết, kiểm chứng được** chưa? (con số, cơ chế, mốc thời gian, sai lầm phổ biến kèm lý do). Nguồn ưu tiên: Extension Service .edu các bang · USDA · RHS.
- Cách kiểm: chừng 5 phút, chỉ cần gạch đầu dòng + tên nguồn dự kiến. Chưa chắc chi tiết nào thì đánh `[VERIFY]`, chi tiết đó không tính.
- Lý do: hiện chất liệu chỉ lộ ra ở [1.5] deep research, lúc title + outline đã duyệt. Thiếu chất liệu thì không làm được Editorial Signature (L13) và Consensus Synthesis.
- Đạt <5 → **BACKLOG** đến khi đủ (kể cả 3/3). 5 chi tiết này chuyển sang [1.5] làm điểm xuất phát cho 5 câu hỏi research.

---

## PHÁN QUYẾT

| Số tín hiệu | Quyết định |
|---|---|
| **3/3** | ✅ ƯU TIÊN — sản xuất ngay, gắn hạn đăng nếu ③ đang tăng theo mùa |
| **2/3 có ①** | ✅ GO |
| **2/3 thiếu ①** (② + ③) | 🟡 GO có điều kiện — bắt buộc **đổi MỘT trục** + wedge khoa học + ghi `TEST` trong `prediction.md` |
| **1/3** | ⏸️ Backlog — đo lại tuần sau |
| **0/3** | ⛔ Bỏ |

**Sau khi tra bảng:** ⓑ bão hoà mà không đổi được góc → hạ 1 bậc · ⓒ chất liệu <5 → BACKLOG.

**⛔ CHẶN CỨNG (không override, kể cả 3/3):** SEED PHẢI BỎ X1 conspiracy · X3 health-fear/YMYL · X4 cơ chế nguy hiểm · X5 persona tự-test · L9 nhãn tuổi · L1 cây exotic · off-niche (L8) · khung sợ/độc/chết làm lời hứa chính (thông số vàng ②). *Khung đảo niềm tin "Stop … Instead / Never Buy … Again" KHÔNG thuộc mục này — được dùng theo L20 (user duyệt 08/11).*

**SAU KHI QUA CỔNG — vẫn bắt buộc khác biệt:**
- **Luật MỘT TRỤC:** đổi đúng 1 trục so với outlier (chủ thể / thời điểm / cơ chế / người kể) — không clone.
- **Wedge kênh:** nguồn extension/.edu + Consensus Synthesis + lời hứa thứ hai (bẫy) — thứ kênh AI-grandma generic không có.
- Vẫn qua đủ outline → research → hook → spine → script → thumbnail.

---

## CHI PHÍ & NHỊP
- Mỗi video: **2–3 lệnh vidIQ** (1 outliers + 1–2 keyword) ≈ **10–20 credit** — đây là bậc 1 của PHỄU GỘP; trần cả phễu 60 credit/ý.
- ⛔ KHÔNG chạy lại `do_trend.py` mỗi lần viết nếu báo cáo còn ≤ 3 ngày tuổi. Cổng này chỉ đo đúng chủ đề đang xét.
- Nhiều ứng viên cùng lúc (chọn bài từ backlog) → chạy cổng cho 3–5 ứng viên, xếp theo số tín hiệu rồi theo ③ growth.

## OUTPUT — ghi vào `pipeline-state.md` (block đặt ngay dưới tiêu đề)

```markdown
## 🚦 TOPIC GATE — [N]/3 → [ƯU TIÊN / GO / GO-TEST / BACKLOG / BỎ] (YYYY-MM-DD)
| Tín hiệu | Đạt? | Bằng chứng |
|---|---|---|
| ① Kênh mình | ✅/❌ | nối hit … (… view) / khung lời hứa … |
| ② Outlier ngách | ✅/❌ | [title] [view] [sub] · [title] [view] [sub] · pattern: … |
| ③ Keyword US | ✅/❌ | [cụm] [search/th] [growth%] [comp] · cụm cụ thể: … |
| Chặn cứng | sạch / [mã] | |
| ⓑ Bão hoà góc | không / có → góc mới: … | [kênh] [view] · [kênh] [view] · [kênh] [view] (3–4 tháng) |
| ⓒ Chất liệu | [n]/5 | 1. … (nguồn) · 2. … · 3. … · 4. … · 5. … |
| Trục đổi so với outlier | … | |
```

## HIỆU CHỈNH (feedback loop)
- **Máy làm (từ 2026-11-08):** `tools/du_bao.py cong` đọc phán quyết trong `pipeline-state.md` của từng thư mục, ghép video đã đăng (`research/thu-muc-video.tsv`, sửa tay khi ghép sai bằng `nguon=tay`) và in bảng tín hiệu ↔ views_5d.
- **Số đầu tiên (08/11, n nhỏ — chỉ xem hướng):** 3/3 ƯU TIÊN: Garlic 544 · Ginger 779 · Pineapple 650 → **0/3 thắng** (ngưỡng 894), trung vị 650 ≈ trung vị kênh 596. 2/3 GO: Lemon 543. Cổng hiện **chưa tách được** video thắng với video thường. Chưa đổi ngưỡng; xét lại khi đủ 8 video có kết quả.
- `retro.md` mỗi video ghi lại tổ hợp tín hiệu (vd `①②③`, `②③`).
- Sau **6–8 video**: so `views_5d` + CTR theo tổ hợp → siết/nới ngưỡng (3,000/th · +30% · ≥2 outlier) và ghi vào file này.
- Mẫu đầu tiên: **big-idea-058 garlic = 3/3** (① ADN Avocado "lười, đồ bếp" · ② 256K + 222K + 72K · ③ +315%).
