---
file: title-keyword-strategy-en.md
role: Per-workspace Title/Keyword/Gap strategy cho Garden US (EN, thị trường US). Skill chung mkt-youtube-outline đọc file này (qua KEYWORD_STRATEGY_FILE) để bật Title C (Hybrid). KHÔNG nhét nội dung này vào file skill.
channel: Senior Garden Guide (garden-us-60k)
market: US / English
derived_from: 10x-youtube-niche-validate-vn (verdict GO borderline) + 10x-youtube-niche-gap-vn — session 2026-06-21
refresh_cadence: re-pull vidIQ mỗi quý hoặc khi weekly sync (CN) thấy keyword trôi
last_updated: 2026-10-05
changelog:
  - 2026-10-05: thêm KEYWORD-FIRST GATE — đo keyword vidIQ + soi outlier BẮT BUỘC trước khi chốt title; keyword chính exact-phrase trong ~25 ký tự đầu khi how-to/theo mùa/nhu cầu +30%. Ghi đè một phần ANCHOR-INTENT RULE 07/15 (user chỉ ra ở big-idea-058).
  - 2026-07-15: Title Engine v2 — thêm ANCHOR-INTENT RULE (neo pipe KHÔNG còn mặc định, chỉ video search-intent) + OUTLIER PATTERN MATCH + POST-PUBLISH TITLE PROTOCOL 48h. Data: top 5 video kênh 0/5 dùng pipe-neo; outlier winners edible-weeds (300K/284K views) 0 neo; US vol tier Entry chỉ ~54–69.
  - 2026-07-04: thêm PAIN-REMOVAL STACK vào POWER LEXICON (công thức video AVD cao nhất kênh 49% — lesson L8) + siết HYBRID_RULE #2 theo L6 (title claim sốc cần proof <20s — 5 video retro chết vùng 19–34s) + 2 title seeds L8.
  - 2026-06-24: thêm POWER LEXICON + OVERCLAIM BLACKLIST + DELIVERY-LOCK TEST (từ phân tích 15 competitor title hype vs data kênh — CTR cao + AVD thấp = clickbait penalty). Chỉ áp cho US.
---

# Title / Keyword / Gap Strategy — Garden US

> ⚠️ Mọi volume là **US countryVolume** (không phải global). vidIQ topMarkets của nhiều keyword senior lệch về VN — số global gây hiểu nhầm; chỉ tin số US.

---

## TITLE_FORMULA

```
[HOOK breakout — ~40 ký tự đầu] + " | " + [KEYWORD NEO winnable]
```

- **40 ký tự đầu = chiến trường.** Audience 60–80 xem mobile thấy ~40 ký tự đầu trước → phải gánh **specific quantity + curiosity** ngay (số / "$" / "no-bend" / "without bending").
- **Đuôi = keyword neo để rank**, ngăn cách bằng ` | `. **Neo bằng tier Entry/Growth (comp ≤30)** — KHÔNG neo Foundation (comp 41–43, kênh chưa đủ authority để thắng).
- Tổng ~60–65 ký tự / ~12 từ (đúng pattern top video kênh).
- Leading number ưu tiên (40% top video).

---

## 🔑 KEYWORD-FIRST GATE (2026-10-05 — ghi đè một phần ANCHOR-INTENT RULE bên dưới)

> **Lý do (user + data):** keyword phân tích là tín hiệu quan trọng để video được ĐỀ XUẤT và được TÌM. Video garlic big-idea-058 suýt ra với title tò mò **không có** keyword trong khi "how to plant garlic" US ~15,990/th **+315%** so với nền 30 ngày (mùa trồng). User chỉ ra → đổi title keyword-first. Luật 07/15 ("browse-intent bỏ neo keyword") quá cứng: nó đúng với listicle/curiosity thuần, **sai** với video how-to/theo mùa có nhu cầu tìm kiếm đang tăng.

**QUY TRÌNH BẮT BUỘC cho MỌI video, TRƯỚC khi chốt title (Bước 3 outline):**
1. **Đo keyword bằng vidIQ** (`vidiq_keyword_research`, `country:"US"`) cho 3–5 ứng viên cụm + biến thể. Ghi vào `pipeline-state.md`: search/tháng · `searchDemandGrowthPct` (so nền 30 ngày) · competition.
   - ⚠️ Chỉ tin số **US** / cụm **đúng ý định** của video. Cụm chung ("how to plant garlic") ≠ cụm cụ thể ("…in pots" thường <750). Ghi rõ.
2. **Soi outlier cùng chủ đề** (`vidiq_outliers`, 1 năm, `minViews` ~10K): đọc pattern title đang thắng (động từ · cụm · kết quả).
3. **Keyword chính vào title — ĐỨNG TRONG ~25 KÝ TỰ ĐẦU, nguyên văn (exact phrase)** khi thoả MỘT trong:
   - video how-to / "cách làm" có nhu cầu tìm kiếm rõ (≥ ~3,000/th US), HOẶC
   - nhu cầu **đang tăng ≥ +30%** so nền 30 ngày (mùa vụ), HOẶC
   - tìm thấy ≥2 outlier cùng chủ đề có cụm đó.
   Không thoả cả 3 (listicle/curiosity thuần) → mới được dùng title không keyword, nhưng keyword vẫn BẮT BUỘC có ở: description dòng 1 · tags · **câu thoại 30–60s đầu** (YouTube đọc cả transcript).
4. **Giữ cụm lọc ý định** trong title (vd "in a Pot") để không hút nhầm người tìm cụm chung.
5. **Vẫn giữ** khung ĐƯỢC THÊM + mốc thời gian/kết quả + L9 (không nhãn tuổi) + ≤65 ký tự. Keyword-first ≠ bỏ lời hứa: dùng ngoặc đơn cho phần hứa ("… Now (Whole Bulbs by Next Summer)").
6. **Title tò mò cũ làm á quân** swap giờ 48 nếu CTR <3.5% — đo cả **traffic Search của riêng video** (Studio → Reach), không chỉ CTR Browse.
7. **Mùa vụ có hạn:** nhu cầu tăng mạnh thường nguội sau 3–6 tuần → KHÔNG chờ giờ 48 mới đổi sang title có keyword; đưa keyword vào ngay lúc đăng.

**Ví dụ (big-idea-058):** ❌ `Plant 1 Garlic Clove in a Pot Now, Get a Whole Bulb Next Summer` (không có cụm) → ✅ `How to Plant Garlic in a Pot Now (Whole Bulbs by Next Summer)` (cụm ở 20 ký tự đầu).

**📊 KIỂM CHỨNG TRÊN KÊNH (05/10/2026 — OAuth, 49 video long-form, lưu lượng trọn đời từng video):**
| Nhóm video lớn (≥50K view) | n | Search share | Lượt xem từ Search | Browse | Suggested |
|---|---|---|---|---|---|
| Title CÓ cụm chủ thể người ta gõ (avocado from seed · aloe vera · lemon tree · bell peppers · root cellar · indoor plants…) | 10 | **2.0%** (median 1.9%) | **69,660** | 86% | 9% |
| Title TÒ MÒ, không cụm chủ thể (6 Weeds · Pesticides · Ancient Liquid · Bug-Free · Minerals) | 5 | **0.5%** (median 0.9%) | 8,289 | 90% | 6% |
- Có cụm chủ thể → Search share **~4×** và Suggested cao hơn (9% vs 6%). Đỉnh: *Grow Avocado From Seed…* 4.7% = **22,967** lượt từ Search (cụm "how to grow avocado from seed" 857, "avocado seeds how to grow" 770).
- ⚠️ **Search KHÔNG phải động cơ chính:** kênh 1.5% từ Search; video lớn nhất cũng chỉ 2–5%. ~86–90% vẫn là Browse → keyword giúp **thêm**, không thay được CTR/AVD.
- ⚠️ Video mới (26 video từ 08/2026): median **21 lượt** từ Search, cụm tìm kiếm là **rác ngẫu nhiên** ("try not to laugh", "james blunt") → YouTube chưa gắn video mới với truy vấn nào. Đa số title mới không có cụm chủ thể rõ.
- "senior garden guide" (tên kênh) là top cụm ở nhiều video → có lượng tìm theo thương hiệu.
- Giới hạn: tương quan, không phải thí nghiệm; nhóm tò mò n=5. Bài garlic (058) là phép thử có chủ đích đầu tiên.

**Dữ liệu cần theo dõi để hiệu chỉnh luật này:** Search share video này (kênh 8.9%) · CTR giờ 48 · Search vs Browse. Retro bài 058 quyết định giữ/siết ngưỡng "+30% / ≥3,000".

---

### ⚖️ ANCHOR-INTENT RULE (2026-07-15 — neo pipe KHÔNG còn mặc định)

> **Data buộc phải sửa luật:** top 5 video kênh (28d) **0/5 dùng pipe-neo** · outlier winners ngách edible-weeds 3 tháng (300K @ 7.9K subs, 284K @ 58.9K subs) **0 video neo** · US volume tier Entry chỉ ~54–69 (≈ vài nghìn search/tháng — rank #1 cũng chỉ vài trăm view/tháng) · kênh là **browse-driven** (Browse từng chiếm đa số traffic trước demotion). Neo pipe ăn mất 20–25 ký tự vàng của title mà trả lại rất ít.

| Video intent | Neo pipe ` \| keyword`? | Thay bằng |
|---|---|---|
| **Search-intent** — how-to cụ thể, "what to plant in [month]", tool/arthritis (white-space comp 1.4), build guide | ✅ NEO (Entry/white-space) — search là kênh acquisition thật của loại video này | — |
| **Browse-intent** — listicle, curiosity packaging (đa số video kênh) | ❌ **BỎ neo** | 1 identity token inline nếu tự nhiên ("Over 60", "no-bend") hoặc không cần; keyword đẩy xuống **description dòng 1 + tags + câu thoại đầu** (bước SEO 4a) |

→ SEO không mất — chuyển tầng metadata. Toàn bộ 65 ký tự title dành cho hook + curiosity gap. Title seeds cũ có neo vẫn hợp lệ cho video search-intent.

---

## KEYWORD_TIERS

> Neo title MẶC ĐỊNH ở **Entry**; lên **Growth** khi đã có vài video rank; **Foundation** chỉ xây authority dài hạn, KHÔNG neo sớm.

**Foundation** (vol cao, comp cao — xây dần, đừng neo sớm)
| Keyword | US vol | Comp |
|---|---|---|
| gardening tips | 76 | 43 |
| gardening for beginners | 73 | 41 |

**Growth** (sweet spot tháng 2–6 — neo được)
| Keyword | US vol | Comp |
|---|---|---|
| gardening for seniors | 69 (US ~7.2k/mo) | 26 |
| container gardening for beginners | 61 | 38 |
| raised bed gardening for seniors | 55 | 36 |
| low maintenance gardening | 54 | 43 |

**Entry** (dễ rank nhất — neo MẶC ĐỊNH, start tháng 1)
| Keyword | US vol | Comp |
|---|---|---|
| senior gardening tips | 59 | 27 |
| gardening over 60 | 54 | 24 |
| gardening for elderly | 54 | **20** |
| old fashioned gardening tips | 53 | 34 |

**White-space** (comp ~0 — SỞ HỮU sớm, neo cho video chuyên sâu)
| Keyword | Comp | Ghi chú |
|---|---|---|
| gardening tools for arthritis | **1.4** | gần như trống — affiliate mạnh |
| garden tools for seniors | ~14 | ergonomic |
| gardening without bending | ~14 | (search noisy, lọc on-topic) |
| stress-free gardening | ~39 (đang lên) | đúng DNA "Lazy" |

---

## GAP_LIST

**🟢 Ưu tiên — white-space cạnh tranh thấp (đối thủ chưa lấp / chỉ 1 video lẻ):**
1. Ergonomic / body-friendly: đau lưng, đầu gối, **viêm khớp** (kw arthritis comp 1.4) — gap#1
2. No-bend / waist-high raised bed **build** (đối thủ chỉ 1 video Amish lẻ) — gap#2
3. Microplastic-safe versions của hack phổ biến (milk-jug, plastic bottle) — gap#3
4. **Science-tested vs AI-slop**: kiểm chứng grandma-hack bằng khoa học (eggshell calcium, blossom-end-rot, baking soda) — gap#4 ⭐ wedge faceless
5. Zone/seasonal-specific cho senior ("what to plant in [month] without bending") — gap#5
6. No-bend tools, kneeler-seat, tưới nhàn (drip/olla) cho người yếu tay/lưng

**🔴 Đại dương đỏ — TRÁNH (hoặc chỉ làm khi đã có authority + khác biệt mạnh):**
- Generic **"grandma free gardening hacks" listicle** → No Longer Here (175k) + đám AI faceless thống trị, retention thấp.
- **Depression-era / frugal hacks listicle** → No Longer Here sở hữu.
- Head terms generic "gardening tips" / "gardening for beginners" → comp 41–43, kênh mới chết.

> ⚠️ **Caveat lifecycle:** ngách verdict **GO borderline** (Tầng 1b outlier 27.3%, sát ngưỡng 30%). Nghĩa là KHÔNG phải cứ chọn gap là nổ — phải **khác biệt** (xem HYBRID_RULE wedge), không làm content senior chung chung.

---

## HYBRID_RULE

Khi ghép Title C, tuân theo (đè lên ví dụ generic của skill):

**4 guardrail bắt buộc (FAIL bất kỳ → viết lại):**
1. **Specific quantity trong 40 ký tự đầu** — số/đo/$/"no-bend"/"without bending". (Channel data: 100% top video có specific quantity.)
2. **Lời hứa deliver được trong 60s đầu script** (lesson L3 — title bait không deliver = AVD chết). **RIÊNG title dạng claim sốc/contrarian (STOP…/Never…/Why Experts…/Only 9 of 15…) → bằng chứng/con số phải xuất hiện TRƯỚC GIÂY 20** (lesson L6 — vùng chết claim-sốc là giây 20–33; 5 video retro đều gãy đúng đây: Snakes -35.1% @20-30s, STOP Composting -22.5% @22-34s…). Chọn title sốc = tự ký cam kết proof-đầu-20s trong bảng Spine (GATE 2.5); không cam kết được → đổi sang pain-removal stack.
3. **Không exotic plant** (L1) + **KHÔNG chạm OVERCLAIM BLACKLIST** (xem section dưới). Botanical/dollar shock OK; human-fear/cure/hype-tăng-trưởng KHÔNG.
4. **DELIVERY-LOCK TEST** — mọi title nêu OUTCOME hoặc TIMEFRAME phải pass cả 2: (a) có claim tương ứng trong `research-brief.md`; (b) script deliver đúng lời hứa đó trong 60s đầu. FAIL bất kỳ → đổi từ ở title, KHÔNG để sửa muộn ở audit. *(Bắt lỗi "in 1 Step / made safe" ngay GATE outline thay vì lọt tới audit Bước 3.)*

**Neo keyword (áp ANCHOR-INTENT RULE ở trên — chỉ video search-intent):** mặc định tier **Entry** (comp ≤27); dùng **Growth** khi có authority; **white-space** (arthritis…) cho video chuyên sâu. KHÔNG neo Foundation sớm. Video browse-intent → bỏ neo, keyword xuống description/tags.

**⭐ FACELESS WEDGE (khác biệt cốt lõi):** kênh này **faceless (AI voice)** → KHÔNG thể đánh bài "người thật". Thắng đám AI-slop bằng thứ chúng FAIL: **độ chính xác science-backed + số liệu cụ thể + chiều sâu verified**. Comment thật cho thấy khán giả chán "AI grandma giống hệt nhau" và **sửa lỗi khoa học** của các kênh đó (eggshell, blossom-end-rot). → Title nên phát tín hiệu **proof/number/"science says"/"the real reason"**, tránh giọng listicle AI-grandma generic, hoán đổi được. Mỗi claim neo về nguồn (research-brief).

**Tone:** theo `BRAND_VOICE_FILE` (Lazy Grandma Wisdom + Science-Backed Proof — bà nội Ohio, không cowboy, narrator = educator).

---

## OUTLIER PATTERN MATCH (Title Engine v2 — 2026-07-15)

Trước khi trình title ở GATE: đối chiếu survivors với **outlier titles thật của chủ đề** (ưu tiên data đã research trong `research/youtube/topics/[slug]/videos.json`; không có → `vidiq_outliers` theo keyword). Title phải khớp **≥1 pattern đã được thị trường trả tiền**. Patterns đang thắng trong ngách garden/foraging (07/2026):
- `More X Than Y` (so kè bất ngờ: weed vs vegetables/fish)
- `Stop Killing/Pulling These N…` (negative command + số)
- `You're Throwing Away / You're Pulling…` (mid-action regret + identity)
- `This "Weed"/One Plant…` (single-reveal — giấu chủ thể, gap mạnh nhất)
- Possessive `Your Yard / Your Garden` (identity token)

Không khớp pattern nào → không tự động loại, nhưng phải ghi rõ "off-pattern" ở GATE để user cân nhắc rủi ro.

## POST-PUBLISH TITLE PROTOCOL (48h — title không phải quyết định 1 lần)

- **Giờ 48 sau publish:** CTR < 4% (benchmark kênh 5.5%) → **swap sang title á quân** đã duyệt ở GATE (giữ nguyên thumbnail), ghi vào `retro.md`: title cũ/mới + CTR trước/sau swap.
- Thumbnail iterate riêng bằng YouTube **Test & Compare** (A/B native).
- **KHÔNG đổi title + thumbnail cùng lúc** — mất khả năng đọc tín hiệu biến nào có tác dụng.
- CTR khỏe nhưng AVD thấp → vấn đề KHÔNG ở packaging, đừng đụng title (xem lesson demotion 07/2026).

## POWER LEXICON + OVERCLAIM BLACKLIST (2026-06-24)

> Rút từ phân tích 15 competitor title CTR cao trong ngách gardening. Bài học data: title hype (CTR cao + AVD thấp) bị thuật toán gắn cờ clickbait & bóp đề xuất — *"retention <40% → hạ ưu tiên bất kể CTR"*. Video tệ nhất kênh ("STOP Pesticides! 1 Spoon" — 30k views, AVD 20.6%) chính là pattern này. Faceless + senior 60–80 = trust mong manh → KHÔNG bắt chước đám AI-slop dùng hype + citation giả.

### ✅ POWER LEXICON — token boost CTR mà KHÔNG phá retention (ưu tiên dùng, nhét 40 ký tự đầu)
- **⭐ Pain-removal stack (L8 — công thức video AVD CAO NHẤT kênh, 49%):** xếp chồng 2–3 vế "No/Zero + pain": "No Soil, No Back Pain, No Cost" · "No Digging, No Weeding" · "Zero Soil, Zero Cost". Là benefit-stack ergonomic (gap#1 seniors) — KHÔNG phải claim sốc nên không kích vùng chết 20–33s; deliver dần trong video. Ưu tiên số 1 khi chọn giữa các nhóm.
- **Quantity:** "Just 1 Spoon/Ingredient/Pot" · "$1 / $2 / under $50" · "40 Plants" · "no soil / no-bend"
- **Time-specific:** "in 10 Days, Not Weeks" · "by August" · "in 1 Afternoon"
- **Curiosity-closed (đóng được trong video):** "(And What It Means)" · "…Explained" · "Finally Found" · "What Nobody Tells You"
- **Credibility (⭐ faceless wedge — thứ AI-slop FAIL):** "Science Says" · "University Research" · "The Real Reason" · "PROVEN" *(chỉ khi research-brief có nguồn)*
- **Action:** "Add THIS" · "Do THIS" *(chỉ khi #1 reveal sớm, deliver 60s)*

### ❌ OVERCLAIM BLACKLIST — reject (clickbait-bait, đào sâu AVD; vi phạm compliance + faceless trust)
`EXPLODE` · `INSTANTLY` · `Brings to Life` · `Comes Back to Life` · `Dead Plants` ·
`Triples/Doubles in N Days` *(trừ khi research-brief có đúng con số đó)* ·
`PROVEN` trần (không nguồn) · `SECRET/SHOCKING` trần · ALL-CAPS toàn title · medical cure/miracle/detox.

> Quy trình ở `mkt-youtube-outline` (Bước 3 tạo title): chạy mỗi candidate qua POWER LEXICON (ưu tiên) → OVERCLAIM BLACKLIST (loại) → DELIVERY-LOCK TEST (HYBRID_RULE #4). Skill đã đọc file này nên KHÔNG cần sửa skill chung.

### Chuyển hoá hype → channel-safe (giữ CTR, deliver được)
| ❌ Hype gốc | ✅ Channel-safe |
|---|---|
| "Make It EXPLODE" (aloe) | `The 1 Kitchen Scrap That Doubles Aloe Growth \| Senior Gardening Tips` |
| "Triples Your Plants in 7 Days" | `Why Epsom Salt Greens a Yellow Lawn in 10 Days \| Gardening Over 60` |
| "Even Dead Plants Come Back to Life!" | `5 Fixes for a Plant You Think Is Dead — What Actually Works` |

---

## Title Seeds (8–10 — hybrid thật: hook + neo + tier + gap)

1. `7 No-Bend Garden Setups That Save Your Back | Gardening for Seniors` — hook 013 + Growth · gap#1
2. `Build a No-Bend Raised Bed for Under $50 | Gardening Over 60` — hook 014 + Entry(24) · gap#2
3. `The Tool That Saves Arthritic Hands | Garden Tools for Arthritis` — white-space(1.4) · gap#1/#6
4. `5 Garden Hacks Science Says Actually Work | Old Fashioned Gardening Tips` — anti-slop wedge + Entry · gap#4
5. `Does Baking Soda Really Help Your Garden? | Senior Gardening Tips` — myth-test + Entry · gap#4
6. `What to Plant in July Without Bending | Gardening Over 60` — zone/seasonal + Entry · gap#5
7. `7 Low-Effort Crops for Tired Hands | Gardening for Elderly` — Entry(20) · gap#6
8. `The Milk-Jug Watering Trick, Made Safe | Low Maintenance Gardening` — microplastic-safe + Growth · gap#3
9. `Raised Beds for Bad Knees: The 30-Minute Build | Gardening for Seniors` — build + Growth · gap#2
10. `Why Your Eggshells Aren't Feeding Your Tomatoes | Senior Gardening Tips` — science correction + Entry · gap#4
11. `Grow 7 Herbs in Water — No Soil, No Bending, No Cost | Gardening for Elderly` — ⭐ L8 pain-stack + Entry(20) · gap#1/#5
12. `5 Crops in Buckets — No Digging, No Weeding, No Sore Knees | Container Gardening for Beginners` — ⭐ L8 pain-stack + Growth · gap#1

> Seeds #1–#2 đã sản xuất thật (big-idea-013, 014) = bằng chứng formula chạy. #3–#10 từ cơ hội gap chưa làm. #11–#12 (2026-07-04) theo công thức L8 của video AVD 49% "7 Plants That Grow in Water — No Soil, No Back Pain, No Cost".
