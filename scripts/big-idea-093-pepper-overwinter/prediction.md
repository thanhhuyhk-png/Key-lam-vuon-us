# Prediction — big-idea-093-pepper-overwinter

> Ghi tại GATE Script (27/10/2026, user duyệt script). Baseline: `references/channel-health-latest.json` (23/10) + phiếu `research/phieu-kiem-dinh-pepper-overwinter-2026-10-26.md` + `research/du-bao.csv` (dòng 26/10). Khoảng dưới đây là **ước lượng dựa trên số đã ghi, không phải mô hình**; số thật ngoài khoảng → ghi nguyên nhân vào `retro.md`.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-093-pepper-overwinter |
| Ngày scripted | 2026-10-27 (Pha D PASS · self-audit · Triple F đã tiết chế · compliance 8/10 → 10/10 vòng 2 · TTS clean) |
| Target publish | **trước ~10/11/2026**, cách big-idea-091 (geranium) ≥1 tuần. Câu tease geranium ở KẾT chỉ giữ nếu 091 đã đăng trước |
| Compliance score (lúc GATE) | **10/10** (subagent độc lập, vòng 2) |
| Lane / nguồn | A · `/san-y-tuong` 26/10 · Topic Gate **3/3 ƯU TIÊN** · nhãn **KHAI THÁC** (phần 2 của "7 Secrets to Growing Infinite Bell Peppers" 343K) |
| Độ dài thực tế | **2.941 từ ≈ 17,8′ @165 wpm** · config 20–24′ → dưới sàn có chủ đích (user chấp nhận 27/10, không độn) |

## 🧪 TEST (khai trước)
1. **TEST độ dài (thứ ba liên tiếp ~17–18′):** sau 091 (~18,2′) và 092 (~17,4′). Câu hỏi retro: views_5d và **giờ xem/lượt** so với dải 12–20′ (median 632 view) và 3 video 20–40′ (median 936). ⚠️ So giờ xem tuyệt đối, không so AVD% giữa video khác độ dài. Đủ 3 video → chạy so sánh trong `channel.config.json` → `video_length._why`.
2. **TEST franchise phần tiếp (đòn bẩy W41):** video nối hit 343K của chính kênh, cùng cây. Câu hỏi retro: traffic **Suggested** có cao hơn trung bình kênh (15,3%) không, và có lượt xem đến từ video "Infinite Bell Peppers" không (Studio → Reach → nguồn "Suggested videos"). Hành động kèm: end screen + bình luận ghim trên video 343K trỏ sang video này.
3. **TEST keyword-first nhẹ:** cụm "Pepper Plants" ở ký tự 11; cụm tìm kiếm "how to make your pepper plants last for years" 3.093/th (dạng cụm giống tiêu đề video — tín hiệu yếu). Câu hỏi retro: Search share của video (kênh: ~2,0% với title có cụm chủ thể).
4. **TEST câu mở dạng Contrarian có bằng chứng 0:03** (hook A): rơi ở giây 20–33 (vùng chết L6) có nhỏ hơn hook cliff TB kênh (-37% tới giây 25) không.
5. **TEST thumbnail** A `KEEP 3 STEMS` vs B `FROST TONIGHT?` (Test & Compare). Xem `thumbnail-prompts.md`.

## Title bet
- **Title chốt:** `Don't Pull Your Pepper Plants Yet. They Can Live for Years` (vidIQ **97/100**, 26/10) — Contrarian
- Specific quantity? **Y (yếu)** — "Years" · không có leading number
- Leading number? **N**
- Độ dài: **11 từ / 58 ký tự** ✅ · keyword "Pepper Plants" ký tự 11 ✅
- Dự phòng: `How to Make Your Pepper Plants Last for Years (Before Frost)` (bản 66 ký tự chấm 96; bản 60 ký tự chưa chấm) — swap nếu CTR giờ 48 <3,5% hoặc Search share <1%
- DELIVERY-LOCK: "Live for Years" ← C01 (NC State "short-lived perennial") + C02/C03 (UF/IFAS "tender perennial", zone 9B–11B). Script nói rõ "won't make a pepper plant live forever… one winter at a time".

## Retention bets (mốc @165 wpm, bản TTS clean)
- **Topic familiarity:** **Y** — ớt là cây phổ biến; kênh có hit 343K cùng cây (L1 ✅).
- **L6:** "A pepper is a perennial" ở 0:03; bằng chứng nằm trong 3 câu đầu.
- **Giây 40–55 (L4/L15):** Loop #1 ("one step happens before the plant ever comes through your door", ~0:29) còn sống; M1 mở bằng giá trị "two ways" ở 0:50; không preview/giới thiệu.
- **Phút 4–6 (L5):** Loop #1 + Loop #2 ("coldest spot… better than your sunniest window", 3:12 → trả 6:13) cùng mở · câu hỏi tự kiểm "spot at fifty to sixty degrees" (~4:15) · bảng chọn cách (~5:00) · Jenga **ON**.
- **Giữa video:** CITE_ZONE bảng hai cách cắt (~7:40) · mistake #1 · re-hook M4 "one bright window" (~9:16).
- **Phần sau:** trả Loop #1 ~11:31 (rửa sạch đất ở rễ, chậu sạch, đất mới) · khối an toàn pet/kid + ASPCA · mistake #2 (xà phòng rửa chén) · lời hứa cuối ~14:01 → trả ~14:28 (sau sương giá cuối) · claim-scoping "not forever" · KẾT callback ACTION_TIP.
- **Điểm yếu đã biết:** (a) Loop #1 chờ ~11 phút mới trả (dài nhất 3 video gần đây); (b) M4 chỉ 371 từ, ít số; (c) M6 thiếu ngày đánh thức cụ thể (nói thẳng là không có); (d) 0 câu hoài niệm đa thế hệ.
- **Editorial Signature (L13):** bảng chọn cách theo chỗ trong nhà (M2) · bảng hai trang, hai cách cắt (M3).
- **Consensus Synthesis:** 2 (M2 "cut it back, keep it cool, water it rarely" · M3 "cut it back hard").

## Engagement bets
- Themes: ☑ Pet/Kid safety (vet, ASPCA (888) 426-4435 — đã xác minh 27/10, "A consultation fee may apply"; nhãn thuốc) · ☑ USDA zone (zone 9–11 + ngày sương giá cuối theo vùng) · ☐ Nostalgia (không có chuyện thật)
- Câu kích: M5 *"Have you ever brought a plant inside and found bugs on it a month later?"* · KẾT *"tell us your zone and the pepper you're keeping."*
- **Bình luận ghim:** câu hỏi zone + giống ớt; nêu thẳng 2 điều nguồn không có (số giờ đèn, ngày đánh thức) → mời người xem kể kinh nghiệm thật (Story Bank cho video sau).

## Dự đoán số (baseline health 23/10)
| Chỉ số | Baseline | DỰ ĐOÁN | Lý do |
|--------|----------|---------|-------|
| **views_5d** *(thước chấm chính)* | median **597** · ngưỡng thắng **896** | **600–1.200** · P25 762 · P50 919 · P75 1.122 · **P(thắng) 0,56** | `chi_so.py` mẫu 7 video (độ tin THẤP). Cộng: franchise 343K cùng cây, video mồi Hippie Chick 111 VPH (kênh 2,5K sub) + video 343K của mình 47 VPH, gói 97 điểm, đúng mùa. Trừ: keyword <750, 4 kênh/90 ngày làm cùng chủ đề, Browse kênh −3,9 điểm |
| **Giờ xem / lượt** *(thước chính thứ hai)* | ~195 giây watch-budget | **3,6–5,0 phút** | = AVD% × 17,8′ nếu AVD 20–28% |
| AVD % *(chẩn đoán phụ, không phải verdict)* | 29,4% (tuần mới nhất) | **20–28%** | dài hơn dải 12–20′; Loop #1 chờ 11′ |
| CTR % (giờ 48) | 5,5% (28 ngày, nhập tay) | **4,5–6,5%** | title 97 + cùng cây với hit; **<4% → Test & Compare thumbnail B + cân nhắc swap title C** |
| Suggested share | 15,3% | **≥20%** | TEST #2 franchise |
| Tổng giờ xem 5 ngày | — | = views_5d × giờ/lượt | đọc kèm views_5d |

**Quy tắc dừng (ghi ở `du-bao.csv`):** views_5d **<500** hoặc CTR giờ 48 **<4%** → không làm thêm video "giữ cây qua đông" trong mùa này; xem lại TEST #2 (franchise) trước khi kết luận về độ dài (#1).

## Rủi ro đã biết
- **Thời điểm:** nhiều vùng đã có sương giá đầu → đăng muộn sau ~10/11 thì nửa khán giả đã nhổ cây. Lời hứa "Yet" mất lực theo từng tuần.
- **C14–C16 (giữ cây xanh)** từ một chuyên gia Ask Extension không ghi tên/bang (2023) → script nói như "the guidance we found".
- **Nguồn chính của phần cho cây ngủ** là 2 câu trả lời Ask Extension (Colorado MG 2022, HGIC UMD 2020) — hạng T1 nhưng không phải fact sheet.
- **Câu tease geranium** ở KẾT phụ thuộc thứ tự đăng.
- **Giọng Key gardent chưa đo bản này;** cần nghe thử: "A S P C A", số hotline, "zones nine through eleven", "hardening off", "insecticidal".
- Bật **"Altered or synthetic content"** khi upload (AI voice/hình AI).

## Mốc đọc retention (retro)
(1) **giây 0–60** vs hook cliff TB kênh · (2) **3:12–6:13** (2 loop mở; bảng ~5:00) · (3) **6:13–7:40** ngay sau Loop #2 đóng + CITE_ZONE · (4) **9:16–11:31** (M4 mỏng, chờ Loop #1) · (5) **14:00–17:50** (lời hứa cuối + KẾT). Rơi ở (4) → video sau trả Loop #1 sớm hơn hoặc thêm mini-loop giữa M4. Chạy `python tools/yt_analytics.py retro <videoId>` 7–14 ngày sau đăng.
