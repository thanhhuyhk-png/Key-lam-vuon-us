"""Cổng máy gộp cho kịch bản Garden US (Bước 3 · 3R, thêm 2026-11-08).

Orchestrator TỰ chạy lệnh này sau MỖI lần script đổi (viết xong lô, Triple F, sửa theo phản biện, TTS clean) —
không tin báo cáo "đã PASS" của người viết.

Usage:
    python tools/gate.py scripts/big-idea-093-pepper-overwinter
    python tools/gate.py <folder> [--script script.md] [--wpm 165]
                         [--competitor <file|folder>]... [--no-competitor "<lý do>"]
                         [--allow "<cụm khoá>"]... [--no-seed "<lý do>"] [--no-claims "<lý do>"]
                         [--nhan "<nhãn ghi log, vd sau-phan-bien-v1>"] [--so-tu 1200-1500]

Chạy lần lượt (mỗi cổng in kết quả riêng, cuối cùng in bảng tổng):
  1. SỐ TỪ        phần TTS trong khoảng video_length.target_words_min..max của channel.config.json
  2. NEED DATA    không còn [NEED DATA] / [TODO] / [??] trong phần TTS
  3. LINT         tools/script_lint.py  (L14–L19 · L22–L27 · E7 + sổ cách nói đã chốt references/cach-noi-da-chot.tsv)
  4. TRÙNG        tools/originality_check.py  (5 script gần nhất · seed (lane B) · transcript đối thủ)
  5. SỐ LIỆU      tools/claim_check.py với allowed-numbers.json (BẮT BUỘC; thiếu file = FAIL trừ khi --no-claims)
  6. MÃ CLAIM     mọi thẻ [C01] trong script.draft-markers.md phải có trong Claim Ledger của research-brief.md
  7. COMPLIANCE   compliance_scan.py của skill youtube-garden-us (HARD-FAIL = FAIL · SOFT-FAIL = cảnh báo)
Ghi một dòng vào <folder>/gate-log.md mỗi lần chạy. Exit 1 nếu có cổng FAIL.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
COMPLIANCE = Path.home() / ".claude" / "skills" / "youtube-garden-us" / "scripts" / "compliance_scan.py"


def tts_part(text: str) -> str:
    _, sep, tts = text.partition("## TTS SCRIPT")
    return tts if sep else text


def run(name, cmd):
    print(f"\n{'=' * 70}\n▶ {name}: {' '.join(str(c) for c in cmd[1:])}\n{'=' * 70}")
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={**__import__('os').environ, "PYTHONIOENCODING": "utf-8"})
    out = (p.stdout or "") + (p.stderr or "")
    print(out.rstrip())
    return p.returncode, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--script", default="script.md")
    ap.add_argument("--wpm", default="165")
    ap.add_argument("--competitor", action="append", default=[])
    ap.add_argument("--no-competitor", default="")
    ap.add_argument("--allow", action="append", default=[])
    ap.add_argument("--no-seed", default="")
    ap.add_argument("--no-claims", default="")
    ap.add_argument("--nhan", default="")
    ap.add_argument("--so-tu", default="", help="khoảng số từ riêng, vd 1200-1500 (lane B theo archetype); mặc định lấy channel.config.json")
    a = ap.parse_args()

    folder = Path(a.folder).resolve()
    script = folder / a.script
    if not script.exists():
        raise SystemExit(f"không thấy {script}")
    raw = script.read_text(encoding="utf-8")
    tts = tts_part(raw)
    res = []  # (cổng, PASS/FAIL/CẢNH BÁO, ghi chú)

    # 1. SỐ TỪ
    body = "\n".join(ln for ln in tts.splitlines() if not ln.lstrip().startswith("#"))
    body = re.sub(r"\[(?:GFX|C\d+)[^\]]*\]|<#[\d.]+#>", " ", body)
    n = len(re.findall(r"[A-Za-z0-9'’-]+", body))
    lo = hi = None
    cfg = ROOT / "channel.config.json"
    if cfg.exists():
        vl = json.loads(cfg.read_text(encoding="utf-8")).get("video_length", {})
        lo, hi = vl.get("target_words_min"), vl.get("target_words_max")
        ps = folder / "pipeline-state.md"
        bh = vl.get("big_hit", {})
        if bh and ps.exists() and re.search(r"HẠNG:\s*\**\s*CÚ ĐÁNH LỚN", ps.read_text(encoding="utf-8"), re.I):
            lo, hi = bh.get("target_words_min", lo), bh.get("target_words_max", hi)
    if a.so_tu:
        lo, hi = (int(x) for x in a.so_tu.split("-"))
    mins = n / float(a.wpm)
    if lo and hi:
        st = "PASS" if lo <= n <= hi else "FAIL"
        res.append(("SỐ TỪ", st, f"{n} từ ≈ {mins:.1f}′ @{a.wpm} wpm · khoảng {lo}–{hi}"))
    else:
        res.append(("SỐ TỪ", "CẢNH BÁO", f"{n} từ ≈ {mins:.1f}′ · config không có target_words"))

    # 2. NEED DATA
    left = re.findall(r"\[(?:NEED DATA|TODO|\?\?)[^\]]*\]", tts, re.I)
    res.append(("NEED DATA", "FAIL" if left else "PASS", f"{len(left)} chỗ: {left[:3]}" if left else "sạch"))

    # 3. LINT
    rc, out = run("LINT", [sys.executable, "-X", "utf8", TOOLS / "script_lint.py", script, "--wpm", a.wpm])
    m = re.search(r"KẾT QUẢ:\s*(.+)", out)
    res.append(("LINT L14–L27 + E7 + ĐC", "PASS" if rc == 0 else "FAIL", m.group(1) if m else f"exit {rc}"))

    # 4. TRÙNG
    cmd = [sys.executable, "-X", "utf8", TOOLS / "originality_check.py", script]
    for c in a.competitor:
        cmd += ["--competitor", c]
    for x in a.allow:
        cmd += ["--allow", x]
    if a.no_competitor:
        cmd += ["--no-competitor", a.no_competitor]
    if a.no_seed:
        cmd += ["--no-seed", a.no_seed]
    rc, out = run("TRÙNG", cmd)
    comp = re.search(r"vs \d+ competitor transcript\(s\): (.+)", out)
    note = comp.group(1) if comp else ("chưa có transcript đối thủ" if "chưa có transcript đối thủ" in out else "")
    worst = re.search(r"Max identical sentences vs any recent script: (\d+)", out)
    note = f"kênh mình max {worst.group(1) if worst else '?'} câu · đối thủ: {note or 'bỏ qua'}"
    st = "FAIL" if rc else ("CẢNH BÁO" if "chưa có transcript đối thủ" in out else "PASS")
    res.append(("TRÙNG (kênh · seed · đối thủ)", st, note))

    # 5. SỐ LIỆU
    allow = folder / "allowed-numbers.json"
    if allow.exists():
        rc, out = run("SỐ LIỆU", [sys.executable, "-X", "utf8", TOOLS / "claim_check.py", script, allow])
        bad = len(re.findall(r"^NOT ALLOWED", out, re.M))
        res.append(("SỐ LIỆU allowed-numbers", "PASS" if rc == 0 else "FAIL", f"{bad} số ngoài danh sách"))
    elif a.no_claims:
        res.append(("SỐ LIỆU allowed-numbers", "CẢNH BÁO", f"bỏ qua: {a.no_claims}"))
    else:
        res.append(("SỐ LIỆU allowed-numbers", "FAIL",
                    "thiếu allowed-numbers.json — lập từ Claim Ledger (mỗi số kèm mã C..), hoặc --no-claims \"<lý do>\""))

    # 6. MÃ CLAIM
    draft = folder / "script.draft-markers.md"
    brief = folder / "research-brief.md"
    if draft.exists() and brief.exists():
        ledger = set(re.findall(r"^\|\s*(C\d+)\s*\|", brief.read_text(encoding="utf-8"), re.M))
        tags = re.findall(r"\[(C\d+(?:\s*[,·/]\s*C\d+)*)\]", tts_part(draft.read_text(encoding="utf-8")))
        ids = {x for t in tags for x in re.findall(r"C\d+", t)}
        missing = sorted(ids - ledger)
        if not ids:
            res.append(("MÃ CLAIM", "CẢNH BÁO", f"draft-markers chưa gắn thẻ [C..] (ledger có {len(ledger)} dòng) — "
                                                 "người phản biện phải tự dò câu ↔ claim"))
        else:
            res.append(("MÃ CLAIM", "FAIL" if missing else "PASS",
                        f"{len(tags)} thẻ, {len(ids)} mã · không có trong ledger: {missing}" if missing
                        else f"{len(tags)} thẻ, {len(ids)}/{len(ledger)} mã ledger được dùng"))
    else:
        res.append(("MÃ CLAIM", "CẢNH BÁO", "thiếu script.draft-markers.md hoặc research-brief.md"))

    # 7. COMPLIANCE
    if COMPLIANCE.exists():
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
            f.write(tts)
        rc, out = run("COMPLIANCE", [sys.executable, "-X", "utf8", COMPLIANCE, f.name])
        Path(f.name).unlink(missing_ok=True)
        v = re.search(r"VERDICT:\s*(\S+)", out)
        v = v.group(1) if v else f"exit {rc}"
        st = "FAIL" if (rc or v == "HARD-FAIL") else ("CẢNH BÁO" if v == "SOFT-FAIL" else "PASS")
        res.append(("COMPLIANCE regex", st, v + " — điểm 0–10 chính thức do người phản biện chấm"))
    else:
        res.append(("COMPLIANCE regex", "CẢNH BÁO", f"không thấy {COMPLIANCE}"))

    # Tổng
    icon = {"PASS": "✅", "FAIL": "🔴", "CẢNH BÁO": "🟡"}
    print(f"\n{'=' * 70}\nCỔNG MÁY — {folder.name} / {script.name}\n{'=' * 70}")
    for name, st, note in res:
        print(f"{icon[st]} {name:<30} {st:<9} {note}")
    fails = [r for r in res if r[1] == "FAIL"]
    verdict = "FAIL" if fails else "PASS"
    print(f"\nKẾT QUẢ: {verdict} ({len(fails)} cổng FAIL, {sum(r[1] == 'CẢNH BÁO' for r in res)} cảnh báo)")

    log = folder / "gate-log.md"
    if not log.exists():
        log.write_text("# Gate log\n\n| Lúc | Nhãn | Tệp | Kết quả | Cổng FAIL |\n|---|---|---|---|---|\n", encoding="utf-8")
    with log.open("a", encoding="utf-8") as f:
        f.write(f"| {dt.datetime.now():%Y-%m-%d %H:%M} | {a.nhan or '-'} | {script.name} | {verdict} | "
                f"{', '.join(r[0] for r in fails) or '-'} |\n")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
