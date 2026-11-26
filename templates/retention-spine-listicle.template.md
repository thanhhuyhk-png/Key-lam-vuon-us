---
file: retention-spine.md  (biến thể LISTICLE)
role: Thay Pha B của packaging-retention-playbook khi chạy lane REMAKE / định dạng đếm ngược.
lane: REMAKE
gate: 🔴 GATE 2.5 — duyệt bảng này TRƯỚC khi viết prose
source: references/packaging-retention-playbook-en.md (Pha A/C/D giữ nguyên) + remake-playbook-en.md §R4
---

# Retention Spine — biến thể LISTICLE

> **Vì sao phải đổi bảng:** Pha B gốc kẻ theo **mốc thời gian tuyệt đối** (0:40–0:55, phút 4–6) vì
> thiết kế cho video **một chủ đề**. Ở listicle, drop zone không nằm ở phút 4–6 — nó nằm ở
> **mọi ranh giới giữa hai mục**. Nên bảng phải kẻ theo **mục**, và micro-bridge phải phủ **100%**
> ranh giới thay vì vá một mốc.

---

## PHẦN 1 — COLD OPEN (giữ nguyên checkpoint kênh, KHÔNG đổi)

Ba mốc này thuộc cold open, không thuộc thân bài → luật cũ vẫn đúng nguyên.

| Mốc | Luật | Word idx | Nội dung video này |
|---|---|---|---|
| giây 0–25 · hook cliff *(-37% TB kênh)* | Đọc thẳng **mảnh sensory** — đúng chữ trong title | 0–60 | |
| 🔴 giây ~20 · **L6** | Claim sốc phải có bằng chứng/số **trước giây 20** | ~38–50 | |
| 🔴 giây 40–55 · **L4** | Loop còn sống — ở đây là **3 vòng lặp mở bằng SỐ THỨ TỰ**, ⛔ KHÔNG phải intro/preview | ~100–140 | |

**Ba vòng lặp số thứ tự** *(mẫu: "Number 16 tastes like fried oysters and it never once saw the ocean. Number 12 is why Congress stepped in on Christmas Eve 1970. And number 2 is the root that tastes like apple and honey.")*

> 🔴 **L27:** mỗi loop ghi giờ gieo → (trả một phần) → đóng; khoảng giữa hai mốc ≤ 180 s, không thì Spine chưa xong. Script khai lại ở header `LOOP:`.

| Loop | Mục số | Câu tease | Đóng ở |
|---|---|---|---|
| #1 | | | |
| #2 | | | |
| #3 *(= payoff title)* | **#2** | | mục #2 |

---

## PHẦN 2 — BẢNG MỤC (thay hoàn toàn phần thân của Pha B)

Mỗi mục **bắt buộc đủ 5 nhịp + 1 micro-bridge**. Điền hết trước khi viết prose.

| # | Mục | N1 · hình ảnh bà | N2 · nó cho gì | N3 · ai giết nó *(năm + tên + tổ chức)* | N4 · giá $ hôm nay | N5 · lưu ý an toàn | ✅ Micro-bridge → mục sau | PB |
|---|-----|---|---|---|---|---|---|----|
| 20 | | | | | | | | |
| 19 | | | | | | | | |
| 18 | | | | | | | | |
| 17 | | | | | | | | |
| 16 | | | | | | | | 🔶 1/4 |
| 15 | | | | | | | | |
| 14 | | | | | | | | |
| 13 | | | | | | | | |
| 12 | | | | | | | | |
| 11 | | | | | | | | 🔶 1/2 |
| 10 | | | | | | | | |
| 9 | | | | | | | | |
| 8 | | | | | | | | |
| 7 | | | | | | | | |
| 6 | | | | | | | | 🔶 3/4 |
| 5 | | | | | | | | |
| 4 | | | | | | | | |
| 3 | | | | | | | | |
| **2** | **← PAYOFF TITLE** | | | | | | | |
| **1** | **KHÔNG phải một cây** — là toàn bộ khu vườn/hệ đứng cùng lúc → identity close | | | | | | — | |

> Xoá bớt hàng nếu làm 15–18 mục. Giữ nguyên: payoff ở **#2**, #1 là identity close, 3 pattern break.

**🔶 Pattern break** — dừng đếm, tuyên bố lại phần thưởng còn lại:

| Vị trí | Nội dung |
|---|---|
| 1/4 | |
| 1/2 | |
| 3/4 | *(mẫu: "Three left. Number five rebuilds the ground under your feet. Number two is the root off the top of this whole thing.")* |

**💬 Câu hỏi bình luận** *(🧪 L22 — đặt ở **2:30–4:00**, ngay sau một mục vừa trả; khai `COMMENT_Q:` ở header script; bình luận ghim hỏi lại đúng câu này)* — hỏi về hoàn cảnh hoặc ký ức của người xem, không hỏi về kỹ thuật, không xin like/sub:
> *(mẫu: "Did your grandmother bake on the same day every week? Tell me which day it was down in the comments.")*
> *(mẫu hoàn cảnh: "Which of these is already in your yard? Tell me in the comments.")*

**🎯 Kết ≤20 s / ≤55 từ** *(🔴 L23 — khai `ENDING_FROM:`; không đọc lại danh sách, không tả cảnh)* — hành động nhỏ nhất làm được hôm nay + mantra + `Happy gardening.`:
> *(mẫu: "Pick one. Not the whole list. One.")*

**🥇 Mục đầu tiên ≤ giây 45** *(🔴 L24 — khai `FIRST_STEP:` = câu mở mục đầu tiên được đếm)*.

---

**🖋️ Editorial Signature (L13 — bắt buộc):** *(loại · vị trí beat · nguồn — xem brand-voice-dna §Authenticity Guard C)*
> …

## PHẦN 3 — PHA D VERIFY (thêm 2 phép đếm cho listicle)

Chạy TRƯỚC audit nặng. Giữ nguyên check L3/L4/L6 của Pha D gốc, **cộng thêm**:

```python
import re
tts = re.search(r"## TTS SCRIPT\s*(.*)", open(PATH, encoding="utf-8").read(), re.DOTALL).group(1)

# BRIDGE: số micro-bridge PHẢI == số mục (0 ngoại lệ)
bridges = len(re.findall(r"\bThe next (?:one|thing)\b", tts, re.I))
items   = len(re.findall(r"\bNumber (?:\d+|one|two|three)\b", tts, re.I))
print(f"bridge={bridges} items={items} -> {'OK' if bridges >= items-1 else 'FAIL: thieu micro-bridge'}")

# FACT DENSITY: mỗi mục cần >=1 năm 4 chữ số và >=1 dấu $
years = len(re.findall(r"\b(1[89]\d{2}|20[0-2]\d)\b", tts))
money = len(re.findall(r"\$\s?\d", tts))
print(f"years={years} money={money} / items={items}"
      f" -> {'OK' if years>=items*0.8 and money>=items*0.8 else 'FAIL: fact thua'}")
```

| Check | Ngưỡng | Kết quả |
|---|---|---|
| `bridges ≥ items − 1` | 0 ngoại lệ *(mục #1 không cần bridge)* | |
| `years ≥ items × 0.8` | mỗi mục ~1 năm cụ thể | |
| `money ≥ items × 0.8` | mỗi mục ~1 giá $ | |
| L6 · số/bằng chứng < giây 20 | *(Pha D gốc)* | |
| L4 · loop-cue sống giây 40–55 | *(Pha D gốc)* | |

---

## PHẦN 4 — Gate R7 trước khi đăng

Trượt 1 điểm = không đăng. Danh sách đầy đủ 11 điểm ở `references/remake-playbook-en.md` §R7.
