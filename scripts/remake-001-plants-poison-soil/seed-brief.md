# Seed Brief — remake-001-plants-poison-soil

**Seed:** `ey3nmNWotKI` · https://www.youtube.com/watch?v=ey3nmNWotKI · kênh **Walt Greer Secrets** (`UCRaMz9Np-zQXrpVWRQks4-g`) · đăng 2026-09-13
**Đường vào:** ☑ **B** — user đưa link video kèm ý định làm bản của mình

---

## 1. Tái thẩm seed (R1) — đo lại tại thời điểm bắt đầu video

| Chỉ số | Cách lấy | Hôm nay | Ngưỡng | Đạt? |
|---|---|---|---|---|
| `monthly_growth_pct` | `vidiq_video_stats granularity:"daily"` — 5 ngày gần nhất: 3,742→3,969→4,014→3,787→3,742 | **~0%** (đi ngang, giảm nhẹ) | ≥5% ✅ · 1-5% ⏳ · <1% ❌ | ❌ FAIL |
| `view / sub` | 3,741 / 7,990 | **0.47×** | ≥5× | ❌ FAIL |
| `breakoutScore` | không nổi bật so với trung bình kênh (~7,830 view/video) — thấp hơn ~52% | thấp | ≥15 | ❌ FAIL |
| Sub kênh gốc | vidiq_channel_stats | 7,990 | <50K | ✅ PASS |
| Tuổi seed | 2026-09-13 → 2026-09-21 | 8 ngày | 60-150 ngày | ❌ (quá mới để đạt ngưỡng lý tưởng, nhưng đã đủ thấy đường cong tắt sớm) |
| Số clone đã đăng (14 ngày, `vidiq_similar_videos` title-match) | 10 kết quả gần nhất, KHÔNG có video nào trùng khái niệm "plants poisoning soil/allelopathy" | 0 clone trực tiếp | ≤2 | ✅ PASS |
| Đường cong | daily stats: tăng vọt 3 ngày đầu (48→209→2,326→3,742) rồi TẮT HẲN, đi ngang/giảm nhẹ 5 ngày sau | ☑ **CHÁY NHANH rồi TẮT** (không phải NỞ) | NỞ / vừa qua đỉnh | ❌ FAIL |

**Verdict R1:** ☐ PASS · ☐ FAIL → chuyển seed khác · ☑ **OVERRIDE**

### 🟡 Khối OVERRIDE

| | |
|---|---|
| Tiêu chí trượt | `monthly_growth_pct` ~0% (<1%) · `view/sub` 0.47× (<5×) · đường cong đã tắt hoàn toàn sau ngày 3, không phục hồi |
| Lý do đánh đổi | Video KHÔNG phải outlier đang được đẩy, nhưng góc nội dung (allelopathy — cây "đầu độc" đất xung quanh) là chủ đề khoa học thật, mạnh, kênh Garden US CHƯA từng làm; cơ chế walnut/juglone có bằng chứng .edu/.gov vững, khớp FACELESS WEDGE. Kênh nguồn (Walt Greer Secrets) tự thân đang tăng trưởng khỏe (+9.6% sub/tháng) dù video này cụ thể không phải hit. User chấp nhận đây là thử nghiệm mở rộng nội dung, không dựa trên bằng chứng thị trường của chính seed. |
| Rủi ro chấp nhận | Không có tín hiệu "nhu cầu đang tăng" thật — có thể remake ra 1 video hiệu suất trung bình/thấp tương tự bản gốc. |
| **Câu hỏi cho retro** | Nếu `views_5d` ≥ `median_5d_views` (285) dù seed gốc đã tắt đà tăng từ đầu, điều đó cho thấy nội dung/archetype A5 (category verdict khoa học) có thể tự đứng vững không cần bằng chứng seed mạnh — có nên nới ngưỡng R1 cho các seed có lõi khoa học xác minh được (kiểu juglone) dù đường cong view yếu? |
| User duyệt | 2026-09-21 — override qua AskUserQuestion ("Override — vẫn chạy Lane B remake") |

---

## 1.5. 🔴 PHÂN LOẠI ARCHETYPE

| # | Câu hỏi | Trả lời |
|---|---|---|
| Q1 | Payoff về mặt vật lý là gì? | ☑ **phán quyết danh mục — A5** (mức độ nguy hiểm theo tiêu chí "dose/distance-dependent", không phải liệt kê mù) |
| Q2 | Thân bài có đánh số (≥8 mục)? | ☑ Có — 10 mục → listicle (A1/A2/A5) |
| Q3 | Seed đặt payoff ở đâu? | ☑ **đầu** (walnut = #1, mở ngay từ đầu) → bắt buộc lời hứa thứ hai — **đã có sẵn trong seed**: "hai thứ quan trọng không kém list — cây bị oan (competing chứ không poisoning) + myth phổ biến nhất" |
| Q4 | Tài sản có hạn sử dụng? | ☐ Không (không phải seasonal) |
| Q5 | Seed từ ngách khác? | ☐ Không (cùng ngách gardening) |

**ARCHETYPE ĐÃ CHỐT:** `A5` — Category Verdict/Ranking
**Archetype bị loại + lý do:** A4 (Mistake/Prohibition) — tài sản không phải "lệnh cấm" mà là phán quyết mức độ · A1 (Sensory Heritage) — không có yếu tố hoài niệm/giác quan lịch sử · A10 (Mechanism Explainer) — có ≥8 mục đánh số rõ (listicle), không phải chuỗi 3-4 tiết lộ đơn tuyến.
**Bằng chứng của gói này:** ☑ 🟡 suy ra (chưa chạy thật ở lane B — theo `channel.config.json`, evidence: "inferred") → **ghi vào `prediction.md` là TEST KHUÔN**

### ⛔ Kiểm SEED PHẢI BỎ (§4)

☐ X1 (conspiracy) — "phần garden center không có lý do để nhắc" chỉ là khung "kiến thức bị lãng quên", KHÔNG tới mức "they're hiding this/banned/government" → không trúng
☐ X3 (health-fear/YMYL) — chủ đề cây hại cây, không phải sức khỏe người → không trúng
☐ X5 (persona tự-test) — bản remake viết lại 100% theo narrator educator riêng của Garden US → không kế thừa
☐ L9 (tuổi trong title) — không có → không trúng
☐ X4 (cơ chế nguy hiểm) — thông tin, không có hướng dẫn nguy hiểm → không trúng
☐ Không đổi được trục nào — có (xem mục 3)

**→ Seed KHÔNG trúng SEED PHẢI BỎ. Đủ điều kiện đi tiếp (với OVERRIDE ở R1).**

---

## 2. Tài sản đã-trả-tiền (R2)

| Mảnh | Trong seed gốc | Trong bản của ta |
|---|---|---|
| 🔒 **Tài sản** (cụm phán quyết A5) | Phân biệt THẬT giữa cây **đầu độc bằng hóa chất** (allelopathy) vs cây **chỉ cạnh tranh/lấn át** (competition) — dùng phép thử đào đất kiểm tra rễ để tự chẩn đoán | **GIỮ NGUYÊN khái niệm + phép thử đào đất** — đây là góc khác biệt nhất, hiếm kênh gardening nào làm rõ phân biệt này |
| Mảnh mutate #1 | Danh mục 10 cây gồm cả eucalyptus/lantana (thiên khí hậu ấm/Úc, ít phổ biến toàn nước Mỹ) | Ưu tiên cây phổ biến toàn quốc Mỹ hơn (walnut giữ nguyên #1 — bằng chứng khoa học mạnh nhất, không đổi); deep-research [1.5] xác nhận lại danh sách 10 cây, chỉ giữ cây có nguồn allelopathy thật |
| Mảnh mutate #2 | Từ "poison" hơi overclaim (chính kênh nguồn cũng tự cảnh báo trong caveat + note lạ trong description) | Giữ từ "poison/poisoning" ở title (đã quen thuộc, không phải blacklist) NHƯNG nội dung phải hedge dose/distance-dependent rõ ràng từ đầu (đúng X2 hard gate của A5) |

⛔ Hard fail: không được đổi/xoá khái niệm "phân biệt đầu độc vs cạnh tranh" khỏi title/thumbnail.
⛔ Hard fail ngược: phải mutate được danh mục 10 cây + khung từ ngữ overclaim — không re-upload nguyên xi.

---

## 3. Đổi MỘT trục (R3)

**Trục đã đổi:** ☑ **vật chủ** (danh mục 10 cây cụ thể)

| | Bên **seed** | Bên **ta** |
|---|---|---|
| Giá trị trên trục đã đổi | 10 cây: walnut, tree of heaven, Norway maple, garlic mustard, Japanese knotweed, bracken fern, tall fescue, sunflower, eucalyptus, lantana | Giữ walnut (#1, anchor khoa học mạnh nhất, KHÔNG đổi) + deep-research xác nhận lại 9 cây còn lại theo mức phổ biến với khán giả Mỹ làm vườn sân sau/container — loại cây nào không tìm được nguồn allelopathy thật (KHÔNG bịa) |
| Người Mỹ 60-80 có ký ức để móc vào? | Không rõ (kênh Anh/quốc tế) | ☑ Có — walnut tree là hình ảnh sân sau kinh điển ("that walnut tree my dad planted"), có thể móc vào ký ức đa thế hệ |
| Đơn vị đo | feet (50-80 ft) — đã là đơn vị Mỹ | Giữ nguyên feet/pound |

**Các trục KHÔNG đổi:** ngôn ngữ (EN), format (10-item listicle + payoff đầu + twist "cây bị oan + myth" cuối), cơ chế khoa học cốt lõi (allelopathy thật), phép thử đào đất phân biệt đầu độc vs cạnh tranh.

---

## 4. Ba title candidate → 🔴 GATE 0

| | Title | Tài sản nguyên văn? | vidiq_score_title |
|---|---|---|---|
| A | `10 Garden Plants Secretly Poisoning the Soil Around Them` | Giữ "poisoning soil" | 87 |
| B | `The Backyard Tree Poisoning Everything Within 80 Feet (Plus 9 More)` | Giữ walnut-anchor + "80 feet" | 88 |
| **C ⭐** | `10 Plants Poisoning Their Neighbors (And the Soil Myth That Isn't True)` | Giữ "poisoning" + bake sẵn lời hứa thứ hai (myth) vào title | **94** |

⛔ L9/L9b: không dùng tuổi người xem — cả 3 title đều sạch.
**Đề xuất:** Title C — điểm cao nhất, đồng thời title tự chứa lời hứa thứ hai (myth reveal) nên không cần giấu quá kỹ, giảm rủi ro clickbait-không-giao (L3).

**Title đã chọn:** Title C — `10 Plants Poisoning Their Neighbors (And the Soil Myth That Isn't True)` (duyệt 2026-09-21)
**Ghi chú thumbnail:** FACELESS · walnut/cây cụ thể làm vật chính · chữ 2 tầng: vàng = "POISONING" (tài sản), trắng = mảnh mutate (vd "10 PLANTS" hoặc con số feet).

---

## 5. Định dạng theo gói archetype A5 (R4)

| | Gói quy định | Video này |
|---|---|---|
| Bộ xương | Đếm ngược 10-15 mục, tiêu chí xếp hạng nói rõ trước mục đầu | 10 mục, mở bằng tiêu chí "không phải cây nào cũng nguy hiểm như nhau — dose/distance-dependent" trước khi vào walnut |
| Số mục / beat | 10 mục, 4 nhịp/mục (nó là gì → con số khiến nó xếp hạng đó → ai KHÔNG nên chọn nó → bắc cầu) | 10 mục giữ nguyên (sau khi deep-research xác nhận/thay 1-2 cây) |
| Vị trí payoff | payoff_position: 1 | walnut = #1, giữ nguyên |
| Độ dài mục tiêu | 14-18' (theo config A5, 🟡 TEST CÓ KIỂM SOÁT — video_length chuẩn kênh 8-10') | **Dùng 8-10' chuẩn kênh** (KHÔNG áp dụng ngoại lệ 14-18' — seed đã yếu ở R1, không nên cộng thêm rủi ro L7 dài) |
| Spine template | `templates/retention-spine-listicle.template.md` | Dùng bản này ở [2.5] |
| Cơ chế trả nợ | Lời hứa thứ hai (payoff đầu → giữ chân bằng "cây bị oan + myth" ở cuối) | Giữ nguyên — đây là tài sản retention chính |

**Hệ quả cho các bước sau:**
- [2] hook: SSSQ giữ nguyên; PHẢI gieo lời hứa thứ hai <55s ("2 điều quan trọng không kém list ở cuối video") theo đúng cơ chế trả nợ của gói.
- [2.5] spine: dùng `retention-spine-listicle.template.md`, kẻ theo MỤC, micro-bridge 100% ranh giới.
- [3] Pha D: thêm phép đếm `criteria_stated_before_first_item` + `numbers ≥ items` (mỗi mục có ≥1 số chứng minh thật).
- [3] R7: X2 hard gate — cấm tuyệt-đối-hoá ("every plant", "always kills") — mỗi thứ hạng phải khoanh vùng "theo dose/distance nào".
- [6] retro: chấm bằng `views_5d` vs `median_5d_views` (285) + tổng giờ xem. ⛔ KHÔNG chấm bằng AVD. Vì gói 🟡 → `prediction.md` ghi TEST KHUÔN, retro phải trả lời câu hỏi OVERRIDE ở mục 1.

---

## 6. Bàn giao sang [1.5] deep-research

| | |
|---|---|
| Tải trọng theo gói | A5: 2 fact/mục (1 số xếp hạng có nguồn .edu/.gov + 1 chi tiết nhận dạng/cách xử lý) × 10 mục |
| Tổng fact cần nguồn | ~20 fact, ưu tiên xác minh trực tiếp: walnut/juglone (nguồn mạnh nhất, phải verify bán kính 50-80ft), tree of heaven/allelothone, Norway maple, garlic mustard/mycorrhizal, Japanese knotweed, bracken fern, tall fescue, sunflower hulls, + xác minh eucalyptus/lantana có phù hợp audience Mỹ không hay cần thay |
| Model | `sonnet` |
| Cách chạy | `garden-deep-researcher` theo lô 5 mục (đúng chuẩn A1/A2/A5) |
| Câu hỏi bắt buộc của gói | (1) Xác minh bán kính ảnh hưởng walnut/juglone qua nguồn extension .edu thật · (2) Với mỗi cây còn lại, tìm nguồn thật cho allelopathy (không suy diễn từ "invasive" = "allelopathic") · (3) Pine needle myth + mint/ivy competition-vs-poisoning distinction có đúng khoa học không · (4) Cây nào trong 10 cây gốc KHÔNG phổ biến ở Mỹ (đặc biệt eucalyptus/lantana) → cần thay cây tương đương có nguồn allelopathy thật và phổ biến hơn với khán giả Mỹ 60-80 tuổi · (5) Danh sách cây CHỊU ĐƯỢC dưới walnut (tolerant list) — xác minh nguồn |

⛔ Fact không tra được nguồn → `[NEED DATA: ...]`. Không bịa năm/tổ chức/số liệu.
