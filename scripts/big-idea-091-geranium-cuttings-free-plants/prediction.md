# Prediction — big-idea-091-geranium-cuttings-free-plants

> Ghi tại GATE Script (24/10/2026). Số baseline: `references/channel-health-latest.json` (làm mới 23/10, 8 tuần) + vidIQ 23/10. Mọi khoảng dưới đây là **ước lượng của tôi dựa trên số kênh đã ghi, không phải mô hình**; số thật nằm ngoài khoảng → ghi nguyên nhân vào `retro.md`.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-091-geranium-cuttings-free-plants |
| Ngày scripted | 2026-10-24 (qua audit độc lập · Triple F · compliance · TTS clean) |
| Target publish | **tuần đầu tháng 11/2026** (sương giá đầu mùa; trễ sau giữa tháng 11 phải dời cửa sổ giâm sang tháng 2–3 và đổi "Now" ở title) |
| Compliance score (lúc GATE) | **9/10** (subagent độc lập, ngưỡng PASS); đã vá 4 điểm an toàn nhỏ sau đó (trẻ em, bột kích rễ, ASPCA "lists as toxic", hedge hook) — **chưa chấm lại** |
| Lane / nguồn | A · `/san-y-tuong` 23/10 (phiếu: `research/phieu-kiem-dinh-geranium-overwinter-2026-10-23.md`, dữ liệu `research/geranium-vongA/`) · Topic Gate 2/3 (① ✅ ② ✅ ③ 🟡) |
| Độ dài thực tế | **3.008 từ ≈ 18,2 phút @165wpm** (voice Key gardent chưa đo bản này) · config `video_length` 20–24′ / 3.300–4.000 từ → **dưới sàn có chủ đích** |

## 🧪 TEST (khai trước để retro biết phải trả lời gì)
1. **TEST độ dài (L7 vs config 20–24′):** video ~18,2′ khi config yêu cầu 20+. Dưới sàn vì brief mỏng ở M3–M6 và **không độn** (user chấp nhận 24/10). Câu hỏi retro: so với dải 12–20′ của kênh (n=15, median 632 view, AVD 29,3%) và 3 video 20–40′ (median 936 view, AVD 26,2%), video này có views_5d và **giờ xem/lượt** cao hơn không? ⚠️ Không so AVD% giữa video dài khác nhau để kết luận độ dài; so **giờ xem tuyệt đối**.
2. **TEST dẫn nguồn "nói thẳng, đừng cite" (L19):** cite chung chung còn 4 câu / 3.000 từ (trước khi sửa: 6 câu/1.100 từ). Câu hỏi retro: đường cong retention có điểm rơi tại các chỗ cite (M5 vùng bảng bất đồng) hay tại chỗ khác? Đây là **ý user, chưa có số** — không coi là luật đã chứng minh.
3. **TEST khán giả 35–60+:** ngôn ngữ đổi (tiền/thời gian/sức, bỏ "seniors/retired"). Đọc Studio → Demographics (độ tuổi) sau 7–14 ngày; so với tỷ lệ 55+ hiện tại của kênh. Cỡ mẫu nhỏ → không kết luận từ 1 video.
4. **TEST thumbnail `$0 NURSERY BILL`** (đòn bẩy chi phí, không từ trùng title). Chưa có A/B (một bản). Nếu CTR giờ 48 <4% → dùng Test & Compare với bản `$0 IN MAY`-không-hứa-mốc hoặc bản không chữ tiền.
5. **TEST khuôn deep-dive giâm cành (đối thủ 709K):** Topic Gate ② mạnh (All About Plants 709K/180K, kênh 126K sub) nhưng ③ yếu (cụm "geranium cuttings" <750/th, số 03/2026). Câu hỏi retro: nhu cầu có đến từ **gợi ý (browse/suggested)** như video đối thủ, hay từ tìm kiếm?

## Title bet
- **Title chốt:** `Take Geranium Cuttings Now - Free Plants Next Spring (The 3-Inch Rule)` (vidIQ 86/100, 24/10)
- Specific quantity? **Y** ("3-Inch") · KEYWORD-FIRST: "Geranium Cuttings" bắt đầu ở ký tự 6 ✅
- Leading number? **N**
- Độ dài: **11 từ / 70 ký tự** (dài hơn mục tiêu 65 → có thể bị cắt trên mobile). **Swap giờ 48 nếu CTR <4%:** `Take Geranium Cuttings Now: Free Plants Next Spring (3-Inch Rule)` (65 ký tự, chưa chấm).
- ⚠️ DELIVERY-LOCK: "3-Inch Rule" = quy ước của kênh; script luôn nói "three to four inches" (`PROMISE_OK` đã khai).

## Retention bets (theo mốc thật của bản TTS clean @165wpm)
- **Topic familiarity:** **Y** — phong lữ là cây hiên quen thuộc nhất với người Mỹ (L1 ✅).
- **L6 (giây 20–34):** không có claim ngược đời; số "three to four inches" ở **0:01**, bằng chứng nguồn bằng thẻ màn hình 0:16–0:25.
- **Giây 40–55 (L4):** Loop #1 ("one guide adds a step…", gieo **0:21**) còn sống; M1 mở bằng giá trị (cách cắt) lúc 0:36, **không** có lộ trình (L15 ✅).
- **Phút 4–6 (L5):** Loop #1 + Loop #2 ("one thing on that stem has to come off", gieo **3:29**, đóng **6:16**) cùng sống · sai lầm #1 ở 4:17 · Jenga: **ON**.
- **Giữa video:** re-hook "turn black at the base" **9:16** → **climax (heal) 10:06**, bảng bất đồng 10:38.
- **Phần sau climax (điểm yếu có biết):** lời hứa cuối gieo **12:06** → mở M7 14:06 → câu trả lời thật ("cuttings are the insurance") chỉ ở **16:10**; sau đó phần Q (17:10) toàn "chưa có câu trả lời". Audit độc lập chỉ ra các điểm rơi dự kiến: ~5:23–6:03, 6:22–9:24 (M3 mỏng nhất), 14:48–15:57, 16:45–17:35. **Chưa vá** vì không có nguồn để gieo vòng lặp mới mà không bịa.
- **Editorial Signature (L13):** bảng đối chiếu bốn hướng dẫn về callus (M5) · phụ: lịch đếm tuần.
- **Consensus Synthesis:** 2 (M3 "three university sites…", M6 "sources give three windows…").
- **Micro-bridge:** cuối M1, M2, M3, M4, M5, M6 đều mở vấn đề mới (không tóm tắt).
- **Scene viewer-POV:** hàng chậu ngoài hiên (M2) · tuần thứ ba (M6). **Story Bank:** trống (không bịa).
- **Hook:** A2.1 (100 từ, 0 tên trường đọc bằng giọng).

## Engagement bets
- Themes: ☑ Pet/Kid safety (ASPCA, trẻ em, bột kích rễ) · ☑ USDA zone/climate (ngày sương giá theo zone, M1 · M7) · ☑ Nostalgia dạng chung ("a paper sack in a cool basement", M7)
- Câu kích: *"Tell us in the comments: heal first, or straight in?"* (M5) · *"Tell us where you keep yours, and what zone you're in."* (M7) · Q: *"Put your answers in the comments."*
- **Bình luận ghim (soạn khi đăng):** danh sách câu chưa ai trả lời (muỗi nấm, giâm trong nước, cắm thẳng vào đất, rác nhựa); ASPCA Poison Control **888-426-4435** (số có trong brief, chưa kiểm lại trang) nên để ở mô tả/pinned, không đọc to.

## Dự đoán số (baseline kênh, health 23/10)
| Chỉ số | Baseline | DỰ ĐOÁN | Lý do |
|--------|----------|---------|-------|
| **views_5d** *(thước chấm chính)* | median **597** (health 23/10; config cũ ghi 285) | **450–900** · PASS ≥597 · stretch ≥900 | chủ đề mùa vụ gấp + franchise nhân giống (13K) + có video đối thủ 709K chứng minh cầu; trừ: cụm tìm kiếm cụ thể nhỏ, kênh Browse đang -3,9 điểm, video ngắn hơn khung nên chưa chắc kéo được giờ xem |
| **Giờ xem / lượt** *(thước chính thứ hai)* | ~195 giây watch-budget | **3,8–5,2 phút** | = AVD% × 18,2′; nếu AVD 21–28% |
| AVD % *(chẩn đoán phụ, KHÔNG phải verdict)* | 29,4% (tuần mới nhất) | **21–28%** | video 18′ dài hơn dải 12–20′ (29,3%) nhưng có 3 loop + climax ở 10′; phần sau climax là điểm yếu |
| CTR % (giờ 48) | 5,5% (28 ngày, nhập tay) | **4,5–6,0%** | title 86/100 + từ khóa sớm + thumbnail chi phí mới; ③ yếu; chưa A/B |
| Tổng giờ xem 5 ngày | — | tính = views_5d × giờ/lượt | đọc kèm views_5d |
> Cược lệch xuống (<400 views_5d) → xem lại TEST #5 và #4 trước khi kết luận về độ dài (#1).

## Rủi ro đã biết
- **Chất liệu mỏng M3–M6** (đã báo từ GATE 1.5): chưa có thời gian "heal" tại nhà, dấu hiệu ra rễ, xử lý mốc, giá tiền, muỗi nấm — script nói thẳng "chưa có" thay vì bịa; có thể làm người xem thấy thiếu thực dụng.
- **Climax dựa trên bất đồng nguồn chứ không phải một kỹ thuật chắc chắn** (2 trang nói heal, 4 trang im; Penn State/Texas A&M giọng nhà kính). Khuyến nghị "heal là mặc định" dựa trên "không nguồn nào nói đừng".
- **Hiệu ứng kênh của đối thủ:** 2/6 video thắng trong mẫu C1 là của một kênh 126K sub → THR 0,64 (độ tin thấp, 9 video) có thể nhiễm.
- **Mốc đăng:** trễ sau giữa tháng 11 → mất cửa sổ sương giá.
- **Giọng Key gardent chưa đo trên bản này**; cần nghe thử "Pelargonium", "Texas A&M", "ASPCA", "pinch, pinch, done".
- **Nhắc video/bình luận ẩn danh của kênh khác:** số "more than seven hundred thousand views" là cận dưới của 709.474 (đo 23/10); nếu đăng muộn nhiều tuần vẫn đúng.
- **Một chỗ đã chỉnh hook đã duyệt:** "you leave" → "you may leave" (hedge, 24/10).

## Mốc đọc retention (để quyết định ở retro)
Đọc 3 đường cong: (1) giây 0–60 so với hook cliff TB kênh (-37% tới giây 25); (2) **11:00–14:00** (ngay sau climax 10:06 — có rơi mạnh không?); (3) **16:00–18:13** (câu trả lời "insurance" + phần Q + KẾT). Nếu rơi ở (2) → lời hứa cuối quá yếu; nếu rơi ở (3) → phần Q/KẾT thừa. Chạy `python tools/yt_analytics.py retro <videoId>` 7–14 ngày sau đăng.
