# Prediction — big-idea-062-sunny-window-winter-veggies

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-062-sunny-window-winter-veggies |
| Ngày scripted | 2026-10-17 |
| Target publish | **sớm trong tháng 10** (3 video cùng khung năm ngoái đăng 20/10–22/12/2025); chốt khi có voice, hình và thumbnail. Tránh trùng ngày với 061 và 047. |
| Compliance score (lúc GATE) | **10/10** — subagent độc lập (vòng 1: 9/10; vòng 2: 10/10). Reviewer chưa mở phần header (title/thumbnail). |
| Lane / nguồn | A · Topic Gate 17/10 (trong `pipeline-state.md`), nguồn ý tưởng `/san-y-tuong` (phiếu `research/phieu-kiem-dinh-winter-veg-indoors-2026-10-17.md`), KHÔNG phải Notion |
| Độ dài thực tế | 3.045 từ, voice Key gardent (clone_2697441) **18:31** (đo từ `voice.mp3`, 17/10) · override `video_length` chỉ cho video này |

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
- **Title chốt:** `Grow Vegetables Indoors This Winter (5 Easy, 2 Need a Light)` — vidIQ **85** cho bản "3 Need"; bản "2 Need" **chưa chấm** (hết credit).
- **Swap giờ 48 nếu CTR <3.5%:** `5 Veggies for a Sunny Window This Winter (+2 That Need a Light)` — vidIQ 89 cho bản "+3"; **phải chấm lại** bản "+2".
- Specific quantity? **Y** (5, 2) · Leading number? **N** (số ở vị trí 8–9) · KEYWORD-FIRST: **bật** — cụm "Grow Vegetables Indoors" nằm trong 23 ký tự đầu ✅
- Độ dài: **11 từ / 60 ký tự** ✅
- Khung W41 ②: "ĐƯỢC THÊM" ~ ra rau ✅ · công sức↓ ("Easy") ✅ · không sợ/độc/chết ✅ · L9 ✅ · cây quen thuộc L1 ✅ · **lệch ③ "MỘT cây"** (xem TEST 2).

## Thumbnail bet (Test & Compare, MODE 1 — user chốt 17/10: dùng nguyên cả A và B)
| | Concept | Text | File |
|---|---|---|---|
| **A** | Verdict / Before→After ❌/✅ (cây vươn dài ở cửa sổ vs cây khỏe dưới đèn) | `LEGGY?` / `6-8 HOURS` | `thumbnail-a.jpg` |
| **B** | Curiosity + số (cà chua có hoa, chưa quả, dưới đèn, đêm có trăng) | `NO FRUIT?` / `6 HOURS DARK` | `thumbnail-b.jpg` |
- Render bằng G-Labs (nano_banana_pro), 17/10; chữ đúng chính tả cả hai; không mặt người, không tay.
- Kênh đang impression thấp → **đọc kết quả thận trọng**: mẫu nhỏ làm Test & Compare yếu thống kê. Chỉ kết luận khi đủ impression; không đổi bài giữa chừng vì chênh nhỏ.
- **Lưu ý giữ lại khi đọc kết quả:**
  1. **A:** `6-8 HOURS` đứng cạnh hình đèn có thể bị đọc là "đèn chạy 6–8 giờ"; số thật là giờ sáng mạnh cho rau lá/thảo mộc (CL-001). Nếu comment hỏi về giờ đèn → đây là nguyên nhân. Hai nửa gần 50/50 (yêu cầu 60/40).
  2. **B:** đèn **bật** trong đêm trong khi chữ nói `6 HOURS DARK`; có thể bị hiểu là "đèn bật cả đêm làm cây không có quả" (khớp câu hỏi) hoặc là mâu thuẫn hình–chữ. Số `6 HOURS DARK` chỉ đúng cho **cà chua** (ớt không cần), hình B là cà chua.
  3. Cả hai là **ảnh AI dựng**, không phải kết quả thật của kênh.
  4. Cùng khuôn "câu hỏi triệu chứng + số" với 061 (`NO BUDS? / 6–8 HRS`) → khuôn chữ lặp; cân nhắc đổi khuôn ở bài sau.
- **Câu hỏi retro:** A (Verdict, lo → nhẹ nhõm) hay B (Curiosity, tò mò) thắng CTR giờ 48? Khán giả kênh phản ứng với "làm gì để đúng" hay "đang thiếu gì"? Thắng ở thumbnail có đi cùng giữ chân tốt không (xem mốc retention ở dưới)?

## Retention bets (3 luật cứng, theo script cuối, 175 wpm)
- **Topic familiarity:** **Y** — xà lách, cà chua, ớt, thảo mộc quen thuộc (L1 ✅)
- **L6:** "six to eight hours" ở giây ~6 ✅ · **L3:** lời hứa 5 + 2 và tên cà chua/ớt ở giây ~30 ✅
- **Giây 40–55 (L4):** Loop A "quiet sign" mở giây ~31–39, câu lộ trình ở giây ~39–59 nhắc lại ("that quiet sign") ✅; đóng ở ~1:47 (đoạn "That's the quiet sign").
- **Phút 4–6 (L5):** Loop B ("hai cây cùng cần đèn, một cây cần tối") mở ~3:20, sống qua 4–6′, đóng ở 9:22–9:44 (cà chua cần ~6 giờ tối, ớt thì không) · Jenga Retention: **ON**
- **Loop C** ("ba chỗ nguồn nói khác nhau") mở ~6:34, đóng ~11:49 (bảng Window or Lamp?).
- **Editorial Signature (L13):** bảng đối chiếu + 3 chỗ bất đồng (số giờ · khoảng cách đèn · rửa microgreens) ở ~11:06–13:02.
- **Micro-bridge:** có ở mọi ranh giới mục 3–9; bộ đếm 2/7, 3/7, 4/7, 5/7 · Scene viewer-POV: "December afternoon" (1:11) · Story Bank: trống (không bịa).
- **Con số xương sống:** "six to eight hours" × 7.
- **Hook:** V2 Proof-first (118 từ, nguyên văn đã duyệt).

## Engagement bets
- Themes: ☑ Pet/Kid safety (nhãn thuốc, cất ngoài tầm với, ASPCA) ☐ Nostalgia (không dùng) ☑ Vùng khí hậu (hướng cửa sổ, giờ nắng mùa đông)
- Câu kích theme: *"Which way does your kitchen window face, and how many hours of sun does it get in winter? Tell me in the comments."* (~17:08)

## Dự đoán số (baseline: video mới, channel-health 05/10)
| Chỉ số | Baseline | DỰ ĐOÁN | Lý do |
|--------|----------|---------|-------|
| CTR % (giờ 48) | 2.94% (video mới) | **2.8–3.8%** | số + keyword-first + chủ đề theo mùa; ③ yếu, ① ❌ |
| AVD % | 28.3% (kênh gần đây) | **14–22%** | video 17–18′: cùng băng 17–19′ cũ ra 14–20%; 3 loop + bảng giữ chân có thể kéo lên |
| Giờ xem/lượt | ~195 giây watch-budget (config) | **3,0–4,2 phút** | = AVD% × 17,3′; đây là thước đo chính |
| View 5 ngày đầu | 523 (median) | **450–900** | sống nhờ Browse; ngưỡng phục hồi >800; nếu <400 cân nhắc nghĩa của TEST khuôn |
> Mọi khoảng trên là ước lượng của tôi dựa trên các số kênh đã ghi, không phải mô hình. Nếu số thật nằm ngoài khoảng, ghi nguyên nhân vào `retro.md`.

## Rủi ro đã biết
- **Nhánh listicle bão hòa** + **không có hit cùng cây** (① ❌).
- **Chất liệu chạm đáy:** radish, ớt, hẹ/mùi tây mỏng nguồn; không độn nên script ngắn hơn mục tiêu 20–22′.
- **Nguồn cũ/ít:** UIUC 2017, UNH Ch.10 (năm không rõ); chỉ một nguồn cho cà chua/ớt (UNH Ch.10) ngoài USU; thụ phấn tay không có nguồn nên bỏ.
- **Tốc độ voice mới đo trên mẫu 23 giây** → thời lượng thật có thể lệch ±10%.
- **Trái mùa/ hạn đăng:** nếu trễ sau giữa tháng 11, nhu cầu "winter indoor veggies" có thể đã qua đỉnh.
- **Sử dụng hình AI/Veo:** rủi ro bị hiểu là quay thật → nhãn `illustration` và cân nhắc nhãn synthetic.
- **Title "Easy":** nếu comment phản ứng "tôi làm không được/ thiếu sáng", đổi sang `5 Worth Trying`.

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
1. Bản 17′ có hơn median 523 views_5d và giờ xem/lượt hơn video 8–10′ gần nhất không?
2. CTR giờ 48 ≥3.5% với title keyword-first khi ③ yếu? Search share so với 058? Thumbnail A hay B thắng (Test & Compare)?
3. Retention qua giây 40–55 và phút 4–6 so với 061 và 058–060?
4. Bảng Window or Lamp? có kéo comment về hướng cửa sổ / "tôi nên làm theo ai" không (Editorial Signature chạm không)?
5. Nhãn "Easy" có bị phản ứng không?
6. Phần hình AI/Veo có bị comment nhận ra/ phàn nàn không?
7. Khuôn "nhiều món + bảng nguồn" có đáng lặp lại ở bài sau không, hay quay lại "một cây, một cách lười"?
