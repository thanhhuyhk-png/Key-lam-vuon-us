# Shot Plan — [video slug]

> Tạo cùng lúc với script. Mỗi nhịp lời nói có 1 dòng hình. Quy tắc: **hình không được chứng minh điều script không chứng minh** và **không mâu thuẫn con số trong lời nói**.

## 4 tầng hình
| Mã | Tầng | Dùng cho | Không dùng cho |
|---|---|---|---|
| **S** | Stock thật (Pexels/Pixabay) | Không khí, cây, bệ cửa sổ, tay làm việc đơn giản | Minh họa con số cụ thể (ngày, inch, giờ); cảnh nhà kính/thủy canh khi script nói "bệ cửa sổ"; kết quả "đã thử" |
| **G** | Đồ họa tự dựng | Bảng đối chiếu, thẻ nguồn 2 dòng, sơ đồ khoảng cách đèn, lịch 4 tuần, bộ đếm "3/7" | — (đây là phần giá trị gốc của kênh) |
| **A** | Ảnh AI | Cảnh khó quay: cây vươn dài so với cây khỏe, bệ cửa sổ mùa đông có nắng yếu, sơ đồ minh họa | Chữ trong ảnh (chèn chữ bằng phần mềm dựng), thương hiệu, bàn tay làm thao tác chính xác, "kết quả" nghe như thật |
| **V** | Clip AI (Veo hoặc tương đương) | Macro cây chuyển động chậm, ánh sáng đổi trong ngày (minh họa) | Time-lapse "chứng minh" số ngày; bất kỳ cảnh nào dễ bị hiểu là ghi hình thật của kênh |

## Quy tắc chung
1. **Stock trước, AI sau.** Chỉ chuyển sang A/V khi tìm stock ≥3 lần với cụm khác nhau không ra clip đúng cây, đúng bối cảnh.
2. **Không gắn nhãn chữ "illustration" lên hình** (user quyết 01/11/2026). Vì không có nhãn, A/V không được thể hiện "kết quả đã xảy ra"; khi đăng, xét khai báo **altered or synthetic content** trong YouTube Studio nếu hình AI trông như quay thật.
3. **Con số trên hình = con số trong script.** Không để clip time-lapse chạy 3 ngày khi lời nói "7–21 ngày".
4. **Không dùng lại clip** trong 3 video gần nhất (sổ duy nhất: cột `used_in` trong `_LIBRARY/catalog.csv`); ưu tiên clip ít phổ biến, cắt/ghép/chỉnh màu.
5. **Style bible cho A/V** (giữ nhất quán): cùng bệ cửa sổ, ánh sáng, loại cây; 16:9; ghi seed/ảnh tham chiếu.
6. **Thẻ nguồn (G)** cho mọi claim chính: 2 dòng, "[Cơ quan], [tên tài liệu], [năm]".
7. **Giấy phép (đã kiểm trang tóm tắt 17/10/2026):** Pexels và Pixabay đều cho dùng, không bắt buộc ghi nguồn, được chỉnh sửa; cấm bán nguyên bản/standalone, cấm gợi ý người/thương hiệu trong hình ủng hộ mình, cấm dùng gây hiểu lầm. Điều khoản đầy đủ của từng trang mới có giá trị pháp lý.

## Bảng shot
| ID | Mốc | Lời nói (câu đầu) | Loại | Mô tả hình / cụm tìm stock / prompt AI | Chữ & thẻ nguồn | Dự phòng | Trạng thái |
|---|---|---|---|---|---|---|---|

## Kiểm cuối
- [ ] Mỗi mục trong script có hình; không có đoạn >8 giây không đổi hình trong phần montage; phần giải thích dài (bảng) có hình G.
- [ ] Không clip nào mâu thuẫn con số trong lời nói.
- [ ] Không hình A/V nào thể hiện kết quả như đã xảy ra; đã quyết định khai báo synthetic trong Studio.
- [ ] Đã cập nhật `used_in` trong catalog.
