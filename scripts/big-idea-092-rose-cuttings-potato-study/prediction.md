# Prediction — big-idea-092-rose-cuttings-potato-study

> Ghi tại GATE Script (24/10/2026). Baseline: `references/channel-health-latest.json` (23/10) + vidIQ 24/10 + `research/phieu-kiem-dinh-rose-potato-2026-10-24.md`. Mọi khoảng dưới đây là **ước lượng của tôi dựa trên số kênh đã ghi, không phải mô hình**; số thật nằm ngoài khoảng → ghi nguyên nhân vào `retro.md`.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-092-rose-cuttings-potato-study |
| Ngày scripted | 2026-10-24 (qua Pha D · audit độc lập REVISE → đã sửa theo nguồn · Triple F · compliance · TTS clean) |
| Target publish | **giữa tháng 11/2026**, cách big-idea-091 (geranium) ≥2–3 tuần; mùa giâm cành hóa gỗ là tháng 11–2 (NC State) nên trễ đến hết tháng 12 vẫn trong cửa sổ |
| Compliance score (lúc GATE) | **9/10** (subagent độc lập, PASS); điểm trừ duy nhất (khối an toàn bột đứng sau phần làm) **đã vá** (chuyển lên trước + thêm "Keep the tin closed…") — chưa chấm lại |
| Lane / nguồn | A · `/san-y-tuong` 24/10 (phiếu: `research/phieu-kiem-dinh-rose-potato-2026-10-24.md`) · Topic Gate 3/3 nhưng **khung hoài nghi 0 video OM ≥2** → nhãn **THĂM DÒ** |
| Độ dài thực tế | **2.876 từ ≈ 17,4 phút @165wpm** (voice Key gardent chưa đo bản này) · config `video_length` 20–24′ / 3.300–4.000 từ → **dưới sàn có chủ đích** |

## 🧪 TEST (khai trước để retro biết phải trả lời gì)
1. **TEST độ dài (L7 vs config 20–24′):** video ~17,4′ khi config yêu cầu 20+. Dưới sàn vì brief mỏng ở M5–M6 và **không độn** (user chấp nhận 24/10). Câu hỏi retro: so với big-idea-091 (≈18,2′, cùng TEST), dải 12–20′ của kênh (median 632 view, AVD 29,3%) và 3 video 20–40′ (median 936 view): views_5d và **giờ xem/lượt** có cao hơn không? ⚠️ Không so AVD% giữa video khác độ dài; so **giờ xem tuyệt đối**. Hai video liên tiếp ~17–18′ cho thêm điểm dữ liệu "17–18′ vs 8–10′".
2. **TEST khung hoài nghi/có nguồn trên chủ đề mẹo (quan trọng nhất):** họ "mẹo" rễ hồng có cầu thật (THR 0,614, 7 kênh, 26 video thắng/42) nhưng **toàn khung tin mẹo**; khung hoài nghi có 0 video OM ≥2 trong 12 tháng. Tiêu đề này đưa **một sự kiện cụ thể ("One Small Study Found No Roots")** vào khung hoài nghi. Câu hỏi retro: khung này có CTR/giờ xem ngang họ mẹo không, hay thua? **Quy tắc dừng khai trước:** views_5d <400 **hoặc** CTR giờ 48 <4% → bỏ khung hoài nghi cho chủ đề mẹo (làm khung "cách làm có nguồn" thay).
3. **TEST "đọc bài báo gốc làm xương sống":** video dựa vào MỘT nghiên cứu nhỏ + bảng "cho biết / không cho biết" (Editorial Signature) thay vì nhiều nguồn đồng thuận. Câu hỏi retro: khán giả 35–60+ ở lại hay rời ở đoạn M2 (3:18–6:30, đoạn chi tiết thiết kế thí nghiệm)?
4. **TEST dẫn nguồn "nói thẳng, đừng cite" (L19):** lần thứ hai (sau 091). Cite chung chung ở mức 9/9 ngân sách (sát trần). Retro: điểm rơi retention có trùng chỗ cite (M4 CITE_ZONE 9:11–10:30) không? **Ý của user, chưa có số.**
5. **TEST thumbnail** `SKIP THE SPUD` / `TRY 2 BUDS` (A, Verdict) vs bản B (Stat+symptom `SOFT BASE?` / `6 IN · 2 BUDS`) — dùng Test & Compare nếu CTR giờ 48 <4% hoặc muốn xác định lever. Xem `thumbnail-prompts.md`.
6. **TEST khán giả 35–60+:** ngôn ngữ đã đổi (tiền/thời gian/công, bỏ nhãn tuổi). Đọc Studio → Demographics sau 7–14 ngày; cỡ mẫu nhỏ → không kết luận từ 1 video.

## Title bet
- **Title chốt:** `Rose Cuttings in a Potato? One Small Study Found No Roots` (vidIQ **88/100**, 24/10)
- Specific quantity? **Y** ("One Small Study", "No Roots") — nhưng **không có leading number**
- Leading number? **N**
- Độ dài: **11 từ / 57 ký tự** (dưới mục tiêu 65 ✅) · keyword "Rose Cuttings" ở ký tự 0 ✅
- Dự phòng đã chấm: `…One Study Found No Roots` (87). ❌ Loại: `…What the Only Study Found` (91, "the only study" tuyệt đối), `…What Universities Actually Say` (85, quá lời so nguồn).
- ⚠️ DELIVERY-LOCK: "One Small Study Found No Roots" đúng với toàn văn (nhóm khoai: không nảy chồi, không ra rễ ở TN2); **không** nâng thành "khoai tây vô dụng".

## Retention bets (theo mốc ước tính @165wpm của bản TTS clean)
- **Topic familiarity:** **Y** — hồng + mẹo khoai tây quen thuộc với người Mỹ (L1 ✅).
- **L6 (giây 12–20):** kết quả đo giao ngay hook ("grew no roots" / "most… in plain soil did"); không dùng claim ngược đời không chứng minh.
- **Giây 40–55 (L4):** Loop #1 ("a second result, and it's about the cutting itself", gieo ~0:17) còn sống; M1 mở bằng cơ chế + "explanation, not a result", ACTION_TIP ở ~2:00.
- **Phút 4–6 (L5):** Loop #1 + Loop #2 ("summary and its full text disagree", gieo ~3:16 → đóng ~6:13) cùng sống · scene viewer-POV (~4:28) · Mistake #1 (~4:42) · Jenga: **ON**.
- **Giữa video:** Loop #1 đóng ~7:00 ("Two buds.") · lời hứa cuối gieo ~7:19 ("a fair way to test it yourself") · re-hook M4 ("soft and dark at the bottom") ~9:11 · con số bất ngờ: nhãn bột có thiram vs nhãn "Greenhouses and Nurseries Only".
- **Phần sau:** M5 phép thử công bằng (6 cành, 3 vs 3) · bản đồ chứng cứ mẹo bếp · M6 "honest scoreboard" ~14:52 · Q (ASPCA) · KẾT callback ACTION_TIP.
- **Điểm yếu đã biết (audit độc lập, chưa vá hết):** (a) 3:18–4:20 đầu M2 là chi tiết thiết kế thí nghiệm (đã rút ~30%); (b) 4:50–6:14 chuỗi câu phủ định "không %, không test…" (đã chèn câu hỏi); (c) 9:40–10:30 CITE_ZONE nhiều tên nguồn (đã rút còn 3 cặp); (d) **11:00–14:00 không có cú twist mới** ngoài thiram; (e) **Loop #1 phải chờ ~7 phút** mới được trả.
- **Editorial Signature (L13):** bảng "nghiên cứu cho biết / không cho biết" (M2) · bảng các trang bất đồng (M4) · bản đồ chứng cứ mẹo bếp (M5).
- **Consensus Synthesis:** 2 (M3 "four to eight inches, a few buds, cut just below one" · M6 "weeks, sometimes months").
- **Hook:** A (Data/Statement, ~105 từ, 0 tên trường đọc bằng giọng).

## Engagement bets
- Themes: ☑ Pet/Kid safety (ASPCA Rosa không độc + "check the Latin name", bột kích rễ, vet/poison control) · ☑ Season/climate theo vùng (không có số zone — NEED DATA) · ☐ Nostalgia (không dùng)
- Câu kích: M5 *"Tell us in the comments: have you tried the potato, and what happened?"* · Q *"So put your answers in the comments."* (hiện là "We'd love your answers in the comments.")
- **Bình luận ghim:** câu hỏi "đã thử khoai tây chưa, kết quả?" + danh sách CHƯA ai trả lời (tỷ lệ ra rễ khoai ngoài một thử nghiệm; hóa gỗ vs bán hóa gỗ cùng điều kiện; mẹo bếp trên hồng; 2 mắt có thật hơn 1 mắt không) + chính sách sửa sai. **Không SĐT chống độc** (NEED DATA).

## Dự đoán số (so baseline kênh, health 23/10)
| Chỉ số | Baseline | DỰ ĐOÁN | Lý do |
|--------|----------|---------|-------|
| **views_5d** *(thước chấm chính)* | median **597** | **350–900** · PASS ≥597 · stretch ≥900 · **dừng khung <400** | THR họ mẹo 0,61 và P50 họ mẹo 1.085 là **trần của khung tin mẹo**, không phải khung này; hệ số khớp 0,7 (khung chưa đo) → P(thắng) 0,43. Trừ: khung hoài nghi 0 bằng chứng; Browse kênh đang -3,9 điểm; video ngắn hơn khung config. Cộng: cầu thật (4 video 290–810K trong họ mẹo hồng), đúng mùa, "rose cuttings" 3.312 tìm kiếm/tháng |
| **Giờ xem / lượt** *(thước chính thứ hai)* | ~195 giây watch-budget | **3,4–4,9 phút** | = AVD% × 17,4′ nếu AVD 20–28% |
| AVD % *(chẩn đoán phụ, KHÔNG phải verdict)* | 29,4% (tuần mới nhất) | **20–28%** | video 17′ dài hơn dải 12–20′ (29,3%); Loop #1 chờ 7′ và 11:00–14:00 không có twist là rủi ro |
| CTR % (giờ 48) | 5,5% (28 ngày, nhập tay) | **4,0–5,5%** | title 88 điểm + keyword ở ký tự 0; khung hoài nghi chưa đo; thumbnail A chưa A/B. **<4% → kích hoạt quy tắc dừng + Test & Compare** |
| Tổng giờ xem 5 ngày | — | = views_5d × giờ/lượt | đọc kèm views_5d |
> Cược lệch xuống (<400 views_5d) → xem lại TEST #2 (khung) trước khi kết luận về độ dài (#1) hay thumbnail (#5).

## Rủi ro đã biết
- **Khung hoài nghi chưa có video OM ≥2** (4 bản hoài nghi trong mẫu đều là kênh nhỏ/nước ngoài, 11–1,4K view) → đây là phép thử, không phải cược chắc.
- **Nguồn trung tâm yếu:** Wali 2019 (tạp chí mở, thiết kế mâu thuẫn: 8 khối × 9 ≠ 108 cành; Results vs Discussion mâu thuẫn ở TN1; không % và không kiểm định khoai–đất). Giọng video phải giữ "một nghiên cứu nhỏ"; nếu chuyên gia/viewer chỉ ra lỗi mới, ghim đính chính.
- **Hook gộp thí nghiệm 2** (hook không nói thí nghiệm 1 không cành nào ra rễ — M2 nói). Người xem chỉ nghe hook có thể hiểu "khoai thua đất" rõ hơn thực tế.
- **Thumbnail A** (`SKIP THE SPUD`) mạnh giọng hơn script ("thin evidence, test it yourself") → dễ bị coi là kết luận.
- **Ngày đăng:** trễ sau tháng 12 → mất cửa sổ hóa gỗ.
- **Giọng Key gardent chưa đo bản này;** cần nghe thử Khost, Clemson, thiram, ASPCA, semi-hardwood.
- Nhãn bột (2010/2006) có thể đã đổi công thức → video nói "a label we read", không khẳng định về sản phẩm hiện bán.
- Bật **"Altered or synthetic content"** khi upload (AI voice/hình AI) — nhắc từ audit.

## Mốc đọc retention (để quyết định ở retro)
Đọc các đường cong: (1) **giây 0–60** so với hook cliff TB kênh (-37% tới giây 25); (2) **3:18–6:30** (M2: chi tiết thí nghiệm + chuỗi phủ định — điểm rơi nghi nhất); (3) **7:00–7:30** ngay sau Loop #1 đóng (có rơi mạnh không?); (4) **11:00–14:00** (không có twist); (5) **16:00–17:30** (Q + KẾT). Nếu rơi ở (2) → rút thêm thông số thí nghiệm / dời bảng; nếu rơi ở (3) → Loop #1 trả quá muộn hoặc không đáng chờ; nếu rơi ở (4) → thêm re-hook ~12:30. Chạy `python tools/yt_analytics.py retro <videoId>` 7–14 ngày sau đăng.
