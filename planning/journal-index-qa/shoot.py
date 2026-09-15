#!/usr/bin/env python3
"""
Journal index QA — shipping `blog-listing.liquid` vs the approved
`docs/Barreletics Journal - Definitive-v6.html` mock.

The section ships as Liquid, so it cannot be opened in a browser. This script
lifts the real <style> block out of sections/blog-listing.liquid and wraps it
around static markup that mirrors the section's Liquid output, using the copy
from templates/blog.json and the article set from the v6 mock (same CDN images,
so the side-by-side compares design, not stand-in art). Same lift technique as
planning/blog-about-type-qa/build.py.

  before-*.png  masthead straight into the 3-up grid (what shipped)
  after-*.png   masthead -> topic filter -> featured article -> 3-up grid
  mock-*.png    the .journal-index band of the v6 mock, cropped
  COMPARE-*.png mock | after, side by side

Headless Chrome on macOS clamps windows to 500px, so 390px comes from
Emulation.setDeviceMetricsOverride over CDP rather than --window-size (same
approach as planning/journal-hero-gallery/shoot.py).

Read-only against docs/ — the mock is never written to.

Usage:
    python3 planning/journal-index-qa/shoot.py                 # build + shoot everything
    python3 planning/journal-index-qa/shoot.py --build-only
"""

import argparse
import base64
import http.client
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.parse

import websocket  # websocket-client

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SECTIONS = os.path.join(REPO, "shopify-build", "sections")
ASSETS = "../../shopify-build/assets"
MOCK = "docs/Barreletics Journal - Definitive-v6.html"

CDN = "https://barreletics.com/cdn/shop"

# Masthead copy is templates/blog.json (approved — unchanged by this work).
EYEBROW = "The Journal"
TITLE = "From the Studio"
LEDE = ("Care that extends grip life, founder notes on why socks failed, and "
        "stories from instructors who dig into chair pose without resetting.")

TOPICS = ["All", "Care", "Founder", "Movement", "Story", "Wellness"]

FEATURED = {
    "title": "How to wash your Performance Skins",
    "meta": "Care · Featured · 3 min",
    "dek": ("A 60-second rinse that keeps molded grip working for years — and the "
            "dryer heat that kills traction faster than studio sweat."),
    "cta": "Read the guide",
    "img": CDN + "/files/Multi_Image.jpg?v=1768346625&width=1600",
    "alt": "Performance Skins — studio care",
    "tag": "Care",
    "date": "March 18, 2026",
}

# The v6 mock's grid, in order.
ARTICLES = [
    ("Why we built a grip-sock replacement",
     "Eight years of barre, three failed prototypes, and the studio conversation that started Barreletics.",
     "Founder", "March 12, 2026",
     CDN + "/products/barreletixxjumpingtogether.jpg?v=1619360969&width=1200"),
    ("Coperni × Barreletics, in Paris",
     "Behind the SS26 runway — and what it means to build a Pilates shoe for haute couture.",
     "Story", "March 4, 2026",
     CDN + "/files/Copreni_Final_More_grey.png?v=1774119812&width=1200"),
    ("A barre teacher’s shoe routine",
     "From morning Megaformer to evening recovery — what one instructor wears when flat back chair can’t slip.",
     "Movement", "February 22, 2026",
     CDN + "/files/IMG_2917.jpg?v=1741040637&width=1200"),
    ("When to retire your Performance Skins",
     "Three signs the grip is past its working life — and why one pair still beats eight of socks.",
     "Care", "February 9, 2026",
     CDN + "/products/barreletixxstefrunningpinkbackground.jpg?v=1710549452&width=1200"),
    ("Inside the SS26 runway",
     "A behind-the-scenes look at the night Barreletics walked the Coperni runway in Paris.",
     "Story", "January 30, 2026",
     CDN + "/files/Multi_Image.jpg?v=1768346625&width=1200"),
    ("Why barefoot still wins",
     "Open-toe freedom that still holds through water ski and lunges — smarter than grip socks that slide when wet.",
     "Wellness", "January 18, 2026",
     CDN + "/files/Square_Pink.png?v=1764627088&width=1200"),
]


def style_of(section):
    """Return the section's <style> body with Liquid interpolation neutralised."""
    with open(os.path.join(SECTIONS, section + ".liquid")) as fh:
        src = fh.read()
    css = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    css = css.replace("{{ section.id }}", "harness")
    return re.sub(r"\{\{.*?\}\}", "", css)


def shell(title, css, body):
    return """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%s/design-tokens.css">
<link rel="stylesheet" href="%s/barreletics-base.css">
<style>
%s
</style>
</head><body>
%s
</body></html>
""" % (title, ASSETS, ASSETS, css, body)


def masthead():
    return """    <div class="blog-listing__header">
      <p class="eyebrow eyebrow--accent">%s</p>
      <h1 class="blog-listing__title type-hero">%s</h1>
      <p class="blog-listing__subtitle">%s</p>
    </div>
""" % (EYEBROW, TITLE, LEDE)


def topics():
    links = "".join(
        '        <a href="#" class="journal-topics__link%s"%s>%s</a>\n'
        % (" is-active" if i == 0 else "",
           ' aria-current="page"' if i == 0 else "", t)
        for i, t in enumerate(TOPICS))
    return '    <nav class="journal-topics" aria-label="Topics">\n%s    </nav>\n' % links


def feature():
    f = FEATURED
    return """    <article class="journal-feature">
      <a class="journal-feature__media" href="#" aria-label="Read %(title)s" tabindex="-1">
        <img src="%(img)s" alt="%(alt)s" width="1200" height="900" class="journal-feature__image">
      </a>
      <div class="journal-feature__copy">
        <p class="journal-feature__meta">%(meta)s</p>
        <h2 class="journal-feature__title type-statement"><a href="#">%(title)s</a></h2>
        <p class="journal-feature__dek">%(dek)s</p>
        <a href="#" class="btn btn--primary journal-feature__cta">%(cta)s</a>
      </div>
    </article>
""" % f


def card(title, dek, tag, date, img):
    return """        <article class="blog-card">
          <a href="#" class="blog-card__link" aria-label="Read %(title)s">
            <div class="blog-card__image-wrap">
              <img src="%(img)s" alt="%(title)s" width="720" height="450" loading="lazy" class="blog-card__image">
              <span class="blog-card__tag">%(tag)s</span>
            </div>
            <div class="blog-card__content">
              <h2 class="blog-card__title">%(title)s</h2>
              <p class="blog-card__excerpt">%(dek)s</p>
              <div class="blog-card__meta">
                <span class="blog-card__author">Barreletics Team</span>
                <span class="blog-card__date"><time>%(date)s</time></span>
              </div>
            </div>
          </a>
        </article>
""" % {"title": title, "dek": dek, "tag": tag, "date": date, "img": img}


def grid(items):
    cards = "".join(card(*a) for a in items)
    return """    <div class="blog-listing__grid">
%s        <nav class="blog-listing__pagination" aria-label="Blog pagination">
          <span class="blog-listing__page-info">Page 1 of 2</span>
          <a href="#" class="btn btn--secondary blog-listing__next">Next &rarr;</a>
        </nav>
    </div>
""" % cards


def wrap(inner):
    return '<section class="section">\n  <div class="section__inner">\n%s  </div>\n</section>\n' % inner


def build():
    css = style_of("blog-listing")

    f = FEATURED
    before_items = [(f["title"], f["dek"], f["tag"], f["date"], f["img"])] + ARTICLES
    before = wrap(masthead() + grid(before_items))
    after = wrap(masthead() + topics() + feature() + grid(ARTICLES))

    out = {}
    for label, body in (("before", before), ("after", after)):
        path = os.path.join(HERE, "preview-%s.html" % label)
        with open(path, "w") as fh:
            fh.write(shell("Journal index — %s" % label, css, body))
        out[label] = path
        print("built %s" % os.path.relpath(path, REPO))
    return out


# --------------------------------------------------------------------------
# Chrome / CDP
# --------------------------------------------------------------------------

HIDE_CSS = ".mock-banner { display: none !important; }"

MEASURE = r"""
(() => {
  const el = document.querySelector(__SEL__);
  if (!el) return { error: 'not found' };
  const r = el.getBoundingClientRect();
  return {
    top: Math.max(0, Math.floor(r.top + window.scrollY)),
    bottom: Math.ceil(r.bottom + window.scrollY)
  };
})()
"""


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Chrome:
    def __init__(self, width, height):
        self.port = free_port()
        self.profile = tempfile.mkdtemp(prefix="jiq-")
        self.proc = subprocess.Popen(
            [CHROME, "--headless=new", "--disable-gpu", "--no-first-run",
             "--no-default-browser-check", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--allow-file-access-from-files",
             "--remote-debugging-port=%d" % self.port, "--remote-allow-origins=*",
             "--user-data-dir=" + self.profile,
             "--window-size=%d,%d" % (width, height), "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.ws = None
        self._id = 0
        self._connect()

    def _connect(self):
        deadline = time.time() + 45
        last = None
        while time.time() < deadline:
            try:
                # http.client, not urllib: urllib honours HTTP(S)_PROXY, which sends
                # loopback DevTools requests to a proxy that cannot answer them.
                conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
                conn.request("GET", "/json/list")
                raw = conn.getresponse().read()
                conn.close()
                for t in json.loads(raw):
                    if t.get("type") == "page":
                        self.ws = websocket.create_connection(
                            t["webSocketDebuggerUrl"], timeout=60,
                            max_size=256 * 1024 * 1024)
                        return
            except Exception as e:
                last = e
                time.sleep(0.4)
        raise RuntimeError("could not attach to headless Chrome: %r" % (last,))

    def send(self, method, params=None):
        self._id += 1
        mid = self._id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError("%s: %s" % (method, msg["error"]))
                return msg.get("result", {})

    def close(self):
        try:
            if self.ws:
                self.ws.close()
        finally:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except Exception:
                self.proc.kill()
            shutil.rmtree(self.profile, ignore_errors=True)


def evaluate(ch, expr):
    r = ch.send("Runtime.evaluate", {"expression": expr, "returnByValue": True,
                                     "awaitPromise": True})
    if r.get("exceptionDetails"):
        raise RuntimeError(json.dumps(r["exceptionDetails"])[:600])
    return r["result"].get("value")


def file_url(rel):
    return "file://" + urllib.parse.quote(os.path.join(REPO, rel))


def shoot(rel_path, out_name, width, mobile, selector, settle, scale=2):
    ch = Chrome(max(width, 520) + 140, 1100)
    try:
        ch.send("Page.enable")
        ch.send("Runtime.enable")
        ch.send("Emulation.setDeviceMetricsOverride",
                {"width": width, "height": 1000, "deviceScaleFactor": scale,
                 "mobile": mobile})
        ch.send("Page.addScriptToEvaluateOnNewDocument", {
            "source": "document.addEventListener('DOMContentLoaded', () => {"
                      " const s = document.createElement('style');"
                      " s.textContent = %s; document.head.appendChild(s); });"
                      % json.dumps(HIDE_CSS)})
        ch.send("Page.navigate", {"url": file_url(rel_path)})
        time.sleep(settle)

        # captureBeyondViewport never scrolls, so lazy card images below the fold
        # would shoot as empty boxes. Promote them and wait for the decode.
        evaluate(ch, "Array.from(document.images).forEach(i => { i.loading = 'eager'; });"
                     "Promise.all(Array.from(document.images).map("
                     "i => i.decode().catch(() => null)))")
        time.sleep(2)

        m = evaluate(ch, MEASURE.replace("__SEL__", json.dumps(selector)))
        if not m or m.get("error"):
            return {"error": "selector not found: %s" % selector, "png": None}

        broken = evaluate(ch, "Array.from(document.images)"
                              ".filter(i => i.complete && i.naturalWidth === 0)"
                              ".map(i => i.currentSrc || i.src).slice(0, 8)") or []

        top, bottom = m["top"], min(m["bottom"], 20000)
        shot = ch.send("Page.captureScreenshot",
                       {"format": "png",
                        "clip": {"x": 0, "y": top, "width": width,
                                 "height": bottom - top, "scale": 1},
                        "captureBeyondViewport": True})
        png = os.path.join(HERE, out_name)
        with open(png, "wb") as fh:
            fh.write(base64.b64decode(shot["data"]))
        return {"png": os.path.relpath(png, REPO), "height": bottom - top,
                "brokenImages": broken}
    finally:
        ch.close()


def compose(left_png, right_png, out_png, left_label, right_label, width):
    from PIL import Image, ImageDraw, ImageFont

    a = Image.open(left_png).convert("RGB")
    b = Image.open(right_png).convert("RGB")
    # Shot at deviceScaleFactor 2 — halve for a composite that stays a sane size.
    a = a.resize((width, round(a.height * width / a.width)), Image.LANCZOS)
    b = b.resize((width, round(b.height * width / b.width)), Image.LANCZOS)

    band, gap, pad = 44, 24, 20
    h = max(a.height, b.height) + band + pad * 2
    canvas = Image.new("RGB", (width * 2 + gap + pad * 2, h), "#ffffff")
    canvas.paste(a, (pad, pad + band))
    canvas.paste(b, (pad + width + gap, pad + band))

    d = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 20)
    except Exception:
        font = ImageFont.load_default()
    d.text((pad, pad + 8), left_label, fill="#1c1916", font=font)
    d.text((pad + width + gap, pad + 8), right_label, fill="#1c1916", font=font)
    d.line([(pad + width + gap // 2, pad), (pad + width + gap // 2, h - pad)],
           fill="#d6cfc0", width=2)
    canvas.save(out_png)
    return os.path.relpath(out_png, REPO)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build-only", action="store_true")
    ap.add_argument("--settle", type=float, default=5.0)
    a = ap.parse_args()

    build()
    if a.build_only:
        return

    results = []
    for width, mobile in ((1440, False), (390, True)):
        for label in ("before", "after"):
            r = shoot("planning/journal-index-qa/preview-%s.html" % label,
                      "%s-%dpx.png" % (label, width), width, mobile,
                      "section.section", a.settle)
            r["key"] = "%s-%d" % (label, width)
            results.append(r)
            print(json.dumps(r), file=sys.stderr)

        r = shoot(MOCK, "mock-%dpx.png" % width, width, mobile,
                  ".journal-index", a.settle)
        r["key"] = "mock-%d" % width
        results.append(r)
        print(json.dumps(r), file=sys.stderr)

        try:
            out = compose(os.path.join(HERE, "mock-%dpx.png" % width),
                          os.path.join(HERE, "after-%dpx.png" % width),
                          os.path.join(HERE, "COMPARE-%dpx.png" % width),
                          "MOCK — Journal Definitive-v6",
                          "AFTER — blog-listing.liquid",
                          width)
            print("composed %s" % out, file=sys.stderr)
        except Exception as e:
            print("compose failed: %r" % (e,), file=sys.stderr)

    with open(os.path.join(HERE, "manifest.json"), "w") as fh:
        json.dump(results, fh, indent=1)


if __name__ == "__main__":
    main()
