# Sổ phản biện vòng 2 — big-idea-094 (08/11/2026)

**Phạm vi:** chỉ các đoạn trong `phan-bien-v2/vung-da-sua.md` + 1 câu trước/sau. Riêng R2 chấm Risk Score trên cả bài.

**R1 · Agy** (`--sandbox`, prompt qua tham số `-p` ~31 KB): ĐẠT CÓ SỬA · 0 CHẶN · 4 NÊN SỬA · 2 GỢI Ý · Hook 35/35 → `phan-bien-v2/agy/agy-phan-bien.txt`
**R2 · Opus** (ngữ cảnh mới): ĐẠT CÓ SỬA · **0 CHẶN** · 5 NÊN SỬA · 7 GỢI Ý · Hook 32/35 · **Risk Score 10/10 (PUBLISH)** → `phan-bien-v2/opus/opus-phan-bien.md`

## Quyết định
| E | Nguồn | Câu gốc → quyết định | Căn cứ |
|---|---|---|---|
| E1 | R1 · R2 | Câu nhử Loop #2 "doesn't need a stem at all" trùng với peperomia (cũng giâm lá) và có phép đối lập không nguồn → **NHẬN**: câu nhử thành "the last plant… turns one single leaf into a whole new plant"; cầu nối 8→9 thành "works the same way" | C12 |
| E2 | R2 | "Indoors, step up one habit" (cây nhóm A cũng ở trong nhà) → **NHẬN**: "In a warm house…" | C06, D03 |
| E3 | R1 · R2 | Swedish ivy "three to five inches [C05]" → **NHẬN**: bỏ số, nói "cut just like the coleus" | C33 (không có độ dài) |
| E4 | R2 | Swedish ivy không có câu thú cưng, mà lại là "cousin" của coleus → **NHẬN**: nói rõ không tìm thấy trên danh sách, đặt ly lên cao như coleus | không có dòng ASPCA cho Swedish ivy |
| E5 | R1 | Peperomia "Water on the stem" trong khi giâm bằng cuống → **NHẬN**: "stem or stalk" | C12 |
| E6 | R1 | "One safety note before you start" đặt sau phần hướng dẫn → **NHẬN**: "One safety note for pet owners." | — |
| E7 | R2 GỢI Ý | Cảnh kết "kitchen window" trái với luật ly để chỗ cao + tránh nắng trực tiếp → **NHẬN**: "a bright shelf" | C36, C25 |
| — | R1 | "[C35] không có trong ledger" → **BÁC**: C35 có trong ledger, chỉ bị cắt khỏi bản prompt rút gọn đưa cho Agy | research-brief A · C35 |
| — | R1 | Bỏ "In spring and summer" khỏi câu hoya → **BÁC**: bảng 9 cây ghi RHS lấy cành vào xuân/hè; R2 vòng 1 yêu cầu có bối cảnh mùa | C14 · bảng 9 cây |
| — | R2 GỢI Ý (6) | "call your vet", lặp chữ "So", ý "chậm" lặp, cuống lá gãy sát phiến… → không áp (giọng/nhịp) | — |
| H | R2 cảnh báo dựng | Header: thẻ ASPCA chuyển sang mục 1, cập nhật câu Loop #2, tên RHS chỉ lên thẻ. Bảng 9 cây khi dựng: hàng 5 = Swedish ivy · hàng 4 "2–3 weeks" là lúc trồng, không phải lúc ra rễ · độ dài rễ African violet ghi 1″ | outline + brief |

**Sau sửa:** `gate.py --nhan sau-phan-bien-v2` PASS → TTS clean (bỏ tiêu đề mục, thẻ [GFX]; số đã viết bằng chữ) → `gate.py --nhan tts-clean` **PASS** (1.781 từ ≈ 10,8′). Không còn lỗi CHẶN → không chạy vòng 3.
