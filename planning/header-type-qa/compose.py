#!/usr/bin/env python3
"""
Stacks header renders into one labelled comparison image.

Rows are captured at devicePixelRatio 2 and halved here, so the composite shows the
header at true CSS pixel size — what a 1440px (or 390px) screen actually shows.

Usage:
    python3 planning/header-type-qa/compose.py
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

INK = (28, 25, 22)
MUTED = (107, 100, 90)
RULE = (214, 207, 192)
PAGE = (250, 249, 246)

LABEL_H = 34
PAD = 20
GAP = 14


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def load(name, logical_width, crop_css=None):
    """Return the shot at 1 image px per CSS px. `crop_css` is (top, bottom) in CSS px."""
    im = Image.open(os.path.join(HERE, name)).convert("RGB")
    ratio = im.width / float(logical_width)  # captured devicePixelRatio
    if crop_css:
        top, bottom = crop_css
        im = im.crop((0, int(top * ratio), im.width, int(bottom * ratio)))
    return im.resize((logical_width, int(im.height / ratio)), Image.LANCZOS)


def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def compose(out_name, rows, width, title, subtitle):
    """rows = [(image, label, note), ...]"""
    f_title = font(FONT_BOLD, 17)
    f_sub = font(FONT_REG, 12)
    f_label = font(FONT_BOLD, 14)
    f_note = font(FONT_REG, 12)

    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    sub_lines = wrap(probe, subtitle, f_sub, width)
    # A note only shares the label's line if it fits; otherwise it wraps beneath.
    row_heads = []
    for _, label, note in rows:
        inline_w = width - probe.textlength(label, font=f_label) - 12
        note_lines = wrap(probe, note, f_note, inline_w) if note else []
        row_heads.append(note_lines)

    head_h = 40 + 16 * len(sub_lines)
    total_h = head_h + PAD
    for (im, _, _), note_lines in zip(rows, row_heads):
        total_h += im.height + GAP + 22 + 16 * max(0, len(note_lines) - 1)

    canvas = Image.new("RGB", (width + PAD * 2, total_h), PAGE)
    d = ImageDraw.Draw(canvas)

    d.text((PAD, 14), title, font=f_title, fill=INK)
    y = 38
    for line in sub_lines:
        d.text((PAD, y), line, font=f_sub, fill=MUTED)
        y += 16

    y = head_h
    for (im, label, _), note_lines in zip(rows, row_heads):
        d.text((PAD, y), label, font=f_label, fill=INK)
        lw = probe.textlength(label, font=f_label)
        for i, line in enumerate(note_lines):
            d.text((PAD + lw + 12 if i == 0 else PAD, y + 1 + i * 16),
                   line, font=f_note, fill=MUTED)
        y += 22 + 16 * max(0, len(note_lines) - 1)
        canvas.paste(im, (PAD, y))
        d.rectangle([PAD, y, PAD + im.width - 1, y + im.height - 1], outline=RULE)
        y += im.height + GAP

    path = os.path.join(HERE, out_name)
    canvas.save(path)
    print("%-46s %dx%d" % (out_name, canvas.width, canvas.height))
    return path


def main():
    # --- Desktop: ours 18 / ours 22 / live -------------------------------------
    ours18 = load("band-18-desktop-1440px.png", 1440)
    ours22 = load("band-22-desktop-1440px.png", 1440)
    # Live's .site-header is 178px tall because its own trust row sits inside it; crop to
    # the logo + nav row so type is compared row-to-row, not block-to-block.
    live = load("live-desktop-band-1440px.png", 1440, crop_css=(90, 205))

    compose(
        "COMPARE-desktop-1440px.png",
        [(ours18, "18px", "current committed default · nav_link_size 18"),
         (ours22, "22px", "preview only · nav_link_size 22"),
         (live, "live (22px at rest)", "barreletics.com · theme 185687998755 · Streamline 7.0")],
        width=1440,
        title="Header nav size — 18px vs 22px, desktop 1440px",
        subtitle="Roboto 400 · 0.025em · title case in all rows. Reconciled M4 Menu labels. "
                 "Rendered at true CSS pixel size.",
    )

    # --- Mobile: closed bar, then drawer ---------------------------------------
    bar18 = load("band-18-mobile-390px.png", 390)
    bar22 = load("band-22-mobile-390px.png", 390)
    compose(
        "COMPARE-mobile-bar-390px.png",
        [(bar18, "18px", "nav is hidden <768px — hamburger + logo + actions only"),
         (bar22, "22px", "identical: nav_link_size never paints on mobile")],
        width=390,
        title="Header bar — 18px vs 22px, mobile 390px",
        subtitle="The desktop nav does not render below 768px, so the closed bar is "
                 "unaffected by nav size. Crowding shows up in the drawer instead.",
    )

    dr18 = load("size-18-mobile-drawer-390px.png", 390)
    dr22 = load("size-22-mobile-drawer-390px.png", 390)
    compose(
        "COMPARE-mobile-drawer-390px.png",
        [(dr18, "18px", "drawer links follow --type-nav-size"),
         (dr22, "22px", "preview only")],
        width=390,
        title="Mobile drawer — 18px vs 22px, 390px",
        subtitle="Drawer panel is 300px wide (max 85vw). Longest label: "
                 "Shop All Grippy Shoes.",
    )


if __name__ == "__main__":
    main()
