# Prompt dựng video — big-idea-091 (dán cho Antigravity)

> Tạo 24/10/2026. **Giọng đọc CHƯA có** (ai33 trả HTTP 503 hai lần, chưa trừ credit). Mốc thời gian dưới đây là ƯỚC TÍNH @165 wpm; khi có `voice.mp3` + `voice.srt`, Antigravity phải **đo lại mốc từ SRT** (bước 1 trong prompt). File text giọng đã sẵn: `voice/voice-text.txt` (3.008 từ, ~16,6K ký tự, dấu ngắt `<#0.7#>` / `<#1.0#>`).
> Khối dán nằm giữa hai đường kẻ `=====`. Đính kèm cho Antigravity: `script.md`, `voice/voice.mp3`, `voice/voice.srt`, thư mục footage đã tải.

=====

# VAI TRÒ
Bạn là editor video YouTube cho kênh làm vườn Mỹ **faceless** (không người, không mặt). Dựng video dài ~18 phút, 16:9, 1920×1080, 30fps, từ giọng đọc có sẵn. Khán giả Mỹ 35–60+, xem trên điện thoại: hình sạch, chữ to, ít chữ.

# ĐẦU VÀO
- `voice/voice.mp3` + `voice/voice.srt` (giọng đọc, nguồn thời gian DUY NHẤT; không đoán giờ).
- `script.md` (phần `## TTS SCRIPT` là lời đọc; phần ghi chú sản xuất ở đầu file).
- Chưa có footage nào: **bạn tự thu thập** (bước 0). Chỉ dùng nguồn giấy phép tự do (Pexels, Pixabay, Coverr, Wikimedia, USDA) + hình AI tự tạo. Không lấy video YouTube hay nguồn có bản quyền.

# QUY TẮC CỨNG (kiểm ở bước 5)
1. **Footage thật ≥ 50% tổng thời lượng hình** (stock video quay thật: Pexels/Pixabay/Coverr, giấy phép tự do). Đo theo giây, in vào `build_report.md`. Mục tiêu 55–60%.
2. **Hình AI POV ≤ 35%**, **thẻ đồ họa (bảng phấn) ≤ 10%**. AI chỉ dùng cho cảnh stock không có: cận cảnh thao tác cắt, đo ba–bốn inch, vết cắt, chai bột kích rễ… 
3. **Góc nhìn POV (người xem tự thấy tay mình):** góc nhìn thứ nhất, hai bàn tay làm việc, cúi nhìn xuống bàn/chậu, ánh sáng tự nhiên. **Không mặt, không toàn thân, không người đứng nhìn máy.** Tay phải có đủ 5 ngón, không biến dạng; hỏng thì loại clip đó.
4. **Không gắn nhãn chữ lên hình AI.** Không dùng AI để dựng "người thật", "bằng chứng", "kết quả đã xảy ra" hay ảnh bệnh/mốc của cây cụ thể.
5. **Nhịp cắt (hợp đồng):** 0–1′ trung bình ≤2,2s, tối đa 3,0s · 1–3′ TB ≤3,0s, tối đa 4,0s · sau 3′ TB ≤3,5s, tối đa 4,0s. Clip stock dùng <4s/lần. Một file nguồn ≤3 lần, không lặp trong 60s. Hình đầy khung, không collage.
6. **Lời–hình khớp:** hình phải ĐÚNG việc đang được nói (nói "pinch off the flowers" thì hình là tay bấm nụ hoa phong lữ, không phải cảnh vườn chung chung). Không chắc → dùng thẻ chữ, không dùng hình sai nghĩa.
7. **Chữ trên màn hình ÍT:** chỉ từ khóa chính (font Impact vàng, `$0`, `3–4 IN`, `HEAL?`…) và chữ phụ ngắn trắng; mỗi cụm cách lần lặp ≥90s. **Mỗi chữ hiện kèm SFX** (woosh nhẹ). Từ khóa hiện bằng động tác `KEYWORD` (mục "MOTION GRAPHICS").
8. **Thẻ nguồn trên màn hình (gánh uy tín thay lời nói):** hiện 3–4s, ≤1 lần/5 phút, đúng lúc lời đọc nhắc tới. Danh sách ở mục "THẺ NGUỒN".
9. Số liệu trên màn hình chỉ được là số có trong script: `3–4 inches`, `6 weeks`, `8 weeks`, `$0`, `three hours` (nếu hiện). Không thêm giá, % hay ngày.
10. Nhạc nền chỉ **0:00–1:00**, âm lượng ~0,09, fade vào 0,5s / ra 3s (guitar acoustic ấm). Sau 1:00 không nhạc. Giọng đọc -14 LUFS.
11. Không logo, không watermark, không thương hiệu trên chai/túi. Che hoặc chọn clip không thấy nhãn.

# THƯ VIỆN FOOTAGE (dùng lại từ các video trước)
Thư viện trung tâm: `D:\0002-Team A Nam\_LIBRARY` (~286 tệp: 159 video + 127 ảnh; gồm `stock/`, `ai/`, `gfx/`, `sfx/`, `wiki/`, `_inbox/`, `_manifests/`). **File quản lý: `_LIBRARY/catalog.csv`** (UTF-8 BOM), cột:
`id, path, class, kind(vid|img), origin, pool, topic, desc, license, credit, author_url, source_url, width, height, duration, bytes, sha256, prompt, tags, used_in, original_paths`.
Mã id: `STK-` stock video · `PHO-` ảnh stock · `AIM-` ảnh AI · `GFX-` thẻ đồ họa. `path` tính từ `_LIBRARY\`. `used_in` = video đã dùng (vd `062x1` = bài 062, 1 lần).

**Tìm (ưu tiên 1) — dùng lệnh có sẵn, hoặc lọc trực tiếp `catalog.csv` theo `desc/tags/pool`:**
```
python tools/garden_lib.py find <từ khóa> [--kind vid] [--pool <pool>]
```
Từ khóa nên thử trước: `pot` · `soil` · `hands` · `window` · `plant` · `cutting` · `scissors` · `calendar` · `timer` · `watering` · `frost` · `leaf` · `paper`. (Không có sẵn: `perlite`, `knife`, `basement` → tải mới/AI.) Duyệt nhanh: `_LIBRARY\wiki\00-Library-INDEX.md` và các trang theo chủ đề (`hands.md`, `care.md`, `herb.md`…).

**Luật dùng lại:**
1. Chỉ dùng clip khớp NGHĨA lời đọc (đọc cột `desc`; nghi ngờ thì mở xem). Clip đang gắn vào chủ đề khác (rau củ, rau mầm mùa đông) chỉ lấy khi cảnh thật sự trung tính: tay, chậu, đất, cửa sổ, lịch, đồng hồ.
2. Ưu tiên clip `used_in` ít/rỗng để khán giả không thấy lại cùng một cảnh; tránh cảnh dễ nhận ra (có chữ, nhãn, người) đã xuất hiện ở video gần đây.
3. Luật ≤3 lần/nguồn, không lặp trong 60s tính TRONG video này.
4. Clip stock thư viện vẫn phải cắt <4s/lần dùng. Giữ nguyên giấy phép/credit trong `credits.csv` (copy từ cột `license, credit, source_url`).
5. KHÔNG sửa, xóa hay di chuyển file gốc trong `_LIBRARY`; đọc và copy/tham chiếu.

**Tải mới → đăng ký vào thư viện (làm sau khi dựng xong):**
- File mới nằm ở `_LIBRARY\_inbox\091\{pexels,photos,ai,gfx}` (KHÔNG rải trong folder video).
- Mỗi file mới thêm 1 dòng vào `catalog.csv`: id tiếp số (STK-/PHO-/AIM-/GFX-), `pool`, `desc` tiếng Anh ngắn đúng nội dung hình, `license/credit/author_url/source_url`, `sha256`, `prompt` (với ảnh AI), `used_in` = `091x<số lần>`. Trùng `sha256` với file đã có → dùng bản cũ, không thêm.
- Cập nhật `used_in` cho cả clip cũ đã dùng (thêm `091xN`).
- Nếu có Python và quyền workspace: chạy `python tools/garden_lib.py ingest` sau khi thêm một mục `_v("091","geranium-cuttings")` vào `SOURCES` trong `tools/garden_lib.py`; không có thì cập nhật CSV thủ công và báo lại.
- Ghi vào `build_report.md`: số clip tái dùng / tải mới / AI, và danh sách id đã thêm.

# CÁC BƯỚC
**0. Nguyên liệu: DÙNG LẠI THƯ VIỆN TRƯỚC, tải mới SAU** (xem mục "THƯ VIỆN FOOTAGE" bên dưới). Thứ tự bắt buộc:
 a. Với mỗi cảnh trong bảng hình, tìm trong thư viện trước (≥ ~1/3 stock lấy từ thư viện nếu có clip khớp nghĩa).
 b. Cảnh nào thư viện không có hoặc không khớp nghĩa → tải mới (Pexels, Pixabay, Coverr, Wikimedia, USDA) vào `_LIBRARY/_inbox/091/{pexels,photos,ai,gfx}`; ghi đủ cột catalog.
 c. Ảnh/video AI POV: tạo A1–A14 (2–3 biến thể, chọn tay đúng nhất) → `_inbox/091/ai`, ghi prompt vào cột `prompt`.
 d. Thẻ chalk G1–G3 (PNG 1920×1080) → `_inbox/091/gfx`. SFX + nhạc: lấy `_LIBRARY/sfx/` trước (có `woosh.mp3`, `swing.mp3`…), thiếu mới tìm nhạc giấy phép tự do.
 e. Thiếu loại nào → ghi `missing.csv`, báo lại, không thay bằng hình sai nghĩa.
**1. Đọc `voice.srt`** → lập bảng chương bằng cách tìm câu mở của mỗi phần (cột "CÂU MỞ" bên dưới). Ghi `chapters.txt` (dạng `0:00 Tên`) — mốc này cũng là chapters YouTube.
**2. Lập `shotlist.csv`:** `start,end,dur,source(stock|ai|gfx),file,section,spoken_phrase,on_screen_text,sfx`. Phủ kín từ 0 đến hết giọng, không khoảng trống.
**3. Gán hình theo "BẢNG HÌNH THEO PHẦN"** (mục dưới): ưu tiên stock; chỉ dùng AI POV khi bảng ghi `AI`. Mỗi cue SRT ~1 shot (thường 2–4s).
**4. Dựng:** crop/zoom nhẹ 3–6% (Ken Burns chậm) để hình không đứng yên; cắt thẳng (cut), không hiệu ứng chuyển cảnh lòe loẹt; thẻ chalk dài ≥9s gắn đúng đoạn lời (còn G2 — G1/G3 đã thay bằng GRID3/COUNTER); dựng đồ họa theo mục "MOTION GRAPHICS" (HTML/Canvas hoặc Remotion, ghép thẳng vào MP4).
**5. Kiểm & xuất:** viết `build_report.md` gồm: % stock / AI / gfx (theo giây), shot dài nhất, nhịp TB theo 3 khung thời gian, số file bị dùng >3 lần, danh sách clip POV bị loại, `missing.csv`. **Nếu stock <50% → dừng, báo thiếu gì, không xuất.** Xuất `garden-091.mp4` (H.264, 12–16 Mbps, AAC 320k) + `chapters.txt`.

# BẢNG HÌNH THEO PHẦN
(Giờ ƯỚC TÍNH @165 wpm — ghi đè bằng SRT. `S` = stock thật, `AI` = ảnh/video AI POV, `G` = thẻ chalk.)

| Phần (giờ ước tính) | CÂU MỞ (để tìm trong SRT) | Hình cần | Nguồn |
|---|---|---|---|
| **HOOK 0:00–0:36** | "That's a stem tip, three to four inches long." | Cận ngọn phong lữ đỏ vừa cắt; hàng chậu phong lữ nở ngoài hiên; sương giá trên lá; dao/kéo sắc; cửa sổ nắng. Thẻ nguồn 0:16–0:25 (xem dưới). | S + 2 AI POV (A1, A2) |
| **M1 0:36–3:32** Cắt 3–4 inch | "Start at the top." | Tay lần theo thân tới ngọn; đo ba–bốn inch; cắt; tuốt lá dưới; giơ cành nhỏ lên "nhìn nhỏ nhưng đủ"; chậu pelargonium ngoài hiên; sương giá/dự báo lạnh | S ưu tiên · AI: A3 đo, A4 cắt, A5 tuốt lá |
| **M2 3:32–6:15** Chọn cây khỏe | "Quick word about the plant itself" → "mistake number one" | Cây khỏe vs cây lá vàng/đốm (stock chung, KHÔNG gán cho cây cụ thể); tay lật lá soi sâu; thân khỏe; chó/mèo ở hiên (ASPCA) — dùng stock thú cưng bình thường, không hoảng sợ | S + AI A6 lật lá |
| **M3 6:15–7:44** Bấm hoa/nụ | "one thing on that stem has to come off" | Tay bấm nụ hoa phong lữ; nụ rơi trên bàn | AI A7 bấm nụ (hoặc S nếu có) |
| **M4 7:44–10:04** Chậu & hỗn hợp | "Picture the kitchen counter on a Saturday morning." | Chậu nhỏ 3–4 inch; túi perlite/vermiculite/cát/than bùn (che nhãn); đổ hỗn hợp; tay vuốt nhẹ; bột kích rễ (tay chấm đáy cành) | S + AI A8 đổ hỗn hợp, A9 chấm bột |
| **M5 10:04–12:10** Cho vết cắt liền | "The step is simple: let the cut end heal" | Cành đặt trên khay/đĩa cát ẩm trong bóng râm; đồng hồ hẹn giờ; tay đặt 4 cành chia 2 nhóm, dán nhãn. **Thẻ chalk G2 so sánh nguồn** (2 nói heal / 4 không nhắc) | S + AI A10 đặt trên đĩa, A11 dán nhãn · G |
| **M6 12:10–14:06** Cắm & chờ | "Healed, or not, now the cutting goes in." | Tay cắm cành vào lỗ đã chọc; chậu trên bệ cửa sổ sáng; túi/nắp trong; lịch tuần (6–8); cận đáy cành tối mềm → "bỏ đi" (dùng stock thối chung, không gán) | S + AI A12 cắm, A13 phủ túi · G3 đếm tuần |
| **M7 14:06–17:10** Cây mẹ & bảo hiểm | "There are three ways to bring a geranium through winter" | Ba cách: cả chậu trong nhà (S), túi giấy bare-root hầm mát (S/AI A14), cành giâm trên bệ cửa sổ (S). "Cành giâm là bảo hiểm" | S + AI A14 · **G1 ba cách** |
| **Q 17:10–17:57** | "Which month?" / "Your questions" | Hỏi–đáp ngắn: lịch, bệ cửa sổ, hỗn hợp. Không hình phức tạp, chữ 1 dòng/ý | S |
| **KẾT 17:57–18:13** | "take one cutting today" | Chậu phong lữ nở trong nhà; cành giâm bắt đầu mọc lá; CTA bình luận | S |

# DANH SÁCH TỪ KHÓA STOCK (tìm Pexels/Pixabay/Coverr, ưu tiên clip dọc ≥1080p, dùng 2–4s)
`geranium flowers porch` · `red geranium pots` · `pelargonium close up` · `frost on leaves morning` · `cutting plant stem knife` · `pruning shears cutting stem` · `hands holding plant cutting` · `potting soil pour` · `perlite vermiculite` · `small pot windowsill` · `windowsill plants sunlight` · `kitchen counter plant pots` · `rooting plant cutting` · `watering seedling` · `plastic bag humidity dome plant` · `timer kitchen close up` · `calendar pages` · `paper bag storage basement` · `basement shelf plants` · `cat dog garden porch` · `autumn garden evening` · `lamp grow light plant`
Chỉ tải những cảnh thư viện chưa có. Ghi mọi clip dùng vào `credits.csv` (id, nguồn, URL, giấy phép).

# PROMPT ẢNH/VIDEO AI POV (tạo bằng công cụ ảnh/video AI của bạn; mỗi prompt 100% tiếng Anh)
Tiền tố chung cho MỌI prompt: `First-person POV looking down at both of my hands working, natural window light, photorealistic, shallow depth of field, 16:9, no face, no full person, no text, no logo, five fingers per hand, anatomically correct hands.`
Hậu tố negative: `no extra fingers, no distorted hands, no watermark, no brand labels, no text on packaging.`

| Mã | Cảnh (ghép sau tiền tố) |
|---|---|
| A1 | `holding upright a freshly cut red-geranium stem tip with green leaves on top, over a wooden porch rail, red geranium pots blurred behind` |
| A2 | `fingertips holding a clean-cut geranium stem against a plain wooden ruler (ruler has no numbers or letters), bright morning light` |
| A3 | `measuring a geranium stem with a plain unmarked wooden ruler, the other hand pinching the stem at about the three-to-four-inch point` |
| A4 | `right hand using a sharp small knife to cut a green geranium stem at an angle on a wooden cutting board, left hand steadying the stem` |
| A5 | `thumb and finger stripping the lower leaves off a geranium cutting, leaves falling onto a wooden table` |
| A6 | `one hand turning over a healthy geranium leaf to inspect the underside, potted red geranium in front` |
| A7 | `thumb and finger pinching off a pink geranium flower bud from a cutting stem, bud dropping onto a wooden table` |
| A8 | `pouring pale perlite and peat mix from a plain unlabeled scoop into a small terracotta pot on a kitchen counter` |
| A9 | `dipping the bare base of a geranium cutting into a small shallow dish of white powder, plain unlabeled jar beside it` |
| A10 | `placing four geranium cuttings in two groups on a saucer of damp sand in a shaded corner` |
| A11 | `hand writing nothing, sticking a blank white label tape on one small pot, four small pots in a row` |
| A12 | `pushing a geranium cutting into a pencil-made hole in a small pot of pale potting mix, other hand firming the mix` |
| A13 | `hands pulling a clear plastic bag loosely over a small pot of cuttings on a bright windowsill` |
| A14 | `hand lifting a brown paper bag of bare-root geraniums from a cool basement shelf, dim light` |
Mỗi mã: tạo 2–3 biến thể, chọn bản tay đúng nhất. Dùng ảnh tĩnh + zoom chậm là đủ; video AI chỉ khi tay sạch.

# THẺ CHALK (kiểu bảng phấn xanh, khung đen, chữ phấn trắng/vàng, font Ink Free; mỗi thẻ ≥9s, gắn đúng đoạn lời)
- **G1 (M7) "3 WAYS THROUGH WINTER":** KEEP THE POT · PAPER BAG BARE-ROOT · CUTTINGS (đánh dấu ★ ở cuối: "only one makes MORE plants").
- **G2 (M5, 13–15s) bảng nguồn heal:** `2 SAY HEAL` | `4 SAY NOTHING` | `NONE SAYS DON'T`. Không ghi tên trường trên thẻ này.
- **G3 (M6) đếm tuần:** vạch 1→8 tuần, tô đậm tuần 6, mũi tên "keep counting to 8".

# THẺ NGUỒN (chữ nhỏ dưới, 3–4s, đúng lúc lời đọc nhắc)
- Hook ~0:16–0:25: `ISU · UW–Madison · Univ. of Illinois Extension — "3–4 inches"`
- M1: `Illinois Extension — move indoors before first frost`
- M2: `ASPCA — Pelargonium is toxic to dogs, cats, horses`
- M5: `Illinois Extension · Texas A&M` (đúng câu họ được nhắc)
- Không thêm thẻ nguồn nào khác.

# MOTION GRAPHICS (6 động tác — spec đầy đủ: `templates/motion-graphics-garden.md`; đính kèm file đó)
Luật chung: một từ khóa mỗi lần, không xuống dòng, ≥1,8s trên màn hình, đổi chữ tối đa mỗi ~2,5s · **mọi hiệu ứng có tiếng** (click/whoosh/tick/stamp; lấy `_LIBRARY/sfx/` trước) · chuyển động trong 0,5s đầu mỗi cảnh, không khung đứng yên >1s · số trên màn hình chỉ là số trong script, số trung tâm lần đầu kèm thẻ nguồn cùng cảnh · chữ không mạnh hơn script · không dissolve/lật 3D/thanh chạy chữ/phụ đề đầy đủ · không đặt chữ ở góc dưới-phải (sticker sóng nhạc) · từ khóa Impact 96–120 px, vàng kênh / đỏ `#FF4A3D` = xấu / trắng ngà `#F7F5EF`.

| # | Động tác | Mốc (câu nói trong SRT) | Nội dung | Nguồn |
|---|---|---|---|---|
| 1 | **KEYWORD** (đập chữ + khối vàng) | Hook "three to four inches long" · M1 "take one cutting today" · M2 "Only healthy plants go forward" · M3 "pinch off the flowers" · M4 "drainage" · M5 "let the cut end heal" · M6 "Mark six on your calendar" · M7 "They're the insurance" | `3–4 INCHES` · `TAKE ONE TODAY` · `HEALTHY ONLY` · `FLOWERS OFF` · `DRAINAGE HOLES` · `LET IT HEAL` · `6–8 WEEKS` (dùng COUNTER) · `INSURANCE` — mỗi cụm 1 lần, cách nhau ≥90s | script |
| 2 | **PAGE_SAYS** (trang nguồn + bút dạ) | Hook ~0:16–0:25 (thay thẻ nguồn chữ) · M5 CITE_ZONE "Illinois Extension names Pelargonium as an exception" và câu Texas A&M | Chụp trang thật: ISU *How do I take geranium cuttings?* (dòng 3–4 inch) · Illinois Extension *Cuttings* (dòng Pelargonium — air dry and heal over) · Texas A&M (dòng about three hours on damp sand). Khối vàng: `3–4 IN` / `HEAL FIRST` / `~3 HOURS` | research-brief C01, C12/C13, C23 |
| 3 | **SPLIT** (tốt/xấu) | M2 "That's mistake number one" (cây bệnh vs cây khỏe) | Trái (xấu, khử màu, ngả đỏ): cây lá đốm/héo **stock chung** · Phải: cây khỏe. Nhãn `RESCUE` / `DONOR`; dấu ❌/✅ trên đường chia. **Không** dùng SPLIT cho "heal vs không heal" (nguồn không đo kết quả) | Illinois (cây khỏe) |
| 4 | **GRID3** (thay thẻ chalk G1, không làm cả hai) | M7 "There are three ways to bring a geranium through winter" — mỗi ô sáng đúng lúc đọc tên | `KEEP THE POT` · `PAPER BAG` · `CUTTINGS` (ô 3 thêm ★ khi đọc "Only one of the three gives you more plants") | UW, Illinois, ISU |
| 5 | **ID_CIRCLE** (khoanh + tên) | M1 "Their proper name is Pelargonium" · M3 nụ hoa trên cành · M6 "goes dark and soft at the base" | Nhãn `Geranium` / *Pelargonium* · khoanh nụ hoa · khoanh gốc thâm (**stock chung, không gán là bệnh của cây trong video**) | Illinois |
| 6 | **FREEZE_Q** (dừng hình + im lặng) | Re-hook M4 "turn black at the base" (dừng, câu hỏi `WHY BLACK?`) · ngay trước M5 "The step is simple" (dừng, `WHAT STEP?`, **2–3s im lặng**, rồi trả "let the cut end heal") | tối đa 2 lần | script |
| + | **COUNTER** (đếm số, thay thẻ chalk G3) | M6 "Mark six on your calendar, then keep counting to eight" | đếm 1 → 6 dừng vàng, rồi tiếp → 8; nhãn `WEEKS` xám | UW, ISU, Illinois-blog |
**Hai khoảng im lặng thật:** (1) trước khi trả Loop #1 ở M5 (FREEZE_Q); (2) sau câu "They're the insurance." ở M7 (1,5–2s, không giọng, không SFX).
**Kiểm trong `build_report.md`:** số lần mỗi động tác · chữ có xuống dòng không · chữ nào <1,8s · khung đứng yên >1s · hiệu ứng nào thiếu tiếng · số trên màn hình có trong script không · vị trí 2 khoảng im lặng.
Thẻ chalk còn dùng: **G2** (M5, bảng nguồn heal). G1 → GRID3, G3 → COUNTER.

# KHÔNG LÀM
Không người/mặt; không số/giá/% ngoài danh sách; không nhạc sau 1:00; không chuyển cảnh lòe loẹt; không tự thay hình sai nghĩa bằng hình "gần giống"; không bỏ qua báo cáo `build_report.md`.

=====

## Ghi chú cho bạn (không dán)
- **Chưa có giọng:** chạy lại `python tools/ai33_voice.py --env "D:/0008. Key Quân sự/.env" --voice clone_2697441 --text-file "scripts/big-idea-091-geranium-cuttings-free-plants/voice/voice-text.txt" --out "scripts/big-idea-091-geranium-cuttings-free-plants/voice/voice.mp3" --max-credits 28000` khi ai33 hết 503 (hoặc bảo tôi chạy). Ước tính ~24,6K credit.
- **Ngưỡng ≥50% footage thật:** stock 3–4s × ~330 shot; hình AI chỉ 14 mã × 2–3 biến thể. Dùng `tools/garden_lib.py find <từ khóa>` để tái dùng footage `_LIBRARY` trước khi tải mới.
- **Antigravity không thấy G-Labs/CapCut** của máy này: nó xuất MP4 + shotlist; nếu bạn muốn draft CapCut kiểu bài 062 thì dùng `garden_build_capcut.py` với `shotlist.csv` đó thay vì Antigravity.
- Các chỗ cần nghe thử sau khi có giọng: Pelargonium, Texas A&M, ASPCA.
