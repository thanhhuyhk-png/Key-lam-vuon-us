---
name: garden-video-map
description: Lập bản đồ hình theo lời đọc cho video Garden US (video-map.json), tìm và chọn stock đúng nghĩa bằng ảnh tổng hợp, xuất prompt clip AI cho user tự render. USE WHEN user nói "lập bản đồ hình", "tìm footage cho video", "prompt clip AI", "chuẩn bị dựng video", sau khi script.md đã duyệt ở GATE [3]. Trạng thái TEST từ 01/11/2026, pilot trên big-idea-093.
---

# Garden Video Map

Đầu vào: `scripts/<video>/script.md` đã duyệt. Không sửa lời đọc.

1. **Lập `video-map.json`** theo schema trong docstring của `tools/garden_map.py`. Mỗi cảnh có câu mở nguyên văn và `show` (hình bắt buộc thấy). **Ban đầu gán mọi cảnh quay được là S; chỉ chuyển sang V sau khi đã tìm ≥3 cụm từ và nhìn ảnh tổng hợp không ra clip đúng nghĩa.** Pilot 093 gán V trước nên ra 31 prompt, tìm lại chỉ cần 9. Đọc `retention-spine.md` và "Ghi chú sản xuất" của script: thẻ đồ họa, thẻ nguồn, những gì script cố ý không nói cũng không được hiện trên hình.
2. **Kiểm:** `python tools/garden_map.py check <map>`. Mục tiêu theo thời lượng: stock ≥50%, AI ≤35%, đồ họa ≤10%.
3. **Tìm ứng viên:** `python tools/footage_pick.py search <map> --sheets <scratchpad> --exclude <3 video gần nhất> --env "D:/0008. Key Quân sự/.env"`. Pexels giới hạn khoảng 200 lượt/giờ.
4. **Nhìn từng ảnh tổng hợp rồi chọn.** Số kết quả tìm kiếm không phải bằng chứng. Không có clip đúng `show` thì đổi cảnh sang V hoặc G, không dùng hình gần đúng. Số hiện trong clip phải khớp lời đọc. Ghi `footage/picks.json`.
5. **Tải:** `python tools/footage_pick.py fetch <map>`. Clip vào `_LIBRARY/_inbox/<mã>/`; xong video chạy `garden_lib.py ingest` và cập nhật `used_in`.
6. **Prompt:** `python tools/garden_map.py prompts <map>` tạo `ai-clip-prompts.md`. User tự render và trả file về `_LIBRARY/_inbox/<mã>/ai/`.

Luật hình AI: không chữ, không logo, không mặt; không thể hiện kết quả như đã xảy ra; không gắn nhãn "illustration" trên hình (`channel.config.json` → `visual_rules`).
