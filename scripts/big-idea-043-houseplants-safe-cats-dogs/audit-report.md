# Audit Report — 9 Houseplants That Are Safe for Cats and Dogs

**Ngày:** 2026-08-19 · **File:** `script.md` (1,127 từ · 7.5–8.1′)
**Audit độc lập** — bài compliance nhạy nhất tuần, soi kỹ nhất trong 4 bài.

```
MODE: C (YMYL — pet safety)   | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: YMYL-PetSafety
DNA VOICE:          Strong
NARRATOR INTEGRITY: Pass (0 flags)
HOOK:               Pass
COMPLIANCE (flag):  1 dấu hiệu (xem 🔴 #1)
FACTUAL ACCURACY:   🔴 1 lỗi + 1 claim chưa verify (đã verify bổ sung, xem 🟡 #2) + 2 claim màu mè chưa gắn nguồn
=> VERDICT: REVISE → **ĐÃ VÁ → PUBLISH** (script.md cập nhật 2026-08-19)
```

---

## 🔴 LỖI 1 — "ASPCA's own safe list" ngụ ý sai về nguồn

**Câu gốc:**
> *"Nine plants, straight from the ASPCA's own safe list."*

**Vì sao sai:** ASPCA **không xuất bản một danh sách "9 cây an toàn"** nào — họ có một cơ sở dữ liệu
tra cứu hàng trăm loài cây, mỗi loài 1 trang riêng. "9 cây" là do **kênh tự chọn và đối chiếu** từng cây
với dữ liệu ASPCA, không phải ASPCA tự tuyển chọn sẵn. Cụm "straight from the ASPCA's own safe list"
ngụ ý ASPCA đã làm sẵn danh sách này — phóng đại thẩm quyền nguồn, đúng loại lỗi cần tránh ở 1 video mà
toàn bộ giá trị dựa trên "chúng tôi đã tra cứu kỹ, không đoán".

Đáng chú ý: script tự mâu thuẫn — dòng 55 dùng đúng cách nói *"checked against the ASPCA's own safety
records"* (chính xác), trong khi dòng 17 dùng cách nói sai *"the ASPCA's own safe list"*.

**Bản vá:**
> *"Nine plants, every one checked against the ASPCA's own records."*

---

## 🟡 LỖI 2 — Claim "rainforest Brazil" chưa có trong research-brief (đã verify bổ sung, giữ lại)

**Câu gốc:**
> *"It's a jungle plant, native to the rainforests of Brazil…"*

**Vì sao gắn cờ:** `research-brief.md` Câu 1 chỉ ghi ASPCA + tên khoa học *Schlumbergera bridgesii* cho
Christmas cactus — KHÔNG có claim về nguồn gốc Brazil. Claim này lọt vào script mà chưa qua research-brief,
vi phạm quy trình (dù bản thân câu đúng).

**Đã verify bổ sung (audit tự kiểm tra):** UC ANR Extension (University of California) + NC State
Extension xác nhận: *Schlumbergera* có nguồn gốc từ **vùng núi ven biển đông nam Brazil**, mọc phụ sinh
(epiphytic) trên cây/đá ở rừng mưa ẩm cao 3.000–5.000 feet, cụ thể ở dãy Organ Mountains gần Rio de
Janeiro. Claim **đúng và giờ đã có nguồn**.
**Nguồn bổ sung:** UC ANR — https://ucanr.edu/blog/real-dirt/article/cactus-rainforest-christmas-cactus-0
· NC State Extension — https://plants.ces.ncsu.edu/plants/schlumbergera-russelliana/
**→ Giữ nguyên câu trong script** (không cần sửa nội dung), chỉ ghi chú bổ sung nguồn vào research-brief
để đúng quy trình cho lần audit sau.

---

## 🟡 LỖI 3 — 3 claim "màu mè" không truy được nguồn cụ thể (mức rủi ro thấp, nên hedge nhẹ)

**Câu gốc (3 chỗ):**
> *"Cats especially seem drawn to those thin, arching leaves…"* (spider plant, mục 1)
> *"…it's the toughest of the nine…"* (spider plant, kết luận)
> *"…it's also the one cats seem to want to chew on the most anyway…"* (spider plant, kết luận)

**Vì sao gắn cờ:** đây là kiến thức làm vườn phổ thông, được lặp lại rộng rãi (bài 1 của kênh cũng từng
dùng ý tương tự cho spider plant), nhưng **không nằm trong bảng Verified Claims** của research-brief bài
này. Rủi ro thấp (không phải safety claim, chỉ là mô tả hành vi mèo/độ bền cây) nhưng để nhất quán với
tiêu chuẩn đã áp dụng ở BÀI 1/BÀI 2, cần hedge nhẹ thay vì phát biểu chắc nịch.

**Bản vá:** thêm hedge "many gardeners report" cho câu đầu tiên (đủ để khoanh vùng, không cần lặp hedge
cả 3 chỗ vì đây không phải claim y tế/an toàn — mức độ rủi ro thấp hơn hẳn 🔴 #1 và không cần rewrite
nặng tay).

---

## ✅ Các góc đạt — không cần sửa (kiểm tra sâu vì đây là bài cao rủi ro nhất)

| Góc | Kết quả |
|---|---|
| **9/9 claim ASPCA cốt lõi** | Đối chiếu lại từng câu trong script với bảng Câu 1 research-brief — khớp 100%, không cây nào bị thổi phồng quá "non-toxic" |
| **Bamboo palm/Parlor palm (điểm khó nhất bài)** | Script nêu ĐÚNG phát hiện ASPCA gộp chung entry, không giấu, không overclaim thêm — đúng tinh thần "nói thật" đã duyệt ở research-brief |
| **Lily section (objection-handling)** | Khớp chính xác ASPCA + FDA: "kidney failure", "18 hours", "cats are the only species known to be affected" → viết thành "cats are the ones at real risk" (hedge hợp lý hơn cả nguồn gốc). Giọng điềm tĩnh, 0 từ giật gân (đã grep: không "deadly!"/"kills"/"poison your pet") |
| **Honesty layer CR4** | Đúng câu đã duyệt, KHÔNG gán cho ASPCA như trích dẫn trực tiếp (research-brief dặn kỹ điều này) |
| **Compliance ngôn ngữ** | 0 lần "100% safe"/"completely safe"/"totally safe" trong 1,127 từ. 12 lần "non-toxic", 13 lần "ASPCA" — hero anchor đúng thiết kế |
| **Retention (DATA MODE)** | `HOOK_DROPOFF_ZONE` 40–55s: loop "Christmas cactus" sống tại 36–44s, payoff đầy đủ @3.8′ (trước dip, có build-up). `MIDROLL_DIP_ZONE` 4–6′: toàn bộ lily/objection-handling nằm gọn 5.3–6.0′ |
| **Narrator Integrity** | 0 vi phạm — "I've gone through the ASPCA's own database" không nhận là chuyên gia thú y |
| **Storytelling craft** | 1 viewer-POV scene (mèo cắn lá) ✅ · per-item intrigue đủ ở item đầu (spider plant) + item cuối (prayer plant, callback họ Marantaceae) ✅ · climax rõ (Christmas cactus @3.8′ + lily @5.3-6.0′ là 2 đỉnh hợp lý cho video 2 phần: listicle + honesty) · forward-visual nhẹ ("save this list before you need it") + identity CTA ("you belong here") ✅ |
| **Anti-slop / differentiation** | 3 bằng chứng: ① phát hiện bamboo/parlor palm trùng entry (không kênh generic nào có) ② chủ động cảnh báo lily dù không cần thiết cho "danh sách an toàn" ③ liên kết họ Marantaceae giữa 2 cây — chi tiết khoa học thật |
| **Lessons-learned ACTIVE RULES** | L1 ✅ (9/9 cây phổ biến) · L3 ✅ (@26s) · L4 ✅ (@36-44s) · L5 ✅ (@5.3-6.0′) — L6/L7/L8 không áp dụng trực tiếp (không phải claim ngược đời, video ngắn hơn 10′) |

---

## ACTIONABLE FIXES (đã áp dụng)

1. 🔴 Sửa "the ASPCA's own safe list" → "the ASPCA's own records" (khớp cách nói chính xác đã dùng ở dòng 55).
2. 🟡 Bổ sung nguồn UC ANR + NC State Extension cho claim Brazil rainforest vào research-brief (giữ nguyên script).
3. 🟡 Thêm hedge "many gardeners report" cho claim hành vi mèo với spider plant.

## INLINE TAGS
`[NEED DATA]` 0 · `[YMYL]` 1 (toàn bộ video — pet safety, đã hedge đúng mức "non-toxic theo ASPCA")
`[PET-SAFETY]` ✅ có, chính xác · `[HEDGE]` ✅ đủ · `[COMPLIANCE]` sạch sau vá

---

⚠️ **Nhắc trước khi upload:** bật **"Altered or synthetic content"** · Producer sign-off trước khi export.
🔴 **Khuyến nghị riêng bài này:** vì là chủ đề an toàn động vật thật, nên có 1 người thật (không phải AI)
đọc lại script trước khi đăng, dù audit này đã kiểm kỹ.
