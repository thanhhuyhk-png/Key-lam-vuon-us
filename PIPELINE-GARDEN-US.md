# 🌱 PIPELINE GARDEN US — Local-First (Script Production)

> Sơ đồ pipeline sản xuất kịch bản YouTube kênh làm vườn US.
> Cập nhật: 2026-11-26 (tích hợp Auto Trend Studio vào Bước 0; khóa cứng `en-US` & tắt dịch ES `translate_es: false` theo L28; thumbnail tách nền sạch ghép chữ tay/Pillow theo L29)

---

## Sơ đồ tổng thể

```
═══════════════════════════════════════════════════════════════════
  GIAI ĐOẠN 0 — TÌM CHỦ ĐỀ  (một đường duy nhất, 0 credit tới cổng ③)
═══════════════════════════════════════════════════════════════════

  [0] tools/do_trend.py  (CN + giữa tuần, chạy nền ~20 phút)
       ├─ trend 10 ngày: video đang lên + từ khoá ĐA_KENH
       ├─ trend mùa: cùng kỳ năm ngoái (đăng trước đỉnh 2–4 tuần)
       └─ đà kênh
       ↓ tools/kiem_de_tai.py kiem  (CHẶN = dừng)
       ↓ TOPIC GATE ①②③ (references/topic-gate-en.md) · ② = báo cáo trend · ③ = vidIQ keyword US
       ↓ san-y-tuong Vòng A/B (chỉ khi chọn giữa ≥ 2 ý) · cú đánh lớn: ý từ tools/sinh_y.py
       ↓ GATE: chọn ý → title A/B/C đều chứa từ khoá trend (~25 ký tự đầu)

═══════════════════════════════════════════════════════════════════
  PIPELINE VIẾT SCRIPT  (lặp cho từng Big Idea đã chọn)
═══════════════════════════════════════════════════════════════════

  [1] mkt-youtube-outline
       ├─ Web research thực tế
       ├─ Chọn format (Listicle/Problem-Fix/Dollar/Plant Once/Transform)
       ├─ 3 title options (A/B/C)         🛡️ guardrail: no conspiracy
       └─ Thumbnail concept               🛡️ guardrail: no human fear
       ↓ 🔴 GATE: chọn title + approve outline
       │  └─ output: outline.md

  [1.5] mkt-youtube-deep-research
       ├─ Đọc outline.md
       ├─ Check Format vs Big Idea (MATCH/MISMATCH)
       ├─ Sinh 5 câu hỏi đào sâu
       ├─ Tự research từng câu (.edu/.gov/peer-reviewed)
       └─ Gắn cờ YMYL claims              🛡️ flag YMYL
       ↓ 🔴 GATE: approve research brief
       │  └─ output: research-brief.md

  [2] mkt-hook-kallaway
       ├─ 5-8 biến thể hook (SSSQ + 3-alignment)
       └─ Tự audit theo checklist 7 bước  🛡️ guardrail: no overclaim
       ↓ 🔴 GATE: chọn hook
       │  └─ hook đã approve

  [3] youtube-garden-us  ◄── nhận 3 input: outline + research-brief + hook
       │
       ├─ SETUP: load brand-voice-dna.md
       │
       ├─ PHASE 1 — VIẾT SCRIPT
       │   ├─ HOOK (dán hook đã approve, không viết lại)
       │   ├─ CREDIBILITY → PREVIEW → MAIN CONTENT → CONCLUSION
       │   ├─ Chỉ dùng claims từ research-brief.md
       │   ├─ 🧩 Jenga Retention Layer (BẮT BUỘC cho Problem-Fix — bắc cầu mid-roll dip phút 4-6)
       │   └─ Signature phrases checklist
       │
       └─ PHASE 2 — QA + EXPORT  (sửa 2026-11-08: phản biện kép thay compliance loop)
           ├─ ⚙️ tools/gate.py  (7 cổng máy — orchestrator TỰ chạy sau MỖI lần script đổi)
           ├─ 2.1 Self-audit 8 góc — lọc thô của người viết, KHÔNG tính là phản biện
           ├─ 2.1.5 Triple F Boost — chỉ trả bảng diff (≤25 câu), không thay cả bài → gate.py
           ├─ 2.2 ⭐ PHẢN BIỆN KÉP ĐỘC LẬP (3R) — ≥2 vòng
           │       R1 Agy --sandbox (khác hãng) + R2 sub-agent Opus ngữ cảnh mới
           │       thư mục cách ly: CHỈ script (có thẻ [C..]) + research-brief + allowed-numbers + brief
           │       soi 6 mục: dữ kiện theo Claim Ledger · an toàn · chính sách/inauthentic ·
           │                  giữ chân (bản đồ loop) · chấm phần mở /35 · cảnh báo dựng
           │       R2 chấm luôn Risk Score 0–10 (mkt-yt-compliance) = Compliance Score chính thức
           │       → lọc nhận/bác bằng bằng chứng (phan-bien-vN.md) → danh sách quyết định D1..Dn
           │       → 1 người biên tập sửa đúng danh sách → gate.py → vòng 2 chỉ soi vùng đã sửa
           │       (còn lỗi CHẶN sau vòng 2 → dừng, hỏi user)
           ├─ 2.3 TTS Clean (số→chữ, bỏ markdown) → gate.py
           └─ 2.4 Lưu script.md
       ↓ 🔴 GATE: approve script (Compliance Score · Hook /35 × 2 · sổ nhận/bác · gate.py cuối)
       │  └─ output: script.md (EN)

  [4] XUẤT BẢN SEO (`en-US` DUY NHẤT — L28 cấm Localization ngoài Mỹ)
       │
       ├─ [4a] mkt-yt-seo-description (EN)
       │        đọc script.md → seo-en.md
       │
       └─ [4b/4c] ~~dịch ES (`script-es.md` / `seo-es.md`)~~ → ĐÃ TẮT từ 26/11/2026 (`translate_es: false`)
       ↓ ✅ DONE

═══════════════════════════════════════════════════════════════════
  🔧 CÔNG CỤ ON-DEMAND  (gọi khi cần, không trong luồng chính)
═══════════════════════════════════════════════════════════════════

  • mkt-youtube-script-audit       → audit độc lập (chạy AI khác)
  • mkt-kane-gold-comparison       → benchmark vs Gold reference
  • mkt-kane-triple-f-boost        → script khô, thêm Feelings/Fun
  • mkt-kane-cta-non-autocratic    → CTA yếu, viết lại
  • mkt-kane-anti-pattern-auditor  → nghi over-branding
```

---

## 📁 Output cuối — tất cả local

```
D:\0002-Team A Nam\scripts\big-idea-[NNN]-[slug]\   ← [NNN] zero-pad 3 chữ số (folder mới)
├── pipeline-state.md   ← bảng theo dõi 6 bước ✅/⬜ (cập nhật mỗi GATE)
├── outline.md          ← [1] mkt-youtube-outline
├── research-brief.md   ← [1.5] mkt-youtube-deep-research
├── script.md           ← [3] youtube-garden-us (EN)
├── seo-en.md           ← [4a] mkt-yt-seo-description (CHỈ en-US — đã TẮT ES từ 26/11/2026)
└── audit-report.md     ← [tùy chọn] mkt-youtube-script-audit
```

---

## 🔍 Phản biện kép (3R) — thêm 2026-11-08

| Thành phần | Tệp |
|---|---|
| Brief người phản biện (chung cho R1, R2) | `templates/brief-phan-bien.template.md` — lỗi CHẶN/NÊN SỬA bắt buộc `Before → After` (L25) |
| Brief người phản biện đóng gói (R3, vòng 1, thêm 22/11/2026) | `templates/brief-phan-bien-dong-goi.template.md` — tiêu đề ↔ 60 s đầu · chặn thumbnail số trừu tượng · 3 phương án thumbnail (L21, L25) |
| Sổ nhận/bác + danh sách quyết định | `templates/phan-bien-so.template.md` → `scripts/<tập>/phan-bien-vN.md` |
| Cổng máy gộp | `python -X utf8 tools/gate.py scripts/<tập>` → `gate-log.md` |
| So trùng đối thủ | `scripts/<tập>/competitor-transcripts/` (transcript outlier cùng chủ đề, lấy ở Topic Gate) |
| Sổ cách nói đã chốt | `references/cach-noi-da-chot.tsv` — `script_lint.py` tự chặn tái phạm |
| Báo nhầm đã biết | `references/lessons-learned.md` § 🧯 |

Vì sao: người viết tự chấm bài mình có điểm mù; mỗi bản vá có thể làm hở chỗ khác (gold-standard: 4 vòng mới sạch); hai hãng bắt hai loại lỗi khác nhau. Ngưỡng so trùng đối thủ (≤1 % 6-gram, 0 đoạn chép ≥10 từ) mượn từ kit tiếng Việt — **cần hiệu chỉnh** trên 2–3 cặp kênh tự viết cùng chủ đề, ghi vào `research/bench/BENCH.md`.

## 🛡️ Compliance — 2 tầng

```
Tầng 1 (guardrail nhẹ):  outline + deep-research + hook
                         → ngăn vi phạm từ gốc, không tốn token
Tầng 2 (full audit):     youtube-garden-us Phase 2.2 — phản biện kép 3R
                         → R2 Opus chấm mkt-yt-compliance Score 0-10, ≥2 vòng
                         + compliance_scan.py (regex) trong tools/gate.py
```

**Nguyên tắc:** Khi xung đột giữa voice DNA và compliance → **compliance thắng**.

---

## 📊 Bảng skills trong pipeline

| Bước | Skill | Trạng thái | Vai trò |
|------|-------|-----------|---------|
| 0 | `tools/do_trend.py` → TOPIC GATE → `san-y-tuong` | **Mới 18/11** | Một đường tìm chủ đề, 0 credit tới cổng ③ |
| **R1–R3** *(lane B)* | `seed-brief.template.md` | **Mới 09/04** | Tái thẩm seed + giải phẫu lời hứa + đổi vật chủ → 🔴 GATE 0 |
| 1 | `mkt-youtube-outline` | Mới + guardrail | Outline + 3 titles + thumbnail |
| 1.5 | `mkt-youtube-deep-research` | Mới | 5 câu hỏi + fact-check + YMYL flag |
| 2 | `mkt-hook-kallaway` | Có sẵn + guardrail | 5-8 hook + audit |
| 3 | `youtube-garden-us` | Đã sửa | Viết script + compliance loop + TTS |
| 3-QA | `mkt-yt-compliance` | Có sẵn (tích hợp) | Risk Score 0-10 |
| 4a/4c | `mkt-yt-seo-description` | Đã sửa (local) | SEO EN + ES |
| 4b | `mkt-yt-translate-es` | Đã sửa (local) | Dịch ES US-Hispanic |
| 3R | Agy + sub-agent Opus | **Mới 08/11** | Phản biện kép độc lập ≥2 vòng (brief chung) |
| 3-gate | `tools/gate.py` | **Mới 08/11** | 7 cổng máy, chạy sau mỗi lần script đổi |
| Tùy chọn | `mkt-youtube-script-audit` | Có sẵn | Audit sâu thêm — không thay 3R |

---

## ⚙️ Model Routing & Token (tối ưu chi phí)

**Cơ chế:** SKILL.md chạy trong context model chính → **không tự đổi model**. Đổi model thật chỉ qua **subagent**. Vì vậy:

| Bước | Model nên chạy | Cách |
|------|----------------|------|
| [1] Outline | **Opus** (sáng tạo title/structure) | chạy ở conversation chính |
| [1.5] Deep Research | **Sonnet** | ✅ subagent `garden-deep-researcher` — orchestrator **LUÔN delegate**, không tự WebFetch (giữ research khỏi context chính) |
| [2] Hook | Opus | conversation chính |
| [3] Script + Compliance | **Opus** (chất lượng cao nhất) | conversation chính |
| [4a/4c] SEO | **Haiku** | ✅ subagent `garden-seo` — orchestrator delegate, ra khỏi context Opus |
| [4b] Dịch ES | **Sonnet** | ✅ subagent `garden-translate-es` — delegate, no compliance |

**Token-light đã áp dụng:**
- Brand voice: đọc block `## AI Quick Start` để viết, full chỉ khi audit fail.
- Channel stats: đọc block `## ⚡ AUDIT TL;DR` (~20 dòng) thay full 150 dòng.
- Handoff giữa bước: truyền **path**, không paste nội dung.
- Compliance loop: gửi **đoạn vi phạm**, không rewrite full script.

> ✅ Đã có 3 subagent isolated: `garden-deep-researcher` (Sonnet, [1.5]), `garden-seo` (Haiku, [4a/4c]), `garden-translate-es` (Sonnet, [4b]). Bước [4] orchestrator luôn delegate.

---

## 🔑 Lệnh khởi động nhanh

### TÌM CHỦ ĐỀ *(một đường cho cả hai lane)*

| Bước | Gõ gì | Output |
|------|-------|--------|
| Dò trend | `dò trend` | `research/trend-us/<YYYYMMDD>/bao-cao-trend.md` (báo cáo > 3 ngày tuổi thì chạy lại) |
| Kiểm ý | `kiểm định ý X` | Topic Gate ①②③ trong `pipeline-state.md` (+ `san-y-tuong` khi chọn giữa ≥ 2 ý) |

### LANE B — REMAKE

| Khi nào | Gõ gì | Output |
|---------|-------|--------|
| có link video hoặc chọn 1 video trong báo cáo trend | `remake video <link>` | `scripts/remake-[NNN]-[slug]/seed-brief.md` → 🔴 GATE 0 |

### LANE A — BIG IDEA *(mặc định)*

| Bước | Gõ gì |
|------|-------|
| Outline | `tạo outline video về [topic]` |
| Deep research | `research kịch bản` (sau khi có outline) |
| Hook | `viết hook cho video` |
| Script | `viết script từ outline` |
| SEO | `viết SEO description` |
| Dịch ES | `dịch sang ES` |
| Audit (tùy chọn) | `audit kịch bản` |

---

## 📌 Nguyên tắc cốt lõi

1. **Local-first** — toàn bộ output là file `.md` trong `D:\0002-Team A Nam\scripts\`, không phụ thuộc Notion khi viết
2. **Zero hallucination** — thiếu data → `[NEED DATA: ...]`, không bịa
3. **Narrator = educator** — kể lại kiến thức, không đóng vai nhân chứng cá nhân
4. **Compliance thắng** khi xung đột với voice
5. **Hard gates** — bắt buộc dừng chờ user confirm ở mỗi bước chính
6. **Humanization** — đã tích hợp qua Human Texture E7 trong brand-voice-dna + audit check
