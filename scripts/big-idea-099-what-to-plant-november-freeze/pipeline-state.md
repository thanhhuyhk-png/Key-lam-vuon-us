# Pipeline State — big-idea-099-what-to-plant-november-freeze

> Auto-tracked. ✅ xong · ⬜ chưa làm. Cập nhật ở mỗi GATE.
> Last sync: 2026-11-19

**Lane:** A — Big Idea (nguồn: báo cáo `do_trend.py` 18/11, chủ thể «rau/cây chịu đông trước tháng 12»; không có Notion #) · **Độ dài:** 10–12′
**Ngày đăng mục tiêu:** ≤ 28/11/2026 (trend 10 ngày từ báo cáo 18/11) — ⚠️ chưa có ngày chốt; cần user xác nhận có kịp không
HẠNG: AN TOÀN · nhãn TEST (2/3 thiếu ①, đổi MỘT trục: «theo vùng USDA» → «theo ngưỡng nhiệt thấp nhất»)

| # | Bước | Skill | Output | Trạng thái |
|---|------|-------|--------|-----------|
| 0-T | 🚦 Topic Gate (≥2/3) | references/topic-gate-en.md | block bên dưới | ✅ 19/11: 2/3 (② ✅ · ③ ✅ mỏng · ① ❌) — GO có điều kiện · user chọn góc 1 «ngưỡng nhiệt» |
| 1 | Outline | mkt-youtube-outline | outline.md | ✅ user chọn Title A 19/11: «What to Plant in November: 6 Crops That Shrug Off 28°F» (54 ký tự) · PROMISE_OK «Plant» (nói rõ giới hạn đất đóng băng ở M4) + «Shrug Off 28°F» (chỉ nhóm hardy có nguồn; kiểm lại ở 1.5) · CTR vidIQ bỏ qua (tool `vidiq_score_title` không tồn tại) |
| 1.5 | Deep Research | garden-deep-researcher | research-brief.md | ✅ user duyệt 19/11 («Duyệt, sang hook») · đủ ~10–10,5′ (thiếu ~1′ ở M4) · title đổi «5 Crops» · MSU/UGA bị chặn 403, không dùng · chỉ nguồn Pass2=Y được vào script · orchestrator CHƯA tự kiểm lại claim |
| 2 | Hook | mkt-hook-kallaway | hook.md | ✅ user chọn **Hook A** 19/11 · Data/Statement «Twenty-eight degrees…» ~0:25 · loop «2 cây bị loại, 1 cây cần lạnh» mở ~0:15 → đóng M3 · lint sạch trừ L16 (khai ACTION_TIP ở script) · so đối thủ CHƯA chạy (chưa có transcript trong competitor-transcripts/) |
| 2.5 | Retention Spine | playbook P2S | retention-spine.md | ✅ user duyệt 19/11 («Duyệt, viết script») · ~1.790 từ ≈ 10:51 · 3 loop (#1 0:15→6:30 · #2 3:40→4:50 · #3 7:40→9:00) · Editorial Signature = bảng số phiếu 7 cây (4:15–5:00) + cộng/trừ vải phủ · ⚠️ M4 mỏng, nhiều claim Pass2=N cần mở lại ở [3] |
| 3 | Script EN | youtube-garden-us | script.md | ✅ user duyệt 19/11 («Duyệt script») sau 3R 2 vòng · 1.837 từ ≈ 11,1′ · gate.py 7/7 PASS · Compliance Risk 9/10 (R2 vòng 2; mục 8 đã sửa chưa chấm lại) · 4 lỗi CHẶN của Agy v2 đã sửa, chưa ai đọc lại |
| 3R | Phản biện kép ≥2 vòng | Agy + Opus | phan-bien-v1/v2.md | ⏳ 19/11: V1 xong — R1 Agy ĐẠT CÓ SỬA (6 CHẶN, Hook 26/35) · R2 Opus ĐẠT CÓ SỬA (3 CHẶN, Hook 29/35, Risk 8/10) · nhận 24 / bác 6 (3 loại báo nhầm do chỉ đọc dòng tóm tắt ledger) · sửa theo D1–D24 · V2: Agy ĐẠT CÓ SỬA (4 CHẶN, Hook 30/35) · Opus ĐẠT CÓ SỬA (0 CHẶN, **Hook 33/35**, **Risk 9/10 PUBLISH**) · nhận 17 / không áp dụng 3 · đã sửa E1–E17, gate.py 7/7 PASS (1.837 từ ≈ 11,1′) · ⚠️ 4 lỗi Agy xếp CHẶN đã sửa nhưng chưa ai đọc lại (không chạy vòng 3 tự động) · mục 8 hedging đã sửa, chưa chấm lại Risk |
| 3.5 | Prediction | templates/prediction.template.md | prediction.md | ✅ 19/11: P25/P50/P75 = 300/550/1.100 views_5d · P(≥896)≈0,25 · P(≥2.982)≈0,04 · 6 TEST · target đăng ≤ 28/11 (CHƯA chốt ngày) |
| 4a | SEO EN | garden-seo | seo-en.md | ✅ 19/11: orchestrator viết lại (bản agent loại: quá lời «survive 28°F», thiếu chapters, xin LIKE/SUBSCRIBE) · 10 chapters @165 wpm (chỉnh theo voice.srt) · 27 nguồn có URL từ ledger · 12 tags · 0 hashtag · thumbnail-prompts.md (A `STILL GREEN`/`AT 26°F` ⭐ · B `2 MISSING`/`FROM THE LIST`) — **A đã render 19/11 qua ChatGPT (Codex CLI `image_generation`) → `thumbnail-a.png` 1672×941**; chữ đúng, lá xanh có sương; ⚠️ nhiệt kế đọc ~30°F (thang 0–120), không đúng 26°F — cân nhắc bỏ nhiệt kế hoặc sửa; B chưa render |
| 4b | Translate ES | garden-translate-es | script-es.md | ⬜ không yêu cầu |
| 4c | SEO ES | garden-seo | seo-es.md | ⬜ không yêu cầu |
| 6 | Retro | yt_analytics.py retro | retro.md | ⬜ (7–14 ngày sau publish) |

**Title đã chốt (19/11, sửa sau [1.5]):** What to Plant in November: 5 Crops That Shrug Off 28°F (user chọn phương án 1; bản «6 Crops» bị bác: cà rốt 1/5 và tỏi 1/2 nguồn đạt ≤28°F; «20°F» không nguồn) · Thumbnail concept: STILL GREEN
**Góc đã chọn (19/11):** chọn rau theo ngưỡng nhiệt chịu rét, không theo vùng USDA
**Bước kế tiếp:** [1.5] `garden-deep-researcher` — chốt cây thứ 6, nguồn A/B cho ngưỡng từng cây, nhiệt độ đất gieo tỏi/cải bó xôi, số độ tăng khi che phủ; mở lại từng trang Purdue/NC State/UGA/MSU/OSU/UMD đã thấy sơ bộ. Chạy sonnet (haiku không đủ cho đối chiếu nguồn bất đồng).
**⚠️ Cảnh báo:** số «20°F» và «6 vegetables» là chỗ giữ chỗ, phải lấy từ nguồn hạng A/B ở [1.5], không có thì `[NEED DATA]` · «Survive» dễ overclaim → kiểm PROMISE_OK ở outline · kiem_de_tai: CẢNH BÁO (giống 0,75 «Don't Plant These 15 Vegetables in the Ground», 355 view; chủ thể có trong lời đọc 098 và 039 mỗi bài 6 lần) · không clone «by USDA zone» của Gardenomics · lịch: 098 đang hướng 10–20/12, bài này có hạn trend sớm hơn → xếp lại thứ tự đăng.

## 🚦 TOPIC GATE — 2/3 thiếu ① → GO có điều kiện (2026-11-19)
| Tín hiệu | Đạt? | Bằng chứng |
|---|---|---|
| ① Kênh mình | ❌ | Hit kênh là cây trong nhà/nhân giống: Aloe 53K · Bơ từ hạt 37K · giâm cành 12,7K · Lemon 12K · 7 cây trồng trong nước 7,3K (trung vị 571). Rau ngoài trời theo mùa: «16 Things Grandma Always Planted in October» 737 view (~1,3×); «7 Cheap Root Cellar Ideas…» 6.446 (cất rau, khác chủ thể). Chưa có franchise «trồng rau trước đông» |
| ② Trend ngách | ✅ | `do_trend.py` 18/11, ĐA_KENH: Gardenomics «9 Vegetables to Plant Before December Arrives (By USDA Zone!)» ×10,24 · Plant Explainer «15 Container Vegetables That Survive Winter in Small Spaces» ×2,59 · Gathering Basket «Elderly Homesteader Plants Cold Frame For Winter Vegetables» ×2,2. Hệ số [ƯỚC], chưa có tăng/ngày [ĐO] |
| ③ Keyword US | ✅ mỏng | «what to plant in november» 4.167/th, cạnh tranh 59 (≥3K/th, không có +30%) · «november gardening» 9.502/th · «fall vegetable garden» 4.622/th · ⛔ «vegetables to plant before december» < 750/th |
| ⓑ Bão hoà góc | 🟡 | «vegetable» 3/8 nóng (ổn), «winter» 3/26 (nhiều kênh làm, ít bản nóng) → đã đổi góc sang ngưỡng nhiệt |
| kiem_de_tai.py | CẢNH BÁO | xem mục cảnh báo phía trên |
| ⛔ Không bám | | X1–X5, L9 (không nhãn tuổi) · không bám đề tài Amish của Model Link |
| Chi phí vidIQ | | 10 credit (key …WBG: 30 → 20), 2 lệnh `vidiq_keyword_research` US · bản gốc: `research/trend-us/20261118/topic-gate-rau-chiu-dong.md` |
