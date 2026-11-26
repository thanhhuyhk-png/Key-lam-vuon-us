"""Thẻ đồ họa bảng phấn cho garden_cut.py, vẽ từ trường "card" trong video-map.json. Mỗi thẻ ra một hoặc nhiều PNG (hiện dần theo lời đọc).

Usage (xem thử):
    python tools/garden_cards.py scripts/<video>/video-map.json <thư mục ra>

Kiểu thẻ (card.kind):
  thermo   lo, hi, big                      nhiệt kế tô dải, không ghi số ngoài dải
  zones    hi[], title, sub                 dải zone 3–11, tô các zone trong hi (không vẽ bản đồ giả)
  vs       left, right, mid                 hai ô so sánh
  table    title, rows[[nhãn, nội dung]]    hiện dần từng dòng
  y        title, sub                       sơ đồ cây chữ Y
  two      items[[nhãn, giá trị]]           hai ô số
  notice   title, big, small                thẻ số điện thoại, cảnh báo
  timeline items[]                          dòng thời gian, hiện dần từng mốc
  pages    pages[[ảnh, nguồn]]              ảnh chụp trang nguồn thật, mỗi trang một PNG
Số trên thẻ phải có trong lời đọc (garden_map.py check kiểm trường text).
"""
import json
import math
import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import garden_gfx_chalk as chalk
from garden_gfx_chalk import Card, GREEN, GREY, RED, W, H, WHITE, YEL, ink

ZONE_DIM = (70, 104, 90)


def thermo(c, a):
    c.center(90, a["big"], 190, YEL)
    x0, x1, y = 300, W - 300, 640
    c.box([x0, y - 44, x1, y + 44], r=44, width=6)
    c.d.ellipse([x0 - 92, y - 92, x0 + 92, y + 92], outline=WHITE, width=6, fill=(70, 150, 200))
    span = x1 - x0
    lo, hi = x0 + span * 0.4, x0 + span * 0.6
    c.d.rounded_rectangle([x0 + 8, y - 34, hi, y + 34], 30, fill=(70, 150, 200))
    c.d.rectangle([lo, y - 60, hi, y + 60], outline=YEL, width=8)
    for k in range(11):
        x = x0 + span * k / 10
        c.d.line([x, y + 58, x, y + 88], fill=GREY, width=4)
    c.text((lo, y + 110), a["lo"], 84, YEL, anchor="ma")
    c.text((hi, y + 110), a["hi"], 84, YEL, anchor="ma")


def zones(c, a):
    c.center(110, a["title"], 170, YEL)
    n = list(range(3, 12))
    x0, gap = 170, 14
    bw = (W - 2 * x0 - gap * (len(n) - 1)) / len(n)
    for i, z in enumerate(n):
        x = x0 + i * (bw + gap)
        on = not a.get("hi") or z in a["hi"]
        c.d.rounded_rectangle([x, 450, x + bw, 760], 20, fill=YEL if on else ZONE_DIM)
        c.text((x + bw / 2, 605), str(z), 120, (24, 50, 40) if on else GREY, anchor="mm")
    c.center(830, a["sub"], 70, WHITE)


def pot(c, cx, base, col):
    c.d.polygon([(cx - 90, base - 130), (cx + 90, base - 130), (cx + 62, base), (cx - 62, base)], outline=col, width=6)
    c.d.line([cx, base - 130, cx, base - 300], fill=col, width=7)
    c.d.line([cx, base - 220, cx - 70, base - 300], fill=col, width=6)
    c.d.line([cx, base - 240, cx + 70, base - 310], fill=col, width=6)


def vs(c, a):
    for i, (x, label, col) in enumerate(((150, a["left"], GREY), (1070, a["right"], YEL))):
        c.box([x, 130, x + 700, 950], outline=col, width=7)
        pot(c, x + 350, 740, col)
        if i:
            cx, cy = x + 540, 270
            c.d.ellipse([cx - 62, cy - 62, cx + 62, cy + 62], outline=YEL, width=7)
            for k in range(8):
                t = k * math.pi / 4
                c.d.line([cx + 82 * math.cos(t), cy + 82 * math.sin(t), cx + 116 * math.cos(t), cy + 116 * math.sin(t)], fill=YEL, width=6)
        c.text((x + 350, 840), label, 84, col, anchor="mm", maxw=640)
    c.text((W / 2, H / 2), a["mid"], 220, RED, anchor="mm")


def table(c, a, upto):
    c.center(90, a["title"], 110, YEL)
    rows = a["rows"]
    gap = (900 - 260) / len(rows)
    for i, (k, v) in enumerate(rows):
        y = 260 + i * gap
        c.box([140, y, W - 140, y + gap - 30], outline=WHITE, width=5)
        c.text((190, y + (gap - 30) / 2), k, 76, YEL, anchor="lm", maxw=470)
        if i < upto:
            c.text((680, y + (gap - 30) / 2), v, 66, WHITE, anchor="lm", maxw=W - 880)


def y_plant(c, a):
    c.center(70, a["title"], 180, YEL)
    cx, base = W // 2, 960
    c.d.polygon([(cx - 170, base - 190), (cx + 170, base - 190), (cx + 120, base), (cx - 120, base)], outline=WHITE, width=7)
    fork = base - 390
    c.d.line([cx, base - 190, cx, fork], fill=GREEN, width=20)
    for dx, dy in ((-230, -240), (230, -240), (24, -300)):
        c.d.line([cx, fork, cx + dx, fork + dy], fill=GREEN, width=16)
        c.d.line([cx + dx - 34, fork + dy - 8, cx + dx + 34, fork + dy + 8], fill=RED, width=7)
    c.text((cx + 330, fork + 40), a["sub"], 66, WHITE, anchor="lm", maxw=480)


def two(c, a):
    for i, (k, v) in enumerate(a["items"]):
        x = 150 + i * 860
        c.box([x, 220, x + 760, 860], outline=YEL if i else GREY, width=7)
        c.text((x + 380, 370), k, 96, WHITE, anchor="mm", maxw=660)
        c.text((x + 380, 610), v, 170, YEL, anchor="mm", maxw=680)


def notice(c, a):
    c.center(190, a["title"], 84, WHITE)
    c.center(420, a["big"], 190, YEL)
    c.center(760, a["small"], 66, GREY)


def timeline(c, a, upto):
    its = a["items"]
    x0, x1, y = 300, W - 300, 470
    c.center(110, a["title"], 110, YEL)
    c.d.line([x0, y, x1, y], fill=GREY, width=6)
    step = (x1 - x0) / (len(its) - 1)
    for i, t in enumerate(its):
        x = x0 + i * step
        on = i < upto
        c.d.ellipse([x - 34, y - 34, x + 34, y + 34], fill=YEL if on else None, outline=YEL if on else GREY, width=6)
        if on:
            lines = t.split("|")
            for k, l in enumerate(lines):
                c.text((x, y + 110 + k * 92), l, 66, WHITE, anchor="ma", maxw=step - 30)


def page_png(path, source, out):
    bg = chalk.board().convert("RGB")
    im = Image.open(path).convert("RGB")
    bw, bh = 1640, 860
    im = im.resize((bw, int(im.height * bw / im.width))).crop((0, 0, bw, bh))
    x, y = (W - bw) // 2, 70
    bg.paste(im, (x, y))
    d = ImageDraw.Draw(bg)
    d.rectangle([x, y, x + bw, y + bh], outline=(242, 240, 230), width=5)
    d.text((W // 2, y + bh + 72), source, font=ink(66), fill=YEL, anchor="mm", stroke_width=1, stroke_fill=YEL)
    bg.save(out)


def render(a, prefix):
    """Trả danh sách PNG; thẻ hiện dần có nhiều PNG, trường "at" của card là tỉ lệ thời lượng lúc mỗi PNG xuất hiện."""
    k = a["kind"]
    if k == "pages":
        out = []
        for i, (path, source) in enumerate(a["pages"]):
            f = f"{prefix}_{i}.png"
            page_png(path, source, f)
            out.append(f)
        return out
    steps = range(0, len(a.get("rows") or a.get("items") or []) + 1) if k in ("table", "timeline") else [None]
    out = []
    for i, n in enumerate(steps):
        c = Card()
        if k == "table":
            table(c, a, n)
        elif k == "timeline":
            timeline(c, a, n)
        else:
            {"thermo": thermo, "zones": zones, "vs": vs, "y": y_plant, "two": two, "notice": notice}[k](c, a)
        f = f"{prefix}_{i}.png"
        c.save(f)
        out.append(f)
    return out


if __name__ == "__main__":
    m = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    d = pathlib.Path(sys.argv[2])
    d.mkdir(parents=True, exist_ok=True)
    for s in m["scenes"]:
        if s.get("card"):
            print(s["id"], render(s["card"], str(d / s["id"])))
