# Pipeline State — big-idea-062-sunny-window-winter-veggies

> Auto-tracked. ✅ xong · ⬜ chưa làm. Cập nhật ở mỗi GATE.
> Last sync: 2026-10-17

**Lane:** A — BIG IDEA · **Nguồn:** `/san-y-tuong` 17/10 (`research/phieu-kiem-dinh-winter-veg-indoors-2026-10-17.md`) — KHÔNG phải Notion Big Idea.
**Chủ đề:** Rau trồng trong nhà mùa đông — 5 loại ra rau trên cửa sổ nắng, 3 loại cần thêm đèn.
> 🎞️ **HÌNH & DỰNG (17/10, theo yêu cầu "cắt <4s/cảnh, như kênh Quân sự"; kiểu hình đầy khung, chỉ nguồn giấy phép tự do + AI, dựng bằng script ghi CapCut):** `footage/` gồm 155 clip Pexels (1,3 GB, `pexels/manifest.json` có tác giả/URL/giấy phép), 77 ảnh Pexels (`photos/`), 14 ảnh AI G-Labs (`ai/`, 12 mã + 2 biến thể), 19 thẻ đồ họa (`gfx/`). `shotlist.csv` = **345 shot** (V 188 · ảnh P 89 · đồ họa G 48 · AI A 20), phút đầu 28 shot avg 2,2s, 1:00–3:00 avg 3,0s, phần còn lại avg 3,35s, không shot stock ≥4s, hình thật ~93%. Draft CapCut **`G062_auto`** đã ghi (345 shot + 6 bộ đếm + 131 sự kiện chữ A/B/nguồn + 20 nhãn ILLUSTRATION + voice 18:31); chưa có SFX/nhạc; chưa xem trong CapCut. Chưa tạo Veo; chưa dùng Unsplash. Công cụ: `tools/garden_shotlist.py`, `garden_gfx.py`, `garden_build_capcut.py`, `pexels_collect.py`, `pexels_photos_collect.py`, `glabs_batch.py`. Bản sao lưu CapCut: `root_meta_info.json.bak_g062_orig`.
> ✅ **VOICE CHẠY XONG (17/10):** `voice/voice.mp3` (17,8 MB) + `voice/voice.srt` (449 cue). **Thời lượng thật 18:31 (1.111 giây)**, 3.064 từ trong SRT ≈ 165,5 từ/phút tính cả dấu ngắt (182,8 lúc đang nói). **Credit đã dùng: 26.091** (+1.040 cho bản thử hook = 27.131). SRT khớp script 98,8% (chênh lệch chủ yếu do dấu nháy); hai chỗ nghe thử: **5:27 "Maryland" bị phiên âm thành "Marilyn"** và **9:20 "Lizzano" thành "Lozano"** — nghe lại, nếu sai thì tạo lại đoạn đó (đổi chính tả: "Mary-land" / "Lee-zah-no"). `seo-en.md` đã cập nhật chapters theo SRT; `shot-plan.md` dùng mốc cũ @175 wpm lệch khoảng +40–60 giây về cuối, đối chiếu lại bằng `voice.srt`.
> 🎙️ **VOICE (17/10):** giọng clone **"Key gardent" = `clone_2697441`** (ai33.pro, MiniMax speech-02-hd), speed 1,0. Test đoạn hook (703 ký tự, 1.040 credit): 116 từ / 41,9 giây ≈ 166 từ/phút tính cả dấu ngắt (≈179 lúc đang nói); dấu ngắt `<#x#>` hoạt động, không bị đọc. File: `voice/test-hook.mp3` + `.srt`. Toàn bài: `voice/voice-text.txt` (chưa chạy — chờ user đồng ý chi phí).
> 🔊 **VOICE CALIBRATION (17/10, `Voice Mẫu.srt`):** 68 từ / 23,3 giây ≈ **175 từ/phút** (mẫu ngắn, 9 cue; trong từng cue ≈189 wpm). Thay cho giả định 140–150. Đổi giây: **word ÷ 2,9**. Với 175 wpm: 2.900–3.100 từ ≈ **16,6–17,7 phút**; muốn 20–22′ cần 3.500–3.850 từ (chất liệu có nguồn không đủ, không độn) hoặc giảm tốc độ voice xuống ~150 wpm (≈19–21′ cho cùng số từ) + nhịp nghỉ/nhạc ~1–2′. **Quyết ở GATE [3].** Cần mẫu dài ≥2 phút để xác nhận.
> ✅ **CHỐT 17/10 (user): chấp nhận ~17–18 phút ở voice hiện tại (3.045 từ ≈ 17,3′ @175 wpm), KHÔNG độn.** Mục tiêu 20–22′ bên dưới đã bị thay thế. Kết quả đo bằng views_5d vs 523 + giờ xem/lượt.
> ~~🎯 TARGET KỊCH BẢN: 20–22 PHÚT~~ (cũ) 🎯 **TARGET KỊCH BẢN: 20–22 PHÚT** (user chốt 17/10/2026 sau research; trước đó 20–25′) @140wpm ≈ **2,900–3,100 từ**. **Title CHỐT:** `Grow Vegetables Indoors This Winter (5 Easy, 2 Need a Light)` (đổi từ "3 Need" vì thiếu nguồn mục 3). Radish ở nhóm 1, nói rõ nguồn không nêu mức sáng. Áp cho mọi bước sau (research, hook, spine, script, SEO chapters). Nếu chất liệu có nguồn không đủ → BÁO USER trước khi viết, không độn.
> ⚠️ **17/10/2026 — LONG-FORM (20–25′).** Outline v2 ~22′ @140wpm. **OVERRIDE video_length** chỉ cho video này. TEST (L7; băng 20–40′ n=2): đo bằng views_5d vs 523 + giờ xem/lượt, ⛔ không chấm bằng AVD%. Chất liệu 4 nguồn hiện chỉ đủ ~10–12′ → [1.5] phải mở rộng các khối `[CẦN MỞ RỘNG]`; nếu chỉ đủ ~14–16′ thì báo user trước khi viết.

**Hạn đăng:** càng sớm càng tốt trong tháng 10 (3 hit cùng chủ đề năm ngoái đều đăng 20/10–22/12/2025).
**Nhãn:** thăm dò (góc mới) · GO-TEST — ghi `TEST` trong prediction.md.

## 🚦 TOPIC GATE — 2/3 thiếu ① → GO-TEST (2026-10-17)
| Tín hiệu | Đạt? | Bằng chứng |
|---|---|---|
| ① Kênh mình | ❌ | Chưa có hit cùng cây/vật. Gần nhất về khung "trong nhà, lười": *7 Indoor Plants That Thrive in JUST Water* 22,880. Chưa có số liệu cho 024 (thủy canh) và 025 (tái sinh rau). |
| ② Outlier ngách | ✅ | Sunnyside Soil *9 Vegetables You Can Actually Grow Indoors This Winter* 536K / 57.9K sub (12/2025) · Backyard Crops *No Garden Needed! Grow These 7 Winter Veggies Indoors* 281K / 27K (11/2025) · SereneGreen *Grow These 7 Winter Veggies INDOORS* 148K / 64.2K (10/2025). Pattern: "N winter veggies indoors" + "no greenhouse/quick harvest". ⚠️ Cả 3 đều quá 6 tháng tuổi. |
| ③ Keyword US | ✅ yếu | "grow vegetables indoors" 4,472/th · "indoor vegetable garden" 3,641 · "growing tomatoes indoors" 4,827 · "indoor gardening" 19,110 (+118% vs nền 30d, cụm rộng) · cụm đúng ý định "grow vegetables indoors in winter" <750 · ⚠️ `countryVolume` null → chưa chắc thuần US; growth null cho cụm chính. |
| Chặn cứng | sạch | Rau quen thuộc với người Mỹ, không khung sợ/độc. Lưu ý vi sinh nếu nhắc microgreens/giá đỗ → [YMYL] nhẹ. |
| ⓑ Bão hoà góc | không | 3 video cùng khung đều thắng (không chỉ trung bình). Mẫu 67 video: 3 kênh/90 ngày, OM trung vị giảm 33% (nhưng 90 ngày gần là trái mùa). Góc "mọc được vs cần đèn" chưa thấy ai dùng. |
| ⓒ Chất liệu | 6/5 (đã mở trang) | 1. Rau lá và thảo mộc cần 6–8 giờ sáng mạnh/ngày; cửa sổ hướng nam tốt (UIUC Ext., 2017) · 2. Đèn bổ sung 14–16 giờ/ngày, 6–12 inch trên cây, ~2 giờ đèn cho mỗi giờ sáng tự nhiên (UIUC) · 3. Cà chua/ớt quả nhỏ trồng được trong nhà nhưng cần đèn bổ sung mùa đông, ~10 tuần thu hoạch, coi chừng rệp/bọ phấn (UNH Ext. Ch.10, năm chưa rõ) · 4. Microgreens 7–21 ngày, baby greens 21–40 ngày, trưởng thành 40–60 ngày; xà lách/arugula/cải chịu thiếu sáng khá tốt (UMD Ext.) · 5. Cửa sổ chỉ đủ cho hạt cần sáng để nảy mầm; cây con vươn dài khi thiếu sáng; đèn 4–6 inch (UNH Ext. Q&A) · 6. Cà chua cần ~6 giờ tối để đậu quả, ớt thì không (UNH Q&A). |
| Trục đổi so với outlier | cơ chế/ phạm vi | Outlier: "N rau làm được trong nhà". Mình: phân loại theo ánh sáng — loại nào mọc trên cửa sổ nắng, loại nào cần thêm đèn (có số giờ từ extension). |

**Hiệu chỉnh trung thực:**
1. ① ❌ và ③ chỉ đạt ở cụm rộng → kỳ vọng quanh median 523, sống nhờ Browse. 3 video hit cùng khung là bằng chứng thị trường chứ không phải bằng chứng cho khán giả của kênh mình.
2. UMD nói cửa sổ nắng "có thể đủ trong một số trường hợp" → ⛔ không khẳng định "cửa sổ không bao giờ đủ".
3. Nguồn UIUC 2017 và UNH Ch.10 cũ; chưa tìm được nguồn extension thứ hai về cà chua/ớt trong nhà → hedge ở [1.5].
4. ⛔ Tránh khung đối thủ: "Actually Grow", "No Greenhouse Needed", "7 Winter Veggies INDOORS", "Quick Harvest".

## 3 ứng viên tiêu đề (vidIQ score_title, chưa duyệt)
| # | Tiêu đề | Ký tự | Điểm |
|---|---|---|---|
| A | 5 Veggies for a Sunny Window This Winter (+3 That Need a Light) | 63 | **89** |
| B | Sunny Window Winter Garden: 5 Veggies That Grow, 3 Need a Light | 63 | 87 |
| C | Grow Veggies Indoors This Winter: What Works on a Sunny Window | 62 | 86 |
> KEYWORD-FIRST: ③ đạt yếu (cụm "grow vegetables indoors" 4,472, chưa xác nhận US). Chỉ C mở bằng cụm gần keyword; cần đổi "Veggies" thành "Vegetables" mới khớp exact phrase. Quyết định ở GATE [1].

| # | Bước | Skill | Output | Trạng thái |
|---|------|-------|--------|-----------|
| 0-T | 🚦 Topic Gate (≥2/3 tín hiệu) | references/topic-gate-en.md | pipeline-state.md | ✅ 2/3 thiếu ① → GO-TEST (17/10) |
| 1 | Outline | mkt-youtube-outline | outline.md | ✅ v2 LONG-FORM ~22′ · Title C chốt (17/10): Grow Vegetables Indoors This Winter (5 Easy, 3 Need a Light) · vidIQ 85 · swap giờ 48 sang A nếu CTR <3.5% |
| 1.5 | Deep Research | mkt-youtube-deep-research | research-brief.md | ✅ 17/10 (agent v2 + Pass2 orchestrator) — 23 claim đã kiểm lại · chất liệu ≈2.900–3.600 từ · mục 3 bỏ · user duyệt |
| 2 | Hook | mkt-hook-kallaway | (trong script) | ✅ V2 Proof-first chọn 17/10 (~118 từ; proof giây ~6; loop "dấu hiệu lặng lẽ" giây ~48) |
| 2.5 | Retention Spine | playbook P2S (Pha A+B) | retention-spine.md | 🟡 nháp xong 17/10 — chờ GATE 2.5 (3 loop · 7 re-hook · Editorial Signature = bảng Window or Lamp? + 3 chỗ nguồn bất đồng · ≈2.940 từ ≈21′) |
| 3 | Script EN | youtube-garden-us | script.md + shot-plan.md | ✅ user duyệt 17/10 (chấp nhận ~17–18′) — xong 17/10 — 3.045 từ ≈ **17,3′ @175wpm** (≈20,2′ @150) · Pha D ✅ · claim_check ✅ · originality ✅ (max 0) · Triple F ✅ (chọn lọc) · compliance **10/10** (vòng 2) — chờ GATE; quyết định độ dài ở bên dưới |
| 3.5 | Prediction | templates/prediction.template.md | prediction.md | ✅ 17/10 (ghi TEST: độ dài, khuôn, hình AI/Veo) |
| 4a | SEO EN | mkt-yt-seo-description | seo-en.md | ✅ 17/10 (agent garden-seo + tôi sửa lại cho gọn và đúng script) — chapters là mốc ước tính @175wpm, chỉnh lại theo voice thật; dòng AI Disclosure đã đổi cho khớp thực tế |
| 4b | Translate ES | mkt-yt-translate-es | script-es.md | ⬜ |
| 4c | SEO ES | mkt-yt-seo-description | seo-es.md | ⬜ |
| 5 | Thumbnail | garden-us-thumbnail | thumbnail-prompts.md + thumbnail-a.jpg + thumbnail-b.jpg | ✅ render 17/10 qua G-Labs (nano_banana_pro): A `LEGGY? / 6-8 HOURS` · B `NO FRUIT? / 6 HOURS DARK`; chữ đúng cả hai; **user chốt 17/10: dùng nguyên cả A và B cho Test & Compare** (ghi trong prediction.md, kèm lưu ý) |
| 6 | Retro | yt_analytics.py retro | retro.md | ⬜ (7–14 ngày sau publish) |

**Tiến độ:** 1/8 bước
**Bước kế tiếp:** [1] Outline → 🔴 GATE: chọn title + approve outline
**⚠️ Cảnh báo:** mọi con số ánh sáng phải verify lại ở [1.5] · hạn đăng sớm trong tháng 10 · cùng cửa sổ mùa với 047 (houseplants indoors before frost) → tách rõ: 047 = cây cảnh vào nhà, bài này = rau ăn được.

## SCRIPT v3 — viết lại theo L14–L18 (18/10/2026)
- `script.v3.md` (≈2.710 từ ≈ 16:26 @165 wpm): `script_lint.py` PASS 0 lỗi/0 cảnh báo · `claim_check.py` OK (chỉ số trong allow-list) · `originality_check.py` 0 câu trùng với 058–061 (trùng với script.md cũ của chính 062 là đương nhiên).
- Title mới: **Grow Vegetables Indoors This Winter (5 Can Use a Window, 2 Need a Lamp)** (bỏ "Easy" — L17). Chưa chấm vidIQ (hết credit).
- Chưa làm: duyệt v3 (GATE), tạo lại voice (Key gardent, ~1,48 credit/ký tự), dựng lại draft CapCut, cập nhật SEO/thumbnail theo title mới. Bản đã xuất giữ nguyên làm mốc đối chứng retro.

## VOICE v3 (18/10/2026)
- `voice/v3/voice.mp3` + `voice.srt` (giọng Key gardent clone_2697441, speed 1,0, text `voice/v3/voice-text.txt` 15.708 ký tự). **Credit đã dùng: 23.264** (ước tính 23.250). Bản voice cũ giữ ở `voice/voice.mp3`.

## DỰNG v3 (18/10/2026)
- `footage/v3/shotlist.csv` (314 shot: 178 clip · 79 ảnh · 40 thẻ GFX · 17 AI; 0–1′ avg 2,18s max 2,8s · 1–3′ avg 3,07s · sau 3′ avg 3,33s max 4,0s; 94% hình thật) từ `voice/v3/voice.srt` + `footage/v3/shotlist_cfg_062v3.py` (pool lấy từ `_LIBRARY/catalog.csv`).
- Draft CapCut mới: **`G062v3_auto`** (`python tools/garden_build_capcut.py --v3`; draft cũ G062_auto không đụng). Chữ: A 14 · B 37 · SRC 5 (Illinois ×2, Maryland ×2, Penn State ×1 — không có New Hampshire) · ILL 17 · thẻ đếm 6. SFX: 62 đoạn trên track "SFX TEXT" (Woosh cho chữ lớn/thẻ đếm, 挥动 cho nhãn nguồn/chữ phụ) — file SFX ở `_LIBRARY/sfx/`.
- Thiếu: ảnh AI-T5-TUBE chưa từng tạo (bỏ khỏi cấu hình); SFX đề xuất thêm: impact/hit nhẹ (stamp), pop nhỏ (chữ phụ), tick/ding (thẻ đếm). Chưa có nhạc nền. SEO/thumbnail theo title mới chưa cập nhật.

## DỰNG v3b — thẻ đồ họa kiểu bảng phấn (18/10/2026)
- Lý do: thẻ GFX cũ hiện 2–4s và dày đặc (ROADMAP ×4, TABLE ×20 liên tiếp). Nay thẻ gắn theo lời đọc (`GRAPHIC_TRIGGERS` trong `footage/v3/shotlist_cfg_062v3.py`), chỉ 10 thẻ, mỗi thẻ 9–21 giây, cách nhau ≥7s: ROADMAP 9,3s · FOOTCANDLE 12,4s · DARKBREAK 10,7s · TABLE-3 16,9s · DIS-HOURS 13,6s · DIS-DIST 13,8s · DIS-WASH 15,1s · DISTANCE 10,7s · 3CARDS 13,2s · CALENDAR 21s.
- Thẻ kiểu phấn theo 4 mẫu user vẽ (DIS-HOURS, TABLE-3, FOOTCANDLE dùng nguyên ảnh của user; ROADMAP vẽ lại vì mẫu ghi "5 easy" trái luật L17 → "5 can use a window, 2 need a lamp"); các thẻ còn lại + thẻ đếm do `tools/garden_gfx_chalk.py` (font Ink Free) — đã vào `_LIBRARY/gfx/CHALK-*`.
- Draft mới **`G062v3b_auto`** (283 shot, SFX 61, chữ A 11/B 40/SRC 4). `G062v3_auto` cũ giữ nguyên.

## SEO v3 (18/10/2026)
- `seo-en.md` viết lại cho title **5 Can Use a Window, 2 Need a Lamp** + chapters từ voice v3 (13 mốc, 0:00–15:29) + mẹo sun/no sun lên đầu mô tả + pinned comment mới; bản cũ giữ ở `seo-en.v2-published.md`. Thumbnail A/B giữ nguyên (đã kiểm 0 từ trùng với title mới). Chưa làm ES; title chưa chấm vidIQ.

## THUMBNAIL ẢNH THẬT (18/10/2026)
- `thumbnail-real-a.jpg` (LEGGY? / 6-8 HOURS, Before→After: ❌ mầm vươn trong tối · ✅ cây dưới đèn bàn) và `thumbnail-real-b.jpg` (NO FRUIT? / 6 HOURS DARK, cà chua xanh) — ảnh Pexels từ `_LIBRARY` (giấy phép tự do, không cần ghi nguồn), chữ vàng/trắng viền đen, pill nguồn nhỏ (ILLINOIS / NEW HAMPSHIRE EXTENSION) làm tín hiệu uy tín. Tool: `tools/garden_thumb_real.py`. Hai bản AI cũ (`thumbnail-a/b.jpg`) giữ nguyên để Test & Compare. Lưu ý: ✅ bên A là cây cảnh (không phải rau), ảnh B là cà chua xanh trên cây (chưa chín) — nếu muốn sát hơn thì đổi ảnh nguồn trong tool.

## QUYẾT ĐỊNH 18/10/2026 (user)
- **Giữ nguyên script.v3 + voice v3 + draft G062v3b_auto**, chấp nhận rủi ro L15 (lộ trình + danh sách nguồn đọc ở 0:43–0:58) để đo bằng retro. Không sửa, không tạo lại voice (đã dùng 23.264 credit).
- Retro phải trả lời: retention quanh 0:40–1:00 có tụt ≥15 điểm % không (xác nhận hay bác L15). Kết quả ghi vào Evidence log của `references/lessons-learned.md`.
- Còn lại trước khi đăng: duyệt draft CapCut sau khi user xem, export, chọn thumbnail Test & Compare (`thumbnail-real-a/b`), đăng seo-en.md; chưa làm ES.
