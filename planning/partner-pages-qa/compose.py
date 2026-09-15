#!/usr/bin/env python3
"""
Turn the full-page QA screenshots into readable contact sheets.

A 390x6400 screenshot is unreadable at any zoom that fits a screen, so each shot is
sliced into fixed-height panels and laid out left-to-right. Reading order is the same
as scrolling order.

Usage:
    python3 planning/partner-pages-qa/compose.py
"""

import math
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ["partners", "ambassador", "studio-program", "wholesale"]
# 1440 shots need a harder downscale to fit the same sheet height.
SCALE = {390: 0.60, 1440: 0.34}
PANEL_H = 1600
GAP = 12
BG = (230, 228, 224)


def sheet(src, out, scale):
    im = Image.open(src).convert("RGB")
    panels = math.ceil(im.height / PANEL_H)
    pw = int(im.width * scale)
    ph = int(PANEL_H * scale)
    canvas = Image.new("RGB", (panels * pw + (panels + 1) * GAP, ph + 2 * GAP), BG)
    for i in range(panels):
        strip = im.crop((0, i * PANEL_H, im.width, min((i + 1) * PANEL_H, im.height)))
        canvas.paste(strip.resize((pw, int(strip.height * scale)), Image.LANCZOS),
                     (GAP + i * (pw + GAP), GAP))
    canvas.save(out, quality=88)
    print("%s  %dx%d  %d panels" % (os.path.basename(out), *canvas.size, panels))


def main():
    for name in PAGES:
        for width, scale in SCALE.items():
            src = os.path.join(HERE, "%s-%dpx.png" % (name, width))
            if os.path.exists(src):
                sheet(src, os.path.join(HERE, "_sheet-%s-%d.jpg" % (name, width)), scale)


if __name__ == "__main__":
    main()
