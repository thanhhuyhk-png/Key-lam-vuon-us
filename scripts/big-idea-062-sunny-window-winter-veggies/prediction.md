# Prediction — big-idea-062-sunny-window-winter-veggies

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-062-sunny-window-winter-veggies |
| Ngày scripted | 2026-10-17 (v2, đã xuất) · **viết lại v3 2026-10-18** (`script.v3.md`, voice v3, draft `G062v3b_auto`) — bản prediction cũ giữ ở `prediction.v2-17oct.md` |
| Target publish | **sớm trong tháng 10** (3 video cùng khung năm ngoái đăng 20/10–22/12/2025); chốt khi có voice, hình và thumbnail. Tránh trùng ngày với 061 và 047. |
| Compliance score (lúc GATE) | v2: **10/10** (subagent độc lập). **v3: chưa chấm lại** — lint L14–L18 (`tools/script_lint.py`): **FAIL 1 lỗi (L15)**; claim_check OK; originality 0 câu trùng với 058–061. |
| Lane / nguồn | A · Topic Gate 17/10 (trong `pipeline-state.md`), nguồn ý tưởng `/san-y-tuong` (phiếu `research/phieu-kiem-dinh-winter-veg-indoors-2026-10-17.md`), KHÔNG phải Notion |
| Độ dài thực tế | **v3: 2.742 từ, voice Key gardent (clone_2697441) 16:44** (1.004 giây, `voice/v3/voice.mp3`, 18/10) · v2 đã xuất: 3.045 từ, 18:31 · override `video_length` chỉ cho video này |

## 🧪 TEST (GATE 2/3 thiếu ①)
1. **TEST độ dài (L7):** video ~17–18′ so với mặc định 8–10′. Dữ liệu cũ: 17–19′ → AVD 14–20%; chỉ "7 Plants Water" 13:56 đạt 49%. Thước đo đúng: `views_5d` vs 523 và **giờ xem/lượt**, ⛔ không chấm bằng AVD%.
2. **TEST khuôn:** listicle nhiều món faceless nhưng khác ở mức sáng + bảng bất đồng nguồn + nguồn đại học. Nhánh listicle faceless-senior đã bão hòa theo `health-log` W41 (2–7K view/video).
3. **① ❌:** kênh chưa có hit cùng cây/vật (nhóm gần nhất: *7 Indoor Plants… JUST Water* 22,9K).
4. **③ yếu:** "grow vegetables indoors" 4,472/th, `countryVolume` null, growth null cho cụm chính; cụm đúng ý định ("…in winter") <750. Không chắc thuần US.
5. **② trái mùa:** 3 outlier (148K–536K) đều đăng 10–12/2025; mẫu 90 ngày gần cho thấy OM giảm ~33% (trái mùa).
6. **Hình ảnh trộn stock + đồ họa + AI/Veo:** chưa có tiền lệ trên kênh.
7. **"Easy" chưa khớp hoàn toàn với nguồn** (microgreens, radish): script đã nêu giới hạn.
8. **Cùng cửa sổ mùa với 047** (houseplants indoors before frost, chưa đăng) → có thể cannibalize; tách rõ: 047 = cây cảnh, 062 = rau ăn được.

## Title bet
- **Title chốt v3:** `Grow Vegetables Indoors This Winter (5 Can Use a Window, 2 Need a Lamp)` (bỏ "Easy" — L17: hẹ 12 tuần, radish "nguồn không nói", microgreens thường tốt nhất dưới đèn). Title cũ v2: `… (5 Easy, 2 Need a Light)`. vidIQ: bản "3 Need" của title cũ **85**; title v3 **chưa chấm** (hết credit).
- **Swap giờ 48 nếu CTR <3.5%:** `5 Veggies for a Sunny Window This Winter (+2 That Need a Lamp)` — chưa chấm.
- Specific quantity? **Y** (5, 2) · KEYWORD-FIRST: **bật** — "Grow Vegetables Indoors" trong 23 ký tự đầu ✅ · L17 ✅ (không còn chữ hứa bị script phủ định) · L9 ✅ · L1 ✅.
- Độ dài: 13 từ / 71 ký tự (dài hơn bản cũ ~11 ký tự; kiểm bị cắt trên mobile nếu CTR thấp).

## Thumbnail bet (Test & Compare, MODE 1 — user chốt 18/10: dùng **ảnh thật** `thumbnail-real-a` và `thumbnail-real-b`)
| | Concept | Text | File |
|---|---|---|---|
| **A** | Verdict / Before→After ❌/✅ (mầm vươn trong tối vs cây dưới đèn bàn) | `LEGGY?` / `6-8 HOURS` + pill `ILLINOIS EXTENSION` | `thumbnail-real-a.jpg` |
| **B** | Curiosity + số (cà chua xanh trên cây, chữ trên nền tối dần) | `NO FRUIT?` / `6 HOURS DARK` + pill `NEW HAMPSHIRE EXTENSION` | `thumbnail-real-b.jpg` |
- Ảnh Pexels từ `_LIBRARY` (giấy phép tự do), chữ vàng/trắng viền đen, tool `tools/garden_thumb_real.py`. Hai bản AI cũ (`thumbnail-a.jpg`, `thumbnail-b.jpg`) **không dùng** cho test này (giữ làm dự phòng). Complementarity với title v3: 0 từ trùng ✅.
- Giả thuyết thêm của lần test này: **ảnh thật + nhãn nguồn nhỏ có tăng CTR/niềm tin so với ảnh AI không?** (chưa có thumbnail AI của chính bài này làm đối chứng đồng thời — so với CTR 3 bài gần nhất).
- Kênh đang impression thấp → **đọc kết quả thận trọng**; chỉ kết luận khi đủ impression; không đổi bài giữa chừng vì chênh nhỏ.
- **Lưu ý giữ lại khi đọc kết quả:**
  1. **A:** `6-8 HOURS` cạnh hình đèn có thể bị đọc là "đèn chạy 6–8 giờ"; số thật là giờ sáng mạnh cho rau lá/thảo mộc (CL-001). Nửa ✅ là **cây cảnh dưới đèn**, không phải rau; nửa ❌ là mầm trong chậu tối (không hẳn "cửa sổ").
  2. **B:** ảnh cà chua **xanh có quả** trong khi chữ hỏi `NO FRUIT?` — có thể bị hiểu là mâu thuẫn hình–chữ. `6 HOURS DARK` chỉ đúng cho cà chua (ớt không cần).
  3. Pill nguồn nhỏ (~26px) khó đọc ở kích thước nhỏ (squint test): vai trò là tín hiệu uy tín, không phải chữ hook.
  4. Cùng khuôn "câu hỏi triệu chứng + số" với 061 (`NO BUDS? / 6–8 HRS`) → cân nhắc đổi khuôn ở bài sau.
- **Câu hỏi retro:** A hay B thắng CTR giờ 48? Ảnh thật + nhãn nguồn có đáng thay AI ở bài sau? Thắng thumbnail có đi cùng giữ chân tốt không?

## Retention bets (theo `voice/v3/voice.srt` thật, 16:44)
- **Topic familiarity:** **Y** (L1 ✅)
- **L6:** "six to eight hours" ở giây ~2 ✅ · **L3:** 5 + 2 và cà chua/ớt ở giây ~25 ✅
- **L4 (giây 40–55): ⚠️ KHÔNG ĐẠT theo audio thật.** Loop A "quiet sign" mở 0:33 nhưng **câu lộ trình + danh sách nguồn đọc ở 0:43–0:58** ("First, the light itself… Then the seven vegetables… Then one table… Everything here comes from university extension offices") — đúng vùng chết 40–55s, vi phạm L15. Lint ước lượng ban đầu tính sai giây nên lúc đầu báo PASS; đã siết regex, hiện FAIL. **Rủi ro đã biết, bản đã dựng giữ nguyên**; nếu retention tụt ≥15 điểm % quanh 0:40–0:60 → xác nhận L15, và lần sau rút lộ trình còn 1 câu đặt sau giây 60.
- **L16 ✅:** mẹo "write sun or no sun" ở **2:28** (v2 ở 17:27), gọi lại ở cuối bài.
- **Phút 4–6 (L5):** Loop B ("hai cây cùng cần đèn, chỉ một cây cần tối") mở **3:17**, sống qua 4–6′, đóng ở **8:51** (cà chua cần ~6 giờ tối) và **10:05** (ớt thì không) · Jenga Retention: **ON**
- **Loop C** ("ba chỗ nguồn nói khác nhau") mở **6:16**, đóng ~11:10–12:30 (bảng + 3 chỗ bất đồng).
- **Editorial Signature (L13):** thẻ bảng Window or Lamp? ở **10:33** + 3 chỗ bất đồng (số giờ · khoảng cách đèn · rửa microgreens), tới ~12:32.
- **L14:** tên nguồn bằng giọng gộp ("extension guides") ngoài vùng bảng; **L18:** bảng chỉ nói quy luật, số do thẻ chalk mang.
- **Micro-bridge:** mọi ranh giới mục · thẻ đếm 2/7–5/7, 7/7 · Scene viewer-POV: "December afternoon" (1:01), "the morning your tray is green" (16:11) · Story Bank: trống (không bịa).
- **Hook:** V2 Proof-first (rút tên New Hampshire khỏi hook).
- **Hình/dựng (template 18/10):** thẻ chalk 9–21s gắn lời đọc, chữ ít, SFX mọi chữ, nhạc 0:00–1:00.

## Engagement bets
- Themes: ☑ Pet/Kid safety (nhãn thuốc, cất ngoài tầm với, ASPCA) ☐ Nostalgia (không dùng) ☑ Vùng khí hậu (hướng cửa sổ, giờ nắng mùa đông)
- Câu kích theme: *"Which way does your kitchen window face, and how many hours of sun does it get in winter? Tell me in the comments."* (~17:08)

## Dự đoán số (baseline: video mới, channel-health 05/10)
| Chỉ số | Baseline | DỰ ĐOÁN | Lý do |
|--------|----------|---------|-------|
| CTR % (giờ 48) | 2.94% (video mới) | **2.8–3.8%** | số + keyword-first + chủ đề theo mùa; ③ yếu, ① ❌ |
| AVD % | 28.3% (kênh gần đây) | **14–22%** | video 16–17′: băng 17–19′ cũ ra 14–20%; 3 loop + bảng + mẹo sớm có thể kéo lên; lộ trình ở 0:43 là nguy cơ |
| Giờ xem/lượt | ~195 giây watch-budget (config) | **2,3–3,7 phút** | = AVD% × 16,7′; đây là thước đo chính |
| View 5 ngày đầu | 523 (median) | **450–900** | sống nhờ Browse; ngưỡng phục hồi >800; nếu <400 cân nhắc nghĩa của TEST khuôn |
> Mọi khoảng trên là ước lượng của tôi dựa trên các số kênh đã ghi, không phải mô hình. Nếu số thật nằm ngoài khoảng, ghi nguyên nhân vào `retro.md`.

## Rủi ro đã biết
- **Nhánh listicle bão hòa** + **không có hit cùng cây** (① ❌).
- **Chất liệu chạm đáy:** radish, ớt, hẹ/mùi tây mỏng nguồn; không độn nên script ngắn hơn mục tiêu 20–22′.
- **Nguồn cũ/ít:** UIUC 2017, UNH Ch.10 (năm không rõ); chỉ một nguồn cho cà chua/ớt (UNH Ch.10) ngoài USU; thụ phấn tay không có nguồn nên bỏ.
- **Tốc độ voice mới đo trên mẫu 23 giây** → thời lượng thật có thể lệch ±10%.
- **Trái mùa/ hạn đăng:** nếu trễ sau giữa tháng 11, nhu cầu "winter indoor veggies" có thể đã qua đỉnh.
- **Sử dụng hình AI/Veo:** rủi ro bị hiểu là quay thật → nhãn `illustration` và cân nhắc nhãn synthetic.
- **Title v3 dài hơn (71 ký tự):** có thể bị cắt trên mobile; kiểm CTR theo thiết bị.
- **Lộ trình đọc ở 0:43–0:58 (L15 FAIL thật):** xem Retention bets.
- **Thumbnail ảnh thật:** nửa ✅ A là cây cảnh, B là cà chua xanh có quả — hình–chữ chưa khớp hoàn toàn.

## Mốc đọc retention (để quyết định ở retro)
Lấy từ `python tools/yt_analytics.py retro <videoId>` và so với video dài gần nhất (061) + 058–060:
| Mốc | Vì sao |
|---|---|
| 0:30 | hook cliff — L6/L3 có giữ không |
| ~2:00 | loop A đóng, vào phần ánh sáng |
| ~5:00 | giữa microgreens/baby greens, loop B còn mở |
| ~9:00 | trước/ khi trả loop B (cà chua) |
| ~12:00 | bảng Window or Lamp? |
| ~15:00 | phần sự cố |
Quy tắc đọc: nơi nào retention tụt >15 điểm % giữa hai mốc liên tiếp → mở script đoạn đó. Nếu tụt chủ yếu sau ~12:00 → chất liệu cuối (đèn, sự cố) cần ngắn hơn lần sau.

## Câu hỏi cho retro
1. Bản 16:44 có hơn median 523 views_5d và giờ xem/lượt hơn video 8–10′ gần nhất không?
2. CTR giờ 48 ≥3.5% với title keyword-first khi ③ yếu? Search share so với 058? Thumbnail A hay B thắng (Test & Compare)?
3. Retention qua giây 40–55 và phút 4–6 so với 061 và 058–060?
4. Bảng Window or Lamp? có kéo comment về hướng cửa sổ / "tôi nên làm theo ai" không (Editorial Signature chạm không)?
5. Title "Can Use a Window" có giữ CTR so với "Easy" không (không có đối chứng trực tiếp)? Có comment nào phản ứng về lời hứa?
6. Phần hình AI/Veo có bị comment nhận ra/ phàn nàn không?
7. Khuôn "nhiều món + bảng nguồn" có đáng lặp lại ở bài sau không, hay quay lại "một cây, một cách lười"?
