---
name: garden-us-thumbnail
description: "Tạo thumbnail YouTube cho kênh Garden US (English) theo CÔNG THỨC WIN đúc kết từ thumbnail thật của kênh (references/thumbnail-stats-garden-us-60k.md): FACELESS object-driven, text 2 tầng ALL CAPS (hook VÀNG + phụ TRẮNG), layout Before→After ❌/✅ / number-badge / triptych, markup khoanh đỏ + mũi tên, Complementarity 1+1=3 (bổ trợ title). Bước cuối sinh thumbnail-prompts.md với 2 MASTER PROMPT A/B (A=layout WIN · B=đổi đúng 1 biến để test), render (Nano Banana Pro) + verify tùy chọn. KHÔNG conspiracy/overclaim/human-fear. CHỈ workspace Garden US, KHÔNG dùng kênh JP. USE WHEN user nói 'tạo thumbnail', 'làm thumb', 'thumbnail cho video', 'tạo ảnh thumbnail', 'thumb cho script', 'cover video', sau khi script.md/outline.md đã xong, hoặc tại bước thumbnail trong pipeline Garden US."
---

# Garden US — Thumbnail Generator (Complementarity · render-ready prompt)

> ⚠️ **SKILL RIÊNG CHO KÊNH GARDEN US.** Project-scoped trong `.claude/skills/` của workspace US → chỉ load khi mở kênh US. Công thức = English ≤3 từ ALL CAPS (KHÁC skill JP chữ 3 tầng). Khi config có `thumbnail_skill` trỏ về đây, `mkt-youtube-outline` Bước 5 sẽ NHƯỜNG cho skill này.

Mục tiêu: biến text thumbnail của outline thành **2 master prompt A/B render-ready** theo **công thức WIN của kênh** (FACELESS · text 2 tầng hook VÀNG + phụ TRẮNG · layout Before→After/number-badge/triptych · markup đỏ) — bổ trợ title (1+1=3), số trên thumb = số trong script. Bước cuối luôn xuất `thumbnail-prompts.md`; render ảnh tùy chọn.
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

**G1 — SQUINT TEST (mobile nhỏ + mắt kém 60-80t)** 🔴 gate CTR số 1 của kênh này
Hình dung thumbnail thu nhỏ còn ~200px (bằng con tem trong feed mobile). Trong 0.5 giây phải: (a) đọc được dòng chữ VÀNG, (b) nhận ra chủ thể chính. Nếu phải nheo mắt → FAIL. Hệ quả cứng: **dòng hook vàng ≤3 từ/dòng**, chủ thể chính chiếm **≥40% khung**, và chi tiết nhỏ (nhãn bao phân, 1 mắt lá, chữ phụ) KHÔNG được là thứ *bắt buộc phải thấy* mới hiểu thumb.

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

### Bước 2 — Dựng 2 MASTER PROMPT A/B (baked text, render-ready)

Xuất **2 prompt** (A = layout WIN · B = đổi đúng 1 biến). Lưu cả 2 vào `thumbnail-prompts.md`.

**Quy tắc chống lỗi (áp cho CẢ A & B) — prompt xuất ẢNH HOÀN CHỈNH CÓ CHỮ, không overlay sau:**
1. Prompt 100% English (mô tả cảnh). KHÔNG để chữ tiếng Việt nào trong prompt.
2. Text overlay đặt trong "..." + lệnh khóa: *render exactly, do NOT translate, do NOT add other text*.
3. Negative list rõ: `no face, no full person` (tay-prop OK — nếu cảnh có tay, mô tả rõ "a single hand as prop"), no extra text/letters/numbers, no watermark, no logo, no gibberish.
4. Text **2 tầng ALL CAPS**; nêu RÕ màu từng dòng (hook VÀNG, phụ TRẮNG — hoặc theo lựa chọn A/B).
5. Mỗi dòng: thick bold sans-serif + **heavy black outline + drop shadow** (nổi trên mọi nền).
6. Chữ KHÔNG đè chủ thể chính; đặt vào negative space.

**🔤 Reliability chữ bake (vì AI phải render CHỮ + ẢNH trong 1 lần — càng nhiều element, AI càng méo chữ):**
7. **Giảm tải cho AI:** tổng chữ **≤5 từ**, **tối đa 2 màu**. Nếu cảnh đã có markup phức tạp (❌✅ + khoanh đỏ + mũi tên) → rút hook còn **1–2 từ** để nhường "ngân sách render" cho chữ sắc nét. Ưu tiên tuyệt đối: **chữ đúng chính tả > markup đẹp** (chữ méo giết CTR mạnh hơn thiếu 1 mũi tên).
8. **Khóa chính tả từng chữ** trong prompt: `The ONLY text in the entire image is exactly two words: "WORD1" in yellow and "WORD2" in white — spelled letter for letter, nothing else, no other letters, numbers, or words anywhere.`
9. **G1 Squint áp vào chữ:** hook vàng ≤3 từ/dòng (đọc được ở 200px). Chữ dài hơn → AI dễ méo VÀ mắt kém đọc không kịp — cắt ngắn, đừng thu nhỏ font.

**TEMPLATE WIN — Before→After ❌/✅ (mặc định myth-bust/problem-fix; điền [...], xoá chú thích VN):**
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background. NO human face, no full person (a single hand as prop is allowed only if described).

LAYOUT: a clean before→after split, two halves.
LEFT HALF (the wrong way): [object SAI khớp script, e.g. a pile of crushed eggshells + a tomato with a black blossom-end-rot patch]. A bold red dashed circle around the key detail and a large red ❌ over it.
RIGHT HALF (the fix): [object ĐÚNG khớp script, e.g. a watering can pouring steady water + straw mulch + a flawless ripe tomato]. A bright green ✅ on this side.

TEXT — render EXACTLY two stacked words in very thick bold sans-serif, heavy black outline + drop shadow, centered, NOT covering the main objects: line 1 "[HOOK WORD]" in bright YELLOW, line 2 "[SECOND WORD]" in WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no face, no full person, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```
> Listicle → đổi LAYOUT thành single hero + **số trong vòng tròn VÀNG** góc trên-trái. Reveal đơn → single hero + mũi tên cong + text negative space.

**TEMPLATE B — tùy MODE đã chọn ở Bước 1:**

**▸ MODE 1 (Concept test — MẶC ĐỊNH):** B là **concept KHÁC HẲN**, vẫn on-formula. Mẫu "Curiosity/Question single-hero":
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel, audience 50–80. Vivid saturated colors, ultra high contrast, blurred garden background. NO human face, no full person (a single hand as prop is allowed only if described).

SCENE: ONE single hero object only — [chủ thể chính khớp script, e.g. a glass jar of crushed eggshells on dark soil], offset to one side leaving clean negative space. A bold red question-mark drawn next to it [or a curved yellow arrow pointing at it]. Macro, shallow depth of field.

TEXT — render EXACTLY this short question in very thick bold sans-serif, heavy black outline + drop shadow, in the negative space, NOT covering the object: "[QUESTION ≤3 WORDS]" with the key word in bright YELLOW and the rest WHITE.
Do NOT add any other text, words, letters, numbers, captions, labels or watermark.

Negative: no face, no full person, no second object, no extra text, no gibberish letters, no watermark, no logo, no UI, no distorted shapes.
```
> A = Verdict/Before→After (phán quyết) · B = Curiosity/Question single-hero (tò mò) → khác ảnh + chữ + cảm xúc. Cả hai faceless + on-formula.

**▸ MODE 2 (Isolation — khi đã có concept thắng):** copy Template WIN, đổi **đúng 1 biến**:
- *màu chữ:* 2 dòng thành **ALL YELLOW** (pattern champion AVD 49% "ZERO SOIL / ZERO COST!") hoặc ALL WHITE → đo vs vàng+trắng mặc định.
- *bố cục:* bỏ split → **single hero** → đo comparison vs single-hero.
- *markup:* bỏ khoanh đỏ/❌/✅ → đo có markup vs sạch.
> ⚠️ MODE 2 chỉ đổi 1 biến, giữ phần còn lại Y HỆT để cô lập.

### Bước 3 — Lưu file prompt A/B (BẮT BUỘC) + Render (tùy chọn)

**3a. Luôn ghi file prompt trước** — `thumbnail-prompts.md` chứa CẢ 2 master prompt render-ready (A + B), để user dán vào tool ảnh bất kỳ / A/B test sau:
```
[WORKSPACE_PATH]\scripts\big-idea-[NNN]-[slug]\thumbnail-prompts.md
```

**3b. Render cả 2 biến thể (nếu user muốn ảnh luôn):**
```bash
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT A>" \
  -o "[WORKSPACE_PATH]/scripts/big-idea-[NNN]-[slug]/thumbnail-a.png" -ar 16:9 -p nano --size 2K -v
python3 "C:/Users/admin/.claude/skills/image-post-creator/scripts/generate.py" "<MASTER PROMPT B>" \
  -o "[WORKSPACE_PATH]/scripts/big-idea-[NNN]-[slug]/thumbnail-b.png" -ar 16:9 -p nano --size 2K -v
```
> `nano` (Gemini Flash Image) render chữ tốt. Chữ sai nét → render lại / rút ngắn text / tối đa 2–3 lần/biến thể.

### Bước 4 — Verify + lưu spec
- Mỗi `thumbnail-[a/b].png` > 50KB, đúng 16:9.
- Mắt kiểm từng ảnh: text TRẮNG đúng/đủ? không đè mặt/chủ thể? tương phản đủ? không chữ thừa? số khớp script?
- `thumbnail-prompts.md` ghi: text trắng + lever + pattern + **2 master prompt (A subject / B botanical)** + nguồn số (khớp script).
- Chữ baked sai dai dẳng sau 3 lần → **RÚT NGẮN chữ** (hook còn 1 từ) + **đơn giản hoá markup** (bỏ bớt mũi tên/khoanh, giữ ❌✅ nếu cần) rồi render lại. **Giữ ảnh hoàn chỉnh từ prompt — KHÔNG chuyển sang overlay Canva** (yêu cầu: prompt phải xuất ảnh hoàn chỉnh có chữ). Ít element hơn = AI bake chữ chuẩn hơn.

---

## OUTPUT
```
[WORKSPACE_PATH]\scripts\big-idea-[NNN]-[slug]\
├── thumbnail-prompts.md   (BẮT BUỘC — text trắng + lever + 2 master prompt A/B + nguồn số)
├── thumbnail-a.png        (tùy chọn — Variant A: layout WIN, hook vàng + phụ trắng)
└── thumbnail-b.png        (tùy chọn — Variant B: đổi 1 biến để A/B test)
```

🔴 **GATE:** present 2 prompt (+ 2 ảnh nếu đã render) → chờ user chọn **A hay B** / "render lại" / "đổi nền".

---

## GUARDRAILS (tóm)
1. Số trên thumb = số trong script (zero hallucination).
2. Bổ trợ title (Complementarity Test) + kéo lever Value Equation khác title.
3. Không conspiracy/overclaim/human-fear.
4. **FACELESS — không người/mặt làm chủ thể; không động vật đe dọa làm hero** (cả A & B; negative list `no face, no full person`; tay-prop OK khi được mô tả rõ).
5. Chữ **2 tầng hook VÀNG + phụ TRẮNG** (~4–6 từ) + viền/bóng; bước cuối luôn xuất `thumbnail-prompts.md` (2 biến thể A/B).
6. Chỉ kênh US (project-scoped), không đụng kênh JP.
7. Chữ baked sai dai dẳng → rút ngắn chữ + đơn giản element, render lại (GIỮ ảnh hoàn chỉnh từ prompt, KHÔNG overlay Canva).
8. **5 GURU-LAYER gate** (Squint / One-Focal / Curiosity-Gap / Emotional-Proxy / Pattern-Interrupt) — mọi biến thể PASS đủ 5 mới xuất prompt.
