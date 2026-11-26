# Audit Report — "Tastes Like Apple and Honey. Grandma Planted It Once. And 6 More"

```
MODE: C (YMYL / edible)   | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: YMYL-Edible
DNA VOICE:          Moderate
NARRATOR INTEGRITY: Pass (0 flags)
HOOK:               Needs work (partial — xem §3)
COMPLIANCE (flag):  1 dấu hiệu (thiếu misID scoping cho cây ăn được)
=> VERDICT: REVISE
```

**Audit độc lập 2026-08-25.** Mọi vị trí giây bên dưới đo lại bằng word-index ÷ 2.5, KHÔNG lấy số của bản self-audit.
**Script:** 1,500 từ / 10.0 phút.

---

## §1 — PHẢN BIỆN 4 ĐIỂM NGƯỜI VIẾT TỰ CHẤM ✅

### ①  "Hook sống qua vùng chết 40–55s" → **🟡 CHẤM DỄ TAY, không phải ✅**

Đo lại vị trí thật:

| Sự kiện | Giây |
|---|---|
| Loop mở: *"I'm holding the name back"* | **26s** |
| **Tên cây được tiết lộ: *"It's called skirret"*** | **38s** |
| Neo họ cà rốt | 44s |
| *"Now, that line."* (setup) | 52s |
| Payoff Worlidge | **60s** |

**Vấn đề:** loop mạnh nhất của hook là *"tên cây là gì"*. Nó **đóng ở giây 38 — ngay trước cửa vùng chết**. Suốt 40–55s, cái giữ chân chỉ còn loop phụ (câu 1677), và nội dung phát trong khoảng đó là **neo thực vật học + một câu dẫn** — đúng thứ L4 cấm: *"KHÔNG chuyển sang preview/giới thiệu tại đây"*.

Bản self-audit đo bằng cue string nên ra "34s" và kết luận ✅. Đo bằng vị trí từ thật thì vùng 40–55 đang được gánh bởi phần yếu nhất của đoạn mở.

**🔴 BẢN VÁ — đảo thứ tự payoff và neo.** Hiện tại: neo (38–52s) → trích dẫn (60s). Đổi thành: trích dẫn (~42s) → neo (~55s).

> All right. It's called skirret. And here's why that name is worth remembering.
> An English gardener named John Worlidge put skirret in his gardening book. He called it, his words, the sweetest, whitest, and most pleasant of roots. Sixteen seventy-seven. And the page is still there. The University of Michigan scanned the original.
> Now, before that name scares anybody off. It's in the same family as carrots and parsley. You grow it about like a parsnip. That's it. That's the whole learning curve.

Vùng chết 40–55s giờ chứa **payoff**, không chứa setup. Neo L1 lùi xuống 55s — vẫn thừa sớm.

### ②  "Anti-slop, 4 bằng chứng" → **🟡 ĐÚNG NHƯNG FRONT-LOADED**

Bằng chứng khác biệt là thật, nhưng đo vị trí thì chúng **dồn hết vào 40% đầu + beat dip**:

| Bằng chứng | Giây |
|---|---|
| Trích dẫn sơ cấp 1677 + tên thư viện | 60s |
| Ghi chú WSU 2008 về catalog | ~250s |
| Consensus synthesis 3 nguồn | 350s |
| Chuyện Seed Savers | 526s |

Khoảng **460s → 500s** (item chives) là đoạn generic nhất cả video — và nó nằm đúng chỗ người xem quyết định có xem hết không. Item 2–7 nói chung có thể bê sang bất kỳ kênh làm vườn nào.

**🟡 BẢN VÁ:** item 7 (chives) đang là item **phẳng nhất** trong khi skill yêu cầu item ĐẦU và CUỐI bắt buộc có intrigue. Thêm một micro-surprise có nguồn — dùng chính con số đã verify:

> Chives is the one that pays you back the same season. Every other plant on this list makes you wait. This one you cut the first summer.

### ③  "Evidence ✅" → **🟡 CÓ MỘT LỖ**

Soi từng claim: **không có claim nào nằm ngoài research-brief** — điểm này người viết chấm đúng. Nhưng:

**Nguồn yếu nhất đang nằm ở vị trí mạnh nhất.** Claim *"three different countries in Europe named this thing after sugar"* nói ở giây **13–26**, là bằng chứng chính cho lời hứa vị ngọt trong hook. Nguồn duy nhất của nó là **Wikipedia** — chính research-brief đã tự gắn nhãn *Tier 4, chỉ dùng cho dữ kiện ngôn ngữ*.

Về mặt kỹ thuật đây là dữ kiện ngôn ngữ nên vẫn trong phạm vi cho phép. Nhưng đặt Tier 4 làm trụ cho hook của một kênh bán bằng độ chính xác là rủi ro không cân xứng — và khán giả ngách này nổi tiếng hay vào comment sửa lỗi.

**🟡 BẢN VÁ:** thay bằng nguồn Tier 1 đã có sẵn — UF/IFAS mô tả *"the taste is sweet… the color is very white"*, và Worlidge 1677 là bằng chứng ngôn ngữ mạnh hơn nhiều. Hoặc giữ câu "sugar root" nhưng bỏ chữ *"three different countries"* (chi tiết đếm được → dễ bị soi) thành *"the old European names for it just translate to sugar root."*

**Xác nhận flag của người viết:** 4 attribution lấy từ search summary là rủi ro thật. Nặng nhất là **UF/IFAS** — trang đó trả **HTTP 410 khi fetch trực tiếp**, nội dung chỉ có qua bản tóm tắt. Mà nó đang chống lưng cho honesty beat. Phải verify trước khi lên sóng.

### ④  "L3 deliver trong 60s ✅" → **🟡 CHẤM ĐÚNG CÂU HỎI SAI**

*"It's sweet"* xuất hiện ở giây **13** → lời hứa "ngọt" giao rất sớm, đúng. Nhưng **lời hứa trong title không phải "ngọt", mà là "apple and honey"** — và ở giây **86** script tự phủ định nó:

> *"It just isn't a spoonful of honey, and I won't sell it to you that way."*

Người xem bấm vào **vì** cụm apple and honey. Giây 86 họ được bảo rằng nó không phải thế. Về mặt liêm chính thì đúng (CR4). Về mặt retention thì đây là **rút lại lý do click** ở đúng phút đầu — và bản self-audit chấm ✅ mà không hề cân nhắc mặt trái này.

**🔴 BẢN VÁ — đừng phủ định, hãy đóng khung lại.** Vẫn trung thực 100%, vẫn scope claim, nhưng không rút lại cú click:

> Here's the thing, though. Apple and honey — that's the language growers reach for when they try to describe it. The extension sheet out of the University of Florida stays plainer about it. Firm. Sweet. Very white. So both things are true. It's genuinely sweet, and it's a root, not a dessert.

Cả hai câu đều đúng với nguồn. Không còn câu *"tôi sẽ không bán cho bạn kiểu đó"* — câu đó nghe liêm khiết nhưng nó bảo người xem rằng thứ họ đến tìm không tồn tại.

---

## §2 — PHÁT HIỆN MỚI (self-audit BỎ SÓT)

### 🔴 A. THIẾU MISID SCOPING CHO CÂY ĂN ĐƯỢC — lỗi nặng nhất của bản này

Quét toàn script: `wild` = 0 · `forage` = 0 · `look-alike` = 0 · `only eat` = 0 · `you planted` = 0.

Video này nói với người 60–80 tuổi rằng có một củ rễ **họ chưa từng nghe tên**, rồi trấn an bằng: *"it's in the same family as carrots and parsley."*

Chính câu trấn an đó tạo ra rủi ro. Apiaceae là họ rộng, và trong đó có những loài **không phải cà rốt và không phải mùi tây**. Script không có lấy một dòng nói rằng chỉ ăn thứ mình tự trồng.

Research-brief **có sẵn** cảnh báo nhận nhầm — nhưng nó bị gán cho **video sequel** (salsify/wild parsnip). Sai chỗ: chính video NÀY là video gieo ý niệm "họ cà rốt, cứ trồng như parsnip".

MODE C yêu cầu misID warning cho nội dung edible. Đây là mục duy nhất khiến verdict không thể là PUBLISH.

**🔴 BẢN VÁ — một câu, không cần thêm claim mới, đặt ngay sau đoạn neo:**

> One rule for this whole video, and it's non-negotiable. You eat what you planted, in the bed where you planted it. Nobody here is telling you to go dig roots out of a ditch.

Câu này: không khẳng định gì về loài nguy hiểm nào (nên không cần nguồn mới) · dùng đúng signature phrase `Non-negotiable` của brand · phục vụ cả 7 item · và mở đường sạch cho video salsify.

### 🟡 B. Sequel tease có thể là hứa hão

Script hứa: *"Next time, we're going after the root the old growers called the oyster plant."*

`SLATE-2026-W34.md` liệt 4 bài đã chốt — **không có bài nào là salsify**. CR8 yêu cầu tease phải móc vào backlog thật. Hoặc đưa salsify vào slate, hoặc hạ tease xuống dạng không hẹn ("somewhere down the line").

### 🟡 C. Video đạt đỉnh ở phút 1 rồi đi ngang

Điểm mạnh nhất cả bài là trích dẫn 1677 — **giây 60**, tức 10% timeline. Sau đó 7 item chạy gần như cùng biên độ, không có build-up tới đỉnh thứ hai.

Beat hay thứ nhì là twist *"split the clump"* ở **350s** — đang bị viết như một ghi chú kỹ thuật. Đây mới là climax tự nhiên của video (nó lật lại chính lời hứa "trồng một lần"). Nên dựng cao độ cho nó, chứ không để nó trôi qua ngang hàng với các item.

### 🟡 D. Item 7 (chives) phẳng — xem §1②

### ✅ E. Quyết định bỏ anonymous social proof — **AUDIT XÁC NHẬN NGƯỜI VIẾT ĐÚNG**

`brand-voice-dna.md` liệt *"a viewer in [state]"* là signature element. Nhưng bịa một nhân chứng để làm bằng chứng là **fake witness** — chính skill này liệt đó là 🔴 Narrator Integrity. Hai luật trong cùng workspace đang mâu thuẫn nhau.

Người viết chọn đúng luật. **Việc cần làm không phải sửa script, mà là sửa `brand-voice-dna.md`**: khoanh lại signature element đó thành *"chỉ dùng social proof ẩn danh khi có nguồn thật; không có nguồn thì dùng 'growers report' / 'extension bulletins note'"*. Nếu không, video sau lại rơi vào cùng cái bẫy.

---

## §3 — HOOK CHECK

- [x] Đòn đau / viễn cảnh tương phản — có (rễ trắng kéo lên khỏi đất lạnh)
- [x] Open Loop — có, mở @26s
- [x] 5 từ đầu mạnh — *"Pull it out of cold October ground"*, động từ mệnh lệnh ✅
- [x] Mini-payoff trước ~20s — *"It's sweet"* @13s ✅
- [ ] **Câu rơi vào HOOK_DROPOFF_ZONE 40–55s có giữ chân không** → **FAIL**, xem §1①

Hook về bản chất **mạnh**. Lỗi nằm ở **thứ tự sau hook**, không nằm ở hook.

---

## §4 — DNA VOICE AUDIT

| Yếu tố | Đếm được | Yêu cầu | |
|---|---|---|---|
| "Here's the thing" | 1 | — | ✅ |
| "Here's why" | 2 | 2–3 | ✅ |
| "That's it" | 2 | 1 | 🟡 hơi nhiều |
| "Don't panic" | 1 | 1 | ✅ |
| grandmother (folklore) | 3 | 1–2 | 🟡 hơi nhiều |
| "one planting" (hero anchor) | 3 | — | ✅ |
| Mantra 3 nhịp | 1 | 1 | ✅ |
| `Happy gardening.` | 1 | 1 | ✅ |
| Cost comparison | 1 | 1 | ✅ |
| **Contractions** | **35%** | **≥60%** | 🟡 |
| AI clichés | 0 | 0 | ✅ |
| Anonymous social proof | 0 | 1 | ✅ *(cố ý — xem §2E)* |
| Accessibility Anchors | 2 | 2–3 | 🟡 sát sàn |

**Contractions 35%:** xác nhận flag của người viết. Giảm nhẹ vì văn phong nhiều câu cụt cố ý (*"Not one." / "Firm. Sweet. Very white."*) vốn không nhận contraction. Vẫn nên nâng ~15 điểm ở các câu dài.

---

## §5 — NARRATOR INTEGRITY SCAN

Quét đủ blacklist: `I've grown` · `I've tested` · `my garden` · `my clients` · `when I was` · `for X years` · `I personally` → **0 hit**.

Ngôi "I" chỉ xuất hiện ở vai host: *"I'm holding the name back"* · *"I won't quote you a zone"* · *"I'm not going to hand you a villain"*. Đều hợp lệ.

**PASS — 0 flag.** Đây là mục người viết làm tốt nhất.

---

## §6 — COMPLIANCE FLAG (không chấm lại Risk Score)

- Blacklist tuyệt đối (guaranteed/100%/miracle/cure/detox) → **0**
- Conspiracy / "họ giấu bạn" → **0**. Beat kinh tế @329s là soft-economics sạch, không quy trách nhiệm cho ai ✅
- YMYL đã hedge: lá rhubarb ✅ · inulin sunchoke (gần nguyên văn WSU) ✅ · zone skirret ✅
- **[PET-SAFETY] thiếu** — 0 lần nhắc chó mèo. Không phải vi phạm policy, nhưng là đòn bẩy engagement kênh đang bỏ trống
- **[COMPLIANCE] misID scoping thiếu** → xem §2A 🔴

---

## §7 — ACTIONABLE FIXES (xếp theo tác động)

| # | | Sửa gì | Tác động |
|---|---|---|---|
| 1 | 🔴 | Thêm câu misID scoping *"You eat what you planted"* sau đoạn neo | Bịt lỗ an toàn duy nhất — chặn verdict PUBLISH nếu không sửa |
| 2 | 🔴 | Đảo thứ tự: trích dẫn Worlidge lên ~42s, neo họ cà rốt xuống ~55s | Đưa payoff vào đúng vùng chết 40–55s của kênh |
| 3 | 🔴 | Viết lại honesty beat: đóng khung lại thay vì phủ định "apple and honey" | Không rút lại lý do click ở phút đầu |
| 4 | 🟡 | Verify 4 attribution (ưu tiên UF/IFAS — trang trả 410) | Kênh bán bằng độ chính xác |
| 5 | 🟡 | Bỏ "three different countries", thay bằng nguồn Tier 1 | Gỡ Tier 4 khỏi vị trí mạnh nhất |
| 6 | 🟡 | Thêm intrigue cho item 7 + dựng climax cho twist "split the clump" @350s | Vá đoạn generic nhất, đúng chỗ người xem bỏ |
| 7 | 🟡 | Nâng contractions lên ~60% ở các câu dài | DNA voice |
| 8 | 🟡 | Salsify vào slate, hoặc hạ sequel tease | CR8 không hứa hão |
| 9 | 🟡 | Sửa `brand-voice-dna.md` — khoanh lại luật social proof | Chặn bẫy này cho video sau |

---

## §8 — INLINE TAGS

`[COMPLIANCE]` misID scoping thiếu (§2A) · `[PET-SAFETY]` thiếu · `[NEED DATA]` 4 attribution chưa fetch trực tiếp · `[HEDGE]` zone skirret ✅ đã hedge đúng · `[YMYL]` rhubarb + inulin ✅ đã hedge đúng

---

## VERDICT: **REVISE**

Không REJECT: narrator sạch tuyệt đối, không blacklist, không conspiracy, YMYL đã hedge, mọi claim truy được về research-brief.

Không PUBLISH: một lỗ an toàn misID trong video edible (MODE C không cho qua), cộng hai lỗi bố cục retention ở đúng hai vùng chết đã đo được của kênh.

**Ba fix 🔴 ước tính 20 phút.** Sau đó bài này publish được.

> ⚠️ Nhắc trước khi upload: bật **"Altered or synthetic content"** (kênh dùng AI voice) · Producer sign-off TRƯỚC khi export VoiceAI.

---

# FIX LOG — áp 2026-08-25 (sau audit)

**Script sau sửa: 1,500 từ / 10m00s · Pha D verify 7/7 PASS · 0 câu >20 từ.**

## 🔴 Đã sửa — cả 3

| # | Fix | Kết quả đo lại |
|---|---|---|
| 1 | **misID scoping.** Thêm: *"One rule for this whole video, and it's non-negotiable. You eat what you planted, in the bed where you planted it. Nobody's telling you to go digging roots out of a ditch."* | `you planted` = 2 (trước: 0). Dùng signature `non-negotiable`. Không thêm claim mới → không cần nguồn mới. Đặt @~67s, ngay sau đoạn neo |
| 2 | **Đảo thứ tự payoff/neo.** Worlidge lên trước, neo họ cà rốt xuống sau | Payoff Worlidge **60s → 51s**, nằm trọn trong vùng chết 40–55s. Neo lùi xuống ~57s, vẫn thừa sớm |
| 3 | **Honesty beat đóng khung lại, bỏ phủ định.** *"…So both things are true. It's genuinely sweet, and it's a root, not a dessert."* (thay cho *"It just isn't a spoonful of honey, and I won't sell it to you that way"*) | Không còn rút lại lý do click. CR4 vẫn đạt: vẫn scope claim bằng nguồn UF/IFAS |

## 🟡 Đã sửa

| # | Fix | Kết quả |
|---|---|---|
| 5 | Bỏ *"three different countries in Europe"* (nguồn Tier 4 ở vị trí mạnh nhất) → *"the old European names for it all mean the same thing. Sugar root."* | Cộng với fix #2, trụ chứng minh vị ngọt giờ là **nguồn sơ cấp 1677 @51s**, không còn là Wikipedia |
| 6a | Dựng climax cho twist *"split the clump"* @328–350s | *"But here's the part nobody tells you. Plant it once isn't quite the whole truth."* → beat dip giờ có biên độ, không còn là ghi chú kỹ thuật |
| 6b | Intrigue cho item 7 (chives) | *"Last one. And here's the small surprise. It's the easiest plant here, and also the one that asks for attention soonest."* — micro-surprise CÓ NGUỒN (2–4 năm, ngắn nhất danh sách) |
| 7 | Contractions | 35% → **41%** (76 occurrence / 186 câu). **Vẫn dưới mốc 60%** — xem mục còn treo |
| 8 | Sequel tease hạ xuống không hẹn: *"Somewhere down the line we'll get to…"* | CR8 không còn hứa hão khi salsify chưa có trong slate |

## ⚠️ Regression đã bắt được và revert trong lúc sửa

Vòng nâng contractions vô tình làm hỏng 4 chỗ, đã revert hết:

- 🔴 **`"They may cause gas"` → `"They'll sometimes cause gas"`** — đây là **hedge YMYL lấy gần nguyên văn WSU**. Đổi sang "will sometimes" là **nâng cấp độ chắc chắn của một claim sức khoẻ**. Đã trả về `may`.
- `"So give it a bed of its own"` → `"So it's getting a bed of its own"` (sai thức câu, mất tính hướng dẫn) — đã revert
- `"pull apart easy"` → `"easy enough"` (làm yếu claim) — đã revert
- `"potatoes"` → `"potatoes yet"` (vô nghĩa) + hai chữ *"though"* liền nhau — đã revert

> Bài học đáng ghi: **tối ưu một chỉ số văn phong (contractions) đã suýt phá một hedge YMYL.** Lần sau nâng contractions thì loại trừ trước các câu mang nhãn `[YMYL]` trong research-brief.

## Còn treo — chưa sửa

| | Mục | Vì sao chưa sửa |
|---|---|---|
| 🟡 | **Contractions 41% vs mốc 60%** | Script cố ý dùng nhiều câu cụt (*"Not one." / "Firm. Sweet. Very white."*) vốn không nhận contraction. Ép lên 60% sẽ phải đổi texture văn. Cần người quyết. |
| 🟡 | **Pet safety = 0** | research-brief **không có nguồn nào** về độc tính với chó mèo cho 7 cây này. Không bịa. Cần thêm 1 vòng research. |
| 🟡 | **4 attribution chưa fetch trực tiếp** | UMN (rhubarb) · Illinois + Iowa State (asparagus) · **UF/IFAS (vị skirret — trang trả HTTP 410)** · Wisconsin (walking onion) |
| 🟡 | **`brand-voice-dna.md` mâu thuẫn nội bộ** | Signature element *"a viewer in [state]"* xung đột với luật cấm fake witness. Sửa file, không sửa script. |
| 🟡 | **L8 pain-removal stack** | Hệ quả của việc chọn góc hoài niệm thay góc ergonomic ở bước outline. Không phải lỗi phát sinh. |

## Verdict sau fix

**REVISE → PUBLISH-READY**, với 4 mục 🟡 còn treo ở trên là quyết định của người sản xuất, không phải lỗi chặn.
