---
file: templates/motion-graphics-garden.md
role: Bộ 6 động tác đồ họa chuyển động cho video Garden US (thêm sinh động, giữ "chữ ít", hợp khán giả Mỹ 35–60+ xem điện thoại)
source: học có chọn lọc từ lemo-opuscar `styles/caption-news/STYLE.md` (thẻ chú thích · §5 Graphics · §8 Native moves) — đọc 24/10/2026. KHÔNG bê nguyên phong cách tin tức.
created: 2026-10-24
status: TEST — chưa dựng thử trên video nào; chưa kiểm `garden_build_capcut.py` có nhận clip nền trong suốt không
used_by: prompt Antigravity của từng video (mục "MOTION GRAPHICS") · shot-plan · templates/video-assembly.template.md
---

# Motion graphics Garden US — 6 động tác

> Mỗi động tác là một **mẫu có tham số** (chữ, vị trí, thời lượng, tiếng). Mỗi video chỉ điền nội dung vào bảng "điền cho video" ở cuối, không thiết kế lại. Áp **cùng** template dựng đã duyệt (`templates/video-assembly.template.md`): thẻ bảng phấn, chữ ít, SFX cho mọi chữ, nhạc chỉ 0:00–1:00, sticker sóng nhạc góc dưới-phải.

## A. Luật chung (áp mọi động tác)
1. **Một từ khóa mỗi lần, không xuống dòng.** Câu dài thì tách, không ép 2 dòng. Chữ trên màn hình ≥1,8 giây (lý tưởng = câu nói + 0,6 giây). Đổi chữ tối đa mỗi ~2,5 giây kể cả khi hình cắt nhanh hơn. Cùng một cụm chữ không lặp trong 90 giây.
2. **Mọi hiệu ứng đồ họa có tiếng.** Đập chữ = click + thump nhẹ · thẻ trượt vào = whoosh · đếm số = tick mỗi ~45 ms · dấu đóng = stamp. Lấy `_LIBRARY/sfx/` trước (`woosh.mp3`, `swing.mp3`…); thiếu tick/stamp thì tải từ nguồn giấy phép tự do và đăng ký vào thư viện. Âm lượng SFX như template dựng (0,3–0,55).
3. **Chuyển động trong 0,5 giây đầu mỗi cảnh; không khung nào đứng yên quá 1 giây** (Ken Burns 3–6% đã có; đồ họa cũng phải có push chậm ×1,02–1,03).
4. **Số trên màn hình = số trong script** (có mã claim). Số trung tâm lần đầu hiện **kèm thẻ nguồn trong cùng cảnh**. Không thêm %, giá, ngày ngoài script.
5. **Chữ không mạnh hơn nguồn:** dùng đúng chữ của script ("thin evidence", "one small study"), không "MYTH BUSTED", "PROVEN", "KILLER" nếu script không nói vậy.
6. **Không gắn nhãn địa danh lên footage minh họa** (stock ở bang khác không được ghi "Iowa"). Bản đồ chỉ khi script có nguồn cho đúng nơi đó.
7. **Cắt theo lưới 0,5 giây khi có thể** (dễ khớp tiếng). Chuyển cảnh mặc định: **cắt thẳng**. Chỉ được: chớp trắng 1–2 khung (ở cú ngoặt/dừng hình) · thẻ trượt từ phải 0,18 giây · chia đôi mở từ đường giữa · ô lưới nhô lên cách nhau 0,1 giây · punch-in 0,3 giây tới ~1,25×.
8. **Hai khoảng im lặng thật mỗi video** (2–3 giây, không giọng, không SFX) — đặt sau cú ngoặt lớn nhất (thường là lúc trả Loop #1) và một chỗ ở nửa sau.
9. **Vùng cấm đặt chữ:** góc dưới-phải (sticker sóng nhạc ~ (0,777; −0,698), scale 0,41) và mép 5% quanh khung. Chữ đồ họa luôn là vector/chữ thật, không phải footage phóng to.
10. **Không dùng:** dissolve, lật trang 3D, thanh chạy chữ, khung trường quay, slide tiêu đề + gạch đầu dòng, phụ đề đầy đủ suốt video (phụ đề để file SRT/CC của YouTube).

## B. Bảng màu & chữ (giữ nhận diện kênh)
| Vai trò | Màu | Ghi chú |
|---|---|---|
| Điểm chính / từ khóa / số tốt | **Vàng kênh** (như chữ A Impact hiện tại; nếu cần mã: `#FFC21A`) | khối vàng sau chữ, chữ đổi sang mực `#0E0E0C` |
| Xấu / mất / sai | Đỏ `#FF4A3D` | nửa "xấu" của chia đôi, ❌, khoanh đỏ nét đứt |
| Đúng | Xanh ✅ như thumbnail | chỉ cho dấu ✅ |
| Chữ thường | Trắng ngà `#F7F5EF` | viền đen dày + bóng như template |
| Nhãn / đơn vị | Xám `#8D8B83` | nhỏ hơn số |
- **Chữ:** từ khóa **Impact 96–120 px** ở 1080p (khán giả 35–60+ xem điện thoại — **không** dùng cỡ 33 px của Caption News). Nhãn phụ 44–56 px. Thẻ bảng phấn giữ font **Ink Free** như đã duyệt.
- **Nền thẻ dữ liệu:** dùng **bảng phấn xanh** của kênh (không dùng nền sổ cái tối của Caption News); khối vàng làm điểm nhấn trên bảng phấn.

## C. 6 động tác

### 1 · Từ khóa đập + khối vàng (`KEYWORD`)
- **Dùng khi:** câu chứa ý chính của phần (thay chữ tĩnh A/B hiện nay). 6–10 lần/video, không dày hơn.
- **Cách chạy:** chữ chia tối đa 2 cụm; mỗi cụm phóng 1,3 → 1 trong 0,13 giây (back ease), cụm sau trễ 0,12 giây. Từ khóa có **khối vàng quét trái → phải 0,12 giây** sau chữ, chữ đổi màu mực. Ở trên màn hình 1,8–3 giây, ra bằng cắt.
- **Vị trí:** canh trái x ≈ 120 px, baseline y ≈ 880–950 (tránh góc dưới-phải). Gradient tối nhẹ dưới chữ nếu nền sáng.
- **Tiếng:** click + thump nhẹ (0,3–0,4).

### 2 · Trang nguồn nói vậy (`PAGE_SAYS`)
- **Dùng khi:** số trung tâm lần đầu, CITE_ZONE, câu "một nguồn nói X". Thay việc đọc tên trường bằng giọng (L14/L19).
- **Cách chạy:** ảnh chụp **trang nguồn thật** (đã mở, có trong research-brief) đặt như tờ giấy trên bàn tối, nghiêng ±1–2°, bóng đổ, push chậm. **Bút dạ vàng quét đúng dòng** trong 0,3–0,5 giây (blend multiply). Sau đó con số/cụm chính hiện thành **khối vàng** bên cạnh trang. Tên nguồn ở thẻ nhỏ góc trên-trái. 3–4,5 giây.
- **Cấm:** dựng lại trang giả, sửa chữ trên trang, phóng chữ trang vượt độ phân giải (chụp ≥ 2× rồi thu nhỏ).
- **Tiếng:** whoosh vào + tiếng bút dạ nhẹ.

### 3 · Chia đôi tốt / xấu (`SPLIT`)
- **Dùng khi:** so sánh hai cách, hai trạng thái **có nguồn**. Không dùng để ngầm nói một kết quả mà nguồn không đo.
- **Cách chạy:** đường chia vàng 4 px rơi xuống trước; hai nửa mở từ đường chia. Nửa "xấu" khử màu ~45%, tối, ngả đỏ nhẹ; nửa "đúng" giữ màu. Mỗi nửa có nhãn khối ngắn (≤3 từ). Dấu ❌/✅ hoặc nhãn chung đóng lên đường chia sau khi hai nửa ổn định. Giữ ≥2,5 giây cho mỗi nửa được nhìn.
- **Tiếng:** whoosh mở + stamp khi đóng dấu.

### 4 · Lưới 3 ô sáng theo lời (`GRID3`)
- **Dùng khi:** 3 cách, 3 sai lầm, 3 nguồn bất đồng. Thay thẻ bảng phấn tĩnh tương ứng (không làm cả hai cho cùng một ý).
- **Cách chạy:** 3 ô (≈632 px, khe 12 px) nhô lên cách nhau 0,1 giây, đánh số 1–2–3. Ô **sáng viền vàng + nhãn vàng đúng lúc giọng đọc tên ô đó**; ô chưa đọc mờ 60%. Số liệu (nếu có) nằm trong ô, giọng không đọc lại (L18). Tổng ≥9 giây như thẻ bảng phấn.
- **Tiếng:** pop nhẹ mỗi ô sáng.

### 5 · Phóng vào + khoanh + tên thường/tên Latin (`ID_CIRCLE`)
- **Dùng khi:** nhận diện cây, bộ phận, triệu chứng (mắt cành, nụ hoa, gốc thâm, *Pelargonium* vs *Geranium*, *Rosa*).
- **Cách chạy:** punch-in 0,3 giây (ease-out) tới ~1,2×; **vòng tròn đỏ nét đứt vẽ quanh chi tiết** trong 0,3 giây; đường dẫn ra nhãn 2 dòng: tên thường (trắng, đậm) + tên Latin (xám, nghiêng). 2–3 giây.
- **Cấm:** khoanh lên footage minh họa rồi gọi đó là "bệnh của cây này"; nhãn bệnh chỉ khi script nói đúng bệnh đó.
- **Tiếng:** whoosh ngắn + nét vẽ.

### 6 · Dừng hình + câu hỏi + im lặng (`FREEZE_Q`)
- **Dùng khi:** lúc gieo hoặc trả vòng lặp lớn (Loop #1, re-hook giữa video). Tối đa 2 lần/video.
- **Cách chạy:** hình dừng, chớp trắng 0,14 giây, punch 1,0 → 1,12, giảm bão hòa còn ~45%, **góc khung vàng khép vào chủ thể**. Câu hỏi (≤5 từ) hiện bằng động tác 1. Sau đó **2–3 giây im lặng** (tắt SFX/nhạc) rồi mới trả lời.
- **Tiếng:** một tiếng "chạm" duy nhất lúc dừng, sau đó im.

### (Phụ) Bộ đếm số (`COUNTER`)
- **Dùng khi:** khoảng thời gian/số lượng có nguồn ("6–8 weeks", "two to four months"). Số nằm trên màn hình để giọng khỏi đọc lại.
- **Cách chạy:** số chạy ease-out 0,45 giây, chữ số ô cố định (không rung), đổi sang vàng khi tới đích; đơn vị nhỏ hơn, màu xám.
- **Tiếng:** tick mỗi ~45 ms, kết bằng stamp nhẹ.

## D. Kỹ thuật dựng (chưa kiểm — ghi rõ khi thử lần đầu)
- **Đường Antigravity:** dựng đồ họa bằng HTML/Canvas (hoặc Remotion) và ghép thẳng vào MP4 cuối. Đây là đường dễ nhất cho 6 động tác.
- **Đường CapCut (`tools/garden_build_capcut.py`):** cần xuất mỗi động tác thành clip nền trong suốt (ví dụ MOV ProRes 4444 hoặc WebM VP9 alpha) hoặc PNG theo từng bước. **Chưa kiểm** builder có nhận clip nền trong suốt không — thử trên 1 động tác trước khi làm cả video.
- **Kiểm sau dựng (ghi vào `build_report.md`):** số lần mỗi động tác · chữ có xuống dòng không · có chữ nào <1,8 giây không · khung đứng yên >1 giây · mọi hiệu ứng có tiếng chưa · số trên màn hình có trong script không · 2 khoảng im lặng ở đâu.

## E. Bảng điền cho từng video (copy vào prompt Antigravity)
| # | Động tác | Mốc (câu nói trong SRT) | Nội dung chữ / hình | Nguồn (mã claim) |
|---|---|---|---|---|
| 1 | KEYWORD | | | |
| 2 | PAGE_SAYS | | | |
| 3 | SPLIT | | | |
| 4 | GRID3 | | | |
| 5 | ID_CIRCLE | | | |
| 6 | FREEZE_Q | | | |
| + | COUNTER | | | |
