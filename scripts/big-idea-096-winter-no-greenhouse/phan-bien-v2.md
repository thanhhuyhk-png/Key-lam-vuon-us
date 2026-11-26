# Sổ phản biện — big-idea-096-winter-no-greenhouse · vòng 2

> Vòng 2 chỉ soi `phan-bien-v2/vung-da-sua.md` (vùng đã sửa sau vòng 1) + 1 đoạn trước/sau.

## Nguồn
| Người phản biện | Model | Thư mục cách ly | Kết luận | Hook /35 |
|---|---|---|---|---|
| R1 Agy | mặc định Agy `--sandbox` | phan-bien-v2/agy/ | ĐẠT CÓ SỬA (0 CHẶN · 4 NÊN SỬA · 2 GỢI Ý) · tự chấm rủi ro 1/10 (thấp) | không chấm lại (hook giữ bản user duyệt) |
| R2 Opus ngữ cảnh mới | opus | phan-bien-v2/opus/ | ĐẠT CÓ SỬA (0 CHẶN · 7 NÊN SỬA · 5 GỢI Ý) · **Risk Score 10/10 → PUBLISH** | 30 (tham khảo, từ vòng 1) |

Bản gốc: `phan-bien-v2/agy/agy-phan-bien.txt` · `phan-bien-v2/opus/opus-phan-bien.md`
**Compliance Score chính thức (R2 Opus, vòng 2): 10/10.**

## ✅ Đã nhận → danh sách quyết định biên tập
| # | Mức | Từ | Câu gốc | Quyết định sửa | Căn cứ |
|---|---|---|---|---|---|
| D23 | NÊN SỬA | cả hai | «Here's why it's enough… A gap of two? Reach for a medium cover, not a light one.» — Loop #1 đóng ngược nghĩa | Thêm «That's why two degrees can be enough for a plant that's only two degrees past its limit.»; bỏ ví dụ «gap of two» | C12 «might», C01/C03; mâu thuẫn với «room to spare» |
| D24 | NÊN SỬA | Opus | «three-degree gap… what closes a gap like that?» treo không đáp | M3: «Remember lettuce's three-degree gap? A light cover won't close it, and a medium one cuts it close. Reach for a heavy cover or a low tunnel.» | C12/C14 («up to 4»), C13/C15, C17 |
| D25 | NÊN SỬA | Opus | «Hardy greens? Way one, with a light fabric on the coldest nights.» | «…plus a cover that fits the gap on the coldest nights.» | luật «room to spare» (M3) |
| D26 | NÊN SỬA | cả hai | «Those numbers come from… west of the Cascades» đứng sát số SDSU | «The hardy numbers, zero to fifteen, come from… and the chart calls them guidance only.» | C01 (PNW 548) vs C10 (SDSU) |
| D27 | NÊN SỬA | Opus + Agy | «you can harvest it all winter» lệch «until the ground freezes solid» | «Kept within its cold limit… you can keep picking through the winter. For roots, that lasts until the ground freezes solid.» | C36, C26; CR4 |
| D28 | NÊN SỬA | cả hai | «take chipping paint… seriously» (không có hành động) | «So if an old window has chipping paint, skip it, or ask your local extension office first.» | C38; YMYL chì |
| D29 | NÊN SỬA | Agy | «a cold frame earns its keep when you can open the lid on every sunny morning» | «…when you're around on sunny days to vent the lid if the heat builds.» | C18 (ngưỡng 85°F trong khung) |
| D30 | NÊN SỬA | cả hai | Đoạn bất đồng nguồn ở M5: 4 cụm số trong ~70 từ, đọc lại kale 0 vs 24–28 | Đảo thứ tự M5 (bất đồng trước, kế hoạch sau); lời nói chỉ giữ «six to ten» vs «four to eight», kale đã nói ở M1; CITE_ZONE khai lại | L18; D1/D2 |
| D31 | GỢI Ý | Opus | «Every cover so far adds a few degrees» (vải dày tới 10) | «buys you a handful of degrees» | C16 |
| D32 | GỢI Ý | cả hai | Pet-safety nằm cuối đoạn giống cây; «Wait for the light» dễ hiểu nhầm | Tách pet-safety thành đoạn riêng; «Pick the plant. Add the cover. Plan around the light.» | CR5; Agy mục 1&4 |
| D33 | Sổ/ghi chú dựng | cả hai | nhãn thẻ Ladder không thống nhất; ô âm «kale ≈ −10°F» | Chốt `CHANNEL ARITHMETIC · AIR TEMP · GUIDANCE ONLY`; cột vải dày = 4; không ô âm; ô cold frame «WARMER» | brief Cover Ladder; plan on the low end |

## ❌ Đã bác (kèm lý do)
| # | Từ | Lỗi nêu | Vì sao bác | Báo nhầm lặp lại? |
|---|---|---|---|---|
| B9 | Opus | «Glass lets the sun in…» không có mã C | Câu cơ chế chung, nằm cạnh C19; Opus tự ghi «chấp nhận được» | không |
| B10 | Opus | «The next one is different» → «The fourth way is different» | Câu nhắc lại ở đầu cold frame («Remember that sunny hour?») đã vá, chữ gốc giữ nhịp loop | không |
| B11 | Agy | Đảo đoạn 35 xuống sau đoạn 37 | Đã nhận dưới dạng D30 (đảo thứ tự M5) | — |

## Sau khi sửa
- Người biên tập: orchestrator · sửa theo D23–D33, thêm 1 câu có nguồn (C40, mốc ngày sương giá đầu mùa) để đạt sàn số từ — `gate.py` sau sửa: **PASS 0 cổng FAIL, 2 cảnh báo** (số từ 1.651 ≈ 10,0′; đối thủ chưa có transcript; compliance regex SOFT-FAIL do câu ASPCA tỏi tây, cố ý).
- ⚠️ Bản sửa cuối chưa có người đọc lại (đúng quy trình: không tự chạy vòng 3).
