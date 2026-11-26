# Dò trend Garden US: đối chiếu với skill chuẩn và đề xuất (22/11/2026)

Nguồn so: `D:\GOHA\GohaKit\.claude\skills\rieng-tu-duy-top-20-ytb\references\do-trend-ngach-moi.md` + `scripts/do_trend.py` (605 dòng) với `tools/do_trend.py` của Garden (485 dòng). Số liệu từ 2 lần quét `research/trend-us/20261118` và `20261122`.

## 1. Bản Garden đang thế nào (số thật)

| | 18/11 | 22/11 |
|---|---|---|
| Video dài ≤ 10 ngày | 78 | 85 |
| Video «lên» trở lên (hệ số ≥ 2) | 9 | 5 |
| Trong đó nền «sub» (kênh lạ, không trần) | 3 | 0 |
| Video < 1 ngày tuổi | 5 | 12 |
| Từ khoá trend | 4 (`vegetable`, `winter`, `november`…) | 3 (`cold`, `food`, `winter`) |
| ĐA_KENH | 2 | 0 |

Ba lỗi đọc được từ bảng:
1. **Từ khoá là từ đơn chung chung** (`cold`, `food`, `winter`, `november`): dùng làm tiêu đề không được. Garden thiếu danh sách `TU_DON` (từ chỉ được nằm trong cụm).
2. **Nhiễu ngoài ngách chiếm 3/5 video nóng hôm nay**: Prepare Pantry (đồ khô, mất điện mùa đông) có 32–53 view mà vẫn hệ số 2,2–2,5, vì video mới 0,7–3,6 ngày và nền kênh nhỏ.
3. **Mẫu quá nhỏ**: 22 kênh, khoảng 80 video/10 ngày, chỉ 5–9 video nóng. Ngách làm vườn đi theo mùa và theo nhu cầu tìm, ít tin nóng, nên ĐA_KENH 10 ngày hiếm khi bật.

Phần Garden đã có mà bản chuẩn không có: **trend mùa cùng kỳ năm ngoái** (`cham_mua`). Giữ lại; nên chép ngược về skill gốc.

## 2. Bảng A (dùng chung): Garden có gì, thiếu gì

| # | Nâng cấp | Garden | Việc cần làm |
|---|---|---|---|
| 1–2 | Hệ số trẻ, nền kênh | có | — |
| 3 | Nền «sub»: trần 10, cần ≥ 20.000 view | **thiếu trần** | chép `TRAN_SUB`, `VIEW_MIN_SUB`; với ngách vườn đề xuất `VIEW_MIN_SUB = 5.000` (kênh vườn nhỏ hơn kênh quân sự) |
| 4–6 | VPH tb, VPH đo, đọc cặp | thiếu (chỉ có tăng/ngày) | chép; đã có 2 ảnh chụp (18 và 22/11) nên lần chạy tới có VPH đo ngay |
| 7–8 | ĐA_KENH, độ nổi | có | — |
| 9 | Gợi ý tìm kiếm YouTube US (`--goi-y`) | **thiếu** | chép; **quan trọng nhất cho ngách vườn** (xem mục 3) |
| 10 | Kênh NGUNG | có | — |
| 11 | Lịch mốc (`--lich`) | thiếu | làm lịch vườn (mục 3) |
| 12 | `--nap-meta` chấm lại không tải | thiếu | chép, để chỉnh bộ lọc nhanh |
| 13 | Hạn 10 ngày | có (CLAUDE.md) | — |
| 14 | Từ khoá trong tiêu đề | có (~25 ký tự đầu, chặt hơn 40–50 của skill) | giữ 25 |
| 15 | Hiệu chỉnh sau 4 tập | có qua `kiem_dinh_ky.py` | thêm cột hệ số + từ khoá trend vào `prediction.md` để so |

## 3. Bảng B (riêng ngách): đề xuất cho Garden

| # | Mục | Đề xuất cụ thể |
|---|---|---|
| B1 | Tách từ | giữ cụm 1–3 từ; gộp tên gọi: `christmas cactus / thanksgiving cactus / holiday cactus`, `tomatoes/tomato`, `usda zone N / zone N` → `zone N`; giữ mã giống cây (`Early Girl`, `F1`) |
| B2 | `TU_DON` (mới) | `winter fall autumn spring summer november december january cold hot frost food vegetable vegetables fruit tree trees flower flowers seed seeds soil indoor indoors outdoor container pot pots water` — chỉ được nằm trong cụm («winter sowing», «cold frame») |
| B3 | `LOAI_MAC_DINH` thêm | `pantry\|bulk\|blackout\|power outage\|stockpil\|survival food\|canning\|emergency food\|budget hacks?\|heat-retention`; và **bỏ Prepare Pantry khỏi `kenh-ngach.txt`** (không phải kênh vườn) |
| B4 | Sàn view video trẻ (mới, Garden riêng) | video < 2 ngày chỉ được ≥ 2 khi view ≥ 500; dùng VPH tb thay hệ số cho video 6–48 giờ |
| B5 | `RE_KHONG_ANH` | chép; tìm `--tim` đang kéo kênh Hà Lan, Romania (Ineke Wennink, Gradina Space…) |
| B6 | `RE_NGU_CANH` (cho gợi ý) | `grow\|plant\|garden\|seed\|soil\|prune\|propagat\|overwinter\|indoor\|zone\|frost\|compost\|fertiliz\|bloom\|harvest\|repot\|cutting` — «christmas cactus care» tính, «christmas cactus meme» không |
| B7 | `kenh-ngach.txt` | 22 kênh là ít; thêm kênh vườn lớn hay hiện qua `--tim` (Charles Dowding, Main St Gardener…) khi có ≥ 5 video dài 30–365 ngày; giữ kênh faceless cùng khuôn với mình |
| B8 | `--tim` | 10–15 cụm, đổi theo tháng. Tháng 11–12: `winter sowing, seed starting indoors, christmas cactus, amaryllis, poinsettia care, overwintering plants, garlic planting, cold frame, indoor herbs winter, houseplants winter, fall cleanup garden, seed catalog` |
| B9 | Lịch mốc vườn (`lich-vuon-us.tsv`) | thay ngày kỷ niệm bằng **mốc mùa vụ US**: Thanksgiving (26/11) · Christmas cactus/poinsettia/amaryllis (1–25/12) · catalog hạt giống (đầu 1) · winter sowing (1–2) · ươm hạt trong nhà zone 5–7 (2–3) · Valentine hoa (14/2) · ngày sương giá cuối (4–5, theo zone) · Mother's Day (5) · trồng tỏi (10) · Halloween bí ngô (10). Lên lịch 21–45 ngày trước mốc, khớp luật «trước đỉnh 2–4 tuần» |
| B10 | Cờ rủi ro | thay THOI_SU/VIET_NAM bằng **`YMYL`**: `cure\|cancer\|diabetes\|blood pressure\|detox\|medicinal\|heal\|doctor\|arthritis` (Harvest & Heal, Nature's Fix nằm trong ngách) → chỉ theo dõi, đi luật YMYL của pipeline; và **`OFF_NICHE`**: prepper, pantry |
| B11 | Mã nước, ngôn ngữ | `gl=US hl=en` cho gợi ý; vidIQ `videoTitleLanguage=en` |

## 4. Đề xuất cách đọc báo cáo cho ngách vườn

Ngách vườn khác ngách quân sự ở chỗ: nhu cầu lặp theo mùa và người xem **tìm** nhiều hơn là chờ tin. Vì vậy thứ tự tin tín hiệu cho cổng ② nên là:

1. **Trend mùa ≥ 2 kênh** (đã có) + **gợi ý US ≥ 1** (mới) → tín hiệu mạnh nhất, đủ để lên lịch trước 2–4 tuần.
2. **Mốc lịch vườn 21–45 ngày** + gợi ý US ≥ 1 → đề tài đoán trước, an toàn.
3. **ĐA_KENH 10 ngày** → hiếm nhưng giá trị cao; khi bật thì làm gấp (hạn 10 ngày).
4. Một kênh đơn lẻ, hoặc chỉ có hệ số mà gợi ý = 0 → chỉ theo dõi.

Thử nghiệm đề nghị: chạy song song `--ngay 10` và `--ngay 14` trong 2 tuần; nếu 14 ngày cho cụm 2–3 từ ổn định hơn mà không kéo video cũ lên đầu thì đổi mặc định cho phần từ khoá (hạn đăng vẫn 10 ngày).

## 5. vidIQ

Giữ như skill: chỉ xác nhận 3–5 cụm đã qua bước trên, hỏi trước, xem số dư trước. Garden đã dùng vidIQ keyword ở cổng ③ nên không cần thêm `trending_videos` làm cổng; thử một lần cho cụm mùa (ví dụ «christmas cactus») để so với bản tự đo.

## 6. Trạng thái (cập nhật 22/11/2026)

Đã làm đợt 1 + 2 trong `tools/do_trend.py` (19 test ở `tools/tests/test_do_trend.py`, đạt hết):
- Đợt 1: `TU_DON`, lọc đồ khô / mất điện, sàn view (`VIEW_MIN_LEN` 300; video < 48 giờ cần ≥ 500), trần nền sub (`TRAN_SUB` 10, `VIEW_MIN_SUB` 5.000), `RE_KHONG_ANH`, gộp tên (christmas cactus, zone, houseplant), `--nap-meta` + tự lưu `meta-video.jsonl`. Prepare Pantry đã bỏ khỏi `kenh-ngach.txt` (dòng để lại dạng chú thích).
- Đợt 2: `vph_tb`, `vph_do` (ảnh chụp có thêm giờ), `--goi-y` + `RE_NGU_CANH` (chạy cho cả từ khoá trend 10 ngày và trend mùa), `--lich research/trend-us/lich-vuon-us.tsv` (18 mốc; mã lễ thanksgiving, mothers, fathers, memorial, labor; cột kịp PHIM_DAI ≥ 21 ngày / GAP), cờ YMYL + OFF_NICHE.
- Chưa làm: B7 thêm kênh vào `kenh-ngach.txt` (cần người dùng chọn), thử `--ngay 14`, đợt 3.

## 7. Thứ tự làm (đề xuất)

1. **Đợt 1, sửa nhiễu (ít rủi ro):** B2 `TU_DON`, B3 lọc + bỏ Prepare Pantry, B4 sàn view, A3 trần nền sub, B5 lọc ngôn ngữ, A12 `--nap-meta`. Chấm lại số 22/11 bằng `--nap-meta` để xem bảng từ khoá sạch chưa. Viết test bằng tiêu đề thật trong 2 lần quét.
2. **Đợt 2, thêm tín hiệu:** A4–6 VPH, A9 `--goi-y` + B6, B9 lịch vườn + `--lich`, B10 cờ YMYL.
3. **Đợt 3, sau 4 tập:** so view thật với hệ số, chỉnh ngưỡng; quyết `--ngay 14`.
4. Chép `cham_mua` ngược về skill gốc GohaKit (tuỳ người dùng).
