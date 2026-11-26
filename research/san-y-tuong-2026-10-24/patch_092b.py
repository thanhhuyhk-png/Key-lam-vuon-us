p = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/script.md"
s = open(p, encoding="utf-8").read()
a = "None of this means the potato works."
assert a in s
s = s.replace(a, "A result is only as good as the way the test was built. " + a, 1)
open(p, "w", encoding="utf-8").write(s)

b = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/research-brief.md"
t = open(b, encoding="utf-8").read()
note = """
## 🔁 BỔ SUNG SAU AUDIT ĐỘC LẬP (24/10/2026 — orchestrator đã mở lại toàn văn Wali 2019 và NC State)
- **C04 (sửa):** văn bản nói *"9 treatments were assigned to eight blocks… Each block containing 9 cuttings"*, *"four blocks with potatoes and four blocks without"*, rồi *"the remaining 108 cuttings in three replications… cultivated in soil"*. 8×9=72 ≠ 108 → số liệu **tự mâu thuẫn**. Bài **không** nêu: số cành ra rễ mỗi nhóm; số cành nhóm khoai. Bảng 1 gắn nhãn "with potato" cho cả 9 nghiệm thức.
- **C02 bổ sung (TN1):** *"The suitable planting time in Khost province for rose cutting is 15 March. This time was passed. The cuttings were planted on May 15, 2017."* Kết luận: *"both cultivation time and elevation gradient is very important for rose cuttings to produce roots."* (không có kiểm định). TN1 cành lấy từ vườn hồng ở độ cao ~2.500 m. **Results nói "most cuttings sprouted" (A few days after planting, the main axillary bud of most cuttings broke); Discussion nói "none of the cutting sprouted"** → bài tự mâu thuẫn ở TN1.
- **C02 (TN2):** cả Results, Discussion, Conclusion đều nói nhóm khoai **không nảy chồi và không ra rễ**; tóm tắt (RePEc/abstract) nói "nảy chồi nhưng không rễ".
- **C05 bổ sung (số mắt):** LSD (critical value 43,0, bảng 5): ô **15 cm × 2 mắt** nổi trội; **1 vs 2 mắt ở 20 cm (chênh 0,50) và ở 25 cm (19,75), 1 vs 3 mắt ở 15 cm (18,5) đều không khác biệt có ý nghĩa**. Chỉ số đo = trọng lượng rễ khô và chiều dài chồi, không phải tỷ lệ ra rễ; CV ≈84–108%. Phần Discussion tóm tắt kết quả này sai khớp với bảng. → "1 mắt = yếu" chỉ đúng ở 15 cm; không nói thành quy luật.
- **C10 bổ sung (Iowa State, How to Propagate Roses):** bán hóa gỗ là cách "easiest" cho hồng; hồng cũng có thể giâm bằng cành hóa gỗ. (Purdue C16 nói cành hóa gỗ nói chung khó hơn và 2–4 tháng — không riêng hồng.)
- **C12 bổ sung (NC State Beaufort):** *"Remove the leaves on the lower portion of the cutting but keep the upper leaves"*; *"Scar the bottom 1 inch"* trước khi nhúng hormone; hormone "will increase your chances". (UC Master Gardeners: bỏ hết lá — khác NC State.)
- **C08/OSU slide:** slide có câu *"Cover a plant with a Quart jar"* (nguồn của "quart jar" trong script).
- **C15 (cột báo Alabama):** có cả "Rooting hormone is optional; most report higher success rate with it" và "considered by some to be very important".
"""
t = t.rstrip("\n") + "\n" + note
open(b, "w", encoding="utf-8").write(t)

st = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/pipeline-state.md"
x = open(st, encoding="utf-8").read()
x = x.replace("🟡 đang viết — Lô 1–2 ✅ duyệt, Lô 3 xong (M5 + M6, ~2.500 từ ≈ 15:09); còn Q, KẾT |",
              "🟡 bản nháp đủ 4 lô (~2.810 từ ≈ 17,0′, TEST độ dài) · Pha D sạch · audit độc lập REVISE → đã sửa các lỗi nguồn/số liệu; còn Triple F, compliance, TTS clean |")
x = x.replace("[3] script — lô 3/4 xong", "[3] script — nháp đủ, đã sửa theo audit; chờ GATE các bước còn lại")
x = x.replace("user duyệt lô 3 → lô 4 (Q + KẾT)", "user duyệt sửa audit → Triple F → compliance → TTS clean → prediction")
open(st, "w", encoding="utf-8").write(x)
print("ok")
