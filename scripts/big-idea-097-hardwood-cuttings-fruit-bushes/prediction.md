# Prediction — big-idea-097-hardwood-cuttings-fruit-bushes

> Ghi tại GATE Script (18/11/2026). 7–14 ngày sau khi đăng, so với số thật trong `retro.md`.
> **Chấm chính:** views_5d so với trung vị 597 (`channel.config.json` → `scoring`) + giây xem/lượt + CTR Studio. ⛔ Không chấm bằng AVD% đơn lẻ.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-097-hardwood-cuttings-fruit-bushes |
| **Hạng** | **AN TOÀN** (Topic Gate 2/3 · GO-TEST · không phải cú đánh lớn) · **TEST** (xem dưới) |
| Ngày scripted | 2026-11-18 (user duyệt script + giữ hook A) |
| Target publish | **12–16/01/2027.** Ràng buộc: **sau 094 (11/11) ≥ 8 tuần ⇒ ≥ 06/01/2027** (giâm cành nội bộ đã có 053 · 091 · 092 · 094) · cách 096 và video M (seed mix, ~28/12–05/01) ≥ 5 ngày. Mùa: cây ngủ đông, lấy cành tháng 1–3 — đăng giữa T1 vừa kịp mùa nho (tháng 2) |
| Compliance score (lúc GATE) | **10/10** (R2 Opus, vòng 2; vòng 1: 7/10 → sửa 3 mục: khối an toàn thú cưng, số liệu, hedging). Agy `--sandbox` hết thời gian ở vòng 1 → 2 người phản biện cùng hãng (Opus). gate.py: 0 cổng FAIL, 2 cảnh báo (chưa có transcript đối thủ · compliance regex SOFT-FAIL do câu «toxic to cats… university plant database», cố ý) |
| Độ dài | 1.652 từ ≈ 10,0′ @165 wpm (sát sàn khung 10–14′, không độn; ngắn hơn spine 1.771) |

## Title bet
- **Title chốt:** `Stop Buying Fruit Bushes: Grow 6 for Free From Winter Cuttings` (user chọn Title A 17/11; vidIQ 86)
- Specific quantity? **Y** («6», «Winter», «Free»)
- Leading number? **N**. «Stop Buying Fruit Bushes» đứng đầu (khung L20 «Stop… / Free» của hit `9qcpNPXL4f8` 184K); số «6» ở giữa.
- Độ dài: **11 từ / 62 ký tự**
- Thumbnail test: `FROM A STICK` (cành nho trơ cắm đất vs nhãn giá gạch; bổ trợ title bằng cơ chế gây tò mò, 0 từ trùng) — chi tiết ở `thumbnail-prompts.md`.

## Retention bets (3 luật cứng)
- **Topic familiarity:** **Y**. Nho, lý chua, elderberry, sung quen với người Mỹ; **lý gai (gooseberry) và lựu (pomegranate) ít quen hơn** (L1 nhẹ) → script gắn mỗi cây vào danh sách có signposting «Plant N» và cảnh báo vùng khí hậu cho sung/lựu.
- **Giây 40–55:** Loop #1 «cây ăn quả nào hay thử mà hiếm khi thành?» (táo; gieo ~0:28) → nhắc ~3:00, ~5:00, ~7:30 → đóng ~7:45. Đi qua vùng 40–55 s bằng quy tắc M1 (payoff mảnh lớn <1:00) + loop táo + Loop #3 «một cái nhãn có thể làm cành cắt không được phép» gieo sớm ở M1 (~1:45).
- **Phút 4–6:** Loop #1 (sống) + **Loop #2** («một cây ra lá trước khi có rễ», mở ~5:00 → đóng ~5:35) + Loop #3 (nhắc); **Editorial Signature = Cutting Calendar** (lúc CẮT ≠ lúc CẮM; ~4:15–5:00) + cảnh báo luật bang Ribes (~4:20). Jenga Retention: **ON** (3 loop).

## Engagement bets
- Themes: ☐ Nostalgia (không dùng — Story Bank trống) · ☑ Pet safety (nho/nho khô — chó (ASPCA); sung — mèo, chó, ngựa; elderberry — người) · ☑ USDA zone/climate (sung 6B–10 chỉ giống Celeste; lựu 8–10; luật bang lý chua/lý gai)
- Câu kích theme: «The ASPCA says grapes and raisins can cause kidney damage in dogs…» · «So which plant on your list will you try first? Tell me in the comments.»

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views_5d | trung vị 597 · an toàn ≥896 · bứt ≥2.982 | **P25 ~350 · P50 ~650 · P75 ~1.300** (bản đã giảm; ước tay, **chưa qua `chi_so.py`** — chưa lấy mẫu THR). **P(≥896) ≈ 0,30 · P(≥2.982) ≈ 0,05** |
| AVD % | 25,6% (video 7–9′: 27–35%; ≥16′: 12–15%) | **~28%** (10′, 3 loop, listicle có luận điểm) — phán đoán, không có mô hình |
| CTR % (giờ 48) | 28d 5,5% · video mới 10/10–07/11 1,3–1,6% | **≥2,5%** (không có keyword mạnh: «hardwood cuttings» <750; sống nhờ khuôn «Stop… free» + thumbnail) |
| Giây xem/lượt | watch-budget kênh ~195 s | **≥185 s** |

> P25/P50/P75 dựa trên: (1) neo **franchise cuttings** `9qcpNPXL4f8` 184K (5d 55.888) — nhưng 3 follow-up chỉ 377 · 649 · 316 → hit đến từ gói tiêu đề, không phải chủ đề; (2) outlier ngách: EcoplanturUSA 291K, Sophie Valentine 59K, Anya Lautenbach 24K; (3) không có mẫu THR; (4) sổ dự báo thổi phồng (P50 1.110/1.085/919 → thực 649/316/290) nên giảm.

## TEST (ghi rõ để retro trả lời)
1. **TEST BÁM MODEL LINK (Frugal Solutions) — bám KHUNG, không bám đề tài:** khuôn «Stop Buying X: N … for Free» + stock + thẻ chữ. Frugal «STOP Buying Fruit Trees» chỉ 2.474 view → kết quả không kết luận được cho Model Link, chỉ cho khung. Video bám thứ 3 (sau 095, 096). **Mốc thôi bám: 3 video bám mà không video nào ≥896**; đo lại Top 20 ngày 16/12/2026.
2. **TEST KHUNG «Stop … for Free» (L20 đảo niềm tin):** CTR giờ 48 có ≥ video «No … Needed» (096) không? Đếm khung đảo niềm tin trong 4 video gần nhất khi lên lịch (L20: ≤1/4).
3. **TEST FRANCHISE GIÂM CÀNH:** đổi 3 trục (bụi/dây ăn quả · cây ngủ đông · cây KHÔNG ra rễ) — views_5d có vượt 053/091/092/094 (316–649) không? Nếu không ⇒ franchise cũ đến từ gói «Stop Rooting in Water», không phải từ «giâm cành».
4. **TEST LOOP #3 GIEO SỚM (lệch spine):** nhãn bằng sáng chế gieo ở ~1:45 thay vì ~8:55 — đường cong có giữ qua ~2:00–8:00 không? Tín hiệu: cú rơi giây 40–55 và phút 2–3.
5. **TEST HOOK A (giữ nguyên bản đã duyệt, không dùng A′):** phản biện chỉ ra «push it into the ground» tháng 2, «nothing to buy», «a neighbor who prunes» (A′ đã sửa). Ghi lại comment/phản ứng: người xem có nêu «cần mua bột/đất ươm»/«đất đóng băng» không? (để quyết định có sửa hook ở video sau).
6. **TEST ĐỘ DÀI ~10′ (sàn khung 10–14′):** giây xem/lượt và tổng giờ xem so với video 8–9′ (125–178 s).

## Quy tắc dừng
- views_5d < 400 **hoặc** CTR giờ 48 < 2% → gói hỏng: đổi thumbnail trước (biến thể `NOT APPLES` nếu chưa dùng; hoặc cảnh nho khác), rồi mới đổi title; kiểm lại bằng `FROM A STICK`.
- views_5d ≥ 896 → đạt mức an toàn; làm tiếp «cây KHÔNG ra rễ: ghép táo/lê» hoặc phần 2 (nhân cành mùa xuân/mềm) nếu comment hỏi.
- views_5d ≥ 2.982 → làm phần tiếp ngay, giữ nguyên khung gói «Stop Buying … for Free».
