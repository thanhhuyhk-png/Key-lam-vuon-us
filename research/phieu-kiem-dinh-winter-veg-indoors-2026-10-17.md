# Phiếu kiểm định — "Rau mùa đông trồng trong nhà" (2026-10-17)

Verdict: **GO CÓ ĐIỀU KIỆN** (bằng chứng yếu ở C1, C4, C7). Chưa vào pipeline. Lane A, nhãn **thăm dò** (góc mới). Số dư vidIQ cuối Vòng B: 30 credit.

## Gói chọn (cặp 1)
- Tiêu đề: `Winter Windowsill Garden: 5 Veggies That Work, 3 That Don't` (59 ký tự)
- Thumbnail: cửa sổ, 1 chậu xanh ✅ và 1 chậu héo ❌, chữ vàng ALL CAPS.
- Chưa chấm `score_title` (đang giữ credit).
- Dự phòng: `Grow Vegetables Indoors This Winter? Start With These 5` (55) · `7 Veggies You Can Grow Indoors This Winter (Plus 3 That Fail)` (61)

## Vòng A (đã chạy)
| Cổng | Kết quả |
|---|---|
| C2 | **Vàng**: khung "N winter veggies indoors" có ≥3 kênh hit cùng mùa năm ngoái. Góc "N ra rau + N hỏng" chưa thấy ai dùng trong mẫu. |
| C3 | Qua. Họ nói "dễ, không cần nhà kính". Mình nói: cửa sổ mùa đông không đủ cho nhiều loại, vì số giờ sáng theo extension. |
| C6 | Xanh/Biên. Không vùng đỏ. Phần riêng: bảng loại rau × giờ sáng × ngày thu hoạch. Kiếm tiền `[CHƯA ĐO]`. |
| C0 | 3 cặp viết xong, chưa chấm điểm. |

## Vòng B
**C1 (mẫu 67 video, chỉ 9 dùng được):**
- Cảnh báo của script: trung vị OM = 3,49 (mẫu thiếu video trượt) và còn 9 video dùng được.
- 32 video không có OM, 22 video thuộc kênh siêu nhỏ bị loại. → `p_thang = null`, không dùng cho verdict.
- THR tham khảo 0,82 là vô nghĩa vì mẫu thiên lệch.
- Độ lặp lại 5 kênh (≥3, Xanh nhưng mẫu thiên lệch).
- Đà tăng 0,28 (Đỏ về số, nhưng video ≤90 ngày là trái mùa, nên chỉ là tín hiệu phụ).
- Bão hòa: 3 kênh/90 ngày, biến động OM −33% → Vàng.
- Dự báo tham khảo 30 ngày: P25 973 · P50 1.825 · P75 3.300 (trung vị kênh 523). Không ghi vào sổ dự báo.
- File mẫu: `research/mau-c1-winter-veg-indoors-2026-10-17.json`.

**C7 video mồi: Biên.**
- Sunnyside Soil, *9 Vegetables You Can Actually Grow Indoors This Winter*: 536K view, 57,9K sub, OM 39,8, VPH hiện tại 799.
- Backyard Crops 281K, VPH 74.
- SereneGreen 148K, VPH 3,6.
- `vidiq_trending_videos` trả rỗng. Kênh nhỏ có xuất hiện cạnh các video này không: `[CHƯA ĐO]`.

**C4 chất liệu: Biên, chưa đạt.**
- Kết quả tìm kiếm từ extension (UMD, UIUC, UMN, MU), chưa mở trang nào:
  - Cửa sổ mùa đông thường không đủ cho rau lá và thảo mộc.
  - Rau lá và thảo mộc cần 6–8 giờ sáng mạnh mỗi ngày.
  - Dùng đèn bổ sung thì 14–16 giờ/ngày (nguồn hướng dẫn cây giống).
  - Cà chua cần ≥10 giờ nắng ngoài trời.
  - Quy tắc "2 giờ đèn cho mỗi giờ sáng tự nhiên" chỉ có ở một bài blog UIUC năm 2017, cần kiểm lại.
- Phần lớn nguồn viết về cây giống và microgreens, thiếu nguồn cho cây trưởng thành trong nhà. Cần hedge.

**C5 hình ảnh: `[CHƯA ĐẾM]`.** Chi phí sản xuất ước tính 2.

## Cập nhật đo bổ sung (cùng ngày) — số dư cuối: 25 credit
- **Điểm tiêu đề (cặp 1):** `vidiq_score_title` = **86**. Chưa có điểm các tiêu đề thắng cùng chủ đề để so, nên C0 vẫn là Xanh chưa đối chiếu.
- **Nguồn đã mở trang:**
  - UIUC Extension (2017): rau xà lách và thảo mộc cần 6–8 giờ sáng mạnh/ngày; cửa sổ hướng nam tốt; đèn bổ sung 2 bóng huỳnh quang 40W đặt cao 6–12 inch, 14–16 giờ/ngày; ~2 giờ đèn cho mỗi giờ sáng tự nhiên; phòng ≤70°F; xà lách lá rời ~4 tuần.
  - UMD Extension (microgreens và baby greens): tổng ánh sáng khoảng 16 giờ/ngày; "cửa sổ nắng có thể đủ trong một số trường hợp", nhưng microgreens lớn tốt nhất dưới đèn; đèn cách tán lá 6–12 inch; xà lách, arugula, cải mù tạt, cải châu Á chịu thiếu sáng khá tốt; microgreens 7–21 ngày, baby greens 21–40 ngày, rau trưởng thành 40–60 ngày.
  - UNH Extension (hỏi đáp chiếu sáng): cửa sổ chỉ đủ cho hạt cần sáng để nảy mầm, cây con vươn dài khi thiếu sáng; đèn cách ngọn 4–6 inch; cà chua cần ~6 giờ tối để đậu quả, ớt không.
  - UNH và UMD là nguồn hạng A theo hồ sơ. Missouri Extension lỗi 403, chưa đọc được.
- **Chưa xác minh:** câu "rau ra quả (cà chua, ớt) cần đèn bổ sung vào mùa đông" mới chỉ có trong tóm tắt kết quả tìm kiếm; trang UNH đã mở **không** nói điều đó. Vậy phần "3 loại hỏng" chưa có nguồn đã mở.
- **Ảnh hưởng đến góc:** UMD nói cửa sổ nắng "có thể đủ trong một số trường hợp", nên không được khẳng định "cửa sổ không bao giờ đủ". Phần "5 loại ra rau" có nguồn tốt (xà lách, arugula, cải, microgreens, thảo mộc). Phần "3 loại hỏng" cần thêm 1 nguồn extension nói thẳng về cà chua/ớt trong nhà.

## Cập nhật nguồn cà chua/ớt (cùng ngày) — đã mở trang
- **UNH Cooperative Extension, "Chapter 10: Planting Vegetables"** (Otho Wells hiệu đính, PDF `extension.unh.edu/sites/default/files/migrated_unmanaged_files/Resource003548_Rep5077.pdf`, mục *Indoor container gardening with vegetables*, trang 27–28; năm xuất bản chưa rõ, nguồn cũ):
  - Cửa sổ nắng, tốt nhất hướng nam, "gần như bắt buộc" khi trồng rau trong nhà.
  - Rau ra quả như cà chua và ớt "cũng cần ánh sáng bổ sung" (ví dụ đèn huỳnh quang trắng ấm + trắng lạnh) vào các tháng mùa đông. Thiếu sáng thì cây cao gầy, không ra hoa, không đậu quả.
  - Cà chua quả nhỏ (Tiny Tim, Small Fry, Roma) và một số ớt quả nhỏ trồng được trong nhà. Thu hoạch khoảng 10 tuần sau khi trồng. Rệp và bọ phấn trắng có thể gây hại.
  - Rau xà lách (leaf lettuce, Tom Thumb) cần chỗ "rất nắng". Củ cải ra nhanh. Củ cà rốt giống nhỏ trồng được. Hẹ ~12 tuần, mùi tây 10–12 tuần mới cắt. Giá đỗ 3–5 ngày.
- Clemson HGIC (trang cà chua): chỉ nói về cây con ("cần đèn bổ sung trừ khi ở cửa sổ nắng hướng nam"), không nói về cà chua trưởng thành trong nhà. Không dùng làm nguồn chính.
- Con số "8 giờ nắng đầy đủ, tốt hơn là 10–12 giờ cho rau ra quả" nằm trong cùng chương UNH, nhưng ở phần trồng ngoài trời. Đừng dùng làm số cho trong nhà.
- Không tìm được nguồn extension thứ hai nói thẳng về cà chua/ớt trong nhà. Nguồn blog/bán lẻ (AOL, Sandia Seed, Burpee) không đủ hạng.
- **Hệ quả cho góc:** "3 loại hỏng" là sai khung. Nguồn nói cà chua nhỏ và ớt nhỏ **trồng được nhưng cần đèn bổ sung + khoảng 10 tuần**. Góc đúng là "5 loại ra rau trên cửa sổ nắng, 3 loại cần thêm đèn" chứ không phải "3 loại không mọc". Cần đổi tiêu đề.

## Điều kiện để thành GO
1. Mở và xác minh nguồn extension ở bước research (≥2 con số mỗi loại rau).
2. Danh sách 5+3 loại rau chỉ chốt sau khi có số giờ sáng thật.
3. Tránh khung đối thủ: "Actually Grow", "No Greenhouse Needed", "7 Winter Veggies INDOORS".
4. Đăng sớm: 3 hit năm ngoái đều đăng từ 20/10 đến 22/12.
5. Kỳ vọng thực tế: không có video cùng góc đã chứng minh. Sống nhờ Browse, giống bài lemon.
