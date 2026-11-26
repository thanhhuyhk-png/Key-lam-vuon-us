# Phản biện vòng 1 — big-idea-097 · Stop Buying Fruit Bushes: Grow 6 for Free From Winter Cuttings

> Ngày: 17/11/2026 · Bản đưa phản biện: `script.draft-markers.v1-before-fix.md` (1.653 từ) · gate.py trước vòng: PASS (0 FAIL, 1 cảnh báo)
> **R1 Agy `--sandbox`:** chạy 15′ rồi DEADLINE_EXCEEDED, đầu ra rỗng (`agy-err.txt`) → **thay bằng sub-agent Opus thứ hai (ngữ cảnh mới, thư mục riêng) — ghi rõ: CÙNG HÃNG** (R1 và R2 đều Claude Opus).
> **R2 Opus #1** (`phan-bien-v1/opus/opus-phan-bien.md`): Hook **27/35** · Risk Score **7/10 (REVISE)** · 3 CHẶN · 20 NÊN SỬA · ĐẠT CÓ SỬA.
> **R1′ Opus #2** (`phan-bien-v1/agy/agy-phan-bien.txt`): Hook **28/35** · 3 CHẶN · 14 NÊN SỬA · ĐẠT CÓ SỬA. Hai bản độc lập hội tụ ở cả 3 lỗi CHẶN.

## Quyết định (D1…D30)

| # | Câu gốc | Quyết định | Căn cứ |
|---|---|---|---|
| D1 | M2 «top bud showing» vs «two or three buds above the soil» (CHẶN) | **NHẬN.** Bỏ câu Arizona + câu 6–12/12–16 in; chốt «Three buds is the target. A taller cutting can carry up to six.» + «just the top bud above the soil» (OSU, ghi ở Addendum C04+) | 2 người cùng bắt; C04/C06 bất đồng (ledger) |
| D2 | M5 «Most figs handle zones six B and up» (CHẶN) | **NHẬN.** «One fig variety, Celeste, is rated for zones six B to ten. Many figs aren't that tough.» [C24, C22] | C24 chỉ nói Celeste; D6 |
| D3 | M5 trình tự callus → chậu vs trữ tủ lạnh tới xuân (CHẶN) | **NHẬN.** Viết lại M5: ôn hoà → chậu ngay [C20]; lạnh → ngăn rau tủ lạnh tới đầu xuân, không đóng băng, rồi chậu [C25]. Bỏ «10–14 ngày callus» | 2 người cùng bắt |
| D4 | Hook «nothing to buy / no special equipment» | **GIỮ TẠM — trình user ở GATE** (hook đã duyệt; sửa bản A′). | luật «không tự thay hook đã duyệt» |
| D5 | Hook «Cut it in February, push it into the ground» | **GIỮ TẠM — trình user ở GATE** (A′). | như D4 |
| D6 | M1 «A sleeping plant isn't growing leaves…» | **NHẬN.** Xoá câu | cơ chế không có trong ledger, tự cãi M4 |
| D7 | M2 inch/bud + «Count the buds» (L18, chồng 4 cụm số) | **NHẬN** (gộp D1) | L18 |
| D8 | M2 «Many growers… a year in a nursery bed» | **NHẬN một phần.** «One grape guide suggests a full year…» + Addendum C04+ (quote OSU đã đọc) | C04 thiếu quote |
| D9 | M3 «Sticking them straight into the ground… less often» | **BÁC xoá, GIỮ + Addendum C08+** (UAF đã đọc: «direct sticking outdoors is less successful») | orchestrator đã đọc trang; hedge «less often» |
| D10 | M3 «one state… another… permit» (CR4) | **NHẬN.** «At least one state bans them statewide, and another needs a permit. Rules vary.» | C13/C14 chỉ NC/NH |
| D11 | M3/CITE_ZONE «Currants can go in late autumn…» lẫn lấy vs cắm | **NHẬN.** «The cutting dates…», «Grapes are cut in February… Currants, anytime from late autumn to late winter» | D1 ledger |
| D12 | «because plants wake up at different times» | **NHẬN.** Thay bằng «because two dates keep getting mixed up. When you cut. And when you plant.» | D1 Sổ bất đồng; mở Editorial Signature đúng chỗ |
| D13 | M4 «potting mix / warm» không có trong ledger | **BÁC xoá, GIỮ + Addendum C16+** (OSU đã đọc) | đã xác nhận |
| D14 | M5 «gallon pots / 4–6 weeks» thiếu ledger | **BÁC xoá, GIỮ + Addendum C26+** (Texas A&M pdftotext đã đối chiếu); nói «about a month» | đã xác nhận |
| D15 | M6 «Pears and plums same pattern» + «rootstocks only sometimes» | **NHẬN.** «Pears and plums are usually grafted, too. [C34]»; bỏ câu C35 | tự mâu thuẫn |
| D16 | Kết «four to six weeks» | **NHẬN.** «In about a month, an elderberry cutting… can have its first roots.» | C16 chỉ elderberry |
| D17 | M2 ASPCA thiếu bước khẩn cấp | **NHẬN.** «If your dog eats some, call your vet right away.» | brief YMYL |
| D18 | Khối an toàn thú cưng/trẻ em đứng sớm (Risk mục 3) | **NHẬN một phần.** Thêm signpost «One quick safety note first… we'll flag each one» ở M1 + câu thú cưng cho sung ở M5 («According to one university plant database…») | C24 |
| D19 | M5 «start both in pots» thiếu giữ chỗ không đóng băng | **NHẬN.** «…keep the pots where they won't freeze» | C20/C25/C27 |
| D20 | M4 elderberry «never eat the leaves» thiếu thân/quả xanh | **NHẬN.** «Cook ripe berries… Skip the unripe ones, the leaves and the stems.» | C41–C43 |
| D21 | M7 «Ask the person who grew it» | **NHẬN.** «Ask the nursery or your local extension office.» | brief YMYL |
| D22 | X2 «works for every plant on this list» / «All it needs is three buds» | **NHẬN phần M1** («the one rule all six share»). Phần hook → A′ | Risk mục 8 |
| D23 | Loop #1 không nhắc 4–5′ + «the apple is still coming» lộ đáp án sớm | **NHẬN.** «And that fruit tree from the start? It's still coming.» ở cuối M2 + nhắc lại ở M3 | cả 2 người |
| D24 | Loop #3 gieo 5s rồi đóng | **NHẬN.** Gieo sớm ở M1 («one small tag can make a cutting off-limits… We'll get to that») — **lệch Spine: Loop #3 mở ~1:40 thay vì ~8:55** (ghi tại GATE) | 2 người |
| D25 | L19 ×4–6 cite chung ở M2–M3 | **NHẬN.** Bỏ «One university source», «Another goes longer», «Some sources… Others say», «The length varies by source»; còn 3 (ngân sách 5) | script_lint |
| D26 | ACTION_TIP chạy trước bước kiểm nhãn PP | **NHẬN.** Thêm «And while you're there, check each tag for the letters P P.» | R1′ |
| D27 | M4 hormone nói hai lần | **NHẬN.** Gộp «optional here, and too much can hurt [C16, C18]» | R2 |
| D28 | «Most of us haul it to the curb» / «than many of us get» («us» = người kể là người làm vườn) | **NHẬN.** Thay bằng «Picture a bare vine in a January yard»; «a lot of gardeners» | X5 nhẹ; cũng trùng góc đối thủ (R2 mục 5⑦) |
| D29 | «It takes ten minutes» không nguồn | **NHẬN.** «It's a quick walk.» | Risk mục 5 |
| D30 | Hook R2 viết lại <28 (27/35) | **KHÔNG tự thay.** Hook A giữ nguyên; trình **phương án A′** (2 sửa nhỏ) và **bản viết lại của R2 (mục 5)** để user chọn ở GATE | luật skill |
| — | «almost everyone reaches for first» (nói quá) | **NHẬN.** «a lot of gardeners try first» | R1′ |
| — | Cảnh báo người dựng (Ficus carica không benjamina · Sambucus thật · PP nhãn giả · chó/nho…) | **NHẬN** — chuyển nguyên vào ghi chú sản xuất | R1/R2 mục 6 |

**Tổng:** nhận 26 · nhận một phần 3 · bác 3 (D9, D13, D14 — đã có quote đọc trực tiếp, bổ sung vào ledger Addendum) · hoãn 2 (D4/D5/D22 hook → GATE).
**Sau sửa:** `gate.py --nhan sau-phan-bien-v1`: 1.650 từ ≈ 10:00, 0 FAIL; compliance regex SOFT-FAIL do câu «toxic to cats… According to one university plant database» (cố ý, có nguồn).
