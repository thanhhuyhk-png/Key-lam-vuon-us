# Nhật ký Tiến trình Kênh — Senior Garden Guide (`garden-us-60k`)

> Repo theo dõi toàn bộ tiến trình phục hồi, sức khỏe kênh, kịch bản, thử nghiệm đóng gói/Ads/Shorts và kết quả thực tế của kênh **Senior Garden Guide** (`UCnCALMh5O4Ykpv_ESjZ6WqA`).
> Bảo mật: `.secrets/`, `.env`, token OAuth và file media nặng (`*.mp4`, `*.mp3`, `Xuất Video/`, `_LIBRARY/`) được loại khỏi Git qua `.gitignore`.

---

## Mốc 2 — Hoàn thành trọn bộ Tập 102 chuẩn phục hồi US (2026-11-26)
- **Thư mục:** [big-idea-102-winter-sowing-milk-jugs](scripts/big-idea-102-winter-sowing-milk-jugs/pipeline-state.md) — **`Winter Sowing in Milk Jugs: 6 Seeds That Work (and 3 That Don't)`** (Lane A · Mùa vụ Mỹ T12–T2 · cửa sổ đăng **15/12–28/12/2026**).
- **Kỷ lục chất lượng:** 43 dòng Claim Ledger `Pass2=Y` từ 7 nguồn `.edu` độc lập · `script.md` **1.751 từ ≈ 10,6′** · **`gate.py` 7/7 PASS (0 lỗi, 0 cảnh báo, 0 câu trùng 5 tập gần nhất)** · Phản biện kép 3R V1 chéo hãng (Gemini + Claude Opus + Đóng gói L25) & V2 độc lập đạt **Hook 34/35 · Compliance Risk Score 10/10 (PUBLISH)**.
- **Tập đầu tiên áp đồng bộ chuẩn mới:** khóa cứng **`en-US` duy nhất (L28)** (`seo-en.md`, đã tắt ES) + **Thumbnail Clean Plate không chữ + ghép chữ tay/Pillow (L29)** (`6 SEEDS IN JANUARY / NO GROW LIGHTS`, `thumbnail-prompts.md`) + nối `thu_muc` vào `research/du-bao.csv` và lập `prediction.md` đặt đích **US ≥ 60% · Smart TV ≥ 40% · CTR 3,8–5,5%**.

---

## Mốc 1 — Đồng bộ Cấu hình & Luật chống lệch tệp (2026-11-26)
- **`channel.config.json`:** đổi `target_viewer` sang **Smart TV (đích ≥45%) + Mobile**; tắt `translate_es: false` (chỉ xuất bản `en-US`); thêm block `publish_rules` khóa `en-US`, cấm Auto-dubbing/Localization ngoài Mỹ, chuẩn thumbnail `clean_plate_manual_overlay`.
- **`references/lessons-learned.md`:** nâng **L28** (cấm Localization/Auto-dubbing ngoài `en-US`) và **L29** (tách ảnh nền sạch `no text` + ghép chữ tay/Canva/Pillow cho Smart TV & mobile) lên **ACTIVE RULES** (gộp nhóm giữ đúng trần 20 dòng C4) + ghi đủ bằng chứng OAuth vào Evidence log.
- **`references/channel-truth.md` & `CLAUDE.md`:** đồng bộ AUDIENCE (Smart TV + Mobile), tắt bước dịch ES, ghi nhận vai trò Radar của Auto Trend Studio ở Bước 0.
- **`.claude/skills/garden-us-thumbnail/SKILL.md`:** đổi mặc định từ *AI tự vẽ chữ* sang **Clean Plate (ảnh nền sạch không chữ) + Overlay Spec ghép chữ tay/Canva/Pillow**.

---

## Mốc 0 — Baseline & Chẩn đoán Toàn diện (2026-11-26)

### 1. Chỉ số gốc (OAuth YouTube Analytics + Studio export tới 21/11/2026)
| Chỉ số | Mốc 2026-11-26 | Đích 30 ngày (26/12) | Đích 90 ngày (26/02) |
|---|---:|---:|---:|
| Quy mô kênh | 62.900 sub · 6,05M view · 260 video | — | — |
| Views 28 ngày | 61.992 (-25,2% vs kỳ trước) | ≥ 90.000 | ≥ 180.000+ |
| Tỷ trọng **US (28d)** | **47,4%** *(video mới chỉ 11%–30% US)* | **≥ 58%** *(video mới ≥ 55%)* | **≥ 62–68%** *(Tier-1 ≥ 80%)* |
| Tỷ trọng **Ấn Độ (28d)** | **16,8%** (AVD 19% vs US 33%) | ≤ 11% | **< 8%** |
| Tỷ trọng **Smart TV** | **29,4%** *(thời đỉnh T1–T4: 59,5%)* | ≥ 40% | **≥ 45%** |
| **CTR video mới (≤45d)** | **2,58%** *(catalog cũ 4,35–8,58%)* | ≥ 3,8% | **≥ 4,2–5,0%** |
| **Trung vị `views_5d`** | **596** | ≥ 1.000 | **≥ 1.500+** |
| Tỷ trọng Catalog cũ | 92,9% view (15 video mới chỉ 7,1%) | ≤ 80% | ≤ 65% |

### 2. 6 Nút thắt đã phát hiện & Hồ sơ giải pháp
1. **19–21 ngôn ngữ Localization (Auto-dubbing / dịch tiêu đề tự động)** trên toàn bộ video mới (gồm 3 video Private sắp đăng `xYgPSm00Wcs`, `zK1CQBLKBck`, `rdsi3pGRMlg`) kéo 60%–88% mẻ thử đầu sang Ấn Độ/Indonesia/Ba Lan/Brazil/Nhật/Hàn với AVD 3%–18%, bóp chết đề xuất Mỹ.
2. **Sụp đổ Smart TV (59,5% → 29,4%)** do pha loãng sang Mobile/non-US & đợt 27 Shorts 9s tháng 6 (đã xóa 18 / ẩn 9).
3. **Thumbnail đang để AI vẽ chữ hoàn toàn** + tiêu đề meta/trừu tượng (L21) làm CTR video mới tụt còn 2,58%.
4. **Channel Keywords trống (`""`)**, `defaultLanguage` chưa khóa `en-US`, mô tả kênh vẫn khóa *"brand-new senior gardeners"*.
5. **Auto Trend Studio:** Đã tạo & nạp dự án `Kênh làm vườn US` (`kenh-lam-vuon-us`, 19 kênh · 1.425 video · 1.032 bình luận · điểm ngách 79/100); chốt **Model Link chính: `Frugal Solutions`** + bổ trợ `Plant Explainer / Backyard Buddy / Evergreen Seniors`, loại `Wonder Balcony` (rủi ro chính sách cao).
6. **Goha Studio:** Đã sẵn sàng 2 tài khoản Flow (PRO + ULTRA) & 3 kịch bản Shorts 30s nối Related Video vào nhóm video US mạnh nhất.

### 3. Hồ sơ chiến dịch đính kèm
- [01-CHAN-DOAN-SUC-KHOE-VA-LECH-TEP.md](research/kenh-lam-vuon-us/01-CHAN-DOAN-SUC-KHOE-VA-LECH-TEP.md)
- [02-AUTO-TREND-KEY-TEP-VA-CHU-DE.md](research/kenh-lam-vuon-us/02-AUTO-TREND-KEY-TEP-VA-CHU-DE.md)
- [03-KE-HOACH-QUANG-CAO-US-5USD.md](research/kenh-lam-vuon-us/03-KE-HOACH-QUANG-CAO-US-5USD.md)
- [04-CHIEN-LUOC-SHORTS-30S-VA-GOHA.md](research/kenh-lam-vuon-us/04-CHIEN-LUOC-SHORTS-30S-VA-GOHA.md)
- [05-LO-TRINH-PHUC-HOI-MO-RONG-NGACH.md](research/kenh-lam-vuon-us/05-LO-TRINH-PHUC-HOI-MO-RONG-NGACH.md)

---

## Quy ước Commit theo dõi tiến trình
- `audit(YYYY-MM-DD): ...` — Cập nhật số liệu kiểm định kỳ (`yt_analytics.py` / `kiem_dinh_ky.py` / Studio CTR)
- `script(NNN): ...` — Kịch bản, outline, research, prediction, retro từng video
- `ads/shorts: ...` — Kết quả test Google Ads \$5/ngày & Shorts 30s (Goha Studio)
- `config/rules: ...` — Cập nhật cấu hình kênh, luật `lessons-learned.md`, pipeline
