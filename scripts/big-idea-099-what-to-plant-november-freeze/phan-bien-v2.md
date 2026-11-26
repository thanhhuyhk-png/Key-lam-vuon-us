# Sổ phản biện — big-idea-099-what-to-plant-november-freeze · vòng 2

> Bước 3R · 19/11/2026 · vòng 2 soi `phan-bien-v2/vung-da-sua.md` + loop + Risk Score cả bài.

## Nguồn
| Người phản biện | Model | Thư mục cách ly | Kết luận | Hook /35 |
|---|---|---|---|---|
| R1 Agy | Agy 1.5.11 `--sandbox` | phan-bien-v2/agy/ | ĐẠT CÓ SỬA — **4 CHẶN** (đều sửa được bằng đổi câu) | 30/35 |
| R2 Opus ngữ cảnh mới | opus | phan-bien-v2/opus/ | ĐẠT CÓ SỬA — **0 CHẶN** · **Risk Score 9/10 (PUBLISH)** | **33/35** |

Bản gốc: `phan-bien-v2/agy/agy-phan-bien.txt` · `phan-bien-v2/opus/opus-phan-bien.md`

## ✅ Đã nhận (E1–E17)
| # | Mức | Từ | Câu gốc | Quyết định sửa | Căn cứ |
|---|---|---|---|---|---|
| E1 | CHẶN (R1) / NÊN SỬA (R2) | R1+R2 | «What if the ground freezes before you're done?» → trả lời việc phải làm TRƯỚC khi đất đóng băng | → «What if the ground is about to freeze before you're done?» | C53 |
| E2 | CHẶN (R1) / NÊN SỬA (R2) | R1+R2 | câu chốt tỏi «split on its leaves» chưa có ở đoạn tỏi | thêm vào đoạn tỏi hai lý do: bảng bất đồng lá (C06 nhẹ / C08 dưới 28°F) + cần lạnh (C13); câu chốt «doesn't just survive the cold. It needs it.» | C06, C08, C13, B8 |
| E3 | CHẶN (R1) / NÊN SỬA (R2) | R1+R2 | «A quick word on the title… We'll get to both.» (0:36–0:47, vùng rơi 40–55 s; loop phụ bỏ quên) | bỏ câu meta và lời hẹn; thay bằng «In mild-winter places… Which one are you? Your forecast will tell you.» | L4, L15 |
| E4 | CHẶN (R1) / GỢI Ý (R2) | R1+R2 | «Now, here's what we couldn't find. The only page we found… for pots» (khuôn «we found» ×2; C47 chỉ cho cải bó xôi) | → «Seeding over frozen ground? The one page on it means spinach seed in late winter, not November. [C47]»; bỏ vế chậu | L19, C47 |
| E5 | NÊN SỬA | R1+R2 (Risk mục 8) | «hardy, wherever it's listed» · «spinach is fine right at the line» · KẾT «ride out the cold nights near twenty-eight» | «all seven tables we opened put it with the hardy crops» · «a fair bet right at the line. Colder than that, cover it.» · «ride out a short night near twenty-eight» | L19, CR4, Compliance 8 |
| E6 | NÊN SỬA | R2 | «moderate bin» dùng khi chưa giới thiệu nhóm | → «the twenty-four-to-twenty-eight group» / «that same group» | rõ nghĩa |
| E7 | NÊN SỬA | R1+R2 | «Star any night that stays low for hours» (app không xem 10 đêm theo giờ) | → «For the next night or two, check the hourly view, and star any night that stays low for hours.» | khả thi |
| E8 | NÊN SỬA | R2 | «First, how many degrees…» ngay sau «three signs» | → «So, how many degrees…» | rõ nhịp |
| E9 | NÊN SỬA | R1+R2 | «Mild-winter states…» nói rộng hơn nguồn; M4 tóm tắt hai lần | bỏ câu tóm tắt «So the answer splits by winter…»; câu kết M4 giữ «Mild winter? Keep planting.» | CR4, C33 |
| E10 | NÊN SỬA | R1 | «A bedsheet isn't row cover…» (ngụ ý) | → «And don't count on a sheet for a deep freeze. Below about twenty-eight, general frost covers typically stop helping.» | C58 |
| E11 | NÊN SỬA | R1 | thẻ bảng số phiếu thiếu C70–C72 | thêm [C70, C71, C72] | nhất quán mẫu số |
| E12 | GỢI Ý | R1 | «Same cold tolerance» | → «Nearly the same cold tolerance» | C04 |
| E13 | NÊN SỬA | R1 | khuôn «Most tables/pages» ×4; «Most other tables agree» | «The other tables list them with the hardy crops too, though one says turnips hold up only for a limited time.»; cabbage «Most tables» | L19 |
| E14 | GỢI Ý | R2 | «Two of those bins come with numbers» gộp Purdue + SDSU | → «One table puts numbers on the two tougher bins.» | C06 |
| E15 | GỢI Ý | R2 | «pale green bulb» không có trong ledger | → «the round bulb» | ledger |
| E16 | GỢI Ý | R2 | thẻ [C31] ở câu «Check the label, and keep pets off…» | bỏ thẻ (câu của kênh) | Compliance |
| E17 | GỢI Ý | R1 | mốc loop khai khác thực tế | ghi mốc thực vào pipeline-state (Loop #1 0:15→~5:45 · #2 ~2:58→~3:59 · #3 ~6:03→~8:16 · #4 ~8:24→~9:50) | bản đồ loop |

## ❌ Không áp dụng (ghi lý do)
| # | Từ | Mục | Lý do |
|---|---|---|---|
| X1 | R1 GỢI Ý | «One Maryland page… through December» khoanh vùng khí hậu | câu đã nói «Maryland»; không thêm điều kiện không có trong C27 |
| X2 | R2 ⑤ (4/5) | hook «Five vegetables in all hold up at that number» | Hook A do user duyệt; cải bó xôi được nói rõ «right at the line» ở M2 |
| X3 | R1 | neo «Five of our eight tables…» bằng con số trong lời đọc | tăng chuỗi số bị đọc (L18); số phiếu để thẻ đồ hoạ mang |

## Hai bên bắt gì khác nhau
- R1 bắt mà R2 không: thiếu [C70–C72] trên thẻ bảng số phiếu · C58 vs «bedsheet isn't row cover» · khuôn «Most tables» lặp.
- R2 bắt mà R1 không: «moderate bin» chưa giới thiệu · «First,» chồng bộ ba · hedging «sure one / fine / ride out» (Risk mục 8).
- Cả hai: câu «quick word on the title» · «frozen ground» trình tự · tỏi «leaves» · «Star any night».
- Lưu ý: vòng 2 R1 vẫn xếp 4 lỗi vào CHẶN; R2 xếp 0. Cả 4 đã sửa đúng chỗ nhưng chưa người phản biện nào đọc lại bản sau sửa (quy trình không cho vòng 3 tự động).

## Sau khi sửa
- Người biên tập: orchestrator, sửa theo E1–E17, chỉ sửa câu trong danh sách.
- `gate.py` sau sửa: **PASS 7/7** — 1.837 từ ≈ 11,1′ · lint 0 lỗi (2 cảnh báo nhẹ khuôn «the pages» ×2) · số liệu 0 ngoài danh sách · 56 thẻ claim · compliance regex CLEAN · đối thủ 6-gram 0,00%.
- Điểm chính thức: **Compliance Risk 9/10 (R2 chấm trước khi sửa mục 8)**; mục 8 đã sửa nhưng chưa chấm lại.
