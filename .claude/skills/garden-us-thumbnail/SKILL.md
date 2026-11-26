---
name: garden-us-thumbnail
description: "Tạo thumbnail YouTube cho kênh Garden US (English) theo CÔNG THỨC WIN đúc kết từ thumbnail thật của kênh (references/thumbnail-stats-garden-us-60k.md) + Luật L29 (26/11/2026): FACELESS object-driven, tách ẢNH NỀN SẠCH KHÔNG CHỮ (clean plate, chừa sẵn negative space) + SPEC GHÉP CHỮ TAY/PILLOW 2 tầng ALL CAPS (hook VÀNG + phụ TRẮNG, viền đen dày) & badge ❌/✅ sắc nét cho cả Smart TV và mobile, layout Before→After / number-badge / triptych, Complementarity 1+1=3 (bổ trợ title). Bước cuối sinh thumbnail-prompts.md với 2 MASTER PROMPT A/B (clean plate) + spec text overlay, render nền sạch + ghép chữ Pillow/Canva tùy chọn. KHÔNG conspiracy/overclaim/human-fear/chữ AI méo. CHỈ workspace Garden US, KHÔNG dùng kênh JP. USE WHEN user nói 'tạo thumbnail', 'làm thumb', 'thumbnail cho video', 'tạo ảnh thumbnail', 'thumb cho script', 'cover video', sau khi script.md/outline.md đã xong, hoặc tại bước thumbnail trong pipeline Garden US."
---

# Garden US — Thumbnail Generator (Clean Plate + Manual/Pillow Overlay · Smart TV & Mobile)

> ⚠️ **SKILL RIÊNG CHO KÊNH GARDEN US (cập nhật 26/11/2026 — L29).** Project-scoped trong `.claude/skills/` của workspace US → chỉ load khi mở kênh US. Công thức = **Ảnh nền sạch KHÔNG chữ (clean plate)** + **ghép chữ 2 tầng ALL CAPS sắc nét bằng Canva/Photoshop hoặc Pillow (`tools/garden_thumb_real.py`)** (hook VÀNG + phụ TRẮNG, viền đen dày). Khi config có `thumbnail_skill` trỏ về đây, `mkt-youtube-outline` Bước 5 sẽ NHƯỜNG cho skill này.

Mục tiêu: biến text thumbnail của outline thành **2 master prompt A/B nền sạch không chữ + spec overlay chữ/badge chuẩn** theo **công thức WIN của kênh** (FACELESS · text 2 tầng hook VÀNG + phụ TRẮNG · layout Before→After/number-badge/triptych · markup đỏ) — bổ trợ title (1+1=3), số trên thumb = số trong script, đọc nét căng ở cả **Smart TV (2–3m)** lẫn **mobile (200px)**. Bước cuối luôn xuất `thumbnail-prompts.md`; render ảnh nền + ghép chữ Pillow tùy chọn.
> 📊 **Công thức từ data, không hardcode:** chi tiết WIN pattern ở `references/thumbnail-stats-[slug].md` (đọc ở BƯỚC ĐẦU mục 4). Skill body chỉ mirror; data file là nguồn override.

---

## BƯỚC ĐẦU — ĐỌC CONFIG + INPUT

1. Đọc `channel.config.json` ở gốc workspace → `WORKSPACE_PATH`, `BRAND_VOICE_FILE`, `SCRIPT_LANGUAGE` (phải là English). (Fallback: `## Channel Config` trong CLAUDE.md.)
2. Xác định folder video: `[WORKSPACE_PATH]\scripts\big-idea-[NNN]-[slug]\` (hoặc `outline-[slug]\`).
3. Đọc `script.md` (hoặc `outline.md`) → extract:
   - **Title đã chọn** + **lever Value Equation title đã kéo** (block `## Titles` của outline ghi "Lever: ...").
   - **Text thumbnail + pattern** nếu outline đã gợi ý (block `## Thumbnail`).
   - **SỐ then chốt CÓ THẬT** trong script ($1,000 / 12 plants / 20 years / 3x …) — ⚠️ chỉ số XUẤT HIỆN trong script, KHÔNG bịa.
   - **Payoff/pain chính** (save money / never replant / stop killing plants …).
   - **Chủ thể** gợi ý (cây cụ thể / khuôn mặt senior biểu cảm / dụng cụ).
4. **(ƯU TIÊN) Đọc `[WORKSPACE_PATH]\references\thumbnail-stats-[YOUTUBE_CHANNEL_SLUG].md`** — chỉ block `## ⚡ AUDIT TL;DR`. Đây là **công thức thumbnail đúc kết từ thumbnail THẬT của kênh** (visual teardown).
   - **Nếu file tồn tại → nó GHI ĐÈ phần hardcode bên dưới** (Section C/D/E + quy tắc "≤3 từ"/"chữ trắng"/"6 pattern"). Lấy `FACELESS`, `TEXT_TIERS`, `COLOR_SYSTEM`, `MARKUP`, `TOP_LAYOUTS` từ file làm chuẩn. Skill body chỉ là fallback khi chưa có data.
   - **Nếu không có** → dùng pattern hardcode Section C/D/E (generic).
5. (tùy) Đọc `references/channel-stats-[slug].md` → bối cảnh title pattern (nếu cần).

Thiếu script → hỏi user dán title + số then chốt, KHÔNG tự bịa.

> ⚙️ **Nguyên tắc tách bạch:** skill = phương pháp chung; **dữ liệu riêng kênh nằm ở `thumbnail-stats`** (giống outline đọc channel-stats). Cập nhật công thức = sửa file data, KHÔNG sửa skill. Re-teardown bằng vidIQ mỗi quý hoặc khi thumbnail style kênh đổi.

---

## CÔNG THỨC (BẮT BUỘC bám đúng)

### A. Complementarity 1 + 1 = 3
Title lo SEO + lời hứa đầy đủ. **Thumbnail lo cảm xúc + curiosity — nói thứ title CHƯA nói.** Không nén lại title.
- ❌ Title "Plant These 12 Perennials Once, Harvest for 20 Years" → Thumb `PLANT ONCE = 20 YEARS` (lặp).
- ✅ → Thumb `$0 EVERY SPRING` hoặc `NEVER REPLANT` (góc tiền/đỡ-công title chưa nhấn).

### B. Lever-Complementarity (nối Value Equation)
Thumbnail kéo **lever Value Equation KHÁC** với title:
- Title kéo *Kết quả↑ + Thời gian↓* → thumb kéo *Công sức↓* (`NEVER REPLANT`) hoặc *tiền* (`$0 EVERY SPRING`).
- Title kéo *Chắc-thắng↑ (tránh lỗi)* → thumb kéo *Kết quả↑* (`100 LBS`).
→ Đọc lever title từ script/outline; chọn lever còn trống.

### C. Quy tắc text — CÔNG THỨC WIN của kênh (đúc kết từ thumbnail-stats)
> Đây là pattern THẮNG thật của kênh (14 thumbnail top teardown). `thumbnail-stats` override nếu có; nếu không, đây là mặc định.
1. **2 tầng chữ, ALL CAPS, ~4–6 từ tổng** (KHÔNG còn ép ≤3 từ — top video kênh dùng 2 dòng). Font đậm + **viền đen dày + đổ bóng**.
2. **MÀU = chữ ký CTR của kênh:** dòng **hook/số/$ = VÀNG**; dòng **phụ/giải thích = TRẮNG**. (Vd `STOP!`(vàng) + `$500 IN YOUR YARD`(trắng); `NO SOIL`(vàng) + `NEEDED!`(trắng).) Pure-white toàn bộ chỉ dùng khi user yêu cầu / để A/B test màu.
3. 🔴 **Toàn thumbnail BẮT BUỘC có ĐỦ HAI: một SỐ (hoặc `$`) VÀ một TRIỆU CHỨNG người xem tự nhận ra.**
   Là gate, không phải "nên". Tránh "How/Why/The/A/An" mở đầu.
   **Phân vai chuẩn (theo mẫu CTR cao nhất `TURNING MUSHY? 5 FIXES INSIDE` = 2.7%):**
   dòng **VÀNG = TRIỆU CHỨNG** (câu hỏi ngắn người xem soi vào cây nhà mình thấy ngay) ·
   dòng **TRẮNG = SỐ + payoff**. ⚠️ Số KHÔNG bắt buộc nằm ở dòng vàng — mẫu thắng đặt số ở dòng trắng.
   Phản ví dụ: câu hỏi trống `CAN THIS COME BACK?` (1.5%) · 2 từ mơ hồ `SWEETER COLD` (1.7%) ·
   có số nhưng thiếu triệu chứng `7 PROVEN TO SURVIVE EXTREME DROUGHT` (1.9%).
   ⛔ **CẤM** thumbnail chỉ có câu hỏi/khẩu hiệu không số VÀ không lời hứa cụ thể.
   *(Bằng chứng: CTR đo từng video n=6, 2026-08-15 — xem §CTR ĐO THẬT trong `thumbnail-stats-[slug].md`,
   đọc kèm 3 confound ở đó trước khi coi là luật tuyệt đối.)*
4. Emoji/symbol tiết chế: ❌ đỏ (sai) · ✅ xanh (đúng) → tạo tương phản.

### D. Layout WIN của kênh (đúc kết từ thumbnail-stats — xếp theo sức mạnh)
> Chọn layout theo Format. Layout #1 gắn với video AVD CAO NHẤT kênh (33%).

| Layout WIN | Khi dùng | Cách dựng | Markup |
|---|---|---|---|
| **① Before→After ❌/✅** ⭐ | Myth-bust / Problem-Fix (MẶC ĐỊNH) | Trái = cách SAI (object hỏng + ❌ đỏ) · Phải = cách ĐÚNG (fix + ✅ xanh) | khoanh đỏ nét đứt điểm hỏng + ❌/✅ |
| **② Single hero + text** | Reveal đơn | 1 chủ thể lệch 1 bên, chữ vào negative space | mũi tên cong vàng/cyan trỏ chủ thể |
| **③ Leading-number badge** | Listicle | Hero + **số trong vòng tròn VÀNG** góc trên-trái | badge tròn |
| **④ Triptych 3 panel** | Multi-item / so sánh sản phẩm | 3 cảnh: nguyên nhân / sản phẩm / kết quả | đường chia + ❌/✅ nếu hợp |

> 6 pattern text cũ (Callout/Number/Reveal/Single-word/Question) vẫn dùng được làm CHỮ, nhưng **bọc trong 4 layout WIN trên** + màu vàng/trắng Section C.

### E. Nền ảnh (photoreal, CTR-grade) — 🚫 FACELESS, KHÔNG mặt người
- Ảnh thật vườn/sân US, **tương phản & bão hòa CAO**.
- Subject rõ = **vật thể/cây/củ/dụng cụ** liên quan (hero object), **KHÔNG người, KHÔNG mặt làm chủ thể**. Kênh faceless → thumb cũng faceless.
- **Bàn tay làm PROP được phép và là chữ ký kênh** (data 07/04: 6/14 top thumb + champion AVD 49% đều có tay cầm/thao tác) — tay chỉ hỗ trợ hành động, KHÔNG là chủ thể. Trong prompt: `a single hand holding/reaching as prop is OK; no face, no full person`.
- **🚫 KHÔNG dùng động vật đe dọa (rắn/chuột…) làm hero** — "Snakes" AVD 14.3% (tệ nhất kênh): fear-imagery hút sai khán giả.
- **Markup chuẩn kênh (BẮT BUỘC cân nhắc, không phải tùy chọn):** **khoanh đỏ NÉT ĐỨT** lên điểm then chốt · **mũi tên cong** vàng/cam/cyan trỏ chủ thể · **❌ đỏ / ✅ xanh** cho before→after.
- Chữ (vàng+trắng) đặt vào negative space (trái/dưới); KHÔNG đè chủ thể chính.

---

## 🎯 GURU LAYER — 5 HARD-GATE tâm lý (chạy SAU khi có concept, TRƯỚC khi xuất prompt)

> Phần A–E lo "đúng chữ ký kênh". Phần này lo "THẮNG trong feed" — tầng tâm lý các guru (MrBeast / Paddy Galloway / Thomas Frank) ám ảnh mà công thức cơ học bỏ sót. **MỖI biến thể A & B phải PASS cả 5.** FAIL bất kỳ → sửa concept, KHÔNG xuất prompt. Ghi kết quả 5 gate vào bảng biến thể (cột "GURU 5G: ✅/❌ + lý do").

**G1 — SQUINT TEST (mobile 200px + Smart TV phòng khách 2–3m + mắt kém 60–80t)** 🔴 gate CTR số 1 của kênh này
Hình dung thumbnail ở cả 2 đầu cực: thu nhỏ còn ~200px trong feed mobile VÀ xem từ ghế sofa cách Smart TV 2–3m. Trong 0.5 giây phải: (a) đọc được dòng chữ VÀNG sắc nét không dính nét/không méo AI, (b) nhận ra chủ thể chính. Nếu phải nheo mắt → FAIL. Hệ quả cứng: **dòng hook vàng ≤3 từ/dòng**, ghép chữ vector/Pillow font đậm + viền đen dày (L29), chủ thể chính chiếm **≥40% khung**, và chi tiết nhỏ (nhãn bao phân, 1 mắt lá, chữ phụ) KHÔNG được là thứ *bắt buộc phải thấy* mới hiểu thumb.

**G2 — ONE FOCAL POINT (1 điểm đọc trước)**
Mắt phải biết nhìn ĐÂU đầu tiên trong 0.3 giây. Before→After **KHÔNG chia 50/50** (2 tiêu điểm = rối ở size nhỏ) → cho **1 bên thống trị ~60/40**, thường bên payoff/after to & rực hơn. Single-hero: chủ thể lệch 1 bên, TO, nét căng; phần còn lại blur nhường chỗ. Nhiều thứ "cùng quan trọng" = không thứ nào nổi.

**G3 — CURIOSITY GAP (gieo câu hỏi, GIẤU đáp án)**
Viết 1 câu: *"Thumb này khiến người xem TỰ HỎI: ___?"*. Nếu thumbnail tự trả lời luôn câu đó → hết tò mò → FAIL. Đáp án nằm TRONG video, không trên thumb. **Test ghép Title×Thumb:** đọc title + nhìn thumb cùng lúc phải ra 1 câu chuyện HOÀN CHỈNH mạnh hơn từng cái riêng (complementarity đúng); nếu 2 cái rời rạc, không liên quan → complementarity quá đà → kéo lại.

**G4 — EMOTIONAL PROXY (faceless → vật thể GÁNH cảm xúc)**
Không có mặt người tải cảm xúc → chọn **1 cảm xúc đích DUY NHẤT** (sốc / tò mò / khao khát / sợ-mất / thoả mãn) + **1 vật thể tải cảm xúc đó qua TRẠNG THÁI của nó**: cây héo rũ tuyệt vọng vs bung hoa mãn nguyện · đất nứt nẻ vs đất mỡ màng · rễ trắng bật khỏi hũ. Trạng thái vật thể = "biểu cảm khuôn mặt" của thumb faceless. Ghi cảm xúc đích vào bảng biến thể.

**G5 — PATTERN-INTERRUPT (chống chìm trong biển xanh lá)**
Feed làm vườn toàn xanh lá → thumb xanh lá = tàng hình. Ép **≥1 yếu tố phá vỡ**: màu tương phản bổ túc (hoa tím/hồng, cà chua đỏ, badge vàng, đất nâu sẫm) HOẶC vật thể/bố cục bất thường (cross-section cắt lớp đất, khoanh đỏ). Tránh nền + chủ thể cùng tông xanh. *(Đây chính là lý do hệ chữ vàng/đỏ của kênh thắng: nó chọi cả với nền xanh LẪN với UI trắng-đỏ của YouTube.)*

---

## 🛡️ GUARDRAILS (US compliance — bám brand voice)
- ❌ **Số bịa** — số trên thumb PHẢI khớp script (zero hallucination).
- ❌ **Overclaim/conspiracy:** "100%", "GUARANTEED", "SHOCKING", "They Don't Want You To Know", "Doctors HATE", "MIRACLE/CURES".
- ❌ **Human-fear:** "TOXIC!", "DEADLY!", "POISON!" về con người. ✅ Botanical shock OK ("INVASIVE!", "KILLS WEEDS").
- ❌ Chữ quá dài (>6 từ / >2 tầng) → mobile không đọc kịp. Giữ 2 tầng, hook vàng + phụ trắng.
- ❌ **KHÔNG người / mặt làm chủ thể** — kênh faceless, thumb object-driven (cả 2 biến thể A/B). Negative list trong prompt: `no face, no full person` (**KHÔNG cấm tay** — tay-prop là chữ ký kênh, 6/14 top thumb + champion AVD 49% có tay).
- ❌ **KHÔNG động vật đe dọa (rắn/chuột) làm hero** — fear-imagery hút sai khán giả ("Snakes" AVD 14.3%, tệ nhất kênh).
- ✅ **Complementarity Test (default):** gạch content word của thumb; mục tiêu 0 trùng với title. **NGOẠI LỆ — PROMISE-ECHO có chủ đích:** được phép lặp lời hứa title (champion AVD 49%: title "No Soil…No Cost" → thumb "ZERO SOIL / ZERO COST!") khi mục tiêu là hút ĐÚNG người xem (AVD) thay vì tò mò; đánh dấu `ECHO` trong bảng biến thể — không tính là FAIL.

---

## WORKFLOW

### Bước 1 — Lấy/viết text

> 🔀 **Packaging-first:** nếu `outline.md` block `## Thumbnail` ĐÃ có concept chốt (text + lever + pattern + visual) từ GATE outline → **DÙNG CHÍNH NÓ**. KHÔNG nghĩ TEXT/lever mới (sẽ phá nguyên tắc title+thumbnail khoá chung trước script). Chỉ xác minh số khớp script + chạy lại Complementarity Test. → nhảy Bước 2.
>
> Chỉ khi **thiếu** concept (chạy độc lập, không qua outline) mới tự viết 2–3 biến thể text dưới đây.

> 🅰️🅱️ **A/B test (BẮT BUỘC ở bước cuối) — 2 MODE theo độ chín của kênh:**
>
> 🚦 **CHỌN MODE THEO GIAI ĐOẠN PHÂN PHỐI (đọc `channel-stats` trước khi chọn):** nếu kênh đang **Browse demotion / impression thấp** (KPI view 5-ngày-đầu < 500) → **BẮT BUỘC MODE 1 (concept khác hẳn)**, TUYỆT ĐỐI không MODE 2. Lý do: impression thấp = Test & Compare không đủ mẫu thống kê → đổi 1 biến nhỏ (markup on/off, 1 từ) là **nhiễu vô nghĩa**; nếu A chết bạn cần 1 phương án THẬT SỰ khác để xoay, không phải bản gần-giống. Chỉ dùng MODE 2 (isolation tinh chỉnh) KHI phân phối đã phục hồi (impression ổn định, đủ mẫu đọc kết quả). *(Garden US tại 2026-07 đang trong demotion → mặc định MODE 1.)*
>
> **MODE 1 — CONCEPT TEST (MẶC ĐỊNH khi kênh chưa chốt công thức / data ít / đang demotion):** giống guru lớn (MrBeast, Paddy Galloway) qua YouTube *Test & Compare* — B **khác hẳn A**: khác **ảnh + chữ + cảm xúc + cảm-xúc-đích G4**, miễn cả hai vẫn ON-FORMULA (faceless, vàng+trắng, pass Complementarity + 5 GURU-gate + guardrails). Mục tiêu: tìm *concept lever lớn* nhanh. Title GIỮ NGUYÊN (Test & Compare chỉ đổi thumbnail).
> **📚 CONCEPT-PAIR LIBRARY (chọn 2 archetype KHÁC ĐÒN TÂM LÝ cho A & B):**
>
> | Archetype | Đòn tâm lý | Layout | Text mẫu (hook vàng / phụ trắng) |
> |---|---|---|---|
> | **Verdict / Myth-bust** | phán quyết, loss | Before→After ❌/✅ | `MYTH` / `BUSTED` |
> | **Curiosity / Question** | tò mò, mở loop | single hero + `?` đỏ | `DOES IT` / `WORK?` |
> | **Stat / Number shock** | giá trị, kết quả | hero + số badge vàng | `$500` / `IN YOUR YARD` |
> | **Versus / Comparison** | so sánh đúng-sai | split A \| B | `THIS` / `NOT THIS` |
> | **Warning / Stop** | cảnh báo | hero + ❌ + mũi tên | `STOP!` / `DON'T` |
>
> **Cách ghép MODE 1:** lấy **2 hàng KHÁC đòn tâm lý**. A và B mỗi cái 1 archetype → tự nhiên khác ảnh+chữ+cảm xúc. Cấm 2 archetype cùng đòn (ra ~giống nhau).
>
> 🔴 **Cặp mặc định = `Stat/Number shock` × `Verdict` (đổi 2026-08-15).** Trước đây mặc định là
> Verdict × Curiosity — **bỏ**, vì `Curiosity/Question` là archetype cho CTR thấp nhất đo được trên
> kênh này (1.5–1.7% với chữ kiểu "CAN THIS COME BACK?" / "SWEETER COLD"), trong khi thumbnail có
> **SỐ + triệu chứng cụ thể** đạt cao nhất (2.7%). Chi tiết + 3 confound: §CTR ĐO THẬT trong
> `thumbnail-stats-[slug].md`.
> Dùng `Curiosity/Question` **chỉ khi** biến thể đó vẫn mang một con số (vd `CAN THIS COME BACK?` →
> `DEAD IN 3 DAYS?`), hoặc khi user chủ động muốn test lại giả thuyết này.
>
> **Biến chính cần test trước mọi biến khác: CÓ SỐ vs KHÔNG SỐ.** Hai test A/B gần nhất của kênh đều
> trả "không có kết quả rõ ràng" — dấu hiệu hai biến thể quá giống nhau. Đừng test đổi màu/bố cục nhẹ
> khi chưa test xong biến này.
>
> **MODE 2 — ISOLATION TEST (khi ĐÃ có concept thắng → tinh chỉnh):** giữ archetype thắng y hệt, đổi **đúng 1 biến** (màu chữ vàng+trắng vs trắng · 1 từ hook · có/không markup). Học được *vì sao* thắng. Dùng sau khi MODE 1 ra winner.
>
> 🔴 **Quy tắc chung:** A & B KHÔNG được ra ~giống nhau (cấm chỉ khác "ánh sáng" trên cùng cảnh). MODE 1 → khác concept rõ; MODE 2 → khác đúng 1 biến. Cả hai vẫn faceless + pass guardrails.
> Packaging-first: lever cốt lõi giữ chung; MODE 1 cho phép B đổi text/concept (vì đang đi tìm công thức, chưa khoá cứng).

Tự kiểm mỗi biến thể:
- [ ] Text 2 tầng ALL CAPS, hook VÀNG + phụ TRẮNG (hoặc theo lựa chọn)?
- [ ] Pass **Complementarity Test** (0 từ trùng title — HOẶC đánh dấu `ECHO` nếu promise-echo có chủ đích)?
- [ ] **Pass 5 GURU-LAYER gate (G1 Squint · G2 One-Focal · G3 Curiosity-Gap · G4 Emotional-Proxy · G5 Pattern-Interrupt)?** 🔴 bắt buộc
- [ ] Pass guardrails (không 100%/conspiracy/human-fear/số bịa)? Faceless?
- [ ] Số (nếu có) khớp script?
- [ ] MODE 1: A & B khác concept (ảnh+chữ+cảm xúc+cảm-xúc-đích)? · MODE 2: khác đúng 1 biến?
→ In bảng `Biến thể | Concept | Cảm-xúc-đích (G4) | Text | Layout | Màu chữ | GURU 5G`.

### Bước 2 — Dựng 2 MASTER PROMPT A/B (CLEAN PLATE — ảnh nền sạch KHÔNG chữ + Spec Overlay tay/Pillow)

> 🔴 **LUẬT L29 (user duyệt 26/11/2026):** **KHÔNG để AI tự vẽ chữ lên thumbnail.** AI chỉ vẽ **ảnh nền sạch 16:9 (`clean plate`, 100% không chữ/không số/không icon lỗi)** có chừa sẵn **negative space tối/sạch** ở vùng trên-trái hoặc một bên; sau đó ghép chữ 2 tầng (VÀNG + TRẮNG, viền đen dày + đổ bóng), badge ❌/✅, khoanh đỏ/mũi tên bằng **Canva / Photoshop** hoặc **Python Pillow** (mẫu sẵn ở `tools/garden_thumb_real.py`).
> *Vì sao:* chữ ghép tay/Pillow sắc nét 100% ở cả 200px mobile lẫn Smart TV 4K, không bao giờ méo chữ/sai chính tả, dễ chạy A/B test đổi chữ trong 30 giây mà không phải render lại ảnh AI.

Xuất **2 gói (A & B)** lưu vào `thumbnail-prompts.md`, mỗi gói gồm:
- **(1) Clean-Plate Image Prompt (100% English, KHÔNG chữ)**
- **(2) Overlay Text & Markup Spec** (chữ dòng 1 VÀNG / dòng 2 TRẮNG, vị trí negative space, font Impact/Arial Black + stroke đen dày, vị trí ❌/✅ hoặc khoanh đỏ/mũi tên).

**Quy tắc chống lỗi cho Clean-Plate Prompt (áp cho CẢ A & B):**
1. Prompt 100% English (mô tả cảnh). KHÔNG để chữ tiếng Việt nào trong prompt.
2. **Chừa vùng trống có chủ đích cho chữ:** ghi rõ `clean dark-blurred negative space in the upper-left third (or left 40%) reserved for text overlay later` — đảm bảo độ tương phản cao khi dán chữ VÀNG/TRẮNG.
3. **Cấm tuyệt đối chữ & ký tự trong ảnh AI:** luôn khóa cuối prompt: `STRICTLY NO TEXT, no letters, no words, no numbers, no labels, no logos, no icons, no watermark anywhere in the image.`
4. Negative list rõ: `no face, no full person` (tay-prop OK — nếu cảnh có tay, mô tả rõ `a single hand as prop`), `no text, no typography, no letters, no numbers, no watermark, no logo, no UI, no distorted shapes`.
5. **G1 Squint áp vào Spec chữ overlay:** tổng chữ **≤5 từ**, hook vàng **≤3 từ/dòng**, font đậm + viền đen dày (`stroke ≥ 8–10px` ở 1280×720) + đổ bóng (đọc nét ở cả 200px mobile và Smart TV phòng khách).

**TEMPLATE WIN — Before→After Clean Plate (mặc định myth-bust/problem-fix; điền [...], xoá chú thích VN):**
```
A photorealistic 16:9 YouTube thumbnail background plate for a US home-gardening channel. Vivid natural colors, ultra high contrast, crisp studio-grade daylight, softly blurred garden background. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: an asymmetrical 40/60 before-and-after visual split (left 40% slightly darker/desaturated, right 60% brighter and vibrant), clean crisp vertical transition.
LEFT SIDE (the wrong way): [object SAI khớp script, e.g. a pile of crushed eggshells beside a wilted tomato showing a dark blossom-end-rot patch], framed slightly lower to leave clean dark negative space at the upper-left for text overlay later.
RIGHT SIDE (the fix): [object ĐÚNG khớp script, e.g. a hand pouring steady water onto mulched dark rich soil with a cluster of flawless ripe red tomatoes glowing in sunlight], large focal point filling the right side.

STRICTLY NO TEXT, no letters, no words, no numbers, no checkmarks, no X icons, no arrows, no labels, no watermark anywhere in the image.

Negative: no text, no typography, no letters, no numbers, no face, no full person, no watermark, no logo, no UI, no distorted shapes.
```
*Overlay Spec đi kèm Template WIN (ghép bằng Canva/Photoshop/Pillow):*
- **Line 1 (VÀNG `#FFD60A`, Impact/Anton/Montserrat Black, stroke đen 9–10px + drop shadow):** `[HOOK ≤3 WORDS]` (góc trên-trái / negative space)
- **Line 2 (TRẮNG `#FFFFFF`, stroke đen 8px):** `[SECOND LINE — NUMBER/PAYOFF]`
- **Markup vector sắc nét:** vòng tròn ❌ đỏ góc dưới-trái, ✅ xanh góc dưới-phải, khoanh đỏ nét đứt hoặc mũi tên cong (nếu cần).

> Listicle → đổi LAYOUT thành single hero lệch phải + chừa negative space bên trái cho vòng tròn số VÀNG & chữ 2 tầng. Reveal đơn → single hero + negative space sạch cho chữ & mũi tên vector.

**TEMPLATE B — tùy MODE đã chọn ở Bước 1:**

**▸ MODE 1 (Concept test — MẶC ĐỊNH):** B là **concept KHÁC HẲN**, vẫn on-formula & **clean plate không chữ**:
```
A photorealistic 16:9 YouTube thumbnail background plate for a US home-gardening channel. Vivid saturated natural colors, ultra high contrast, shallow depth of field, softly blurred dark garden soil background. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE dominant single hero object only — [chủ thể chính khớp script, e.g. a clear glass jar filled with glowing healthy white plant roots on rich dark soil], placed firmly on the right 55% of the frame, leaving clean dark blurred negative space across the left 45% for bold text overlay later. Macro crisp detail, golden-hour side lighting.

STRICTLY NO TEXT, no letters, no words, no numbers, no arrows, no question marks, no labels, no watermark anywhere in the image.

Negative: no text, no typography, no letters, no numbers, no face, no full person, no second competing object, no watermark, no logo, no UI, no distorted shapes.
```
*Overlay Spec đi kèm Template B:* đặt dòng hook VÀNG + dòng số/payoff TRẮNG vào 45% negative space bên trái + 1 mũi tên cong vàng/đỏ trỏ vào chủ thể.

**▸ MODE 2 (Isolation — khi đã có concept thắng):** dùng **cùng clean plate A**, chỉ đổi **đúng 1 biến trên layer overlay** (màu chữ ALL YELLOW vs vàng+trắng · đổi 1 từ hook · có/không badge ❌/✅) — tốn **0 credit render ảnh mới**!

### Bước 3 — Lưu file prompt A/B + Spec Overlay (BẮT BUỘC) + Render nền & ghép chữ (tùy chọn)

**3a. Luôn ghi file prompt + spec overlay trước** — `thumbnail-prompts.md` chứa CẢ 2 clean-plate prompt + bảng Overlay Spec (A + B):
```
[WORKSPACE_PATH]\scripts\big-idea-[NNN]-[slug]\thumbnail-prompts.md
```

**3b. Render 2 ảnh nền sạch không chữ (nếu user muốn ảnh luôn):**
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<CLEAN-PLATE PROMPT A>" \
  -o "[WORKSPACE_PATH]/scripts/big-idea-[NNN]-[slug]/thumbnail-a-clean.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<CLEAN-PLATE PROMPT B>" \
  -o "[WORKSPACE_PATH]/scripts/big-idea-[NNN]-[slug]/thumbnail-b-clean.png" -ar 16:9 -p nano --size 2K -v
```
*(Hoặc dùng ảnh thật từ `_LIBRARY/` / Pexels hoặc render nền sạch trên Goha Studio Nano Banana Pro 0 cr.)*

**3c. Ghép chữ 2 tầng & markup sắc nét:** ghép trên **Canva / Photoshop** theo Overlay Spec, hoặc chạy script Python Pillow (tham khảo `tools/garden_thumb_real.py`) xuất ra `thumbnail-a.png` và `thumbnail-b.png` (1280×720).

### Bước 4 — Verify + lưu spec
- Mỗi `thumbnail-[a/b].png` > 50KB, đúng 16:9 (1280×720).
- Mắt kiểm từng ảnh ở **2 kích thước** (thu nhỏ 200px như mobile + toàn màn hình như Smart TV): ảnh nền có lọt chữ rác AI không? chữ overlay VÀNG/TRẮNG có rõ nét, không đè chủ thể chính? tương phản đủ? số khớp script?
- Nếu ảnh nền AI vẫn lỡ sinh chữ thừa → xóa bằng inpaint/crop hoặc render lại nền sạch, **tuyệt đối không để chữ rác AI lọt ra ảnh xuất bản**.

---

## OUTPUT
```
[WORKSPACE_PATH]\scripts\big-idea-[NNN]-[slug]\
├── thumbnail-prompts.md    (BẮT BUỘC — Overlay Spec + lever + 2 clean-plate prompt A/B + nguồn số)
├── thumbnail-a-clean.png   (tùy chọn — ảnh nền sạch không chữ A)
├── thumbnail-b-clean.png   (tùy chọn — ảnh nền sạch không chữ B)
├── thumbnail-a.png         (tùy chọn — bản hoàn chỉnh A sau khi ghép chữ Canva/Photoshop/Pillow)
└── thumbnail-b.png         (tùy chọn — bản hoàn chỉnh B sau khi ghép chữ Canva/Photoshop/Pillow)
```

🔴 **GATE:** present 2 clean-plate prompt + Overlay Spec (+ ảnh nếu đã render/ghép) → chờ user chọn **A hay B** / "render lại nền" / "chỉnh chữ".

---

## GUARDRAILS (tóm)
1. Số trên thumb = số trong script (zero hallucination).
2. Bổ trợ title (Complementarity Test) + kéo lever Value Equation khác title.
3. Không conspiracy/overclaim/human-fear.
4. **FACELESS — không người/mặt làm chủ thể; không động vật đe dọa làm hero** (cả A & B; negative list `no face, no full person`; tay-prop OK khi được mô tả rõ).
5. **L29 — TÁCH NỀN SẠCH + GHÉP CHỮ TAY/PILLOW:** prompt AI luôn khóa `STRICTLY NO TEXT`; chữ **2 tầng hook VÀNG + phụ TRẮNG** (~4–6 từ) + viền đen dày/bóng + badge ❌/✅ ghép sắc nét bằng Canva/Photoshop/Pillow để đọc nét trên cả **Smart TV** lẫn **mobile**.
6. Chỉ kênh US (project-scoped), không đụng kênh JP.
7. Không chữ meta/trừu tượng (`Study/Test/Research/Count This Number` — L21) và không nhãn tuổi (`Senior/Over 60/No Back Pain` — L9).
8. **5 GURU-LAYER gate** (Squint Smart TV+Mobile / One-Focal / Curiosity-Gap / Emotional-Proxy / Pattern-Interrupt) — mọi biến thể PASS đủ 5 mới xuất prompt.
