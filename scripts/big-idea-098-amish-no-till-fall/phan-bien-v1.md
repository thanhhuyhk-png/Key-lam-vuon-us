# Phản biện vòng 1 — big-idea-098 (18/11/2026)

**Người phản biện:** R1 = Agy `--sandbox` → **thất bại 2 lần** (lần 1: 503 hết công suất · lần 2: DEADLINE_EXCEEDED 15′, đầu ra rỗng) → thay bằng **Opus #2** ngữ cảnh mới (`phan-bien-v1/opus2/`). ⚠️ **Cùng hãng** — vòng này không có người phản biện khác hãng. R2 = Opus #1 (`phan-bien-v1/opus/`) + Risk Score.

| | Opus #1 (R2) | Opus #2 (thay Agy) |
|---|---|---|
| Kết luận | ĐẠT CÓ SỬA | ĐẠT CÓ SỬA |
| CHẶN | 3 | 2 |
| Hook /35 | **23** (4·3·3·4·2·4·3) | **26** (4·3·3·4·3·5·4) |
| Risk Score | **8/10** (Fail: Pet/Kid · Hedging) | — |

Cả hai < 28 → mỗi người viết lại phần mở. **Không tự thay hook user đã duyệt** — trình user ở GATE (A giữ · A′ sửa 1 câu · bản Opus #1 · bản Opus #2).

## Danh sách quyết định

| # | Câu gốc (rút gọn) | Quyết định | Căn cứ |
|---|---|---|---|
| D1 | H3 «Nebraska… four to six inches… Four to six is a solid start» | **NHẬN (CHẶN)** → 8–10 in thu-đông (UNL) vs 6–8 in lá băm (CSU); «six to eight is a fair middle… go toward ten» | C17 nguyên văn: 4–6 in là lớp lập luống, 8–10 in giữ qua thu-đông |
| D2 | M1 C06 (1/3 còn làm nông) + C46 (giá đất) ở 0:40–1:10 | **NHẬN** → cắt cả đoạn | L4/L15: không phục vụ lời hứa, nằm vùng rơi |
| D3 | H2 «same habit you'd see on Amish farms. They're more likely…» | **NHẬN** → «In one Missouri survey, Amish horse farmers more often spread manure… than commercial horse barns did» | C45 phạm vi Missouri, có vế so sánh |
| D4 | M1 «Nothing gets bought. And the soil is left alone all winter.» | **NHẬN** → chỉ gán thói quen phân cho Amish; «the rest of the rhythm comes from extension research» | không có mã; PROMISE_OK |
| D5 | H1 «move that crop to a new spot next season» | **NHẬN** → «out of that spot for a few years» | C33 |
| D6 | H2 «does best composted first» (phân gà) | **NHẬN** → «should be composted before it goes on a food garden» | C12, YMYL |
| D7 | Không có pet/kid + rửa tay | **NHẬN** → thêm 3 câu: ký sinh trùng sống lâu hơn (C48) · giữ thú cưng ra khỏi vườn rau · rửa tay 20 giây nước nóng xà phòng (C47) | nguồn mới UMaine #2510 (orchestrator mở 18/11) |
| D8 | H2 «a lot of us make it. We think…» | **NHẬN** → «it's a common one. A pile… looks like compost.» | giọng narrator (X5 nhẹ) |
| D9 | Timing wall thiếu câu hỏi extension | **NHẬN** → «written for organic farms… smart habit for a home garden… county extension office can help» | YMYL C09/C10 |
| D10 | «by early December» | **NHẬN** → «by the end of November» | 120 ngày trước 1/4 = 2/12 → cần biên |
| D11 | «manure on bare soil… needs a blanket» mâu thuẫn chờ đông giá | **NHẬN** → «bare soil has a problem…»; mốc phủ thành «one common rule… rule of thumb for a vegetable bed» | C21 là ngữ cảnh cây lâu năm |
| D12 | «In a warmer zone… wait for them» | **NHẬN** → «if hard freezes don't come where you live, ask your county extension office» | vùng 9–10 |
| D13 | «Earthworms pull them down» không mã | **BÁC một phần** → giữ ý, sửa câu theo nguyên văn UNL «earthworms and other soil organisms work it into the soil below», thêm **C49** | UNL (orchestrator đã mở 18/11) |
| D14 | «No need to dig it in» không mã | **BÁC** → thêm **C50** (Penn State: rải trên mặt hoặc vùi) | Penn State (đã mở) |
| D15 | «Weed seeds only sprout» | **NHẬN** → «Most weed seeds sprout only…» | C28 «usually» |
| D16 | «One pass to break the hardpan» | **NHẬN** → «loosen that packed ground» | C43 không nói hardpan |
| D17 | Đào cỏ lâu năm nằm ở H4 (sau khi đã phủ) | **NHẬN** → chuyển lên H3 trước «Timing matters», «before the leaves go down» | trình tự |
| D18 | Rye «September through the first of November» — cửa sổ đã đóng | **NHẬN** → «it's a job for next fall» | C40/C41, ngày đăng T12 |
| D19 | Loop #3 phép thử cỏ chưa có nguồn, năm đầu có thể nhiều cỏ | **NHẬN** → «The first year, you may still see a flush… Over the seasons, fewer…» | Consensus #2 (C22, C28) |
| D20 | Loop #1 không nhắc 0:26→4:57 | **NHẬN** → thêm câu nhắc cuối H1 (~2:55) | L4/L5 |
| D21 | Hook «Old-style Amish gardens get ready for spring a different way» (CHẶN) · «every pass drags old weed seeds» · L3/L6 (không số trước 0:20, chưa gọi tên 4 thói quen <1:00) | **HOÃN → GATE user** | hook đã duyệt; không tự thay |
| D22 | Triple F «vines are brown and tired» vs cây bệnh — hai cảnh phải khác | **NHẬN** → cảnh báo người dựng | cảnh |
| D23 | Thẻ nguồn UNL dễ nhầm Lancaster County PA | **NHẬN** → thẻ ghi «University of Nebraska–Lincoln Extension» | cảnh báo dựng |

**Tổng:** nhận 20 · bác 2 (D13 một phần, D14 — bổ sung mã) · hoãn 1 (hook → user).
**gate.py sau sửa (`sau-phan-bien-v1`):** 7/7 PASS · 1.862 từ ≈ 11,3′.
