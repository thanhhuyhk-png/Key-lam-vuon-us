# 01. Chẩn đoán Toàn diện Sức khỏe Kênh & Truy gốc "Lệch tệp" — Senior Garden Guide

- **Kênh:** Senior Garden Guide (`@seniorgardenguide` · `UCnCALMh5O4Ykpv_ESjZ6WqA`)
- **Ngày đo:** 2026-11-26 (dữ liệu OAuth YouTube Analytics + Data API v3 + Export Studio tới 21/11/2026)
- **Dữ liệu gốc:** [oauth-deep-audit.json](file:///d:/0002-Team%20A%20Nam/research/kenh-lam-vuon-us/oauth-deep-audit.json) · [channel-health-latest.json](file:///d:/0002-Team%20A%20Nam/references/channel-health-latest.json) · [latest.md](file:///d:/0002-Team%20A%20Nam/research/kiem-dinh-ky/latest.md)
- **Quy mô hiện tại:** 62.900 sub · 6.054.442 tổng view · 260 video công khai

---

## 1. Báo cáo kỹ thuật về lỗi Proxy trên Auto Trend Studio (`PROXY_ENV_UNSUPPORTED`)

> **Kết luận ngắn:** **4 proxy trong kho của bạn KHÔNG hề hỏng** — lỗi nằm ở **bản đóng gói của phần mềm Auto Trend Studio** trên ổ E. Chúng tôi **KHÔNG tắt proxy** theo đúng yêu cầu của bạn.

### Bằng chứng đo trực tiếp từ kho proxy (`trang_thai_proxy`)
| ID Proxy | Host:Port | Tài khoản gắn | Trạng thái | Ping |
|---|---|---|---|---|
| `p_0c2de6c3` | `proxy02004.hproxy.id.vn:43466` | Profile 001 VN | ✅ Active / Alive | 772 ms |
| `p_85f65126` | `proxy13240.uproxy.id.vn:6375` | Profile 002 VN | ✅ Active / Alive | 847 ms |
| `p_956be7f3` | `proxy15216.eproxy.id.vn:28013` | Profile 003 VN | ✅ Active / Alive | 955 ms |
| `p_7d8a9871` | `proxy03243.xproxy.id.vn:24558` | Profile 004 VN | ✅ Active / Alive | 777 ms |

### Nguyên nhân gốc chính xác trong mã nguồn Auto Trend Studio
- File kiểm tra: `E:\001.Goha\AutoTrendStudio\src\autotrend\collect\ytdlp_client.py` (dòng 69–86):
  - Hàm `proxy_env_honored()` tìm file `E:\001.Goha\AutoTrendStudio\docs\probes\results\ytdlp_live.json` và đọc cờ `findings.proxy_env_honored == true`.
  - Khi kiểm tra thư mục `E:\001.Goha\AutoTrendStudio\docs\`, **chỉ có duy nhất 1 file** `gioi-thieu-hoi-vien.md` — bộ cài Windows của Auto Trend Studio **thiếu hoàn toàn thư mục `docs\probes\results\ytdlp_live.json`**.
  - Vì thiếu file probe này, mỗi khi trong kho có bất kỳ proxy nào đang bật (`proxy_pool.has_enabled() == True`), `ensure_proxy_supported()` tự động ném lỗi `PROXY_ENV_UNSUPPORTED` và **chặn mọi lệnh `yt-dlp`** (quét ngách vòng mở rộng, tải video/phụ đề) — dù bản thân `yt-dlp 2026.11.23` và cả 4 proxy đều hoạt động bình thường.
- **Cách chúng tôi đã xử lý sạch mà KHÔNG tắt proxy:** Toàn bộ dữ liệu dự án `Kênh làm vườn US` (gợi ý hạt giống, cào 19 kênh lõi làm vườn US, xếp hạng TOP 20, phân tích từ khóa, gom Top View ngách, đào 600+ bình luận, Google Trends US) đều đã chạy thành công **100% qua tầng YouTube Data API v3 (dùng ~104/10.000 đơn vị hạn mức ngày)** mà **không cần tắt proxy**.
- **Cách khắc phục triệt để lỗi này:** Báo bên phát triển Auto Trend Studio cập nhật bản vá (bổ sung file/probe kiểm tra thực tế hoặc đóng gói `docs/probes/results/ytdlp_live.json` trong installer).

---

## 2. Quỹ đạo 13 tháng của kênh (Số thật YouTube Analytics)

| Tháng | Views | Net Sub (+ / -) | AVD % | Giây xem/lượt | Likes | Comments |
|---|---:|---:|---:|---:|---:|---:|
| 2025-11 | 98.025 | +2.740 (+2.800 / -60) | 26,7% | 421 s | 3.118 | 94 |
| 2025-12 | 338.462 | +5.040 (+5.205 / -165) | 25,5% | 316 s | 7.194 | 186 |
| **2026-01** | **1.155.547** | **+14.829** | 27,1% | 235 s | 26.475 | 603 |
| **2026-02** | **722.219** | **+7.758** | 25,9% | 203 s | 14.675 | 357 |
| **2026-03** | **1.118.969** | **+13.300** | 25,1% | 199 s | 23.997 | 903 |
| **2026-04** | **1.568.112** | **+12.353** | 26,2% | 203 s | 23.864 | 652 |
| 2026-05 | 395.414 | +3.483 | 26,3% | 213 s | 7.203 | 268 |
| 2026-06 | 226.103 | +1.317 | 25,6% | 193 s | 3.353 | 144 |
| 2026-07 | 120.206 | +714 | 25,7% | 203 s | 1.764 | 67 |
| 2026-08 | 104.197 | +610 | 28,0% | 220 s | 1.429 | 74 |
| 2026-09 | 112.435 | +331 | 28,3% | 235 s | 945 | 54 |
| 2026-10 | 87.437 | +248 (+497 / -249) | 28,9% | 242 s | 718 | 34 |
| 2026-11 *(tới 25/11)* | 54.452 | +189 (+324 / -135) | 29,7% | 243 s | 411 | 23 |

---

## 3. SÁU "BẰNG CHỨNG VÀNG" GIẢI THÍCH VÌ SAO KÊNH GIẢM ĐỀ XUẤT & LỆCH TỆP

### 🔴 Nguyên nhân #1 (NẶNG NHẤT & MỚI PHÁT HIỆN): Gắn **19–21 ngôn ngữ Localization** vào TẤT CẢ video mới → tự bơm traffic rác ngoài Mỹ, kéo sập AVD & cắt Browse US
Kiểm tra trực tiếp trường `localizations` từ YouTube Data API v3 cho thấy **toàn bộ video từ tháng 9–11/2026 đều đang dịch tiêu đề/mô tả sang 19–21 ngôn ngữ**: Hindi (`hi`), Tamil (`ta`), Telugu (`te`), Bengali (`bn`), Malayalam (`ml`), Punjabi (`pa`), Indonesia (`id`), Ả Rập (`ar`), Nga (`ru`), Nhật (`ja`), Hàn (`ko`), Ba Lan (`pl`), Brazil (`pt-BR`)... trong khi nội dung vẫn làm cho thị trường Mỹ (giọng tiếng Anh).

**Hệ quả đo được ngay trên từng video mới:**
- Video từng được coi là "tốt nhất 2 tháng qua" — `rr_1fCTtuP4` (*Nobody Believed Dragon Fruit Could Survive on Desert Sand*, 1.256 view, CTR 4,41%): **CHỈ CÓ 11,2% VIEW TỪ MỸ**, còn lại **Ấn Độ 42,4% · Indonesia 23,0% · Bangladesh 9,8%**!
- `NFPmRO2FZYI` (*No Flowers on Your Lemon Tree*, 636 view): **US chỉ 16,7%**, Ấn Độ 39,6%, Bangladesh 8,8%.
- `ocByKNBqZFg` (*Geraniums Will Explode*, 754 view): **US chỉ 24,0%**, Hàn Quốc 18,3% (do localization `ko`), Ấn Độ 6,6%.
- `9PWB233HBFc` (*You're Throwing Away Free Plants*, 961 view): **US chỉ 29,8%**, Nhật 16,8% (`ja`), Ba Lan 10,7% (`pl`), Brazil 4,7% (`pt-BR`).
- **Tác động lên AVD toàn kênh:** Trong 28 ngày gần nhất, **khán giả US xem đạt AVD 33%, Canada 35%, UK 33%** — trong khi **Ấn Độ chỉ 19%, Indonesia 20%, Pakistan 16%**! Việc bật 21 ngôn ngữ khiến mẻ thử đầu của video mới bị rải đi 20 nước ngoài Mỹ → người xem bấm vào tiêu đề dịch tiếng địa phương rồi thoát ngay vì nghe tiếng Anh → AVD video mới tụt còn 12%–24% → thuật toán ngừng đẩy sang Browse Mỹ!

**CẢNH BÁO KHẨN:** Hiện trong YouTube Studio đang có **3 video ở trạng thái PRIVATE (chưa công khai) ngày 24–25/11** (`xYgPSm00Wcs` *Flower Seeds on Snow*, `zK1CQBLKBck` *4 Amish Fall Habits*, `rdsi3pGRMlg` *Grow 6 Fruit Bushes From Winter Cuttings*) và 1 video vừa công khai hôm qua (`3q44GhlmPes`) — **CẢ 4 VIDEO ĐỀU ĐANG GẮN 19–21 LOCALIZATIONS!** Phải gỡ bỏ toàn bộ ngôn ngữ ngoài tiếng Anh TRƯỚC khi công khai 3 video này.

### 🔴 Nguyên nhân #2: Sụp đổ **Smart TV Mỹ** (từ 59,5% xuống còn 25,9%–29,4%)
| Giai đoạn | Smart TV | Mobile | Desktop | Tablet |
|---|---:|---:|---:|---:|
| Đỉnh T1–T4/2026 (4,56M view) | **59,5%** | 27,6% | 7,8% | 5,1% |
| Suy giảm T5–T8/2026 (846K view) | 36,7% | 46,6% | 11,2% | 5,5% |
| Gần đây T9–T11/2026 (254K view) | **25,9%** | **56,9%** | 13,6% | 3,6% |
| 28 ngày gần nhất (62K view) | **29,4%** | **53,7%** | 13,4% | 3,5% |

- Kênh từng bùng nổ nhờ **người xem Mỹ 55–65+ (68,2% tổng tệp) xem trên Smart TV phòng khách (59,5% thiết bị)** — trong khi cấu hình workspace lại đang viết `mostly on mobile`.
- Khi tệp bị pha loãng sang Ấn Độ/Đông Nam Á (chủ yếu xem Mobile) và Shorts 9 giây, Smart TV Mỹ mất hơn một nửa tỷ trọng!

### 🔴 Nguyên nhân #3: Dịch chuyển Địa lý & Độ tuổi (Tệp Mỹ bị pha loãng gấp đôi bởi Ấn Độ)
| Giai đoạn | US % | Tier-1 % (US/CA/GB/AU/NZ) | Ấn Độ (IN) % | Độ tuổi 55+ % | Độ tuổi 18–34 % |
|---|---:|---:|---:|---:|---:|
| Đỉnh T1–T4/2026 | **53,7%** | **75,4%** | 9,7% | **68,2%** (65+: 44,6%) | 6,7% |
| Suy giảm T5–T8/2026 | **42,8%** (-10,9đ) | **60,6%** (-14,8đ) | **20,6%** (×2,1) | 51,3% (65+: 32,2%) | **15,1%** (×2,25) |
| Gần đây T9–T11/2026 | 45,0% | 63,2% | 18,0% | 56,2% (65+: 35,9%) | 13,2% |
| 28 ngày gần nhất | 47,4% | 65,5% | 16,8% | 57,9% (65+: 36,6%) | 12,2% |

- **Bằng chứng phân cực theo chủ đề:** Video cây nhiệt đới kéo cực mạnh Ấn Độ (*7 Indoor Plants in Water* `cTuGnXMSdnw`: **39,4% Ấn Độ vs 29,8% US**; *STOP Pesticides*: 19,1% IN + 14,5% PH vs 31,9% US). Ngược lại, **chủ đề mùa đông / làm vườn sân nhà Mỹ** khóa tệp US cực sạch:
  - *7 Cheap Root Cellar Ideas* (`x0-7HzQnLaU`): **75,1% US · 91,4% Tier-1**!
  - *Pour THIS Over Dry Leaves → Compost* (`7GzeVsMet3s`): **68,6% US · 81,9% Tier-1**!
  - *Grow Avocado From Seed* (`NmL--ywpKns`): **66,3% US · 79,6% Tier-1**!
  - *What to Plant in November — Shrug Off 28°F* (`krtVPWEZimY`): **62,7% US** (cao nhất loạt video mới nhờ mốc **28°F** chuẩn Mỹ!).

### 🔴 Nguyên nhân #4: Đợt spam **27 Shorts 9 giây rập khuôn** tháng 6/2026 + **Xóa 18 / Ẩn 9 video**
Truy vết 180 ngày từ OAuth Analytics phát hiện:
- Từ 20/06 → 27/06/2026, kênh đăng dồn dập **27 Shorts 9–11 giây** cùng 1 công thức clickbait phi khoa học (*"Why Pothos Experts Stick Vine Cuttings Inside Ripe..."*, *"Why Orchid Experts Bury Potato Peels..."*, *"Why Orchid Experts Stuff Sprout Inside Fresh Lemon"*), kéo 57.541 view tệp trẻ/non-US.
- Sau đó kênh đã **XÓA HẲN 18 Shorts** và chuyển **PRIVATE 9 Shorts**. Theo sổ tay thuật toán & `yt-channel-health-audit`, chuỗi "đăng Shorts AI rập khuôn → xóa hàng loạt" tạo rủi ro tín hiệu *Inauthentic Content* cấp kênh và làm nhiễu hồ sơ khán giả.

### 🔴 Nguyên nhân #5: **Thumbnail để AI vẽ chữ hoàn toàn** + Đóng gói sai trục (CTR video mới 2,58% vs cũ 4,35%–8,58%)
- Xác nhận vận hành từ chủ kênh: hiện đang để AI render trọn gói cả chữ trên thumbnail.
- Rủi ro kép: (1) dễ bị xếp nhóm "nội dung sản xuất số lượng / AI template" giảm ưu tiên Browse; (2) chữ AI bake hay thiếu sắc nét khi xem ở màn hình 200px Mobile lẫn 3m Smart TV; (3) nhiều video gần đây dùng chữ trừu tượng/meta (*Count This 1 Number*, *Window Test*, *One Small Study* → CTR tụt xuống 1,35%–2,22%).

### 🟡 Nguyên nhân #6: Vận hành & Metadata kênh chưa tối ưu cho mở rộng tệp Mỹ
- **Channel Keywords (YouTube Data API): TRỐNG HOÀN TOÀN (`""`)** và **`defaultLanguage = None`** (chưa khóa `en-US`).
- **Mô tả kênh** vẫn khóa cứng *"help brand-new senior gardeners... senior-first"*, tạo trần tâm lý với nhóm 35–55 tuổi.
- **2 tài khoản quản lý đăng nhập nhiều máy:** Cần xác minh 2 người đang dùng **2 Gmail riêng biệt được phân quyền Manager trên Brand Account** (AN TOÀN) hay đang **đăng nhập chung 1 Gmail chủ kênh trên nhiều máy/IP khác nhau** (RỦI RO cờ bảo mật/sandbox).
- **Phản hồi người xem trong 500 comment đã đào:** Khán giả Mỹ tinh ý phát hiện lỗi hình ảnh AI phi thực tế (*"At 6:50 the shovel is not moving in the direction of the dug-up earth — Good CGI's"*, *"Says not to root in water, at 5:35 it's in water?"* — 41 likes) và câu chuyện bà nội bịa (*"Oh, now an AI has grandmothers? Was her name ENIAC?"*).

---

## 4. Bảng chấm 5 Trục Sức khỏe Kênh (Self-Baseline · 28d vs 28d trước)

| Trục | Kỳ này (28d tới 25/11) | Kỳ trước (28d trước đó) | Biến động | Đánh giá |
|---|---:|---:|---:|:---:|
| **1. Phân phối (tuyệt đối)** | **61.992 view** (Browse 43.312 · Sug 8.039 · Search 6.099) | **82.926 view** (Browse 56.037 · Sug 12.397 · Search 8.189) | **-25,2%** (-20.934 view) | 🔴 Giảm >20% |
| **2. Giữ chân (AVD)** | **29,7%–30,7%** (US 33%, IN 19%) · AvgDur 243–247s | 28,9%–29,2% · AvgDur 241s | **+1,5 điểm** | ✅ Ổn định / đi lên |
| **3. Đóng gói (CTR video mới)** | Trung vị **2,58%** (video ≤45 ngày; catalog cũ 4,35–8,58%) | Catalog cũ chi phối 92,9% view | Thấp hơn catalog cũ **-41%** | 🔴 **Nút thắt trực tiếp** |
| **4. Thoả mãn** | `views_5d` 10 video gần nhất: **596** · Sub 28d +189 · BL/1K ~0–1,3 | `views_5d` trước đó: 543 · Sub T4 +12.353 | Phẳng ở mức thấp | ⚠️ Yếu sub & tương tác |
| **5. Nhất quán ngách & Tệp US** | **US 47,4%** (nhưng video mới chỉ **11%–30% US** do 21 ngôn ngữ + Dragon Fruit/nhiệt đới) | Đỉnh T1–T4: **53,7% US · 75,4% Tier-1 · 59,5% TV** | **Lệch tệp nặng** | 🔴 **Gốc rễ hệ thống** |

> **KẾT LUẬN CHẨN ĐOÁN:** Kênh **KHÔNG** bị tụt vì nội dung dài quá hay thiếu kỹ thuật giữ chân (AVD nhóm khán giả Mỹ đang rất khỏe: **33%–35%**!). Kênh tụt đề xuất vì **2 van bị tắc cùng lúc**:
> 1. **Van Tệp (Lệch địa lý):** Bật 19–21 ngôn ngữ localization + chọn một số chủ đề nhiệt đới đẩy video mới vào Ấn Độ/Indonesia/Nhật/Hàn (AVD 16–20%) làm bẩn tín hiệu đầu vào.
> 2. **Van Đóng gói (CTR lạnh 2,58%):** Thumbnail AI tự vẽ chữ + tiêu đề meta/trừu tượng khiến khán giả Mỹ lạnh không bấm dù YouTube vẫn thử mở rộng 10K–15K impressions.

---

## 5. THÔNG SỐ VÀNG (Tính từ dữ liệu thật 26/11/2026)

1. **Độ dài & Trải nghiệm Smart TV:** **10–12 phút (1.650–2.000 từ @165 wpm)** cho đơn chủ đề / problem-fix (views_5d trung vị ×1,59 so với >12′); listicle cao điểm có thể 12–15 phút. Chữ đồ họa siêu to, nhịp êm, âm thanh rõ để **kéo lại tệp Smart TV Mỹ (mục tiêu 29% → 45%+)**.
2. **Đóng gói (Title + Thumbnail):**
   - **Title:** Bắt buộc chứa **con số/\$ cụ thể + chủ thể Mỹ quen thuộc + lợi ích được thêm** (khung *Free / \$0 / Never Buy / Stop … Instead* theo L20), **0 từ meta** (L21), **0 nhãn tuổi** (L9).
   - **Thumbnail:** Render ảnh sạch bằng AI (**KHÔNG để AI vẽ chữ**) → **tự đắp chữ tay 2 tầng (Vàng hook + Trắng phụ, 4–6 từ, viền đen dày)** + chạy **Test & Compare 3 concept khác hẳn nhau** trên Studio.
3. **Hàng rào Khóa tệp Mỹ (US-Anchor):**
   - **Chỉ giữ duy nhất ngôn ngữ `en-US`** (tắt toàn bộ 19–20 ngôn ngữ dịch tiêu đề/mô tả trên video mới!).
   - Ưu tiên chủ thể **đóng đinh khí hậu/đời sống Mỹ**: *USDA Zones 3–8 · 28°F/Frost · Winter Sowing · Root Cellar · Amish/Homestead · Dry Leaves · Native Perennials · Raised Bed / Patio Container · Holiday Plants (Christmas Cactus / Amaryllis)*.
