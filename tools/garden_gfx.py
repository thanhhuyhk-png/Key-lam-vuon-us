"""Garden US graphic cards (1920x1080 PNG) for big-idea-062. Every number/claim on a card comes from the verified claims in research-brief.md.

Usage: python tools/garden_gfx.py OUTDIR
Cards: ROADMAP, FOOTCANDLE, DARKBREAK, TABLE-1/2/3, DIS-HOURS, DIS-DIST, DIS-WASH, DISTANCE, 3CARDS, CALENDAR, plus 7 counters COUNT-1..7.
Style: dark green background, cream text, yellow for the key number, large type for readers aged 60-80.
"""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
BG = (18, 55, 42)
PANEL = (28, 78, 60)
CREAM = (245, 238, 220)
YEL = (255, 214, 10)
RED = (232, 84, 70)
GREEN = (120, 220, 140)
GREY = (170, 190, 180)
F = "C:/Windows/Fonts/"


def font(name, size):
    return ImageFont.truetype(F + name, size)


BOLD = lambda s: font("arialbd.ttf", s)
REG = lambda s: font("arial.ttf", s)
IMP = lambda s: font("impact.ttf", s)


def canvas():
    im = Image.new("RGB", (W, H), BG)
    return im, ImageDraw.Draw(im)


def center(d, text, y, f, fill=CREAM, x=W // 2):
    w = d.textlength(text, font=f)
    d.text((x - w / 2, y), text, font=f, fill=fill)


def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def para(d, text, x, y, f, fill, maxw, gap=8):
    for ln in wrap(d, text, f, maxw):
        d.text((x, y), ln, font=f, fill=fill)
        y += f.size + gap
    return y


def footer(d, text):
    d.text((60, H - 48), text, font=REG(28), fill=GREY)


def roadmap(out):
    im, d = canvas()
    center(d, "WHAT'S IN THIS VIDEO", 90, IMP(80), YEL)
    items = [("1", "The light: what a winter window gives you"), ("2", "Seven vegetables: 5 easy, 2 need a light"),
             ("3", "One table, and 3 places the sources disagree"), ("4", "Lamps, 3 common problems, a 4-week plan")]
    y = 250
    for n, t in items:
        d.rounded_rectangle([160, y, W - 160, y + 150], 24, fill=PANEL)
        d.text((210, y + 8), n, font=IMP(120), fill=YEL)
        d.text((340, y + 40), t, font=BOLD(54), fill=CREAM)
        y += 175
    im.save(out / "GFX-ROADMAP.png")


def footcandle(out):
    im, d = canvas()
    center(d, "SOUTH-FACING WINDOW", 150, IMP(90), CREAM)
    center(d, "about 300 foot-candles", 290, IMP(150), YEL)
    center(d, "the best window option in the guide", 480, BOLD(54), CREAM)
    d.rounded_rectangle([260, 620, W - 260, 820], 24, fill=PANEL)
    center(d, "Winter hours per day?", 650, BOLD(60), CREAM)
    center(d, "Not in the sources I found.", 740, BOLD(60), RED)
    footer(d, "Source: Illinois Extension, Make Sure Houseplants Get Enough Light in Winter (2021)")
    im.save(out / "GFX-FOOTCANDLE.png")


def darkbreak(out):
    im, d = canvas()
    center(d, "TOMATO vs PEPPER: THE DARK BREAK", 80, IMP(80), YEL)
    x0, x1 = 160, W - 160
    for i, (label, dark, note, col) in enumerate([("TOMATO", True, "needs about 6 hours of dark to fruit", RED), ("PEPPER", False, "does not need a dark break", GREEN)]):
        y = 260 + i * 330
        d.text((x0, y), label, font=IMP(80), fill=CREAM)
        bar_y = y + 110
        d.rounded_rectangle([x0, bar_y, x1, bar_y + 90], 18, fill=PANEL)
        if dark:
            seg = int((x1 - x0) * 0.25)
            d.rounded_rectangle([x1 - seg, bar_y, x1, bar_y + 90], 18, fill=(20, 24, 70))
            d.text((x1 - seg + 25, bar_y + 18), "6 h DARK", font=BOLD(50), fill=CREAM)
            d.text((x0 + 30, bar_y + 18), "lamp on", font=BOLD(50), fill=YEL)
        d.text((x0, bar_y + 110), note, font=BOLD(54), fill=col)
    footer(d, "Source: University of New Hampshire Extension, Optimizing Plant Growth with Indoor Lighting Q&A (2021)")
    im.save(out / "GFX-DARKBREAK.png")


ROWS = [
    ("Microgreens", "window may suffice in some cases; lamp is better", "7-21 days", "Maryland"),
    ("Baby greens", "tolerate less-than-ideal light", "21-40 days", "Maryland"),
    ("Leaf lettuce", "very sunny spot; 6-8 h bright light", "about 4 weeks", "Illinois, New Hampshire"),
    ("Chives, parsley", "6-8 h bright light", "10-12 weeks", "Illinois, New Hampshire"),
    ("Radish", "the sources don't say", "-", "New Hampshire"),
    ("Tomatoes (small)", "extra light in winter; 6 h dark", "about 10 weeks", "New Hampshire, Utah State"),
    ("Peppers (small)", "extra light in winter; no dark break", "about 10 weeks", "New Hampshire"),
]


def table(out, n, rows_shown, title):
    im, d = canvas()
    center(d, title, 24, IMP(70), YEL)
    cols = [60, 430, 1180, 1500]
    heads = ["CROP", "LIGHT (per the sources)", "TIME", "WHO SAYS"]
    y = 118
    for x, h in zip(cols, heads):
        d.text((x, y), h, font=BOLD(32), fill=GREY)
    y += 44
    for i, r in enumerate(ROWS[:rows_shown]):
        hot = i >= 5
        d.rounded_rectangle([40, y, W - 40, y + 106], 16, fill=(60, 40, 30) if hot else PANEL)
        d.text((cols[0], y + 28), r[0], font=BOLD(42), fill=YEL if hot else CREAM)
        para(d, r[1], cols[1], y + 12, BOLD(34), CREAM, 720, 2)
        d.text((cols[2], y + 28), r[2], font=BOLD(38), fill=CREAM)
        para(d, r[3], cols[3], y + 12, REG(32), GREY, 380, 2)
        y += 116
    footer(d, "Table assembled by this channel from the extension guides listed in the description")
    im.save(out / f"GFX-TABLE-{n}.png")


def disagree(out, key, title, left, right):
    im, d = canvas()
    center(d, title, 80, IMP(80), YEL)
    for i, (head, txt, src) in enumerate([left, right]):
        x = 100 + i * 880
        d.rounded_rectangle([x, 240, x + 840, 840], 28, fill=PANEL)
        d.text((x + 40, 270), head, font=IMP(70), fill=CREAM)
        para(d, txt, x + 40, 400, BOLD(52), CREAM, 760, 10)
        d.text((x + 40, 760), src, font=REG(34), fill=GREY)
    center(d, "vs", 470, IMP(90), RED)
    im.save(out / f"GFX-{key}.png")


def distance(out):
    im, d = canvas()
    center(d, "HOW FAR BELOW THE LAMP?", 50, IMP(80), YEL)
    # left: lamp above a tray with a gap arrow
    d.rounded_rectangle([140, 250, 880, 290], 14, fill=CREAM)
    d.rectangle([220, 290, 800, 326], fill=(60, 60, 60))
    d.rounded_rectangle([140, 820, 880, 900], 12, fill=(120, 80, 50))
    for i in range(8):
        x = 190 + i * 90
        d.line([x, 820, x, 760 - (i % 3) * 14], fill=GREEN, width=14)
    d.line([510, 330, 510, 740], fill=YEL, width=8)
    d.polygon([(510, 330), (490, 370), (530, 370)], fill=YEL)
    d.polygon([(510, 740), (490, 700), (530, 700)], fill=YEL)
    d.text((540, 500), "the gap", font=BOLD(54), fill=YEL)
    # right: three source cards
    cards = [("6-12 in", "Illinois Extension (2017)", RED), ("4-6 in", "New Hampshire Extension (2021)", YEL), ("3-6 in", "Utah State Extension (tomatoes)", GREEN)]
    y = 230
    for big, src, col in cards:
        d.rounded_rectangle([980, y, 1820, y + 200], 26, fill=PANEL)
        d.text((1020, y + 20), big, font=IMP(110), fill=col)
        d.text((1020, y + 140), src, font=BOLD(36), fill=CREAM)
        y += 230
    footer(d, "If seedlings stretch: lower the lamp or run it longer. If they burn: raise it. (New Hampshire)")
    im.save(out / "GFX-DISTANCE.png")


def three_cards(out):
    im, d = canvas()
    center(d, "3 COMMON PROBLEMS", 60, IMP(84), YEL)
    cards = [("1", "STRETCHING", "Lower the lamp, run it longer, or both", "New Hampshire"),
             ("2", "MOLD", "Good air circulation; a gentle fan; wash trays before reuse", "Maryland"),
             ("3", "TINY PESTS", "Yellow sticky traps; read the label and follow it", "New Hampshire")]
    for i, (n, t, txt, src) in enumerate(cards):
        x = 70 + i * 610
        d.rounded_rectangle([x, 220, x + 570, 900], 28, fill=PANEL)
        d.text((x + 40, 240), n, font=IMP(130), fill=YEL)
        d.text((x + 40, 400), t, font=IMP(64), fill=CREAM)
        para(d, txt, x + 40, 500, BOLD(44), CREAM, 490, 8)
        d.text((x + 40, 820), src, font=REG(34), fill=GREY)
    im.save(out / "GFX-3CARDS.png")


def calendar(out):
    im, d = canvas()
    center(d, "YOUR 4-WEEK PLAN", 50, IMP(84), YEL)
    weeks = [("WEEK 1", "Sow microgreens and a tray of leaf lettuce. Start tomatoes or peppers now if you want them (about 10 weeks)."),
             ("WEEKS 2-3", "Microgreens: 7-21 days after sowing. Cut with clean scissors."),
             ("WEEK 4", "Loose-leaf lettuce: about 4 weeks. Chives and parsley keep growing (10-12 weeks).")]
    y = 200
    for h, t in weeks:
        d.rounded_rectangle([80, y, W - 80, y + 230], 26, fill=PANEL)
        d.text((130, y + 30), h, font=IMP(80), fill=YEL)
        para(d, t, 560, y + 38, BOLD(46), CREAM, 1240, 8)
        y += 260
    footer(d, "Timelines from Maryland, Illinois and New Hampshire Extension guides")
    im.save(out / "GFX-CALENDAR.png")


def counters(out):
    for n in range(1, 8):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([W - 380, 40, W - 40, 190], 26, fill=(18, 55, 42, 235))
        d.text((W - 340, 50), f"{n}/7", font=IMP(110), fill=YEL)
        im.save(out / f"COUNT-{n}.png")


def main():
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    roadmap(out)
    footcandle(out)
    darkbreak(out)
    table(out, 1, 3, "WINDOW or LAMP? THE TABLE (1/3)")
    table(out, 2, 5, "WINDOW or LAMP? THE TABLE (2/3)")
    table(out, 3, 7, "WINDOW or LAMP? THE TABLE (3/3)")
    disagree(out, "DIS-HOURS", "DISAGREEMENT 1: HOW MANY HOURS?", ("ILLINOIS", "6-8 hours of bright light (lettuce, herbs)", "UIUC Extension, 2017"),
             ("MARYLAND", "about 16 hours total, from all sources (microgreens)", "UMD Extension"))
    disagree(out, "DIS-DIST", "DISAGREEMENT 2: HOW FAR IS THE LAMP?", ("ILLINOIS / NEW HAMPSHIRE", "6-12 inches / 4-6 inches", "UIUC 2017 / UNH 2021"),
             ("UTAH STATE", "3-6 inches (tomatoes)", "USU Extension"))
    disagree(out, "DIS-WASH", "DISAGREEMENT 3: WASH MICROGREENS?", ("MARYLAND", "rinse, pat dry, use now or fridge up to 10 days", "UMD Extension"),
             ("PENN STATE", "washing not recommended unless absolutely necessary (guide framed for commercial producers)", "Penn State Extension"))
    distance(out)
    three_cards(out)
    calendar(out)
    counters(out)
    print("cards", len(list(out.glob("*.png"))), "->", out)


if __name__ == "__main__":
    main()
