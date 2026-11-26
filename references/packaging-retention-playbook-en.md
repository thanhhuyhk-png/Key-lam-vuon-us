---
type: playbook (per-workspace) — KHÔNG auto-load mỗi video; orchestrator gọi tại GATE 2.5
applies: Garden US (garden-us-60k) · English
goal: kéo AVD 25.6% → 40% bằng packaging-first (thiết kế giữ-chân TRƯỚC khi viết, không vá ở audit)
derived_from: channel-stats AUDIT TL;DR (drop zones) + lessons-learned L1–L6 + title-keyword-strategy-en.md (POWER LEXICON/DELIVERY-LOCK)
last_updated: 2026-06-24
---

# Packaging → Spine (P2S) Playbook — Garden US

> Nguyên lý: **Package = lời hứa. AVD = đo bạn có GIỮ lời hứa đủ nhanh + đủ liên tục không.**
> Lỗi chết AVD #1 của kênh = title hứa nhưng 60s đầu không giao (L3). P2S chốt lời hứa + bộ xương
> giữ-chân TRƯỚC khi viết → leak bị thiết kế-loại-bỏ, audit chỉ còn là kiểm định cuối.

## CHECKPOINT CỐ ĐỊNH CỦA KÊNH (số thật — không đổi giữa các video)
- Hook cliff: cumulative loss giây 2→25% **trung bình -37%** (hook yếu = vấn đề kênh).
- 🔴 **DROP ZONE = giây 40–55** (hook→credibility). [L4]
- 🔴 **MID-ROLL DIP = phút 4–6** (~50–70% timeline). [L5]
- Quy đổi: **word index ÷ 2.5 = giây** @150wpm (≈ ÷2.33 @140wpm nhịp seniors).

---

## PHA A — PROMISE DECOMPOSITION (sau khi chốt Title C + thumbnail)
Mổ package thành lời hứa, mỗi cái BẮT BUỘC có điểm giao:

| Thành phần | Giá trị video này | Giao ở (mốc) |
|---|---|---|
| Core promise | … | xuyên suốt |
| Number/scope | … | … |
| **Implicit question = Open Loop #1** | … | đóng ở … |
| Timeframe (nếu có) | … | … |

**EDITORIAL SIGNATURE (L13 — bắt buộc, thêm 2026-10-09):** ghi 1 hàng riêng trong bảng Spine: loại (bảng đối chiếu nguồn · phép tính riêng · dòng thời gian tổng hợp · Q&A comment thật · kiểm chứng mẹo) + vị trí (science moment hoặc vùng dip) + nguồn. Thiếu hàng này → Spine chưa xong.

**DELIVERY-LOCK (HYBRID_RULE #4):** mọi OUTCOME/TIMEFRAME ở title phải (a) có claim trong research-brief.md, (b) có điểm giao <60s. FAIL → đổi từ ở title NGAY, không để tới audit.

---

## PHA B — RETENTION SPINE (điền TRƯỚC khi viết prose)
Bảng tái dùng — copy & điền cho từng video:

| Mốc | Open loop ĐANG mở | Payoff/giá trị giao | Pattern-break | Word idx mục tiêu |
|---|---|---|---|---|
| 0:00–0:30 Cold open | gieo Loop #1 | 1 mảnh payoff NGAY (số/đòn đau) | — | 0–75 |
| 0:15–0:20 🔴 L6 *(chỉ khi title = claim ngược đời/sốc)* | — | bằng chứng/con số chứng minh claim (vùng chết claim-sốc = giây 20–33, KHÔNG đợi tới 40) | — | ~38–50 |
| ≤0:45 🔴 L24 | Loop #1 còn sống | **bước làm đầu tiên / mục #1** (`FIRST_STEP`) — lý thuyết nhúng vào bước, không đứng trước | — | ≤124 |
| 0:40–0:55 🔴 L4 | Loop #1 còn sống | re-tease / micro-payoff (KHÔNG intro) | — | ~100–140 |
| ~1:00 L3 | … | giao mảnh LỚN của lời hứa title | — | ~150 |
| mỗi 60–90s | đóng cũ + mở mới (Jenga) | … | transition rõ | — |
| 2:30–4:00 🧪 L22 | … | **câu hỏi bình luận** về hoàn cảnh người xem (`COMMENT_Q`) — ngay sau một payoff, không xin like/sub | — | ~410–660 |
| 4:00–6:00 🔴 L5 | 1 loop LỚN còn mở | item/"the trick" mạnh nhất đáp ở đây | pattern-break | ~600–900 |
| trước Ending | — | gọi lại `ACTION_TIP` bằng **1 câu** (L16) — không đọc lại cả quy trình | — | — |
| Ending 🔴 L23 | đóng Loop #1 | ≤20 s / ≤55 từ (`ENDING_FROM`): identity CTA + câu hỏi + mantra 3-nhịp + Happy gardening. — không tóm tắt, không tả cảnh | — | cuối |

Quy tắc: tối đa 2–3 loop chồng (nhiều hơn = rối). Mỗi loop PHẢI đóng (đừng hứa hão).
🔴 **L27 (22/11/2026): mỗi loop ghi giờ gieo · (trả một phần) · trả; khoảng giữa hai mốc liền nhau ≤ 180 s.** Mốc giữa là **trả một mảnh đáp án thật**, không phải câu nhắc «nhớ đợi…». Bảng Spine có loop treo > 3′ = Spine **chưa xong** — kéo đáp án lên, chèn trả-một-phần, hoặc đừng gieo loop đó sớm. Script chép đúng các mốc này vào header `LOOP: <cụm gieo> .. [<cụm trả một phần> ..] <cụm trả>` để `script_lint.py` đo.

> 🔀 **Video 20+ phút (thêm 2026-10-23):** khi `video_length.target_minutes` ≥18 và video là single-topic
> (Lane A, không phải listicle) → **KHÔNG dùng bảng trên**. Dùng `templates/retention-spine-single-topic-20min.template.md`:
> 7 phần × 450–520 từ, mỗi phần 3 nhịp giữ chân (mở · nhịp giữa phần · cầu nối sang vấn đề mới), Loop #1 trả ở M5/M6,
> Loop #2 bắc qua phút 4–6, **lời hứa cuối** giữ 6 phút cuối. Listicle 20+′ vẫn dùng `retention-spine-listicle`.

---

## PHA C — WRITE TO THE SPINE
- Hook skill + youtube-garden-us viết **bám từng hàng spine**, không free-form.
- Mỗi đoạn prose khớp 1 checkpoint; đoạn nào không phục vụ checkpoint nào → cắt.
- Signposting cho seniors: "setup #4 is next" / "here's the second one" → giảm confusion-drop.

### Pha C′ — VIẾT THEO LÔ (bắt buộc khi video ≥18′, thêm 2026-10-23)
Viết một mạch 3.500 từ thì phần sau loãng dần (lặp ý, cầu nối thành tóm tắt, số liệu trôi khỏi research-brief).
Chia 4 lô, mỗi lô lưu nối vào `script.md` rồi tự kiểm trước khi viết lô sau:

| Lô | Gồm | Từ ≈ |
|---|---|---|
| 1 | Hook + M1 + M2 | ~1.100 |
| 2 | M3 + M4 | ~970 |
| 3 | M5 + M6 | ~970 |
| 4 | M7 + Kết | ~590 |

**Tự kiểm cuối mỗi lô** (1 dòng báo cáo, sửa ngay nếu FAIL): số từ từng phần trong 450–520 · mọi số có mã claim research-brief ·
0 AI-ism / 0 "I / my garden" · contractions ≥60% · câu cầu nối mở vấn đề mới (không tóm tắt) · loop nào đang mở, loop nào vừa đóng ·
**đọc lại 2 câu cuối của lô trước** trước khi viết lô mới (để nối giọng, không mở đầu lại).
Mặc định dừng mềm sau mỗi lô chờ "tiếp"; user nói "viết liền" → chạy hết 4 lô, vẫn tự kiểm từng lô.

---

## PHA D — VERIFY CƠ HỌC (chạy TRƯỚC audit nặng)
Bắt L3/L4/L5 ở thiết kế. Snippet (đổi path script):

```python
import re
tts = re.search(r"## TTS SCRIPT\s*(.*)", open(PATH,encoding="utf-8").read(), re.DOTALL).group(1)
W = lambda s: len(re.sub(r"[#*\-`>\[\]()_]"," ",s).split())
total = W(tts); sec = lambda i: W(tts[:i])/2.5
# L3: value lớn giao < giây 60 ? -> tìm điểm payoff đầu (đánh dấu tay bằng cụm khoá, vd "setup one"/"step one"/"here's why")
for cue in ["setup one","step one","here's why this works","number one"]:
    i = tts.lower().find(cue)
    if i>0: print(f"[L3] '{cue}' @ giây ~{sec(i):.0f}  (mục tiêu <60)"); break
# L4: có loop-cue sống quanh giây 40-55 ?
print("[L4] cụm giây 40-55:", [c for c in ["coming up","step ","number ","the trick","we get to"] if any(40<=sec(m.start())<=58 for m in re.finditer(re.escape(c),tts.lower()))])
# L6: title claim ngược đời -> bằng chứng/số phải xuất hiện < giây 20 (tìm digit/percent/số viết chữ trong 50 từ đầu)
head20 = " ".join(tts.split()[:50]).lower()
proof = re.findall(r"\d+|percent|degrees|dollar|inches|days|weeks|half|double|twice", head20)
print(f"[L6] bằng chứng trước giây 20: {proof if proof else '❌ KHÔNG CÓ — nếu title là claim sốc thì FAIL (vùng chết 20-33s)'}")
# độ dài
print(f"[len] {total} từ ~ {total/150:.1f}'@150 ({total/140:.1f}'@140)")
```

Checklist Pha D (PASS hết mới qua):
- [ ] Title claim ngược đời → bằng chứng/số trước giây 20 (L6 — vùng chết 20–33s)
- [ ] Value LỚN giao < giây 60 (L3)
- [ ] Có loop-cue sống tại giây 40–55 (L4)
- [ ] Có loop chưa đóng vắt qua phút 4–6 (L5)
- [ ] DELIVERY-LOCK: mọi outcome title có claim brief + điểm giao
- [ ] **L12 chống khuôn:** `python tools/originality_check.py <script.md>` → ≤3 câu trùng nguyên văn với mỗi script trong 5 gần nhất (exit code 0); tiêu đề bước / đoạn kết / identity CTA / câu tease viết riêng. **Lane B / có mẫu dán:** tool tự so thêm với `seed-transcript.*` trong folder (≤1 câu trùng · ≤2% 6-gram), thêm `--allow "<tài sản khoá>"`
- [ ] **L11:** 0 nhân chứng/người thân bịa, 0 câu "Trust me"/"I mean it"
- [ ] **L13:** Editorial Signature của Spine đã xuất hiện trong script, đúng vị trí
- [ ] **L14–L18 tự động:** `python tools/script_lint.py <script.md> [--wpm 165]` → exit 0. Kiểm: tên nguồn ≤1/90s và ≤2/30s (L14) · giây 38–60 không lộ trình/danh sách nguồn (L15) · `ACTION_TIP` lần đầu ≤3:00 + gọi lại cuối bài (L16) · chữ hứa trên title không bị script phủ định (L17) · không đọc lại ≥4 cụm số đã nói (L18). Header script khai: `ACTION_TIP:` (bắt buộc) · `CITE_ZONE:` / `RECAP_OK:` / `PROMISE_OK:` (khi cần, kèm lý do)
- [ ] Độ dài khớp chất, trong `video_length` của config (từ 2026-11-10: 10–14′ / 1.650–2.300 từ — đừng pad; bản 20–24′ của 23/10 đã thôi; audit 2026-07: watch-budget thật ~195s). Video 20+′ chạy thêm Pha D của `retention-spine-single-topic-20min` (7 phần · loop #1/#2/lời hứa cuối)

---

## 4 LEVER AVD packaging-first mở khoá
1. **Clickability ÷ Deliverability:** chỉ greenlight package giao được nhanh. CTR cao + không giao = clickbait penalty (vd "STOP Pesticides" 30k view, AVD 20.6%).
2. **Độ dài khớp chất:** AVD% rớt khi pad. Audit 2026-07: watch-budget ~195s → 9′ cùng nội dung = AVD 33–36% vs 16′ = ~20%. **Từ 2026-10-23 user chốt 20–24′** (config `video_length` thắng) → bù bằng spine 7 phần + viết theo lô, chấm bằng `views_5d` + tổng giờ xem, không bằng AVD%.
3. **Open loop ĐÓNG được** (Curiosity-closed — POWER LEXICON), không bait.
4. **Signposting** cho 60–80: luôn báo "đang ở đâu / cái kế tiếp".

---

## SLOT VÀO PIPELINE — GATE 2.5
```
[2] hook → [2.5] 🆕 RETENTION SPINE GATE (Pha A+B, chốt với user)
        → [3] script viết-bám-spine (Pha C) → Pha D verify cơ học → audit
```
Orchestrator đọc CLAUDE.md (mục Pipeline) thấy [2.5] → dừng GATE trình Promise Decomposition + bảng Spine cho user duyệt TRƯỚC khi viết script. Audit Bước 3 từ "thợ vá" thành "kiểm định cuối".
