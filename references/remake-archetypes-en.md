---
file: remake-archetypes-en.md
role: BỘ ĐỊNH TUYẾN KHUÔN (Archetype Router) cho LANE B — REMAKE. Quyết định seed thuộc dạng nào, rồi nạp đúng gói luật cho R2/R3/R4/[1.5]/[2.5]/Pha D/R7.
read_by: [skill-garden-us-pipeline, mkt-youtube-outline, mkt-hook-kallaway, youtube-garden-us, mkt-youtube-script-audit]
pairs_with: references/remake-playbook-en.md (bằng chứng gốc + R0/R5/R6)
token_note: Đọc §1 (nguyên lý) + §2 (router) + ĐÚNG 1 gói archetype của seed. KHÔNG đọc cả file.
created: 2026-09-09
---

# Remake Archetypes — Bộ định tuyến khuôn cho LANE B

> **Vì sao có file này.** Playbook v1 (`remake-playbook-en.md`) rút từ **một** cụm teardown
> ("Tastes Like Apple and Honey", 9 video) nên mọi luật R2–R4–R7 đều bám **một khuôn duy nhất**:
> *lời hứa cảm giác + cây di sản + danh sách đếm ngược 20 mục*. Hai video lane B thật của kênh
> **đều phải phá luật mới chạy được**:
>
> | Video | Seed thuộc dạng | Chỗ playbook v1 gãy |
> |---|---|---|
> | `remake-001-october-planting` | listicle **khẩn cấp theo mùa** | R2 không có "mảnh sensory" để khoá → tự chế "mảnh khẩn cấp". R3 không đổi cây → đổi **tháng**. |
> | `remake-002-rose-bloom-spoon-trick` | **1 kỹ thuật đơn** (tỷ lệ định lượng) | Phải viết hẳn mục "⚠️ DEVIATION" tắt gần hết cơ chế lane B: bỏ listicle, bỏ 3 vòng lặp số, bỏ spine listicle, bỏ 2 phép đếm Pha D. |
>
> ⇒ Lane B v1 **không phải một lane, nó là một khuôn**. File này tách phần **bất biến** (quy trình)
> khỏi phần **đổi theo dạng seed** (gói archetype), để mọi dạng kịch bản đưa vào đều có đường chạy —
> thay vì override thủ công từng lần.

---

## 0. BA ĐƯỜNG VÀO — seed tới từ đâu

| | Đường vào | R1 đo được? | Xử lý |
|---|---|---|---|
| **A** | Video đang lên trong báo cáo dò trend (`research/trend-us/<YYYYMMDD>/bao-cao-trend.md`, từ 18/11/2026 thay radar R0) | ✅ | Chuẩn — R1 tái thẩm rồi chạy tiếp |
| **B** | User đưa **link video** | ✅ | Chạy R1 tại chỗ (bắt buộc `video_stats granularity:"daily"`) |
| **C** | User **dán mẫu kịch bản / transcript**, không có link, không có số | ❌ | 🔴 **BẮT BUỘC truy ngược nguồn** — xem dưới |

### 🔴 Đường vào C — mẫu kịch bản trần

> **Vì sao không được chạy thẳng.** Remake ăn tiền nhờ **bằng chứng thị trường**, không nhờ cấu trúc.
> Một mẫu kịch bản trần cho bạn **bộ xương**, nhưng ⛔ không mang theo **tài sản đã-trả-tiền** —
> không biết title nào bán được, không biết thumbnail nào giữ chữ, không biết có ai đã clone chưa.
> Chạy lane B trên mẫu không đo được = lặp lại đúng bài học Botanical Vault (1.061 view).

**Quy trình bắt buộc:**

0. **Lưu mẫu user dán** thành `seed-transcript.txt` trong folder video — Pha D so script với nó (`originality_check.py`), kể cả khi hạ xuống lane A.
1. **Phân loại archetype ngay từ mẫu** (§2) — cái này làm được không cần số.
2. **Truy ngược video nguồn** — thử theo thứ tự: user có nhớ link không → `vidiq_youtube_search` bằng
   câu mở đầu/cụm đặc trưng của mẫu → `vidiq_outliers` bằng cụm title đoán được → tìm cụm khuôn tương đương.
3. **Tìm ra video nguồn (hoặc ≥1 video cùng khuôn đang win)** → chạy R1 bình thường → **lane B thật**.
4. **Không tìm ra** → ⛔ không gọi là remake. Hạ xuống **"LANE A — mượn bộ xương"**:
   - Dùng bộ xương + nhịp của gói archetype (đó là thứ duy nhất mẫu cho bạn)
   - ⛔ KHÔNG khoá tài sản nguyên văn từ mẫu — chưa ai chứng minh mảnh đó bán được
   - Title chạy Title Engine đầy đủ như lane A, không kế thừa title của mẫu
   - Folder vẫn là `big-idea-[NNN]-[slug]`, ghi rõ ở `pipeline-state.md`: *"bộ xương mượn từ mẫu, không có bằng chứng thị trường"*
   - `prediction.md` ghi **TEST KHUÔN**

---

## 1. NGUYÊN LÝ BẤT BIẾN — đúng cho MỌI archetype

Ba luật dưới đây là thứ thật sự làm remake ăn tiền. Chúng **không** phụ thuộc dạng seed.

### 1.1 Tài sản đã-trả-tiền (Paid Asset) — bản tổng quát của R2

> Trong mọi title thắng có **đúng một mảnh** mà thị trường đã bỏ tiền chứng minh. Mảnh đó là tài sản
> duy nhất được thừa kế: **khoá cứng nguyên văn** ở title **và** thumbnail. Mọi mảnh còn lại được mutate —
> và **phải** mutate, nếu không thì là re-upload (1.061 view).

Tài sản không phải lúc nào cũng là "mảnh cảm giác":

| Dạng tài sản | Ví dụ | Seed |
|---|---|---|
| Cụm cảm giác | `Tastes Like Apple and Honey` | apple-and-honey |
| Hạn chót | `Plant in September ASAP` · `Before the First Frost` | `dOYKEdmPXWY` |
| Tỷ lệ định lượng | `1 Spoon` → `10x Faster` | `3NuDlyBJk-A` |
| Lệnh cấm | `STOP Boiling & Frying Eggs The OLD WAY` | Opal Rowe (R0-B) |
| Phán quyết xếp hạng | `Worth More Than Gold` | `D0Zywpdrfxs` |

**Cách tìm tài sản bằng 1 câu hỏi:** *xoá mảnh này khỏi thumbnail, video còn lý do tồn tại không?*
Không → đó là tài sản. Bằng chứng: 2/2 bản xoá mảnh tài sản khỏi thumbnail đều chết (7.459 và 1.061 view).

### 1.2 Luật MỘT TRỤC (One-Axis Rule) — bản tổng quát của R3

> Đổi **đúng một trục** để lời hứa giữ nguyên nhưng vật chủ thành **quen thuộc với khán giả Mỹ 60–80**.
> Đổi 0 trục = clone (chết). Đổi ≥2 trục = video mới, **không thừa kế bằng chứng nào** — lúc đó chạy
> LANE A cho trung thực, đừng gọi là remake.

| Trục | Đổi cái gì | Đã dùng ở |
|---|---|---|
| **Vật chủ** | cây exotic → cây bản địa/di sản US | A1 (yacón → skirret) |
| **Thời gian** | tháng/mùa của seed → cửa sổ kế tiếp của ta | A2 (September → October) |
| **Cây nền** | cây trong nhà exotic → cây sân vườn Mỹ | A3 (anthurium → roses) |
| **Bối cảnh** | bếp / sửa nhà / săn bắn → vườn | A6 (port khuôn ngách liền kề) |
| **Quy mô** | 1 cây → cả luống / cả sân | dùng khi 4 trục trên bí |

### 1.3 Nợ giao hàng (Delivery Debt)

> Người xem vào để lấy **một** thứ. Khoảng cách từ giây 0 tới lúc trao thứ đó là **món nợ** — mỗi giây nợ
> phải trả bằng **một cơ chế giữ chân**. Đây là lý do listicle chịu được 20 phút còn single-topic thì không.

| Payoff nằm ở | Nợ | Cơ chế bắt buộc |
|---|---|---|
| Cuối (listicle, #2/N) | rất lớn | 3 vòng lặp số thứ tự + micro-bridge **100% ranh giới** + 3 pattern break |
| Giữa (single-topic reveal) | vừa | **Lời hứa thứ hai** (xem A3) — thứ chỉ trả *sau* khi payoff chính đã trả |
| Đầu (hook trả luôn) | ~0 | ⛔ CẤM ở lane B: hết nợ = hết lý do ở lại. Phải dời payoff hoặc thêm lời hứa thứ hai |

---

## 2. BỘ PHÂN LOẠI — chạy ở R1.5, TRƯỚC GATE 0

Đọc **title + 3 phút đầu transcript** của seed, trả lời 5 câu. Ghi kết quả vào `seed-brief.md §1.5`.

| # | Câu hỏi | Trả lời → Archetype |
|---|---|---|
| Q1 | Payoff của title **về mặt vật lý** là cái gì? | cụm cảm giác → **A1** · hạn chót/thời điểm → **A2** · tỷ lệ + hành động → **A3** · lệnh cấm/lỗi sai → **A4** · xếp hạng/phán quyết danh mục → **A5** · **đúng/sai một niềm tin phổ biến** → **A7** · **triệu chứng + cây đang chết** → **A8** · **một vật dựng được + giá/ràng buộc** → **A9** · **nghịch lý "vì sao"** → **A10** |
| Q2 | Thân bài **có đánh số** không? | Có (≥8 mục) → nhánh listicle (A1/A2/A5) · Không → nhánh single-thread (A3/A4/A7/A8/A9/A10) |
| Q3 | Seed đặt payoff ở **đâu**? | cuối / giữa → giữ nguyên vị trí · **đầu** → bắt buộc cài lời hứa thứ hai (§1.3) |
| Q4 | Tài sản có **hạn sử dụng** không? | Có (mùa/tháng/sự kiện) → **A2**: ngày đăng thành ràng buộc CỨNG · Không → evergreen |
| Q5 | Seed đến từ **ngách khác** (bếp/săn/sửa nhà/làm đẹp)? | Có → **A6** trước, rồi phân loại lại theo Q1 |

**Hai archetype cùng khớp** → chọn cái Q1 mạnh hơn (Q1 thắng Q2). Ghi cái bị loại + lý do.

**Không archetype nào khớp** → ⛔ dừng, không tự chế. Báo user, chọn 1 trong 2:
(a) chạy LANE A cho chủ đề này, hoặc (b) mở gói archetype mới theo điều kiện §5.

---

## 3. GÓI ARCHETYPE

Mỗi gói khai đúng 8 biến. Bước nào không nhắc = **giữ nguyên pipeline chuẩn**.

### A1 — Sensory Heritage Listicle  ✅ *bằng chứng: teardown 9 video — 640K / 509K / 1.56M*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title hứa **vị/cảm giác** về một thứ bị lãng quên |
| 🔒 Tài sản khoá | Cụm cảm giác, **nguyên văn**, title + thumbnail |
| Trục đổi | **Vật chủ** — exotic → cây có trong catalog hạt giống Mỹ (L1) |
| Bộ xương | Đếm ngược 15–18 mục · payoff title ở **#2** · #1 = identity close (cả khu vườn, không phải 1 cây) |
| Nhịp mỗi mục | 5 nhịp: hình ảnh bà → nó cho gì → ai giết nó *(năm + tên + tổ chức)* → giá $ hôm nay → lưu ý an toàn |
| Spine | `templates/retention-spine-listicle.template.md` |
| Tải [1.5] | **3 fact/mục × N mục** (≈45–54) · `sonnet` · chạy **theo lô 5 mục** |
| Pha D thêm | `bridges ≥ items−1` · `years ≥ items×0.8` · `money ≥ items×0.8` |
| R7 thêm | 3 vòng lặp số thứ tự <50s · payoff ở #2 · **mọi** mục có micro-bridge · mỗi thủ phạm có năm + tên + tổ chức |

### A2 — Seasonal Urgency Listicle  ✅ *bằng chứng: A/B tự nhiên n=31 trên Plant Explainer — trong khuôn tháng 7K–191K view, ngoài khuôn 61–971 view*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title = `[N] [việc] in [THÁNG/MÙA]` + từ khẩn cấp (`ASAP` · `Before the First Frost` · `Last Window`) |
| 🔒 Tài sản khoá | **Cụm hạn chót** (tháng + từ khẩn cấp), nguyên văn, title + thumbnail |
| Trục đổi | **Thời gian** — tháng của seed → cửa sổ kế tiếp của ta. ⚠️ Trục DUY NHẤT được đổi; đổi thêm cây/định dạng = mất thừa kế |
| Bộ xương | Đếm ngược 12–18 mục, **nhóm theo "ai làm được"** (vd 7 dễ / 3 vừa / 6 khó) — không nhóm theo loại cây |
| Nhịp mỗi mục | 4 nhịp: việc cụ thể → **cửa sổ đóng khi nào** *(ngày / ngưỡng nhiệt cụ thể)* → hỏng gì nếu trễ → **zone caveat** (USDA zone nào KHÔNG áp dụng) |
| Spine | `retention-spine-listicle.template.md` — đổi cột `N3 ai giết nó` → `cửa sổ đóng khi nào`, `N4 giá $` → `zone caveat` |
| Tải [1.5] | 2 fact/mục (mốc ngày + ngưỡng nhiệt/zone) + 1 lượt tra frost-date theo zone · `sonnet` |
| Pha D thêm | `bridges ≥ items−1` · `zone_mentions ≥ 3` · `date_or_temp ≥ items×0.8` |
| R7 thêm | ⏰ **Ngày đăng là gate cứng** — trễ cửa sổ = huỷ, không đăng bù · mọi mục có mốc thời gian tra được · ≥1 câu "zone nào không làm được" |
| ⚠️ Riêng | Tài sản **mau hỏng**: trễ 1–2 tuần rơi giá trị rất nhanh (`remake-001/pipeline-state.md`). Lên lịch **ngược** từ ngày đăng, không xuôi từ ngày bắt đầu viết |

### A3 — Single-Technique Hack  🟡 *bằng chứng: seed 1.16M view + 2 clone EN yếu (breakout <14); bản của ta `remake-002` đang chạy — CHƯA có số*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title = **1 hành động nhỏ → kết quả lớn định lượng** (`1 Spoon` → `10x Faster`) |
| 🔒 Tài sản khoá | **Cặp tỷ lệ**: liều lượng nhỏ + bội số kết quả. Cả hai nguyên văn, title + thumbnail |
| Trục đổi | **Cây nền** — cây trong nhà exotic → cây sân vườn Mỹ ai cũng có (roses · tomatoes · hydrangea) |
| Bộ xương | Single-topic 8–10′ (giữ `video_length` config, ⛔ KHÔNG kéo dài) · Problem-Fix · payoff ở **beat 4/6** |
| 🔴 Bắt buộc | **LỜI HỨA THỨ HAI** — cài trước giây 55, chỉ trả **sau** payoff chính. Hai dạng: (a) *"có 1 sai lầm vô hiệu hoá cả chiêu này"* · (b) **science correction** — chỗ khoa học KHÔNG ủng hộ bản gốc. (b) là wedge riêng của kênh: seed là AI-slop, ta là science-tested |
| Spine | `templates/retention-spine-single-technique.template.md` |
| Tải [1.5] | 5 câu hỏi chuẩn LANE A + **1 câu bắt buộc**: cơ chế của seed có đứng vững trên cây nền MỚI, trồng ngoài trời không? (nguồn .edu/.gov) · `sonnet` |
| Pha D thêm | `second_promise_planted < 55s` · `second_promise_paid > payoff_position` · giữ nguyên L3/L4/L5/L6 |
| R7 thêm | Tỷ lệ nguyên văn trên thumbnail · **claim-scoping bắt buộc** (CR4): nói rõ chỗ cơ chế KHÔNG hoạt động · ⛔ 0 câu "I tried it" (X5) |
| ⚠️ Riêng | Seed dạng này thường là **AI-slop/pseudo-science**. ⛔ Không bê nguyên claim. [1.5] không tìm được nguồn → giữ tài sản (tỷ lệ) nhưng **đổi cơ chế** sang cái có nguồn, hoặc bỏ seed. Không bịa |

### A4 — Mistake / Prohibition  🟡 *khung suy ra từ CR3 + R0-B (Opal Rowe 151K · Margret Miller 445K) — CHƯA chạy thật ở kênh này*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title = **lệnh cấm hoặc lỗi sai** (`STOP doing X` · `X is killing your Y` · `Never plant Z near W`) |
| 🔒 Tài sản khoá | **Cụm lệnh cấm** + đối tượng bị cấm, nguyên văn |
| Trục đổi | **Vật chủ** hoặc **bối cảnh** — hành động bị cấm giữ nguyên, đổi thứ nó tác động lên |
| Bộ xương | 3 hồi: **cơ chế TRƯỚC danh sách** (CR3) → 5–8 lỗi xếp theo thiệt hại tăng dần → lỗi nặng nhất cuối |
| Nhịp mỗi lỗi | 4 nhịp: dấu hiệu bạn đang mắc → cơ chế vì sao hỏng → thiệt hại $ hoặc thời gian → cách sửa **hôm nay** |
| Spine | `retention-spine-listicle.template.md` — cột `N3` → `cơ chế`, `N5` → `cách sửa` |
| Tải [1.5] | 2 fact/lỗi (1 cơ chế có nguồn extension + 1 con số thiệt hại) · `sonnet` |
| Pha D thêm | `fix_count == mistake_count` — mỗi lỗi phải có cách sửa, cấm chỉ chê không sửa |
| R7 thêm | ⛔ **X3 hard gate**: cấm khung sợ-sức-khoẻ · ⛔ X1: "sai" phải là **cơ chế nông học**, không phải "họ giấu bạn" · mỗi lệnh cấm có nguồn extension/USDA |
| ⚠️ Riêng | Dạng dễ trượt X1/X3 nhất. Nếu tài sản của seed **chính là** thuyết âm mưu hoặc nỗi sợ sức khoẻ → ⛔ BỎ SEED, không có cách cứu (§4) |

### A5 — Category Verdict / Ranking  🟡 *khung suy ra từ `D0Zywpdrfxs` ("Worth More Than Gold", vph 896) — CHƯA chạy thật*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title = **phán quyết giá trị / xếp hạng** (`Worth More Than Gold` · `Best vs Worst` · `What Nurseries Never Sell`) |
| 🔒 Tài sản khoá | **Cụm phán quyết** (chuẩn so sánh), nguyên văn |
| Trục đổi | **Vật chủ** — đổi danh mục được xếp hạng sang danh mục quen của khán giả Mỹ |
| Bộ xương | Đếm ngược 10–15 mục · **tiêu chí xếp hạng nói rõ trước mục đầu tiên** (không xếp hạng mù) · #1 = mục gây tranh cãi nhất |
| Nhịp mỗi mục | 4 nhịp: nó là gì → **con số làm nó xếp hạng đó** → ai KHÔNG nên chọn nó → bắc cầu |
| Tải [1.5] | 2 fact/mục (1 số xếp hạng có nguồn + 1 giá $) · `sonnet` |
| Pha D thêm | `criteria_stated_before_first_item` · `numbers ≥ items` |
| R7 thêm | ⛔ **X2 hard gate**: cấm tuyệt-đối-hoá (`every` · `always` · `the best`) — khoanh vùng "theo tiêu chí X" · mỗi thứ hạng có số chứng minh |

### A6 — Cross-Niche Frame Port  ✅ *bằng chứng: R0-B — 6 video ngoài ngách, breakout 8–3.470*

**Meta-archetype**: seed nằm ở ngách khác (bếp · săn bắn · sửa nhà · làm đẹp · dọn dẹp).

1. Giữ **khung câu** của title, thay danh từ sang vườn — *"Why Grandma Boiled Dish Rags"* → *"Why Grandma Buried Eggshells Under the Tomatoes"*
2. Chạy lại §2 trên **title mới** → rơi vào A1/A2/A4/A5 → dùng gói đó
3. Thủ phạm/cơ chế **phải là sự kiện vườn tra được** — ⛔ không mượn thủ phạm của ngách gốc
4. ⛔ Không port: ngách YMYL sức khoẻ/thuốc/da liễu (X3) · title dán nhãn tuổi người xem (L9)

**Lợi thế:** không phải chen cửa sổ với 5 clone khác. **Rủi ro:** chưa có bằng chứng khuôn đó chạy được
**trong vườn** → luôn coi A6 là test có kiểm soát, ghi log ở retro.

---

### A7 — Myth Verdict / Phán xử niềm tin  🟡 *khung suy ra từ 4 video lane A của kênh (`017-do-eggshells-add-calcium` · `012-avocado-pit-truth` · `018-tomatoes-rot-not-calcium` · `050-sugar-spray-viewer-claim`) — CHƯA chạy ở lane B*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title hỏi hoặc phán xử **một niềm tin ai cũng nghe** (`Do eggshells really add calcium?` · `The truth about avocado pits`) |
| 🔒 Tài sản khoá | **Cụm niềm tin nguyên văn** — đúng câu người ta hay nói. Đó là thứ tạo click, không phải phán quyết |
| Trục đổi | **Vật chủ** — niềm tin về cây X → niềm tin tương đương trên cây quen hơn với khán giả Mỹ |
| Bộ xương | Single-topic 8–10′ · 4 hồi: nêu niềm tin nguyên văn + **vì sao ai cũng tin** (nguồn gốc lịch sử) → bằng chứng → **phán quyết có điều kiện** → làm gì thay |
| 🔴 Bắt buộc | **Verdict sớm + điều kiện muộn.** Trả phán quyết **trước giây 60** (L3 — không bait), rồi giữ chân bằng *"nó đúng trong điều kiện nào"*. ⛔ Cấm phán quyết nhị phân thuần "sai" — trả xong ở phút 1 là nợ = 0, khán giả thoát |
| Tải [1.5] | **≥3 nguồn độc lập** cho phán quyết chính + 1 nguồn cho **nguồn gốc niềm tin**. Bắt buộc **Consensus Synthesis** (2–3 nguồn → 1 nguyên tắc) · `sonnet` |
| Pha D thêm | `verdict_stated < 60s` · `conditions_count ≥ 2` · `independent_sources ≥ 3` |
| R7 thêm | ⛔ **X2**: cấm tuyệt-đối-hoá phán quyết (`never works` · `completely useless`) — luôn khoanh điều kiện *(CR4)* · ⛔ tone không được chê người xem ngu: niềm tin sai là do **lịch sử/quảng cáo**, không do họ · nếu phán quyết là "ĐÚNG" thì title ⛔ không được gợi ý ngược |

### A8 — Rescue / Chẩn đoán  🟡 *khung suy ra từ 4 video lane A (`011-aloe-er-rescue` · `044-save-dying-orchid` · `023-snake-plant-root-rot` · `027-clematis-wilt-misdiagnosis`) — CHƯA chạy ở lane B*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title = **cứu thứ đang chết** (`Save your dying orchid` · `Yellow leaves? Here's what it really means`) |
| 🔒 Tài sản khoá | **Cặp triệu chứng + kết cục** (`yellow leaves` + `dying`) — chữ triệu chứng chính là thứ người ta gõ đi tìm |
| Trục đổi | **Vật chủ** — cây exotic → cây phổ biến trong nhà/vườn Mỹ |
| Bộ xương | Single-topic 8–10′ · **cây quyết định**: 1 triệu chứng → **≥3 nguyên nhân** → mỗi nguyên nhân 1 cách phân biệt + 1 fix |
| 🔴 Bắt buộc | **Chẩn đoán phân biệt** — mỗi nguyên nhân phải có **phép thử 10 giây** để người xem tự xác định mình thuộc nhánh nào. Đây là cơ chế trả nợ: phải xem hết 3 nhánh mới biết nhánh của mình. Cộng **điểm không quay lại** (*"nếu đã X thì không cứu được"*) — vừa là honest note vừa là mở loop |
| Tải [1.5] | 1 nguồn/nguyên nhân + 1 nguồn cho ngưỡng "quá muộn" · `sonnet` |
| Pha D thêm | `causes ≥ 3` · `distinguish_test_count == causes` · `point_of_no_return_stated` |
| R7 thêm | ⛔ **X4**: mọi fix phải **an toàn kể cả khi chẩn đoán sai** (không khuyến nghị việc gây hại nếu nhầm nhánh) · có honest note "trường hợp không cứu được" *(CR5)* · **0 câu** "cây của tôi / tôi đã cứu" *(X5)* |

### A9 — Build / Dự án có giá  🟡 *khung suy ra từ 3 video lane A (`014-no-bend-raised-bed` · `051-budget-bed-under-15` · `026-bottle-drip-tomatoes`) — CHƯA chạy ở lane B*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Title = **dựng một vật**, kèm giá hoặc ràng buộc (`A raised bed for under $15` · `No-bend bed`) |
| 🔒 Tài sản khoá | **Cặp vật + con số** (giá trần / thời gian / ràng buộc thể chất) |
| Trục đổi | **Quy mô** (1 luống → cả sân) hoặc **vật chủ** (đổi vật liệu) |
| Bộ xương | Single-topic 8–10′ · bảng vật tư **trước**, các bước **sau** (5–8 bước) · payoff = vật hoàn thành ở beat cuối |
| 🔴 Bắt buộc | Nợ giao hàng lớn (payoff ở cuối) → trả bằng **tổng chi phí cộng dồn** hiện ít nhất 3 lần trong bài (`$4 so far…`) + **1 bước "sai là hỏng cả"** gieo từ đầu, trả ở gần cuối |
| Tải [1.5] | Giá thật **hiện tại** từng vật tư *(kèm nơi bán + ngày đo)* + 1 nguồn an toàn/kết cấu · `sonnet` |
| Pha D thêm | `running_total_shown ≥ 3` · `steps 5–8` · `failure_step_present` · `prices_have_date` |
| R7 thêm | ⛔ **X2**: giá phải gắn ngày đo, cấm hứa giá cố định · an toàn dụng cụ là 1 nhịp rõ *(CR5)* · lợi ích ergonomic **được nói trong nội dung**, ⛔ KHÔNG lên title/thumbnail *(L9, L8)* |

### A10 — Mechanism Explainer / Nghịch lý  🟡 *khung suy ra từ 3 video lane A (`aloe-30-years-biology` · `029-nitrogen-trap-clematis` · `001-feed-soil-not-grass`) — CHƯA chạy ở lane B*

| Biến | Giá trị |
|---|---|
| Nhận dạng | Payoff = **hiểu vì sao**, đóng gói bằng **nghịch lý** (`Feed the soil, not the plant` · `The more you feed it, the less it blooms`) |
| 🔒 Tài sản khoá | **Cụm nghịch lý** — vế mâu thuẫn chính là thứ bán click, không phải cơ chế |
| Trục đổi | **Vật chủ** — cùng nghịch lý, đổi sang cây khán giả Mỹ đang trồng |
| Bộ xương | Single-topic 8–10′ · **chuỗi 3–4 tiết lộ tăng dần**, mỗi tiết lộ mở một nghịch lý nhỏ mới · nguyên lý gọn đặt ở beat cuối + **2 việc làm được hôm nay** |
| 🔴 Bắt buộc | **Mỗi tiết lộ phải đổi một hành động.** Hiểu mà không đổi việc gì = bài giảng → AVD chết. Đây là gói dễ trượt nhất về retention, không phải về compliance |
| Tải [1.5] | **Consensus Synthesis bắt buộc**: mỗi nguyên lý ≥2 nguồn độc lập → 1 phát biểu · `sonnet` |
| Pha D thêm | `reveals ≥ 3` · `actionable_per_reveal == reveals` · `principle_stated_before_last_60s` |
| R7 thêm | ⛔ **X4**: cấm đơn giản hoá cơ chế còn tranh cãi tới mức thành lời khuyên sai · mỗi nguyên lý ≥2 nguồn · kết bằng **2 việc làm được**, không phải recap |

---

## 4. ⛔ SEED PHẢI BỎ — không archetype nào cứu được

Kiểm ngay ở R1, trước khi tốn công R2/R3:

| Dấu hiệu | Vì sao bỏ |
|---|---|
| Tài sản **chính là** thuyết âm mưu (`they're hiding this` · `banned` · `government doesn't want`) | X1 — bỏ tài sản thì hết thừa kế, giữ tài sản thì mất kiếm tiền |
| Tài sản là **nỗi sợ sức khoẻ** / thuốc / bệnh | X3 + YMYL |
| Tài sản là **persona tự trồng/tự test** (`I tested this for 30 days`) | X5 + Narrator Integrity — kênh không có narrator tự trồng |
| Title chứa **tuổi người xem** (`Over 60` · `for Seniors`) | L9 — kể cả khi seed thắng nhờ nó |
| Cơ chế **nguy hiểm** nếu người 60–80 làm theo | X4 |
| Không đổi được **trục nào** mà lời hứa vẫn sống | Không đổi trục = re-upload = 1.061 view |

---

## 5. Mở gói archetype MỚI — điều kiện

Chỉ mở khi có **≥2 video độc lập** (khác kênh) cùng khuôn, mỗi video `view/sub ≥ 5×`. Gói mới phải khai đủ
8 biến như §3 + nhãn xuất xứ (✅ có bằng chứng · 🟡 suy ra · 🔴 giả thuyết). Gói 🟡/🔴 **bắt buộc** ghi
vào `prediction.md` là "test khuôn", và retro phải trả lời: *khuôn này có mang lời hứa qua được không?*

---

## 6. Bảng tra nhanh — dán vào `seed-brief.md §1.5`

| | A1 Sensory | A2 Seasonal | A3 Technique | A4 Mistake | A5 Verdict |
|---|---|---|---|---|---|
| Tài sản khoá | cụm cảm giác | cụm hạn chót | cặp tỷ lệ | cụm lệnh cấm | cụm phán quyết |
| Trục đổi | vật chủ | thời gian | cây nền | vật chủ / bối cảnh | vật chủ |
| Định dạng | listicle 15–18 | listicle 12–18 | single 8–10′ | 3 hồi + 5–8 lỗi | listicle 10–15 |
| Payoff | #2 | rải theo cửa sổ | beat 4/6 | lỗi nặng nhất cuối | #1 |
| Cơ chế trả nợ | 3 loop số + bridge 100% | bridge + đếm ngược ngày | **lời hứa thứ hai** | cơ chế trước list | tiêu chí trước list |
| Rủi ro chính | L7 (dài) | trễ cửa sổ | X2 / pseudo-science | X1 / X3 | X2 |
| Bằng chứng | ✅ | ✅ | 🟡 | 🟡 | 🟡 |

| | A7 Myth Verdict | A8 Rescue | A9 Build | A10 Mechanism |
|---|---|---|---|---|
| Tài sản khoá | cụm niềm tin | cặp triệu chứng + kết cục | cặp vật + con số | cụm nghịch lý |
| Trục đổi | vật chủ | vật chủ | quy mô / vật liệu | vật chủ |
| Định dạng | single 8–10′, 4 hồi | single 8–10′, cây quyết định | single 8–10′, 5–8 bước | single 8–10′, 3–4 tiết lộ |
| Payoff | **verdict trước giây 60** | chẩn đoán đúng *(không phải fix)* | vật hoàn thành, beat cuối | nguyên lý, beat cuối |
| Cơ chế trả nợ | **điều kiện muộn** | **phép thử phân biệt ×3** + điểm không quay lại | **tổng chi phí cộng dồn** + bước hỏng-cả | **mỗi tiết lộ đổi 1 hành động** |
| Rủi ro chính | X2 / tone chê người xem | X4 (fix sai nhánh) | X2 (giá) / L9 | AVD — thành bài giảng |
| Bằng chứng | 🟡 | 🟡 | 🟡 | 🟡 |

> ⚠️ **7 gói mang nhãn 🟡** (A3 · A4 · A5 · A7 · A8 · A9 · A10) là khung suy ra, chưa có số thật ở lane B.
> Mỗi lần chạy gói 🟡: `prediction.md` ghi **TEST KHUÔN** + retro phải trả lời *"khuôn này có mang lời hứa qua được không?"*.
> Gói nào chạy đủ **2 video** mà `views_5d` vượt `median_5d_views` → nâng lên ✅ và ghi số vào đây.
