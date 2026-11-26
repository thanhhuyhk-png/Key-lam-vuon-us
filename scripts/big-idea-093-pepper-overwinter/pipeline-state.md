# Pipeline State — big-idea-093-pepper-overwinter

> Auto-tracked. ✅ xong · ⬜ chưa làm. Cập nhật ở mỗi GATE.
> Last sync: 2026-11-01

**Lane:** A — Big Idea (nguồn: `/san-y-tuong` 26/10/2026, phiếu `research/phieu-kiem-dinh-pepper-overwinter-2026-10-26.md`; không có Notion #) · **Nhãn:** KHAI THÁC (phần 2 của "7 Secrets to Growing Infinite Bell Peppers" 343K) · **Độ dài:** config 20–24′; kế hoạch **6 phần ≈17–19′ (TEST độ dài, user duyệt 27/10)** · **Hạn đăng:** trước ~10/11/2026, cách geranium (big-idea-091) ≥1 tuần

| # | Bước | Skill | Output | Trạng thái |
|---|------|-------|--------|-----------|
| 0-T | 🚦 Topic Gate (≥2/3 tín hiệu) | references/topic-gate-en.md | block bên dưới | ✅ 3/3 ƯU TIÊN (user duyệt 26/10) |
| 1 | Outline | mkt-youtube-outline | outline.md | ✅ user duyệt 26/10 — title A (97), thumbnail `KEEP 3 STEMS` / `FROST TONIGHT?`; khung 7 phần ~3.400 từ, M4/M6 phụ thuộc [1.5] |
| 1.5 | Deep Research | garden-deep-researcher | research-brief.md | ✅ user duyệt 27/10 — 22 claim (14 A · 8 B); bỏ M6 giâm cành (0 nguồn T1–2) → 6 phần ≈17–19′, TEST độ dài |
| 2 | Hook | mkt-hook-kallaway | hook.md | ✅ user chọn Hook A (27/10) |
| 2.5 | Retention Spine | templates/retention-spine-single-topic-20min (6 phần) | retention-spine.md | ✅ user duyệt 27/10 — ~3.090 từ ≈18,7′ (TEST độ dài) |
| 3 | Script EN | youtube-garden-us | script.md (+ script.draft-markers.md) | ✅ user duyệt 27/10 — 2.941 từ ≈17,8′ (TEST độ dài) · compliance 10/10 |
| 3.5 | Prediction | templates/prediction.template.md | prediction.md | ✅ 27/10 — 5 TEST · P(thắng) 0,56 · quy tắc dừng views_5d <500 / CTR <4% |
| 3.6 | Voice | ai33 clone_2697441 | voice/voice.mp3 · voice.srt | ✅ 01/11 — 16:57, 24.254 credit |
| 4a | SEO EN + thumbnail prompt | garden-seo · garden-us-thumbnail | seo-en.md · thumbnail-prompts.md | ✅ 27/10 — SEO đã sửa chapter + câu quá lời; thumbnail A `FROST TONIGHT? / KEEP 3 STEMS` · B `NOVEMBER FROST? / 50–60°F, NO SUN` · user chọn cả A + B (Test & Compare) 27/10 · chưa render: G-Labs HTTP 401 (khóa trong .env chưa đổi); Gemini HTTP 429 limit 0 (khóa Free Tier, không có hạn mức ảnh) — 01/11 |
| 3.7 | Dựng video | garden_cut.py | build/final.mp4 | ⬜ chờ user duyệt — bản gốc build/final.mp4 (16:57, 01/11): 26 chữ đủ, -14,1 LUFS, KHÔNG nhạc; user tự chèn nhạc trong CapCut (bỏ final-music.mp4); chưa nhập clip vào thư viện, chưa viết credits |
| 4b | Translate ES | garden-translate-es | script-es.md | ⬜ |
| 4c | SEO ES | garden-seo | seo-es.md | ⬜ |
| 6 | Retro | yt_analytics.py retro | retro.md | ⬜ (7–14 ngày sau publish) |

**Tiến độ:** 0/9 bước (Topic Gate ✅; outline chờ GATE [1])
**Bước kế tiếp:** user tự render thumbnail A + B từ thumbnail-prompts.md (01/11) + clip AI từ ai-clip-prompts.md → voice (ai33) → dựng video theo video-map.json (TEST luồng mới, nếu đến 07/11 chưa đạt thì dựng CapCut) → đăng trước ~10/11 (sau geranium 091 ≥1 tuần) → retro · ES chờ user quyết

## Tiêu đề đã chấm vidIQ (26/10, tk3 400 → 385)
- A: `Don't Pull Your Pepper Plants Yet. They Can Live for Years` — 97 (58)
- B: `Make Your Pepper Plants Last for Years: 3 Ways to Overwinter` — 91 (60)
- C: `How to Make Your Pepper Plants Last for Years (Before Frost)` — bản 66 ký tự "(Start Before Frost)" 96; bản 60 ký tự chưa chấm
- ❌ `Pepper Plants Aren't Annuals. Keep Yours Alive This Winter` — 82

## 🚦 TOPIC GATE — 3/3 → ƯU TIÊN (2026-10-26)
| Tín hiệu | Đạt? | Bằng chứng |
|---|---|---|
| ① Kênh mình | ✅ | Nối hit "7 Secrets to Growing Infinite Bell Peppers" **343K** trọn đời (12/2025, OM 103), vẫn 47 VPH ngày 26/10 → cùng cây + cùng khung lời hứa "giữ một cây cho thu mãi" |
| ② Outlier ngách | ✅ | Hippie Chick "Don't Let Winter Kill Your Peppers: Do This Now!" 84K · 2,5K sub · OM 205 (12/10/2026) · "Don't Throw Away Your Pepper Plant in Winter! Bring It Indoors…" 61K · 4,6K sub · OM 19,5 (9/2026) · "STOP Replanting These! 5 Plants You Can Overwinter" 14K · 164K sub · OM 1,9. Ngoài ngưỡng 300K sub: Pepper Geek 139K, Next Level 53K. Pattern title: **"Don't [throw away / let winter kill] your pepper plants"** → không chép stem |
| ③ Keyword US | ✅ (yếu) | "how to make your pepper plants last for years" **3.093/th** (comp 28) — khớp đúng lời hứa · "don't ignore your pepper plants in october — winter is coming!" 9.094/th · "overwintering peppers" <750 · "growing peppers" 8.516 (−4%). ⚠️ Các cụm có số cao là cụm dạng tiêu đề video (người tìm lại video đã thấy) → coi là tín hiệu yếu; growth không có số |
| Chặn cứng | sạch | Không X1/X3/X4/X5 (không persona "tôi đã thử"), không L9, ớt không phải cây exotic, không khung sợ |
| ⓑ Bão hoà góc | không hạ | 4 kênh/90 ngày làm "giữ ớt qua đông" nhưng OM không nguội (+19%). Đã đổi góc: **3 cách giữ + chọn theo chỗ trong nhà, có số nhiệt độ** thay vì 1 cách demo |
| ⓒ Chất liệu | 6/5 | 1. Cắt còn 3 cành chính sau thu hoạch, trước sương giá (Ask Extension, Colorado MG, 27/9/2022) · 2. Rửa sạch hết đất ở rễ, trồng lại bằng chậu sạch + đất mới (cùng nguồn) · 3. Giữ 50–60°F (cùng nguồn) · 4. Tưới thưa: cho ngủ nhưng không để chết, không để khô kiệt (cùng nguồn) · 5. Ớt là cây thân thảo sống lâu năm ngắn hạn, gốc Nhiệt đới châu Mỹ, sống quanh năm chỉ ở zone 9a–11b (NC State Extension Plant Toolbox, cayenne) · 6. Sâu bệnh hay gặp: rệp, nhện đỏ, bọ phấn trắng → kiểm trước khi đưa vào nhà (NC State) |
| Trục đổi so với outlier | Cách kể | Outlier = 1 cách, demo của người trồng. Mình = educator so 3 cách (cả chậu · cắt trơ cho ngủ · giâm cành) + bảng chọn theo nhà + mốc đánh thức tháng 2–3 |

## ⚠️ Cảnh báo
- Chất liệu hạng A đã mở mới có 2 nguồn (Ask Extension CO, NC State). Bị chặn: Oregon State (trang đã lưu trữ), Missouri Extension "overwintering tropical plants" (403 từ máy này). Bước [1.5] cần thêm ≥2 trang hạng A: nhiệt độ ra hoa, đánh thức, giâm cành ớt.
- Các con số từ blog (55–65°F, cắt còn 4–8 in, ra ngoài khi đêm >55–60°F, ớt ngọt không ra hoa <65°F) **chỉ để dẫn đường**, chưa dùng trong kịch bản.
- Không hứa ra quả trong mùa đông (Ask Extension: mục tiêu là cây ngủ mà không chết).

## [1.5] Kết quả research (26/10)
- DELIVERY-LOCK "for Years": **GIỮ** — NC State "short-lived perennial" + UF/IFAS FP105 "tender perennial… perennial in zones 9B–11B". Không nguồn nào nêu số năm → kịch bản cấm "3/5 years", "forever".
- M4 (giữ xanh bên cửa sổ): giữ — đêm >50°F, ngày ~70°F, cần đèn, lắc cây để thụ phấn (Ask Extension 2023, không ghi tên chuyên gia); không có số giờ đèn → không nói số.
- **M6 (giâm cành): 0 nguồn T1–2** sau 3 lượt tìm → đề xuất BỎ hẳn (không dùng blog chưa mở). Video còn 6 phần ≈ 17–19′ → ghi TEST độ dài trong prediction như 091/092.
- YMYL: ASPCA không có mục riêng cho *Capsicum annuum* ("ornamental pepper" của ASPCA là Jerusalem cherry) → không nói "an toàn với thú cưng"; dùng câu hỏi bác sĩ thú y / ASPCA Poison Control.
- UNREADABLE: UConn insecticidal soap (cert) · UMD vegetable transplants (cert) · MSU hardening off (trống) · Oregon State (lưu trữ) · Missouri (403).

## [3] Script — báo cáo GATE (27/10)
- Độ dài: 2.941 từ ≈ 17,8′ @165 wpm (config 20–24′ → TEST độ dài, user chấp nhận, không độn). Phần: Hook 125 · M1 443 · M2 441 · M3 538 · M4 371 · M5 ~560 · M6 376 · KẾT ~89.
- Pha D: Loop #1 hook 0:29 → M5 11:31 · Loop #2 M1 3:12 → M3 6:13 · lời hứa cuối M5 → M6 · bằng chứng 0:03 (L6) · giá trị <0:60 (L3) · ACTION_TIP 2:24 + gọi lại ở KẾT (L16) · lint L14–L19 PASS · originality ≤1 câu trùng.
- Self-audit: Hook vs drop-off ✅ · pattern số cụ thể ✅ · comment themes (zone ✅, pet ✅, đa thế hệ — không có câu hoài niệm vì không có chuyện thật) 🟡 · mid-roll 2 loop mở qua phút 4–6 ✅ · evidence: mọi số có mã, 2 Consensus ✅ · voice: Here's why this works ×2, Don't panic ×1, That's it ×1, Happy gardening ✅ · Editorial Signature ×2 bảng ✅ · anti-slop: claim-scoping + so 2 nguồn ✅.
- Triple F: contractions 52% → 64%; đã bỏ 9/10 dấu chấm than + câu "Congratulations, you're the bee now!"; khôi phục "Don't panic".
- Compliance: vòng 1 8/10 (pet/kid block thiếu + sai vị trí; 4 câu hứa chắc) → vòng 2 **10/10**. Số ASPCA (888) 426-4435 orchestrator xác minh trên aspca.org 27/10. Sau vòng 2 thêm 1 câu theo góp ý của reviewer: "If a child gets into the spray, follow the first-aid directions on the label."
- ⚠️ KẾT nhắc video geranium — chỉ giữ nếu big-idea-091 đã đăng trước.
