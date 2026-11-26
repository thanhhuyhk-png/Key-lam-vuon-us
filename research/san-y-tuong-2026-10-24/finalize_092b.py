import re, os
D = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/"
tts = open(D + "tts-markers.tmp", encoding="utf-8").read()
tts = re.sub(r"^###.*\n?", "", tts, flags=re.M)          # bo tieu de phan
tts = tts.replace("A 2010 label", "A twenty ten label")      # so -> chu cho TTS
tts = re.sub(r"[*`_#>]", "", tts)                          # bo ky tu markdown con sot
tts = re.sub(r"\n{3,}", "\n\n", tts).strip() + "\n"
assert not re.search(r"\d", tts), "con chu so"
words = len(tts.split())

header = """# Rose Cuttings in a Potato? One Small Study Found No Roots

## SEO
- **Title:** Rose Cuttings in a Potato? One Small Study Found No Roots
- **Tags:** (điền ở bước SEO)

## Thumbnail
- **Text overlay:** `SKIP THE SPUD` (vàng) / `TRY 2 BUDS` (trắng) — concept ở outline.md

## Ghi chú sản xuất (không đọc vào TTS)
- **Trạng thái: TTS CLEAN — chờ GATE user.** Đã qua: Pha D · audit độc lập (REVISE → đã sửa theo nguồn) · Triple F · compliance 9/10 (đã vá khối an toàn bột lên trước phần làm). ~%d từ ≈ %.1f phút @165wpm — **dưới sàn config 3.300 từ/20′ (TEST độ dài)**.
- ACTION_TIP: make three or four cuttings, not one
- CITE_ZONE: Here's where the pages split .. Some of it is plain disagreement.
- Phát âm cần nghe thử: **Khost**, **Clemson**, **thiram** (THY-ram), **ASPCA**, **semi-hardwood**.
- Thẻ nguồn trên màn hình (không đọc bằng giọng): `ONE SMALL STUDY · 2019` (hook) · `Extension talk — "Garden Myths & Legends"` (M1) · `Wali, Shafiqi & Ahmadi · IJIRSS 2(4):55–61 · full text vs summary` (M2) · `Iowa State · NC State · Clemson` (M4) · `ASPCA — Rose (Rosa)` (Q).
- Bảng đồ họa: M2 "Nghiên cứu này cho biết / không cho biết" · M4 "các trang bất đồng" · M5 "bản đồ chứng cứ mẹo bếp".
- Bản có tiêu đề ### M1…KẾT (để chạy lại Pha D): `script.draft-markers.md`.

---

## TTS SCRIPT

""" % (words, words / 165)
open(D + "script.md", "w", encoding="utf-8").write(header + tts)
os.remove(D + "tts-markers.tmp")
bak = D + "script.md.bak-pre-audit"
if os.path.exists(bak):
    os.remove(bak)
print("final words", words)
