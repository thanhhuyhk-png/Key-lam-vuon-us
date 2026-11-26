# Top 20 — Garden US (Senior Garden Guide) — đo ngày 2026-11-16 (BẢN NHÁP chờ phản biện)

## Khung (pha 0) — xem khung.md
Khán giả: người làm vườn tại nhà ở Mỹ, lõi 60–80, mục tiêu 35–60+. Định dạng làm được: không lộ mặt, giọng AI, 10–14′, hình = stock miễn phí + tư liệu công cộng + đồ hoạ code; KHÔNG tự quay, KHÔNG stock trả phí. Nguồn lực: 1 người + Claude, ~2 video dài/tuần. Ràng buộc nội dung của mình: an toàn quảng cáo, không giọng sợ hãi lệch ngách (L8), không lời khuyên y tế.

## Dữ liệu (pha 1–2) [ĐO]
- 97 kênh khảo sát (ytsearch 26 truy vấn + NexLev 39 kênh). 97/97 thu được video bằng yt-dlp (6 kênh phải thu lại do bot-check). Sub: 95/97 (2 kênh ẩn sub: Blackout Basics, Wonders → Theo dõi).
- Kiểm tay 4 số view với trang gốc: lệch 0 %, 0 %, 0 %, 0,24 % (≤ 3 % → đạt).
- Cờ NGHI_LOI_DON_VI ở The Green Archive: báo nhầm (view từ metadata đầy đủ khớp trang gốc 36.687).
- Nhóm «mới < 365 ngày từ video đầu»: 45/97 kênh.
- Chưa có sub 30 ngày trước (lần đo đầu) → bộ «đà» không xếp được kênh nào; độ nhạy chỉ có 5 cách hợp lệ.

## Lọc sơ bộ (5.1) — loc-so-bo.tsv
Giữ 61 · Loại 27 · Theo dõi 9. Lý do loại chính: người dẫn lên hình / quay thật (14 kênh, phần lớn [SUY LUẬN từ tiêu đề], 2 kênh [ĐO bằng storyboard]: Survival Kitchen 1930 quay tay thật, The Good Steward có người dẫn nữ); lệch hướng (tài chính, Roblox, chính trị, săn bắn); lõi kịch bản sụp đổ/cướp bóc (Collapse Theory, Mr prepper).
- Lưu ý: Survival Kitchen 1930 là hạng 1 ở 5/5 cách khi còn trong tập Giữ (trung vị 269.712, trung vị/sub 1,39, 77 video, 194K sub) — bị loại vì nguồn lực, không vì số.

## Xếp hạng tập Giữ (xep-hang.md, --do-nhay) [ĐO]
TOP 20: xem top20.tsv. Độ nhạy: Forgotten American Survival hạng 1 ở 3/5 cách; No Longer Here 1/5 (hạng 1 ở «tích luỹ»); Forgotten Old American 1/5 (hạng 1 ở «chỉ trung vị tuyệt đối»). → KHÔNG đủ 5/6 → trình ≥ 2 ứng viên.

## Ứng viên Model Link (pha 6)
| | Forgotten American Survival (FAS) | No Longer Here (NLH) |
|---|---|---|
| Hạng / khoảng hạng / hạng 1 ở | 1 / 1–5 / 3 trên 5 cách | 4 / 1–4 / 1 trên 5 cách |
| Sub · trung vị 20 video dài · đà trung vị | 119.000 · 9.126 · 2,09 | 238.000 · 21.818 · 0,99 |
| Video 30 ngày · thời lượng trung vị | 23 · 30′ | 26 · 31′ |
| Tuổi kênh (từ video đầu) | 238 ngày | 468 ngày (video đầu 2025-08, khoảng trống tới 2026-08) |
| Trung vị theo tháng 2026 | Th4 113K (n5) → Th7 16,7K → Th8 5,9K → Th9 7,8K → Th10 8,5K | Th8 9,1K → Th9 11,5K → Th10 18,9K |
| Hình [ĐO storyboard 1 video] | stock + ảnh lưu trữ đen trắng + thẻ chữ code | stock + ảnh minh hoạ |
| Đề tài nhóm thắng (20 % đầu) | mẹo «Poor Man» cúp điện, đồ Walmart/Costco/Tractor Supply trữ trước cúp điện | cây ăn quả/cây cũ bà trồng (2,66M), đồ Tractor Supply/Dollar Tree mùa đông, đồ cổ 1950s |
| Đề tài nhóm thua | an ninh nhà, phòng an toàn, thoát lũ, chiến tranh lạnh | mẹo vườn thời chiến/ông bà, kiểm soát sâu 1950s |
| Tuổi khán giả (mẫu bình luận, đọc tay) | ~5 nhãn chắc (55–76), Thấp | ~8 nhãn chắc (41, 65, 69, 71, ~77–80), Vừa; có bình luận chê «hokey AI voice» |
| Rủi ro ràng buộc | đề tài sợ hãi (home defense, safe room) gần L8 | trộn nhiều ngách (vườn, sinh tồn, đồ cổ) |

Loại khỏi ứng viên: Homestead Roots (hạng 2 đồng) — lõi «… Will Heal You Instantly» vi phạm ràng buộc y tế; Agriculture Insight (hạng 2 đồng) — dùng clip của người khác (Ronaldo), video 50′, đề tài nông nghiệp vĩ mô lệch khán giả; Forgotten Old American (hạng 5) — clip TV người nổi tiếng (rủi ro bản quyền).

Đề xuất sơ bộ của phiên chính: NLH làm Model Link (khoảng hạng hẹp hơn 1–4, đà tháng đang lên, video đỉnh là đề tài làm vườn, tuổi khớp ở mức Vừa), FAS làm ứng viên 2 cho mảng «tự cung tự cấp / cúp điện thực dụng». Cả hai đăng ~1 video/ngày, 30′ — vượt nguồn lực 2 video/tuần → bám cách chọn đề tài + cách dựng, KHÔNG bám nhịp và độ dài.

## Câu bắt buộc (luật thép 3)
«Kênh ít video mà sub nhiều, video dài, view tốt?» — cột it_video_sub_nhieu = Có: Survival Kitchen 1930 (77 video, 194K sub, trung vị 269.712; loại vì quay thật), The Good Steward (44 video, 186K sub, trung vị 159.898; loại vì người dẫn lên hình), Survival Blueprint (25 video, 16.200 sub, 31′, trung vị 8.313) — hạng 10, không hạng 1 vì đà trung vị 0,04 (video gần đây chỉ bằng 4 % trung vị) và phân tán 57.

## Kho video vượt trội (kho-vuot-troi.tsv): 326 video hệ số ≥ 3 trong TOP 20. Đề tài làm vườn nổi bật: NLH cây bà trồng (954×), Living Self-Sufficiently mẹo nhổ cỏ/giâm cành (677–694×), Backyard Bill xương rồng Giáng sinh tháng 10 (490×), Plant Explainer «N rau trồng tháng X» (4 video 138–426×).

## Giới hạn
Storyboard chỉ 1 video/kênh; tuổi đo trên 2 video/kênh; «cùng nguồn lực» ở 14 kênh loại là suy luận từ tiêu đề; chưa có vidIQ (0 credit dùng); mốc sub 30 ngày trước chưa có.
