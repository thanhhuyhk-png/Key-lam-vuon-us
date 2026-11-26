"""Garden US chalkboard graphic cards (1920x1080 PNG), matching the user's hand-made reference cards (18/10/2026).

Usage: python tools/garden_gfx_chalk.py OUTDIR [--user-dir DIR_WITH_REFERENCE_IMAGES]
Cards (CHALK-*): DARKBREAK, DIS-DIST, DIS-WASH, DISTANCE, 3CARDS, CALENDAR, COUNT-1..7 (transparent badge).
The user's four reference cards (ROADMAP, FOOTCANDLE, DIS-HOURS, TABLE-3) are NOT redrawn: pass --user-dir to convert them to CHALK-*.png at 1920x1080
(expects 3.webp=DIS-HOURS, 4.webp=TABLE-3, 5.webp=ROADMAP, 6.webp=FOOTCANDLE).
Every number/claim comes from the verified claims in research-brief.md (CL-xxx). Style: chalk handwriting (Ink Free), grain, white outlines, yellow titles.
"""
import pathlib
import random
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
BOARD = (27, 66, 52)
WHITE = (242, 240, 230)
YEL = (255, 208, 64)
RED = (242, 104, 104)
GREEN = (140, 220, 150)
GREY = (170, 186, 176)
F = "C:/Windows/Fonts/"
rnd = random.Random(7)


def ink(size):
    return ImageFont.truetype(F + "Inkfree.ttf", size)


def board():
    base = Image.new("RGB", (W, H), (0, 0, 0))
    inner = Image.new("RGB", (W - 80, H - 80), BOARD)
    noise = Image.effect_noise((W - 80, H - 80), 28).convert("L")
    inner = ImageChops.add(inner, Image.merge("RGB", [noise.point(lambda v: max(0, v - 118) // 2)] * 3))
    # soft vignette
    vg = Image.new("L", inner.size, 0)
    ImageDraw.Draw(vg).ellipse([-300, -250, inner.width + 300, inner.height + 250], fill=255)
    vg = vg.filter(ImageFilter.GaussianBlur(160))
    dark = Image.new("RGB", inner.size, (10, 30, 22))
    inner = Image.composite(inner, dark, vg)
    base.paste(inner, (40, 40))
    return base


def chalk(im):
    """Roughen the chalk layer: multiply alpha-like by grain so strokes look dusty."""
    return im


class Card:
    def __init__(self):
        self.bg = board()
        self.layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.layer)

    def _fit(self, s, size, maxw):
        while size > 24 and self.d.textlength(s, font=ink(size)) > maxw:
            size -= 2
        return size

    def text(self, xy, s, size, fill=WHITE, anchor="la", maxw=None):
        if maxw:
            size = self._fit(s, size, maxw)
        self.d.text(xy, s, font=ink(size), fill=fill, anchor=anchor, stroke_width=1, stroke_fill=fill)

    def center(self, y, s, size, fill=WHITE, maxw=1560):
        size = self._fit(s, size, maxw)
        self.d.text((W // 2, y), s, font=ink(size), fill=fill, anchor="ma", stroke_width=1, stroke_fill=fill)

    def wrap(self, x, y, s, size, fill, maxw, gap=8):
        f = ink(size)
        cur = ""
        for w_ in s.split():
            t = (cur + " " + w_).strip()
            if self.d.textlength(t, font=f) <= maxw:
                cur = t
            else:
                self.d.text((x, y), cur, font=f, fill=fill, stroke_width=1, stroke_fill=fill)
                y += size + gap
                cur = w_
        self.d.text((x, y), cur, font=f, fill=fill, stroke_width=1, stroke_fill=fill)
        return y + size + gap

    def box(self, xy, r=36, width=5, outline=WHITE, fill=None):
        self.d.rounded_rectangle(xy, r, outline=outline, width=width, fill=fill)

    def decorations(self):
        d = self.d
        for (cx, cy, sx) in ((70, 70, 1), (W - 70, H - 70, -1)):
            for k in range(3):
                x = cx + sx * (30 + k * 38)
                y = cy + sx * (18 + (k % 2) * 30)
                d.ellipse([x - 20, y - 14, x + 20, y + 14], fill=(200, 205, 195, 150))
            d.line([cx, cy + sx * 70, cx + sx * 150, cy + sx * 60], fill=WHITE, width=3)
        for _ in range(4):
            x, y = rnd.randint(200, W - 200), rnd.randint(70, 140)
            d.line([x - 12, y, x + 12, y], fill=(240, 240, 230, 200), width=3)
            d.line([x, y - 12, x, y + 12], fill=(240, 240, 230, 200), width=3)

    def save(self, path, grain=True):
        lay = self.layer
        if grain:
            g = Image.effect_noise((W, H), 60).convert("L").point(lambda v: 238 + (v - 128) // 6 if v > 70 else 200)
            a = ImageChops.multiply(lay.getchannel("A"), g)
            lay.putalpha(a)
        out = self.bg.convert("RGBA")
        out.alpha_composite(lay)
        out.convert("RGB").save(path)


def darkbreak(out):
    c = Card()
    c.decorations()
    c.center(80, "TOMATO vs PEPPER: THE DARK BREAK", 96, YEL)
    x0, x1 = 170, W - 170
    for i, (label, dark, note, col) in enumerate([("TOMATO", True, "needs about 6 hours of dark to fruit", RED),
                                                  ("PEPPER", False, "does not need a dark break", GREEN)]):
        y = 250 + i * 330
        c.text((x0, y), label, 90, WHITE)
        by = y + 120
        c.box([x0, by, x1, by + 100], 22, 5)
        if dark:
            seg = int((x1 - x0) * 0.25)
            c.d.rounded_rectangle([x1 - seg, by, x1, by + 100], 22, fill=(36, 44, 110, 230), outline=WHITE, width=5)
            c.text((x1 - seg + 30, by + 14), "6 h DARK", 64, WHITE)
            c.text((x0 + 36, by + 14), "lamp on", 64, YEL)
        c.text((x0, by + 120), note, 66, col, maxw=1500)
    c.text((90, H - 100), "Source: University of New Hampshire Extension, Indoor Lighting Q&A (2021)", 34, GREY)
    c.save(out / "CHALK-DARKBREAK.png")


def disagree(out, key, title, left, right):
    c = Card()
    c.decorations()
    c.center(70, title, 100, YEL)
    for i, (head, txt, src) in enumerate([left, right]):
        x = 90 + i * 930
        c.box([x, 220, x + 780, 860], 44, 5)
        c.text((x + 50, 250), head, 88, WHITE, maxw=680)
        c.wrap(x + 50, 380, txt, 58, WHITE, 680, 10)
        c.text((x + 50, 780), src, 40, GREY, maxw=680)
    c.d.ellipse([890, 400, 1030, 540], outline=RED, width=6)
    c.text((960, 470), "VS", 80, RED, anchor="mm")
    c.save(out / f"CHALK-{key}.png")


def distance(out):
    c = Card()
    c.decorations()
    c.center(70, "HOW FAR BELOW THE LAMP?", 100, YEL)
    c.d.rounded_rectangle([140, 270, 880, 312], 14, outline=WHITE, width=5)
    c.d.rectangle([230, 312, 790, 346], outline=WHITE, width=4)
    c.d.rounded_rectangle([140, 820, 880, 900], 14, outline=WHITE, width=5)
    for i in range(8):
        x = 190 + i * 90
        c.d.line([x, 820, x, 760 - (i % 3) * 14], fill=GREEN, width=10)
    c.d.line([510, 360, 510, 735], fill=YEL, width=6)
    c.d.polygon([(510, 360), (490, 400), (530, 400)], fill=YEL)
    c.d.polygon([(510, 735), (490, 695), (530, 695)], fill=YEL)
    c.text((545, 520), "the gap", 66, YEL)
    cards = [("6-12 in", "Illinois Extension (2017)", RED), ("4-6 in", "New Hampshire Extension (2021)", YEL),
             ("3-6 in", "Utah State Extension (tomatoes)", GREEN)]
    y = 220
    for big, src, col in cards:
        c.box([980, y, 1840, y + 210], 36, 5)
        c.text((1020, y + 8), big, 110, col)
        c.text((1020, y + 138), src, 44, WHITE)
        y += 240
    c.text((90, H - 100), "If seedlings stretch: lower the lamp or run it longer. If they burn: raise it.", 38, GREY)
    c.save(out / "CHALK-DISTANCE.png")


def three_cards(out):
    c = Card()
    c.decorations()
    c.center(70, "3 COMMON PROBLEMS", 104, YEL)
    cards = [("1", "STRETCHING", "Lower the lamp, run it longer, or both", "New Hampshire"),
             ("2", "MOLD", "Good air circulation; a gentle fan; wash trays before reuse", "Maryland"),
             ("3", "TINY PESTS", "Yellow sticky traps; read the label and follow it", "New Hampshire")]
    for i, (n, t, txt, src) in enumerate(cards):
        x = 80 + i * 600
        c.box([x, 220, x + 560, 900], 40, 5)
        c.d.ellipse([x + 36, 244, x + 146, 354], outline=YEL, width=5)
        c.text((x + 91, 299), n, 80, YEL, anchor="mm")
        c.text((x + 40, 390), t, 84, WHITE, maxw=480)
        c.wrap(x + 40, 510, txt, 52, WHITE, 480, 8)
        c.text((x + 40, 810), src, 40, GREY)
    c.save(out / "CHALK-3CARDS.png")


def calendar(out):
    c = Card()
    c.decorations()
    c.center(70, "YOUR 4-WEEK PLAN", 104, YEL)
    weeks = [("WEEK 1", "Sow microgreens and a tray of leaf lettuce. Start tomatoes or peppers now if you want them (about 10 weeks)."),
             ("WEEKS 2-3", "Microgreens: 7-21 days after sowing. Cut with clean scissors."),
             ("WEEK 4", "Loose-leaf lettuce: about 4 weeks. Chives and parsley keep growing (10-12 weeks).")]
    y = 210
    for h, t in weeks:
        c.box([90, y, W - 90, y + 220], 40, 5)
        c.text((140, y + 60), h, 80, YEL)
        c.wrap(620, y + 30, t, 52, WHITE, 1180, 6)
        y += 250
    c.text((90, H - 100), "Timelines from Maryland, Illinois and New Hampshire Extension guides", 34, GREY)
    c.save(out / "CHALK-CALENDAR.png")


def counters(out):
    for n in range(1, 8):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([W - 380, 70, W - 80, 220], 36, fill=(27, 66, 52, 235), outline=WHITE, width=5)
        d.text((W - 230, 145), f"{n}/7", font=ink(110), fill=YEL, anchor="mm")
        im.save(out / f"CHALK-COUNT-{n}.png")


def convert_user(out, ud):
    ud = pathlib.Path(ud)
    for src, key in (("3.webp", "DIS-HOURS"), ("4.webp", "TABLE-3"), ("6.webp", "FOOTCANDLE")):
        p = ud / src
        if p.exists():
            Image.open(p).convert("RGB").resize((W, H), Image.LANCZOS).save(out / f"CHALK-{key}.png")
            print("user card ->", f"CHALK-{key}.png")


def roadmap(out):
    """Chalk version of the user's roadmap card, with wording matched to the v3 title (no 'easy' - lesson L17)."""
    c = Card()
    c.decorations()
    c.center(70, "WHAT'S IN THIS VIDEO", 104, YEL)
    items = ["The light: what a winter window gives you", "Seven vegetables: 5 can use a window, 2 need a lamp",
             "One table, and 3 places the sources disagree", "Lamps, 3 common problems, a 4-week plan"]
    y = 230
    for i, t in enumerate(items):
        c.box([140, y, W - 140, y + 170], 44, 5)
        c.d.ellipse([190, y + 30, 300, y + 140], outline=YEL, width=5)
        c.text((245, y + 85), str(i + 1), 84, YEL, anchor="mm")
        c.text((350, y + 38), t, 66, WHITE, maxw=1180)
        ix, iy = W - 270, y + 85
        if i == 0:
            c.d.ellipse([ix - 28, iy - 28, ix + 28, iy + 28], outline=YEL, width=5)
            for a in range(8):
                import math
                dx, dy = math.cos(a * math.pi / 4), math.sin(a * math.pi / 4)
                c.d.line([ix + dx * 40, iy + dy * 40, ix + dx * 56, iy + dy * 56], fill=YEL, width=4)
        elif i == 1:
            c.d.ellipse([ix - 40, iy - 30, ix, iy + 6], outline=WHITE, width=4)
            c.d.ellipse([ix, iy - 30, ix + 40, iy + 6], outline=WHITE, width=4)
            c.d.line([ix, iy + 6, ix, iy + 40], fill=WHITE, width=4)
        elif i == 2:
            c.d.rectangle([ix - 36, iy - 36, ix + 36, iy + 36], outline=WHITE, width=4)
            c.d.line([ix, iy - 36, ix, iy + 36], fill=WHITE, width=4)
            c.d.line([ix - 36, iy, ix + 36, iy], fill=WHITE, width=4)
        else:
            c.d.polygon([(ix - 30, iy - 10), (ix + 30, iy - 10), (ix + 16, iy - 40), (ix - 16, iy - 40)], outline=WHITE, width=4)
            c.d.line([ix, iy - 10, ix, iy + 34], fill=WHITE, width=4)
            for dx in (-24, 0, 24):
                c.d.line([ix + dx, iy + 44, ix + dx, iy + 58], fill=YEL, width=4)
        y += 200
    c.save(out / "CHALK-ROADMAP.png")


def main():
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    if "--user-dir" in sys.argv:
        convert_user(out, sys.argv[sys.argv.index("--user-dir") + 1])
    roadmap(out)
    darkbreak(out)
    disagree(out, "DIS-DIST", "DISAGREEMENT 2: HOW FAR IS THE LAMP?",
             ("ILLINOIS / NEW HAMPSHIRE", "6-12 inches / 4-6 inches", "UIUC 2017 / UNH 2021"), ("UTAH STATE", "3-6 inches (tomatoes)", "USU Extension"))
    disagree(out, "DIS-WASH", "DISAGREEMENT 3: WASH MICROGREENS?",
             ("MARYLAND", "rinse, pat dry, use now or fridge up to 10 days", "UMD Extension"),
             ("PENN STATE", "washing not recommended unless absolutely necessary (guide framed for commercial producers)", "Penn State Extension"))
    distance(out)
    three_cards(out)
    calendar(out)
    counters(out)
    print("cards", len(list(out.glob("CHALK-*.png"))), "->", out)


if __name__ == "__main__":
    main()
