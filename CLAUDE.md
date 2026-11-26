# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

Production workspace cho kênh YouTube làm vườn US (Garden US). Pipeline chạy local-first: từ Radar xu hướng (Auto Trend Studio + `do_trend.py`) → Big Idea/Remake → Outline → Research → Hook → Retention Spine → Script (EN) → SEO `en-US` *(đã tắt dịch ES từ 26/11/2026)*.

Brand Voice: **Lazy Grandma Wisdom meets Science-Backed Proof** — nguồn sự thật gộp (voice + số liệu kênh) trong `references/channel-truth.md`; deep-dive tone trong `references/brand-voice-dna.md`.  
Pipeline đầy đủ: xem `PIPELINE-GARDEN-US.md`.

---

## Skill Routing — BẮT BUỘC ĐỌC TRƯỚC KHI GỌI SKILL

### Trigger → Skill đúng

| Khi user nói… | Gọi skill này | KHÔNG gọi |
|---------------|---------------|-----------|
| "viết kịch bản big idea #N" / "script big idea N" / "làm video big idea N" / "chạy pipeline big idea N" | **`skill-garden-us-pipeline`** | ~~mkt-ideas-to-script-notion~~ |
| "dò trend" / "trend tuần này" / "tìm chủ đề mới" / "làm video gì tiếp" / "tuần này làm video gì" / "video nào đang được đẩy" / "quét seed" / "radar tuần" | **ĐƯỜNG TÌM CHỦ ĐỀ DUY NHẤT** (mục «Tìm chủ đề» ngay dưới): `tools/do_trend.py` → `kiem_de_tai.py` → TOPIC GATE ①②③ → `san-y-tuong` (khi chọn giữa ≥ 2 ý) | ~~mkt-big-idea~~ ~~youtube-trend-finder~~ ~~breakout-video-finder~~ ~~mkt-topic-to-video-ideas~~ ~~mkt-youtube-topic-researcher~~ ~~notion-video-trend-sync~~ ~~10x-youtube-niche-*~~ ~~R0 vidiq_outliers vph~~ |
| "remake video này" / "viết kịch bản remake" / đưa link YouTube kèm ý định làm bản của mình (hoặc chọn 1 video trong báo cáo trend) | **`skill-garden-us-pipeline` — LANE REMAKE** (Bước 0-B: R1 → lọc SEED PHẢI BỎ → **R1.5 phân loại archetype** → R2/R3 → title → 🔴 GATE 0) | ~~mkt-big-idea~~ |
| "tạo outline" / "outline video" | **`mkt-youtube-outline`** (qua pipeline) | |
| "viết hook" | **`mkt-hook-kallaway`** (qua pipeline) | |
| "audit kịch bản" | **`mkt-youtube-script-audit`** | |
| "health check" / "sức khỏe kênh" / "kênh tụt view" / "audit kênh" | **`yt-channel-health-audit`** (chỉ kiểm sức khoẻ kênh, KHÔNG dùng để tìm chủ đề) | ~~yt-weekly-health-check~~ (đã xoá, skill mới thay thế) |
| "SEO description" | **`mkt-yt-seo-description`** | |
| "dịch sang ES" / "Spanish" | **`mkt-yt-translate-es`** | |
| "lập bản đồ hình" / "tìm footage cho video" / "prompt clip AI" / "chuẩn bị dựng video" | **`garden-video-map`** *(TEST từ 01/11/2026)* | |
| "caption news" / "làm video caption news" / "video tin tức làm vườn" / "garden caption news" | **`garden-caption-news`** | |

**Quy tắc vàng:** Mọi yêu cầu liên quan đến "viết kịch bản" cho kênh Garden US đều đi qua `skill-garden-us-pipeline`. Skill này là orchestrator — nó tự gọi các skill con.

### Tìm chủ đề — MỘT đường duy nhất (user chốt 18/11/2026)

1. **Dò trend** (0 credit, ~20 phút, chạy nền; CN + một lần giữa tuần — lần 2 có tốc độ view [ĐO] thật):
   `python -X utf8 tools/do_trend.py --ds research/trend-us/kenh-ngach.txt --video-dir research/top20-<ngày>/thu-video --tim "<10–15 cụm mùa, đổi theo tháng>" --goi-y --lich research/trend-us/lich-vuon-us.tsv --out-dir research/trend-us/<YYYYMMDD>`
   → `bao-cao-trend.md`: mốc mùa vụ 45 ngày · từ khoá trend 10 ngày (kèm gợi ý tìm kiếm US) · trend mùa (cùng kỳ năm ngoái) · video đang lên (hệ số + VPH tb/đo) · đà kênh. Báo cáo > 3 ngày tuổi thì chạy lại. Chỉnh bộ lọc xong thì chấm lại không tải: `--nap-meta research/trend-us/<ngày>/meta-video.jsonl`. Test: `python -X utf8 -m pytest -q tools/tests/test_do_trend.py -p no:cacheprovider`.
   Thứ tự tin tín hiệu cổng ② (nâng cấp 22/11/2026, `references/do-trend-garden-de-xuat.md`): trend mùa ≥ 2 kênh + gợi ý US ≥ 1 → mốc mùa vụ PHIM_DAI (≥ 21 ngày) + gợi ý US ≥ 1 → ĐA_KENH 10 ngày (làm gấp) → còn lại chỉ theo dõi. Cờ YMYL: không tự đề xuất.
2. **Kiểm trùng** `tools/kiem_de_tai.py kiem` (CHẶN = dừng).
3. **TOPIC GATE ①②③** (`references/topic-gate-en.md`): ② lấy từ báo cáo trend, ③ vidIQ keyword US. Hạn: trend 10 ngày → đăng ≤ 10 ngày; trend mùa → đăng trước đỉnh 2–4 tuần.
4. **`san-y-tuong`** Vòng A/B chỉ khi phải chọn giữa ≥ 2 ý. Suất «cú đánh lớn» (1/4 video) lấy ý từ `tools/sinh_y.py`, cũng qua bước 1–3.
5. **Tiêu đề A/B/C** đều chứa ≥ 1 từ khoá trend trong ~25 ký tự đầu, chỉ khi video nói đúng về nó (luật ở `topic-gate-en.md` ②).

**Top 20 và Model Link trong đường này (user duyệt 18/11/2026):**
- **Top 20** (`tu-duy-top-20-ytb`, đo lại mỗi tháng, lần tới 16/12) chỉ là **danh sách kênh + nền đo**: kênh lõi làm vườn → `research/trend-us/kenh-ngach.txt`; `thu-video/` → nền view từng kênh cho `do_trend.py --video-dir`. Đo top 20 mới thì cập nhật cả hai.
- **Model Link** (Frugal Solutions) chỉ là **mẫu cách làm** (đóng gói tiêu đề, cách dựng). ⛔ Không bám đề tài của Model Link — đề tài chỉ từ báo cáo trend. Theo dõi đà Model Link bằng `trend-kenh.tsv` (`da_view_60`); kênh cờ NGUNG không được làm Model Link. Thôi bám khi 3 video bám mà views_5d không vượt 896.
- Tab «ý tưởng» trong YouTube Studio: không dùng (10 video kênh đã làm theo chủ đề kiểu này, 9/10 dưới trung vị kênh, đo 16/11).

Đã cất 18/11/2026 (không dùng nữa): R0 radar seed `vidiq_outliers sort=vph` + kho seed tuần, `trend-radar` chạy tay, Lane A «Big Idea #N từ Notion» (`mkt-big-idea`), và 6 skill chung tìm ý (`~/.claude/_luu-tru/skills-2026-11-18/`). Tệp cũ ở `_luu-tru/2026-11-18/`.

---

## Pipeline Garden US (5 bước + GATE + Feedback Loop)

**Hai lane, chung một pipeline.** Chỉ khác **nguồn đầu vào** và **3 bước rẽ nhánh**:

| | LANE A — BIG IDEA *(mặc định)* | LANE B — REMAKE |
|---|---|---|
| Nguồn Bước 0 | Ý đã qua TOPIC GATE (đường «Tìm chủ đề» ở trên) | `seed-brief.md` từ link user đưa hoặc 1 video trong báo cáo trend |
| Định dạng | 1 chủ đề, 8–10′ | **Theo ARCHETYPE của seed** (A1/A2/A5 listicle · A3 single-topic 8–10′ · A4 3 hồi) — xem router |
| Folder | `scripts/big-idea-[NNN]-[slug]/` | `scripts/remake-[NNN]-[slug]/` |
| Rẽ nhánh | — | R1.5 phân loại archetype → gói khai 8 biến cho [1.5] tải · [2.5] spine · Pha D · R7 · thước chấm |

```
── NHỊP TUẦN (task `garden-us-kiem-dinh-ky`, CN + T4 20:00 — thêm 22/11/2026) ──
Kiểm định kỳ → tools/kiem_dinh_ky.py → research/kiem-dinh-ky/latest.md (đo mọi video ≥7 ngày · retro-auto.md · CTR từ export Studio · chấm luật bằng số kênh)
            └─ CN: phiên tự viết retro.md 3 video mới nhất + Evidence log · đề xuất hiệu chỉnh luật CHỜ user duyệt (không tự sửa ACTIVE RULES)
            └─ User: thả export Studio (Analytics → Nội dung → Xuất) vào research/ mỗi tuần — nguồn CTR duy nhất
Dò trend → tools/do_trend.py → research/trend-us/<YYYYMMDD>/bao-cao-trend.md (0 credit; task trên chạy cả CN lẫn T4)
            └─ KHÔNG có GATE. Đây là nguồn ý + bằng chứng cổng ②, không phải lệnh sản xuất.

── NHỊP MỖI VIDEO ──
Bước 0-T → 🚦 PHỄU GỘP: bậc 0 `tools/kiem_de_tai.py kiem` (0 credit, CHẶN = dừng) → TOPIC GATE (mọi lane): ① kênh mình (franchise hit cũ) · ② trend ngách (`do_trend.py`: ĐA_KENH hoặc trend mùa ≥2 kênh) · ③ keyword US (≥3K/th hoặc +30%) → san-y-tuong Vòng A/B dùng lại dữ liệu · trần 60 credit/ý
            └─ danh mục 3 an toàn : 1 CÚ ĐÁNH LỚN (ý từ `tools/sinh_y.py`, cổng riêng ở topic-gate-en.md) · thắng: an toàn ≥1,5× · bứt ≥5× trung vị views_5d
            └─ CN (0 credit): du_bao.py dong-bo → dna_kenh.py do → du_bao.py dien → du_bao.py cong → kiem_de_tai.py lap → sinh_y.py
            └─ cần ≥2/3 · ghi block vào pipeline-state.md · chi tiết `references/topic-gate-en.md`
Bước 0   → LANE A: ý đã qua TOPIC GATE · LANE B: R1 tái thẩm seed (monthly_growth ≥5%) → lọc SEED PHẢI BỎ
            ├─ LANE B 🔴 R1.5 PHÂN LOẠI ARCHETYPE (A1..A6) — quyết định 8 biến cho mọi bước sau
            └─ LANE B 🔴 GATE 0: duyệt archetype + tài sản khoá (R2) + trục đã đổi (R3) + title
[1]      → mkt-youtube-outline          🔴 GATE: chọn title + approve outline
            ├─ title phủ MA TRẬN 5 GÓC: Mistake · Contrarian (bằng chứng <20s) · Lazy/High-Yield · Myth vs Science · Dollar-Value
            └─ ≥18′ single-topic → KHUNG 7 PHẦN (M1–M7 × 450–520 từ, cầu nối = vấn đề mới, không tóm tắt)
[1.5]    → mkt-youtube-deep-research    🔴 GATE: approve research brief
            └─ 🔀 LANE B: tải trọng + cách chạy theo GÓI (A1: 3 fact×mục, chạy lô 5 · A3: 5 câu + cơ chế trên cây nền mới) → sonnet
[2]      → mkt-hook-kallaway            🔴 GATE: chọn hook
            └─ 🔀 LANE B: ràng buộc CỦA GÓI (A1/A2/A5: ≥3 vòng lặp SỐ THỨ TỰ trong 50s · A3: gieo LỜI HỨA THỨ HAI <55s) — SSSQ không vi phạm
[2.5]    → Retention Spine (P2S)        🔴 GATE: duyệt Promise Decomposition + bảng Spine
            ├─ packaging-first: thiết kế giữ-chân TRƯỚC khi viết → đóng AVD ở bản vẽ, không vá ở audit
            ├─ LANE A ≥18′ single-topic → templates/retention-spine-single-topic-20min (Loop #1 · Loop #2 qua phút 4–6 · lời hứa cuối)
            └─ 🔀 LANE B: dùng spine_template CỦA GÓI — A1/A2/A4/A5 → retention-spine-listicle (kẻ theo MỤC,
               micro-bridge 100% ranh giới) · A3 → retention-spine-single-technique (LỜI HỨA THỨ HAI, trả sau payoff)
[3]      → youtube-garden-us            🔴 GATE: approve script (kèm Compliance Score · Hook /35 · sổ nhận/bác)
            ├─ ⚙️ `tools/gate.py scripts/<tập>` — orchestrator TỰ chạy sau MỖI lần script đổi (7 cổng máy)
            ├─ 🔍 [3R] PHẢN BIỆN KÉP ĐỘC LẬP ≥2 vòng (ĐƯỜNG NHANH 1 vòng cho đề tài không YMYL, vòng 1 sạch — từ 22/11/2026): Agy --sandbox + sub-agent Opus ngữ cảnh mới, thư mục cách ly
            │     (chỉ script có thẻ [C..] + research-brief + allowed-numbers + `templates/brief-phan-bien.template.md`)
            │     + vòng 1: R3 PHẢN BIỆN ĐÓNG GÓI (tiêu đề ↔ 60s đầu · thumbnail) `templates/brief-phan-bien-dong-goi.template.md`
            │     · lỗi CHẶN/NÊN SỬA bắt buộc Before → After (L25) · header script khai FIRST_STEP / ENDING_FROM / COMMENT_Q / LOOP (L22–L24, L27: loop ≤180 s giữa hai mốc) · bản After của người phản biện (kể cả góp ý ngoài) phải qua lint + Claim Ledger trước khi nhận
            │     → lọc nhận/bác (`phan-bien-vN.md`) → 1 người biên tập sửa đúng danh sách → vòng 2 trên vùng đã sửa
            ├─ viết BÁM bảng Spine (Pha C) → Pha D verify cơ học (L3/L4/L5) trước audit
            ├─ ≥18′ → VIẾT THEO 4 LÔ (Hook+M1+M2 · M3+M4 · M5+M6 · M7+Kết), tự kiểm + dừng mềm mỗi lô (playbook §Pha C′)
            ├─ 🔀 LANE B: Pha D thêm phép đếm CỦA GÓI (A1: bridges ≥ items−1 · years/money ≥ items×0.8 · A3: lời hứa 2 gieo <55s + trả sau payoff)
            ├─ 🔀 LANE B: Pha D chạy originality_check.py so với seed-transcript (≤1 câu trùng · ≤2% 6-gram · --allow tài sản khoá)
            └─ audit ĐỌC references/lessons-learned.md (ACTIVE RULES) + 🔀 LANE B: R7-CORE (9 điểm chung) + R7-DELTA của gói
[4]      → SEO EN (`en-US` duy nhất)    ✅ Tự động, không gate *(đã TẮT 4b/4c dịch ES từ 26/11/2026 — L28 cấm Localization ngoài en-US)*
[5]      → prediction.md                ✍️ tại GATE Script: ghi "cược" (Phase 2)
[6]      → retro.md                     🔁 7–14 ngày sau publish: diff số thật → lessons-learned.md
            └─ 🔀 LANE B: chấm bằng views_5d vs median_5d_views (285) + tổng giờ xem. ⛔ KHÔNG chấm bằng AVD.
```

> **LANE REMAKE — 2 file, đọc theo thứ tự:**
> 1. 🔴 `references/remake-archetypes-en.md` — **ROUTER**. §1 nguyên lý bất biến (tài sản đã-trả-tiền ·
>    luật MỘT TRỤC · nợ giao hàng) · §0 **đường vào** (báo cáo trend · link video · **dán mẫu kịch bản → bắt buộc truy ngược nguồn**) · §2 bộ phân loại 5 câu → chốt gói **A1…A10** · §3 gói (mỗi gói khai 8 biến:
>    tài sản khoá · trục đổi · bộ xương · nhịp · spine template · tải [1.5] · Pha D thêm · R7 delta) ·
>    §4 **SEED PHẢI BỎ** (X1/X3/X4/X5/L9 — không override được). Gói ✅ có số thật: A1 · A2 · A6. Gói 🟡 suy ra (A3–A5, A7–A10) → bắt buộc ghi TEST KHUÔN vào prediction.
> 2. `references/remake-playbook-en.md` — **bằng chứng + gói A1**: ~~R0 radar~~ (cất 18/11 — tìm seed bằng `do_trend.py`; R1 vẫn chấm
>    bằng `monthly_growth_pct` ≥5%) · R0-B port khuôn · R5 thumbnail *(FACELESS, ảnh mới)* · R6 người kể ·
>    R7-CORE 9 điểm chung + R7-DELTA theo gói · đọc 3 đường cong sau khi đăng.
>
> Template: `seed-brief` *(v2 archetype-aware)* · `retention-spine-listicle` · `retention-spine-single-technique` · `retention-spine-single-topic-20min` *(Lane A ≥18′)*.
> ⚠️ **Đừng mặc định coi mọi seed là listicle di sản (A1)** — `remake-001` (khẩn cấp theo mùa) và `remake-002`
> (1 kỹ thuật đơn) đều phải override thủ công vì thiếu bước phân loại. R1.5 sinh ra để trám chỗ đó.
> ⚠️ Remake là chiến lược **volume**: tỷ lệ trúng ~1/50, title stem dùng lần 2 suy giảm 8–118×.

> **Packaging-first / Retention Spine (GATE 2.5):** quy trình + template Spine + Pha D verify ở
> `references/packaging-retention-playbook-en.md`. Mục tiêu: kéo AVD 25.6%→40% bằng cách chốt lời hứa
> (Promise Decomposition) + dựng bộ xương giữ-chân theo drop zone kênh (giây 40–55, phút 4–6) TRƯỚC khi
> viết script. youtube-garden-us viết bám Spine; audit Bước 3 thành kiểm định cuối, không còn vá leak muộn.
>
> **Feedback Loop (Phase 2):** quy trình đầy đủ ở `references/feedback-loop.md`. Vòng lặp
> script→đăng→retention→audit giúp mỗi video học từ video trước. Template ở `templates/`.
>
> **Phase 4 — OAuth Analytics tự động** (`tools/yt_analytics.py`, chỉ đọc):
> - `python tools/yt_analytics.py sync` → refresh baseline 28d + top videos → ghi đè block DATA TRUTH trong `channel-truth.md` + `references/yt-analytics-latest.json`.
> - `python tools/yt_analytics.py retro <videoId>` → AVD + retention curve + biggest-drop second cho 1 video → block ACTUAL cho `retro.md`.
> - `python tools/yt_analytics.py health [tuần]` → self-baseline: xu hướng AVD theo tuần · traffic mix 28d vs 28d trước · outlier ratio · duration band · view 5 ngày đầu → `references/channel-health-latest.json`. Tự tách Shorts + video đã xoá/private khỏi thống kê long-form. Đọc bởi `yt-channel-health-audit`.
> - Tự refresh token. **CTR** vẫn nhập tay (API không expose). Credentials ở `.secrets/` (gitignored).
>
> **Phase 3 — Tự động hoá + Token routing:**
> - **Lịch tự động (từ 22/11/2026):** task `garden-us-kiem-dinh-ky` (CN + T4 20:00) là lần chạy định kỳ DUY NHẤT — `tools/kiem_dinh_ky.py` (health + du_bao + retention + CTR Studio + chấm luật) · dò trend · CN viết retro + đề xuất hiệu chỉnh chờ duyệt. Task cũ `garden-us-60k-weekly-benchmark` đã TẮT từ 09/06/2026 (Notion + tool benchmark cũ) — không bật lại.
> - **Refresh thủ công bất kỳ lúc nào:** `tools/run-sync.cmd` (fetch độc lập → channel-truth + toast) hoặc `python tools/yt_analytics.py sync`.
> - **CTR:** API không có → điền `manual_ctr_pct` trong `channel-stats-...json` để channel-truth hiện số; nếu không, dòng CTR tự đóng dấu `[NHẬP TAY — tuần YYYY-Www]`.
> - **Model routing** (`channel.config.json` → `model_routing`): mặc định **Haiku**; **Sonnet** chỉ ở hook / script / script_audit (bước quyết định CTR/AVD/compliance). Orchestrator đọc map này khi chọn model/subagent. High-stakes → bump lên Opus thủ công.
> - **Đa kênh / onboard kênh mới:** xem `tools/README-multi-channel.md` (tools đã config-driven; chỉ token OAuth + scheduled-task là per-kênh).

Nguồn Big Ideas mặc định: `https://lunar-headlight-f5a.notion.site/Big-idea-377d73f564198028a6c8dbd7445d461f`

---

## Output Folder

Mọi file output lưu tại (folder MỚI: `[NNN]` zero-pad 3 chữ số — `5`→`005`, `89`→`089`).
**LANE A** → `scripts\big-idea-[NNN]-[slug]\` · **LANE B** → `scripts\remake-[NNN]-[slug]\`
*(tách folder để retro thống kê được 2 lane riêng — đây là điều kiện để sau 6–8 video biết lane nào ăn)*
```
scripts\big-idea-[NNN]-[slug]\   ← hoặc remake-[NNN]-[slug]\
├── pipeline-state.md  (bảng theo dõi các bước ✅/⬜)
├── seed-brief.md      (CHỈ LANE B — R1 tái thẩm + R2 giải phẫu + §2B mổ xẻ seed + R3 vật chủ; 🔴 GATE 0)
├── seed-transcript.txt (CHỈ LANE B / mẫu dán — transcript seed có timestamp; Pha D so trùng câu chữ)
├── outline.md
├── research-brief.md
├── retention-spine.md (GATE 2.5 — Promise Decomposition + bảng Spine, duyệt TRƯỚC khi viết)
├── script.md          (EN — 10-12 phút / 1.650–2.000 từ từ 2026-11-22; xem video_length trong channel.config.json)
├── seo-en.md          (CHỈ en-US — đã TẮT script-es.md / seo-es.md từ 26/11/2026 để chống lệch tệp, L28)
├── prediction.md      (Phase 2 — ghi tại GATE Script, từ templates/prediction.template.md)
└── retro.md           (Phase 2 — điền 7–14 ngày sau publish, từ templates/retro.template.md)
```

---

## Channel Config

| Biến | Giá trị |
|------|---------|
| `CHANNEL_NAME` | Garden US |
| `WORKSPACE_PATH` | `D:\0002-Team A Nam` |
| `YOUTUBE_CHANNEL_SLUG` | `garden-us-60k` |
| `NOTION_BIG_IDEAS_URL` | `https://lunar-headlight-f5a.notion.site/Big-idea-377d73f564198028a6c8dbd7445d461f` |
| `NOTION_BENCHMARK_DB` | `a0386a02-e6fe-4a24-9df1-468b432e94db` |
| `SCRIPT_LANGUAGE` | `English` |
| `TRANSLATE_ES` | `false` *(tắt từ 26/11/2026 — L28: chỉ xuất bản `en-US`, cấm Localization ngoài Mỹ)* |
| `TARGET_VIEWER` | American home gardeners **35–60+** (lõi hiện tại 60–80), **Smart TV (đích ≥45%) + Mobile** — cập nhật 26/11/2026; câu chữ theo `brand-voice-dna.md` § Ngôn ngữ cho khán giả 35–60+ |
| `BRAND_VOICE_FILE` | `references/channel-truth.md` (gộp voice + số liệu thật; deep-dive tone ở `brand-voice-dna.md`) |
| `KEYWORD_STRATEGY_FILE` | `references/title-keyword-strategy-en.md` (Title Hybrid: formula + 3-tier keyword + GAP_LIST + HYBRID_RULE) → bật Title C ở `mkt-youtube-outline` |

> ⚙️ **Nguồn sự thật là `channel.config.json` ở gốc workspace.** Bảng trên chỉ là bản mirror cho người đọc. Skill đọc JSON trước, fallback bảng này nếu JSON không có. Sửa config → sửa trong `channel.config.json`.

**Khi mở workspace nào, skill tự động dùng config của workspace đó.**

---

## Nguyên tắc cốt lõi

- **Local-first** — không ghi lên Notion trong quá trình viết
- **Zero hallucination** — thiếu data → `[NEED DATA: ...]`, không bịa
- **Compliance thắng** khi xung đột với brand voice
- **Phản biện kép là bắt buộc** — self-audit không tính; ≥2 vòng, 2 hãng, thư mục cách ly; không viết lại cả bài sau khi người phản biện đã đọc. **Đường nhanh** (user duyệt 22/11/2026): đề tài không YMYL, không cú đánh lớn, vòng 1 0 lỗi CHẶN dữ kiện/an toàn + Risk ≥9 → bỏ vòng 2, orchestrator đối chiếu vùng đã sửa với Claim Ledger. Mục tiêu nhịp ≥4 video / 14 ngày
- **Vệ sinh luật** (user duyệt 22/11/2026): trần 20 dòng ACTIVE trong `lessons-learned.md`; luật mới không có số của kênh vào 🧪 TESTING; 60 ngày chưa đo được → phiên kiểm định đề xuất hạ
- **Tỷ lệ lane** (user duyệt 22/11/2026, TEST 6 video): ~1/3 video là **Lane B remake** (cứ 3 video thì 1 remake) — `kiem_dinh_ky.py` chấm lại sau 6 video
- **Phần tiếp theo catalog** (C2, user duyệt 22/11/2026, TEST 8 video): ~1/4 video là phần tiếp theo trực tiếp của 1 video top-5 đang kéo view (cùng chủ thể, góc mới, end screen + thẻ 2 chiều); ghi `PHẦN TIẾP THEO: <videoId gốc>` vào pipeline-state.md — chi tiết `references/topic-gate-en.md`
- **Giọng dân dã** (L26, user duyệt 22/11/2026): lời đọc như người làm vườn Trung Tây chân chất nói chuyện, không giọng tài liệu, không cao bồi; `script_lint.py` cổng E7 + sổ `references/giong-dan-da.tsv` chặn (chỉ áp kịch bản mới)
- **User sửa cách nói → ghi ngay** 1 dòng vào `references/cach-noi-da-chot.tsv`; `script_lint.py` chặn tái phạm
- **Hard GATE** — dừng chờ user confirm ở mỗi bước, không tự nhảy
- **TOPIC GATE ≥2/3** — không "thấy video nổ là làm theo": chủ đề phải đạt ≥2/3 tín hiệu (kênh mình · outlier ngách · keyword US) trước outline (`references/topic-gate-en.md`)
- **KEYWORD-FIRST** — trước khi chốt title: đo keyword vidIQ (US, growth vs nền 30d) + soi outlier cùng chủ đề; keyword chính exact-phrase ở ~25 ký tự đầu khi how-to/theo mùa/nhu cầu +30% (`references/title-keyword-strategy-en.md` § KEYWORD-FIRST GATE · lesson L10)
- **Narrator = educator**, không phải người trồng có kinh nghiệm cá nhân (xem Narrator Integrity Rules trong `references/brand-voice-dna.md`)
- **Khóa tệp Mỹ & Thumbnail ảnh sạch ghép chữ tay (L28, L29 — user duyệt 26/11/2026):** chỉ xuất bản `en-US` (`translate_es: false`, cấm bật Auto-dubbing/Localization ngôn ngữ ngoài Mỹ); thumbnail tách **ảnh nền sạch không chữ** (`no text`) + ghép chữ 2 tầng & badge ❌/✅ bằng Canva/Photoshop hoặc Pillow (`tools/garden_thumb_real.py`) để sắc nét trên cả **Smart TV** lẫn **mobile**.
- **Auto Trend Studio (Radar Bước 0):** dự án `Kênh làm vườn US` (`kenh-lam-vuon-us`) bổ trợ song song `do_trend.py` ở Bước 0 & 1.5 (quét video mới, từ khóa US, kho bình luận thật US cho L13/Q&A, quản trị Model Link `Frugal Solutions`).
