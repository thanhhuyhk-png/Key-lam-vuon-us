# Research Brief — Nitrogen Trap Clematis (Why Your Lush Green Clematis Never Blooms)

> Agent: garden-deep-researcher | Model: claude-sonnet-4-6 | Date: 2026-07-14

---

## ⚠️ KHUYẾN NGHỊ ƯU TIÊN CHO ORCHESTRATOR (đọc trước khi viết script)

1. **Potassium permanganate — ĐỔI GÓC, không giữ claim "giết vi sinh đất".** Sau 3 vòng search (an toàn hóa chất, extension, EPA, case report y khoa), KHÔNG tìm được bất kỳ nguồn .edu/.gov nào xác nhận "thuốc tím giết vi sinh vật đất" khi dùng trong vườn dân dụng. Nhưng tìm được bằng chứng mạnh cho góc khác: (a) thuốc tím **không phải thuốc trừ nấm/thuốc trừ sâu được EPA đăng ký** cho mục đích vườn/đất (archive.epa.gov xác nhận "not a registered algaecide", chỉ có hướng dẫn dùng cho ao/nuôi trồng thủy sản ở nồng độ rất cụ thể 2 ppm — không có hướng dẫn liều dân dụng cho đất); (b) **NIH/PMC ghi nhận nhiều ca ngộ độc/bỏng hóa chất có thật** khi tiếp xúc da/mắt hoặc nuốt nhầm, đặc biệt ở trẻ em, không có thuốc giải độc đặc hiệu. → **Khuyến nghị: đổi cảnh báo sang "hóa chất ăn mòn, dễ pha sai nồng độ, không có hướng dẫn liều lượng dân dụng rõ ràng, rủi ro bỏng da/mắt và ngộ độc nếu nuốt/trẻ nhỏ tiếp xúc"** — KHÔNG khẳng định "giết vi sinh vật có lợi trong đất" như một fact khoa học.
2. **Công thức "5-10-10 / high-phosphorus" — cần hedge mạnh hơn dự kiến, không chỉ là "thiếu nguồn .edu".** Tìm được nguồn .edu (NDSU 2023, và gián tiếp qua UMass Amherst — không fetch được nội dung do 403 nhưng tiêu đề xác nhận cùng luận điểm) nói THẲNG rằng **"bón thêm phốt-pho không làm tăng số hoa"** ở đất vườn thông thường (đa số đất phi nông nghiệp đã đủ phốt-pho), và khuyến nghị nhà kính thương mại dùng tỷ lệ N:P thấp hơn (3:1 hoặc 5:1) chứ không phải P cao tuyệt đối. Đây là **claim khoa học mạnh hơn và AN TOÀN hơn để dùng làm nguyên tắc chính: "GIẢM ĐẠM" mới là cơ chế được khoa học xác nhận (PNAS, Journal of Experimental Botany, Physiologia Plantarum review) — còn "phải bón thêm phốt-pho" là khuyến nghị nghề vườn phổ biến (Clemson HGIC + nhiều nguồn dân gian) nhưng KHÔNG có nghiên cứu xác nhận phốt-pho tự nó kích hoa.** Script nên diễn đạt: "cắt giảm đạm" = cơ chế khoa học chứng minh; "chuyển sang công thức thiên P-K như 5-10-10" = khuyến nghị thực hành phổ biến từ chuyên gia làm vườn + tối thiểu hại (không thừa đạm) — không viết "nghiên cứu chứng minh phốt-pho làm cây ra hoa".

---

## Câu hỏi 1: Cơ chế sinh học/hormone chính xác nào khiến dư đạm ức chế chuyển từ sinh trưởng dinh dưỡng sang sinh sản?

**Findings:**
- Ở Arabidopsis, thụ thể/cảm biến nitrate NPF6.3/NRT1.1 phát hiện nitrate dư → **ức chế con đường sinh tổng hợp gibberellin (GA)** → protein DELLA (vốn bị phân hủy khi GA cao) tích tụ lại → DELLA kích hoạt 2 gen ức chế ra hoa **SMZ và SNZ** → SMZ/SNZ gắn vào vùng khởi động của gen "florigen" **FT** (gen phát tín hiệu ra hoa) và ức chế nó → hoa bị trì hoãn. (Gras et al., *Journal of Experimental Botany*, 2018/PMC5853263) — https://pmc.ncbi.nlm.nih.gov/articles/PMC5853263/
  → Action: khi thấy cây leo xanh um không ra nụ, hiểu rằng "công tắc ra hoa" (gen FT) đang bị 1 tầng gen ức chế khác chặn lại do dư đạm → Benefit: biết đây là vấn đề *tín hiệu hormone*, không phải cây "yếu" hay "bệnh" — nên fix bằng dinh dưỡng, không phải thuốc.
- PNAS 2021 (Han et al., *"Low nitrogen conditions accelerate flowering by modulating the phosphorylation state of FLOWERING BHLH 4 in Arabidopsis"*) xác nhận chiều ngược lại: **đạm THẤP đẩy nhanh ra hoa** thông qua thay đổi trạng thái phosphoryl hóa của protein FBH4 — một cơ chế riêng, cho thấy đạm tác động lên ra hoa qua *nhiều* con đường phân tử song song. — https://www.pnas.org/doi/10.1073/pnas.2022942118
  → Action: đừng chỉ chờ "hết đạm dư" một cách bị động → Benefit: chủ động đổi công thức bón sẽ tạo tín hiệu phân tử đẩy nhanh quá trình ra hoa, thay vì cây tự "hết pha lá" theo thời gian.
- Review tổng hợp Weber & Burow, *Physiologia Plantarum* 2018, "Nitrogen – essential macronutrient and signal controlling flowering time": **đạm vừa-thấp → ra hoa sớm hơn; đạm rất cao HOẶC đói đạm hoàn toàn → ra hoa trễ hơn** (mối quan hệ hình chữ U ngược, không phải "càng ít đạm càng tốt"). Ghi nhận thực tế nông nghiệp: bón phân đạm quá liều đã được báo cáo làm chậm chuyển pha sinh trưởng sang sinh sản ở cây trồng. — https://onlinelibrary.wiley.com/doi/full/10.1111/ppl.12664
  → Action: không cắt đạm về 0 (cây vẫn cần đạm để sống/quang hợp) mà GIẢM VỀ MỨC VỪA ĐỦ → Benefit: cây vẫn khỏe, lá vẫn xanh, nhưng "công tắc hoa" được mở lại.

**Giản lược cho Grade 6-8 (an toàn khoa học):** "Cây có 1 loại protein đóng vai trò như công tắc bật đèn 'ra hoa'. Khi đất dư đạm, cây tạo ra 1 tín hiệu hóa học khác đi ĐÈ lên công tắc đó, giữ nó ở vị trí TẮT — cây cứ tiếp tục 'xây nhà' (mọc lá) mà không bao giờ 'mở tiệc' (ra hoa)." — cách nói này giữ đúng chuỗi nhân quả (đạm dư → ức chế tín hiệu GA → gen ức chế bật lên → gen ra hoa bị khóa), không bịa thêm cơ chế.

---

## Câu hỏi 2: Công thức phân bón cụ thể (N-P-K, thời điểm) nào từ nguồn .edu để chuyển "nuôi lá" sang "ép ra hoa"?

**Findings:**
- **Clemson HGIC** (Home & Garden Information Center, .edu) — factsheet Clematis: bón dư đạm "kích thích mô non, dễ nhiễm bệnh hơn"; khuyến nghị **test đất trước** để xác định nhu cầu bón thật sự, và **KHÔNG bón phân khi cây đang ra hoa/có nụ**. Không đưa ra tỷ lệ N-P-K cụ thể cho clematis. — https://hgic.clemson.edu/factsheet/clematis/
  → Action: test đất (soil test qua extension office địa phương) trước khi đổi công thức → Benefit: biết chính xác đất đang dư/thiếu gì thay vì đoán.
- **NDSU Extension** (Esther McGinnis, 2023) — "myth of high phosphorus fertilizers for more flowers": **nghiên cứu cho thấy tỷ lệ phốt-pho cao KHÔNG làm tăng số hoa.** Nhà kính thương mại thực ra dùng tỷ lệ đạm:phốt-pho 3:1 hoặc 5:1 (đạm CAO hơn lân, không phải ngược lại) cho các cây ra hoa liên tục. Ngay cả phân "cân bằng" 10-10-10 cũng bị coi là lãng phí phốt-pho. Đa số đất vườn (ngoài nông nghiệp) đã đủ phốt-pho sẵn. — https://www.ag.ndsu.edu/news/newsreleases/2023/august/dakota-gardener-the-myth-of-high-phosphorus-fertilizers-for-more-flowers
  → Action: đừng tự động đổ thêm phân "bloom booster" giàu P mà không test đất → Benefit: tránh lãng phí tiền + tránh nguy cơ dư phốt-pho gây hại (khóa vi lượng) mà không giải quyết được vấn đề gốc (đạm dư).
- **Đối chiếu:** nguồn nghề vườn phổ biến (Tier 4/5 — Petal Republic, Plant Addicts, Gardener's Path, Home to Sight) đồng thuận rộng rãi: dùng **5-10-10 hoặc 5-10-5** đầu xuân, bón 1 lần/tháng từ tháng 4-9, ngưng khi cây có nụ/hoa. Đây là *consensus nghề nghiệp*, không phải kết quả thí nghiệm N-P-K cho riêng clematis từ .edu.
  → Action → Benefit: xem Consensus Principle #2 bên dưới để cách diễn đạt an toàn.

**[NEED DATA]** Không tìm được nghiên cứu .edu/.gov nào thử nghiệm trực tiếp tỷ lệ N-P-K tối ưu CHO RIÊNG clematis (mọi khuyến nghị .edu chỉ nói "giảm đạm" chung chung, số 5-10-10 chỉ đến từ nguồn thương mại/blog).

---

## Câu hỏi 3: Tro gỗ dư khóa dưỡng chất nào, ở ngưỡng pH bao nhiêu, số liệu định lượng từ university extension?

**Findings:**
- **Purdue Extension** (John E. Woodmansee, 27/02/2026): khi pH đất vượt **7.0**, các dưỡng chất **phốt-pho, sắt, boron, mangan, đồng, kẽm và kali** bị "khóa hóa học vào đất", cây không hấp thụ được dù đất không thiếu chúng. Về liều lượng: các trường đại học land-grant khuyến nghị KHÔNG thống nhất — dao động từ 10-20 lbs/100 sq ft đến 5-25 lbs/1000 sq ft/năm; Purdue khuyên **test pH đất trước, không có 1 con số cố định**. — https://extension.purdue.edu/news/county/whitley/2026/02/using-wood-ash-in-the-garden.html
  → Action: test pH đất trước khi rắc tro gỗ, không rắc theo cảm tính → Benefit: tránh đẩy đất qua ngưỡng 7.0 rồi tự "khóa" dinh dưỡng của chính mình.
- **Nebraska Extension — Lancaster County** (Sarah Browning, 01/11/2019): xác nhận cùng ngưỡng pH 7.0 và cùng nhóm dưỡng chất bị khóa. Đưa ra khuyến nghị cụ thể hơn: đất hơi chua (pH 6.0-6.5) có thể bón **tối đa 20 lbs tro gỗ/100 sq ft/năm**; đất trung tính/kiềm (pH ≥ 7.0) → **tránh hoàn toàn**; đất rất chua (pH <5.5) hưởng lợi nhiều nhất. Không bao giờ dùng tro gỗ quanh cây ưa đất chua (khoai tây, đỗ quyên). — https://lancaster.unl.edu/using-wood-ash-garden/
  → Action: nếu đất đã trung tính hoặc kiềm (nhiều vùng đất Mỹ vốn đã kiềm), KHÔNG dùng tro gỗ cho clematis dù nghe "tro gỗ bổ sung kali tốt cho hoa" → Benefit: clematis vốn thích pH gần trung tính-hơi kiềm (5.5-7.0 theo nguồn nghề vườn) nên rất dễ bị đẩy pH vượt ngưỡng an toàn nếu rắc tro tùy tiện.

**Lưu ý số liệu:** 2 nguồn .edu dùng đơn vị khác nhau (Purdue: /100 sq ft và /1000 sq ft lẫn lộn tùy khuyến nghị được trích; Nebraska: 20 lbs/100 sq ft = tương đương 200 lbs/1000 sq ft — **cao hơn nhiều** so với con số "15-20 lbs/1000 sq ft" trong nghiên cứu nháp ban đầu). → Khi viết script, nên dùng cách diễn đạt an toàn: "một lớp mỏng, rắc như rắc đường lên bánh, không quá 1 lon cà phê cho khoảng sân nhỏ" thay vì nêu con số lbs chính xác dễ gây tranh cãi giữa các nguồn — hoặc trích rõ "theo Nebraska Extension, tối đa khoảng 20 pound cho mỗi 100 sq ft/năm trên đất hơi chua."

---

## Câu hỏi 4: Thuốc tím (potassium permanganate) dùng "khử trùng đất" tại nhà — hại thật hay claim dân gian?

**Findings:**
- **EPA (archive.epa.gov)**: potassium permanganate **KHÔNG phải là sản phẩm được đăng ký FIFRA** (không phải thuốc trừ sâu/thuốc diệt tảo được EPA cấp phép). Nó được dùng như chất oxy hóa/khử trùng trong nuôi trồng thủy sản ở nồng độ rất cụ thể (2 ppm cho ao, 10 ppm cho xử lý bể 10 phút) — **KHÔNG có hướng dẫn liều dùng dân dụng cho đất vườn.** — https://archive.epa.gov/oppsrrd1/registration_review/web/html/index-228.html
  → Action: không có "công thức pha loãng chuẩn" nào được cơ quan uy tín công bố cho việc rắc vào đất vườn → Benefit: người xem hiểu đây không phải "mẹo dân gian an toàn đã được kiểm chứng" mà là dùng ngoài mục đích được kiểm định.
- **NIH/PMC — nhiều case report y khoa** (ví dụ PMC4561647, PMC7279867, PMC1342846): ghi nhận các ca **ngộ độc/bỏng hóa chất có thật** do tiếp xúc/nuốt phải potassium permanganate — gây bỏng ăn mòn niêm mạc miệng-thực quản-dạ dày, phù nề, loét đường tiêu hóa; **không có thuốc giải độc đặc hiệu**, xử trí chỉ là hỗ trợ. Trẻ em là nhóm dễ gặp tai nạn nhất do tò mò/bắt chước người lớn. — https://pmc.ncbi.nlm.nih.gov/articles/PMC1342846/ , https://pmc.ncbi.nlm.nih.gov/articles/PMC7279867/
  → Action: cất xa tầm tay trẻ em, đeo găng/kính bảo hộ nếu bắt buộc dùng, không tự pha nồng độ theo cảm tính → Benefit: tránh bỏng da/mắt hoặc tai nạn ngộ độc đã được y văn ghi nhận thật.
- **KHÔNG tìm thấy** nguồn .edu/.gov nào xác nhận trực tiếp claim "thuốc tím giết vi sinh vật có lợi trong đất khi dùng làm vườn". Search cho thấy nó có hoạt tính kháng khuẩn phổ rộng nói chung (diệt vi khuẩn trong nước ở nồng độ thấp ~2 mg/L) nhưng không có nghiên cứu áp dụng riêng cho hệ vi sinh đất vườn.

→ **Xem khuyến nghị đổi góc ở đầu brief.** Đây là claim YMYL (an toàn hóa chất) — đủ băng chứng thật để cảnh báo, nhưng phải cảnh báo ĐÚNG THỨ có bằng chứng (ăn mòn da/mắt, ngộ độc khi nuốt, không có hướng dẫn liều dân dụng) chứ không phải thứ chưa có bằng chứng (giết vi sinh đất).

---

## Câu hỏi 5: Người xem cần làm gì cụ thể (nhận biết → đổi công thức → chờ hoa) và sai lầm phổ biến nào?

**Findings:**
- **Clemson HGIC**: tuyệt đối không bón phân khi cây đang trong giai đoạn ra nụ/ra hoa — bón lúc này chỉ kích thêm mô lá non, không giúp hoa. — https://hgic.clemson.edu/factsheet/clematis/
  → Action: quan sát cây — nếu đã thấy nụ, NGỪNG bón, chờ hoa tàn rồi mới bón lại → Benefit: tránh vô tình lặp lại chính sai lầm "dư đạm" ngay giữa mùa ra hoa.
- **Đồng thuận nghề vườn (Petal Republic, Plant Addicts, Old World Garden Farms, Gardener's Path):** lịch bón phổ biến — bón đầu xuân khi cây vừa nhú chồi mới (2-3 inch tăng trưởng cho cây mới trồng), 1 lần/tháng từ tháng 4 đến tháng 9, ngưng khi có nụ. Sai lầm phổ biến nhất được lặp lại trong nhiều nguồn: (1) dùng phân "all-purpose" N-P-K cao đều (vd 20-20-20) nghĩ là "an toàn" nhưng đạm 20 vẫn là quá cao cho giai đoạn ép hoa; (2) bón tiếp tục cả khi cây đã có nụ; (3) không đợi đủ thời gian — cây vừa đổi công thức có thể mất trọn 1 mùa mới thấy hoa nhiều hơn, không phải 1-2 tuần.
  → Action: đổi sang phân N thấp hơn P/K (không cần thiết phải "cao P tuyệt đối" — xem Câu hỏi 2) NGAY đầu mùa xuân, kiên nhẫn hết 1 mùa mới đánh giá kết quả → Benefit: kỳ vọng đúng thực tế, không bỏ cuộc giữa chừng hoặc đổ thêm phân vì "chưa thấy hoa sau 2 tuần" — chính hành vi bón thêm đó mới là thứ kéo dài "cái bẫy đạm".
- **[NEED DATA]** không có nguồn .edu định lượng chính xác "bao lâu thì thấy hoa trở lại sau khi giảm đạm" cho riêng clematis — nên hedge bằng "trong vòng 1 mùa sinh trưởng" (thuật ngữ phổ biến trong mọi nguồn nghề vườn) thay vì đưa ra con số tuần cụ thể.

---

## Consensus Principles (3 — nguyên liệu twist/authority cho script)

1. **Đạm dư không "làm hại" cây — nó khóa nhầm công tắc sinh học của cây ở chế độ "mọc lá" thay vì "ra hoa".**
   - Hội tụ: Gras et al. (*J. Exp. Botany* 2018), Han et al. (*PNAS* 2021), Weber & Burow (*Physiologia Plantarum* 2018) đều xác nhận đạm/nitrate tác động trực tiếp lên mạng lưới gen kiểm soát thời điểm ra hoa (qua GA/DELLA/SMZ-SNZ hoặc qua FBH4), không phải chỉ là "cây no quá nên lười ra hoa" theo cách hiểu dân gian.
   - Khác nhau: mỗi nghiên cứu tìm ra 1 con đường phân tử khác nhau (GA-DELLA-SMZ/SNZ vs. phosphoryl hóa FBH4) — cho thấy đạm ảnh hưởng ra hoa qua NHIỀU cơ chế song song, không phải 1 "công tắc" đơn giản, nhưng kết luận cuối cùng giống nhau: đạm dư = trễ hoa.
   - URLs: https://pmc.ncbi.nlm.nih.gov/articles/PMC5853263/ · https://www.pnas.org/doi/10.1073/pnas.2022942118 · https://onlinelibrary.wiley.com/doi/full/10.1111/ppl.12664

2. **Giảm đạm là fix được khoa học xác nhận; "bón thêm phốt-pho" chỉ là khuyến nghị nghề nghiệp phổ biến, KHÔNG phải kết luận nghiên cứu.**
   - Hội tụ: NDSU Extension (2023) và tinh thần chung của UMass Amherst CAFE (cùng chủ đề, không fetch được nội dung đầy đủ do lỗi 403 nhưng tiêu đề "Avoid Too Much Phosphorus" cùng hướng) đồng ý: phốt-pho dư không làm tăng hoa, đất vườn thường đã đủ P. Clemson HGIC (.edu) đồng ý điểm cốt lõi: đạm dư là vấn đề, khuyến nghị test đất thay vì đổ thêm phân theo công thức có sẵn.
   - Khác nhau: nguồn nghề vườn phổ biến (Petal Republic, Plant Addicts...) vẫn khuyên công thức "5-10-10" như một quy ước an toàn/thực dụng (P/K cao hơn N một cách tương đối, không phải P cao tuyệt đối) — đây là *kinh nghiệm thực hành*, không mâu thuẫn với khoa học nếu hiểu đúng: cái thực sự hiệu quả trong công thức đó là TỶ LỆ ĐẠM THẤP, không phải "liều phốt-pho cao".
   - URLs: https://www.ag.ndsu.edu/news/newsreleases/2023/august/dakota-gardener-the-myth-of-high-phosphorus-fertilizers-for-more-flowers · https://hgic.clemson.edu/factsheet/clematis/ · https://www.umass.edu/agriculture-food-environment/cafe/fact-sheets/fertilizing-flower-gardens-avoid-too-much-phosphorus (tiêu đề xác nhận, nội dung không fetch được)

3. **Tro gỗ dư nguy hiểm không phải vì "độc" mà vì nó âm thầm đẩy pH đất qua ngưỡng 7.0, tự khóa luôn dinh dưỡng của chính khu vườn.**
   - Hội tụ: Purdue Extension (2026) và Nebraska Extension–Lancaster County (2019) đều xác nhận cùng ngưỡng pH 7.0 và cùng nhóm 7 dưỡng chất bị khóa (P, Fe, B, Mn, Cu, Zn, K) khi vượt ngưỡng.
   - Khác nhau: liều lượng khuyến nghị an toàn không thống nhất giữa các trường (dao động rộng tùy pH nền của đất địa phương) — cả 2 nguồn đều nhấn mạnh PHẢI test pH trước, không có 1 con số chung cho mọi nơi ở Mỹ.
   - URLs: https://extension.purdue.edu/news/county/whitley/2026/02/using-wood-ash-in-the-garden.html · https://lancaster.unl.edu/using-wood-ash-garden/

---

## Story Bank (nguyên liệu scene)

`Story Bank: trống` — không tìm được câu chuyện lịch sử có nguồn .edu/.gov/archive đủ mạnh gắn trực tiếp với chủ đề "đạm dư chặn ra hoa" hoặc "tro gỗ/thuốc tím chữa đất" sau nhiều vòng search. 

Có 1 lead chưa đủ chuẩn để đưa vào brief chính thức (không WebFetch được nguồn gốc, chỉ có snippet + Wikipedia — vi phạm quy tắc tránh Wikipedia làm nguồn): **Clematis 'Jackmanii'** — giống lai clematis hoa lớn đầu tiên, tạo ra bởi nhà vườn George Jackman (Jackman & Sons, Woking, Surrey, Anh) từ phép lai năm 1858, ra mắt năm 1862, gây ra cơn sốt "Clematis Mania" ở Anh thời Victoria. Nếu muốn dùng, orchestrator/writer nên tự WebFetch một nguồn sơ cấp hơn (vd. Royal Horticultural Society, RHS Plant Finder, hoặc sách lịch sử làm vườn) để xác minh trước khi đưa vào script — KHÔNG dùng thẳng Wikipedia làm citation.

---

## Verified Claims Table

| # | Claim | Verdict | Nguồn mạnh nhất | Tier |
|---|-------|---------|------------------|------|
| A | Đạm dư trì hoãn ra hoa qua cơ chế hormone/gen (GA-DELLA-SMZ/SNZ, FBH4) | ✅ Xác nhận mạnh | J. Exp. Botany 2018 (PMC) + PNAS 2021 + Physiologia Plantarum 2018 | 2 (peer-reviewed) |
| B1 | Giảm đạm giúp cây chuyển sang ra hoa | ✅ Xác nhận mạnh | Weber & Burow 2018 (Springer/Wiley) + Clemson HGIC | 1-2 |
| B2 | Bón thêm phốt-pho (5-10-10) tự nó kích hoa | ⚠️ KHÔNG xác nhận — nguồn .edu nói ngược lại (myth) | NDSU Extension 2023 | 1 (phản bác), 4/5 (nguồn ủng hộ công thức) |
| C | Tro gỗ dư → pH >7.0 → khóa 7 dưỡng chất | ✅ Xác nhận mạnh | Purdue Extension 2026 + Nebraska Extension 2019 | 1 |
| D | Thuốc tím giết vi sinh vật có lợi trong đất | ❌ KHÔNG tìm được bằng chứng .edu/.gov | — (không có nguồn) | Không xác minh được |
| E | Thuốc tím là hóa chất ăn mòn/độc nếu dùng sai, không có hướng dẫn liều dân dụng | ✅ Xác nhận mạnh | EPA (archive.epa.gov) + NIH/PMC case reports | 1-2 |

---

## YMYL Flags
- **Potassium permanganate** → claim ăn mòn da/mắt + ngộ độc khi nuốt là có thật (NIH case reports) — cần disclaimer "không tự pha nồng độ, giữ xa tầm tay trẻ em, đeo bảo hộ nếu dùng". KHÔNG dùng claim "giết vi sinh đất" (chưa xác minh được).
- **Wood ash / pH đất** → không phải rủi ro sức khỏe con người trực tiếp, nhưng là claim "chữa/hại đất" cần chính xác về ngưỡng và khuyến nghị test đất trước — tránh đưa ra 1 con số lbs "chắc nịch" khi 2 nguồn .edu còn lệch nhau.

## NEED DATA
- Không tìm được thử nghiệm N-P-K định lượng riêng cho clematis từ nguồn .edu/.gov (chỉ có khuyến nghị chung "giảm đạm" + test đất).
- Không tìm được nguồn .edu/.gov xác nhận hoặc bác bỏ trực tiếp claim "thuốc tím giết vi sinh vật đất vườn" — cần hedge/đổi góc như khuyến nghị ở đầu brief.
- Không tìm được mốc thời gian cụ thể (số tuần/tháng) từ nguồn .edu cho "bao lâu sau khi giảm đạm thì clematis ra hoa trở lại" — chỉ có ước lượng nghề vườn "trong vòng 1 mùa sinh trưởng".
- UMass Amherst CAFE fact sheet (cùng chủ đề myth phốt-pho) bị chặn WebFetch (403) — nội dung chưa xác minh được đầy đủ, chỉ dùng được tiêu đề làm tín hiệu đồng thuận.
