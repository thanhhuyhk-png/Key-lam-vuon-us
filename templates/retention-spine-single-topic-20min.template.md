---
file: retention-spine.md  (biến thể SINGLE-TOPIC 20–24′ — 7 phần)
role: Thay bảng Pha B của packaging-retention-playbook khi LANE A single-topic và video_length ≥18′.
lane: BIG IDEA (Lane A) · mọi format không phải listicle (Problem-Fix · Once-Recurring · Value-Number · Transformation)
gate: 🔴 GATE 2.5 — duyệt bảng này TRƯỚC khi viết prose
source: packaging-retention-playbook-en.md (Pha A/C/D giữ nguyên) + channel.config.json video_length (2026-10-23)
created: 2026-10-23
---

# Retention Spine — SINGLE-TOPIC 20–24′ (7 phần)

> **Vì sao cần bảng riêng.** Bảng Pha B gốc kẻ cho 8–10′: một loop lớn qua phút 4–6 rồi hết.
> Ở 20+ phút, người xem có **gấp đôi số lần muốn rời**. Watch-budget thật của kênh ~195s
> (audit 2026-07) — tức phần lớn người xem sẽ rời trước phút 4 dù video dài bao nhiêu. Bảng này
> không cứu được điều đó; nó chỉ bảo đảm **người đã ở lại không bị đẩy ra** bởi một phần dài
> không có lý do ở lại. Đo sau 3 video: `views_5d` vs median 285 + tổng giờ xem (memory 2026-10-23).

**Video:** … · **Format:** … · **Tổng từ mục tiêu:** đọc `video_length` (3.300–4.000) · **wpm:** 165 (Key gardent)
**Quy đổi:** word index ÷ 2,75 = giây · 480 từ ≈ 2′55″

---

## PHẦN 1 — NGÂN SÁCH TỪ + MỐC THỜI GIAN

| Khối | Từ mục tiêu | Mốc (≈ @165wpm) | Vai trò |
|---|---|---|---|
| Hook | 95–125 | 0:00–~0:40 | Hook đã chọn ở [2] — không viết lại. **Mốc các phần dưới dịch theo độ dài hook thật** (word idx ÷ 2,75). Hook ngắn → vùng chết giây 40–55 rơi vào đầu M1: M1 phải mở bằng **giá trị**, không giới thiệu (L15) |
| **M1** | 450–520 | ~0:40–3:35 | Giao mảnh LỚN của lời hứa title **<60s** (L3) · `ACTION_TIP` lần đầu (≤3:00, L16) |
| **M2** | 450–520 | 3:40–6:35 | 🔴 nằm đè vùng dip phút 4–6 (L5) → Loop #2 phải mở trước 4:00, đóng sau 6:00 |
| **M3** | 450–520 | 6:35–9:30 | Science moment + Consensus Synthesis #1 |
| **M4** | 450–520 | 9:30–12:25 | Re-hook giữa video (nói thẳng với nhóm định rời) |
| **M5** | 450–520 | 12:25–15:20 | ⭐ Ứng viên trả **Loop #1** (bí mật lớn từ hook) |
| **M6** | 450–520 | 15:20–18:15 | ⭐ Ứng viên trả Loop #1 · nếu đã trả ở M5 → **lời hứa cuối** phải đang mở |
| **M7** | 450–520 | 18:15–21:10 | Trả lời hứa cuối · kế hoạch áp dụng (không đọc lại số — L18) |
| Kết | ~100 | 21:10–21:50 | forward-visual close · identity CTA · mantra 3 nhịp · `Happy gardening.` |

Tổng: 125 + 7×(450–520) + 100 = **3.375–3.865 từ**. Không đạt sàn vì đã giao hết → chấp nhận, ghi chú tại GATE. **Không pad.**

---

## PHẦN 2 — CÁC LOOP (tối đa 2–3 loop mở cùng lúc)

| Loop | Câu gieo (nguyên văn) | Gieo ở | Trả ở | Người xem không đoán trước được vì |
|---|---|---|---|---|
| **#1 — bí mật lớn** (từ hook) | | Hook, <0:45 | M5 hoặc M6 | |
| **#2 — bắc qua dip** | | M1 cuối hoặc M2 đầu (<4:00) | M3 (>6:00) | |
| **Lời hứa cuối** | | phần trả Loop #1 | M7 | |

> Sau khi Loop #1 được trả, nợ = 0 → phần còn lại sống nhờ **lời hứa cuối**. Thiếu hàng này = 6 phút cuối không có lý do ở lại.
> Dạng gợi ý cho lời hứa cuối: sai lầm làm hỏng cả cách này · science correction (chỗ khoa học không ủng hộ mẹo phổ biến) · phép tính chi phí cả mùa.

---

## PHẦN 3 — BẢNG 7 PHẦN (mỗi phần 3 nhịp giữ chân ≈ mỗi 60–90s)

Mỗi phần có cấu trúc cố định: **mở (lý do ở lại, 1 câu) → nội dung A + "Here's why this works" → NHỊP GIỮA PHẦN (~90s) → nội dung B (từng bước, liều lượng) → CẦU NỐI (vấn đề mới, không tóm tắt)**.

| Phần | Tên / nội dung chuyên môn | Ví dụ Mỹ (zone · vật tư · giá "give or take") | Claim (mã research-brief) | Nhịp giữa phần (loại + câu) | Cầu nối cuối phần → vấn đề mới | Cờ |
|---|---|---|---|---|---|---|
| M1 | | | | | | L3 · L16 |
| M2 | | | | | | 🔴 L5 |
| M3 | | | | | | |
| M4 | | | | | | re-hook |
| M5 | | | | | | ⭐ |
| M6 | | | | | | ⭐ |
| M7 | | | | | | — (không cầu nối; dẫn vào Kết) |

**Loại nhịp giữa phần** (xoay vòng, không dùng cùng loại 2 phần liền nhau): sai lầm phổ biến lộ ra · scene viewer-POV / Story Bank · con số bất ngờ có nguồn · bảng đối chiếu [GFX] · câu hỏi người xem tự kiểm · mini-loop đóng ngay trong phần.

**Cầu nối — luật:** đóng ý cũ bằng **một vế** → mở **một vấn đề mới cụ thể**. ⛔ "So now you know…", "To recap…", "Number three." đứng trơ. Con số trong câu cầu nối phải có mã nguồn — không bịa kiểu "wipes out 80% of gardens".

---

## PHẦN 4 — PHÂN BỔ BẮT BUỘC (ghi phần nào chứa)

| Yếu tố | Số lượng | Ở phần |
|---|---|---|
| Sai lầm phổ biến ("3 mistakes") | 3 | |
| So sánh chi phí DIY vs mua (Home Depot/Lowe's/Tractor Supply) | ≥1 | |
| Câu an toàn thú cưng / cháu nhỏ | ≥1 | |
| Nhắc USDA zone | ≥2 | |
| Consensus Synthesis | ≥2 | M3 + 1 phần khác |
| Story Bank (chuyện có thật, có nguồn) hoặc viewer-POV scene | 1–2 | |
| Accessibility anchor ("just 1 tablespoon", "30 seconds") | 2–3 | |
| Re-hook giữa video | 1 | M4 |
| Climax beat (đỉnh duy nhất) | 1 | M5 hoặc M6 |

**🖋️ Editorial Signature (L13 — bắt buộc):** *(loại · phần · nguồn — brand-voice-dna §Authenticity Guard C)*
> …

**🔒 Claim-scoping (CR4):** câu nói rõ chỗ cách này KHÔNG hiệu quả (zone/đất/mùa):
> …

---

## PHẦN 5 — PHA D (cộng thêm cho 20+ phút)

Giữ nguyên L3/L4/L5/L6 + L11–L18 của Pha D gốc. Bản nháp script giữ tiêu đề `### M1 …` đến `### M7 …` và `### KẾT` cho tới sau Pha D (TTS clean ở Bước 2.3 mới bỏ).

```python
import re, json
cfg = json.load(open(r"D:\0002-Team A Nam\channel.config.json", encoding="utf-8"))["video_length"]
LO, HI = cfg["target_words_min"], cfg["target_words_max"]
tts = re.search(r"## TTS SCRIPT\s*(.*)", open(PATH, encoding="utf-8").read(), re.DOTALL).group(1)
W = lambda s: len(re.sub(r"[#*\-`>\[\]()_]", " ", s).split())
parts = re.split(r"^###\s*(M\d|Q|KẾT)\b.*$", tts, flags=re.M)   # Q = "Your questions" (tùy chọn, ~150–200 từ, đặt trước KẾT)
mods = {k: v for k, v in zip(parts[1::2], parts[2::2]) if k not in ("KẾT", "Q")}
for k, v in mods.items():
    n = W(v); print(f"{k}: {n} từ", "OK" if 430 <= n <= 560 else "LỆCH (mục tiêu 450–520)")
print("số phần:", len(mods), "OK" if len(mods) == 7 else "FAIL: cần 7")
total = W(re.sub(r"^###.*$", "", tts, flags=re.M))
print(f"tổng {total} từ ≈ {total/165:.1f}′ @165 ->", "OK" if LO <= total <= HI else f"LỆCH ({LO}–{HI})")
def at(cue):
    i = tts.lower().find(cue.lower()); return W(tts[:i]) / 2.75 if i >= 0 else -1   # không phân biệt hoa/thường
LOOP1_SEED, LOOP1_PAY = "...", "..."      # dán nguyên văn
LOOP2_SEED, LOOP2_PAY = "...", "..."
FINAL_SEED, FINAL_PAY = "...", "..."
def where(cue):                    # phần chứa câu: "HOOK" | "M1".."M7" | "KẾT" | None
    for k, v in {"HOOK": tts.split("### M1")[0], **mods}.items():
        if cue.lower() in v.lower(): return k
    return None
print("Loop#1 gieo trong HOOK & trả ở M5/M6:", where(LOOP1_SEED) == "HOOK" and where(LOOP1_PAY) in ("M5", "M6"))
print("Loop#2 gieo ở M1/M2 trước 4:00 & trả ở M3 (sau 6:00):", at(LOOP2_SEED) < 240 and where(LOOP2_PAY) == "M3" and at(LOOP2_PAY) > 360)
print("Lời hứa cuối gieo ở M5/M6, trả ở M7:", where(FINAL_SEED) in ("M5", "M6") and where(FINAL_PAY) == "M7")
```

| Check | Ngưỡng | Kết quả |
|---|---|---|
| 7 phần, mỗi phần 450–520 từ (cho phép 430–560) | | |
| Tổng từ trong `video_length` | 3.300–4.000 | |
| Loop #1 gieo <0:45, trả ở M5/M6 | | |
| Loop #2 gieo <4:00, trả >6:00 (L5) | | |
| Lời hứa cuối mở khi Loop #1 đóng, trả ở M7 | | |
| 6 câu cầu nối (M1–M6) đều mở **vấn đề mới**, 0 câu tóm tắt | đọc tay | |
| Nhịp giữa phần không trùng loại 2 phần liền nhau | đọc tay | |
