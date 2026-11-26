# Sổ phản biện vòng 1 — big-idea-100 (22/11/2026)

R1 Agy (khác hãng, `--sandbox`) · R2 Opus (cách ly, kèm Risk Score) · R3 Sonnet đóng gói (chỉ thấy 60 s đầu + ledger-60s).
Điểm: Hook **28/35** (Agy) · **30/35** (Opus) · Risk Score **8/10 = REVISE** · R3 khớp title↔60 s **6/10**, thumbnail **6/10** · Kết luận cả ba: **ĐẠT CÓ SỬA**.
Mỗi bản After được ghép vào script rồi chạy `script_lint.py` + đối chiếu Claim Ledger (L25) — bản trượt hoặc thêm claim không mã bị bác.

## Lỗi hội tụ (2 người phản biện độc lập cùng chỉ ra — độ tin cao)
| # | Lỗi | R1 | R2 | Quyết định |
|---|---|---|---|---|
| H1 | **Quy tắc «pup không rễ → 1 tuần / pup có rễ → trồng ngay» tự đặt** (C03 không nói «no fresh roots»; C24 cũng nói về pup aloe; mâu thuẫn Bước 1 vì mọi pup đã tách đều có rễ) | CHẶN | CHẶN | **NHẬN** — viết lại Bước 3: Arizona «a week or so» (C03) ↔ Illinois «re-pot right away» (C24) là bất đồng thật giữa hai nguồn cùng nói về pup; lá/cành (C28/C22) là câu hỏi khác; quy tắc = «pot now OR give it about a week; if not sure, take the week [C03]» |
| H2 | **«Across the extension guides, three things line up… a dry cut»** là đồng thuận giả (trái C24, C16–C18), cite chung chung, tóm tắt ngay trước kết | CHẶN | CHẶN | **NHẬN** — xoá câu |
| H3 | **Mùa đông nói quá nguồn** («That's about the only change… even with snow outside») — brief ghi NEED DATA | NÊN SỬA | CHẶN | **NHẬN** — «There's no word on whether pups root slower in winter, so give them a little extra patience. Pups that pass both checks can still come off now.» [C16, C13] |
| H4 | **Trình tự kiểm rễ:** nghiêng chậu nhìn không thấy rễ | CHẶN | NÊN SỬA | **NHẬN một phần** — sửa câu Bước 1 («brush a little soil back, so you can see each pup's roots» [C24, C17]); **hook giữ nguyên** (user đã duyệt) → hỏi user sửa hook (mục Q1) |
| H5 | **Đọc dồn số (L18)** ở Bước 5 (5 cụm trong ~45 từ) + cite «Another extension guide puts it» (L19) | CHẶN | NÊN SỬA | **NHẬN** — chỉ giữ «three to four weeks» + «add the week of drying, if you gave it one → four to five weeks» |
| H6 | **Phần sau payoff cuối quá dài (L23)** — «Before the end» 72 từ (tóm tắt lại 2 phép kiểm, tả cảnh, câu hàng xóm) | CHẶN | NÊN SỬA | **NHẬN** — còn 1 câu gọi lại mẹo (L16) + kết; bỏ «Got more pups… / Come spring… / neighbors» |
| H7 | **Độ sâu/cỡ chậu cho pup lấy từ C14/C11 (cây mẹ)** + «is fine» không nguồn | NÊN SỬA | NÊN SỬA | **NHẬN** — «There's no pot size or planting depth written just for pups. So borrow the rules for a grown aloe…» [C11, C14] |
| H8 | **An toàn thú cưng:** chỉ nhắc chậu mới, bỏ quên pup đang phơi; thiếu dòng trẻ em; thiếu «call your vet» | NÊN SỬA | NÊN SỬA (Compliance mục 3 ❌) | **NHẬN** — «keep the new pots, and pups that are drying, where curious noses and little hands can't reach. If your pet ever chews one, call your vet.» [C33] |
| H9 | **«Soak it»** ngay sau «never leave it soaked» | GỢI Ý | NÊN SỬA | **NHẬN** — «Water it well, then wait till the top of the soil's dry.» [C13] |
| H10 | **Mốc trả một phần Loop A tuyệt đối («needs»)** trái C24 | CHẶN* | NÊN SỬA | **NHẬN** — «Most of the time, a cut pup should scab over…» (*Agy tính mốc giữa là «chưa trả gì → 186 s»; Opus tính 171 s. Lint đo 172 s ≤ 180 s ✅; vẫn giảm 8 s bằng cách bỏ câu độn) |
| H11 | **«the longest wait you'll hear, and it's the one written for aloe pups»** — tuyệt đối hoá + sai (C24 cũng nói về pup) | NÊN SỬA | CHẶN (gộp H1) | **NHẬN** — xoá |

## Lỗi một người phản biện nêu
| Nguồn | Lỗi | Quyết định |
|---|---|---|
| Opus | «four of them are easy» tự phủ định «Easy» (L17) — **nằm trong hook đã duyệt** | **CHỜ USER** (Q1) — lint đạt nhờ `PROMISE_OK`; đề xuất «each one's simple» |
| R3 | «Free» không được nói trong 60 s đầu — **hook đã duyệt** | **CHỜ USER** (Q1) — «plants of their own» → «free plants, each in a pot of its own» |
| Opus | Hook «A month from now» lệch «four to five weeks» | **CHỜ USER** (Q1) — «A month or so from now» (C04) |
| R3 | Tiêu đề: keyword «aloe vera plant care» không nằm đúng cụm 25 ký tự đầu → đề xuất «Aloe Vera Plant Care: Get Free Plants From Pups (5 Steps)» | **CHỜ USER** (Q2) — mình **không khuyến nghị**: «plant care» là người tìm cách chăm, khác người tìm tách pup (growth null); «aloe vera» đã ở ký tự 6 ✅ L10; bỏ «Easy Way» làm yếu khung kênh |
| R3 | Thumbnail thêm dòng trắng `CHECK THE BASE` (P1) | **NHẬN vào concept** (chưa render; công thức 2 tầng của kênh) — ghi `thumbnail-prompts` · user xem ở GATE |
| R3 | Hook hứa «that answer» nhưng nguồn bất đồng; loop treo >180 s | **BÁC phần loop** (R3 chỉ thấy 60 s đầu, không thấy mốc trả một phần ở 3:24 → thiếu thông tin) · **NHẬN phần «một đáp án»:** Bước 3 giờ nói thẳng là bất đồng thật và đưa quy tắc chọn |
| R3 | After «Guides run from overnight to about a week» | **BÁC** — «overnight» chỉ có ở C30 (thư viện, tin cậy C, không dùng làm số) |
| R3 | Bỏ câu trấn an «Those little ones aren't weeds…» (không phải loop) | **NHẬN** — xoá, thêm biên an toàn cho Loop A |
| Agy | After kết bài là 1 câu dài tả cảnh + gộp mẹo + bạn bè | **BÁC After** (trái L23: tả cảnh) — nhận phần xoá |
| Agy | After «[NEED DATA — Brief §D/§E]» chèn thẻ vào lời đọc | **BÁC** — gate NEED DATA sẽ fail; đã viết lại khẳng định thiếu nguồn bằng câu thường |
| Agy | Hook ① 2/5 (chưa có câu hỏi/loop trong 10 s đầu) | **GHI NHẬN, KHÔNG SỬA** — hook đã duyệt; Opus chấm 3/5, tổng hook ≥28 |
| Opus | Bỏ «Picture a row of little pots…» (tả cảnh gần kết) | **NHẬN** — sau khi bài ngắn lại câu này rơi vào 15% cuối và lint L23 bắt |
| Agy | Chữ «Soak it» → «water it thoroughly» | gộp H9 |
| Agy, Opus | Cảnh báo người dựng (clip tay gạt đất; không cảnh thú ngửi aloe; nhãn LEAF/STEM/PUP; không stock agave/haworthia; tưới nhẹ; chỉ ảnh thật) | **NHẬN toàn bộ** → chuyển cho bước dựng |
| Agy | Phân bón: thêm «follow the label» | GỢI Ý — không áp (không có nguồn C18 về nhãn) |

## Câu hỏi cho user (chưa áp — hook và title bạn đã duyệt)
- **Q1 (hook C′, 4 chỗ):** (a) «Look at the base… check two things» → «Brush back a little soil at the base and check two things on each pup» (R1) · (b) «four of them are easy» → «each one's simple» (R2+R3, khớp title «Easy») · (c) «plants of their own» → «free plants, each in a pot of its own» (R3) · (d) «A month from now» → «A month or so from now» (R2).
- **Q2 (title):** giữ Title A (khuyến nghị) hay đổi theo R3.
- **Điều kiện đường nhanh (C3): KHÔNG đủ** — video có độc tính thú cưng (ASPCA) và vòng 1 có 3 lỗi CHẶN ⇒ **bắt buộc vòng 2**.

## Danh sách quyết định đã áp (D1–D13) và gate
Áp 13 thay thế chính xác vào `script.draft-markers.md` + `script.md` (dựng từ một nguồn). `script_lint` PASS (L27: Loop A 172 s) · gate.py: chỉ SỐ TỪ FAIL (**1.377 từ ≈ 8,3′** — thấp hơn 8,8′ bạn chấp nhận vì xoá các câu không nguồn/độn; mọi mốc Spine đã giao, không độn).

## Quyết định của user (22/11/2026)
- **Q1: «Giữ nguyên hook»** — hook C′ không đổi (R1/R2 vòng 2 được dặn không đề xuất sửa hook; lỗi an toàn/chính sách trong hook chỉ ghi nhận). Hệ quả: `four of them are easy` vẫn được giữ nhờ `PROMISE_OK: easy`; chữ «Free» và «A month» ở hook giữ nguyên.
- **Q2:** user không đề nghị đổi title → **giữ Title A** (khuyến nghị của orchestrator). R3 đóng gói không chạy lại ở vòng 2 (title, chữ thumbnail và 60 s đầu không đổi).
