"""Thumbnail Garden US từ ẢNH THẬT trong _LIBRARY (Pexels, giấy phép tự do) + chữ 2 tầng (vàng/trắng, viền đen dày).

Usage: python -X utf8 -I tools/garden_thumb_real.py <outdir>
Tạo 1280x720: A = Before->After (LEGGY? / 6-8 HOURS) · B = NO FRUIT? / 6 HOURS DARK. Chữ hook không trùng chữ title (complementarity).
Ảnh nguồn tra theo tên gốc Pexels trong catalog (đổi SRC_* nếu muốn ảnh khác).
"""
import glob
import pathlib
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

LIB = r"D:\0002-Team A Nam\_LIBRARY"
W, H = 1280, 720
YEL, WHITE, RED, GREEN = (255, 214, 10), (255, 255, 255), (232, 60, 52), (70, 200, 90)
IMP = lambda s: ImageFont.truetype("C:/Windows/Fonts/impact.ttf", s)
BOLD = lambda s: ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", s)


def lib(name):
    g = glob.glob(LIB + "/**/*__" + name, recursive=True)
    if not g:
        raise SystemExit("không thấy trong thư viện: " + name)
    return Image.open(g[0]).convert("RGB")


def cover(im, w, h, fx=0.5, fy=0.5):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    x = int((im.width - w) * fx)
    y = int((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))


def punch(im, sat=1.25, con=1.12):
    return ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(sat)).enhance(con)


def outlined(d, xy, s, font, fill, stroke=9):
    d.text(xy, s, font=font, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0))


def badge(d, cx, cy, ok):
    d.ellipse([cx - 44, cy - 44, cx + 44, cy + 44], fill=GREEN if ok else RED, outline=(255, 255, 255), width=6)
    if ok:
        d.line([cx - 22, cy + 2, cx - 6, cy + 20, cx + 24, cy - 18], fill=(255, 255, 255), width=12, joint="curve")
    else:
        d.line([cx - 20, cy - 20, cx + 20, cy + 20], fill=(255, 255, 255), width=12)
        d.line([cx - 20, cy + 20, cx + 20, cy - 20], fill=(255, 255, 255), width=12)


def pill(d, x, y, s):
    f = BOLD(26)
    w = d.textlength(s, font=f)
    d.rounded_rectangle([x, y, x + w + 36, y + 46], 12, fill=(0, 0, 0, 200))
    d.text((x + 18, y + 7), s, font=f, fill=(255, 255, 255))


def thumb_a(out):
    left = punch(cover(lib(SRC_A_LEFT), 520, H, 0.5, 0.45), 1.0, 1.25)
    left = ImageEnhance.Brightness(left).enhance(0.8)
    right = punch(cover(lib(SRC_A_RIGHT), W - 520, H, 0.5, 0.5), 1.3, 1.1)
    im = Image.new("RGB", (W, H))
    im.paste(left, (0, 0))
    im.paste(right, (520, 0))
    # darken top band for text legibility
    band = Image.new("RGB", (W, 330), (0, 0, 0)).convert("RGBA")
    mask = Image.linear_gradient("L").resize((W, 330)).rotate(180).point(lambda v: int(v * 0.75))
    im.paste(band.convert("RGB"), (0, 0), mask)
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle([514, 0, 526, H], fill=(255, 255, 255))
    outlined(d, (36, 30), "LEGGY?", IMP(158), YEL, 9)
    outlined(d, (40, 205), "6-8 HOURS", IMP(96), WHITE, 8)
    badge(d, 450, 640, False)
    badge(d, 1210, 640, True)
    pill(d, 40, 640, "ILLINOIS EXTENSION")
    im.save(out / "thumbnail-real-a.jpg", quality=92)


def thumb_b(out):
    im = punch(cover(lib(SRC_B), W, H, 0.5, 0.4), 1.25, 1.12)
    dark = Image.new("RGB", (W, H), (0, 0, 0))
    mask = Image.linear_gradient("L").resize((H, W)).rotate(90, expand=True).resize((W, H)).point(lambda v: int(v * 0.85))
    im = Image.composite(dark, im, mask.transpose(Image.FLIP_LEFT_RIGHT))
    d = ImageDraw.Draw(im, "RGBA")
    outlined(d, (40, 70), "NO FRUIT?", IMP(190), YEL, 10)
    outlined(d, (44, 270), "6 HOURS DARK", IMP(110), WHITE, 8)
    pill(d, 40, 640, "NEW HAMPSHIRE EXTENSION")
    im.save(out / "thumbnail-real-b.jpg", quality=92)


# ảnh nguồn (tên gốc Pexels, tra trong thư viện)
SRC_A_LEFT = "pexels-photo-985626.jpg"
SRC_A_RIGHT = "pexels-photo-38094546.jpg"
SRC_B = "pexels-photo-35775444.jpg"

if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    thumb_a(out)
    thumb_b(out)
    print("OK ->", out)
