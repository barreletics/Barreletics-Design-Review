#!/usr/bin/env python3
"""Before / after for the PDP reviews slot — curated social-proof vs live Judge.me.

Andrew authorised live Judge.me reviews on 2026-08-08 ("Live for everything"), not
a layout change, so the swap has to be shown rather than assumed neutral. This
lifts the reviews section out of the pre-swap preview and the post-swap preview,
drops both into the same page shell and CSS, and shoots them at 1440 and 390.

    python3 planning/reviews-live-qa/compare.py
"""

import os
import re
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
QA = os.path.join(REPO, "planning", "pdp-variants-qa")
BEFORE = os.path.join(HERE, "before")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def section_of(path, cls):
    src = open(path, encoding="utf-8").read()
    m = re.search(r'<section class="%s".*?</section>' % cls, src, re.S)
    if not m:
        raise SystemExit("no <section class=%s> in %s" % (cls, path))
    return m.group(0)


def head_of(path):
    """Reuse the preview's own <head> so both panels get identical tokens/CSS."""
    src = open(path, encoding="utf-8").read()
    head = re.search(r"<head>(.*?)</head>", src, re.S).group(1)
    # The previews sit one directory deeper than this harness.
    return head.replace("../../shopify-build/assets", "../../shopify-build/assets")


SHELL = """<!doctype html>
<html lang="en"><head>{head}
<style>
html,body{{margin:0;padding:0;background:#fff}}
.cmp-label{{background:{bg};color:#fff;padding:12px 24px;
  font:700 12px/1.4 Roboto,sans-serif;letter-spacing:.14em;text-transform:uppercase}}
.cmp-label span{{display:block;font-weight:400;letter-spacing:.04em;text-transform:none;
  font-size:12px;color:#f0e6dd;margin-top:4px}}
</style>
</head><body>
<div class="cmp-label">{label}<span>{note}</span></div>
{body}
</body></html>
"""

PANELS = [
    ("before", os.path.join(BEFORE, "preview-closed.html"), "qa-social", "#6b645a",
     "Before — curated social-proof",
     "Hand-authored review blocks in product.json. Not live data."),
    ("after", os.path.join(QA, "preview-closed.html"), "qa-rev", "#1c1916",
     "After — live Judge.me (pdp-reviews)",
     "Judge.me widget renders at runtime; static preview shows the labelled stand-in."),
]


def run_chrome(args):
    return subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--allow-file-access-from-files", "--force-device-scale-factor=1"] + args,
        capture_output=True, text=True, timeout=300)


HARNESS = ('<!doctype html><html><head><meta charset="utf-8">'
           '<style>html,body{{margin:0;padding:0;background:#fff}}'
           'iframe{{display:block;border:0;margin:0}}</style></head>'
           '<body><iframe width="{width}" height="{height}" src="{src}"></iframe></body></html>')


def shoot(path, out_png, width, height):
    if width >= 500:
        run_chrome(["--window-size=%d,%d" % (width, height), "--virtual-time-budget=12000",
                    "--screenshot=" + out_png, path])
        return
    harness = os.path.join(HERE, "__cmp-harness.html")
    with open(harness, "w") as fh:
        fh.write(HARNESS.format(width=width, height=height, src=os.path.basename(path)))
    tmp = os.path.join(tempfile.gettempdir(), "cmp-raw.png")
    try:
        run_chrome(["--window-size=%d,%d" % (width + 120, height), "--virtual-time-budget=12000",
                    "--screenshot=" + tmp, harness])
        from PIL import Image
        im = Image.open(tmp)
        im.crop((0, 0, min(width, im.width), im.height)).save(out_png)
    finally:
        for f in (harness, tmp):
            if os.path.exists(f):
                os.remove(f)


def trim(path):
    """Drop the blank tail so the two panels compose at their real heights."""
    from PIL import Image, ImageChops
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    box = ImageChops.difference(im, bg).getbbox()
    if box:
        im.crop((0, 0, im.width, min(im.height, box[3] + 24))).save(path)


def compose(paths, out_png, gap=24):
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in paths]
    h = max(i.height for i in ims)
    w = sum(i.width for i in ims) + gap * (len(ims) - 1)
    canvas = Image.new("RGB", (w, h), "#ffffff")
    x = 0
    for im in ims:
        canvas.paste(im, (x, 0))
        x += im.width + gap
    canvas.save(out_png)


def main():
    for width, tag, height in ((1440, "1440", 2600), (390, "390", 3200)):
        shots = []
        for name, src, cls, bg, label, note in PANELS:
            page = os.path.join(HERE, "__%s-%s.html" % (name, tag))
            with open(page, "w") as fh:
                fh.write(SHELL.format(head=head_of(src), body=section_of(src, cls),
                                      bg=bg, label=label, note=note))
            out = os.path.join(HERE, "%s-%s.png" % (name, tag))
            shoot(page, out, width, height)
            trim(out)
            os.remove(page)
            shots.append(out)
            print("shot %s" % os.path.basename(out))
        combo = os.path.join(HERE, "REVIEWS-BEFORE-AFTER-%spx.png" % tag)
        compose(shots, combo)
        print("composed %s" % os.path.basename(combo))


if __name__ == "__main__":
    main()
