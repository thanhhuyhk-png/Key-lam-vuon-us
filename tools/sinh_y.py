"""Sinh ý CÚ ĐÁNH LỚN — Garden US (thêm 2026-11-08).

Công thức rút từ hit của chính kênh (research/chan-doan-kenh-2026-11-08.md):
    [thứ ai cũng có / đang vứt đi] × [đảo niềm tin] × [phần thưởng lớn: free / never buy] × [phạm vi rộng, nhiều món]
Mỗi "hạt ý" là 1 dòng trong references/dna-but.tsv (thêm/sửa tay; cột ghi_chu = điều phải có nguồn).
Mỗi hạt được ráp vào 4 khung tiêu đề của chính các hit kênh, rồi:
  1. qua máy kiểm trùng tools/kiem_de_tai.py (CHẶN → loại, CẢNH BÁO → trừ điểm),
  2. chấm ĐIỂM ƯU TIÊN = tổng ln(hệ số) các đặc điểm có trong tiêu đề, theo references/dna-kenh.json
     (trung bình hệ số cửa sổ gần và giai đoạn tham chiếu), + thưởng nếu có hit cùng chủ thể, + thưởng mùa,
  3. ghi research/sinh-y-<năm>-W<tuần>.md — 1 hạt lấy tiêu đề nháp điểm cao nhất.
Điểm ưu tiên KHÔNG phải P(thắng): chỉ để chọn 2–3 ý đưa vào PHỄU GỘP (bậc 1 Topic Gate trở đi).
Tiêu đề ở đây là NHÁP để kiểm định — tiêu đề thật làm ở [1] outline (Title Engine, L9, KEYWORD-FIRST).

Lệnh:
    python -X utf8 tools/sinh_y.py [--top 10] [--mua winter]
"""
import csv
import datetime as dt
import json
import math
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from dna_kenh import FEATURES, has  # noqa: E402
import kiem_de_tai as kdt  # noqa: E402

SEEDS = ROOT / "references" / "dna-but.tsv"
DNA = ROOT / "references" / "dna-kenh.json"

# Khung tiêu đề của chính các hit kênh. can_duyet = khung đang vướng luật kênh, chờ user quyết (bước 4 đề xuất 08/11).
TEMPLATES = [
    ("GIA_TRI", "These {n} {vat} Could Be the Most Valuable Plants in Your Yard",
     ("n", "vat"), "937K · These 6 Weeds…", ""),
    ("STOP_INSTEAD", "Stop {cu} — {dao} Instead ({thuong})",
     ("cu", "dao", "thuong"), "182K · Stop Rooting Cuttings in Water!",
     "L20: vế sau phải là thứ được thêm, có nguồn A/B, chứng minh ≤ 20 s; tối đa 1 video/4"),
    ("NEVER_BUY", "Never Buy {mua_buy} Again — {dao}",
     ("mua_buy", "dao"), "28K/12K · Never Buy Potting Soil / Ginger Again", ""),
    ("JUST", "{n} {vat} That {dao} (No {pain}, No Cost)",
     ("n", "vat", "dao", "pain"), "985K/16K · 7 Plants … in JUST Water (No Soil…)", ""),
    ("VUT_DI", "You're Throwing Away {thuong}: {dao}",
     ("thuong", "dao"), "DNA thứ đang vứt đi (×2,1 tham chiếu)", ""),
]
SEASON_NOW = {11: "fall", 12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
              6: "summer", 7: "summer", 8: "summer", 9: "fall", 10: "fall"}
SEASON_NEXT = {"fall": "winter", "winter": "spring", "spring": "summer", "summer": "fall"}


def lifts():
    if not DNA.exists():
        raise SystemExit("chưa có references/dna-kenh.json — chạy `python -X utf8 tools/dna_kenh.py do`")
    d = json.loads(DNA.read_text(encoding="utf-8"))["dac_diem"]
    out = {}
    for f, x in d.items():
        vals = [v for v in (x["he_so_gan"], x["he_so_tham_chieu"]) if v]
        out[f] = sum(math.log(v) for v in vals) / len(vals) if vals else 0.0
    return out


PRONOUN = re.compile(r"\b(them|it|this)\b", re.I)
L20_SO = re.compile(r"\b(toxic|poison\w*|kill\w*|dying|die|dies|dead|warning|don'?t)\b", re.I)  # = DC009 cach-noi-da-chot.tsv


def build(seed, tpl):
    """Ráp 1 tiêu đề nháp; bỏ khi ráp ra câu sai (đại từ treo, lặp chữ)."""
    k, pat, need, _, _ = tpl
    if any(not seed.get(x) for x in need):
        return None
    dao, thuong = seed["dao"], seed["thuong"]
    if k == "STOP_INSTEAD":
        if re.search(r"\binstead\b", dao, re.I):
            pat = "Stop {cu} — {dao}"
        if thuong.lower() in dao.lower():
            pat = pat.replace(" ({thuong})", "")
    elif PRONOUN.search(dao):
        return None  # "Never Buy X Again — Compost Them First": đại từ không có chỗ dựa ngoài khung STOP
    if k == "VUT_DI" and thuong.lower() in dao.lower():
        return None
    t = pat.format(**seed)
    return t if len(t) <= 80 else None


def main():
    a = sys.argv[1:]
    top = int(a[a.index("--top") + 1]) if "--top" in a else 10
    mua = a[a.index("--mua") + 1] if "--mua" in a else SEASON_NOW[dt.date.today().month]
    L = lifts()
    seeds = list(csv.DictReader(SEEDS.open(encoding="utf-8"), delimiter="\t"))
    res = []
    for s in seeds:
        best = None
        cands = [(tpl, build(s, tpl)) for tpl in TEMPLATES]
        for t in (s.get("nhap_tay") or "").split("||"):  # tiêu đề nháp viết tay trong dna-but.tsv
            if t.strip():
                k = "STOP_INSTEAD" if t.strip().lower().startswith(("stop", "don't")) else "TAY"
                warn = TEMPLATES[1][4] if k == "STOP_INSTEAD" else ""
                cands.append((("TAY", "", (), "viết tay", warn), t.strip()))
        for tpl, t in cands:
            if not t or L20_SO.search(t):  # L20 ②: đảo niềm tin không đi kèm chữ sợ / "Don't"
                continue
            g = kdt.danh_gia(t, f"{s['cu']} {s['dao']}", s["vat"].lower().replace(" ", ","))
            feats = [f for f in FEATURES if has(f, t)]
            score = sum(L.get(f, 0) for f in feats)
            hit = g["hit"][0][0] if g["hit"] else 0
            if hit:
                score += min(1.0, math.log10(hit / 1000) / 3)  # 1K→0 · 10K→0,33 · 1 Tr→1
            if s["mua"] in (mua, SEASON_NEXT[mua]):
                score += 0.15
            if g["verdict"] == "CẢNH BÁO":
                score -= 0.3
            if len(t) > 70:
                score -= 0.2  # tiêu đề dài bị cắt trên điện thoại
            row = {"seed": s, "tpl": tpl, "title": t, "g": g, "feats": feats, "score": round(score, 2), "hit": hit}
            if g["verdict"] == "CHẶN":
                row["score"] = None
            if best is None or (row["score"] or -9) > (best["score"] or -9):
                best = row
        if best:
            res.append(best)
    ok = sorted([r for r in res if r["score"] is not None], key=lambda r: -r["score"])
    bad = [r for r in res if r["score"] is None]
    y, w, _ = dt.date.today().isocalendar()
    out = ROOT / "research" / f"sinh-y-{y}-W{w:02d}.md"
    Lm = [f"# Sinh ý cú đánh lớn — {dt.date.today()} (mùa đang nhắm: {mua} → {SEASON_NEXT[mua]})", "",
          "Máy ghi: `python -X utf8 tools/sinh_y.py`. Điểm ưu tiên = tổng ln(hệ số DNA kênh) + thưởng hit cùng chủ thể + "
          "thưởng mùa − trừ CẢNH BÁO. **Không phải P(thắng).** Chọn 2–3 ý → PHỄU GỘP bậc 1 (`references/topic-gate-en.md`).", "",
          "| # | Điểm | Tiêu đề nháp (ký tự) | Khung (hit gốc) | Kiểm trùng | Hit cùng chủ thể | Đặc điểm DNA | Phải có nguồn |",
          "|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(ok[:top], 1):
        k, _, _, ref, warn = r["tpl"]
        Lm.append(f"| {i} | {r['score']} | {r['title']} ({len(r['title'])}) | {k}{' ⚠️' if warn else ''} ({ref}) | "
                  f"{r['g']['verdict']} | {f'{r['hit']:,}' if r['hit'] else '—'} | {', '.join(r['feats'])} | {r['seed']['ghi_chu']} |")
    if any(r["tpl"][4] for r in ok[:top]):
        Lm += ["", "⚠️ = khung đảo niềm tin — " + TEMPLATES[1][4] + "."]
    if bad:
        Lm += ["", "## Bị CHẶN (mọi khung)", ""]
        for r in bad:
            Lm.append(f"- {r['seed']['ma']} {r['seed']['vat']}: {r['g']['chan'][0][1] if r['g']['chan'] else ''}")
    Lm += ["", "## Chi tiết kiểm trùng (ý trong bảng)", ""]
    for i, r in enumerate(ok[:top], 1):
        notes = [t for _, t in r["g"]["canh"][:3]] + [f"lời đọc {f}: {n} lần" for n, f in r["g"]["sau"][:2]]
        Lm.append(f"{i}. **{r['title']}** — " + ("; ".join(notes) if notes else "sạch"))
    out.write_text("\n".join(Lm) + "\n", encoding="utf-8")
    print("\n".join(Lm[:top + 7]))
    print(f"\n✓ {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
