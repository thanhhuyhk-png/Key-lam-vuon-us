"""Bản đồ hình theo lời đọc (video-map.json) cho Garden US: kiểm trước khi tìm footage, xuất nhu cầu footage và prompt clip AI.

Usage:
    python tools/garden_map.py check   scripts/<video>/video-map.json
    python tools/garden_map.py queries scripts/<video>/video-map.json          -> footage/queries.txt (cho tools/footage_search.py)
    python tools/garden_map.py prompts scripts/<video>/video-map.json          -> ai-clip-prompts.md (cảnh loại V chưa có file)

video-map.json: {"video", "script", "wpm", "style", "negative", "scenes": [...]}
Mỗi scene:
  a     câu mở, nguyên văn trong ## TTS SCRIPT; cảnh kéo dài tới câu mở của cảnh sau
  sec   tên phần (HOOK, M1...)
  t     S = stock thật · G = đồ họa dựng bằng code · V = clip AI do user tự render
  show  hình bắt buộc thấy (đối chiếu khi chọn clip; không khớp thì không dùng)
  q     từ khóa tìm stock (t=S)
  alt   hình dự phòng khi không có clip đúng nghĩa (t=S, thường là một id V hoặc G)
  p     prompt tiếng Anh, chỉ tả cảnh (t=V)
  text  chữ trên màn hình; số phải có trong lời đọc, trừ khi "num_ok": true
Không network, không tốn credit.
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
WPM_DEFAULT = 165
WORDS = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven",
         "50": "fifty", "60": "sixty", "70": "seventy"}


def load(path):
    p = pathlib.Path(path)
    m = json.loads(p.read_text(encoding="utf-8"))
    tts = (p.parent / m.get("script", "script.md")).read_text(encoding="utf-8").split("## TTS SCRIPT", 1)[1]
    return p, m, tts.strip()


def mmss(s):
    return f"{int(s // 60)}:{int(s % 60):02d}"


def timed(m, tts):
    """Gắn vị trí và mốc ước tính; mốc thật lấy từ SRT sau khi có voice."""
    pos, bad = 0, []
    for s in m["scenes"]:
        i = tts.find(s["a"], pos)
        if i < 0:
            bad.append(s["a"])
            continue
        s["_i"] = i
        pos = i + len(s["a"])
    wpm = m.get("wpm", WPM_DEFAULT)
    ok = [s for s in m["scenes"] if "_i" in s]
    for k, s in enumerate(ok):
        end = ok[k + 1]["_i"] if k + 1 < len(ok) else len(tts)
        s["_w"] = len(tts[s["_i"]:end].split())
        s["_t"] = len(tts[:s["_i"]].split()) / wpm * 60
    return ok, bad


def cmd_check(path):
    p, m, tts = load(path)
    ok, bad = timed(m, tts)
    fails = [f"câu mở không khớp hoặc sai thứ tự: {a[:70]}" for a in bad]
    if ok and ok[0]["_i"] != 0:
        fails.append("cảnh đầu không bắt đầu từ câu đầu của lời đọc")
    low = tts.lower()
    for s in m["scenes"]:
        tag = s["a"][:40]
        if s.get("t") not in ("S", "G", "V"):
            fails.append(f"t không hợp lệ: {tag}")
        if not s.get("show"):
            fails.append(f"thiếu show: {tag}")
        if s.get("t") == "S" and not (s.get("q") and s.get("alt")):
            fails.append(f"cảnh S thiếu q hoặc alt: {tag}")
        if s.get("t") == "V" and not s.get("p"):
            fails.append(f"cảnh V thiếu p: {tag}")
        if s.get("text") and not s.get("num_ok"):
            for n in re.findall(r"\d+", s["text"]):
                if n not in tts and WORDS.get(n, "\0") not in low:
                    fails.append(f"số '{n}' trên hình không có trong lời đọc: {s['text']}")
    total = len(tts.split())
    mins = total / m.get("wpm", WPM_DEFAULT)
    n = {k: sum(1 for s in ok if s["t"] == k) for k in "SGV"}
    words = {k: sum(s["_w"] for s in ok if s["t"] == k) for k in "SGV"}
    print(f"{len(ok)} cảnh · {total} từ · ~{mins:.1f} phút @{m.get('wpm', WPM_DEFAULT)} wpm")
    for k, name in (("S", "stock"), ("G", "đồ họa"), ("V", "clip AI")):
        print(f"  {name}: {n[k]} cảnh · {words[k] / max(total, 1):.0%} thời lượng")
    gaps = sorted(ok, key=lambda s: -s["_w"])[:3]
    print("  cảnh dài nhất: " + " · ".join(f"{mmss(s['_t'])} {s['_w']} từ" for s in gaps) + " (mỗi cảnh sẽ chia nhiều shot ≤4 giây)")
    if fails:
        print("\nFAIL:")
        print("\n".join("  - " + f for f in fails))
        sys.exit(1)
    print("PASS")


def cmd_queries(path):
    p, m, tts = load(path)
    ok, _ = timed(m, tts)
    out = p.parent / "footage" / "queries.txt"
    out.parent.mkdir(exist_ok=True)
    lines = [f"{s['id']}|{q}" for s in ok if s["t"] == "S" for q in s["q"]]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(lines)} truy vấn -> {out}")


def cmd_prompts(path):
    p, m, tts = load(path)
    ok, _ = timed(m, tts)
    need = [s for s in ok if s["t"] == "V" and not s.get("file")]
    L = [f"# Prompt clip AI: {m['video']}", "",
         "Render 16:9, 1920×1080 nếu tool cho phép. Lưu vào một thư mục con trong `_LIBRARY/_inbox/" + m["video"].split("-")[2] + "/`, đúng tên file trong từng mục. Clip có bàn tay biến dạng, chữ hoặc logo thì bỏ.", "",
         "## Khối dán chung", "Thêm vào cuối mọi prompt:", "", "```text", m["style"], "```", "", "Negative prompt nếu tool hỗ trợ:", "", "```text", m["negative"], "```", ""]
    for s in need:
        L += [f"## {s['id']}.mp4 · khoảng {mmss(s['_t'])} · {s.get('dur', 6)} giây", f"Lời đọc: \"{s['a']}\"", "", "```text", s["p"], "```", ""]
    out = p.parent / "ai-clip-prompts.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"{len(need)} prompt -> {out}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("check", "queries", "prompts"):
        sys.exit(__doc__)
    {"check": cmd_check, "queries": cmd_queries, "prompts": cmd_prompts}[sys.argv[1]](sys.argv[2])
