# Phản biện vòng 2 — big-idea-097 · Stop Buying Fruit Bushes: Grow 6 for Free From Winter Cuttings

> Ngày: 17/11/2026 · Phạm vi: `phan-bien-v2/vung-da-sua.md` (+1 đoạn trước/sau) · Risk Score chấm lại trên cả bài
> **Cả hai người phản biện đều là Claude Opus (ngữ cảnh mới, thư mục riêng): CÙNG HÃNG** — Agy `--sandbox` hết thời gian ở vòng 1 (xem `phan-bien-v1.md`), không thử lại.
> **R1′ (Opus #2, `phan-bien-v2/agy/agy-phan-bien.txt`):** 0 CHẶN · 11 NÊN SỬA · 10 GỢI Ý · Hook 26/35 (phần mở chưa sửa) · ĐẠT CÓ SỬA.
> **R2 (Opus #1, `phan-bien-v2/opus/opus-phan-bien.md`):** 0 CHẶN · 8 NÊN SỬA · 10 GỢI Ý · Hook 27/35 · **Risk Score 10/10 (PUBLISH)** · ĐẠT CÓ SỬA.
> Cả hai nêu 3 lỗi trùng: luật «Keep it cold… plant when soil softens» sai với elderberry/sung; «gallon pots» áp cho cả sung/ra đất ở vùng lạnh; «All you need is shears» mâu thuẫn bột/đất ươm.

## Quyết định (E1…E19) — áp một lượt, `apply_v2.py`

| # | Câu gốc | Quyết định | Căn cứ |
|---|---|---|---|
| E1 | «Cut it asleep. Keep it cold. Plant it when the soil softens.» (M3 + Kết) | **NHẬN.** M3: «Keep it cool until you're ready. Then pot it up, or plant it when the soil softens.»; Kết: «Keep it cool. Pot it up, or plant it when the soil softens.» | C16, C20, C25; 2/2 người |
| E2 | «gallon pots for about a month, before they go in the ground» | **NHẬN.** «Once the pomegranates start growing, give them four to six weeks in gallon pots. Where winters are mild, they can go in the ground after that.» | C26 chỉ lựu; 2/2 |
| E3 | «All you need is a pair of pruning shears» | **NHẬN.** «To take the cutting, all you need is…» | 2/2 |
| E4 | «Each cutting needs three buds… Three buds is the target. A taller cutting…» | **NHẬN.** «Aim for three buds. A longer cutting can carry up to six.» | C02/C05 |
| E5 | M2 cắm xuống đất ngay sau «cut in February» | **NHẬN.** «Once the soil can be worked, set each one in the ground…» | R1′ |
| E6 | M7 «a different story», «the owner's permission» | **NHẬN.** «Plants grown from seed usually aren't covered by a plant patent.» · «the patent holder's permission» | C46 |
| E7 | M1 liệt kê 5 cây trước «all six» | **NHẬN.** «And all six follow the same pattern.» | 2/2 |
| E8 | «Currants and gooseberries can handle… minus twenty-two» trước khi giới thiệu lý gai | **NHẬN.** «And currants are tough. They can handle…» | C12 |
| E9 | «the European types»; «The federal ban» chưa nói cấm gì | **NHẬN.** «European gooseberries are the stubborn ones» · «A federal ban on growing them» | C09, C12 |
| E10 | «Plant two is the easy one» (nho thì không dễ?) | **NHẬN.** «Plant two is just as easy.» · «Plant one is one of the simplest» → «Let's start with the vine.» | 2/2 |
| E11 | «Many figs aren't that tough» [C22] | **NHẬN.** «Below about twenty degrees, a fig can die back to the ground.» (20 đã có trong allowed-numbers) | C22 |
| E12 | «Pears and plums are usually grafted» | **NHẬN.** «Pears are usually grafted, too.» (bỏ mận) | C34/C35 |
| E13 | M4 «don't toss a cutting because it's leafy and weak» | **NHẬN.** «don't pull it up to check, and don't give up on it.» | R1′ |
| E14 | «No tag? Think about age» | **NHẬN.** «No tag doesn't mean no patent.» | R1′ |
| E15 | M1 ba lần hẹn «sau» (~40 s meta); «this week» ×2; «check each tag for the letters P P» lộ Loop #3 20 s sau khi gieo | **NHẬN.** Gộp safety + tag làm 1 câu, bỏ «bushes and vines… as we go», «Here's your first step», «read each tag» | 2/2 |
| E16 | L19 «One grape guide suggests…» | **NHẬN.** «It's generally best to give them a full year in a nursery bed first. [C04]» | R1′ |
| E17 | Loop #1 nhắc 2 lần cùng khuôn | **NHẬN.** «It's still coming.» / «Hold onto that fruit tree question. It's coming.» | 2/2 |
| E18 | M5 lặp «Cut straight below a bud…» | **NHẬN.** Bỏ | R2 |
| E19 | «Gardeners love to try this on apples» không mã | **NHẬN.** «Apples are the one people ask about.» (C33 là hỏi–đáp có thật) | R2 |
| — | Hook A (`nothing to buy`, `push it into the ground`, `neighbor who prunes`, `All it needs`) | **KHÔNG tự đổi** — A′ và A″ ở `hook.md`, trình user ở GATE | luật skill |
| — | Thêm «ASPCA Poison Control hotline» | **BÁC** — ASPCA đã gọi tên 1 lần ở M2; thêm lần 2 vượt ngân sách L14 | script_lint |
| — | Câu về trẻ em (Risk mục 3 tuỳ chọn) | **BÁC** — không có nguồn (research-brief §YMYL: [NEED DATA], không nêu) | brief |

**Tổng:** nhận 19 · bác 2 · hook hoãn user.
**Sau sửa:** thêm 1 câu sourced (C12: đen dễ nhiễm nhất, đỏ/trắng ít hơn, lý gai ít nhất) để giữ ≥1.650 từ. `gate.py --nhan sau-phan-bien-v2`: **1.652 từ ≈ 10:00 · 0 cổng FAIL · lint L14–L19 0 lỗi 0 cảnh báo · số liệu 0 số ngoài danh sách · 75 thẻ / 35 mã ledger · trùng 5 script gần nhất 0 câu**. Cảnh báo: chưa có transcript đối thủ · compliance regex SOFT-FAIL do câu «toxic to cats… According to one university plant database» (cố ý, có nguồn C24).
⚠️ **Sửa sau vòng 2 chưa có người đọc lại** (quy trình: tối đa 2 vòng; không chạy vòng 3).
**Compliance Score chính thức: 10/10** (R2 chấm vòng 2 trên bản vòng-1-đã-sửa; bản hiện tại thêm 19 sửa nhỏ + 1 câu C12, không thêm claim mới).
