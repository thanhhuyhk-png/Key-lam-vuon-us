---
file: remake-playbook-en.md
role: SOP remake video outlier của kênh khác → bài của mình. Dựng từ teardown cụm "Tastes Like Apple and Honey" (9 video, 04/09/2026).
read_by: [mkt-youtube-outline, mkt-hook-kallaway, youtube-garden-us, mkt-youtube-script-audit, garden-us-thumbnail]
token_note: Bước outline/title chỉ cần đọc §R2–R3–R5 + §Gate R7. Phần Evidence là bằng chứng.
updated: 2026-09-09
router: references/remake-archetypes-en.md  ← ĐỌC TRƯỚC khi áp R2/R3/R4
---

> 🔴 **v2 (09/09/2026) — file này là BẰNG CHỨNG + gói khuôn A1, KHÔNG phải luật chung cho mọi seed.**
> §R2 (mảnh sensory) · §R3 (đổi cây) · §R4 (listicle đếm ngược) đều rút từ **một** cụm teardown, nên chỉ
> đúng với seed dạng **A1 — Sensory Heritage Listicle**. Seed dạng khác (hạn chót theo mùa · 1 kỹ thuật đơn ·
> lệnh cấm · phán quyết xếp hạng · port ngách khác) dùng **bản tổng quát + gói riêng** ở
> `references/remake-archetypes-en.md`. §R0 · §R5 · §R6 · §"đọc số sau khi đăng" vẫn đúng cho mọi archetype.
>
> 🧪 **Luật teardown lần sau (12/10/2026):** teardown 1 kênh đối thủ = **3 video thắng + 2 video TRƯỢT** của
> **cùng kênh đó**, video trượt phải **≥2 tuần tuổi**. Câu hỏi chính: thắng và trượt khác nhau ở đâu
> (title/góc · hook · cấu trúc · thumbnail)? Không có nhóm đối chứng thì mọi luật rút ra chỉ ở cấp
> 🧪 TESTING trong `lessons-learned.md`. Học XƯƠNG (cấu trúc, nhịp), không chép DA (phong cách hình).

# Remake Playbook — Garden US

> Nguồn: teardown 9 video cùng title stem "Tastes Like Apple and Honey…", đo bằng vidIQ
> (view theo ngày, transcript đầy đủ, thumbnail, channel growth). Ngày chốt số: 2026-09-04.

## 0. Bảng sự thật — cụm 9 video

| Kênh | Sub | Đăng | Dài | View | Định dạng | Cây |
|---|---|---|---|---|---|---|
| Botanical Vault *(gốc EN)* | 24.3K | 17/04 | 16:55 | **640,032** | 1 cây, how-to, ngôi 1 | yacón |
| The Green Archive | 26.3K | 18/04 | 11:53 | 1,911 | copy | yacón |
| Censored Soils | 4.06K | 27/06 | 14:57 | 7,459 | viết lại, US-conspiracy | yacón |
| **Silas Mercer Farmstead** | 43.3K *(7.5K lúc đăng)* | 13/08 | 39:02 | **509,581** | listicle 25 mục + persona bịa | **skirret** |
| Elias Gardener | 4.33K | 14/08 | 21:54 | 21,435 | listicle "Amish" | skirret |
| Grow Simple | 1.85K | 20/08 | 9:39 | 1,361 | copy | yacón |
| **No Longer Here** | 204K *(190K lúc đăng)* | 22/08 | 31:32 | **1,560,118** | listicle 20 mục, ngôi 2 | **skirret** |
| Garden Explained w/ Harry | 17.2K | ~27/08 | 16:38 | 10,443 | copy | yacón |
| Botanical Vault *(tự remake)* | 24.3K | 30/08 | 15:55 | **1,061** | **re-upload nguyên văn** | yacón |

**Phát hiện lõi:** hai bản thắng lớn KHÔNG remake về yacón. Họ giữ lời hứa vị, **đổi vật chủ sang skirret**
(cây có trong catalog hạt giống Mỹ đến 1902, người Pennsylvania Dutch trồng) rồi **đổi định dạng
từ 1-cây-how-to sang danh sách đếm ngược 20–25 mục**, đặt payoff của title ở **#2**.

---

## R0 — Săn hàng tuần: tìm video ĐANG được đẩy (không phải video ĐÃ to)

> ⛔ **ĐÃ NGỪNG 18/11/2026.** Không chạy R0 (`vidiq_outliers sort=vph`) nữa. Tìm video đang được đẩy bằng `tools/do_trend.py` (0 credit, tốc độ view đo thật qua hai lần chụp) — xem `references/topic-gate-en.md` ②. Phần dưới giữ làm bằng chứng vì sao `vph` không dùng được.

**Cơ chế:** `viewCount` là lịch sử — nó nói chuyện đã xảy ra. `vph` (views per hour) là **tốc độ hiện tại** —
nó nói YouTube có đang mở van hay không. Hai con số này thường ngược nhau.

| Video | Tổng view | `vph` hiện tại | Đọc ra |
|---|---|---|---|
| `GzKzYG2qajM` bản gốc | 640,032 | **26** | Chết. Sống bằng đuôi dài. Remake bây giờ = remake một xác. |
| `2CNq-yl6WMA` bản 1.56M | 1,560,118 | **3,070** | Còn nóng nhưng đang hạ (đỉnh 12,703 ở ngày 9). |
| `GEQKrSglRAM` Silas · "Painkiller" | 592,734 | **3,159** | 🔥 Đang được đẩy mạnh nhất toàn mẫu. |
| `pj03vcxCkJo` Silas · "Tastes Like Lemonade" | 63,571 | **1,031** | 🔥 Đang lên — mới 63K nhưng tốc độ gấp **39×** bản 640K. |
| `D0Zywpdrfxs` Silas · "14 Plants Worth More Than Gold" | 63,755 | **896** | 🔥 Đang lên. |
| `popMtz1L9dQ` Censored Soils | 7,459 | **4.96** | Chết hẳn. |

> **Luật R0:** sort theo `vph`, **đừng sort theo `viewCount`** — nhưng chỉ dùng `vph` để **XẾP HẠNG**,
> ⛔ **KHÔNG dùng để CHẤM ĐẬU**. Lý do ở khối đỏ ngay dưới.

### 🔴 HAI LỖI CHÍ MẠNG VỀ `vph` — sửa 04/09 sau khi đo hụt

**Lỗi 1 — `vph` trong `outliers` / `similar_videos` KHÔNG ĐÁNG TIN.**
`vrvLNbIL7tk` được trả về `vph 409.97`. Kéo `video_stats` theo ngày: **vph thật = 4,09**. Sai **100 lần**.
Kiểm chéo bằng kênh: cả kênh chỉ +20.122 view/30 ngày, mà vph 410 thì riêng video đó phải đẻ ~295.000 view/tháng — bất khả.

> ⛔ **KHÔNG BAO GIỜ** nhận seed dựa trên `vph` từ `outliers`/`similar_videos`.
> **BẮT BUỘC** chạy **lượt 3** (`vidiq_video_stats granularity:"daily"`) trước khi cho seed vào kho.

**Lỗi 2 — ngưỡng `minVph ≥ 200` là bịa, và nó loại chính seed đã thắng.**
`GzKzYG2qajM` — seed đẻ ra **cả 509K lẫn 1,56 triệu** — có `vph` chỉ **26–83** lúc được remake.

### ✅ Ngưỡng ĐÚNG: tốc độ tích luỹ tháng, không phải vph

```
monthly_growth_pct = (view tăng trong 30 ngày) / (tổng view) × 100
```

| Video | +30 ngày | % tổng | Trạng thái |
|---|---|---|---|
| `GzKzYG2qajM` *(seed đẻ 2 bản thắng)* | +55.000 | **8,6%** | ✅ CÒN SỐNG |
| `vrvLNbIL7tk` *(tôi từng đề xuất nhầm)* | +8.652 | **1,0%** | ❌ đuôi dài |
| `popMtz1L9dQ` *(bản chết)* | +2 | **0,03%** | ❌ chết |

| Ngưỡng | Verdict |
|---|---|
| **≥ 5%/tháng** | ✅ NHẬN — còn được phân phối |
| 1–5%/tháng | ⏳ THEO DÕI — đang tắt dần |
| **< 1%/tháng** | ❌ BỎ — đuôi dài, remake một cái xác |

`minVph` trong truy vấn giữ ở mức **thấp** (≈50) chỉ để cắt rác, **không phải để chấm đậu**.

### ⚠️ Hai lỗi đã sửa ngày 04/09 — đọc trước khi chạy

| Lỗi | Sai ở đâu | Đã sửa thành |
|---|---|---|
| **Cửa sổ tự đá nhau** | R0 quét `publishedWithin:"thisMonth"` nhưng R1 đòi seed **60–150 ngày**. Video ≤30 ngày **không bao giờ** qua nổi cổng R1. | `publishedWithin:"sixMonths"` + `minVph` cao = "đã chín mà **vẫn** đang được đẩy" |
| **Keyword là nam châm rác** | `forgotten` / `old` hút cả YouTube. Quét thật trả về nhạc thiếu nhi *Old MacDonald*, phim ngắn TQ, mộ sao Hollywood, nước hoa, Runescape. | Bỏ quét keyword rộng làm lượt chính. Dùng **`vidiq_similar_videos` seed từ video thắng đã biết** — nhắm cả title lẫn thumbnail |

### 📉 Cung thật của ngách — đo ngày 04/09

Quét 85 kết quả (2 lượt outliers + 1 lượt similar_videos). Số video vừa **đúng ngách/liền kề**,
vừa **60–150 ngày**, vừa `vph` đủ cao, vừa kênh < 60K sub: **1**.

> **Ngách chỉ đẻ 0–2 seed/tuần.** Ép quét 3–4 seed/tuần không sinh thêm seed — nó chỉ sinh ra
> việc hạ chuẩn, và hạ chuẩn là đúng cách Botanical Vault nhận 1.061 view.
> ⇒ Vì vậy R0 tách làm **hai cuộc săn**, không phải một.

---

### R0-A — SĂN SEED (remake đúng seed) · hiếm, 0–1/tuần

**Lượt 1.** `vidiq_similar_videos` seed từ **video thắng đã biết** của ngách (bắt đầu bằng `2CNq-yl6WMA`):

```
matchOn: "both" · publishedWithin: "sixMonths" · minEngagementRate: 0.015
maxSubscribers: 60000 · excludeSeedChannel: true · limit: 45
```

Nhắm cả **title lẫn thumbnail** nên bám ngách chặt hơn keyword rất nhiều.

**Lượt 2.** `vidiq_outliers` bổ sung, chỉ khi cần mở rộng — **bắt buộc** `requireAllTitleTerms: true`,
keyword là **cụm hẹp** (`gardening tricks grandparents`, `perennial vegetables plant once`),
`publishedWithin: "sixMonths"`, `sort: "vph"`, `maxSubscribers: 60000`.

**Lượt 3.** `vidiq_video_stats granularity:"daily"` cho top 3 → đọc đường cong. Chỉ nhận **NỞ** hoặc vừa qua đỉnh.

---

### R0-B — SĂN KHUÔN (port từ ngách liền kề) · dồi dào, 1–2/tuần

**Phát hiện 04/09:** thứ mạnh nhất trong dữ liệu **không phải video làm vườn** — là **cái khuôn**
(`số đếm + Forgotten/Grandma + thủ phạm kinh tế mềm`) đang chiếm bếp núc, săn bắn, sửa nhà, làm đẹp, dọn dẹp:

| Video | Kênh | Sub | View | breakout |
|---|---|---|---|---|
| *Why Grandma Boiled Dish Rags (And Why I Tried It)* | Tales From the Mutiny | 7,62K | **844.171** | **1.823** |
| *25 Forgotten Diner Sandwiches America Used to Order Every Day* | Retro State | 9,19K | 673.367 | **863** |
| *NEVER Grill Your Steak Again — 80-Year-Old Grandma Butcher's Method* | Margret Miller | 13,1K | 445.341 | **3.470** |
| *25 FORGOTTEN Farmhouse Skills Every American Family Knew 100 Years Ago* | Forgotten American Skills | 28,3K | 137.992 | 28 |
| *STOP Boiling & Frying Eggs The OLD WAY! 45 Appalachian Tricks* | Opal Rowe | 23,7K | 151.554 | 16,9 |
| *20 Old-House Drainage Tricks Modern Builders Quietly Abandoned* | Forgotten Home Engineering | 6,04K | 55.215 | 8,1 |

> **Tài sản trao đổi được là CÁI KHUÔN, không phải cái seed.** Port khuôn vào vườn thì mỏ không cạn,
> và **không phải chen cửa sổ** với 5 bản clone khác.

**Cách chạy:** `vidiq_outliers` với `publishedWithin:"threeMonths"`, `sort:"vph"`, `maxSubscribers:60000`,
keyword theo **ngách liền kề** — `appalachian cooking tricks` · `forgotten farmhouse skills` ·
`old house tricks builders abandoned` · `grandma kitchen tricks`.

**Port sang vườn theo 3 bước:**
1. Giữ **khung câu** của title gốc, thay danh từ sang vườn
   *(“Why Grandma Boiled Dish Rags” → “Why Grandma Buried Eggshells Under the Tomatoes”)*
2. Giữ **5 nhịp/mục** và **micro-bridge** (R4) nguyên vẹn
3. Thủ phạm phải là **sự kiện lịch sử vườn** tra được (catalog Ferry-Morse bỏ skirret 1902 ·
   Earl Butz 1971 · ammonium nitrate 1947), ⛔ không mượn thủ phạm của ngách gốc

⚠️ **Không port** ngách YMYL: sức khỏe/thuốc/da liễu (`X3`), và ⛔ không port title có nhãn tuổi
người xem kiểu `OVER 60?` (`L9`) — kể cả khi bản gốc thắng nhờ nó.

### Nhảy vào lúc nào

| Ai | Vào sau seed gốc | Số clone lúc vào | Kết quả |
|---|---|---|---|
| Silas Mercer | **D+118** | 1 | 509,581 |
| No Longer Here | D+127 *(D+9 sau Silas)* | 2 | **1,560,118** |
| Botanical Vault | D+135 | **6** | 1,061 |

> **Cửa sổ: 60–150 ngày sau seed gốc VÀ ≤2 clone đã đăng.** Quá sớm thì seed chưa chứng minh;
> quá muộn hoặc quá đông thì thuật toán đã bão hoà chủ đề.

Output tuần: ghi 3 seed tốt nhất vào `research/seed-radar-YYYY-Www.md` — mỗi seed kèm
`videoId · vph · breakoutScore · view/sub · tuổi · số clone · đường cong`.

---

## R1 — Săn seed (chọn video để remake)

Lọc bằng `vidiq_outliers` / `vidiq_similar_videos`, giữ seed đạt **cả 5**:

- `breakoutScore` ≥ 15 → video vượt xa mức thường của chính kênh nó
- `views / subscriberCount` ≥ 5× → thắng nhờ **packaging**, không nhờ authority kênh
- Tuổi 60–150 ngày → đủ chín để loại flash, chưa bão hoà
- Kênh gốc < 50K sub → chứng minh title tự bán, không cần thương hiệu
- Đếm clone đã đăng 14 ngày gần nhất: **≥3 clone = cửa sổ đang đóng** → phải mutate mạnh hơn (R3+R4 bắt buộc), hoặc bỏ

*Seed thực tế:* `GzKzYG2qajM` — breakout 188, 640K trên 24.3K sub (26×), 118 ngày tuổi khi Silas remake.

> ⚠️ **Thay `vph` bằng `monthly_growth_pct`** khi chấm đậu — xem khối đỏ ở §R0. `vph` chỉ để xếp hạng.

### R1-OVERRIDE — khi user cố tình chạy seed trượt ngưỡng

Ngưỡng R1 là **hiệu chỉnh rủi ro**, không phải luật vật lý — `remake-002` chạy với seed 16 ngày tuổi,
kênh gốc 103K sub, vì đường cong đang tăng tốc và 2 bản EN hiện có đều đóng gói kém. Điều đó **được phép**,
với 4 điều kiện ghi vào `seed-brief.md` khối OVERRIDE:

1. Ghi rõ **tiêu chí nào trượt** và **đánh đổi** là gì
2. Ghi **rủi ro chấp nhận** — thứ có thể sai
3. Viết sẵn **câu hỏi cho retro** — retro bắt buộc trả lời và đẩy kết luận vào `lessons-learned.md`
4. ⛔ Override **không áp dụng** cho bộ lọc SEED PHẢI BỎ (X1 · X3 · X4 · X5 · L9) — cái đó là luật, không phải ngưỡng

---

## R1.5 — Phân loại archetype 🔴 *(bước mới, v2)*

Trước GATE 0, chạy bộ 5 câu hỏi ở `remake-archetypes-en.md` §2 để biết seed thuộc gói nào (A1–A6),
rồi nạp đúng gói đó cho R2/R3/R4/[1.5]/[2.5]/Pha D/R7. **Bỏ bước này = mặc định coi mọi seed là A1** —
đó chính là lỗi khiến `remake-001` và `remake-002` phải override thủ công.

---

## R2 — Giải phẫu lời hứa (Promise Autopsy) · *gói A1 — bản tổng quát ở §1.1 file archetypes*

> **Bảng mổ xẻ chuẩn (2026-10-23):** ngoài tài sản, R2 điền `seed-brief.md §2B` — điểm giữ chân theo mốc giây ·
> chuyển đoạn · nỗi đau · **sổ claim của seed** (bàn giao [1.5]). Transcript seed lưu `seed-transcript.txt` cùng folder.

Chẻ title gốc làm 3 mảnh, xử lý khác nhau:

| Mảnh | Ví dụ | Xử lý |
|---|---|---|
| **Sensory** *(tài sản)* | "Tastes Like Apple and Honey" | 🔒 **GIỮ NGUYÊN CHỮ.** Cả trong title **và trên thumbnail.** |
| **Condition** | "Grows Wild Without Care" / "Plant Once" | ✏️ Được mutate |
| **Open question** | "Why Does Nobody Plant It?" | ✏️ Được mutate |

**Bằng chứng 2 chiều:**
- 3/3 video thắng **giữ** mảnh sensory trên thumbnail (640K · 509K · 1.56M)
- 2/2 video xoá mảnh sensory khỏi thumbnail đều chết: Censored Soils đổi thành `SWEETER THAN SUGAR`
  → 7,459 view; Botanical Vault v2 đổi thành `PLANT ONCE FORGET IT` → **1,061 view**

> ⚠️ Mảnh sensory là thứ thị trường đã trả tiền để chứng minh. Sửa nó = ném đi toàn bộ bằng chứng.

---

## R3 — Đổi vật chủ (Subject Swap) — bước quyết định nhất · *gói A1 — bản tổng quát (One-Axis Rule) ở §1.2 file archetypes*

|  | Yacón *(gốc)* | Skirret *(bản thắng)* |
|---|---|---|
| Xuất xứ | Andes, Peru/Bolivia | Châu Âu → catalog hạt giống Mỹ đến **1902** |
| Người Mỹ 60–80 nhận ra | Không | "Bà tôi **có thể** đã trồng" |
| Có ký ức để móc vào | ❌ | ✅ |
| Đơn vị đo trong script | kg, mét, cm | pound, feet, inch |

**Luật R3:** chủ thể gốc exotic → tìm chủ thể **bản địa / di sản** cho **cùng một lời hứa cảm giác**.

> Đây chính là **L1** của kênh ("đừng chọn cây exotic người Mỹ không biết → AVD chết")
> được xác nhận lại ở quy mô 1.56M view, bởi một kênh ngoài.

---

## R4 — Nâng cấp định dạng: 1 cây → danh sách đếm ngược · *gói A1 — các gói khác có bộ xương riêng*

Đây là chỗ chênh 640K vs 1.56M.

- **Gốc:** 1 cây · 17′ · 1 lời hứa → hết lời hứa là hết lý do ở lại.
- **Bản thắng:** 20 mục · 31′ · lời hứa của title nằm ở **#2** → người xem phải ở lại **28 phút** mới lấy được thứ họ vào để lấy.

### Bộ xương chuẩn (copy được)

| Vị trí | Việc |
|---|---|
| 0:00–0:50 | **Cold open**: đọc thẳng mảnh sensory (đúng chữ trong title), rồi **mở 3 vòng lặp bằng số thứ tự** — *"Number 16 tastes like fried oysters and it never once saw the ocean. Number 12 is why Congress stepped in on Christmas Eve 1970. And number 2 is the root that tastes like apple and honey."* |
| Mỗi mục | **5 nhịp cố định**: [hình ảnh bà/ông + nó cho cái gì] → [ai/cái gì giết nó, **có năm cụ thể**] → [hôm nay cửa hàng bán bao nhiêu **$**] → [1 *honest note* an toàn] → [**micro-bridge** sang mục sau] |
| Micro-bridge | **20/20 mục đều có, không ngoại lệ**: *"The next one plants itself, and then it walks."* · *"The next one is the hottest thing your grandmother ever kept in a jar."* |
| 1/4 · 1/2 · 3/4 | **Pattern break**: dừng đếm, tuyên bố lại phần thưởng còn lại (*"Three left. Number five rebuilds the ground under your feet. Number two is the root off the top of this whole thing."*) |
| Giữa video | **Comment bait ký ức**: *"Did your grandmother bake on the same day every week? Tell me which day it was down in the comments."* |
| **#2** | Payoff của title. Trả đúng chữ đã hứa. |
| **#1** | **Không phải một cây.** Là toàn bộ cái vườn sau nhà bà đứng cùng lúc → identity close. |
| CTA | *"Pick one. Not the whole list. One."* — hành động nhỏ nhất có thể làm hôm nay. |

**Kết quả đo được của bộ xương này:** top comment 1,042 like là một người **tự chép lại cả danh sách** —
danh sách tạo giá trị lưu trữ, giá trị lưu trữ tạo comment, comment tạo tín hiệu.

---

## R5 — Thumbnail: giữ chữ, đổi ảnh

| Video | Ảnh | Chữ | View |
|---|---|---|---|
| Gốc 640K | củ AI dính đất + mật chảy, bàn tay | `TASTES LIKE APPLE AND HONEY` / `NOBODY PLANTS IT` | 640,032 |
| Censored Soils | **cùng ảnh AI đó** | `SWEETER THAN SUGAR` / `NOBODY STOCKS IT` | 7,459 |
| Botanical Vault v2 | **cùng ảnh AI đó** | `PLANT ONCE FORGET IT` / `EAT SWEET ALL YEAR` | **1,061** |
| Silas 509K | **thêm mặt ông già râu bạc, mũ da** | `TASTES LIKE APPLE AND HONEY` / `NOBODY PLANTS IT` | 509,581 |
| NLH 1.56M | **bà cụ thật, kính, dao cắt củ, mật chảy, mũi tên đỏ, đống củ** | `TASTES LIKE APPLE AND HONEY` / `NOBODY GROWS IT NOW` | 1,560,118 |

**Luật R5:** **giữ chữ — làm ảnh MỚI.** Làm ngược lại (giữ ảnh, đổi chữ) = 1,061 view.
Chữ 2 tầng bắt buộc: **tầng vàng = mảnh sensory**, **tầng trắng = mảnh phủ định**.

> ⚠️ **Đính chính (bản đầu nói quá).** Biến thật sự phân biệt là **ảnh mới vs ảnh dùng lại**,
> KHÔNG phải có-mặt-người vs faceless. Bằng chứng: bản gốc 640K **faceless** và vẫn thắng;
> 3/3 bản chết đều **dùng lại y hệt** file ảnh AI của bản gốc; 3/3 bản thắng đều có **ảnh riêng**.
> Mặt người xuất hiện ở 2 bản thắng nhưng bị lẫn với hàng loạt biến khác (kích cỡ kênh, định dạng,
> độ dài) → **chưa cô lập được, không đủ tư cách thành luật**.
> ⇒ Với Garden US: **giữ nguyên luật FACELESS** (`thumbnail-stats`: 14/14 thumbnail top không có mặt người).
> R5 chỉ yêu cầu ảnh phải do mình dựng mới, không tái sử dụng ảnh của seed.

---

## R6 — Chân dung người kể: ký ức NGƯỜI XEM > tiểu sử NGƯỜI KỂ

Hai bản thắng chạy **gần như cùng một script** (trùng cả câu: *"That is not a hobby. That is not a lifestyle."*
· *"Pick one. Not the whole list. One."*). Khác nhau ở 4 điểm — và chênh **3×**:

| | Silas Mercer 509K | No Longer Here 1.56M |
|---|---|---|
| Người kể | Bịa danh tính: *"I'm Silas Mercer, seventh generation on this ridge"* + ông nội "Eli" | **Không nhân vật.** Ngôi thứ 2: *"your grandmother"* |
| Bán hàng | Chèn pitch sách 904 trang ở **phút 2** | **Không bán gì** |
| Nội dung | Thêm dê sữa, mổ heo, sữa tươi, gà, ong | **Cắt sạch livestock/butchery** — chỉ cây + kỹ năng bếp |
| Cảm xúc mở đầu | Doom: *"there's something coming for this country"* | Hoài niệm thuần, **không doom** |
| Like rate | 2.81% *(fan nóng, tệp hẹp)* | 1.30% *(tệp rộng, lạnh)* |
| Đường cong | Bùng ngày 1–3, **chững ngày 6** | 24h thấp, **nở liên tục 9 ngày** |

**Luật R6:** ký ức mà **ai cũng có** (bà, cái vườn, mùi bánh mì thứ Bảy) mở rộng được impressions.
Tiểu sử người kể chỉ chạm fan. → **Clone No Longer Here, đừng clone Silas Mercer.**
Bonus: NLH không vi phạm **X5** (narrator tự trồng); Silas vi phạm nặng.

---

## R7 — Gate trước khi đăng (fail 1 = không đăng)

Gate chia 2 tầng: **6 điểm CHUNG** cho mọi archetype + **delta** của gói đang chạy.

### R7-CORE — 9 điểm, mọi archetype

- [ ] **Tài sản đã-trả-tiền nguyên văn** trong title **và** trên thumbnail *(§1.1 archetypes)*
- [ ] Đã đổi **đúng một trục**, và vật chủ mới quen với khán giả Mỹ 60–80; đơn vị đo là pound/feet/inch/gallon *(§1.2, L1)*
- [ ] **Nợ giao hàng đã trả** bằng đúng cơ chế của gói (loop số / lời hứa thứ hai / cơ chế-trước-list) *(§1.3)*
- [ ] Mỗi claim mạnh có **năm + tên + tổ chức tra được**. ⛔ Cấm "họ giấu bạn" *(X1, CR11 soft-economics)*
- [ ] Ngôi thứ 2 xuyên suốt; **0 câu** "I grew / I tested / in my garden" *(X5, Narrator Integrity)*
- [ ] Title dùng **tuổi của NGUỒN** (`Grandma…` · `Our Grandparents…`), **không** tuổi người xem *(L9/L9b)*
- [ ] Thumbnail **FACELESS** *(luật kênh — 14/14 thumbnail top)* · ảnh **dựng mới**, ⛔ cấm tái sử dụng ảnh của seed *(R5)*
- [ ] Mỗi mục/beat rủi ro có **honest note** riêng 1 nhịp (lá rhubarb · wild parsnip · vỏ/hạt pawpaw) *(CR5)*
- [ ] **Khác câu chữ seed** *(2026-10-23)*: `python tools/originality_check.py <script.md> --allow "<tài sản khoá>"` → exit 0 —
      tự đọc `seed-transcript.*` trong folder; ≤1 câu trùng nguyên văn và ≤2% 6-gram của script có trong seed. Mọi đoạn trùng
      ≥8 từ được liệt kê → viết lại đúng đoạn đó. Đường vào C không tìm ra nguồn → vẫn so với mẫu user dán (lưu làm `seed-transcript.txt`)

> ⚠️ **Đính chính 09/09:** bản v1 của gate này ghi *"thumbnail có khuôn mặt người già thật"* — mâu thuẫn với
> chính phần đính chính ở §R5 và với luật FACELESS của kênh. Biến thật sự phân biệt là **ảnh mới vs ảnh dùng lại**.
> Dòng cũ đã bị thay. Nếu thấy checklist nào còn đòi mặt người → đó là bản cũ, bỏ.

### R7-DELTA — theo gói archetype

Chép các dòng delta của gói đang chạy từ `remake-archetypes-en.md` §3 (hàng "R7 thêm"). Ví dụ gói A1:

- [ ] Payoff của title nằm ở **#2**, không phải #1 và không phải mở đầu *(R4)*
- [ ] Cold open mở **≥3 vòng lặp bằng số thứ tự** trong 50 giây đầu *(R4, L4)*
- [ ] **Mọi** mục kết bằng micro-bridge — đếm đủ, 0 ngoại lệ *(R4)*
- [ ] Mỗi mục có **1 con số $ hiện tại** của cửa hàng *(CR6)*

---

## Slot vào pipeline có sẵn — nhánh REMAKE

Pipeline Garden US **giữ nguyên 5 bước + GATE**. Remake là một **nguồn đầu vào thứ hai**
(song song Notion Big Idea), rẽ nhánh ở đúng **3 bước**, còn lại dùng chung.

> 🔴 **v2:** bảng dưới mô tả nhánh cho gói **A1**. Với seed dạng khác, cột "Nhánh REMAKE" lấy từ
> `remake-archetypes-en.md §3` — mỗi gói khai đúng 8 biến (tài sản khoá · trục đổi · bộ xương · nhịp ·
> spine template · tải [1.5] · Pha D thêm · R7 thêm). Những bước gói không nhắc = giữ nguyên pipeline chuẩn.

| Bước hiện có | Nhánh REMAKE | Mức đổi |
|---|---|---|
| **Bước 0** đọc Big Idea từ Notion | Đọc **seed** từ `research/seed-radar-YYYY-Www.md` (R0) → viết `seed-brief.md` vào folder video | 🔁 **Đổi nguồn** |
| **[1]** `mkt-youtube-outline` | Dùng nguyên. Title Hybrid chạy như thường, **thêm 1 ràng buộc**: mảnh sensory của seed khoá cứng, chỉ mutate mảnh condition + question *(R2)*. Chốt vật chủ bản địa *(R3)* | 🟡 Thêm ràng buộc |
| **[1.5]** `mkt-youtube-deep-research` | ⚠️ **Nặng gấp ~4 lần.** Listicle 15–18 mục cần mỗi mục: 1 năm cụ thể + 1 tên tổ chức + 1 giá $ hiện tại ≈ **45–54 fact có nguồn**, thay vì 5 câu hỏi như thường lệ. `garden-deep-researcher` phải chạy **theo lô mục**, không chạy 1 lượt | 🔴 **Đổi tải trọng** |
| **[2]** `mkt-hook-kallaway` | Dùng nguyên. SSSQ **không bị vi phạm**: single question vẫn là *"cái gì tastes like apple and honey"*, 15–18 mục là **đường đi tới câu trả lời**. Thêm ràng buộc R4: cold open mở **≥3 vòng lặp bằng số thứ tự** trong 50s | 🟡 Thêm ràng buộc |
| **[2.5]** Retention Spine | 🔴 **Đổi trục bảng.** Bảng Spine hiện tại kẻ theo **mốc thời gian tuyệt đối** (0:40–0:55, phút 4–6) — thiết kế cho video 1 chủ đề. Listicle phải kẻ theo **mục**: mỗi mục 1 hàng × cột `[tên mục][5 nhịp][micro-bridge][vị trí #]`. Xem template bên dưới | 🔴 **Đổi cấu trúc** |
| **[3]** `youtube-garden-us` | Dùng nguyên, viết bám bảng mục. **Signposting cho seniors** mà Pha C đã yêu cầu (*"here's the second one"*) chính là bộ đếm listicle → khớp sẵn, không phải thêm | ✅ Khớp sẵn |
| **audit** `mkt-youtube-script-audit` | Đọc thêm **gate R7 (11 điểm)** cạnh ACTIVE RULES | 🟡 Thêm input |
| **Pha D verify** | Thêm 1 phép đếm cơ học: `số micro-bridge == số mục` *(0 ngoại lệ)* | 🟡 Thêm 1 check |
| **thumbnail** `garden-us-thumbnail` | ✅ **Không đổi.** Luật FACELESS giữ nguyên (xem đính chính R5). Chỉ thêm: ⛔ cấm tái sử dụng ảnh của seed | ✅ Không đổi |
| **[4a/b/c]** SEO EN + ES | ✅ Không đổi | ✅ |
| **[5][6]** prediction / retro | Không đổi quy trình, **đổi thước chấm**: `views_5d` vs `median_5d_views` (285) + tổng giờ xem. ⛔ Không chấm bằng AVD | 🟡 Đổi metric |

### Bảng Spine biến thể LISTICLE (thay Pha B khi chạy nhánh remake)

Giữ nguyên 2 checkpoint đầu của kênh — chúng thuộc về cold open, không thuộc về thân bài:

| Mốc | Giữ nguyên từ Pha B |
|---|---|
| giây 0–25 hook cliff | -37% trung bình → cold open phải đọc thẳng mảnh sensory |
| 🔴 giây 20 **L6** | claim sốc phải có bằng chứng/số trước giây 20 |
| 🔴 giây 40–55 **L4** | loop còn sống — ở đây là **3 vòng lặp số thứ tự**, không phải intro |

Từ đó trở đi, **L5 (mid-roll dip phút 4–6) được thay bằng luật mục**:

| Cột | Nội dung |
|---|---|
| `#` | vị trí trong đếm ngược (payoff title = **#2**) |
| `Mục` | tên item |
| `5 nhịp` | hình ảnh bà → nó cho gì → ai giết nó *(năm + tên + tổ chức)* → giá $ hôm nay → lưu ý an toàn |
| `Micro-bridge` | câu bắc cầu sang mục sau — **bắt buộc, 0 ngoại lệ** |
| `Pattern break` | đánh dấu ở 1/4 · 1/2 · 3/4: dừng đếm, tuyên bố lại phần thưởng còn lại |

> **Vì sao đổi được:** drop zone của listicle không nằm ở phút 4–6 mà nằm ở **mọi ranh giới giữa 2 mục**.
> Micro-bridge chính là vá cho drop zone đó — nên nó phải phủ 100% ranh giới, không phải phủ 1 mốc.

### Model routing cho nhánh remake

`channel.config.json` hiện để `deep_research: haiku`. Với tải 45–54 fact có nguồn, haiku sẽ ra research mỏng
và đó đúng là chỗ công thức này gãy. **Đề xuất: nhánh remake bump `deep_research` lên `sonnet`.**
Các bước khác giữ nguyên map hiện tại.

---

## Đọc số sau khi đăng — 3 đường cong

| Đường cong | Dấu hiệu | Việc phải làm |
|---|---|---|
| **NỞ** *(NLH)* | 24h chỉ 1,848 view (1% sub) → ×10 mỗi ngày 3 ngày → đỉnh VPH **12,703 ở ngày 9** | Không sửa gì. Chỉ trả lời comment. Đây là browse/suggested đang mở rộng theo từng sóng impressions. |
| **CHÁY NHANH** *(Silas)* | 24h **12,633 view = 168% sub** → đỉnh ngày 2–3 → chững ~400K ngày 6 | Sub yêu, browse không mở rộng. Đòn bẩy tiếp theo là **thumbnail rộng hơn**, không phải script. |
| **CHẾT** *(Censored Soils)* | ngày 12 đứng ở 7,3xx rồi **VPH = 0 suốt 2 tháng** | Không cứu được. Đừng đổi title. Làm bài mới. |

---

## ⚠️ Sự thật khó chịu — tỷ lệ trúng và độ suy giảm

- **No Longer Here**: median video ≈ 1.5–2.5K view. Bài 1.56M là **~1/50**, cỡ 600–1000× median.
- Bài kế **cùng công thức** — *"Better Than Potatoes. Grandma Planted It Once…"* (03/09, 30:02) = **2,496 view**.
- Dùng lại chính title stem: NLH *"Tastes Like Lemonade…"* = **13,204** *(giảm 118×)*.
  Silas *"Tastes Like Lemonade…"* = **63,571** *(giảm 8×)*.

> **Title stem không phải tài sản.** Tài sản là *packaging × vật chủ × thời điểm*. Lần dùng thứ hai suy giảm 8–120×.
> ⇒ Remake là chiến lược **volume**, không phải chiến lược **một phát ăn ngay**. Và phải chấm bằng
> `views × AVD × duration` hoặc `views_5d` vs `median_5d_views`, **không chấm bằng AVD**.

---

## Xung đột với luật hiện hành của kênh — cách xử lý

| Xung đột | Phán quyết |
|---|---|
| **L7** cấm >10′; bản thắng 31–39′ | L7 rút từ **how-to 1 chủ đề** (pad = chết). Listicle đếm ngược có kiến trúc giữ chân **khác**: mỗi mục là một open loop mới. **Đừng nhảy 10′→31′.** Test có kiểm soát: 1 video listicle **18–22′**, đo bằng `views_5d` vs `median_5d_views` (285) và tổng giờ xem. |
| **X1** cấm conspiracy; bản thắng có "ai giết nó" | Bản thắng dùng **soft-economics + sự kiện lịch sử tra được** (PVPA 1970, Earl Butz 1971, Crisco 1911, Chicken of Tomorrow 1948) — đúng **CR11 bản SOFT**. ✅ Được dùng, với điều kiện năm + tên + tổ chức. ⛔ Cấm "họ giấu bạn". |
| **X5** cấm narrator tự trồng | NLH **không vi phạm** (ngôi 2). Silas vi phạm nặng. → clone NLH. |
| **L9b** tuổi của NGUỒN | *"Grandma Planted It Once"* = tuổi của NGUỒN → **1.56M**. Đây là bằng chứng ngoài mạnh nhất hiện có cho L9b. |

---

## Evidence — số thô

**Đường cong view/ngày (vidIQ, granularity=daily):**

- `2CNq-yl6WMA` (NLH): 1,848 → 19,960 → 96,542 → 194,476 → 290,082 → 480,608 → 712,407 → 925,483 → 1,188,025 → 1,344,529 → 1,450,625 → 1,507,465 → 1,543,050. VPH đỉnh 12,703 (ngày 9).
- `eosvndgjLwY` (Silas): 12,633 → 149,421 → 218,413 → 316,077 → 363,108 → 388,525 → … → 507,692. VPH đỉnh 5,645 (ngày 1).
- `popMtz1L9dQ` (Censored Soils): 161 → 1,539 → 3,074 → 4,290 → … → 7,307 (ngày 12) → 7,459 (69 ngày). VPH = 0.
- `UZuiqrU51C8` (BV re-upload): 277 → 552 → 688 → 839 → 1,022 (5 ngày).

**Tăng trưởng kênh 30 ngày (05/08 → 04/09):** Silas Mercer 3,550 → **43,300 sub** trên **46 video/30 ngày**
(≈1.5 video/ngày) — mô hình volume farm, có 2 video >500K. No Longer Here 184,000 → **204,000 sub**,
+2.51M view, trong đó **1.56M đến từ một video** (62% cả tháng).
