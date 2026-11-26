# 04. Chiến lược YouTube Shorts 30 Giây Kích Tệp Mỹ & Kết nối Goha Studio

- **Bối cảnh thực tế từ OAuth Audit:**
  - Hiện kênh có **0% traffic Shorts**.
  - Tháng 6/2026 kênh từng đăng dồn **27 Shorts 9–11 giây kiểu clickbait phi khoa học** (*"Why Orchid Experts Stuff Sprout Inside Fresh Lemon"*) rồi phải xóa 18 / ẩn 9 — việc này làm loãng tệp sang khán giả trẻ/non-US và tạo rủi ro *Inauthentic Content*.
- **Chiến lược Shorts 30 giây MỚI (Khác 180° đợt tháng 6):**
  - **Độ dài chuẩn:** **28–35 giây** (đủ truyền tải 1 mẹo thực tế có chiều sâu + 1 con số chứng minh, tối ưu **Engaged Views** theo sổ tay thuật toán 2026 thay vì loop 9 giây vô nghĩa).
  - **Vai trò duy nhất:** **Cầu nối "kích tệp Mỹ" vào Long-form** bằng tính năng **Related Video (Video liên quan)** gắn ở góc dưới màn hình.
  - **Tần suất an toàn:** **3 Shorts / tuần** (cách ngày), **KHÔNG spam hàng loạt**, **KHÔNG bật 21 ngôn ngữ localization** (chỉ `en-US`!), **KHÔNG dùng mẹo bịa/phi khoa học** (tuân thủ Narrator Integrity & L11).
  - **Đồng bộ thương hiệu:** Dùng đúng giọng **Ohio-grandma educator** sẵn có của kênh ([tools/ai33_voice.py](file:///d:/0002-Team%20A%20Nam/tools/ai33_voice.py) / mẫu [Voice Gardent.MP3](file:///d:/0002-Team%20A%20Nam/Voice%20Gardent.MP3)) để khi người xem bấm sang Long-form thấy liền mạch 100%.

---

## 1. Trạng thái & Báo giá Thực tế Goha Studio (Đã kiểm tra trực tiếp)

Kiểm tra trực tiếp qua `goha:get_health` và `goha:get_model_pricing`:
- **Google Flow:** **SẴN SÀNG (`generationReady: true`)** với **2 tài khoản khỏe**:
  - Tài khoản 1: gói **PRO** (`tha…@gmail.co·3436`, ready)
  - Tài khoản 2: gói **ULTRA** (`thu…@gmail.co·a575`, ready)
- **Các engine phụ đang sẵn sàng:** **Muse** (1 tài khoản ready) · **Google Vids** (2 tài khoản ready) · **Goha AVS** (`avs-manifest` sẵn sàng ghép sub dọc, nhạc nền, chuẩn -14 LUFS).
- **Đơn giá THẬT trên gói ULTRA đang kết nối (tối ưu chi phí nhất):**

| Thành phần cho 1 Short 30 giây (5–6 cảnh dọc 9:16) | Model đề xuất | Giá trên gói ULTRA | Tổng ước tính / 1 Short |
|---|---|---:|---:|
| 5–6 ảnh khung 9:16 (`gen_anh_khung`) | **Nano Banana Pro (`GEM_PIX_2`)** | **0 credit** | **0 credit** |
| 5–6 clip video 6s (`tao_video_canh`, i2v) | **Veo 3.1 Lite (`lite`)** | **5 credit / clip** | **25–30 credit** |
| *(Tùy chọn tiết kiệm tối đa)* | **Veo 3.1 Lite [Lower Priority]** | **0 credit** *(chậm hơn)* | **0 credit** |
| Nâng nét 1080p (`veo_3_1_upsampler_1080p`) | **Veo 3.1 Upsampler 1080P** | **0 credit** | **0 credit** |
| Giọng đọc đồng bộ kênh | `tools/ai33_voice.py` (giọng Garden US) | Ngoài Flow | Giữ 100% DNA giọng |
| Ghép cắt nhịp + Phụ đề dọc to + Nhạc + Mix | `avs-manifest` (Goha AVS) | **0 credit** | **0 credit** |

> ⚠️ **Lưu ý quan trọng:** Google sẽ gỡ Veo 3.1 Fast, Veo 3.1 Quality và Omni 1.1 Flash từ **05/12/2026**, nên toàn bộ quy trình Shorts dưới đây chuẩn hóa luôn trên **Nano Banana Pro (0 cr) + Veo 3.1 Lite (5 cr/clip hoặc Free LP) + Upscale 1080p (0 cr)**.

---

## 2. 3 Kịch bản Shorts 30 Giây Chuẩn Tệp Mỹ (Sẵn sàng nạp vào Goha Studio)

> Mỗi kịch bản dài **~75–82 từ tiếng Anh** (≈ 28–30 giây ở tốc độ 165 wpm), **faceless (chỉ có bàn tay làm prop)**, đóng đinh bối cảnh nhà Mỹ, không nhân chứng bịa, không AI cliché, chốt bằng mũi tên trỏ **Related Video**.

---

### SHORT #1 (ƯU TIÊN #1) — Nối về Video *7 Cheap Root Cellar Ideas* (`x0-7HzQnLaU` · 75,1% US) hoặc *Root Cellar Without a Cellar* (`8bHtI8SpcTc`)
- **Tiêu đề Short (EN):** `Keep Carrots Crisp Until April With a $3 Bucket (No Basement!) #shorts`
- **Related Video gắn dưới:** `x0-7HzQnLaU` (*7 Cheap Root Cellar Ideas That Keep Vegetables Fresh ALL WINTER*)
- **Mục tiêu tệp:** Chủ nhà Mỹ Zones 3–7, thích tiết kiệm tiền đi chợ & bảo quản thực phẩm mùa đông.

**Lời đọc TTS (78 từ ≈ 28,5 giây @165 wpm):**
> Your fridge ruins carrots in two weeks — but a three-dollar bucket of damp sand keeps them crisp until April. No basement needed. Here's why it works: carrots breathe out moisture fast in dry fridge air. Bury them in barely damp play sand — never touching each other — and slide the bucket into an unheated garage or cool closet around thirty-five to forty degrees. Just don't wash them first, or they rot. Want six more zero-cost winter storage tricks? Tap the linked video below.

**Bảng Storyboard 5 cảnh (9:16 dọc · 6 giây/cảnh = 30s · Goha Studio):**
| Cảnh | Giây | Hình ảnh dọc 9:16 (Photoreal · US home · Faceless, tay làm prop) | Chữ to trên màn hình (Canva/AVS) |
|---:|---:|---|---|
| 1 | 0–6s | Cận cảnh củ cà rốt héo mềm trong ngăn mát tủ lạnh Mỹ, rồi chuyển cắt nhanh sang bàn tay nhấc củ cà rốt cam tươi giòn rộp từ xô cát sạch. | `CRISP TIL APRIL?` *(vàng)* / `$3 BUCKET` *(trắng)* |
| 2 | 6–12s | Góc nhìn từ trên xuống: bàn tay rải một lớp cát ẩm nhẹ (damp play sand) dày 2 inch dưới đáy xô nhựa 5-gallon trong nhà xe Mỹ. | `DAMP PLAY SAND` |
| 3 | 12–18s | Bàn tay xếp từng củ cà rốt còn nguyên lớp đất mỏng đặt cách nhau không chạm vào nhau, rồi phủ lớp cát tiếp theo lên trên. | `DON'T LET THEM TOUCH` |
| 4 | 18–24s | Đậy hờ nắp, đặt chiếc xô gọn vào góc gara không sưởi / tủ mát cạnh nhiệt kế hiện `38°F` (`35–40°F`). | `35–40°F` / `DON'T WASH FIRST!` |
| 5 | 24–30s | Bàn tay bẻ đôi củ cà rốt giòn tan trong bếp Mỹ ấm cúng, ánh sáng tự nhiên, mũi tên vàng chỉ xuống góc dưới trái vị trí nút Related Video. | `6 MORE $0 TRICKS 👇` |

---

### SHORT #2 (ƯU TIÊN #2) — Nối về Video *7 Flower Seeds to Scatter in Winter — Even on Snow* (`xYgPSm00Wcs` · video sắp ra mắt)
- **Tiêu đề Short (EN):** `Scatter These 3 Flower Seeds Right on Winter Snow (Zero Digging!) #shorts`
- **Related Video gắn dưới:** `xYgPSm00Wcs` (*7 Flower Seeds to Scatter in Winter — Even on Snow*)
- **Mục tiêu tệp:** 100% khán giả Mỹ có sân vườn vùng có tuyết/băng giá (Zones 3–7) — **bộ lọc địa lý US siêu sạch!**

**Lời đọc TTS (80 từ ≈ 29 giây @165 wpm):**
> Sounds backwards, right? Tossing flower seeds right onto winter snow. But for poppies, coneflowers, and milkweed, freezing weather isn't the enemy — it's the alarm clock. Their hard seed coats need weeks of freezing and thawing just to wake up. As the snow melts, it pulls every seed snug into the soil for you. No digging, no grow lights, and zero nursery bills come spring. Just skip windy days and bare slopes. Want all seven snow-sowing flowers? Tap the video right below.

**Bảng Storyboard 5 cảnh (9:16 dọc · 6 giây/cảnh = 30s · Goha Studio):**
| Cảnh | Giây | Hình ảnh dọc 9:16 (Photoreal · US backyard winter · Faceless) | Chữ to trên màn hình |
|---:|---:|---|---|
| 1 | 0–6s | Bàn tay đeo găng len rắc hạt giống hoa nhỏ màu tối trực tiếp lên lớp tuyết trắng mịn phủ trên luống đất vườn sau nhà Mỹ. | `SEEDS ON SNOW?!` *(vàng)* / `NO DIGGING` *(trắng)* |
| 2 | 6–12s | Bộ 3 ảnh ghép cận cảnh sắc nét hoa Mỹ quen thuộc rực rỡ: Poppies đỏ, Purple Coneflowers tím, Milkweed cam. | `POPPIES · CONEFLOWER · MILKWEED` |
| 3 | 12–18s | Cận cảnh tuyết tan chậm thấm xuống đất nâu sẫm, kéo hạt giống nhỏ lọt vừa khít vào khe đất ẩm tự nhiên. | `MELTING SNOW PLANTS THEM` |
| 4 | 18–24s | Biến đổi thời gian (timelapse ánh sáng ấm): luống đất mùa đông bừng nở thành dải hoa lâu năm rực rỡ ven hàng rào gỗ Mỹ. | `$0 NURSERY BILL` |
| 5 | 24–30s | Cận cảnh góc vườn hoa nở rộ nắng sớm, không gian thoáng ở đáy màn hình có mũi tên chỉ xuống nút Related Video. | `ALL 7 FLOWERS 👇` |

---

### SHORT #3 (ƯU TIÊN #3) — Nối về Video *Pour THIS Over Dry Leaves → Compost* (`7GzeVsMet3s` · 68,6% US · AVD 39,2%)
- **Tiêu đề Short (EN):** `Stop Bagging Fall Leaves — Turn Them Into Free Black Gold Fast #shorts`
- **Related Video gắn dưới:** `7GzeVsMet3s` (*Pour THIS Over Dry Leaves and Watch Them Turn Into Compost in DAYS!*)
- **Mục tiêu tệp:** Chủ nhà Mỹ đang dọn lá rụng cuối thu/đầu đông — 68,6% US / 81,9% Tier-1.

**Lời đọc TTS (80 từ ≈ 29 giây @165 wpm):**
> Stop dragging bags of fall leaves to the curb — you're throwing away fifty dollars of free garden gold. Dry leaves only take forever to break down because they're all carbon and zero fuel for soil microbes. Shred them once with your lawn mower, wet them like a wrung-out sponge, then pour on a cheap nitrogen boost like used coffee grounds or lawn clippings. The pile heats up fast, no turning required. Want the exact ratio that melts leaves fast? Tap the video below.

**Bảng Storyboard 5 cảnh (9:16 dọc · 6 giây/cảnh = 30s · Goha Studio):**
| Cảnh | Giây | Hình ảnh dọc 9:16 (Photoreal · US suburban yard · Faceless) | Chữ to trên màn hình |
|---:|---:|---|---|
| 1 | 0–6s | Hàng túi giấy nâu đựng lá khô xếp ngoài lề đường khu dân cư Mỹ bị gạch chéo ❌ đỏ, chuyển sang bàn tay bốc nắm đất mùn đen tơi xốp ✅ xanh. | `STOP BAGGING LEAVES` *(vàng)* / `$50 FREE SOIL` *(trắng)* |
| 2 | 6–12s | Máy cắt cỏ đẩy tay chạy qua lớp lá phong/sồi khô trên bãi cỏ Mỹ, băm nhỏ lá thành mảnh vụn. | `STEP 1: SHRED ONCE` |
| 3 | 12–18s | Bàn tay tưới nước nhẹ lên đống lá vụn rồi vắt thử nắm lá ẩm đều không nhỏ giọt (như miếng bọt biển vắt ráo). | `STEP 2: WRING-OUT DAMP` |
| 4 | 18–24s | Bàn tay rắc bã cà phê / cỏ cắt xanh trộn vào đống lá ẩm, hơi ấm nhẹ bốc lên trong sáng thu se lạnh. | `STEP 3: ADD NITROGEN` |
| 5 | 24–30s | Đống lá biến thành đất mùn đen nhánh giàu giun đất trong luống vườn gỗ, mũi tên trỏ xuống nút Related Video. | `EXACT RATIO 👇` |

---

## 3. Quy trình Chạy ngay trên Goha Studio (Chờ bạn chọn Short & duyệt credit)

Khi bạn nhắn chọn **Short #1, #2 hoặc #3** (hoặc cả 3) và chọn chế độ **Veo 3.1 Lite (25 credit/Short — nhanh)** hay **Veo 3.1 Lite Lower Priority (0 credit — chậm hơn)**:
1. Mở Lượt trên Goha (`luot_bat_dau`) và tạo dự án phim ngắn 9:16 (`tao_du_an`, 0 credit).
2. Nạp kịch bản kiểm chuẩn (`kiem_kich_ban`) & dựng Storyboard 5 cảnh theo khung prompt chuẩn của Goha (`tao_storyboard` + `goi_y_prompt`).
3. Gen ảnh khung mẫu Cảnh 1 trước bằng **Nano Banana Pro (0 credit trên ULTRA)** → bạn duyệt phong cách → chạy nốt 4 ảnh khung (0 credit).
4. Báo giá tổng `tao_video_canh` 2 pha → bạn xác nhận `ma_xac_nhan` → gen 5 clip video 6s + nâng nét 1080p (**0 credit trên ULTRA**).
5. Chạy giọng đọc bằng `tools/ai33_voice.py` (giọng Garden US) + dựng hậu kỳ phụ đề dọc to rõ & mix -14 LUFS trên **Goha AVS (`avs-manifest`)** → xuất MP4 9:16 sẵn sàng đăng kèm **Related Video**.
