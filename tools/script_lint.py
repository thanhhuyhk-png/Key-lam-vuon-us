"""Pha D — kiểm tự động L14–L18 cho script Garden US (lessons-learned.md).

Usage:
    python tools/script_lint.py scripts/big-idea-062-.../script.md [--wpm 165]

Đọc phần `## TTS SCRIPT`, quy đổi vị trí từ -> giây theo --wpm (mặc định 165 = giọng Key gardent đo thật, có dấu ngắt;
nếu dùng giọng khác thì truyền wpm của giọng đó). Kiểm:
  L14  ngân sách trích nguồn: tên tổ chức đọc bằng giọng <= 1 lần / 90 giây; không quá 2 tên trong 30 giây
  L19  cite chung chung ("the guides say", "according to"…) ≤ 1 / 300 từ; cấm tuyệt đối hoá ("every guide", "all agree", "the guides are clear")
  L15  giây 38–60 không có lộ trình / preview / danh sách nguồn
  L16  mẹo hành động (miễn phí, làm ngay) xuất hiện lần đầu <= giây 180 và được gọi lại ở 15% cuối
  L17  chữ hứa trên title ("easy", "fast", "no ...") không bị chính script phủ định
  L18  không đọc lại một chuỗi số đã nói (bảng tổng hợp để hình đảm nhận)
  L22  (TEST, chỉ cảnh báo) câu hỏi bình luận về hoàn cảnh người xem nằm ở 2:30–4:00
  L23  phần kết <= 20 giây (55 từ @165 wpm), không tóm tắt lại quy trình, không tả cảnh
  L24  bước làm đầu tiên / mục #1 <= giây 45
  L27  khoảng cách loop: từ lúc gieo tới lúc trả (hoặc trả một phần) <= 180 giây
Cờ --hook: chấm riêng phần mở (hook.md / bản nháp hook) — bỏ L16 callback, L22, L23, L27 và sàn thành ngữ E7
  (các mục đó là ngân sách cả bài); giữ L14 L15 L17 L18 L19 L24 ĐC và tỷ lệ rút gọn + dấu dân dã của E7.
Khai báo trong phần header của script (trước `## TTS SCRIPT`), mỗi dòng một khóa:
  ACTION_TIP: <cụm từ nguyên văn trong TTS>      (bắt buộc cho L16; thiếu -> FAIL)
  PROMISE_OK: <chữ hứa> — <lý do>                 (bỏ qua L17 cho chữ đó, phải có lý do)
  CITE_ZONE: <cụm mở> .. <cụm đóng>               (vùng Editorial Signature được phép gọi tên dày, vd bảng bất đồng)
  RECAP_OK: <cụm mở> .. <cụm đóng>                (đoạn kế hoạch áp dụng được nhắc lại số; KHÔNG dùng cho bảng tổng hợp)
  FIRST_STEP: <cụm nguyên văn>                    (bắt buộc cho L24; thiếu -> FAIL)
  ENDING_FROM: <cụm nguyên văn mở phần kết>       (bắt buộc cho L23; thiếu -> FAIL)
  COMMENT_Q: <cụm nguyên văn câu hỏi bình luận>   (L22 — thiếu chỉ cảnh báo)
  LOOP: <cụm gieo> .. [<cụm trả một phần> ..] <cụm trả>   (L27, mỗi loop 1 dòng; bắt buộc ≥1 dòng; mỗi
        khoảng giữa hai mốc liền nhau <= 180 s. Mốc giữa phải là TRẢ MỘT PHẦN, không phải câu nhắc «nhớ đợi…»)
Exit code 1 nếu có FAIL.
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SOURCES = [r"new hampshire", r"illinois", r"maryland", r"utah state", r"penn state", r"cornell", r"purdue", r"rutgers",
           r"clemson", r"texas a&m", r"oregon state", r"michigan state", r"ohio state", r"iowa state", r"minnesota",
           r"wisconsin", r"colorado state", r"nc state", r"virginia tech", r"uc davis", r"usda", r"epa", r"cdc", r"fda",
           r"aspca", r"university of [a-z]+"]
SRC_RE = re.compile(r"\b(" + "|".join(SOURCES) + r")\b(?:'s)?(?:\s+extension)?", re.I)
GENERIC_CITE_RE = re.compile(
    r"\b(?:the|every|all|most|these|those)\s+(?:university\s+|extension\s+)?(?:guides?|sources?|studies|researchers|experts|guidelines)\b"
    r"|\b(?:guides?|sources?|experts?|extension (?:offices?|services?))\s+(?:all\s+)?(?:say|says|agree|agrees|are clear|recommend\w*|suggest\w*|warn\w*|confirm\w*)\b"
    r"|\b(?:university|extension|one|the|a|that|those|these|two|three|four|no)\s+pages?\b|\bpages?\s+(?:says?|adds?|warns?|covers?|compares?|behind)\b"
    r"|\b(?:we|nothing)\s+(?:couldn't|didn't|could not|did not)\s+find\b|\bin what we read\b|\bwe (?:read|checked|found)\b"
    r"|\baccording to\b|\b(?:research|studies|experts)\s+(?:show|shows|say|says)\b", re.I)
OVERCLAIM_RE = re.compile(
    r"\b(?:every|all)\s+(?:university\s+|extension\s+)?(?:guides?|sources?|studies|experts)\b"
    r"|\b(?:the\s+)?(?:guides|sources|experts)\s+(?:all\s+agree|are clear)\b|\beveryone agrees\b", re.I)
PREVIEW_RE = re.compile(r"here's the plan|in this video|we'll cover|by the end of this video|first,? the .{0,40}then|"
                        r"here's what we'll|let's get started|coming up in this video|nearly everything here comes from|"
                        r"everything here comes from university|then the seven vegetables|then one table|first,? the light itself",
                        re.I)
PROMISE = {
    "easy": r"\bslow\b|patience|\bfussy\b|sources (?:don't|do not) say|could not find|couldn't find|best under (?:grow )?lights?|"
            r"plan on a lamp|(?:ten|eleven|twelve|fourteen|sixteen) weeks|three months",
    "fast": r"\bslow\b|patience|(?:ten|eleven|twelve) weeks|three months|wait longer",
    "quick": r"\bslow\b|patience|(?:ten|eleven|twelve) weeks|three months|wait longer",
    "no lamp": r"need(?:s)? a lamp|plan on a lamp|grow lights?",
    "no light": r"need(?:s)? a lamp|plan on a lamp|grow lights?",
    "no soil": r"potting mix|\bsoil\b",
    "foolproof": r"fail|failure|won't work",
    "guaranteed": r".",
    "never": r".",
    "always": r".",
}
NUMW = ("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen "
        "eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred").split()
NUM_RE = re.compile(r"\b(?:\d+(?:\.\d+)?|(?:" + "|".join(NUMW) + r")(?:-(?:" + "|".join(NUMW[:9]) + r"))?)\b", re.I)


# ---------- E7 giọng dân dã ----------
E7_RUT_GON_FAIL = 0.40     # câu ≥ 5 từ có dạng rút gọn (don't, here's…): dưới mức này FAIL
E7_RUT_GON_MUC_TIEU = 0.50  # mục tiêu; 4 kịch bản mẫu người thật (voice-samples) đo 39–49 % (22/11/2026)
E7_THANH_NGU_MIN = 1        # dưới mức này FAIL
E7_THANH_NGU_MUC_TIEU = 2   # dưới mức này cảnh báo
E7_DAN_DA_MIN = 1
E7_SACH_TREN = 600          # chữ sách vở: tối đa 1 chỗ / 600 từ (tối thiểu 2 chỗ) trước khi FAIL
E7_KHONG_RUT_GON_TREN = 400  # «do not», «it is»…: quá 1 chỗ / 400 từ thì cảnh báo (người thật vẫn nói 2–16 chỗ/bài)
E7_GIONG_TAI_LIEU = 4.0     # chữ «table/page/source/rated…» trên 1.000 từ: vượt thì cảnh báo
E7_GIONG_TAI_LIEU_FAIL = 10.0  # vượt thì FAIL (mẫu người thật 0; bài 099 là 12,5)
RE_RUT_GON = re.compile(r"\b\w+(?:'|’)(?:s|re|ll|ve|d|t|m)\b|\b(?:gonna|wanna|gotta|kinda|lemme|ain't)\b", re.I)
RE_KHONG_RUT_GON = re.compile(
    r"\b(?:do|does|did|is|are|was|were|would|could|should|have|has|had) not\b|\bwill not\b|\bcannot\b|"
    r"\b(?:it|that|there|here|what|who|he|she) is (?!not\b)(?=\w)|\b(?:you|we|they) (?:are|will|have) (?=\w)|"
    r"\b(?:i am|let us)\b", re.I)
RE_GIONG_TAI_LIEU = re.compile(r"\b(?:tables?|pages?|sources?|rated|ratings?|the data|studies|study|percent|"
                               r"categor\w+|classif\w+|according to)\b", re.I)


def doc_so_giong(p: Path) -> list[tuple[str, re.Pattern, str]]:
    ra = []
    if not p.exists():
        return ra
    for d in p.read_text(encoding="utf-8").splitlines():
        if not d.strip() or d.startswith("#") or d.startswith("loai\t"):
            continue
        c = d.split("\t")
        if len(c) < 2:
            continue
        try:
            ra.append((c[0].strip(), re.compile(c[1], re.I), c[2].strip() if len(c) > 2 else ""))
        except re.error:
            continue
    return ra


def tts_cua(p: Path) -> str:
    s = p.read_text(encoding="utf-8", errors="replace")
    _, _, t = s.partition("## TTS SCRIPT")
    return re.sub(r"<#[\d.]+#>", " ", t)


def cham_e7(tts: str, script_path: Path | None = None, so_path: Path | None = None):
    """Trả (fails, warns, dòng log). Đo: từ sáo AI (0), chữ sách vở, dạng rút gọn, thành ngữ, dấu dân dã,
    giọng tài liệu, thành ngữ lặp qua 5 bài gần nhất."""
    so_path = so_path or Path(__file__).resolve().parent.parent / "references" / "giong-dan-da.tsv"
    so = doc_so_giong(so_path)
    fails, warns = [], []
    if not so:
        return fails, [f"E7 không thấy sổ {so_path}"], "[E7] bỏ qua (không có sổ)"
    n_tu = max(len(tts.split()), 1)
    cau = [c.strip() for c in re.split(r"(?<=[.!?])\s+", tts) if len(c.split()) >= 5]

    def cho(m):
        a, b = max(m.start() - 30, 0), min(m.end() + 30, len(tts))
        return " ".join(tts[a:b].split())

    cam = [(m, thay) for loai, rx, thay in so if loai == "cam" for m in rx.finditer(tts)]
    for m, thay in cam[:8]:
        fails.append(f"E7 từ sáo/khuôn AI '{m.group(0)}' → {thay or 'bỏ'} · «…{cho(m)}…»")
    sach = [(m, thay) for loai, rx, thay in so if loai == "sach" for m in rx.finditer(tts)]
    tran_sach = max(2, n_tu // E7_SACH_TREN)
    if sach:
        msg = "; ".join(f"'{m.group(0)}' → {thay}" for m, thay in sach[:10])
        (fails if len(sach) > tran_sach else warns).append(f"E7 chữ sách vở {len(sach)} chỗ (trần {tran_sach}): {msg}")
    krg = list(RE_KHONG_RUT_GON.finditer(tts))
    tran_krg = max(3, n_tu // E7_KHONG_RUT_GON_TREN)
    if krg:
        msg = "; ".join(f"«…{cho(m)}…»" for m in krg[:6])
        (warns if len(krg) > tran_krg else []).append(
            f"E7 nói không rút gọn {len(krg)} chỗ (trần {tran_krg}) — 'do not' → don't, 'it is' → it's, 'you will' → you'll: {msg}")
    rg = sum(1 for c in cau if RE_RUT_GON.search(c)) / max(len(cau), 1)
    if rg < E7_RUT_GON_FAIL:
        fails.append(f"E7 chỉ {rg:.0%} câu (≥ 5 từ) có dạng rút gọn — sàn {E7_RUT_GON_FAIL:.0%}, mục tiêu {E7_RUT_GON_MUC_TIEU:.0%}. "
                     "Nói như người thật: that's / here's / you'll / don't / it's")
    elif rg < E7_RUT_GON_MUC_TIEU:
        warns.append(f"E7 {rg:.0%} câu có dạng rút gọn (mục tiêu {E7_RUT_GON_MUC_TIEU:.0%})")
    tn = sorted({m.group(0).lower() for loai, rx, _ in so if loai == "thanh_ngu" for m in rx.finditer(tts)})
    dd = sorted({m.group(0).lower() for loai, rx, _ in so if loai == "dan_da" for m in rx.finditer(tts)})
    if len(tn) < E7_THANH_NGU_MUC_TIEU:
        (fails if len(tn) < E7_THANH_NGU_MIN else warns).append(
                     f"E7 thành ngữ / so sánh nhà nông {len(tn)} (sàn {E7_THANH_NGU_MIN}, mục tiêu {E7_THANH_NGU_MUC_TIEU}) {tn or ''} — "
                     "chọn trong references/giong-dan-da.tsv (thanh_ngu), dùng mới thì thêm 1 dòng vào sổ")
    if len(dd) < E7_DAN_DA_MIN:
        fails.append(f"E7 dấu dân dã {len(dd)} (cần ≥ {E7_DAN_DA_MIN}): folks / fair warning / nothing fancy / come spring…")
    tl = len(RE_GIONG_TAI_LIEU.findall(tts)) * 1000 / n_tu
    if tl > E7_GIONG_TAI_LIEU:
        (fails if tl > E7_GIONG_TAI_LIEU_FAIL else warns).append(f"E7 giọng tài liệu {tl:.1f}/1.000 từ (trần {E7_GIONG_TAI_LIEU}) — bớt 'tables / pages / sources / rated'; "
                     "nói như người kể lại: 'the extension folks have said this for years'")
    lap = []
    if script_path is not None and tn:
        khac = sorted((p for p in script_path.resolve().parent.parent.glob("*/script.md")
                       if p.resolve() != script_path.resolve()), key=lambda p: p.stat().st_mtime, reverse=True)[:5]
        rx_tn = [(rx, None) for loai, rx, _ in so if loai == "thanh_ngu"]
        for cum in tn:
            rx = next(r for r, _ in rx_tn if r.search(cum))
            n = sum(1 for p in khac if rx.search(tts_cua(p)))
            if n >= 2:
                lap.append(f"'{cum}' ({n}/5 bài)")
        if lap:
            warns.append("E7 thành ngữ lặp ở các bài gần đây (dễ thành khuôn): " + ", ".join(lap))
    log = (f"[E7] từ sáo AI {len(cam)} · chữ sách vở {len(sach)} · không rút gọn {len(krg)} · câu rút gọn {rg:.0%} · "
           f"thành ngữ {len(tn)} {tn} · dân dã {len(dd)} {dd} · giọng tài liệu {tl:.1f}/1.000 từ")
    return fails, warns, log


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--wpm", type=float, default=165.0)
    ap.add_argument("--hook", action="store_true", help="chấm riêng phần mở (bỏ ngân sách cả bài)")
    a = ap.parse_args()
    raw = Path(a.script).read_text(encoding="utf-8")
    head, _, tts = raw.partition("## TTS SCRIPT")
    if not tts:
        raise SystemExit("không thấy '## TTS SCRIPT'")
    tts = re.sub(r"<#[\d.]+#>", " ", tts)
    words = list(re.finditer(r"\S+", tts))
    wps = a.wpm / 60.0
    total_s = len(words) / wps

    def sec(ch):
        lo, hi = 0, len(words)
        while lo < hi:
            m = (lo + hi) // 2
            if words[m].start() < ch:
                lo = m + 1
            else:
                hi = m
        return lo / wps

    def mmss(s):
        return f"{int(s // 60)}:{int(s % 60):02d}"

    title = (re.search(r"^- \*\*Title:\*\*\s*(.+)$", head, re.M) or re.search(r"^#\s+(.+)$", head, re.M))
    title = title.group(1).strip() if title else ""
    keys = {}
    for k in ("ACTION_TIP", "PROMISE_OK", "CITE_ZONE", "RECAP_OK", "FIRST_STEP", "ENDING_FROM", "COMMENT_Q", "LOOP"):
        keys[k] = [m.strip() for m in re.findall(rf"^\s*[-*]?\s*\**{k}\**:\s*(.+)$", head, re.M)]
    fails, warns = [], []
    low = tts.lower()
    print(f"script: {a.script}\ntitle: {title}\nTTS ~{len(words)} từ ≈ {mmss(total_s)} @{a.wpm:.0f} wpm\n")

    # ---- L14 ----
    zones = []
    for z in keys["CITE_ZONE"]:
        if ".." in z:
            s1, s2 = [x.strip().lower() for x in z.split("..", 1)]
            i, j = low.find(s1), low.find(s2)
            if i >= 0 and j > i:
                zones.append((i, j + len(s2)))
            else:
                warns.append(f"L14 CITE_ZONE không khớp TTS: {z}")
    cites = [(m.start(), m.group(1).lower()) for m in SRC_RE.finditer(tts)]
    counted = [c for c in cites if not any(i <= c[0] <= j for i, j in zones)]
    budget = max(3, int(total_s // 90))
    per = {}
    for _, n in counted:
        per[n] = per.get(n, 0) + 1
    print(f"[L14] tên nguồn đọc bằng giọng: {len(cites)} (ngoài CITE_ZONE: {len(counted)}) · ngân sách {budget} (1/90s) · {per}")
    if len(counted) > budget:
        fails.append(f"L14 trích nguồn {len(counted)} > ngân sách {budget} — gộp thành 'the extension guides agree…', để nhãn nguồn hiện trên màn hình")
    dense = []
    for k in range(len(counted) - 2):
        if sec(counted[k + 2][0]) - sec(counted[k][0]) <= 30:
            dense.append(int(sec(counted[k][0])))
    if dense:
        msg = f"L14 >2 tên nguồn trong 30s tại: {', '.join(mmss(x) for x in sorted(set(dense))[:12])}"
        (fails if len(set(dense)) > 3 else warns).append(msg)

    # ---- L19 ---- (thêm 24/10/2026: cite chung chung "the guides say…" cũng là cite)
    gen_hits = [m for m in GENERIC_CITE_RE.finditer(tts) if not any(i <= m.start() <= j for i, j in zones)]
    gen_budget = max(3, len(words) // 300)
    over = [m for m in OVERCLAIM_RE.finditer(tts) if not any(i <= m.start() <= j for i, j in zones)]
    forms = {}
    for m in gen_hits:
        k = re.sub(r"\s+", " ", m.group(0).lower())
        forms[k] = forms.get(k, 0) + 1
    print(f"[L19] cite chung chung ngoài CITE_ZONE: {len(gen_hits)} · ngân sách {gen_budget} (1/300 từ) · cùng một khuôn lặp: "
          f"{ {k: v for k, v in forms.items() if v > 1} or 'không'}")
    if len(gen_hits) > gen_budget:
        fails.append(f"L19 {len(gen_hits)} câu cite chung chung > ngân sách {gen_budget} — nói thẳng dữ kiện ('Cut three to four inches.'), "
                     "để thẻ nguồn trên màn hình gánh uy tín; chỉ cite khi: số trung tâm lần đầu · nguồn bất đồng · YMYL · bác claim phổ biến")
    if over:
        fails.append("L19 tuyệt đối hoá nguồn (chỉ đọc vài trang): " + "; ".join(f"'{m.group(0)}' @{mmss(sec(m.start()))}" for m in over[:6]) +
                     " — bỏ 'every/all/are clear', hoặc viết 'the pages we read'")
    rep = [k for k, v in forms.items() if v > 1]
    if rep:
        warns.append("L19 lặp khuôn cite: " + "; ".join(f"'{k}' ×{forms[k]}" for k in rep))

    # ---- L15 ----
    hits = []
    for m in PREVIEW_RE.finditer(tts):
        s = sec(m.start())
        if 38 <= s <= 60:
            hits.append(f"'{m.group(0)[:40]}' @{s:.0f}s")
    win = [c for c in cites if 38 <= sec(c[0]) <= 60]
    if len(win) >= 3:
        hits.append(f"danh sách {len(win)} tên nguồn @{sec(win[0][0]):.0f}–{sec(win[-1][0]):.0f}s")
    print(f"[L15] giây 38–60: {hits or 'sạch'}")
    if hits:
        fails.append("L15 lộ trình/preview/danh sách nguồn rơi vào vùng chết 40–55s: " + "; ".join(hits) +
                     " — rút lộ trình còn 1 câu sau giây 60, danh sách nguồn chuyển xuống mô tả")

    # ---- L16 ----
    if not keys["ACTION_TIP"]:
        fails.append("L16 thiếu khai báo 'ACTION_TIP: <cụm nguyên văn>' trong header (mẹo miễn phí, làm ngay)")
        print("[L16] chưa khai báo ACTION_TIP")
    for tip in keys["ACTION_TIP"]:
        occ = [sec(m.start()) for m in re.finditer(re.escape(tip.lower()), low)]
        if not occ:
            fails.append(f"L16 ACTION_TIP không có trong TTS: '{tip}'")
            continue
        first, last = occ[0], occ[-1]
        late = last >= total_s * 0.85
        print(f"[L16] '{tip}': lần đầu {mmss(first)} · lần cuối {mmss(last)} · gọi lại ở 15% cuối: {'có' if late else 'không'}")
        if first > 180:
            fails.append(f"L16 mẹo hành động lần đầu ở {mmss(first)} > 3:00 — đưa lên đúng chỗ nó trả lời câu hỏi, cuối bài chỉ gọi lại")
        if not late or len(occ) < 2:
            warns.append("L16 mẹo hành động chưa được gọi lại ở phần kết (callback)")

    # ---- L17 ----
    ok = {re.split(r"\s+[—-]\s+", x)[0].strip().lower() for x in keys["PROMISE_OK"]}
    tl = title.lower()
    found = [w for w in PROMISE if re.search(r"\b" + re.escape(w) + r"\b", tl)]
    print(f"[L17] chữ hứa trên title: {found or 'không có'}")
    for w in found:
        if w in ok:
            print(f"      '{w}' đã có PROMISE_OK")
            continue
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", tts) if re.search(PROMISE[w], s, re.I)]
        if sents:
            ex = " | ".join(x[:90] for x in sents[:4])
            fails.append(f"L17 title hứa '{w}' nhưng script tự phủ định ({len(sents)} câu): {ex} — đổi chữ trên title "
                         f"hoặc ghi 'PROMISE_OK: {w} — <lý do>'")

    # ---- L18 ----  cụm "số (to số) đơn vị" đã nói trước đó, bị đọc lại dày trong một đoạn
    N = r"(?:\d+(?:\.\d+)?|(?:" + "|".join(NUMW) + r")(?:-(?:" + "|".join(NUMW[:9]) + r"))?)"
    PH = re.compile(rf"\b{N}(?:\s+(?:to|or)\s+{N})?\s+(?:days?|weeks?|hours?|inches|feet|degrees|months?|percent|foot-candles)\b", re.I)
    phr = [(m.start(), re.sub(r"\s+", " ", m.group(0).lower())) for m in PH.finditer(tts)]
    first = {}
    for pos, t in phr:
        first.setdefault(t, pos)
    starts = [w.start() for w in words]
    flagged, i, W = [], 0, 150
    while i < len(starts) - W:
        a0, a1 = starts[i], starts[i + W]
        rep = sorted({t for p, t in phr if a0 <= p < a1 and first[t] < a0 - 200})
        if len(rep) >= 4:
            flagged.append((sec(a0), rep))
            i += W
        else:
            i += 20
    print(f"[L18] đoạn đọc lại ≥4 cụm số đã nói (trong ~{W} từ): {[(mmss(s), len(r)) for s, r in flagged] or 'không'}")
    rz = []
    for z in keys["RECAP_OK"]:
        if ".." in z:
            s1, s2 = [x.strip().lower() for x in z.split("..", 1)]
            i1, j1 = low.find(s1), low.find(s2)
            if i1 >= 0 and j1 > i1:
                rz.append((sec(i1) - 30, sec(j1) + 5))
    for s, r in flagged:
        if any(x <= s <= y for x, y in rz):
            warns.append(f"L18 đọc lại {len(r)} cụm số quanh {mmss(s)} — đã khai RECAP_OK (kế hoạch áp dụng), chấp nhận")
            continue
        fails.append(f"L18 đọc lại {len(r)} cụm số đã nói quanh {mmss(s)} ({'; '.join(r[:5])}) — để thẻ bảng trên màn hình mang số, giọng chỉ nói quy luật")

    QUOTES = "\"'«»“”"
    # ---- L24 ---- (thêm 22/11/2026) bước làm đầu tiên / mục #1 <= giây 45
    def first_pos(phrase):
        i = low.find(phrase.lower().strip().strip(QUOTES))
        return None if i < 0 else sec(i)
    if not keys["FIRST_STEP"]:
        fails.append("L24 thiếu khai báo 'FIRST_STEP: <cụm nguyên văn>' trong header (bước làm đầu tiên / mục #1)")
        print("[L24] chưa khai báo FIRST_STEP")
    else:
        fs = keys["FIRST_STEP"][0]
        t = first_pos(fs)
        if t is None:
            fails.append(f"L24 FIRST_STEP không có trong TTS: '{fs}'")
        else:
            print(f"[L24] bước đầu '{fs[:50]}': {mmss(t)} (trần 0:45)")
            if t > 45:
                fails.append(f"L24 bước làm đầu tiên ở {mmss(t)} > 0:45 — đưa bước/mục #1 lên trước, lý thuyết nhúng vào bước")

    # ---- L23 ---- (thêm 22/11/2026) phần kết <= 20 s, không tóm tắt, không tả cảnh
    END_MAX = 20.0
    RECAP_RE = re.compile(r"\bso here's the plan\b|\bto recap\b|\b(?:quick|let's) recap\b|\bto sum (?:it )?up\b|\bin summary\b|"
                          r"\blet's review\b|\bone more time\b|\bso remember\b|\bhere's (?:the|a) (?:quick )?(?:summary|rundown)\b", re.I)
    SCENE_RE = re.compile(r"\bpicture (?:a|this|yourself|the)\b|\bimagine (?:a|this|yourself|walking|stepping)\b|\byou walk out\b", re.I)
    if not keys["ENDING_FROM"]:
        fails.append("L23 thiếu khai báo 'ENDING_FROM: <cụm nguyên văn mở phần kết>' trong header")
        print("[L23] chưa khai báo ENDING_FROM")
    else:
        ef = keys["ENDING_FROM"][0]
        i = low.rfind(ef.lower().strip().strip(QUOTES))
        if i < 0:
            fails.append(f"L23 ENDING_FROM không có trong TTS: '{ef}'")
        else:
            t = sec(i)
            dur = total_s - t
            print(f"[L23] phần kết từ {mmss(t)}: {dur:.0f}s (trần {END_MAX:.0f}s)")
            if dur > END_MAX:
                fails.append(f"L23 phần kết dài {dur:.0f}s > {END_MAX:.0f}s — giữ identity CTA + câu hỏi + mantra + Happy gardening")
    tail_i = int(len(tts) * 0.85)
    for rx, lab in ((RECAP_RE, "tóm tắt lại quy trình"), (SCENE_RE, "tả cảnh")):
        for m in rx.finditer(tts, tail_i):
            fails.append(f"L23 {lab} ở 15% cuối: '{m.group(0)}' @{mmss(sec(m.start()))} — bỏ; mẹo hành động gọi lại bằng 1 câu trước phần kết")

    # ---- L22 ---- (TEST 22/11/2026, chỉ cảnh báo) câu hỏi bình luận ở 2:30–4:00
    CQ_RE = re.compile(r"\b(?:tell me|let me know|drop|leave|share|write)\b[^.?!]{0,40}\bcomments?\b|\bin the comments\b", re.I)
    cq_hits = [sec(m.start()) for m in CQ_RE.finditer(tts)]
    if keys["COMMENT_Q"]:
        t = first_pos(keys["COMMENT_Q"][0])
        if t is not None:
            cq_hits.append(t)
        else:
            warns.append(f"L22 COMMENT_Q không có trong TTS: '{keys['COMMENT_Q'][0]}'")
    mid = [x for x in cq_hits if 150 <= x <= 240]
    print(f"[L22] câu hỏi bình luận: {[mmss(x) for x in sorted(set(cq_hits))] or 'không có'} · trong 2:30–4:00: {'có' if mid else 'không'}")
    if not mid:
        warns.append("L22 (TEST) chưa có câu hỏi bình luận về hoàn cảnh người xem ở 2:30–4:00 — khai COMMENT_Q, bình luận ghim hỏi lại đúng câu đó")

    # ---- L27 ---- (thêm 22/11/2026, user duyệt) khoảng cách loop: gieo → (trả một phần) → trả, mỗi khoảng <= 180 s
    LOOP_MAX = 180.0
    if not keys["LOOP"]:
        fails.append("L27 thiếu khai báo 'LOOP: <cụm gieo> .. <cụm trả>' trong header (mỗi loop 1 dòng)")
        print("[L27] chưa khai báo LOOP")
    for ln in keys["LOOP"]:
        moc = [x.strip().strip(QUOTES) for x in ln.split("..") if x.strip()]
        if len(moc) < 2:
            fails.append(f"L27 LOOP cần ≥ 2 mốc (gieo .. trả): '{ln}'")
            continue
        pos, start, bad = [], 0, False
        for m in moc:
            i = low.find(m.lower(), start)
            if i < 0:
                fails.append(f"L27 mốc loop không có trong TTS (hoặc sai thứ tự): '{m}'")
                bad = True
                break
            pos.append(sec(i))
            start = i + 1
        if bad:
            continue
        gaps = [pos[j + 1] - pos[j] for j in range(len(pos) - 1)]
        print(f"[L27] loop '{moc[0][:40]}': " + " → ".join(mmss(p) for p in pos) + f" · khoảng dài nhất {max(gaps):.0f}s (trần {LOOP_MAX:.0f}s)")
        if max(gaps) > LOOP_MAX:
            j = gaps.index(max(gaps))
            fails.append(f"L27 loop '{moc[0][:40]}' treo {max(gaps):.0f}s từ {mmss(pos[j])} tới {mmss(pos[j + 1])} > {LOOP_MAX:.0f}s — "
                         "trả lời sớm hơn, hoặc trả MỘT PHẦN ở giữa (không phải câu nhắc «nhớ đợi…») và khai mốc đó")

    # ---- ĐC ---- sổ cách nói đã chốt (thêm 08/11/2026): mỗi lần user sửa một cách nói → 1 dòng trong
    # references/cach-noi-da-chot.tsv. pham_vi: tts = chặn trong lời đọc · title = chặn trên title ·
    # ca-hai = chặn trên title, chỉ cảnh báo trong lời đọc.
    dc_path = Path(__file__).resolve().parent.parent / "references" / "cach-noi-da-chot.tsv"
    dc_hits = 0
    if dc_path.exists():
        rows = dc_path.read_text(encoding="utf-8").splitlines()[1:]
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", tts) if s.strip()]
        for row in rows:
            col = row.split("\t")
            if len(col) < 4 or not col[2].strip():
                continue
            ma, pv, rx, dung = col[0], col[1].strip(), col[2], col[3]
            try:
                cre = re.compile(rx, re.I)
            except re.error as e:
                warns.append(f"ĐC {ma} regex hỏng: {e}")
                continue
            if pv in ("title", "ca-hai") and title and cre.search(title):
                dc_hits += 1
                fails.append(f"ĐC {ma} title phạm '{cre.search(title).group(0)}' — {dung}")
            if pv in ("tts", "ca-hai"):
                bad = [s for s in sents if cre.search(s)]
                for s in bad[:4]:
                    dc_hits += 1
                    msg = f"ĐC {ma} '{cre.search(s).group(0)}' @{mmss(sec(low.find(s.lower()[:40])))}: {s[:90]} — {dung}"
                    (fails if pv == "tts" else warns).append(msg)
        print(f"[ĐC] sổ cách nói đã chốt: {len(rows)} dòng · chỗ phạm {dc_hits}")
    else:
        warns.append(f"ĐC không thấy {dc_path}")

    # ---- E7 ---- giọng dân dã (thêm 22/11/2026, user duyệt): sổ references/giong-dan-da.tsv
    e7_fail, e7_warn, e7_log = cham_e7(tts, Path(a.script))
    print(e7_log)
    fails += e7_fail
    warns += e7_warn

    if a.hook:
        # chấm riêng phần mở: bỏ các ngân sách tính cho cả bài (L16 callback · L22 · L23 · L27 · sàn thành ngữ E7)
        bo = ("L16 mẹo hành động chưa được gọi lại", "L22", "L23", "L27")
        warns = [w for w in warns if not w.startswith(bo)]
        warns += [f + " (ngân sách cả bài — tính ở script)" for f in fails if f.startswith("E7 thành ngữ")]
        fails = [f for f in fails if not f.startswith(bo) and not f.startswith("E7 thành ngữ")]
        print("[--hook] chấm riêng phần mở: bỏ L16 callback · L22 · L23 · L27 · sàn thành ngữ E7")

    print()
    for w in warns:
        print("🟡", w)
    for f in fails:
        print("🔴", f)
    print("\nKẾT QUẢ:", "FAIL" if fails else "PASS", f"({len(fails)} lỗi, {len(warns)} cảnh báo)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
