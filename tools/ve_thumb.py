"""Vẽ thumbnail bằng GPT Image qua shopaikey — Garden US (thêm 2026-11-08).

⚠️ BẠN TỰ CHẠY lệnh này trong terminal của mình. Claude không chạy chế độ vẽ, vì luật dự án cấm Claude đọc
tệp có chữ "key" trong tên. Tool tự đọc key, KHÔNG in key ra màn hình, không ghi key vào đâu.

Nguồn key (theo thứ tự): biến môi trường SHOPAIKEY_KEY → tệp ~/.shopaikey_key.
Prompt: mọi khối ``` nằm ngay sau dòng **Prompt <tên>:** trong file gói (mặc định
research/goi-moi-pineapple-lemon-2026-11-08.md).

Lệnh:
    python -X utf8 tools/ve_thumb.py xem                    # liệt kê prompt sẽ vẽ — KHÔNG đọc key, KHÔNG tốn tiền
    python -X utf8 tools/ve_thumb.py ve [--chi "A,Lemon A"] [--model gpt-image-2.5-flare-1k] [--goi <file.md>]
        Mỗi prompt = 1 lần gọi /v1/images/generations (1536×1024, n=1) — TỐN TIỀN, xem giá trên shopaikey trước.
        Lưu: research/thumb-moi/<tên>-goc.png (1536×1024) và <tên>.png (cắt giữa 16:9, 1280×720).
        Ảnh đã có thì bỏ qua (thêm --ve-lai để vẽ lại).
Sau khi vẽ: soi chữ trên ảnh bằng mắt (AI hay viết sai chữ) trước khi đưa vào Test & Compare.
"""
import base64
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
GOI = ROOT / "research" / "goi-moi-pineapple-lemon-2026-11-08.md"
OUT = ROOT / "research" / "thumb-moi"
BASE = "https://api.shopaikey.com/v1"


def prompts(path):
    txt = path.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"\*\*Prompt ([^:*]+?):?\*\*[^\n]*\n```[a-z]*\n(.*?)\n```", txt, re.S):
        name = m.group(1).strip()
        if not name.lower().startswith(("lemon", "pineapple")):
            name = "Pineapple " + name  # "Prompt A" trong mục 060
        out[name] = m.group(2).strip()
    return out


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def key():
    k = os.environ.get("SHOPAIKEY_KEY", "").strip()
    if not k:
        p = Path.home() / ".shopaikey_key"
        if p.exists():
            k = p.read_text(encoding="utf-8").strip()
    if not k:
        raise SystemExit("Không thấy key: đặt biến SHOPAIKEY_KEY hoặc tệp ~/.shopaikey_key")
    return k


def call(prompt, model, k):
    body = json.dumps({"model": model, "prompt": prompt, "size": "1536x1024", "n": 1}).encode()
    req = urllib.request.Request(BASE + "/images/generations", data=body, method="POST", headers={
        "Authorization": "Bearer " + k, "Content-Type": "application/json",
        "User-Agent": "curl/8.5.0"})  # thiếu User-Agent này Cloudflare trả 403
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            j = json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"API lỗi {e.code}: {e.read().decode(errors='replace')[:300]}")
    d = j["data"][0]
    if d.get("b64_json"):
        return base64.b64decode(d["b64_json"])
    with urllib.request.urlopen(urllib.request.Request(d["url"], headers={"User-Agent": "curl/8.5.0"}), timeout=120) as r:
        return r.read()


def crop(src, dst):
    from PIL import Image
    im = Image.open(src)
    w, h = im.size
    nh = round(w * 9 / 16)
    top = max(0, (h - nh) // 2)
    im.crop((0, top, w, top + nh)).resize((1280, 720), Image.LANCZOS).save(dst)


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("xem", "ve"):
        raise SystemExit(__doc__)
    opt = lambda k, d="": a[a.index(k) + 1] if k in a else d
    goi = Path(opt("--goi", str(GOI)))
    ps = prompts(goi)
    chi = [x.strip().lower() for x in opt("--chi").split(",") if x.strip()]
    if chi:
        ps = {n: p for n, p in ps.items() if n.lower() in chi or n.lower().replace("pineapple ", "") in chi}
    if not ps:
        raise SystemExit(f"Không thấy prompt nào trong {goi.name}")
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"{len(ps)} prompt từ {goi.name}:")
    for n, p in ps.items():
        f = OUT / f"{slug(n)}.png"
        txt = re.findall(r'"([^"]+)" in (?:bright )?(YELLOW|WHITE)', p)
        print(f"  · {n:<12} chữ: {' / '.join(t for t, _ in txt)}  → {f.relative_to(ROOT)}{'  (đã có)' if f.exists() else ''}")
    if a[0] == "xem":
        print("\nChế độ xem: không đọc key, không gọi API. Vẽ thật: thêm lệnh `ve` (tốn tiền).")
        return
    model = opt("--model", "gpt-image-2.5-flare-1k")
    k = key()
    for n, p in ps.items():
        goc, f = OUT / f"{slug(n)}-goc.png", OUT / f"{slug(n)}.png"
        if f.exists() and "--ve-lai" not in a:
            continue
        print(f"… vẽ {n} ({model})", flush=True)
        goc.write_bytes(call(p, model, k))
        crop(goc, f)
        print(f"  ✓ {f.relative_to(ROOT)}")
    print("\nSoi chữ trên từng ảnh bằng mắt trước khi tải lên Studio.")


if __name__ == "__main__":
    main()
