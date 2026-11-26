# Phản biện độc lập v1 — Top 20 Garden US (đo 2026-11-16)

Người phản biện: sub-agent ngữ cảnh mới, chỉ đọc dữ liệu trong `research/top20-2026-11-15/`. Mọi con số dưới đây tôi tự tính lại từ `tong-hop-do.tsv`, `thu-video/*.tsv`, `*.meta.json`, `hoc-tron/soi-0.jpg`, không chép từ báo cáo.

## 1. Điểm tin (0–10)

| Đối tượng | Điểm | Lý do bằng số |
|---|---|---|
| Model Link = No Longer Here (NLH) | **3/10** | Hạng 4 ở cách tính chính, hạng 1 ở 1/3 cách *độc lập* (xem lỗ hổng 2). 0/104 video ≤ 14′ (trung vị 31,1′). Đăng 26 video/30 ngày, gấp khoảng 3 lần nhịp 2 video/tuần. Lịch sử kênh chỉ đọc 104/410 video dài, nên «khoảng trống» và «đà tháng» chưa được chứng minh. Điểm cộng: trong NLH, đề tài làm vườn có trung vị 17.550 (n = 30) so với 10.991 ở đề tài khác (n = 39), tính trên video đã đủ 30 ngày, đăng 2026-08 đến 2026-10-16. |
| Ứng viên 2 = Forgotten American Survival (FAS) | **2/10** | Chỉ 1/57 video đã đủ tuổi (08 → 10-16) là đề tài làm vườn. Đề tài thắng là cúp điện, phòng hoảng loạn, phòng vệ nhà, sát luật L8. Trung vị theo tháng lấy từ mẫu lệch (lỗ hổng 3). 0/108 video ≤ 14′. Đăng 23 video/30 ngày. |
| TOP 20 | **4/10** | Phần thu số tốt: 97/97 kênh thu được video, kiểm tay lệch 0–0,24 %. Nhưng 0/20 kênh có thời lượng trung vị trong khung 10–14′ (trung vị của TOP là 26,3′; dải 8,4–65,1′). Chỉ 4/20 kênh có hướng A (làm vườn). 2 kênh không đăng video nào trong 30 ngày (AgroWorks USA, Living Self-Sufficiently) vẫn ở hạng 8 và 14. |

## 2. Năm lỗ hổng nặng nhất

### LH1. TOP 20 và cả hai ứng viên nằm ngoài định dạng chủ kênh vừa chốt — mức CAO
- **Mô tả:** khung (`khung.md` dòng 4) ghi 10–14′, và nhãn «cùng nguồn lực» (dòng 6) yêu cầu ≤ 4 video dài mỗi tuần. Phần lọc và xếp hạng không dùng hai điều kiện này. Báo cáo kết luận «bám cách chọn đề tài, không bám nhịp và độ dài» (`bao-cao-nhap.md` dòng 36), nhưng không đo xem đề tài của kênh mẫu có còn thắng khi làm ở độ dài 10–14′ hay không.
- **Bằng chứng:** `top20.tsv` cột `dur_m`, đối chiếu với `tong-hop-do.tsv` cột `dur_med_s`: 0/20 kênh có thời lượng trong khoảng 10–14′. NLH có 0/104 video dài ≤ 14′, FAS có 0/108 (`thu-video/UCkN5…tsv`, `UCmNd9…tsv`). Số video trong 30 ngày (`video_30_ngay`): FAS 23 (≈ 5,4/tuần), NLH 26 (≈ 6,1/tuần), đều vượt ngưỡng ≤ 4/tuần của khung. Chủ kênh vừa bỏ bản 17–20′ vì giây xem mỗi lượt không tăng. Kênh mẫu 30′ là chính cái biến số vừa bị bác.
- **Việc cần làm:** thêm một trục «định dạng» rồi xếp lại tập Giữ, chỉ lấy kênh có thời lượng trung vị 8–16′ và ≤ 4 video dài/tuần. Trình chủ kênh hai vai riêng: «Model Link đề tài» và «Model Link định dạng». Nếu vẫn giữ NLH, phải đo trung vị của những video ≤ 16′ của NLH. Hiện NLH có 0 video như vậy, nên mệnh đề «học đề tài, rút độ dài» là [CHƯA CÓ] bằng chứng.

### LH2. Độ nhạy «3/5» của FAS là ảo, thực chất chỉ có 3 cách độc lập và 3 kênh hạng 1 khác nhau — mức CAO
- **Bằng chứng:** `xep-hang.md` dòng 7–67: cột `pct_tang_sub_30` = «–» ở cả 61 kênh. Vì vậy cách «tổng bỏ % tăng sub 30 ngày» trùng hoàn toàn với «tổng». Cách «chỉ kênh ≥ 90 ngày» chỉ bỏ 1 kênh (When Power Fails, 52 ngày, hạng 19), và 60 kênh còn lại vẫn xếp như cũ (dòng 76). Như vậy FAS hạng 1 ở 3 cách nhưng đó chỉ là 1 kết quả lặp 3 lần. Ba cách thật sự độc lập (tổng, tích luỹ, chỉ trung vị) cho ra 3 kênh hạng 1 khác nhau: FAS, NLH, Forgotten Old American.
- Báo cáo chọn NLH vì «khoảng hạng hẹp hơn 1–4» (dòng 36). Khoảng của FAS là 1–5, tức chỉ chênh 1 bậc. Ở cách chính, NLH hạng 4 với 76,3 điểm, thấp hơn FAS 6,0 điểm. Lý do chọn chưa đủ số để đứng vững.
- **Việc cần làm:** sửa `--do-nhay` để gộp các cách cho kết quả trùng nhau, rồi báo «hạng 1 ở n/3 cách độc lập». Ghi rõ trong báo cáo rằng không có kênh nào vững.

### LH3. Bảng «trung vị theo tháng» và «khoảng trống» của NLH dựng trên mẫu lệch — mức CAO
- **Bằng chứng:** trong `thu-video/UCmNd9…meta.json`, FAS có 152 video dài, video đầu ngày 2026-03-23, nhưng `cua_so_tu` = 2026-07-04. Các tháng 3 và 4 chỉ có 8 video, đều thuộc danh sách «phổ biến». Vì vậy con số «Th4 113K (n5)» (`bao-cao-nhap.md` dòng 27) là trung vị của 5 video hot nhất, không phải trung vị của tháng, và câu «sụt từ 113K xuống 5,9K» là do cách chọn mẫu tạo ra.
- NLH (`UCkN5…meta.json`) có `n_dai_flat` = 410, `cua_so_tu` = 2026-08-08, và chỉ đọc 104 video dài. Khoảng 306 video dài chưa được đọc, nên câu «khoảng trống từ 2025-08 tới 2026-08» (dòng 26) chưa được chứng minh.
- 8 video tháng 8/2025 của NLH thuộc ngách hoài cổ («20 Old House Styles No Longer Built», «Mall Restaurants from the 1980s That No Longer Exist»). Hiện kênh làm bà ngoại, làm vườn, dự trữ. Đây là dấu hiệu kênh đã đổi ngách: 238K sub có thể là sub của ngách cũ. Hai chỉ số dựa trên sub của NLH (515 sub/video, 509 sub/ngày) bị thổi lên, mà chúng chiếm 2/4 tiêu chí của bộ «tích luỹ», cũng là bộ duy nhất NLH đứng hạng 1.
- **Việc cần làm:** thu lại toàn bộ danh sách video có ngày đăng (flat list) của NLH và FAS rồi tính lại trung vị theo tháng trên mọi video. Gắn cờ kiểu TAI_SINH hoặc «đổi ngách» cho NLH sau khi lấy được ngày lập kênh. Chạy lại xếp hạng khi bỏ 2 chỉ số dựa trên sub của NLH.

### LH4. Bỏ sót, loại oan: The Good Steward là kênh khớp định dạng nhất trong 97 kênh nhưng bị loại sau khi xem 1 video — mức CAO
- **Bằng chứng:** dòng 33 của `tong-hop-do.tsv` và file `thu-video/UCb3sv…tsv` cho The Good Steward 44 video, 186.000 sub. Kênh này có số sub mỗi video cao nhất trong 97 kênh (4.227). Trung vị 20 video là 159.898, gấp 7,3 lần NLH, và trung vị ÷ sub = 0,86. Thời lượng trung vị **11,4′**, với 29/44 video nằm trong khoảng 10–14′. Nhịp đăng 4–6 video/tháng, khớp nguồn lực 2 video/tuần.
- Kênh bị loại vì «người dẫn nữ lên hình», căn cứ duy nhất là storyboard của 1 video. Trên chính `hoc-tron/soi-0.jpg`, người dẫn xuất hiện ở 2/9 khung (đoạn mở). 7 khung còn lại là stock B-roll kèm thẻ số. Phần lớn hình là thứ chủ kênh làm được. Người dẫn có thể là một phần lý do kênh được tin, nên chưa thể coi đây là Model Link, nhưng loại hẳn khỏi bảng là bỏ phí.
- Đề tài thắng của kênh («18 Benefits of Hydrogen Peroxide», «Borax», «Dawn», «Vaseline») mang lời hứa sức khoẻ, nên phải ghi vào cột «Không học».
- Kênh thứ hai: The Grid-Down Kitchen (`tong-hop-do.tsv` dòng 38). Trung vị 10.062, thời lượng 9,8′, 100K sub. Kênh bị đẩy sang «Không đủ chỉ số» do cờ SUB_LAN_SHORTS. Tỉ trọng view Shorts 0,218 được *ước từ mẫu* (nguồn = mau), chỉ cao hơn ngưỡng 0,20 một chút.
- **Việc cần làm:** xem storyboard ≥ 3 video của The Good Steward (đếm tỉ lệ khung có người dẫn) và đưa kênh vào tab «đối chứng định dạng hoặc đề tài». Lấy tỉ trọng view Shorts 30 ngày thật cho Grid-Down Kitchen (vidIQ, khi có credit) và dùng `--ghi-de` nếu tỉ trọng dưới 20 %. Lưu ý Grid-Down Kitchen dừng đăng từ 2026-09-26.

### LH5. TOP 20 trôi khỏi ngách làm vườn và đẩy kênh về đề tài sợ hãi, cúp điện — mức VỪA–CAO
- **Bằng chứng:** cột `huong` trong `loc-so-bo.tsv` cho thấy chỉ 4/20 kênh trong TOP có hướng A (Golden Seniors Living, Frugal Solutions và Backyard Bill là AB, Plant Explainer là A). 16/20 kênh thuộc hướng B hoặc C.
- FAS có 1/57 video làm vườn. Bảy video top của FAS là cúp điện, phòng hoảng loạn, phòng vệ nhà, Costco «trước khi mất điện».
- NLH có tiêu đề «… for Seniors Living Alone», vi phạm L9 (nhãn tuổi), và «Hydrogen Peroxide Kills Roaches… Exterminators Hide», kiểu thuyết âm mưu. Hai tiêu đề này chưa được đưa vào cột «Không học».
- Plant Explainer (hạng 12) vào TOP 20 nhờ đà trung vị 12,11 và phân tán 140, tức nhờ một vài video đột biến.
- **Việc cần làm:** xếp hạng riêng tập A và AB (khoảng 28 kênh Giữ) để có ứng viên Model Link thuộc ngách chính. Bỏ FAS khỏi vị trí ứng viên 2 và chuyển sang «kho đề tài lân cận», kèm cột «Không học» (phòng vệ nhà, phòng hoảng loạn, «before the next blackout»).

### Lỗi nhỏ hơn (ghi để sửa)
- `kho-vuot-troi.tsv` chỉ có 6 cột: thiếu `he_so_sau`, «kiểm tra số thật» và cờ «chưa chín» theo §2 công thức. Con số 954× của NLH dựa trên mức nền 15 video trước chỉ ≈ 2.790 view (2.662.237 ÷ 954), là những video đầu cửa sổ. 326 video «vượt trội» này chưa đạt điều kiện để tô xanh.
- `bao-cao-nhap.md` dòng 39 giải thích «đà 0,04 = video gần đây chỉ bằng 4 % trung vị». Định nghĩa đúng là trung vị 10 video gần nhất ÷ trung vị 10 video trước đó (công thức §1).
- Tuổi khán giả: NLH có khoảng 8 nhãn, FAS khoảng 5. Với n ≤ 8, mức «Vừa» là quá cao, nên hạ xuống «Thấp».
- Tỉ lệ bình luận trên 1.000 view: NLH 0,82, FAS 1,00, Forgotten Old American 2,87, kênh mình 4,55. Khán giả NLH tương tác kém hơn khán giả của kênh mình khoảng 5 lần. Báo cáo chưa nêu điều này.
- Storyboard của Lost American Memories (`soi-1.jpg`) có khung phỏng vấn truyền hình («Gary, Indiana»), tức có rủi ro dùng lại nội dung, nhưng `loc-so-bo.tsv` dòng 36 không ghi.

## 3. Câu bắt buộc — tự kiểm trong `tong-hop-do.tsv`

**«Kênh nào ít video mà sub nhiều, video dài, view tốt?»** Tôi lọc ≤ 130 video, ≥ 5.000 sub, trung vị ≥ 2.000, rồi sắp theo số sub mỗi video:

| Kênh | Trạng thái | Video | Sub | Sub/video | Trung vị 20 dài | TV÷sub | Thời lượng | Video/30 ngày | Đà |
|---|---|---|---|---|---|---|---|---|---|
| **The Good Steward** | Loại | 44 | 186.000 | **4.227** | **159.898** | 0,86 | **11,4′** | 5 | 0,36 |
| Survival Kitchen 1930 | Loại | 77 | 194.000 | 2.519 | 269.712 | 1,39 | 8,3′ | 3 | 1,26 |
| Survival Blueprint | Giữ, hạng 10 | 25 | 16.200 | 648 | 8.313 | 0,51 | 31,9′ | 7 | 0,04 |
| Sheffield Made Gardens | Loại | 102 | 36.000 | 353 | 11.594 | 0,32 | 9,4′ | 0 | 1,26 |
| Blackout Shelter | Giữ, hạng 15 | 27 | 9.000 | 333 | 9.262 | 1,03 | 21,0′ | 3 | 0,11 |
| Home Garden Concepts (A) | Giữ, hạng 26 | 27 | 8.560 | 317 | 7.914 | 0,92 | 30,2′ | 0 | 0,16 |

- **Trả lời:** **The Good Steward** đúng nhất cả 4 vế: ít video, sub nhiều, view rất cao, và thời lượng 11,4′ đúng khung (Survival Kitchen 1930 chỉ 8,3′, 10/49 video nằm trong 10–14′). Kênh này **không ở hạng 1** vì bị loại trước khi xếp hạng, với lý do «người dẫn lên hình» dựa trên 1 storyboard (xem LH4). Nếu được giữ, chỉ số tích luỹ của nó đứng đầu tập: trung vị gấp 7,2 lần kênh cao nhất trong tập Giữ (Agriculture Insight, 22.096). Riêng đà 0,36 sẽ kéo hạng của nó xuống ở bộ «đà».
- Trong tập Giữ, Survival Blueprint không đứng hạng 1, dù đứng hạng 2 ở bộ tích luỹ, vì đà 0,037 nằm gần đáy (10 video gần nhất chỉ bằng khoảng 4 % trung vị 10 video trước) và phân tán 57,3 (một video đột biến). Kênh này cũng chỉ mới 91 ngày tuổi, với 7 video trong 30 ngày.
- Báo cáo bỏ sót **Home Garden Concepts**, kênh hướng A duy nhất trong nhóm này: 27 video, 0,92 trung vị÷sub. Kênh này không được cờ «ít video sub nhiều» vì sub/video 317 thấp hơn phân vị 75 của tập Giữ. Nhưng nó đã ngừng đăng (0 video/30 ngày) và đà chỉ 0,16, nên xếp hạng 26 là hợp lý.

## 4. Kênh có thể bị bỏ sót, loại oan hoặc giữ sai

**Loại oan hoặc cần mở lại:**
- **The Good Steward:** xem LH4. Đưa vào tab đối chứng, không làm Model Link.
- **The Grid-Down Kitchen:** bị xếp «Không đủ chỉ số» chỉ vì tỉ trọng Shorts *ước từ mẫu* là 0,218, sát ngưỡng 0,20. Trung vị 10.062, thời lượng 9,8′.
- **Sheffield Made Gardens** (hướng A, trung vị 11.594, 9,4′, đà 1,26): bị loại vì «Úc/Anh, quay thật [SUY LUẬN]». Lý do thị trường có thể đúng, nhưng chưa ai mở video để kiểm. Nên kiểm 1 storyboard.
- **Bị loại vì «lên hình» chỉ dựa trên tiêu đề:** có 14 kênh. Tôi đọc tiêu đề trong `thu-video/`. Các kênh S&K Greenhouse («I Visit This Garden…»), Charlie Survival («I Tried to Bug Out…»), SleepyLizard («Picking Avocado With a Professional Farmer»), Back To Reality (dừng đăng từ 2026-03-06) đúng là kênh có người lên hình hoặc đã chết. Epic Gardening, Millennial Gardener, Next Level, GrowVeg, Growing In The Garden là kênh người dẫn nổi tiếng, nên việc loại không làm sai kết luận. Tuy vậy, nhãn của các kênh này phải đổi từ [SUY LUẬN] sang [ĐO] bằng 1 storyboard mỗi kênh (khoảng 14 lần tải, 0 credit).
- Các kênh lớn này (trung vị 24K–162K) là **tín hiệu nhu cầu đề tài làm vườn**. Báo cáo bỏ chúng hoàn toàn thay vì đưa vào tab «đối chứng đề tài».

**Có thể đang được giữ sai trong TOP 20:**
- AgroWorks USA (hạng 8) và Living Self-Sufficiently (hạng 14): 0 video trong 30 ngày, tức đã ngừng đăng.
- Agriculture Insight (hạng 2): video 50,6′, dùng clip của người khác.
- Vintage Lifestyle USA: video 65,1′, đăng 29 video/30 ngày.
- When Power Fails: 52 ngày tuổi, phân tán 202, chỉ 3.220 sub.
- Plant Explainer: đà 12,1 là do một video đột biến.
- Ít nhất 6 kênh này nên mang cờ «không dùng làm mẫu».

## 5. Phép đo cần làm lại hoặc bổ sung trước khi dùng kết luận
1. Thu **danh sách video đầy đủ có ngày đăng** của NLH (410 video dài) và FAS (152), rồi tính lại trung vị theo tháng và đà trên mọi video, không chỉ cửa sổ cộng video phổ biến.
2. Lấy **ngày lập kênh** cho TOP 20 để tính hạng theo ngày lập và cờ TAI_SINH. Hiện cột này = «–» ở cả 61 kênh. Ưu tiên NLH vì có dấu hiệu đổi ngách.
3. **Xếp lại có trục định dạng**: chỉ tập Giữ có thời lượng 8–16′ và ≤ 4 video/tuần. Chạy thêm một lần riêng cho tập hướng A và AB.
4. **Sửa độ nhạy** để gộp các cách cho kết quả trùng nhau. Khi chưa có sub 30 ngày trước, báo «n/3 cách độc lập».
5. **Storyboard ≥ 3 video** cho The Good Steward, NLH, FAS, cộng 1 video cho mỗi kênh trong 14 kênh bị loại vì [SUY LUẬN]. Mỗi kênh mẫu cần ghi tỉ lệ khung là ảnh AI (NLH có khung trông giống ảnh AI dựng cảnh gia đình, chưa xác minh), vì chủ kênh muốn dùng AI càng ít càng tốt.
6. **Cặp đối chứng** cho mệnh đề «đề tài làm vườn thắng ở NLH». Tôi có số sơ bộ: trung vị 17.550 (n = 30) so với 10.991 (n = 39). Cần thêm kiểm tra mốc đăng (cùng tuần, cùng độ dài) và lấy ≥ 3 kênh làm vườn khác có hệ số > 3 cho cùng đề tài «cây bà trồng».
7. **Kho vượt trội**: tính `he_so_sau`, gắn cờ «chưa chín» cho video < 30 ngày, và kiểm tra số thật (like ≥ 0,5 %, đọc bình luận) cho các video ≥ 5×.
8. **Tuổi khán giả**: tăng mẫu bình luận lên ≥ 30 nhãn mỗi kênh trước khi xếp mức «Vừa».
9. **Tỉ trọng Shorts 30 ngày thật** (vidIQ) cho Grid-Down Kitchen và Roothaven Grounds.

## 6. Checklist `phan-bien.md` A–D

| # | Kết quả | Lý do ngắn |
|---|---|---|
| A1 | chưa đạt | Báo cáo trả lời đúng tên kênh nhưng không nêu The Good Steward khớp 10–14′ (11,4′). Survival Kitchen 1930 dài 8,3′ mà vẫn được gọi là «video dài». Lý do Survival Blueprint không hạng 1 giải thích sai định nghĩa đà. |
| A2 | đạt | 11/20 kênh trong TOP có tuổi < 365 ngày tính từ video đầu (FAS 238, Survival Blueprint 91, When Power Fails 52…). |
| A3 | chưa đạt | 12 kênh bị loại vì «lên hình [SUY LUẬN]» và 3 kênh «Úc/Anh [SUY LUẬN]» chưa mở video. The Good Steward bị loại chỉ dựa trên 1 storyboard. |
| A4 | chưa đạt | 8/20 kênh trong TOP có phân tán > 20 (Living Self-Sufficiently 262, When Power Fails 202, Plant Explainer 140, Saving Savers 90, Survival Blueprint 57, Lost American Memories 26, Frugal 22,6, FAS 21,6) nhưng vẫn ở TOP mà không có ghi chú. |
| B5 | đạt | NGHI_LOI_DON_VI (The Green Archive) đã kiểm tay. IT_VIDEO và NHIEU_VIDEO_CUNG_NGAY chỉ có ở kênh ngoài TOP hoặc kênh Theo dõi. |
| B6 | đạt | Kiểm 4 số, lệch 0 / 0 / 0 / 0,24 %. |
| B7 | chưa đạt | Cột `hang_theo_ngay_lap` = «–» ở cả 61 kênh, vì không lấy ngày lập. |
| B8 | đạt (có ghi chú) | `top20.tsv` và `xep-hang.md` chỉ lệch ở mức làm tròn (FAS đà 2,08 so với 2,09; Survival Blueprint 0,03 so với 0,04). Nhưng bảng tháng trong báo cáo mâu thuẫn với meta (`n_dai_flat` 410 trong khi chỉ đọc 104), xem LH3. |
| B9 | chưa đạt | Nhãn [ĐO]/[SUY LUẬN] có. Dòng 26–27 của báo cáo không ghi n và không ghi rằng đó là mẫu cửa sổ cộng video phổ biến. |
| B9a | chưa đạt | Xếp hạng có chạy trên tập Giữ (đạt). Khoảng hạng của TOP 5 là 1–5, 2–6, 2–8, 1–4, 5–10, tức không có kênh nào vững. |
| B9b | chưa đạt | Grid-Down Kitchen và Roothaven Grounds mang SUB_LAN_SHORTS và «Không đủ chỉ số», nhưng tỉ trọng Shorts mới ước từ mẫu, chưa lấy số thật. |
| B9c | chưa đạt | Lost American Memories (đà 0,15, hạng 9), Survival Blueprint (0,04, hạng 10), Blackout Shelter (0,11, hạng 15) đang đi xuống mà vẫn nằm trong TOP, không có cảnh báo. |
| B9d | chưa đạt | Đã chạy, nhưng 2 trong 5 cách trùng với «tổng», nên «3/5» thực chất là 1/3 (LH2). |
| B9e | chưa đạt | HOI_VIEN đã ghi cho NLH và Sidney Explains. TAI_SINH không tính được vì thiếu ngày lập, trong khi NLH đã đổi ngách (hoài cổ 2025 → bà ngoại, vườn, dự trữ 2026) mà chưa được ghi. |
| C10 | chưa đạt | Tuổi khán giả chỉ có n ≈ 8 (NLH) và ≈ 5 (FAS). NLH có tiêu đề «for Seniors» vi phạm L9 mà chưa đưa vào cột «Không học». |
| C11 | chưa đạt | Cả hai ứng viên đăng khoảng 6 video/tuần, dài 30′. Khung yêu cầu ≤ 4 video/tuần và 10–14′. |
| C12 | đạt một phần | FAS có ghi rủi ro L8. NLH thiếu cột «Không học» cho tiêu đề nhãn tuổi, tiêu đề âm mưu «Exterminators Hide», và mảng đồ cổ hay trang điểm 1950s. |
| C13 | chưa đạt | Chưa có cặp đối chứng hay kiểm mốc đăng. Số sơ bộ của tôi (vườn 17.550 so với khác 10.991) mới chỉ là gợi ý. |
| D14 | đạt một phần | vidIQ dùng 0 credit (đúng, vì cả 4 tài khoản gần hết credit). Không ghi tổng thời gian. Có 6 kênh phải thu lại vì bị chặn bot, đã thu xong. |
| D15 | chưa đạt | Agriculture Insight và Forgotten Old American đã có ghi chú. Lost American Memories có khung phỏng vấn truyền hình nhưng chưa ghi. Chưa đánh giá tỉ lệ ảnh AI hay nhãn nội dung AI cho NLH và FAS. |
