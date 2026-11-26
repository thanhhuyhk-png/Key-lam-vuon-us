# Research Brief — 7 No-Dig Perennials for September That Come Back Every Year

> Agent: garden-deep-researcher | Model: claude-sonnet-4-6 | Date: 2026-08-20

**7 candidate plants:** hosta, daylily (Hemerocallis), coreopsis (threadleaf — C. verticillata), sedum/stonecrop (Hylotelephium spectabile 'Autumn Joy' type), black-eyed susan (Rudbeckia fulgida), Russian sage (Perovskia/Salvia yangii), lavender (Lavandula angustifolia).

---

## Câu hỏi 1: Giá thật 2026 (Home Depot/Lowe's) — perennial quart vs annual mỗi mùa xuân

**Findings:**
- Home Depot lists a **1.0 qt. Perennial Hosta 'Whirlwind' (2-Pack)** at **$33.93 per package = $16.97 per plant**. (Home Depot product listing, via search index, 2026) — https://homedepot.com/p/1-0-qt-Perennial-Hosta-Whirlwind-2-Pack-1334/319855645
  → Action: mua 1 lần vào tháng 9 → Benefit: không phải mua lại năm sau.
- Home Depot **6-Pack Easy Wave Petunia (annual)**: **$26.98 = $4.50/plant**; a comparable Impatiens 6-pack runs **$32.84–$44.37 = $5.47–$7.40/plant**. (Home Depot product listings, via search index, 2026) — https://www.homedepot.com/p/EASY-WAVE-6-Pack-Red-Easy-Wave-Petunia-Annual-Plant-with-Red-Flowers-2781/324239691
  → Action: so sánh — annual rẻ hơn/plant lúc mua, nhưng phải mua lại MỖI mùa xuân → Benefit: sau 3 mùa xuân, annual ($4.50-7.40 x 3 = $13.50-$22.20) tốn ngang hoặc hơn 1 perennial mua 1 lần ($8-17).
- **[NEED DATA: giá chính xác thời gian thực]** — Cả Lowe's (lowes.com) và Home Depot (homedepot.com) đều chặn bot fetch trực tiếp (HTTP 403 trên mọi product page cố truy cập trực tiếp — đã thử 6 lần, cả 2 domain). Số liệu trên lấy từ index/snippet của search engine, KHÔNG phải giá live đã tự tay đọc trên trang. Cần **script writer hoặc user tự mở Lowe's.com/HomeDepot.com kiểm tra giá quart-size thật của daylily, sedum, coreopsis, Russian sage, black-eyed susan trước khi đưa số cụ thể vào script** — giá dao động theo mùa/khu vực/store.

**Kết luận dùng được cho script (an toàn, không cần số chính xác tuyệt đối):**
- Nguyên tắc "1 lần mua vs mua lại mỗi năm" là ĐÚNG về mặt cấu trúc chi phí (perennial = one-time cost ~$8-17/plant; annual = recurring cost ~$4.50-7.40/plant MỖI mùa xuân) — dùng framing "trong 3 mùa xuân, annual tốn bằng hoặc hơn perennial" thay vì chốt 1 con số đô-la tuyệt đối chưa verify.
- ⚠️ KHÔNG dùng con số "$16.97" hay "$4.50" như fact cứng trong script nếu chưa verify lại — dùng làm ballpark/order-of-magnitude, hoặc thay bằng câu chung "a quart-size perennial runs about the same as one restaurant coffee — but you only buy it once."

---

## Câu hỏi 2: Zone 4 container overwintering — cây nào có bằng chứng .edu/.gov xác nhận (QUAN TRỌNG NHẤT)

**Findings:**

**A. Quy tắc buffer container (nguồn .edu xác nhận):**
- University of Illinois Extension (2014): *"Go two Zones colder. Picking perennials that are rated two zones colder than your own will greatly reduce the amount of effort required to protect plants from cold temperatures."* — https://extension.illinois.edu/blogs/hort-home-landscape/2014-11-10-overwintering-perennial-patio-containers
  → Action: chọn cây có zone rating THẤP HƠN zone vườn 2 bậc để trồng chậu an toàn → Benefit: giảm công bảo vệ mùa đông.
- University of Maryland HGIC (qua Ask Extension, 2020): xác nhận ĐỘC LẬP cùng quy tắc — *"you can overwinter perennials that are winter hardy in two zones colder"* (ví dụ: ở zone 7, chọn cây hardy tới zone 5). — https://ask.extension.org/kb/faq.php?id=721081

**B. Bằng chứng CỤ THỂ zone 4 (Hennepin County Extension, Minnesota — zone 4b, thảo luận ĐÚNG các cây này):**
- Câu hỏi gốc từ Hennepin County (Minnesota, zone 4b) hỏi về daylily, black-eyed susan, lavender, Shasta daisy TRONG CHẬU. Chuyên gia extension trả lời: *"just because something is listed as hardy in your zone does not mean it is hardy in a container in your zone."* Và: *"Even heavily mulched the plants may not survive, especially if we have a harsh winter."* Lavender được nêu riêng: chỉ hardy chắc chắn từ zone 5+, cần bảo vệ thêm hoặc đem vào nhà ở zone 4b. — https://ask.extension.org/kb/faq.php?id=371280

**C. USDA zone rating từng cây (North Carolina Extension Gardener Plant Toolbox — .edu, đã WebFetch trực tiếp từng trang):**
| Cây | Zone (NC State Extension) | Buffer so với zone 4 (chậu) |
|---|---|---|
| Hosta | 3a–9b | 1 zone (không đủ buffer "2 zones" khuyến nghị) |
| Daylily (Hemerocallis) | 3a–9b | 1 zone |
| Sedum 'Autumn Joy' (Hylotelephium spectabile) | 3a–10b | 1 zone |
| Coreopsis verticillata (threadleaf) | 3a–9b | 1 zone |
| Black-eyed Susan (Rudbeckia fulgida) | 3a–9b | 1 zone |
| Russian sage (Perovskia) | 4–9 (Wisconsin Extension) | 0 zone — KHÔNG có buffer |
| Lavender (Lavandula angustifolia) | 5a–9b (USU + NC State) | ÂM — không sống nổi zone 4 kể cả trồng đất |

Nguồn: https://plants.ces.ncsu.edu/plants/hosta/ · https://plants.ces.ncsu.edu/plants/hemerocallis/ · https://plants.ces.ncsu.edu/plants/hylotelephium-spectabile-autumn-joy/ · https://plants.ces.ncsu.edu/plants/anacis-verticillata/ · https://plants.ces.ncsu.edu/plants/rudbeckia-fulgida/ · https://hort.extension.wisc.edu/articles/russian-sage-perovskia-atriplicifolia/ · https://plants.ces.ncsu.edu/plants/lavandula-angustifolia/ · https://extension.usu.edu/yardandgarden/research/english-lavender-in-the-garden

**⚠️ KẾT LUẬN QUAN TRỌNG — RỦI RO CỦA LỜI HỨA GỐC ("Number 3 survives zone 4 winters — even in a pot"):**

Không tìm được nguồn .edu nào xác nhận TRỰC TIẾP "cây X sống sót thành công qua đông trong chậu ở zone 4" như một kết quả đã kiểm chứng/thử nghiệm cho BẤT KỲ cây nào trong 7 cây. Bằng chứng tốt nhất tìm được là suy luận từ 2 lớp: (1) zone rating buffer, và (2) hướng dẫn extension trực tiếp về rủi ro chậu ở đúng zone 4b (Minnesota) — và nguồn đó nói RÕ ngay cả cây hardy zone 3 cũng "may not survive" trong chậu nếu mùa đông khắc nghiệt, dù đã mulch kỹ.

**Về sedum cụ thể (Claim B trong brief gốc):** Bằng chứng của sedum KHÔNG yếu hơn 4 cây còn lại — Sedum 'Autumn Joy' (Hylotelephium spectabile) được NC State Extension xác nhận zone 3a–10b, ngang hàng hosta/daylily/coreopsis/black-eyed susan (đều zone 3a). **Không cần thay sedum bằng Russian sage hay coreopsis** — Russian sage thực ra YẾU HƠN sedum về zone buffer (Russian sage chỉ zone 4, buffer = 0; sedum zone 3, buffer = 1). Nếu phải chọn 1 cây "chắc ăn nhất" trong 5 cây zone-3, cả 5 đều ngang nhau về mặt rating — không có cây nào nổi trội hơn theo dữ liệu tìm được.

**Khuyến nghị cho script (bắt buộc để giữ compliance/không overclaim):**
- KHÔNG dùng câu tuyệt đối "survives zone 4 winters even in a pot" mà không kèm điều kiện.
- Đổi lời hứa thành có điều kiện, dựa đúng trên nguồn: *"Number 3 is rated a full zone hardier than what this zone needs — and Extension offices agree: bury the pot or mound mulch over it, and that's your best shot at zone 4 in a container."* (giữ đúng tinh thần "khoa học xác nhận" nhưng không hứa quá).
- Chọn 1 trong 5 cây zone-3 (hosta / daylily / sedum / coreopsis / black-eyed susan) cho vị trí "Number 3" — sedum vẫn dùng được, không cần đổi.
- LOẠI Russian sage và lavender khỏi bất kỳ lời hứa liên quan "zone 4 pot" — cả hai đều thiếu buffer theo nguồn.

---

## Câu hỏi 3: Độ sâu trồng (inch) + số tuần trước sương giá — cây nào nông nhất/ít thể lực nhất

**Findings:**
- **Daylily:** phủ 1 inch đất lên củ/crown. (North Carolina Extension Gardener Plant Toolbox, đã WebFetch) — https://plants.ces.ncsu.edu/plants/hemerocallis/
  → Action: đặt crown, phủ 1 inch đất → Benefit: không cần đào hố sâu.
- **Sedum:** trồng sâu 0.5–1 inch; đặt mặt bầu rễ ngang mặt đất xung quanh. (Growing guides tổng hợp — Tier 4-5, KHÔNG có nguồn .edu nêu số inch cụ thể; đã search 3 lần không ra .edu) — cross-check với hình thái rễ sedum (rễ cạn, mọng nước) hợp lý về mặt sinh lý học.
  → Action: xới nhẹ mặt đất 1 inch, đặt cây, ấn nhẹ → Benefit: không cần cúi sâu, không cần xẻng, phù hợp người ngồi ghế thấp.
- **Coreopsis (rễ trần):** đào hố sâu 3-4 inch, đặt crown ngang mặt đất. (Eden Brothers planting guide — Tier 4-5, không có nguồn .edu nêu số inch cụ thể sau 3 lần search) — [NEED DATA: nguồn .edu cho độ sâu coreopsis].
- **Hosta, Russian sage, Black-eyed Susan, Lavender (cây quart/gallon đã có sẵn trong chậu):** quy tắc chung "trồng ngang độ sâu bầu rễ trong chậu nursery" — đây là quy tắc phổ biến trên mọi nguồn (kể cả Wisconsin Extension cho Russian sage: *"setting them at the same depth as they were in the pot"* — https://hort.extension.wisc.edu/articles/russian-sage-perovskia-atriplicifolia/). Với chậu quart/gallon tiêu chuẩn, độ sâu hố thường ~4-6 inch — SÂU HƠN sedum/daylily đáng kể, đòi hỏi xẻng và cúi người nhiều hơn.

**Weeks trước sương giá đầu (áp dụng 6/7 cây, xem Consensus Principle #1 bên dưới):** tối thiểu 4 tuần, lý tưởng 6 tuần trước frost đầu tiên.

**KẾT LUẬN — cây NÔNG NHẤT / ít thể lực nhất:** **Sedum (0.5–1 inch)** là ứng viên rõ nhất cho lời hứa "plant sitting in a chair, not bent over a shovel" — độ sâu nông hơn hẳn daylily (1 inch nhưng cần đặt củ đúng hướng) và nông hơn NHIỀU so với hosta/Russian sage/black-eyed susan/lavender (phải đào hố bằng độ sâu chậu nursery, ~4-6 inch). Tuy nhiên số liệu 0.5-1 inch cho sedum là Tier 4-5 (consensus nhiều growing guide, KHÔNG có .edu trực tiếp nêu con số inch) — nên diễn đạt hedge: *"most growers plant sedum barely below the surface — under an inch"* thay vì trích dẫn như số liệu university.

---

## Câu hỏi 4: Độc tính thú cưng + USDA zone chính xác + kiểm tra exotic/niche

**Findings:**

| Cây | Độc với mèo? | Độc với chó? | USDA Zone (.edu) | Nguồn |
|---|---|---|---|---|
| **Daylily (Hemerocallis)** | ⚠️ **CÓ — nghiêm trọng** | Không | 3a–9b | ASPCA + NC State (đã WebFetch cả 2) |
| **Hosta** | ⚠️ Có (nhẹ hơn daylily) | ⚠️ Có | 3a–9b | ASPCA + NC State (đã WebFetch cả 2) |
| Lavender | Có (mức độ thấp) | Có (mức độ thấp) | 5a–9b | NC State (đã WebFetch) |
| Coreopsis | Không | Không | 3a–9b | NC State (đã WebFetch) |
| Russian sage | Không | Không | 4–9 | ASPCA (đã WebFetch trực tiếp) + Wisconsin Extension |
| Sedum | Không (theo tổng hợp — xem ghi chú) | Không | 3a–10b | ASPCA (tổng hợp qua search index, CHƯA WebFetch trực tiếp trang ASPCA riêng cho Sedum) |
| Black-eyed Susan (Rudbeckia) | Không có trong danh sách độc ASPCA | Không (kích ứng nhẹ nếu ăn nhiều lá gai) | 3a–9b | Tổng hợp qua search (CHƯA WebFetch trực tiếp trang ASPCA riêng) |

**⚠️⚠️ YMYL — DAYLILY ĐỘC VỚI MÈO (đã verify kỹ theo yêu cầu):**
ASPCA (đã WebFetch trực tiếp): *"Vomiting, inappetence, lethargy, kidney failure, death."* Toàn bộ cây (thân, lá, hoa, phấn hoa, cả nước bình cắm hoa) đều độc. Chỉ cần ăn 1 lượng nhỏ lá hoặc cánh hoa, hoặc liếm phấn hoa dính lông khi tự chải lông, có thể gây suy thận cấp tử vong trong vòng CHƯA ĐẦY 3 NGÀY. Mèo là loài DUY NHẤT được ghi nhận bị ảnh hưởng (chó an toàn). — https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants/day-lilies-many-varieties
→ **BẮT BUỘC gắn cảnh báo ⚠️ rõ ràng trong script tại đoạn giới thiệu daylily** — đây là an toàn thật, không phải formality. Khuyến nghị câu dạng: *"If you have a cat, this one needs a fenced bed or a container out of paw's reach — daylily is one of the most dangerous plants for cats, full stop."*

**Hosta — toxicity bổ sung cần biết:** ASPCA (đã WebFetch): độc với CẢ mèo, chó, VÀ ngựa (saponins → nôn, tiêu chảy, uể oải). Không nguy hiểm chết người như daylily nhưng vẫn cần 1 câu cảnh báo ngắn nếu script nhắc hosta gần vị trí có thú cưng.

**Kiểm tra exotic/niche:** Cả 7 cây đều CỰC KỲ phổ biến tại Mỹ — xác nhận có bán sẵn tại cả Home Depot và Lowe's (tìm thấy product listing cho tất cả 7 cây ở cả 2 nhà bán lẻ trong quá trình research). Không có cây nào cần gắn cờ "exotic/niche."

**[NEED DATA]:** Chưa WebFetch trực tiếp trang ASPCA riêng cho Sedum và Rudbeckia (chỉ có qua tổng hợp search index — đa số nguồn thứ cấp trích dẫn ASPCA đồng thuận "non-toxic," nhưng khuyến nghị double-check trực tiếp trên aspca.org/pet-care/animal-poison-control/cats-plant-list và dogs-plant-list trước khi in câu "100% safe" vào script.

---

## Câu hỏi 5: Đồng thuận "bao nhiêu tuần trước sương giá" — có áp dụng đều cho cả 7 cây không

**Findings — xem Consensus Principle #1 bên dưới cho tổng hợp đầy đủ.**

Áp dụng ĐỀU cho 6/7 cây (hosta, daylily, sedum, coreopsis, black-eyed susan, Russian sage) — đây là nguyên lý sinh lý học rễ chung cho perennial thân thảo, không đặc thù theo loài trong các nguồn đã tìm.

**NGOẠI LỆ: Lavender.** Nhiều growing guide (Tier 4-5, KHÔNG có .edu trực tiếp xác nhận sau 2 lần search) khuyên KHÔNG trồng lavender vào mùa thu ở zone lạnh (zone 1-6) — nên trồng mùa XUÂN, sau khi hết sương giá cuối, vì rễ lavender cần nhiều thời gian/nhiệt hơn cửa sổ 6 tuần để đủ chắc qua đông đầu tiên. — Đây là lý do bổ sung (ngoài việc không đủ hardy zone 4) để loại lavender khỏi lời hứa chính của video, hoặc đóng khung lavender như "bonus cho zone 5+ only, trồng xuân thay vì thu."

---

## Consensus Principles (3 — nguyên liệu authority cho script)

### 1. Quy tắc "6 tuần trước sương giá đầu" (Claim A — đã verify lại đầy đủ)

**Nguyên tắc thực tế:** Trồng perennial mùa thu cần TỐI THIỂU 4 tuần, LÝ TƯỞNG 6 tuần trước ngày sương giá đầu tiên trung bình của khu vực — đủ thời gian để rễ bén trước khi đất đóng băng.

- **Hội tụ:** University of Illinois Extension (6 tuần) · Clemson HGIC (tối thiểu 6 tuần trước "hard-freezing weather") · University of Vermont Extension (tối thiểu 1 tháng) · Colorado State PlantTalk (không dưới 1 tháng) — cả 4 đều đồng ý hướng: sớm hơn = tốt hơn, và có một ngưỡng tối thiểu rõ ràng trước khi đất đóng băng.
- **Khác nhau:** Illinois và Clemson dùng con số cụ thể "6 tuần"; UVM và Colorado State dùng ngưỡng thận trọng hơn "tối thiểu 1 tháng" (không nói rõ 6 tuần là bắt buộc, chỉ là "càng sớm càng tốt"). → Dùng "6 tuần" làm con số chính (2 nguồn .edu độc lập nêu đúng số này), có thể nói thêm "at minimum a month" như ngưỡng an toàn thấp nhất.
- **URLs:** https://extension.illinois.edu/news-releases/establishing-perennials-early-fall · https://hgic.clemson.edu/factsheet/growing-perennials/ · https://www.uvm.edu/extension/news/planting-perennials-fall · https://planttalk.colostate.edu/topics/annuals-perennials/1017-perennials-plant

### 2. Container hardiness cần buffer zone — "hardy in the ground ≠ hardy in a pot" (Claim B — đã verify, kết luận SỬA lại lời hứa gốc)

**Nguyên tắc thực tế:** Một chậu ngoài trời KHÔNG có lớp cách nhiệt của đất — Extension đồng thuận rằng cây trồng chậu cần được đánh giá như đang ở vùng LẠNH HƠN 1-2 zone so với zone thực tế của khu vườn, và ngay cả cây đạt buffer đó vẫn có thể chết nếu mùa đông khắc nghiệt và không được bảo vệ thêm (chôn chậu, phủ mulch dày, hoặc cất trong nhà kho không sưởi).

- **Hội tụ:** University of Illinois Extension ("go two zones colder") · University of Maryland HGIC qua Ask Extension ("hardy in two zones colder") · Hennepin County MN Extension qua Ask Extension (zone 4b, thảo luận đúng daylily/black-eyed susan/lavender trong chậu: "hardy in your zone does not mean hardy in a container in your zone", "may not survive... even heavily mulched").
- **Khác nhau:** Illinois/Maryland đưa ra công thức chung "2 zones colder"; nguồn Minnesota (đúng zone 4, đúng loại cây) nhấn mạnh RỦI RO THỰC TẾ hơn là công thức — ngay cả cây "đủ zone" cũng không đảm bảo 100%.
- **URLs:** https://extension.illinois.edu/blogs/hort-home-landscape/2014-11-10-overwintering-perennial-patio-containers · https://ask.extension.org/kb/faq.php?id=721081 · https://ask.extension.org/kb/faq.php?id=371280

### 3. English lavender = zone 5 tối thiểu, không phải zone 4 (Claim C — đã verify với nguồn mạnh hơn .edu)

**Nguyên tắc thực tế:** English lavender (Lavandula angustifolia) được XÁC NHẬN bởi 2 nguồn .edu độc lập là chỉ hardy từ zone 5 trở lên — KHÔNG dùng cho bất kỳ lời hứa "zone 4" nào trong script, kể cả trồng đất (chưa nói tới trồng chậu).

- **Hội tụ:** Utah State University Extension ("Climates suitable for lavender range from zones 5 to 10... English Lavender is hardy to zone 5") · North Carolina Extension Gardener Plant Toolbox (zone range 5a–9b, WebFetch trực tiếp).
- **Khác nhau:** Không có mâu thuẫn — cả 2 nguồn .edu đồng nhất zone 5 là ngưỡng dưới. (Nguồn Tier 4-5 gốc trong outline — epicgardening.com, bloomingexpert.com — giờ đã được THAY bằng 2 nguồn .edu mạnh hơn, không cần dùng nữa.)
- **URLs:** https://extension.usu.edu/yardandgarden/research/english-lavender-in-the-garden · https://plants.ces.ncsu.edu/plants/lavandula-angustifolia/

---

## Story Bank (2 mẩu — nguyên liệu scene, CÓ THẬT + có nguồn)

1. **Người tạo ra daylily được trồng nhiều nhất nước Mỹ** — Năm 1975, Walter Jablonski — một nông dân nuôi gà tây đã nghỉ hưu ở Merrillville, Indiana — lai tạo thành công giống daylily 'Stella de Oro,' giống daylily tái nở hoa (rebloom) đầu tiên trong lịch sử; trước đó mọi giống daylily chỉ nở đúng 1 đợt ngắn trong mùa hè. Cái tên "Stella de Oro" ghép từ tiếng Ý ("stella" = ngôi sao) và tiếng Tây Ban Nha ("de oro" = bằng vàng). Giống này giành giải Stout Award năm 1985 và trở thành daylily phổ biến nhất thế giới. (Sandoval County Extension Master Gardeners, qua WebFetch trực tiếp) — https://sandovalmastergardeners.org/stella-de-oro-daylily/
2. **Ruth Stout và khởi nguồn phương pháp "no-dig"** — Ruth Stout, sinh 1884 tại Kansas trong 1 gia đình Quaker làm nông, chuyển tới sống ở 1 nông trại tại Connecticut và làm vườn theo cách truyền thống suốt gần 15 năm trước khi chuyển sang phương pháp phủ mulch quanh năm thay vì cày/đào đất. Bà bắt đầu viết cho tạp chí Organic Gardening từ năm 1953, phổ biến triết lý "đất tự có lớp lá phủ hàng năm — không cần đào" ra khắp nước Mỹ, sống tới hơn 90 tuổi (mất 1980). (Homestead.org, qua WebFetch trực tiếp — lưu ý: bài không nêu chi tiết "người cày ruộng tới trễ" như truyền miệng phổ biến trên các nguồn khác chưa verify được) — https://www.homestead.org/gardening/ruth-stout-no-dig-duchess/

---

## YMYL Flags

- **⚠️ Daylily (Hemerocallis) — ĐỘC VỚI MÈO, có thể gây suy thận/tử vong.** Bắt buộc cảnh báo rõ trong script tại đoạn giới thiệu daylily, khuyến nghị chậu/vị trí ngoài tầm với của mèo hoặc gợi ý gọi ASPCA Poison Control (888-426-4435) nếu nghi ngờ mèo ăn phải. Nguồn: ASPCA + NC State Extension (đã WebFetch trực tiếp cả 2).
- **Hosta — độc với mèo, chó, VÀ ngựa** (saponin, gây nôn/tiêu chảy/uể oải — không đe dọa tính mạng như daylily nhưng vẫn cần 1 câu cảnh báo ngắn). Nguồn: ASPCA + NC State (đã WebFetch).
- **Lavender — độc tính nhẹ** với mèo/chó (nausea/vomiting, mức độ "low severity" theo NC State) — không cần cảnh báo nặng nhưng có thể nhắc thoáng qua nếu script có đoạn pet-safety tổng hợp.

---

## 🔒 QUYẾT ĐỊNH ORCHESTRATOR — gán lại thứ tự 7 mục theo research (outline gốc chỉ là đề xuất tạm)

Research phát hiện 2 điều buộc phải đổi so với outline nháp:
1. **Sedum** phù hợp nhất cho lời hứa **"trồng ngồi ghế"** (mục #7 — độ sâu 0.5-1", nông nhất trong 7 cây), KHÔNG phải lời hứa zone-4 như outline nháp gán.
2. **Lavender** chỉ hardy zone 5+ VÀ có khuyến nghị (Tier 4-5) nên trồng mùa XUÂN thay vì mùa thu ở zone lạnh — phải reframe thành "bonus zone 5+", không thể đứng chung mâm với lời hứa "trồng tháng 9" vô điều kiện.

**Thứ tự CHỐT (7 mục, dùng cho Hook/Spine/Script từ đây):**
1. Black-Eyed Susan — mở bài, độ nhận diện cao, không độc tính
2. Hosta — nostalgia (Comment Theme 1); ⚠️ độc nhẹ mèo/chó/ngựa — 1 câu cảnh báo ngắn
3. 🔒 Coreopsis — **lời hứa zone-4-pot (HEDGED)**: "rated a full zone hardier than zone 4 needs — bury the pot or mound mulch over it, that's your best shot." Không dùng cây có toxicity flag ở vị trí này để giữ beat gọn.
4. Daylily — ⚠️⚠️ **BẮT BUỘC safety callout độc mèo nghiêm trọng** (CR5, xem YMYL Flags) ngay tại đoạn giới thiệu
5. Russian sage — bonus deer-resistant (CR10, objection-handling)
6. Lavender — ⚠️ reframe rõ: "this one's a bonus if you're zone 5 or warmer — colder than that, save it for spring, not this September" (honest scoping, CR4)
7. 🔒 Sedum — **lời hứa "trồng ngồi ghế"**: độ sâu 0.5-1 inch (hedge Tier 4-5: "most growers plant sedum barely below the surface — under an inch"), đóng bài

**Giá đô-la dùng cho hook 0-20s:** dùng ballpark có nguồn thật (Home Depot listing, KHÔNG bịa) — hosta ~$17/plant (nguồn: Home Depot product listing) so với annual 6-pack ~$4.50-7.40/plant phải mua lại MỖI mùa xuân. Diễn đạt mềm: "around seventeen dollars" thay vì chốt cứng "$16.97", và khung theo cấu trúc chi phí (mua 1 lần vs mua lại) thay vì khẳng định tuyệt đối giá real-time.

---

## NEED DATA
- Giá quart-size CHÍNH XÁC, thời gian thực (2026) tại Home Depot/Lowe's cho daylily, sedum, coreopsis, Russian sage, black-eyed susan, lavender — cả 2 domain chặn WebFetch trực tiếp (403), chỉ có số liệu từ search-engine snippet cho hosta và annual 6-pack. Cần verify tay trước khi in số cụ thể vào script.
- Nguồn .edu trực tiếp cho độ sâu trồng (inch) của coreopsis (đào 3-4") và hosta/Russian sage/black-eyed susan/lavender (hiện chỉ có quy tắc chung "same depth as pot," không có số inch cụ thể từ .edu).
- Xác nhận ASPCA trực tiếp (chưa WebFetch riêng lẻ, chỉ qua tổng hợp search) cho Sedum và Rudbeckia (black-eyed susan) — cả hai được báo cáo "non-toxic" nhất quán qua nhiều nguồn thứ cấp, nhưng nên double-check trực tiếp trên aspca.org trước khi khẳng định "100% pet-safe" trong script.
- Nguồn .edu trực tiếp cho "lavender nên trồng mùa xuân thay vì mùa thu ở zone lạnh" (Câu hỏi 5, ngoại lệ) — hiện chỉ có Tier 4-5 (growing guides thương mại), chưa tìm được .edu xác nhận riêng điểm này sau 2 lần search.
