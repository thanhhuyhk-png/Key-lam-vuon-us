# Phiếu kiểm định — Giâm hồng bằng khoai tây — 2026-10-24

**Verdict: SỬA GÓC (vòng 1/2).** Chủ đề có cầu thật (C1 Xanh), nhưng **khung mình định dùng (hoài nghi/verdict) chưa có bằng chứng ăn view**, còn khung đã thắng là khung "tin mẹo" mà kênh không dùng được. Vòng A (24/10): C2 Vàng · C3 Xanh–Vàng · C6 Xanh · C0 Xanh. Vòng B: C1 chủ đề **Xanh**, C1 khung **Đỏ** · C7 Vàng · C4 Xanh–Biên · C5 Biên.
vidIQ tk3: 420 → 390 (Vòng B tiêu 30, đúng trần). Dữ liệu thô: `research/san-y-tuong-2026-10-24/` (`mau-c1-rose-potato-v2.json`, `r*-raw.json`).

## C1 — Chỉ số cầu
- Mẫu: 68 video long-form 4–20 phút, kênh <180K sub (3× kênh mình), 12 tháng, 3 truy vấn vidIQ. Dùng được **42** (loại 16 không OM, 8 kênh siêu nhỏ, 2 chưa đủ tuổi) → độ tin **cao**.
- ⚠️ Bản chưa bù cho `chi_so.py` báo "mẫu thiếu video trượt" (trung vị OM 2,34). Tôi ước tính OM cho **11 video** có OM null nhưng cùng kênh có ≥2 video đã có OM (view ÷ view điển hình kênh); sau đó trung vị OM = 1,82, hết cảnh báo. 11/42 là số ước tính.
- THR (OM ≥1,5) **0,614** · breakout (OM ≥2) 0,432 · độ lặp lại **7 kênh** · đà tăng **0,89** · bão hoà: 2 kênh/90 ngày, biến động OM +43%.
- Dự báo (mốc 597): P25 **622** · P50 **1.085** · P75 **2.863**; ngưỡng thắng ≈ 900. P(thắng) tham khảo 0,61; EV 878. **Chỉ áp cho khung "tin mẹo"** (xem dưới).
- Video nổ của họ mẹo này đều là khung tin: "Just Rice!…" 1,2M (OM 293), "Grow 1,000 Rose Plants in 7 Days" 1,7M (OM 1.208), "Just An Onion!" 1,6M (OM 266), "Just Rice!" 669K, "Stop Throwing Away Roses! Use the POTATO TRICK for 100% SUCCESS" 391K (OM 130). Chúng đến từ các kênh 70K–116K sub đăng hàng loạt, cùng khuôn "Just X! … Roots Grow Overnight". Hầu hết video khoai tây khác chỉ 1–10K (OM ≈ 1,0–1,3).
- ❌ **Khung của mình (hoài nghi/verdict): 0 video OM ≥2.** Bốn bản hoài nghi trong mẫu: Telugu 225 · Bồ Đào Nha 56 · "The Rose in Potato Hack: Why It Fails" 11 · "…Actually Works?" 1,4K. Đều là kênh nhỏ/nước ngoài → **chưa có bằng chứng**, không phải bằng chứng thất bại.
- Khung tin mẹo vi phạm giọng kênh (quá lời: "900%", "1001 roots", "100% success") → không dùng.

## C2 — Bão hoà: Vàng
≥7 kênh (70K–312K sub) đăng khuôn "tin mẹo" liên tục (rice, potato, onion, garlic, banana…); nhưng khung hoài nghi/có nguồn còn trống. Nội bộ: 0 video về giâm hồng bằng mẹo (remake-002 là mẹo hoa nở, khác).

## C7 — Video mồi: Vàng
- `rose cuttings potato` (US) **<750/tháng**, nhưng `rose cuttings` **3.312/tháng (Medium)**, `how to grow rose` 6.025 (+81%), `gardening hacks` 50.569 (+125%).
- 3 video có VPH cao hiện nay (Dream Rose, 70–91K sub): 22,4K (VPH 149) · 9,8K (148) · 6,0K (101). Không đo được kênh nhỏ có nằm cạnh chúng trong đề xuất hay không → `[CHƯA ĐO]`.

## C4 — Chất liệu: Xanh–Biên (đã mở thật 4 nguồn)
1. **Wali, Shafiqi & Ahmadi (2019), *Int. J. of Innovative Research and Scientific Studies* 2(4):55–61** — *chỉ đọc được phần tóm tắt* (RePEc): thử cành hồng bán hóa gỗ 3 tháng tuổi, dài 15/20/25 cm, 1/2/3 mắt, **cắm khoai tây vs cắm đất**, thí nghiệm lặp 2 lần. Lần 2: cành trong đất mọc rễ phần lớn; cành trong khoai tây **nảy chồi nhưng không cành nào ra rễ**. Lần 1 không cành nào ra rễ. Cành 15 cm 2 mắt khác biệt ý nghĩa. Tóm tắt không nêu %, không nêu kiểm định cho so sánh khoai–đất. Số lượng cành chưa biết.
2. **UC Master Gardeners (Tulare–Kings) "Propagating Roses by Cuttings"** (PDF 2 trang): nhúng đầu vát vào nước rồi bột kích rễ (vd Rootone), cắm ~½ chiều dài, giữ ẩm không ướt; **làm ít nhất 3–4 cành mỗi giống vì không phải cành nào cũng ra rễ**; tác giả có **60–70%** khi cắm thẳng vào đất vườn (kinh nghiệm một người, không phải thí nghiệm).
3. **Iowa State Extension "How to Propagate Roses"**: cành bán hóa gỗ lấy tháng 7–8 ("cách dễ nhất"); cành hóa gỗ lấy từ gỗ năm trước, cuối đông khi cây ngủ. **Không nhắc khoai tây**; nhiều chi tiết (dài, giá thể, thời gian ra rễ) "không nêu" (trang dẫn sang bài khác).
4. **Ohio State Extension "Garden Myths & Legends" (Eric Barrett, bài thuyết trình)**: câu hỏi "Can I start a rose in a potato?" và giải thích **cơ chế**: giữ ẩm chỗ cắt, đường từ lá/thân đọng ở vết cắt khởi động mô sẹo, rễ rồi tìm giá thể ẩm để mọc. **Đây là một slide giải thích cơ chế, không phải kết luận "huyền thoại" hay "đúng".**
⚠️ **Đính chính phiếu 24/10:** tôi đã viết ở phiếu trước rằng các nguồn extension "đều nghi ngờ phương pháp này". Điều đó **quá lời**: câu "chưa thấy kết quả tốt" của blog UC chỉ thấy ở đoạn tìm kiếm (trang bị 403, chưa đọc), và slide Ohio State chỉ giải thích cơ chế. Chứng cứ thật hiện có là **một nghiên cứu nhỏ (tóm tắt)** + **hướng dẫn chuẩn dùng giá thể ẩm, bột kích rễ, nhiều cành**.
→ **Không dùng "What Universities Actually Say" làm tiêu đề** (L17: lời hứa tiêu đề phải khớp nguồn).
Bị chặn: UC Cooperative Extension blog (403), academia.edu (403). Thiếu: tỷ lệ ra rễ của cành trong khoai tây (số cụ thể), thử nghiệm của extension, thời gian ra rễ.

## C5 — Hình ảnh: Biên
`garden_lib.py find`: **rose 0 · potato 0 · cuttings 0 · knife 0 · pruning 0**; cutting 7 (rau/thảo mộc), pot 40, hands 29, soil 14, stem 7, scissors 6. Cảnh then chốt (cành hồng, hoa hồng, khoai tây, cắm cành) phải tải/tạo mới. Chi phí 2.

## C3 / C6 / C0
- **C3:** "Video đã có nói *cắm hồng vào khoai tây thì rễ mọc qua đêm*. Mình nói *một nghiên cứu có đối chứng thấy cành trong khoai tây không ra rễ* và *cách giâm hồng thực sự dùng*." Z là bằng chứng nghiên cứu. Xanh–Vàng vì mới có tóm tắt.
- **C6:** Không vùng đỏ. Phần phân tích riêng: đặt cơ chế (Ohio State) cạnh kết quả thí nghiệm (Wali 2019) cạnh hướng dẫn chuẩn (UC, Iowa State). Xanh.
- **C0 (vidIQ):** 87: `Rose Cuttings in a Potato? One Study Found No Roots` (51 ký tự, lời hứa khớp nguồn) · 85: `Rose Cuttings in a Potato? What Universities Actually Say` (✗ quá lời) · 84: `Rose Cuttings: Skip the Potato, Do This Instead` (47).

## SỬA GÓC — đề xuất (≥2) để chạy lại Vòng A
1. **Giữ khung hoài nghi nhưng nhét số cụ thể vào tiêu đề** (khung thua đã thất bại vì mơ hồ, không có sự kiện): `Rose Cuttings in a Potato? One Study Found No Roots` + 1 phút đầu đưa kết quả thí nghiệm. Phép thử: nếu CTR giờ 48 <4% thì đổi. Chưa có bằng chứng khung này ăn view → nhãn **thăm dò**.
2. **Chuyển sang khung "giâm hồng thật sự hiệu quả"** (đổi trục nghịch lý): `How to Root Rose Cuttings: Hardwood Cuttings This Winter` — khung how-to đã có kết quả (Iowa State: hardwood cuttings cuối đông) nhưng bằng chứng view khung này trong mẫu chỉ ở mức vừa (1,4K OM 2,3; 15,5K OM 1,2; 280K nhưng kênh 1,29M sub). Chất liệu mỏng (Iowa State nhiều mục "không nêu").
3. Không nên: khung "Just X! Roses Grow Roots Overnight" (khung thắng nhưng vi phạm giọng/quá lời).

## Điều kiện để GO
Đọc được toàn văn Wali 2019 (số cành, %); thêm 1–2 trang extension về giâm hồng hóa gỗ mở được (Iowa State bài chi tiết, Clemson HGIC, MSU…); kiểm khung hoài nghi: mở trang video của 2–3 video mồi để xem có kênh nhỏ ăn theo hay không; giãn lịch ≥2–3 tuần sau video geranium.

*Chưa ghi `du-bao.csv` (chỉ ghi khi GO).*


---
## Vòng A lại — góc "Rose Cuttings in a Potato? One Small Study Found No Roots" (24/10, vòng sửa 2/2)
vidIQ tk3: 390 → 380 (tiêu 10, chấm 2 tiêu đề). Kết quả: **Vòng A QUA (Xanh ×4). Còn một điều kiện cầu chưa đo được → GO có điều kiện, nhãn THĂM DÒ.**

### Đã đọc toàn văn Wali, Shafiqi & Ahmadi (2019), IJIRSS 2(4):55–61
Nguồn: ijirss.com (PDF). Điều đọc được, và **những chỗ nó yếu** (phải nói thẳng trong video):
- Địa điểm: Khost, Afghanistan, 900 m, Khoa Nông nghiệp Đại học Shaikh Zayed. Thí nghiệm 1: cành lấy từ vườn hồng ở 2.500 m (Paktya), trồng ngày 15/5/2017 (tóm tắt ghi 2016; không khớp). Thí nghiệm 2: 15/3/2018.
- Thiết kế: 3 lần lặp; 9 tổ hợp (cành dài 15/20/25 cm × 1/2/3 mắt); **số cành mỗi nghiệm thức không ghi** (tổng ANOVA 108 cành suy ra ~12). Văn bản nói 8 khối, ANOVA chỉ 4 khối; **Bảng 1 gắn nhãn "có khoai tây" cho cả 9 nghiệm thức, mâu thuẫn với văn bản** (4 khối có khoai, 4 không). Cách chuẩn bị khoai (giống, cách cắm) **không mô tả**.
- Kết quả: TN1 **không cành nào ra rễ**. TN2: cành trong **đất** — "phần lớn" nảy chồi và ra rễ; cành trong **khoai tây** — **không nảy chồi và không ra rễ** (toàn văn) — *khác với phần tóm tắt, vốn nói "nảy chồi nhưng không ra rễ"*. **Không có tỷ lệ % và không có kiểm định thống kê cho khoai tây vs đất**; ý nghĩa thống kê (p<0,001; p=0,0094; p=0,0222) chỉ cho số mắt và độ dài cành. Hệ số biến thiên rất lớn (84% chiều dài chồi; 108% khối lượng rễ khô).
- Kết luận của tác giả: "khó khẳng định khoai tây có vai trò đáng kể trong việc tạo rễ" — họ **không chứng minh được giả thuyết rằng khoai tây giúp**; họ không chứng minh được rằng khoai tây làm hại. Cành 15 cm, 2 mắt tốt nhất.
- Tạp chí: IJIRSS (mở, không thuộc nhóm tạp chí uy tín cao) → trình bày là **"một nghiên cứu nhỏ"**, không phải "khoa học đã chứng minh".
→ Tiêu đề "One Small Study Found No Roots" **đúng với toàn văn** (khoai tây: không rễ), nhưng **không được kết luận "khoai tây không bao giờ có tác dụng"**.

### Hai trang extension giâm hồng mới mở được
1. **NC State Extension (Beaufort County) "How do I propagate roses from clippings?"**: lấy cành bất cứ lúc nào nhưng "tốt nhất tháng 11–2"; cành **6–8 inch** từ ngọn; chậu nhỏ, đất tơi, ẩm; dùng bột kích rễ (cạo xước 1 inch đáy trước khi nhúng); **trùm túi** giữ ẩm, **xịt nhẹ mỗi ngày**; để cành cả mùa rồi mới trồng bồn vào mùa thu năm sau; không nhắc khoai tây; không có số tuần ra rễ.
2. **Iowa State Extension "Propagation of Deciduous Trees and Shrubs from Semi-Hardwood Cuttings"**: cành **4–6 inch**, lấy **giữa tháng 7 đến đầu thu**; cắt dưới nút; bột kích rễ khuyến nghị nhưng không bắt buộc; giá thể cát thô/perlite/vermiculite có lỗ thoát nước; cắm **~2 inch**; trùm túi/nắp; sáng nhưng không nắng gắt; **6–8 tuần** (kiểm 2–3 cành sau 4–5 tuần); hồng nằm trong danh sách.
Cộng các nguồn đã mở ở Vòng B: Iowa State "How to Propagate Roses" (bán hóa gỗ tháng 7–8; hóa gỗ cuối đông), UC Master Gardeners (3–4 cành mỗi giống; 60–70% khi cắm đất vườn — kinh nghiệm một người), Ohio State slide (cơ chế giữ ẩm). Bị chặn: Missouri g6970 (403).
Lưu ý mùa vụ: hướng dẫn tháng 7–8 (Iowa) **và** tháng 11–2 (NC State) cho hai loại cành khác nhau; video đăng cuối tháng 10 nên phần "làm gì bây giờ" = cành hóa gỗ mùa đông.

### Các cổng Vòng A
| Cổng | Mức | Ghi chú |
|---|---|---|
| C2 | **Xanh** | Tìm "rose cutting potato study research tested university experiment" (NexLev, 12 tháng): 0 video có góc nghiên cứu/thí nghiệm có đối chứng cho khoai tây–hồng. Họ "mẹo" đã bão hoà nhưng góc có bằng chứng còn trống |
| C3 | **Xanh** | "Video đã có nói rễ mọc qua đêm. Mình nói *thí nghiệm có đối chứng duy nhất mình tìm được cho 0 rễ ở cành cắm khoai* (và vì sao nó chưa đủ kết luận) *cộng cách giâm hồng theo hai trang extension*." Z = nghiên cứu + extension |
| C6 | **Xanh** | Phần phân tích riêng: cơ chế (Ohio State) ↔ kết quả (Wali 2019 + điểm yếu của nó) ↔ hướng dẫn chuẩn (Iowa State, NC State, UC). Không vùng đỏ |
| C0 | **Xanh** | **88**: `Rose Cuttings in a Potato? One Small Study Found No Roots` (57) · 87: `…One Study Found No Roots` (51) · 91: `…What the Only Study Found` (52) **bị loại**: "the only study" là khẳng định tuyệt đối mà mình không chứng minh được |

### Phán quyết: **GO CÓ ĐIỀU KIỆN — THĂM DÒ** (ưu tiên sau video geranium)
- **Còn đỏ về cầu:** khung hoài nghi/có nguồn vẫn **0 video OM ≥2**. Mình chỉ thay đổi bằng cách đưa *một sự kiện cụ thể (0 rễ)* vào tiêu đề và dùng cụm "Rose Cuttings in a Potato" đã nổi. Chưa đo được tác dụng. Dự báo `P25 622 · P50 1.085 · P75 2.863` là **trần của họ mẹo**, không phải số của khung này.
- **Quy tắc dừng (khai trước):** views_5d <400 hoặc CTR giờ 48 <4% → bỏ khung hoài nghi cho chủ đề mẹo.
- **Thời điểm:** hóa gỗ mùa đông (11–2) → đăng giữa tháng 11, cách geranium ≥2–3 tuần.
- **Chất liệu:** đủ khoảng 10–14 phút (cơ chế · thí nghiệm · điểm yếu thí nghiệm · cách giâm hóa gỗ & bán hóa gỗ · 3–4 cành · sai lầm). Khung 20–24′ của kênh sẽ cần thêm nguồn hoặc chấp nhận bản ngắn (TEST độ dài).
- **Chưa ghi `du-bao.csv`** vì chưa có P(thắng) cho khung này; chỉ ghi khi bạn duyệt làm.
