# Phản biện vòng 2 — big-idea-098 (18/11/2026)

**Phạm vi:** 11 vùng đã sửa (`phan-bien-v2/vung-da-sua.md`) + 1 câu trước/sau; hook chờ user, không chấm. R2 chấm Risk Score trên cả bài.
**Người phản biện:** R1 = Agy `--sandbox` → **thất bại lần 3** (DEADLINE_EXCEEDED 15′, rỗng) → Opus #2 ngữ cảnh mới (`phan-bien-v2/r1/opus2-phan-bien.md`). ⚠️ **Cùng hãng cả 2 vòng.** R2 = Opus (`phan-bien-v2/r2/opus-phan-bien.md`).

| | Opus R2 | Opus #2 (thay Agy) |
|---|---|---|
| Kết luận | ĐẠT CÓ SỬA · 0 CHẶN | ĐẠT CÓ SỬA · 0 CHẶN |
| Risk Score | **8/10** (Fail §3 Pet/Kid · §8 Hedging) — «sửa ~4 câu là lên 10/10» | — |

## Danh sách quyết định

| # | Câu gốc | Quyết định | Căn cứ |
|---|---|---|---|
| E1 | H3 mốc phủ: «wait for a few hard freezes… Thanksgiving–Christmas» mâu thuẫn «bare soil needs a blanket» (cả 2 nêu) | **NHẬN** → C17 làm luật chính («once your fall cleanup is done, and stay on through winter»); C21 nói rõ là luật cho hoa lâu năm | C17 (8–10 in thu-đông) · C21 ngữ cảnh perennial |
| E2 | KẾT «tucked in snug after a few hard freezes» | **NHẬN** → «tuck the beds in snug for winter» | theo E1 |
| E3 | M1 «Manure from the farm's own animals goes straight onto the fields» (nói rộng) | **NHẬN** → «one horse-era habit: putting the farm's own manure back on the land» | C45 chỉ Missouri |
| E4 | H2 «…than commercial horse barns did» | **NHẬN** → bỏ vế so sánh, «often spread manure straight onto their fields for their crops» | ledger C45 không ghi nhóm so sánh |
| E5 | «Six to eight… is a fair middle» (cả 2 nêu) | **NHẬN** → «Start with six to eight inches… go toward ten» | 6–8 là đầu thấp |
| E6 | Pet/kid chỉ có pets (§3 Fail) | **NHẬN một phần** → «wash your hands, and the kids' hands» | C47 (rửa tay sau khi đụng động vật); không có nguồn riêng về trẻ em và đống phân → không thêm câu «giữ trẻ tránh xa» |
| E7 | Hedging: «the first hard rain seals the top» · «get used up» · «no matter how deep the mulch» | **NHẬN** → «a hard rain can seal the surface» · «gradually run down» · bỏ «no matter how deep» | C44 · C22 («gradually») · C37 |
| E8 | C33 «keep that crop out of that spot» | **NHẬN** → «plant something there that isn't prone to that disease» | C33 nguyên văn |
| E9 | Rải phân trước khi nói luật 120 ngày | **NHẬN** → «Just mind the calendar. That part's coming up in a minute.» | trình tự an toàn |
| E10 | H4 «Here's why this works» lặp 4 lần, lạc nghĩa ở phép thử cỏ | **NHẬN** → bỏ ở H4 (còn 1 lần trong bài nháp có thẻ) | L19 khuôn lặp |
| E11 | Loop #3 dễ hiểu nhầm khi cỏ mọc từ rễ cũ | **NHẬN** → «Weeds pushing up from old roots don't count…» | C37 |
| E12 | M5 sau khi xới một lần nên phủ 4–6 in | **NHẬN** → «Then cover it with four to six inches of organic matter» | C17 (lớp lập luống) |
| E13 | «bare soil» chưa gắn mã | **NHẬN** → [C44, C17] | |
| E14 | «county extension office» lặp 3 lần/5′ | **ĐÃ GIẢM** còn 2 (bỏ câu vùng 9–10 khi viết lại E1) | L19 |
| E15 | Loop #1 không nhắc 5:17→9:04 | **BÁC** | Loop #3 mở 7:00 giữ đoạn này; spine cho phép ≤2 loop chồng |
| E16 | 7 cụm số trong 3:53–4:58 | **NHẬN cho người dựng** → thẻ đồ hoạ mang 113/140 °F và lịch «Nov 30 + 120 → Mar 30» | L18 (giọng không đọc lại) |
| E17 | Hook ngụ ý cả 4 thói quen là của Amish | **HOÃN → GATE user** | hook đã duyệt |

**Sửa sau vòng 2 chưa có người đọc lại** (đúng quy trình: vòng 2 không còn CHẶN → không chạy vòng 3).
**gate.py `sau-phan-bien-v2`:** 7/7 PASS · 1.872 từ ≈ 11,3′.
**Risk Score dự kiến sau E6/E7:** 9–10/10 (chưa chấm lại; §3 vẫn có thể bị trừ vì không có câu riêng về trẻ em — không có nguồn).
