# Sổ phản biện kép — Vòng 2 (16/11/2026) — big-idea-095

Phạm vi: 28 đoạn đã sửa sau vòng 1 (`phan-bien-v2/vung-da-sua.md`) + 1 câu trước/sau. Risk Score chấm lại cả bài.
**R1 Agy** (`--sandbox`, prompt có cột quote): Hook **34/35** · 3 CHẶN · 5 NÊN SỬA · 2 GỢI Ý · Risk (thang riêng) 28/100 → ~10/100 sau vá · ĐẠT CÓ SỬA.
**R2 Opus** (ngữ cảnh mới): Hook **32/35** · 1 CHẶN · 11 NÊN SỬA · 9 GỢI Ý · **Risk Score 9/10** (mục 8 hedge hiệu quả; cần 10 vì chủ đề ăn được/YMYL) · ĐẠT CÓ SỬA.

## Danh sách quyết định

| # | Nguồn | Vấn đề | Quyết định | Căn cứ / cách sửa |
|---|---|---|---|---|
| E1 | Cả hai CHẶN | «Onions and garlic get cured warm and dry first» | **NHẬN** | C23: tỏi «shaded, well-ventilated and cool» → «Onions get cured warm and dry, garlic in a shaded, airy spot. Then both move…» |
| E2 | Agy CHẶN · Opus NÊN SỬA | Quy tắc mở lỗ thông gió «khi ngoài lạnh hơn trong» → giữa đông kho xuống <32°F | **NHẬN** | «…but not when it's freezing out. Shut them tight when it's warmer outside.» |
| E3 | Agy CHẶN (L18) | «The charts put the ceiling closer to eight months… ten for potatoes» đọc lại số | **BÁC** | Đây là câu bác claim «full year» của đối thủ, cần số trần; `script_lint` L18 PASS (không có ≥4 cụm số lặp). Câu thay thế của Agy («top out short of twelve months») là claim mới không có trong sổ |
| E4 | Opus NÊN SỬA | Khoanh vùng khí hậu: nhiệt kế «tonight» chưa đo được đêm lạnh nhất; «isn't ready yet» ngầm bảo chờ | **NHẬN** | «Check it again after your first hard freeze. If it dips below thirty-two, that spot won't work for vegetables.» |
| E5 | Cả hai | Thùng chôn: «harshest winters» mơ hồ, «keep it from freezing» không đường lui; thiếu cảnh báo đào đất | **NHẬN** | «…where winters get bitter cold. Check for buried lines before you dig. Then keep a thermometer in it. If it heads toward freezing, move the vegetables to your coolest spot indoors.» |
| E6 | Opus | «By lunch, you've got…» (hứa mốc thời gian + mâu thuẫn «không rõ chôn sâu») — Risk mục 8 | **NHẬN** | «Picture a fall Saturday, before the ground freezes… That's a cold spot in the yard.» |
| E7 | Opus (Risk mục 8) | «That's a whole winter, and then some» sau «one to eight» | **NHẬN** | «At the top of those ranges, that's a whole winter, and then some.» |
| E8 | Opus NÊN SỬA | M1 «cùng khoảng 32–40» vênh M4 (khoai <40 ngọt) | **NHẬN** | Thêm «That's the warm end of the range, so potatoes get the warmest of your cold spots.» |
| E9 | Cả hai | Chậu nước / «closed bin» trong phòng chung phá vùng khô | **NHẬN** | «covered, dark bin that still breathes… The room air is the dry zone, so skip the pan of water when onions share the room.» |
| E10 | Cả hai | Câu ASPCA chen làm «this could be why» trỏ nhầm; «those racks» chưa có tiền đề | **NHẬN** | Chuyển ASPCA thành đoạn riêng sau cảnh «February morning»; «skipping the cure could be why» |
| E11 | Opus | Hành «warm start» nhầm Loop #2 | **NHẬN** | «Onions get a warm start too, but out in the air. The one that needs the dark is still coming.» (thêm nhịp nhắc loop) |
| E12 | Cả hai | Sawdust lặp ý (S5/S6); «Don't panic» báo động vô cớ | **NHẬN** | S5 chỉ «moist sand»; S6 «No sand? Don't panic. Sawdust works just as well…» (giữ cụm đặc trưng) |
| E13 | Cả hai | «extension services list the first two» ngầm bác Option 3 (C32 có nguồn) | **NHẬN** | → «You've got three options. None of them needs a dug cellar.» |
| E14 | Agy NÊN SỬA | Cắt «One guide says two to three weeks. Another says up to four.» | **NHẬN một phần** | Giữ câu bất đồng (D4, nói thật), bỏ lặp «two to four weeks» ngay trước đó |
| E15 | Opus GỢI Ý | «Lay the dry zone next to the wet zone» nghe như đặt sát nhau | **NHẬN** | «Put the two zones side by side on the chart» |
| E16 | Opus GỢI Ý | «other side of the shelf» ngược luận điểm | **NHẬN** | «in the next zone over» |
| E17 | Opus GỢI Ý | «wet towel» → «damp towel» | **NHẬN** | |
| E18 | Opus GỢI Ý | «So keep apples away from potatoes» thiếu cà rốt/bắp cải; «within reach» thiếu late-crop; «shed in January» | **NHẬN** | C16 + C02 + «bin in January» |
| E19 | Agy GỢI Ý | «porch» → «enclosed porch» (C28); mã [C09] không thuộc «vegetables» | **NHẬN** | ACTION_TIP đổi «garage, enclosed porch or shed» (header + 2 chỗ + callback, lint PASS); [C01–C08] |
| E20 | Agy NÊN SỬA | «The research we have» lộ giọng ghi chú | **BÁC** | Opus xác nhận đúng L19 ⑤ (thừa nhận giới hạn); narrator tập thể «the research we have» không phải tự nhận trải nghiệm cá nhân |
| E21 | Opus GỢI Ý | «three mistakes» gieo/trả xa; header «Tên đọc bằng giọng: 0» | **NHẬN một phần** | Sửa header (ASPCA ×1); để nguyên gieo/trả mistakes (GỢI Ý) |
| E22 | Opus | Thumbnail `NEVER TOGETHER` | **GHI NHẬN** | ưu tiên `98% vs 65%` (đã là ⭐ ở outline) |

## Kết quả
- **Không chạy vòng 3** (theo quy trình). Các sửa E1–E21 áp **sau vòng 2** nên **chưa có người độc lập đọc lại** các câu mới. Mỗi sửa bám đúng câu mà người phản biện đề xuất hoặc khớp một dòng sổ claim; `gate.py` + `script_lint` kiểm lại bằng máy.
- `gate.py --nhan sau-phan-bien-v2`: **PASS** (0 FAIL). Cảnh báo: chưa có transcript đối thủ; compliance regex SOFT-FAIL vì câu thú cưng ASPCA (cố ý; Opus chấm mục I = ✅).
- **Risk Score:** Opus 9/10 → hai câu mục 8 («whole winter», «By lunch») đã sửa theo đúng đề xuất → kỳ vọng 10/10, **chưa được chấm lại độc lập**.
- Script: 1.830 từ ≈ 11,1′. Bản trước vòng 2: `script.draft-markers.v1-before-round2-fix.md`; trước 3R: `script.v0-before-3R.md`.
- **Chờ user quyết ở GATE:** (1) chữ «garage» trong hook A (nguồn nói hành lang/hiên kín/nhà kho); (2) có chạy vòng 3 cho các sửa sau vòng 2 không.
