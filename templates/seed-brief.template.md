---
file: seed-brief.md
role: Chốt 1 seed → input cho [1] mkt-youtube-outline. Thay "Big Idea #N từ Notion" ở lane REMAKE.
lane: REMAKE
version: v2.1 (2026-10-23) — thêm §2B mổ xẻ seed + lưu seed-transcript cho originality_check --against. v2 (2026-09-09) archetype-aware.
source: references/remake-playbook-en.md §R1–R2–R3 + references/remake-archetypes-en.md §1–§3
gate: 🔴 GATE 0 — user duyệt ARCHETYPE + vật chủ + title trước khi vào outline
---

# Seed Brief — remake-[NNN]-[slug]

**Seed:** `videoId` · URL · kênh · ngày đăng
**Đường vào:** ☐ **A** radar tuần (`research/seed-radar-YYYY-Www.md`) · ☐ **B** user đưa link video · ☐ **C** user dán mẫu kịch bản *(bắt buộc truy ngược nguồn — xem dưới)* · ☐ R0-B port khuôn ngách khác

### Nếu ĐƯỜNG VÀO C — truy ngược nguồn *(bắt buộc trước GATE 0)*

| | |
|---|---|
| Đã thử tìm bằng | ☐ hỏi user ☐ `vidiq_youtube_search` câu mở đầu ☐ `vidiq_outliers` cụm title ☐ tìm video cùng khuôn đang win |
| Kết quả | ☐ **tìm ra** → chạy R1 bên dưới như bình thường · ☐ **không tìm ra** → ⛔ hạ xuống **LANE A — mượn bộ xương** |
| Nếu hạ lane A | folder `big-idea-[NNN]-[slug]` · ⛔ không khoá tài sản từ mẫu · title chạy Title Engine đầy đủ · `prediction.md` ghi **TEST KHUÔN** |

---

## 1. Tái thẩm seed (R1) — đo lại tại thời điểm bắt đầu video

> ⛔ **KHÔNG** dùng `vph` từ `vidiq_outliers` / `vidiq_similar_videos` để chấm đậu — đã đo sai **100 lần**
> (`vrvLNbIL7tk`: báo 409,97 · thật 4,09). **BẮT BUỘC** chạy `vidiq_video_stats granularity:"daily"` rồi tự tính.

| Chỉ số | Cách lấy | Hôm nay | Ngưỡng | Đạt? |
|---|---|---|---|---|
| `monthly_growth_pct` = view tăng 30 ngày / tổng view | từ daily stats | | **≥ 5%** ✅ · 1–5% ⏳ · <1% ❌ | |
| `view / sub` | | | ≥ 5× | |
| `breakoutScore` | | | ≥ 15 | |
| Sub kênh gốc | | | < 50K | |
| Tuổi seed | | | 60–150 ngày | |
| Số clone đã đăng | `similar_videos` 14 ngày | | ≤ 2 | |
| Đường cong | daily stats | ☐ NỞ ☐ vừa qua đỉnh ☐ CHÁY NHANH ☐ CHẾT | NỞ / vừa qua đỉnh | |

**Verdict R1:** ☐ PASS · ☐ FAIL → chuyển seed khác · ☐ **OVERRIDE** (điền khối dưới)

### 🟡 Khối OVERRIDE — chỉ điền khi user cố tình chạy seed trượt ngưỡng

| | |
|---|---|
| Tiêu chí trượt | *(vd: tuổi 16 ngày < 60 · kênh gốc 103K > 50K)* |
| Lý do đánh đổi | |
| Rủi ro chấp nhận | |
| **Câu hỏi cho retro** | *(bắt buộc — retro phải trả lời câu này và ghi vào `lessons-learned.md`)* |
| User duyệt | ngày … |

---

## 1.5. 🔴 PHÂN LOẠI ARCHETYPE — chạy TRƯỚC GATE 0

> Bộ phân loại đầy đủ: `references/remake-archetypes-en.md` §2. Sai bước này thì mọi bước sau sai theo.

| # | Câu hỏi | Trả lời |
|---|---|---|
| Q1 | Payoff của title **về mặt vật lý** là gì? | ☐ cụm cảm giác **A1** ☐ hạn chót **A2** ☐ tỷ lệ+hành động **A3** ☐ lệnh cấm **A4** ☐ phán quyết danh mục **A5** ☐ đúng/sai một niềm tin **A7** ☐ triệu chứng + cây đang chết **A8** ☐ vật dựng được + giá/ràng buộc **A9** ☐ nghịch lý "vì sao" **A10** |
| Q2 | Thân bài có đánh số (≥8 mục)? | ☐ Có → listicle (A1/A2/A5) ☐ Không → single-thread (A3/A4/A7/A8/A9/A10) |
| Q3 | Seed đặt payoff ở đâu? | ☐ cuối ☐ giữa ☐ **đầu** → bắt buộc lời hứa thứ hai |
| Q4 | Tài sản có hạn sử dụng? | ☐ Có → **ngày đăng là gate cứng** ☐ Không |
| Q5 | Seed từ ngách khác? | ☐ Có → **A6** rồi phân loại lại ☐ Không |

**ARCHETYPE ĐÃ CHỐT:** `A_` — …
**Archetype bị loại + lý do:** …
**Bằng chứng của gói này:** ☐ ✅ có số thật ☐ 🟡 suy ra → **ghi vào `prediction.md` là TEST KHUÔN**

### ⛔ Kiểm SEED PHẢI BỎ (§4) — trượt 1 dòng = dừng, không viết

☐ tài sản là thuyết âm mưu (X1) · ☐ nỗi sợ sức khoẻ/YMYL (X3) · ☐ persona tự-test (X5)
☐ title có tuổi người xem (L9) · ☐ cơ chế nguy hiểm cho người 60–80 (X4) · ☐ không đổi được trục nào

---

## 2. Tài sản đã-trả-tiền (R2 — bản tổng quát)

> Xoá mảnh này khỏi thumbnail thì video còn lý do tồn tại không? Không → đó là tài sản.

| Mảnh | Trong seed gốc | Trong bản của ta |
|---|---|---|
| 🔒 **Tài sản** *(dạng: … theo archetype)* | | **PHẢI TRÙNG TỪNG CHỮ** |
| Mảnh mutate #1 | | |
| Mảnh mutate #2 | | |

⛔ **Hard fail:** tài sản bị đổi chữ ở title HOẶC thumbnail → dừng, viết lại.
*Bằng chứng: 2/2 bản xoá tài sản khỏi thumbnail đều chết (7.459 và 1.061 view).*
⛔ **Hard fail ngược:** **0 mảnh** được mutate → đó là re-upload (1.061 view).

---

## 2B. 🔬 MỔ XẺ SEED (R2 — bảng chuẩn, thêm 2026-10-23)

> Mổ để lấy **cơ chế**, không lấy **câu chữ**. Mọi ô ghi bằng **tóm ý của mình** — chép câu seed vào đây
> thì sớm muộn nó trôi vào script. Pha D lane B chạy `originality_check.py` so thẳng với transcript seed.

**Transcript seed:** lưu nguyên văn kèm mốc giây vào `seed-transcript.txt` (hoặc `.srt`) **cùng folder** —
lấy bằng `vidiq_video_transcript` hoặc skill `youtube-transcript` (có timestamp). Đường vào C → lưu mẫu user dán.
Độ dài seed: …′ · … từ · payoff chính ở mốc …

### A. Điểm giữ chân theo mốc giây

| Mốc | Thiết bị *(open loop · vòng lặp số thứ tự · bằng chứng sớm · pattern break · re-hook · scene · lời hứa thứ hai)* | Tóm ý (không chép câu) | Đụng vùng chết KÊNH MÌNH? *(20–34s · 40–55s · 4–6′ · không)* | Ta dùng? |
|---|---|---|---|---|
| 0:00 | | | | ☐ mượn cơ chế ☐ bỏ — lý do |
| | | | | |

**Seed thủng ở đâu** *(mốc seed không có thiết bị nào mà kênh mình lại hay rơi ở đó)*: … → spine [2.5] phải vá chỗ này.

### B. Chuyển đoạn

| Từ → sang | Kiểu *(vấn đề mới · câu hỏi · số thứ tự trơ · tóm tắt)* | Có giữ được không? | Bản của ta *(micro-bridge: đóng 1 vế + mở vấn đề mới)* |
|---|---|---|---|
| | | | |

### C. Nỗi đau tâm lý

| Nỗi đau | Seed chạm ở mốc | Có trong comment/customer profile kênh mình? | Hợp người 60–80? |
|---|---|---|---|
| | | ☐ có ☐ không | ☐ ☐ |

### D. 📒 Sổ claim của seed → bàn giao [1.5]

| Mã | Claim (tóm) | Mốc | Nhãn | Xử lý |
|---|---|---|---|---|
| S1 | | | ☐ có nguồn ☐ chưa nguồn ☐ giả khoa học ☐ persona bịa *(I tested · bà tôi · hàng xóm)* ☐ nguy hiểm cho 60–80 | ☐ giữ — [1.5] phải tìm nguồn ☐ đổi thành **science correction** ☐ bỏ |

- Mọi claim **giữ** → thành câu hỏi bắt buộc ở §6. Không tìm được nguồn → `[NEED DATA]`, không dùng.
- Claim **giả khoa học** mạnh nhất → ứng viên **lời hứa thứ hai** / góc **Myth vs Science** / **Editorial Signature**.
- Claim **persona bịa** → ⛔ không chuyển sang script dưới bất kỳ dạng nào (L11 · X5).

---

## 3. Đổi MỘT trục (R3 — One-Axis Rule)

**Trục đã đổi:** ☐ vật chủ ☐ thời gian ☐ cây nền ☐ bối cảnh ☐ quy mô — **chỉ được chọn 1**

| | Bên **seed** | Bên **ta** |
|---|---|---|
| Giá trị trên trục đã đổi | | |
| Người Mỹ 60–80 có ký ức để móc vào? | | ☐ Có ☐ Không → **phải gắn vào thứ quen (L1)**: … |
| Đơn vị đo trong script | | **pound / feet / inch / gallon** |

**Các trục KHÔNG đổi (xác nhận giữ nguyên):** …
*(Đổi ≥2 trục = mất thừa kế bằng chứng → chạy LANE A cho trung thực.)*

---

## 4. Ba title candidate → 🔴 GATE 0

| | Title | Tài sản nguyên văn? | Tuổi NGUỒN, không phải tuổi NGƯỜI XEM? | vidiq_score_title |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| C | | | | |

⛔ **L9/L9b:** cấm `Senior` · `Over 60` · `Over 65` · `for Elderly` · `No Bending` · `No Back Pain` ở title và chữ thumbnail.
✅ Dùng tuổi của NGUỒN: `Grandma's…` · `Our Grandparents…` · `Old Gardeners…` · `Before bagged soil existed…`

**Title đã chọn:** … *(ghi ngày + người duyệt)*
**Á quân cho swap giờ 48 nếu CTR <4%:** …
**Ghi chú thumbnail:** FACELESS *(luật kênh 14/14)* · ⛔ cấm tái sử dụng ảnh của seed · chữ 2 tầng: **vàng = tài sản**, trắng = mảnh mutate

---

## 5. Định dạng theo gói archetype (R4)

> Chép từ `remake-archetypes-en.md §3` gói `A_`. ⛔ Không tự chế định dạng ngoài gói —
> nếu gói không vừa, mở gói mới theo §5 của file đó, đừng viết "DEVIATION" một lần rồi quên.

| | Gói quy định | Video này |
|---|---|---|
| Bộ xương | | |
| Số mục / số beat | | |
| Vị trí payoff | | |
| Độ dài mục tiêu | | *(⚠️ vượt `video_length` = va L7 — ghi lý do dưới)* |
| Spine template | | |
| Cơ chế trả nợ *(§1.3)* | | |
| Lý do vượt L7 *(nếu có)* | | |

**Hệ quả cho các bước sau** *(điền để bước [2]/[2.5]/[3] không phải đoán)*:
- [2] hook: …
- [2.5] spine: …
- [3] Pha D: … *(phép đếm riêng của gói)*
- [6] retro: chấm bằng `views_5d` vs `median_5d_views` (285) + tổng giờ xem · ⛔ KHÔNG chấm bằng AVD

---

## 6. Bàn giao sang [1.5] deep-research

| | |
|---|---|
| Tải trọng theo gói | *(vd A1: 3 fact × N mục · A3: 5 câu chuẩn + 1 câu cơ chế trên cây nền mới)* |
| **Tổng fact cần nguồn** | |
| Model | `sonnet` *(lane B không dùng haiku ở bước này)* |
| Cách chạy | *(A1/A2/A5: `garden-deep-researcher` theo lô 5 mục · A3/A4/A9: 1 lượt · A7/A10: 1 lượt + **Consensus Synthesis** ≥2–3 nguồn/nguyên lý · A8: 1 lượt/nguyên nhân)* |
| Câu hỏi bắt buộc của gói | |
| **Claim seed phải kiểm** *(từ §2B-D)* | S… · S… — mỗi claim "giữ" có nguồn .edu/.gov hoặc bị loại; claim "science correction" cần nguồn phản chứng |

⛔ Fact không tra được nguồn → `[NEED DATA: ...]`. **Không bịa năm, không bịa tổ chức, không bịa giá.**
