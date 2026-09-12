#!/usr/bin/env python3
"""
Blog / Article / About type QA harness.

The three surfaces under review ship as Liquid sections, so they cannot be opened
in a browser directly. This script lifts the real <style> block out of each
section file and wraps it around static markup that mirrors the section's Liquid
output, using the copy from the matching templates/*.json. The stylesheets are
linked live from shopify-build/assets, so a preview always reflects the current
working tree — edit the section, re-run, re-shoot.

Mobile: headless Chrome on macOS clamps windows to 500px, so true 390px comes
from an iframe inside a wider window (same technique as planning/mobile-qa/mqa.py).

Usage:
    python3 planning/blog-about-type-qa/build.py --label before
    python3 planning/blog-about-type-qa/build.py --label after
    python3 planning/blog-about-type-qa/build.py --label after --no-shots
"""

import argparse
import os
import re
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SECTIONS = os.path.join(REPO, "shopify-build", "sections")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

ASSETS = "../../shopify-build/assets"

LOREM_P1 = (
    "Grip is not a feature you notice until it fails. The moment a carriage moves "
    "under you and your foot slides, the whole practice stops being about strength "
    "and starts being about staying upright."
)
LOREM_P2 = (
    "Performance Skins were designed from the opposite direction: start with the "
    "floor, the carriage, the platform, and work back to the foot. One pair, 360 "
    "degrees of grip, no laundry cycle that slowly kills the silicone dots."
)
LOREM_P3 = (
    "Most studio footwear is a sock with something printed on the bottom. Injection "
    "molding lets the grip be part of the shoe instead of a coating applied to it, "
    "which is why it does not peel after a month of daily classes."
)


def style_of(section):
    """Return the section's <style> body with Liquid interpolation neutralised."""
    src = open(os.path.join(SECTIONS, section + ".liquid")).read()
    blocks = re.findall(r"<style>(.*?)</style>", src, re.S)
    css = "\n".join(blocks)
    css = css.replace("{{ section.id }}", "harness")
    css = re.sub(r"\{\{.*?\}\}", "", css)
    return css


def shell(title, css, body, extra_css=""):
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ASSETS}/design-tokens.css">
<link rel="stylesheet" href="{ASSETS}/barreletics-base.css">
<style>
/* harness only — image stand-ins, no type rules */
.qa-img {{ width: 100%; height: 100%; background: linear-gradient(135deg, #e6e0d4, #cfc6b4); }}
.qa-hero-img {{ width: 100%; aspect-ratio: 16/9; background: linear-gradient(135deg, #e6e0d4, #cfc6b4); }}
{extra_css}
</style>
<style>
{css}
</style>
</head><body>
{body}
</body></html>
"""


def blog_card(title, excerpt, tag, date):
    return f"""            <article class="blog-card">
              <a href="#" class="blog-card__link">
                <div class="blog-card__image-wrap">
                  <div class="qa-img"></div>
                  <span class="blog-card__tag">{tag}</span>
                </div>
                <div class="blog-card__content">
                  <h2 class="blog-card__title">{title}</h2>
                  <p class="blog-card__excerpt">{excerpt}</p>
                  <div class="blog-card__meta">
                    <span class="blog-card__author">Barreletics Team</span>
                    <span class="blog-card__date"><time>{date}</time></span>
                  </div>
                </div>
              </a>
            </article>
"""


BLOG_ARTICLES = [
    ("Why grip socks stop gripping", "Silicone dots are a coating, not a structure. Here is what happens to them after thirty washes.", "Education", "March 12, 2026"),
    ("Reformer footwear, ranked honestly", "We tested every category of studio footwear on a Megaformer for six weeks.", "Reviews", "March 4, 2026"),
    ("The hygiene case for Performance Skins", "Fabric absorbs. Molded material does not. That difference matters more than grip.", "Education", "February 22, 2026"),
    ("What studio owners tell us", "Five instructors on what they wish their clients knew about footwear.", "Studios", "February 9, 2026"),
    ("One pair, three years", "Durability math on a product designed to outlast the hype cycle.", "Product", "January 30, 2026"),
    ("Barre floors are the hardest test", "Sprung wood, sweat, and lateral movement — the worst case for any grip.", "Education", "January 18, 2026"),
    ("Sizing without guesswork", "How to read our size chart if you are between sizes.", "Guides", "January 6, 2026"),
    ("Made in the USA, start to finish", "Material sourcing, molding, and quality control all stay domestic.", "Brand", "December 14, 2025"),
    ("Open sole vs closed sole", "Two constructions, two use cases. A plain-language comparison.", "Guides", "December 2, 2025"),
]


def build_blog():
    cards = "".join(blog_card(*a) for a in BLOG_ARTICLES)
    body = f"""<section class="section">
  <div class="section__inner">
    <div class="blog-listing__header">
      <p class="eyebrow eyebrow--accent">The Journal</p>
      <h1 class="blog-listing__title type-hero">The Barreletics Journal</h1>
      <p class="blog-listing__subtitle">Studio tips, product insights, and performance stories.</p>
    </div>
    <div class="blog-listing__grid">
{cards}
      <nav class="blog-listing__pagination">
        <span class="blog-listing__page-info">Page 1 of 2</span>
        <a href="#" class="btn btn--secondary blog-listing__next">Next &rarr;</a>
      </nav>
    </div>
  </div>
</section>
"""
    return shell("Blog listing — type QA", style_of("blog-listing"), body)


def build_article():
    body = f"""<article class="section">
  <div class="section__inner section__inner--narrow">
    <header class="article__header">
      <span class="article__category">Education</span>
      <h1 class="article__title type-hero">Why grip socks stop gripping</h1>
      <div class="article__meta">
        <span class="article__author">By Barreletics Team</span>
        <time class="article__date">March 12, 2026</time>
      </div>
    </header>
    <div class="article__hero-image"><div class="qa-hero-img"></div></div>
    <div class="article__body rte">
      <p>{LOREM_P1}</p>
      <h2>The coating problem</h2>
      <p>{LOREM_P2}</p>
      <h3>What thirty washes do</h3>
      <p>{LOREM_P3}</p>
      <ul>
        <li>Dots flatten under heat and lose their edge.</li>
        <li>Fabric stretches, so the grip no longer sits where your foot lands.</li>
        <li>Absorbed sweat stays absorbed &mdash; see the <a href="#">size chart</a> for fit notes.</li>
      </ul>
      <p>The short version: <strong>a coating is not a structure.</strong></p>
      <h2>Designing from the floor up</h2>
      <p>{LOREM_P1}</p>
    </div>
    <footer class="article__footer">
      <div class="article__share">
        <span class="article__share-label">Share:</span>
        <a href="#" class="article__share-link">X</a>
        <a href="#" class="article__share-link">Facebook</a>
        <a href="#" class="article__share-link">Email</a>
      </div>
      <div class="article__tags">
        <a href="#" class="article__tag">Education</a>
        <a href="#" class="article__tag">Grip</a>
      </div>
    </footer>
  </div>
</article>

<section class="section section--cream">
  <div class="section__inner">
    <h2 class="article__related-title h2-standard">Keep Reading</h2>
    <div class="article__related-grid">
      <a href="#" class="article__related-card">
        <div class="article__related-image-wrap"><div class="qa-img"></div></div>
        <h3 class="article__related-name">Reformer footwear, ranked honestly</h3>
        <time class="article__related-date">March 4, 2026</time>
      </a>
      <a href="#" class="article__related-card">
        <div class="article__related-image-wrap"><div class="qa-img"></div></div>
        <h3 class="article__related-name">The hygiene case for Performance Skins</h3>
        <time class="article__related-date">February 22, 2026</time>
      </a>
      <a href="#" class="article__related-card">
        <div class="article__related-image-wrap"><div class="qa-img"></div></div>
        <h3 class="article__related-name">One pair, three years</h3>
        <time class="article__related-date">January 30, 2026</time>
      </a>
    </div>
  </div>
</section>
"""
    return shell("Article — type QA", style_of("article-content"), body)


VALUES = [
    ("Performance Over Promise", "Every claim we make is backed by the product itself. Injection-molded grip that never peels. Materials that never absorb. Results you can feel from day one."),
    ("Category Creation", "We're not competing in the grip sock market — we're replacing it. Performance Skins are a new category of studio footwear built from first principles."),
    ("Durability as Design", "Products should outlast the hype cycle. Many customers report 3-4 years of daily use. One purchase replaces years of disposable socks."),
    ("Commitment Match", "You show up 6 days a week. Your gear should match that commitment. Built for people who take their practice seriously."),
    ("Studio-First", "Designed for the demands of real studio environments — reformer carriages, Megaformer platforms, barre floors. Every detail serves the practice."),
]


def build_about():
    values = "".join(
        f"""      <div class="page-about__value">
        <h3 class="page-about__value-title">{t}</h3>
        <p class="page-about__value-body">{d}</p>
      </div>
"""
        for t, d in VALUES
    )
    body = f"""<section class="section">
  <div class="section__inner section__inner--narrow">
    <p class="eyebrow eyebrow--accent page-about__eyebrow">Our Story</p>
    <h1 class="page-about__title type-hero">Redefining Grip</h1>
    <div class="page-about__intro">
      <p>Barreletics is replacing the grip sock category with Performance Skins &mdash; injection-molded grippy shoes engineered for barre, reformer, Lagree, and Pilates.</p>
      <p>Instead of asking 'which grip sock?' we want you asking 'why grip socks at all?' One pair. 360&deg; grip. Done.</p>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="section__inner section__inner--narrow">
    <blockquote class="page-about__manifesto type-statement">
      <p>We didn't improve the grip sock. We made it obsolete.</p>
    </blockquote>
  </div>
</section>

<section class="section section--cream">
  <div class="section__inner">
    <h2 class="page-about__values-title h2-standard">What We Stand For</h2>
    <div class="page-about__values-grid">
{values}    </div>
  </div>
</section>

<section class="section">
  <div class="section__inner section__inner--narrow">
    <div class="page-about__usa">
      <p class="eyebrow">Made in USA</p>
      <h2 class="page-about__usa-title h2-standard">Designed and Made in the USA</h2>
      <div class="page-about__usa-body">
        <p>Every pair of Barreletics is manufactured in the United States. From material sourcing to injection molding to quality control &mdash; the entire process stays domestic. No overseas factories. No compromises on quality oversight.</p>
      </div>
    </div>
  </div>
</section>
"""
    return shell("About — type QA", style_of("page-about"), body)


PAGES = {"blog": build_blog, "article": build_article, "about": build_about}

HARNESS = """<!doctype html>
<html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0;background:#fff}}iframe{{display:block;border:0;margin:0}}</style>
</head><body><iframe id="f" width="{width}" height="{height}" src="{src}"></iframe></body></html>
"""


def run_chrome(args):
    return subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--allow-file-access-from-files", "--force-device-scale-factor=1"] + args,
        capture_output=True, text=True, timeout=300)


def page_height(path, width):
    r = run_chrome(["--window-size=%d,900" % max(width, 500), "--virtual-time-budget=6000",
                    "--dump-dom", path])
    m = re.search(r"data-qa-h=\"(\d+)\"", r.stdout or "")
    return int(m.group(1)) if m else 0


def shoot_desktop(path, out_png, width=1440):
    run_chrome(["--window-size=%d,3000" % width, "--virtual-time-budget=8000",
                "--screenshot=" + out_png, "--hide-scrollbars", path])


def shoot_mobile(path, out_png, width=390, height=6400):
    harness = os.path.join(HERE, "__shot-harness.html")
    with open(harness, "w") as fh:
        fh.write(HARNESS.format(width=width, height=height, src=os.path.basename(path)))
    tmp = os.path.join(tempfile.gettempdir(), "blogabout-raw.png")
    try:
        run_chrome(["--window-size=%d,%d" % (max(width + 110, 500), height),
                    "--virtual-time-budget=8000", "--screenshot=" + tmp, harness])
        if not os.path.exists(tmp):
            return False
        try:
            from PIL import Image
            im = Image.open(tmp)
            im.crop((0, 0, min(width, im.width), im.height)).save(out_png)
        except Exception:
            shutil.copy(tmp, out_png)
        return True
    finally:
        for f in (harness, tmp):
            if os.path.exists(f):
                os.remove(f)


MOBILE_HEIGHT = {"blog": 5400, "article": 3600, "about": 3200}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="after")
    ap.add_argument("--no-shots", action="store_true")
    ap.add_argument("--pages", nargs="*", default=list(PAGES))
    a = ap.parse_args()

    for name in a.pages:
        html = PAGES[name]()
        path = os.path.join(HERE, "preview-%s.html" % name)
        with open(path, "w") as fh:
            fh.write(html)
        print("built %s" % os.path.relpath(path, REPO))
        if a.no_shots:
            continue
        d = os.path.join(HERE, "%s-%s-1440.png" % (name, a.label))
        shoot_desktop(path, d)
        print("  desktop %s" % os.path.basename(d))
        m = os.path.join(HERE, "%s-%s-390.png" % (name, a.label))
        shoot_mobile(path, m, height=MOBILE_HEIGHT[name])
        print("  mobile  %s" % os.path.basename(m))


if __name__ == "__main__":
    main()
