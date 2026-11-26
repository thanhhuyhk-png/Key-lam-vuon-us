# Gói mới (tiêu đề + thumbnail) — Pineapple 060 & Lemon 061 — 2026-11-08

**Vì sao:** export Studio 10/10–07/11 cho thấy cả hai video đã được YouTube **thử mở rộng** (Pineapple 14.232 impressions, Lemon 15.206) nhưng CTR với người xem lạnh chỉ **1,62 % / 1,33 %** (catalog cũ ~5,4 %). Gói là chỗ sửa rẻ nhất khi video còn đang được phân phối. Nguồn: `research/chan-doan-kenh-2026-11-08.md` mục 4.

**Đã kiểm:**
- Mọi lời hứa đối chiếu với `script.md` của từng video (L17), không hứa thứ video không nói.
- `script_lint.py` [ĐC] 0 chỗ phạm (gồm DC009 / L20).
- `compliance_scan.py` CLEAN.
- Không có nhãn tuổi (L9).
- Tiêu đề ≤ 63 ký tự.
- Chữ thumbnail không lặp từ của tiêu đề cùng gói, và có số hoặc $ (LUẬT SỐ).

**Chưa kiểm:** `vidiq_score_title` (tốn credit, chưa chạy).

---

## 🍍 060 — How to Grow a Pineapple at Home (It Takes 2 Years!) · 7′ · AVD 29 % · CTR 1,62 %
Video giữ chân tốt (AVD 29 %), chỉ gói yếu → **ưu tiên đổi video này trước.** Tiêu đề cũ tự làm yếu lời hứa: "(It Takes 2 Years!)" báo trước là lâu, mà video thật ra hứa *một cây miễn phí từ thứ bạn sắp vứt*.

| Gói | Tiêu đề (ký tự) | Khung | Lời hứa có trong video ở đâu |
|---|---|---|---|
| **A** ⭐ | Stop Throwing Away Pineapple Tops — Grow a Free Plant Instead (63) | L20 đảo niềm tin (thứ đang vứt đi × free) | Câu mở đầu, giây 0–5: "That spiky green top you're about to throw away can become a living pineapple plant" |
| **B** | Grow a Pineapple From the Top You'd Throw Away (5 Steps) (56) | Keyword-first ("grow a pineapple from … top" 3,9–5K/tháng US) | 5 bước Twist / Dry / Pot / Warm / First year |
| **C** | What a Pineapple Top Really Does in Its First Year (50) | Tò mò trung thực | Bước 5 "The honest first year" |

L20 cho gói A:
1. Vế sau là thứ được thêm (cây miễn phí).
2. Không có chữ sợ.
3. Có nguồn hạng A (UF/IFAS, NC State Extension).
4. Chứng minh ngay câu đầu.

### Thumbnail
| Gói | Hình | Chữ VÀNG (hook) | Chữ TRẮNG |
|---|---|---|---|
| A | Before→after 40/60: trái là đầu dứa nằm trên vỏ rau trong thùng rác bếp ❌; phải là đúng đầu dứa đó đã lên lá trong chậu đất nung ✅ | `$0` | `10 MIN` (script: "about ten minutes") |
| B | Một vật chính: đầu dứa úp ngược hong khô trên bậu cửa sổ, gốc đã se và lộ mầm rễ nhỏ, vòng đỏ đứt nét quanh gốc | `DRY 1 WEEK` (NC State "one week") | `BEFORE SOIL` |
| C | 3 khung thời gian: đầu dứa mới trồng → cây lá xum xuê trong chậu lớn → cây có trái nhỏ ở giữa | `MONTH 1 → 24` | `YEAR ONE?` |

**Prompt A** (theo khuôn MASTER PROMPT của `scripts/big-idea-060-pineapple-top/thumbnail-prompts.md`):
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel. Vivid saturated colors, ultra high contrast. NO human face, no person.
SCENE: split before/after, 40/60. LEFT (40%): a fresh pineapple crown lying on vegetable peels inside an open kitchen trash bin, slightly dull light, a bold red X in the corner. RIGHT (60%, dominant): the same pineapple crown now planted in a terracotta pot, leaves green and spreading, bright warm window light, a bold green check mark. A thin white divider between halves.
TEXT — the ONLY text is exactly two lines, top-left over the LEFT half, not covering the pot: line 1 "$0" in bright YELLOW; line 2 "10 MIN" in WHITE. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow. Render exactly, no other text anywhere.
```

**Prompt B:**
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel. Vivid saturated colors, ultra high contrast. NO human face, no person.
SCENE: ONE hero object — a pineapple crown set UPSIDE DOWN to dry on a sunny white windowsill, the trimmed base facing the camera, dry and callused with a few tiny root nubs visible. Offset right, filling ~45% of the frame, clean negative space on the left. Warm light on the crown, cool blue-grey background. A bold red DASHED circle around the base and ONE curved bright yellow arrow pointing to it.
TEXT — the ONLY text is exactly two lines in the left negative space: line 1 "DRY 1 WEEK" in bright YELLOW; line 2 "BEFORE SOIL" in WHITE. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow. Render exactly, no other text anywhere.
```

---

## 🍋 061 — Lemon Tree Won't Flower? Light Hours Extension Guides Actually Recommend · 20′ · AVD 14 % · CTR 1,33 %
⚠️ Đổi gói chỉ sửa được CTR. AVD 14 % ở bản 20′ là giới hạn riêng; đừng kỳ vọng ngang Pineapple.

**Đã loại:** "Stop Feeding Your Lemon Tree in Winter…". Khung này hợp L20 nhưng phạm điều kiện ④: mẹo bón phân chỉ xuất hiện ở lý do số 2 (khoảng phút 3), không chứng minh trong 20 giây đầu. Ba gói dưới đây đều hứa đúng thứ video nói ở giây 0–40: 5 nguyên nhân, và con số 6–8 giờ nắng.

| Gói | Tiêu đề (ký tự) | Khung | Lời hứa có trong video ở đâu |
|---|---|---|---|
| **A** ⭐ | No Flowers on Your Lemon Tree? Count This 1 Number Tomorrow (59) | Triệu chứng + số + việc làm được ngay | Giây ~30: "the number to remember is six to eight hours"; "a small job for tomorrow… a window and a clock" |
| **B** | Lemon Tree Won't Flower? It's One of These 5 Things (51) | Keyword đầu + danh sách | Giây ~10: "five things… Light. Feeding. Temperature. Age. And the move" |
| **C** | Lemon Trees Need 6 Hours of Sun to Flower. Does Your Window? (60) | Số + câu hỏi tự kiểm | Lý do 1 (Iowa State, Oregon State, Arkansas: 6–8 giờ) |

### Thumbnail
| Gói | Hình | Chữ VÀNG | Chữ TRẮNG |
|---|---|---|---|
| A | Cây chanh chậu cạnh cửa sổ, vệt nắng chéo, mặt đồng hồ lớn mờ phía sau | `6 HOURS?` | `OF DIRECT SUN` |
| B | Cây chanh ở giữa, 5 biểu tượng quanh cây (mặt trời · chai phân · nhiệt kế · cây non · thùng chuyển nhà) | `5 SUSPECTS` | `#1 = LIGHT` |
| C | Before→after: cửa sổ tối, cây xanh không nụ ❌ / cửa sổ sáng, cành có hoa trắng ✅ | `2 HRS vs 7 HRS` | `NO BUDS?` |

**Prompt Lemon A:**
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel. Vivid saturated colors, ultra high contrast. NO human face, no person.
SCENE: ONE hero object — a potted lemon tree with glossy green leaves and NO flowers, standing beside a bright window, a strong diagonal beam of direct sunlight falling on half of the tree. Offset right, filling ~45% of the frame, clean negative space on the left. Behind the tree, a large soft-focus analog wall clock face. Warm sunlight on the leaves, cool blue room shadow for contrast. A bold red DASHED circle around the sunlit patch and ONE curved bright yellow arrow pointing to it.
TEXT — the ONLY text is exactly two lines in the left negative space: line 1 "6 HOURS?" in bright YELLOW; line 2 "OF DIRECT SUN" in WHITE. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow. Render exactly, no other text, numbers or letters anywhere (no numbers on the clock).
```

**Prompt Lemon B:**
```
A photorealistic 16:9 YouTube thumbnail for a US home-gardening channel. Vivid saturated colors, ultra high contrast. NO human face, no person.
SCENE: a potted lemon tree with green leaves and no flowers in the center-right, filling ~40% of the frame. Around it, five simple bold flat icons in white circles with thin black outline: a sun, a fertilizer bottle, a thermometer, a small seedling, a cardboard moving box. The sun icon is larger and ringed in bright yellow. Clean warm background, strong contrast.
TEXT — the ONLY text is exactly two lines on the left: line 1 "5 SUSPECTS" in bright YELLOW; line 2 "#1 = LIGHT" in WHITE. Very thick bold sans-serif, ALL CAPS, heavy black outline and drop shadow. Render exactly, no other text anywhere.
```

Gói C có hoa trắng trên thumbnail. Script không hứa chắc sẽ ra hoa ("directions, not guarantees"), nên đây là ảnh minh hoạ kết quả mong muốn. Nếu muốn chặt hơn thì dùng A hoặc B.

---

## Cách test (bạn làm trong Studio)
1. **Thứ tự:** Pineapple trước, Lemon sau.
2. **Test & Compare thumbnail:** chạy A vs B. Nếu Studio có test tiêu đề thì test thêm cả tiêu đề cùng gói.
3. **Chờ** Studio báo kết quả, hoặc đủ ≥ 5.000 impressions mỗi bên. Ghi CTR giờ 48 và kết quả vào `references/thumbnail-stats-garden-us-60k.md` mục A/B RESULTS LOG.
4. **Tuần sau:** export Studio 28 ngày bỏ vào `research/studio/`, rồi chạy `tools/dna_kenh.py do` để xem impressions có tăng lại không.
