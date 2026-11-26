# Prediction — big-idea-096-winter-no-greenhouse

> Ghi tại GATE Script (17/11/2026). 7–14 ngày sau khi đăng, so với số thật trong `retro.md`.
> **Chấm chính:** views_5d so với trung vị 597 (`channel.config.json` → `scoring`) + giây xem/lượt + CTR Studio. ⛔ Không chấm bằng AVD% đơn lẻ.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-096-winter-no-greenhouse |
| **Hạng** | **AN TOÀN** (Topic Gate 2/3 · không phải cú đánh lớn) · **TEST** (xem dưới) |
| Ngày scripted | 2026-11-17 |
| Target publish | **30/11 → ~07/12/2026.** Ràng buộc: **cách 095 ≥ 5 ngày** (095 dự kiến đăng trước ~25/11; nếu 095 trượt thì lùi 096 theo đó) và **cách video winter sowing ≥ 3 tuần** (winter sowing dự kiến ~cuối T12 → 096 phải đăng trước ~07/12). Đề tài theo mùa: đăng càng sớm trong đầu đông càng đúng «cây còn trong vườn»; sau giữa T12 giá trị «làm ngay» giảm |
| Compliance score (lúc GATE) | **10/10** (R2 Opus, vòng 2; vòng 1: 9/10 → sửa mục 8 hedging). Agy tự chấm thang rủi ro riêng 1/10 (thấp). gate.py: 0 cổng FAIL, 2 cảnh báo (chưa có transcript đối thủ · compliance regex SOFT-FAIL do câu ASPCA tỏi tây, cố ý) |
| Độ dài | 1.655 từ ≈ 10,0′ @165 wpm (khung config 10–14′; sát sàn, không độn) |

## Title bet
- **Title chốt:** `No Greenhouse Needed: 5 Ways to Grow Food All Winter` (user chọn Title A 16/11; **chưa chấm vidIQ** — điểm 96/91 trong phiếu săn ý là của title cũ «Don't Buy…», đã bỏ vì L20 điều kiện ②)
- Specific quantity? **Y** («5 Ways», «All Winter»)
- Leading number? **N**. «No Greenhouse Needed» đứng đầu (KEYWORD-FIRST: «greenhouse» + «winter»); số «5» ở đuôi — đúng khuôn Frugal, bù bằng cụm phủ định đầu title.
- Độ dài: **10 từ / 52 ký tự**
- Thumbnail test: `STILL GREEN` (cửa sổ cũ trên tuyết, rau xanh bên dưới; bổ trợ title bằng kết quả nhìn thấy, 0 từ trùng) — chi tiết ở `thumbnail-prompts.md`.

## Retention bets (3 luật cứng)
- **Topic familiarity:** **Y**. Kale, rau bó xôi, xà lách, cà rốt, tỏi tây; «greenhouse/winter garden» quen với người Mỹ. (Mache/corn salad là cây ít quen hơn → script gắn «also called corn salad» ở thân bài; hook giữ «mache» theo bản đã duyệt — **rủi ro L1 nhẹ**.)
- **Giây 40–55:** Loop #1 «why is two degrees enough?» (mở ~0:38–0:41) → nhắc ~2:17 («what closes a gap like that?») và ~3:57 → đóng ~4:06–4:47 (cây chịu lạnh gánh phần lớn cái lạnh, cover chỉ bù vài độ cuối).
- **Phút 4–6:** Loop #1 đang đóng + **Loop #2** («one sunny hour into a disaster», mở ~3:48 → nhắc 4:47 → đóng ~5:26–5:53) + **Loop #3** («the one thing none of them can do», mở ~6:02 → nhắc ~7:08, ~8:10 → đóng ~8:14 Persephone); Editorial Signature = Cover Ladder + phép tính khoảng hở (~4:06); nhịp căng mỗi 40–60 s (ladder · cold frame · chì sơn cửa sổ · 130°F · 85°F). Jenga Retention: **ON**.

## Engagement bets
- Themes: ☐ Nostalgia (không dùng — không có Story Bank) · ☑ Pet safety (ASPCA tỏi tây độc với chó/mèo; cảnh báo sơn chì cửa sổ cũ) · ☑ USDA zone/climate (số lấy từ mùa đông ôn hoà phía tây Cascades; mache «zone six or higher»; ngày Persephone ~Chicago)
- Câu kích theme: «One note for pet owners. Leeks are in the onion family, and the ASPCA lists them as toxic to dogs and cats, so keep pets out of that bed.» · «Which crop will you try first? Tell me in the comments.»

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views_5d | trung vị 597 · an toàn ≥896 · bứt ≥2.982 | **P25 ~400 · P50 ~600 · P75 ~950** (bản đã giảm; máy tính ra 782/1.164/1.522 — bỏ vì 3 dự báo gần nhất đều cao hơn thực: P50 1.110/1.085/919 → thực 649/316/290). **P(≥896) ≈ 0,30 · P(≥2.982) ≈ 0,03** |
| AVD % | 25,6% (video 7–9′: 27–35%; ≥16′: 12–15%) | **~28%** (10′, 3 loop, listicle nhẹ có luận điểm) — phán đoán, không có mô hình |
| CTR % (giờ 48) | 28d 5,5% · video mới 10/10–07/11 1,3–1,6% | **≥2,5%** (keyword theo mùa «greenhouse/winter»; thumbnail số + cảnh; **chưa đo keyword sau khi đổi title**) |
| Giây xem/lượt | watch-budget kênh ~195 s | **≥185 s** |

> P25/P50/P75 là phán đoán dựa trên: (1) neo Frugal Solutions — video nhà kính 122.978 view (57× trung vị Frugal) chứng minh đề tài, không chứng minh khuôn trên kênh mình; (2) mẫu C1 chỉ 9 video dùng được (THR 0,64 làm mượt, độ tin thấp); (3) đề tài ngoài khung vàng W41 (nhân giống 1 cây) — nên giữ thận trọng, như 095.

## TEST (ghi rõ để retro trả lời)
1. **TEST BÁM MODEL LINK (Frugal Solutions):** đề tài mùa đông/tự cung tự cấp + khuôn «N cách / không cần X» + stock + thẻ chữ — views_5d có vượt trung vị không? 096 là video bám thứ 2 (sau 095). **Mốc thôi bám: 3 video bám mà không video nào ≥896** (theo `research/top20-2026-11-15/`; đo lại 16/12/2026).
2. **TEST KHUÔN «No … Needed» (khung đảo niềm tin nhẹ, L20):** title/thumbnail không có «Don't»/chữ sợ; CTR giờ 48 có ≥ video kiểu «Never Buy X Again» không? Đếm khung đảo niềm tin trong 4 video gần nhất khi lên lịch (L20: ≤1/4).
3. **TEST «PHÉP TÍNH» (Cover Ladder + «simple arithmetic»):** đường cong giữ chân có giữ qua ~4:06–5:53 (ladder + cold frame) và qua giây 38–60 không? Tín hiệu: cú rơi lớn nhất ở giây nào.
4. **TEST ĐỘ DÀI ~10′ (sàn của khung 10–14′):** giây xem/lượt và tổng giờ xem có ≥ video 8–9′ (125–178 s) không?
5. **TEST THÔNG ĐIỆP TRUNG THỰC «cold storage» (PROMISE_OK):** câu «These plants aren't growing during the darkest weeks» có làm comment/CTR khác không (comment có nhắc «growth»/«title lie»)?

## Quy tắc dừng
- views_5d < 400 **hoặc** CTR giờ 48 < 2% → gói hỏng: đổi thumbnail trước (biến thể 1 con số nhiệt độ hoặc cảnh khác), rồi mới đổi title; kiểm lại keyword trước khi đổi.
- views_5d ≥ 896 → đạt mức an toàn; làm tiếp «những cây nào đã sống qua tuần X» hoặc phần 2 (phủ rơm/cold frame chuyên sâu) nếu comment hỏi.
- views_5d ≥ 2.982 → làm phần tiếp ngay, giữ nguyên khung gói «No … Needed».
