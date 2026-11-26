# Sổ phản biện — big-idea-102-winter-sowing-milk-jugs · vòng 1

> Bước 3R · 26/11/2026 · Phản biện chéo hãng (Gemini + Claude Opus + Đóng gói L25) trong thư mục cách ly `phan-bien-v1/`.
> Nguyên tắc: nhận lỗi có dẫn chứng (C.. / ACTIVE RULES / `gate.py`); bác lỗi mà trang gốc/ledger chứng minh sai.

## Nguồn
| Người phản biện | Model | Thư mục cách ly | Kết luận | Điểm |
|---|---|---|---|---|
| **R1 Gemini** | Gemini Flash (isolated `research`) | `phan-bien-v1/r1-gemini.md` | **ĐẠT CÓ SỬA** | Hook **31/35** |
| **R2 Claude Opus** | Claude Opus (`claude -p --tools ""`) | `phan-bien-v1/r2-claude.md` | **ĐẠT CÓ SỬA** | Hook **27/35** · Compliance Risk **8/10 (REVISE)** |
| **R3 Đóng gói (L25)** | Gemini Flash (isolated `research`) | `phan-bien-v1/dong-goi.md` | **ĐẠT CÓ SỬA** | Khớp 60s **7.5/10** · Thumb A **5.5/10** · B **5.0/10** |

---

## ✅ Đã nhận → Danh sách quyết định biên tập (D1–D16)

| # | Mức | Từ | Vị trí | Quyết định sửa (chỉ sửa đúng danh sách) | Căn cứ |
|---|---|---|---|---|---|
| **D1** | **CHẶN** | R1 + R2 | @3:58 & @6:21 | Bỏ cụm `"built for cool soil"` trên Kale và giải thích minh bạch phạm vi từng nguồn (Spinach có mặt từ Northern Plains C17 tới Trung Tây/PNW; Kale thuộc họ cải nhưng vẫn xuất hiện ở 4 nguồn `.edu` mùa đông C12/C22/C26/C40 — đồng thời nói thẳng mối liên hệ Kale ở đoạn C19). | C12 · C17 · C19 · C22 · C26 · C40 |
| **D2** | **CHẶN** | R1 + R2 | @0:48 & @9:15 | Đưa cảnh báo thông gió khi đốt lỗ nhựa bằng súng keo/mỏ hàn (`C36`) lên **ngay sau câu đục lỗ @0:48** trong M1; xóa bản đặt muộn ở M4. | C36 · An toàn trình tự |
| **D3** | **CHẶN** | R1 + R2 | @6:50 (M3) | Bỏ đọc lại 5 cụm số+đơn vị (`two to four`, `three to four`, `five to eight`, `fifteen`, `four`) khi bảng GFX M3 đã hiện số → giọng chỉ nói quy luật gọn. | L18 |
| **D4** | **CHẶN** | R2 + R3 | Thumbnail A & B | **Bỏ `"$0 IN JANUARY"`** (overclaim vì vẫn mua potting mix/băng dính/bút) → sửa **Thumb A** thành **`6 SEEDS IN JANUARY`** (vàng) / **`NO GROW LIGHTS`** (trắng); sửa **Thumb B** bổ sung tháng thành **`ROTTING SEEDS?`** / **`JANUARY JUG FIX`** (và giữ PA3 `SOW 6 IN JANUARY` / `SKIP THESE 3!` để Test & Compare). | L17 · L25 · L29 · LUẬT THÁNG |
| **D5** | **NÊN SỬA** | R2 | @2:15–2:35 (M1) | Đổi trình tự: đặt đoạn **ghi nhãn (paint pen / laundry marker + thẻ thứ 2 cắm trong đất)** lên **TRƯỚC** câu `"Close the top and seal the seam"` (không dặn cắm thẻ vào đất sau khi đã dán kín bình!). | Trình tự làm · C09 · C27 · C32 · C38 |
| **D6** | **NÊN SỬA** | R2 | @8:45 (M4) | Đổi trình tự thích nghi: đưa câu `"wait until each seedling's got two sets of true leaves or stands about two inches tall"` lên **TRƯỚC** câu mở bình thích nghi `1–2 ngày` (khớp đúng trình tự C28). | C20 · C28 |
| **D7** | **NÊN SỬA** | R1 + R2 | @3:08 (M2) | Bỏ `"sit rotting in icy mix"` (không có trong C12/C13) → sửa bám đúng C03/C12: cây mùa ấm không cần lạnh và đợt ấm giả khiến hạt nảy mầm sớm dễ chết trong đợt rét kế tiếp. | C03 · C12 · X4 |
| **D8** | **NÊN SỬA** | R1 + R2 | @6:10 (M3) | Sửa `"early winter"` → `"January and February"` cho Illinois (`C12`) và `"some lettuce varieties"` cho SDSU (`C17`). | C12 · C17 |
| **D9** | **NÊN SỬA** | R2 | @4:03 (M2) | Bỏ `"crowding each other for light"` và nêu đúng 2 mốc mật độ hạt (`twenty to twenty-five` theo C27, `six to eight` cho hạt vừa / `four to six` cho hạt to theo C34). | C27 · C34 |
| **D10** | **NÊN SỬA** | R2 | @1:42 (M1) | Khoanh vùng `green algae` đúng bối cảnh C36 (mùa đông ẩm với `moisture-control mix`, không gán cho phân bón); sửa từ tiếng Việt trong `research-brief.md` từ *"rêu xanh"* → *"tảo xanh (green algae)"*. | C31 · C36 · CR4 |
| **D11** | **NÊN SỬA** | R2 | @6:38 (M3) | Bỏ `"you won't waste seed"` (lời hứa tuyệt đối X2) và mốc mơ hồ `"late winter"` → đổi sang `"hold broccoli, lettuce, and cosmos until March, when the later guides start them"`. | C29 · C41 · X2 |
| **D12** | **NÊN SỬA** | R2 | @4:22, @4:38, @8:38 | Bỏ 3 chi tiết chưa có mã ledger (`"pricey little starter pots"`, `"bring pollinators right to your yard"`, `"freeze the root zone solid"`) và câu chê ngầm `"copying one video blindly can burn you"`. | C14 · C16 · C22 · C26 · C32 · C40 |
| **D13** | **NÊN SỬA** | R2 + R3 | Hook D (0:00–0:41) | Chỉnh phẫu thuật nhẹ Hook D (vẫn giữ nguyên Story Bank Trudi Davidoff mà user đã chọn tại GATE 2): ① chèn cụm exact keyword **`"winter sowing"`** ngay câu 1 (@0:04, L10/R3); ② bỏ quan hệ nhân quả không nguồn `"It worked so well"`; ③ bỏ `"Let's prep your jug first"` ở giây 0:39 để tránh sát vùng 38–60s; ④ sửa dòng header `LOOP` chỉ đúng điểm đóng đầy đủ. | L10 · L15 · C10 · C15 · R3 |
| **D14** | **GỢI Ý** | R1 + R2 | @1:25, @2:15, @7:55, Kết | Sửa tiểu tiết gọn: bỏ `"packs down hard"` (chỉ giữ mầm bệnh & cỏ dại C08); đổi `"two tiny holes"` → `"a couple spots"` (C20); đổi `"about once a week"` → `"at least once a week"` (C39); bỏ `"for a week"` ở hardening off; bổ sung 1 câu hỏi ngắn vào phần Kết ≤55 từ (L23); đồng bộ `C10/C11/C20/C34` trong `research-brief.md` & mã mới trong `allowed-numbers.json`. | C08 · C20 · C39 · L23 |
| **D15** | **GỢI Ý** | R2 | @0:42, @2:38 | Sửa thẻ `[C..]` thừa/lệch (`[C06]` cho rửa bình, `[C09]` cho két sữa, `[C37]` cho nắng ngoài trời) và ghi cảnh báo sản xuất không quay thú cưng cạnh milkweed. | Claim Ledger hygiene |
| **D16** | **GỢI Ý** | R2 | Lặp chữ | Đổi lần dùng thứ 2 của `"Fair warning"` ở M2 thành `"One heads-up"` để tránh lặp cụm. | Phong cách |

---

## ❌ Đã bác (kèm bằng chứng)

| # | Từ | Lỗi người phản biện nêu | Vì sao bác (bằng chứng từ 7 tài liệu `.edu` đã mở) | Báo nhầm lặp lại? |
|---|---|---|---|---|
| **B1** | R2 | «Nguồn nói rêu, không nói algae» | Bản PDF gốc WSU Skagit County (trang 4) viết nguyên văn: `"I also learned green algae can grow on the surface of the potting soil"`. Lỗi chỉ do bản tóm tắt tiếng Việt trong `research-brief.md` dịch thoát là *"rêu xanh"* (đã đính chính về *"tảo xanh (green algae)"*). | Không (lỗi dịch brief) |
| **B2** | R2 | «duct tape không có trong nguồn» | `duct tape` có nguyên văn trong 6/7 nguồn `.edu` đã mở: Penn State (`"light-colored duct tape"` C09), Illinois (`"secure with duct tape"` C10), SDSU (`"duct tape"` C20), NC State (`"duct tape"`), OSU Lucas (`"Heavy Tape like duct tape"`), OSU Licking (`"duct tape"` C31), WSU (`"duct tape"`). Chỉ nhận đổi `"two tiny holes"` → `"a couple spots"`. | Không |
| **B3** | R1 | «Không nguồn nào nói packet depth / spray bottle / rắc mỏng hạt nhỏ» | Có nguyên văn trong các trang `.edu` đã mở: Illinois (`"Leave small seeds on top of the soil. Follow the instructions on the seed packet for planting depths of larger seeds"`), SDSU (`"Use a spray bottle on the spritz or mist setting"`), OSU Licking (`"Tiny, dust-like seeds... Sow thinly"`). Đã bổ sung quote vào bảng C11/C20/C34 của `research-brief.md` để V2 tra rõ 100%. | Không (tóm tắt brief thiếu quote) |
| **B4** | R2 | Đề xuất viết lại toàn bộ Hook D bỏ giai thoại Trudi Davidoff | User đã chọn Hook D tại GATE 2 và R1 chấm Hook D **31/35**; chỉ chỉnh phẫu thuật 3 điểm (D13) thay vì thay cả Hook. | Không |

---

## Hai bên bắt gì khác nhau (kinh nghiệm)
- **R1 & R2 cùng bắt (tín hiệu 100% chuẩn):** mâu thuẫn Kale/họ cải C19 · vị trí cảnh báo khói nhựa C36 · L18 đọc lại 5 cụm số ở M3 · `"sit rotting"` không nguồn · Illinois `"January and February"`.
- **R2 (Claude Opus) bắt mà R1 không:** 2 lỗi trình tự cực đắt (cắm thẻ đất sau khi dán kín bình · đợi 2 cặp lá trước khi tập quen 1–2 ngày), lời hứa `"you won't waste seed"`, 3 cụm nhỏ ngoài ledger (`starter pots`, `pollinators`, `freeze solid`), cảnh báo milkweed/thú cưng và overclaim `"$0"` trên Thumb A.
- **R3 (Đóng gói L25) bắt mà R1/R2 ít nhấn:** thiếu cụm từ khóa nguyên văn `"winter sowing"` trong 60 giây đầu + thiếu tên tháng trên Thumb B.

---

## Sau khi sửa (Vòng 1 → Vòng 2)
- Đã áp dụng trọn vẹn `D1–D16` vào `script.draft-markers.md`, `script.md`, `research-brief.md`, `allowed-numbers.json`, `outline.md` (cập nhật Thumb A/B).
- Chạy lại `tools/gate.py` (`sau-phan-bien-v1`) và tiến hành phản biện Vòng 2 trên `phan-bien-v2/vung-da-sua.md`.
