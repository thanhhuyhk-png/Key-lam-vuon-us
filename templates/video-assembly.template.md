# Template dựng video Garden US (chốt 18/10/2026 từ bài 062 bản v3b `G062v3b_auto`)

Quy trình từ voice đến draft CapCut. Mỗi video mới: copy cấu hình `scripts/big-idea-062-.../footage/v3/shotlist_cfg_062v3.py` làm mẫu.

## 1. Đầu vào
- `voice/<v>/voice.mp3` + `voice.srt` (giọng Key gardent, `tools/ai33_voice.py`; text có dấu ngắt `<#0.7#>`, `<#1.0#>` giữa đoạn).
- Footage lấy từ `_LIBRARY` (tìm bằng `tools/garden_lib.py find`); tải mới → `_LIBRARY/_inbox/<mã>/{pexels,photos,ai,gfx}`, xong chạy `garden_lib.py ingest`.

## 2. Shotlist (`tools/garden_shotlist.py <srt> <cfg>`)
- Nhịp cắt: 0–1′ avg ≤2,2s max 3,0s · 1–3′ avg ≤3,0s max 4,0s · sau 3′ avg ≤3,5s max 4,0s; clip stock <4s; nguồn ≤3 lần, không lặp trong 60s; hình thật >70%.
- **Thẻ đồ họa (kiểu bảng phấn) gắn theo lời đọc**, KHÔNG chèn định kỳ: `GRAPHIC_TRIGGERS = [(cụm nói, mã thẻ, giây tối thiểu)]`; mỗi thẻ ≥9s (bảng/so sánh 13–17s, kế hoạch ~20s), cách nhau ≥7s. Thẻ cũ hiện 2–4s liên tiếp bị user chê.
- **Chữ**: ít, chỉ từ khóa chính/phụ theo nội dung (`OVERLAYS` + `OVERLAY_GAP`: cùng một chữ không lặp trong 90–300s; nhãn nguồn ≤1 lần/5 phút, hiện 4s; KHÔNG nhãn "New Hampshire"); không chữ lấp chỗ trống (`BREAK_FILL=False`, `MIN_EVENTS=0`).
- Thẻ chalk: `tools/garden_gfx_chalk.py <outdir> --user-dir <ảnh mẫu user>` (font Ink Free, khung đen, bảng xanh). Ảnh user vẽ dùng nguyên; chữ trên thẻ phải khớp title (L17: không "easy" nếu title không có).

## 3. Draft CapCut (`tools/garden_build_capcut.py --v3 --name <tên>`; CapCut ĐÓNG)
- Hàng chữ: A (số/stamp lớn, Impact vàng) · B (chữ phụ, tự dịch vào trong khung theo độ dài) · SRC (nhãn nguồn). Từ 01/11/2026 không gắn nhãn "ILLUSTRATION" trên hình AI. Thẻ đếm = PNG.
- **SFX gắn mọi hiệu ứng chữ** (track "SFX TEXT"): A/stamp → Woosh 0,55 · nhãn nguồn → swing 0,35 · chữ phụ B → "Soft touch sound" 0,3 · thẻ đếm → "Soft and clear button sound" 0,35. Mẫu SFX copy trong `_LIBRARY/sfx/`. Thiếu: impact/stamp riêng.
- **Nhạc dạo đầu** chỉ 0:00–1:00: "Warm Morning Acoustic", âm lượng 0,09, fade vào 0,5s / ra 3s (`tools/patch_music_sfx_062v3b.py`). Từ khóa CapCut: gentle acoustic guitar · warm morning acoustic · calm ukulele · soft folk piano · cozy kitchen. User kéo mẫu xuống cuối timeline, rồi script đặt đúng chỗ.
- **Sticker sóng nhạc (user thêm tay trong CapCut, 18/10/2026):** "Equalize EN Music Tone V4" (mục Yêu thích), scale 0,41, vị trí (0,777; -0,698) góc dưới-phải, phủ cả video. Đã lưu `templates/capcut_sticker_equalizer.json`; builder `--v3` tự thêm. Lưu ý: sticker nằm trong cache CapCut của máy này.
- Draft đã sửa tay: không build đè; vá tại chỗ có sao lưu (`fix_caption_x.py`, `patch_*`), mất liên kết media → `relink_capcut_draft.py`.

## 4. Kiểm trước khi giao
0 tham chiếu hỏng · 0 file thiếu · lint kịch bản `tools/script_lint.py` PASS · thẻ không dày đặc · chữ không bị cắt mép.
