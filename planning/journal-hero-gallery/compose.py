#!/usr/bin/env python3
"""
Composite the Journal / blog hero crops into one labelled gallery image,
oldest to newest, so the evolution reads left to right and top to bottom.

Usage:
    python3 planning/journal-hero-gallery/compose.py
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CROPS = os.path.join(HERE, "crops")

BG = (28, 25, 22)
CARD = (255, 255, 255)
TEXT = (255, 255, 255)
MUTED = (168, 160, 150)
ACCENT = (232, 196, 184)

PANEL_W = 760          # rendered width of each hero card in the composite
GUTTER = 34
MARGIN = 44
CAP_H = 86             # caption block above each card
TITLE_H = 132

FONT_DIR = "/System/Library/Fonts/Supplemental"


def font(name, size):
    for candidate in (os.path.join(FONT_DIR, name),
                      "/System/Library/Fonts/Helvetica.ttc"):
        if os.path.exists(candidate):
            try:
                return ImageFont.truetype(candidate, size)
            except Exception:
                pass
    return ImageFont.load_default()


F_TITLE = font("Arial Bold.ttf", 34)
F_SUB = font("Arial.ttf", 17)
F_CAP = font("Arial Bold.ttf", 21)
F_META = font("Arial.ttf", 15)
F_TAG = font("Arial Bold.ttf", 13)


DESKTOP = [
    ("01-legacy-blog-1440px.png", "1 · Legacy Blog.html",
     "May 2026 handoff · centred type masthead + horizontal featured card",
     "OLDEST"),
    ("02-legacy-article-1440px.png", "2 · Legacy Article.html",
     "May 2026 handoff · full-bleed image hero, text overlaid bottom-left",
     "IMAGE HERO"),
    ("03-journal-v1-1440px.png", "3 · Journal Definitive-v1",
     "Centred masthead + topic filter row + featured card",
     ""),
    ("04-journal-v2-1440px.png", "4 · Journal Definitive-v2 / v3",
     "Hero pixel-identical to v1 apart from lede copy · v2 and v3 identical",
     ""),
    ("06-journal-v4-1440px.png", "5 · Journal Definitive-v4",
     "Same structure · unified FAQ below the fold",
     ""),
    ("07-journal-v5-1440px.png", "6 · Journal Definitive-v5",
     "Type OS hero 72 / 700 · title cased 'From the Studio' · HUB LOCKED",
     "LOCKED"),
    ("08-journal-v6-1440px.png", "7 · Journal Definitive-v6",
     "Hero unchanged from v5 · footer copy fix only",
     ""),
    ("09-shipping-blog-1440px.png", "8 · blog-listing.liquid",
     "SHIPPING · centred type-only masthead, straight into a 3-up card grid",
     "CURRENT"),
    ("10-shipping-article-1440px.png", "9 · article-content.liquid",
     "SHIPPING · centred type-only title, image sits below as contained block",
     "CURRENT"),
]

MOBILE = [
    ("01-legacy-blog-390px.png", "1 · Legacy Blog.html", "May 2026 handoff"),
    ("02-legacy-article-390px.png", "2 · Legacy Article.html", "full-bleed image hero"),
    ("07-journal-v5-390px.png", "6 · Journal v5", "hub Locked"),
    ("08-journal-v6-390px.png", "7 · Journal v6", "footer fix"),
    ("09-shipping-blog-390px.png", "8 · blog-listing.liquid", "shipping"),
    ("10-shipping-article-390px.png", "9 · article-content.liquid", "shipping"),
]


def load(name, width):
    img = Image.open(os.path.join(CROPS, name)).convert("RGB")
    h = round(img.height * width / img.width)
    return img.resize((width, h), Image.LANCZOS)


def tag_chip(draw, x, y, label, fill=ACCENT, fg=BG):
    if not label:
        return
    w = draw.textlength(label, font=F_TAG)
    draw.rounded_rectangle([x, y, x + w + 20, y + 24], radius=12, fill=fill)
    draw.text((x + 10, y + 5), label, font=F_TAG, fill=fg)


def build_desktop():
    cols = 3
    tiles = [(load(n, PANEL_W), t, s, tag) for n, t, s, tag in DESKTOP]

    rows = [tiles[i:i + cols] for i in range(0, len(tiles), cols)]
    row_heights = [CAP_H + max(t[0].height for t in row) for row in rows]

    W = MARGIN * 2 + cols * PANEL_W + (cols - 1) * GUTTER
    H = TITLE_H + sum(row_heights) + GUTTER * (len(rows) - 1) + MARGIN

    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)

    d.text((MARGIN, 38), "Barreletics — Journal / blog hero treatments",
           font=F_TITLE, fill=TEXT)
    d.text((MARGIN, 84),
           "Every hero that has existed in the M4 repo, oldest to newest · "
           "1440px desktop · cropped to the hero band",
           font=F_SUB, fill=MUTED)

    y = TITLE_H
    for row, rh in zip(rows, row_heights):
        x = MARGIN
        for img, title, sub, tag in row:
            d.text((x, y + 4), title, font=F_CAP, fill=TEXT)
            d.text((x, y + 32), sub, font=F_META, fill=MUTED)
            tw = d.textlength(title, font=F_CAP)
            tag_chip(d, x + tw + 16, y + 2, tag)
            canvas.paste(img, (x, y + CAP_H))
            x += PANEL_W + GUTTER
        y += rh + GUTTER

    out = os.path.join(HERE, "GALLERY-journal-heroes-1440.png")
    canvas.save(out)
    return out, canvas.size


def build_mobile():
    width = 390
    tiles = [(load(n, width), t, s) for n, t, s in MOBILE]
    maxh = max(t[0].height for t in tiles)

    W = MARGIN * 2 + len(tiles) * width + (len(tiles) - 1) * GUTTER
    H = TITLE_H + CAP_H + maxh + MARGIN

    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)
    d.text((MARGIN, 38), "Journal / blog heroes — 390px mobile",
           font=F_TITLE, fill=TEXT)
    d.text((MARGIN, 84),
           "Only versions with a meaningfully different mobile hero. "
           "v1–v4 mobile matches v5 apart from the hero size token.",
           font=F_SUB, fill=MUTED)

    x = MARGIN
    for img, title, sub in tiles:
        d.text((x, TITLE_H + 4), title, font=F_CAP, fill=TEXT)
        d.text((x, TITLE_H + 32), sub, font=F_META, fill=MUTED)
        canvas.paste(img, (x, TITLE_H + CAP_H))
        x += width + GUTTER

    out = os.path.join(HERE, "GALLERY-journal-heroes-390.png")
    canvas.save(out)
    return out, canvas.size


if __name__ == "__main__":
    for path, size in (build_desktop(), build_mobile()):
        print("%s  %dx%d" % (path, size[0], size[1]))
