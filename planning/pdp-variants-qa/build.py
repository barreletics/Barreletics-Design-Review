#!/usr/bin/env python3
"""
PDP variant QA harness — Closed Sole (product.json) vs Open Sole vs Outdoor.

2026-08-08, Andrew's direction: the refined v19 spine (templates/product.json)
now serves Closed Sole; Open Sole moved to templates/product.open-sole.json.

The three PDPs ship as Shopify templates, so they cannot be opened in a browser.
This script reads the real templates/product*.json settings, lifts the real
<style> blocks out of the matching sections/*.liquid, and wraps them around
static markup that mirrors each section's Liquid output. Stylesheets link live
from shopify-build/assets, so a preview always reflects the working tree.

Every section renders for real — there are no stubs. variant-grid, the buy-box
accordions, home-juicer and pdp-sticky-atc used to be placeholder strips, which
is why the previews read as "the accordion section is missing the descriptions"
and "where is the all variants". Fixed 2026-08-08. variant-grid, buy box and
sticky ATC are driven by real store data in product-data.json. Juicer uses the
same pattern as SEO v37: live embed-code.js + a mosaic of REAL juicer.io media
as fallback so the Instagram section never shows empty product placeholders.
See README.md for the full fidelity table.

Reviews, 2026-08-08 evening: hybrid — 3 curated photo cards + live Judge.me
text row under. Judge.me still cannot fetch in a static file (labelled stand-in).

Mobile: headless Chrome on macOS clamps windows to 500px, so true 390px comes
from an iframe inside a wider window (same technique as planning/mobile-qa/mqa.py
and planning/blog-about-type-qa/build.py).

Usage:
    python3 planning/pdp-variants-qa/build.py
    python3 planning/pdp-variants-qa/build.py --no-shots
"""

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SECTIONS = os.path.join(REPO, "shopify-build", "sections")
SNIPPETS = os.path.join(REPO, "shopify-build", "snippets")
TEMPLATES = os.path.join(REPO, "shopify-build", "templates")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ASSETS = "../../shopify-build/assets"

PAGES = [
    # H1 matches locked Definitive-v19 — NO "— Open/Closed Sole" in the title.
    # Badge: Open = rust; Closed/Outdoor = charcoal (CURRENT MESSAGE 2026-08-08).
    ("closed", "product.json", "Closed Sole — default product template (v19 spine)",
     "Best Grippy Shoes for Barre, Pilates & Yoga",
     "/products/best-reformer-pilates-legree-workout-shoes", "$74.00", "Closed Sole", "#1c1916"),
    ("open", "product.open-sole.json", "Open Sole — product.open-sole template",
     "Best Grippy Shoes for Barre, Pilates & Yoga",
     "/products/studio-performance-skin-footwear", "$74.00", "Open Sole", "#c45c3f"),
    ("outdoor", "product.outdoor.json", "Outdoor — product.outdoor template",
     "Grippy Water Shoes",
     "/products/aquatic-performance-skins", "$74.00", "Outdoor", "#1c1916"),
]

# Live product.images from storefront.js (same CDN URLs the real PDP uses).
# Regenerated into product-data.json; build prefers product-data gallery if present.
GALLERY = {
    "open": [
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/Studio_TopBottom_Pink-1000x1000.jpg?v=1776396965",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/black_desktop_3.jpg?v=1776396965",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/Blue__1_2490f04b-134f-43a4-add6-3f8319947f25.jpg?v=1776396965",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/Performance-Skin-Footwear-White_a7103efd-c227-477c-84f8-41352ac1053e.jpg?v=1776396965",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/studio-performance-skin-footwear.jpg?v=1776396965",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/Front_3QT_Pink-600x600_4d6c963a-2d0e-4b41-8fad-9bb0bef6d135.jpg?v=1773521092",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/files/Rvian_Green_Final.png?v=1772558925",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/files/Blue_Heaven_Open_Final.png?v=1772474002",
    ],
    "closed": [
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/files/Purple_45b2348c-f5a1-45a8-a704-88f8afd10414.jpg?v=1776454640",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/files/A14_TopBottom_Yellow-600x600.jpg?v=1776454640",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/Rear_3QT_Blue-600x600.jpg?v=1776454640",
    ],
    "outdoor": [
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/A14_TopBottom_Yellow-600x600_15161205-cd7c-4bb9-b9c4-a1e8d1d0d042.jpg?v=1749228033",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/A14_Front_3QT_Blue-600x600_1e8fd664-a864-4672-8be2-df6887d705ee.jpg?v=1749228033",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/files/A14_TopBottom_LightGray-1000x1000.jpg?v=1749228033",
        "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/A14_TopBottom_Blue-1000x1000.jpg?v=1773920303",
    ],
}

# Hexes match pdp-buy-box.liquid swatch case — signed-off visual, not invent.
def swatch_hex(name):
    key = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return {
        "onyx": "#050505", "black": "#050505", "ebony": "#050505",
        "dusty-rose": "#e9d3cb", "dustyrose": "#e9d3cb",
        "stone": "#c9c5b8", "light-grey": "#c9c5b8", "lightgrey": "#c9c5b8",
        "light-gray": "#c9c5b8",
        "sage": "#7b8c84",
        "white": "#ffffff", "cream": "#ffffff",
        "terracotta": "#d4a78a", "peach": "#d4a78a",
        "espresso": "#3d3530", "dark-grey": "#3d3530", "darkgrey": "#3d3530",
        "mist": "#b8c4c0",
        "mocha": "#8b7355",
        "forest": "#5c6b5e",
        "rivian-green": "#5c6b45", "rivian": "#5c6b45", "olive": "#5c6b45",
        "green": "#5c6b45",
        "coperni": "#c8b99a",
        "cobalt": "#2f5fa7", "blue": "#2f5fa7", "cobalt-blue": "#2f5fa7",
        "orange": "#c45c3f", "brand-coral": "#c45c3f", "coral": "#c45c3f",
        "bright-yellow": "#e8c93f", "yellow": "#e8c93f",
        "turquoise": "#3fa8a0",
        "deep-teal": "#2b5f5c",
        "purple": "#6b4d8a",
        "copper-swirl": "#b08a6a",
        "dusty-blue": "#7a9bb0",
    }.get(key, "#d6cfc0")

SWATCHES = {
    "open": ["Rivian Green", "Bright Yellow", "White", "Coral", "Black", "Blue",
             "LightGrey", "DarkGrey", "Dusty Blue"],
    "closed": ["Dusty Rose", "Turquoise", "Copper Swirl", "Deep Teal", "Black",
               "Bright Yellow", "LightGrey", "Purple", "DarkGrey", "Coral", "Blue", "White"],
    "outdoor": ["DarkGrey", "Black", "Blue", "Bright Yellow", "White", "LightGrey", "Coral"],
}


# --------------------------------------------------------------------------- css

def styles_of(path):
    """Return a file's <style> bodies with Liquid interpolation neutralised."""
    src = open(path).read()
    css = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    css = css.replace("#shopify-section-{{ section.id }} ", "")
    css = css.replace("{{ section.id }}", "harness")
    css = re.sub(r"\{%.*?%\}", "", css, flags=re.S)
    css = re.sub(r"\{\{.*?\}\}", "", css)
    return css


def collect_css():
    parts = [styles_of(os.path.join(SECTIONS, n + ".liquid")) for n in (
        "value-strip", "pdp-features", "disciplines", "fifty-fifty",
        "fullbleed-statement", "pdp-sock-math", "guarantee-band", "pdp-reviews",
        "pdp-buy-box", "variant-grid", "home-juicer")]
    parts.append(styles_of(os.path.join(SNIPPETS, "faq-accordion.liquid")))
    parts.append(styles_of(os.path.join(SNIPPETS, "sticky-atc.liquid")))
    return "\n".join(parts)


def load_product_data():
    with open(os.path.join(HERE, "product-data.json")) as fh:
        return json.load(fh)["products"]


PRODUCTS = load_product_data()


def money(v):
    """Mirror Liquid money_without_trailing_zeros."""
    return "$%d" % v if float(v).is_integer() else "$%.2f" % v


# ------------------------------------------------------------------------ render

def esc(s):
    return html.escape(s or "", quote=False)


def raw(s):
    """Settings that legitimately carry markup (<br>, <strong>, richtext)."""
    return s or ""


def sec(t, key, default=None):
    return t["sections"].get(key, {"settings": {}, "blocks": {}}) if default is None else default


def blocks_of(s):
    order = s.get("block_order") or list(s.get("blocks", {}))
    return [s["blocks"][k] for k in order if k in s.get("blocks", {})]


def gallery_for(slug):
    """Live PDP media: product-data gallery/featured + colour images, else GALLERY."""
    p = PRODUCTS.get(slug) or {}
    out = []
    for key in ("gallery", "images"):
        for u in p.get(key) or []:
            if u and u not in out:
                out.append(u)
    feat = p.get("featured")
    if feat and feat not in out:
        out.insert(0, feat)
    for u in (p.get("colour_images") or {}).values():
        if u and u not in out:
            out.append(u)
    if not out:
        out = list(GALLERY.get(slug) or [])
    return out[:8] or list(GALLERY.get(slug) or [])


def r_buybox(s, page):
    """Mirror pdp-buy-box.liquid markup + signed-off CSS classes (no qa-* sizing)."""
    slug, _, _, title, url, price, badge, badge_bg = page
    g = gallery_for(slug)
    st = s["settings"]
    hero = g[0] if g else ""
    thumbs = "".join(
        '<button class="pdp-gallery__thumb%s" type="button" aria-label="View image %d">'
        '<img src="%s" alt="" width="72" height="72" loading="lazy"></button>'
        % (" is-active" if i == 0 else "", i + 1, u)
        for i, u in enumerate(g[:6]))
    colors = SWATCHES.get(slug) or list((PRODUCTS.get(slug) or {}).get("colour_images") or {})
    sw = "".join(
        '<button type="button" class="pdp-buy__swatch%s" aria-label="%s" data-color="%s" '
        'style="background: %s;%s"></button>'
        % (
            " is-active" if i == 0 else "",
            esc(name), esc(name), swatch_hex(name),
            " box-shadow: inset 0 0 0 1px #ccc;" if swatch_hex(name) == "#ffffff" else "",
        )
        for i, name in enumerate(colors))
    kit = ""
    if st.get("show_kit_links"):
        kit = (
            '<div class="pdp-buy__kit-links">'
            '<span class="pdp-buy__kit-label">%s</span>'
            '<div class="pdp-buy__kit-row">'
            '<a class="pdp-buy__kit-link" href="#">%s</a>'
            '<a class="pdp-buy__kit-link" href="#">%s</a>'
            '</div>'
            '<p class="pdp-buy__kit-hint">%s</p></div>' % (
                esc(st.get("kit_label", "")),
                esc(st.get("kit_link_1_label", "")),
                esc(st.get("kit_link_2_label", "")),
                esc(st.get("kit_hint", "")),
            ))
    soon_cls = " pdp-buy__sizes--soon" if st.get("show_soon_size") else ""
    soon = ""
    if st.get("show_soon_size"):
        soon = ('<button type="button" class="pdp-buy__size-btn is-soon" disabled>'
                'S<span class="pdp-buy__size-range">Coming soon</span></button>')
    note = ""
    if st.get("show_soon_size") and st.get("size_soon_note"):
        note = '<p class="pdp-buy__size-note">%s</p>' % esc(st["size_soon_note"])
    badge_html = ""
    badge_label = st.get("sole_badge") or badge
    color_key = (st.get("sole_badge_color") or "rust").lower()
    badge_hex = {
        "blue": "#458CD9",
        "charcoal": "#1c1916",
        "black": "#000000",
        "rust": "#c45c3f",
        "orange": "#c45c3f",
    }.get(color_key, badge_bg or "#c45c3f")
    if st.get("show_sole_badge", True) and badge_label:
        badge_html = (
            '<span class="pdp-buy__badge" style="--pdp-badge-bg: %s;">%s</span>'
            % (badge_hex, esc(badge_label)))
    rating = ""
    if st.get("show_rating_row") is not False:
        rating = (
            '<div class="pdp-buy__rating">'
            '<span class="pdp-buy__stars" aria-hidden="true">★★★★★</span>'
            '<span class="pdp-buy__rating-text">%s</span>'
            '<a href="#reviews" class="pdp-buy__reviews-link">Reviews →</a>'
            '</div>' % esc(st.get("rating_text") or "Trusted by 1,000+ Instructors"))
    return f"""
<section id="buy" class="pdp-hero" aria-label="Product details" data-buy-box>
  <div class="pdp-gallery">
    <div class="pdp-gallery__hero">
      <img id="pdp-main-img" src="{hero}" alt="{esc(title)}" loading="eager">
    </div>
    <div class="pdp-gallery__thumbs">{thumbs}</div>
  </div>
  <div class="pdp-buy">
    {rating}
    <div class="pdp-buy__header">
      <h1 class="pdp-buy__seo-title">{esc(title)}</h1>
      {badge_html}
    </div>
    <p class="pdp-buy__name">
      <span style="font-weight:400;">{esc(st.get('lede_line_1',''))}</span><br>
      <span style="font-weight:400;">{esc(st.get('lede_line_2',''))}</span>
    </p>
    <p class="pdp-buy__desc">{esc(st.get('short_description',''))}</p>
    <div class="pdp-buy__price-block">
      <span class="pdp-buy__price-now">{price}</span>
      <span class="pdp-buy__price-meta">{esc(st.get('payment_line',''))}</span>
    </div>
    <div class="pdp-buy__option">
      <div class="pdp-buy__option-header">
        <span class="pdp-buy__option-label">Color · <span>{esc(colors[0] if colors else '')}</span></span>
      </div>
      <div class="pdp-buy__swatches">{sw}</div>
    </div>
    <div class="pdp-buy__option">
      <div class="pdp-buy__option-header">
        <span class="pdp-buy__option-label">Size</span>
      </div>
      <div class="pdp-buy__sizes{soon_cls}">{soon}
        <button type="button" class="pdp-buy__size-btn is-active">M
          <span class="pdp-buy__size-range">W 5.5–7.5</span></button>
        <button type="button" class="pdp-buy__size-btn">L
          <span class="pdp-buy__size-range">W 8–11</span></button>
      </div>
      {note}
    </div>
    <button type="button" class="btn btn--primary pdp-buy__cta">Add to cart</button>
    {kit}
    {accordions(slug, st)}
    <p class="qa-url">{url}</p>
  </div>
</section>"""


def accordions(slug, st):
    """The four real pdp-buy-box accordions, in section order.

    pdp-buy-box.liquid renders Description / Care & how to wear / Shipping /
    30-day returns + 90-day warranty as <details>. The first two were missing
    from this harness entirely, which is what read as "the accordion section is
    missing the descriptions".
    """
    rows = [
        ("Description", "<p>%s</p>" % esc(PRODUCTS[slug]["description"])),
        ("Care &amp; how to wear",
         "<p><strong>How to put on:</strong> pull from the top of the foot — not the straps — "
         "to help extend their lifespan.</p>"
         "<p><strong>Cleaning:</strong> warm soapy water, rinse well, air dry. "
         "No machine washing.</p>"),
        ("Shipping", esc(st.get("shipping_accordion", ""))),
        ("30-day returns + 90-day warranty", esc(st.get("returns_accordion", ""))),
    ]
    note = PRODUCTS[slug].get("description_note")
    if note:
        rows[0] = (rows[0][0],
                   rows[0][1] + '<p class="qa-admin-flag">%s</p>' % esc(note))
    # Closed, exactly as the theme renders them. They used to be force-opened,
    # which spilled the Shipping and returns policy text into the buy box as a
    # wall of loose copy — the section reads completely differently that way.
    items = "".join(
        '<details class="pdp-accordion" data-pdp-accordion>'
        '<summary class="pdp-accordion__trigger" aria-expanded="false">%s <span>+</span></summary>'
        '<div class="pdp-accordion__body">%s</div></details>' % (label, body)
        for label, body in rows)
    return '<div class="pdp-buy__accordions">%s</div>' % items


def r_value_strip(s, page):
    """Both lines, as the section renders them: the full · list on desktop and the
    show_on_mobile subset below 768px. The harness used to emit only the desktop
    span, so the strip vanished at 390px."""
    def line(blocks):
        return '<span class="value-strip__sep" aria-hidden="true"> · </span>'.join(
            '<span class="value-strip__text">%s</span>' % esc(b["settings"]["text"])
            for b in blocks)
    items = [b for b in blocks_of(s) if b["settings"].get("text")]
    short = [b for b in items if b["settings"].get("show_on_mobile") is not False]
    return ('<section class="section-frame value-strip-section">'
            '<div class="value-strip trust-strip__inner">'
            '<span class="value-strip__full">%s</span>'
            '<span class="value-strip__short">%s</span>'
            '</div></section>' % (line(items), line(short)))


def r_features(s, page):
    st = s["settings"]
    eyebrow = ('<p class="pdp-features__eyebrow">%s</p>' % esc(st["eyebrow"])) if st.get("eyebrow") else ""
    cells = "".join(
        '<div class="pdp-feature"><p class="pdp-feature__title">%s</p>'
        '<p class="pdp-feature__desc">%s</p></div>' % (
            esc(b["settings"]["title"]), esc(b["settings"]["description"]))
        for b in blocks_of(s))
    return (f'<section class="pdp-features"><div class="pdp-features__inner">'
            f'<header class="pdp-features__header">{eyebrow}'
            f'<h2 class="pdp-features__title">{raw(st.get("title"))}</h2></header>'
            f'<div class="pdp-features__grid">{cells}</div></div></section>')


def r_disciplines(s, page):
    st = s["settings"]
    moves = ""
    for i, b in enumerate(blocks_of(s)):
        if i:
            moves += '<span aria-hidden="true"><em>·</em></span>'
        moves += "<span>%s</span>" % esc(b["settings"]["discipline"])
    head = esc(st.get("headline", "")).replace("\n", "<br>")
    return (f'<section class="section-frame discipline-film">'
            f'<div class="discipline-film__inner">'
            f'<p class="discipline-film__line h2-display">{head}</p>'
            f'<div class="discipline-film__moves">{moves}</div></div></section>')


def r_fifty(s, page):
    st = s["settings"]
    contain = st.get("media_fit") == "contain"
    cls = "section-frame split-section"
    if st.get("reverse"):
        cls += " split-section--reverse"
    if contain:
        cls += " split-section--contain"
    media_pct = st.get("media_column_pct", 50)
    focal = st.get("image_position", "center")
    if focal == "custom":
        focal = "%s%% %s%%" % (st.get("focal_x", 50), st.get("focal_y", 50))
    # Mirror the Liquid `assign … | default:` block verbatim. These used to be
    # hardcoded (520 / 72 / 78%), so the harness measured a page the theme never
    # renders — spacing QA off it was meaningless.
    style = (f"--ff-media-fr:{media_pct}fr;--ff-text-fr:{100 - media_pct}fr;"
             f"--ff-min-height:{st.get('min_height', 640)}px;"
             f"--ff-mobile-media-height:{st.get('mobile_media_height', 320)}px;"
             f"--ff-column-gap:{st.get('column_gap', 0)}px;"
             f"--ff-side-padding:{st.get('side_padding', 64)}px;"
             f"--ff-vertical-padding:{st.get('vertical_padding', 88)}px;"
             f"--ff-contain-width:{st.get('contain_width', 72)}%;"
             f"--ff-object-position:{focal};"
             f"--ff-image-scale:{st.get('image_scale', 100) / 100.0};"
             f"--ff-media-radius:{st.get('media_radius', 0)}px;"
             f"--ff-text-radius:{st.get('section_radius', 0)}px;"
             f"--ff-quote-star:#d4af37;--ff-quote-style:italic;"
             f"--ff-cta-bg:#1c1916;--ff-cta-border:#1c1916;--ff-cta-text:#fff;"
             f"background:{st.get('bg_color', '#fff')};")
    src = st.get("poster_url") or st.get("image_url") or ""
    media_bg = st.get("media_bg", "#f9f9f9")
    media = ('<div class="split-media"%s><img class="split-media__img" src="%s" alt="%s"></div>'
             % (' style="background:%s;"' % media_bg if contain else "", src, esc(st.get("image_alt", ""))))
    style_kind = st.get("content_style", "standard")
    tcls = "split-text align-editorial"
    if style_kind == "quote":
        tcls += " split-text--quote"
    elif style_kind == "statement":
        tcls += " split-text--statement"
    if style_kind == "quote":
        inner = ('<div class="split-quote__stars" aria-hidden="true">★★★★★</div>'
                 '<p class="split-quote__text">“%s”</p>'
                 '<p class="split-quote__author">%s</p>'
                 '<p class="split-quote__meta">%s</p>' % (
                     esc(st.get("title", "")), esc(st.get("quote_author", "")),
                     esc(st.get("quote_meta", ""))))
        if st.get("cta_text"):
            inner += ('<a class="btn split-cta split-cta--after-stack btn--primary">%s</a>'
                      % esc(st["cta_text"]))
    else:
        eyebrow = ('<p class="split-text__eyebrow type-label%s">%s</p>' % (
            "" if style_kind == "statement" else " eyebrow--accent", esc(st["eyebrow"]))
        ) if st.get("eyebrow") else ""
        if style_kind == "statement":
            title_class = "split-text__title type-statement"
        elif st.get("heading_register") == "standard":
            title_class = "split-text__title h2-standard"
        else:
            title_class = "split-text__title h2-display"
        inner = '%s<h2 class="%s">%s</h2>' % (eyebrow, title_class, raw(st.get("title")))
        if st.get("body"):
            inner += ('<p class="split-text__body type-body%s">%s</p>' % (
                " split-text__body--quiet" if style_kind == "statement" else "", esc(st["body"])))
        if st.get("cta_text"):
            inner += '<a class="btn split-cta btn--primary">%s</a>' % esc(st["cta_text"])
    return ('<section class="%s" style="%s">%s<div class="%s" style="background:%s;">%s</div></section>'
            % (cls, style, media, tcls, st.get("bg_color", "#fff"), inner))


# The shot windows are 12000-18000px tall, so vh-based section heights would blow
# up. Resolve them against a nominal real viewport instead.
VH_DESKTOP, VH_MOBILE = 900, 844


def r_fullbleed(s, page):
    st = s["settings"]
    show = st.get("show_text", True)
    cls = "section-frame fullbleed-statement" + ("" if show else " fullbleed-statement--media-only")
    hd = round(int(st.get("height_desktop", "64")) / 100 * VH_DESKTOP)
    hm = round(int(st.get("height_mobile", "52")) / 100 * VH_MOBILE)
    style = (f"--fb-media-radius:0px;--fb-height-desktop:{hd}px;--fb-height-mobile:{hm}px;"
             f"--fb-overlay:rgba(28,25,22,0.55);--fb-cta-bg:#fff;--fb-cta-border:#fff;"
             f"--fb-cta-text:#1c1916;")
    body = ""
    if show:
        body = ('<div class="fullbleed-statement__content">'
                '<p class="fullbleed-statement__line type-statement">%s</p>%s</div>' % (
                    raw(st.get("title")),
                    '<a class="fullbleed-statement__cta">%s</a>' % esc(st["cta_text"])
                    if st.get("cta_text") else ""))
    return ('<section class="%s" style="%s"><div class="fullbleed-statement__bg">'
            '<img src="%s" alt="%s" width="2000" height="1200"></div>%s</section>'
            % (cls, style, st.get("image_url", ""), esc(st.get("image_alt", "")), body))


def r_sock_math(s, page):
    st = s["settings"]
    quote = ""
    if st.get("quote"):
        quote = ('<blockquote class="sock-math__quote"><p>“%s”</p><cite>— %s</cite></blockquote>'
                 % (esc(st["quote"]), esc(st.get("quote_cite", ""))))
    theirs = "".join('<li><span class="sock-math__x" aria-hidden="true">✗</span>%s</li>' % esc(
        st.get("theirs_%d" % i, "")) for i in (1, 2, 3))
    ours = "".join('<li><span class="sock-math__check" aria-hidden="true">✓</span>%s</li>' % esc(
        st.get("ours_%d" % i, "")) for i in (1, 2, 3))
    return f"""
<section class="sock-math sock-math--compact">
  <div class="sock-math__header"><h2 class="sock-math__headline">{esc(st.get('headline',''))}</h2></div>
  <p class="sock-math__sub">{esc(st.get('subheadline',''))}</p>
  <div class="sock-math__inner">{quote}
    <div class="sock-math__grid">
      <div class="sock-math__col sock-math__col--theirs">
        <p class="sock-math__col-brand">{esc(st.get('theirs_label',''))}</p>
        <p class="sock-math__col-price">{esc(st.get('their_price',''))}<span>/yr</span></p>
        <ul class="sock-math__list">{theirs}</ul>
      </div>
      <div class="sock-math__col sock-math__col--ours">
        <p class="sock-math__col-brand sock-math__col-brand--accent">{esc(st.get('ours_label',''))}</p>
        <p class="sock-math__col-price sock-math__col-price--bold">{esc(st.get('our_price',''))}<span> once</span></p>
        <ul class="sock-math__list">{ours}</ul>
      </div>
    </div>
  </div>
</section>"""


def r_reviews(s, page):
    """pdp-reviews — 3 photo cards + 6 text cards (original community row).

    Matches pdp-reviews.liquid: curated text_review blocks under photo cards.
    Live Judge.me is skipped on compact PDPs when text cards are present.
    """
    st = s["settings"]
    head = ""
    if st.get("title") or st.get("body"):
        cta = ('<a class="pdp-reviews__more" href="%s">%s</a>'
               % (esc(st.get("all_reviews_url") or "/pages/reviews"),
                  esc(st["all_reviews_label"]))
               if st.get("all_reviews_label") else "")
        head = (
            '<header class="pdp-reviews__head"><div>'
            '<h2 class="pdp-reviews__title h2-standard">%s</h2>'
            '<p class="pdp-reviews__body">%s</p></div>%s</header>'
            % (esc(st.get("title", "")), esc(st.get("body", "")), cta))
    photos = []
    texts = []
    for b in blocks_of(s):
        bs = b.get("settings") or {}
        body = (bs.get("body") or "").strip().strip('"').strip("\u201c").strip("\u201d")
        if b.get("type") == "photo_review" and len(photos) < 3 and st.get("show_photo_cards", True):
            photos.append(
                '<article class="pdp-reviews__photo-card">'
                '<div class="pdp-reviews__photo-img pdp-reviews__photo-img--empty" '
                'role="img" aria-label="Add customer photo"><span>Add image</span></div>'
                '<div class="pdp-reviews__photo-pad">'
                '<div class="pdp-reviews__photo-stars" aria-hidden="true">★★★★★</div>'
                '<p class="pdp-reviews__photo-body">“%s”</p>'
                '<footer class="pdp-reviews__photo-footer">'
                '<span class="pdp-reviews__photo-author">%s</span>'
                '<span class="pdp-reviews__photo-loc">%s</span>'
                '</footer></div></article>'
                % (esc(body), esc(bs.get("author", "")), esc(bs.get("location", "")))
            )
        elif b.get("type") == "text_review" and len(texts) < 6 and st.get("show_text_cards", True):
            texts.append(
                '<article class="pdp-reviews__text-card">'
                '<div class="pdp-reviews__text-stars" aria-hidden="true">★★★★★</div>'
                '<p class="pdp-reviews__text-body">“%s”</p>'
                '<footer class="pdp-reviews__text-footer">'
                '<span class="pdp-reviews__text-author">%s</span>'
                '<span class="pdp-reviews__text-loc">%s</span>'
                '</footer></article>'
                % (esc(body), esc(bs.get("author", "")), esc(bs.get("location", "")))
            )
    photo = ('<div class="pdp-reviews__photo-grid">%s</div>' % "".join(photos)) if photos else ""
    text = ""
    if texts:
        label = ""
        if st.get("community_label"):
            label = '<p class="pdp-reviews__community-label">%s</p>' % esc(st["community_label"])
        text = label + '<div class="pdp-reviews__text-grid">%s</div>' % "".join(texts)
    return f"""
<section class="section-frame pdp-reviews pdp-reviews--compact" id="reviews"
  style="background:{st.get('bg_color', '#ffffff')};">
  <div class="pdp-reviews__inner">{head}
    {photo}
    {text}
  </div>
</section>"""


def r_guarantee(s, page):
    st = s["settings"]
    items = "".join('<div class="guarantee-item"><h4>%s</h4><p>%s</p></div>'
                    % (esc(b["settings"]["title"]), esc(b["settings"]["detail"]))
                    for b in blocks_of(s))
    return (f'<section class="section-frame guarantee-section" style="--guarantee-cols:3;">'
            f'<div class="guarantee-head"><p class="guarantee-head__eyebrow type-label">{esc(st.get("eyebrow",""))}</p>'
            f'<h2 class="guarantee-head__title type-statement">{esc(st.get("title",""))}</h2></div>'
            f'<div class="guarantee-inner">{items}</div></section>')


def r_faq(s, page):
    st = s["settings"]
    # Closed by default — same as the theme. Never force-open (that made the
    # FAQ look like a wall of open copy instead of accordions).
    items = "".join(
        '<details class="faq__item"><summary class="faq__trigger">'
        '<span class="faq__question">%s</span><span class="faq__icon" aria-hidden="true"></span>'
        '</summary><div class="faq__body">%s</div></details>'
        % (esc(b["settings"].get("question", "")), raw(b["settings"].get("answer", "")))
        for b in blocks_of(s))
    return (f'<div class="faq faq--cream"><div class="faq__inner">'
            f'<h2 class="faq__heading">{esc(st.get("heading",""))}</h2>'
            f'<div class="faq__list">{items}</div></div></div>')


def var_card(key, v, sole_label, tab_key, msg="meta"):
    """Mirror snippets/variant-card.liquid for one colour×size variant."""
    p = PRODUCTS[key]
    img = p["colour_images"].get(v["colour"], p["featured"])
    name = v["colour"]
    meta = "%s · Size %s" % (sole_label, v["size"])
    limited = sole_label == "One-Off"
    if limited:
        meta = "One-Off · Limited Edition"
    badges = ('<span class="var-card__badge var-card__badge--le">Limited Edition</span>'
              if limited else "")
    if v["available"]:
        media = ('<a class="var-card__img var-card__imglink" href="/products/%s">'
                 '<img src="%s" alt="%s" width="600" height="600" loading="lazy">%s</a>'
                 % (p["handle"], img, esc(name), badges))
        title = '<a href="/products/%s">%s</a>' % (p["handle"], esc(name))
        action = ('<form class="var-card__form"><button type="button" class="var-card__add">'
                  'Quick Add →</button></form>')
    else:
        media = ('<div class="var-card__img"><img src="%s" alt="%s" width="600" height="600" '
                 'loading="lazy" class="var-card__img--muted">'
                 '<span class="var-card__badge var-card__badge--soldout">Sold Out</span>%s</div>'
                 % (img, esc(name), badges))
        title = esc(name)
        action = '<span class="var-card__sold">Sold Out</span>'
    return (
        '<article class="var-card var-card--msg-%s%s" data-tab="%s" data-br-size="%s">'
        '%s<div class="var-card__content">'
        '<p class="var-card__name">%s</p>'
        '<p class="var-card__meta">%s</p>'
        '<p class="var-card__price">%s</p>'
        '<p class="var-card__installment">or 4 × %s</p>'
        '%s</div></article>'
        % (msg, "" if v["available"] else " var-card--sold-out", tab_key, v["size"],
           media, title, esc(meta), money(v["price"]), money(round(v["price"] / 4.0, 2)),
           action))


def r_variant_grid(s, page):
    """Real variant grid — tabs, size filter, See all, real cards.

    Mirrors sections/variant-grid.liquid + snippets/variant-grid-panel.liquid,
    populated from the live product/variant data in product-data.json.
    """
    st = s["settings"]
    anchor = st.get("anchor_id") or "variants"
    tabs_spec = [("closed", "show_closed", "label_closed", "Closed Sole"),
                 ("open", "show_open", "label_open", "Open Sole"),
                 ("oneoffs", "show_oneoffs", "label_oneoffs", "One-Offs"),
                 ("outdoor", "show_outdoor", "label_outdoor", "Outdoor")]
    live = [(k, st.get(lk) or dl) for k, sk, lk, dl in tabs_spec
            if st.get(sk) and k in PRODUCTS]
    default_tab = st.get("default_tab", "closed")
    if default_tab not in [k for k, _ in live]:
        default_tab = live[0][0] if live else "closed"

    tabs = "".join(
        '<button type="button" class="variants-tab%s" role="tab" aria-selected="%s" '
        'data-tab="%s">%s</button>'
        % (" is-active" if k == default_tab else "",
           "true" if k == default_tab else "false", k, esc(label))
        for k, label in live)

    panels = ""
    for k, _ in live:
        p = PRODUCTS[k]
        cards = "".join(var_card(k, v, p["sole_label"], k,
                                 st.get("card_messaging", "meta"))
                        for v in p["variants"])
        panels += ('<div class="var-grid%s" id="grid-%s" data-grid-tab="%s">%s</div>'
                   % ("" if k == default_tab else " is-grid-hidden", k, k, cards))

    eyebrow = ('<p class="variants-head__eyebrow type-label eyebrow--accent">%s</p>'
               % esc(st["eyebrow"])) if st.get("eyebrow") else ""
    body = ('<p class="variants-head__body type-body">%s</p>'
            % esc(st["body"])) if st.get("body") else ""
    see_label = st.get("see_all_label") or "See all colors & styles"
    return f"""
<section class="section-frame variants-section" id="{esc(anchor)}" aria-label="Shop all styles"
  data-variants-collapse data-initial-rows="{st.get('initial_rows', 2)}"
  data-see-all="{esc(st.get('see_all', 'expand'))}" data-variants-expanded="false"
  data-default-tab="{esc(default_tab)}">
  <div class="variants-inner">
    <header class="variants-head align-editorial">{eyebrow}
      <h2 class="variants-head__title h2-standard">{esc(st.get('title', ''))}</h2>{body}
    </header>
    <div class="variants-toolbar">
      <div class="variants-tabs" role="tablist">{tabs}</div>
      <div class="variants-utils">
        <div class="variants-size" data-variants-size>
          <span class="variants-size__label">Size</span>
          <button type="button" class="variants-size__btn is-active" data-size="M">M</button>
          <button type="button" class="variants-size__btn" data-size="L">L</button>
        </div>
        <a href="/pages/performance-skins-size-chart" class="variants-link">Size chart →</a>
        <a href="/pages/compare-open-closed-sole" class="variants-link">Compare →</a>
      </div>
    </div>
    {panels}
    <div class="variants-see-all">
      <button type="button" class="variants-see-all__btn" data-variants-see-all
        data-see-all-label="{esc(see_label)}" aria-expanded="false">{esc(see_label)}</button>
    </div>
  </div>
</section>
{VARIANT_GRID_JS.replace('__ANCHOR__', anchor)}"""


def fetch_juicer_posts(feed_id="barreletics", per=12):
    """Pull real Instagram media URLs from juicer.io (same feed as the theme)."""
    url = "https://www.juicer.io/api/feeds/%s?page=1&per=%d" % (feed_id, per)
    try:
        raw = subprocess.check_output(
            ["curl", "-sL", url], stderr=subprocess.DEVNULL, timeout=20)
        data = json.loads(raw.decode())
        items = (data.get("posts") or {}).get("items") or []
    except Exception:
        items = []
    out = []
    for p in items:
        img = p.get("image") or ""
        href = p.get("full_url") or "https://www.instagram.com/barreletics/"
        if img:
            out.append((img, href))
    return out


def r_juicer(s, page):
    """home-juicer — same pattern as SEO v37 (the one that actually worked).

    Live juicer embed + mosaic of REAL juicer.io Instagram media as fallback.
    Never product-photo placeholders. Force https API_ROOT before the embed
    script (protocol-relative juicer URLs flake on localhost http).
    """
    st = s["settings"]
    per = int(st.get("posts_per_page", 12) or 12)
    pages = int(st.get("max_pages", 1) or 1)
    feed = st.get("feed_id") or "barreletics"
    posts = fetch_juicer_posts(feed, per)
    if not posts:
        # Last-resort known-good juicer media (from the live feed, not product shots)
        posts = [
            ("https://www.juicer.io/api/media/25133084?s=13d4f192cbade0cc5ce80079e3bfa4b584a64e38",
             "https://www.instagram.com/p/C0SUkpDrjuf/"),
            ("https://www.juicer.io/api/posts/468037265/images.jpg?external_id=CrTvd_Bvohm&s=653c4db1371a8490d730ac6b0d5f8406c05ba2c9",
             "https://www.instagram.com/p/CrTvd_Bvohm/"),
            ("https://www.juicer.io/api/posts/466191034/images.jpg?external_id=CcGEm78L2F8&s=30318da99b47d4a2b79182629198cac74b311e13",
             "https://www.instagram.com/p/CcGEm78L2F8/"),
        ]
    cards = "".join(
        '<a class="home-juicer__fallback-card" href="%s" target="_blank" rel="noopener noreferrer">'
        '<img src="%s" alt="" loading="lazy"></a>' % (esc(href), esc(img))
        for img, href in posts[:per])
    eyebrow = ('<p class="home-juicer__eyebrow type-label">%s</p>'
               % esc(st["eyebrow"])) if st.get("eyebrow") else ""
    body = ('<p class="home-juicer__body type-body">%s</p>'
            % esc(st["body"])) if st.get("body") else ""
    see_more = ('<button type="button" class="home-juicer__see-more" data-juicer-see-more>'
                'See more</button>' if st.get("enable_see_more") else "")
    return f"""
<section class="section-frame home-juicer home-juicer--see-more is-fallback"
  id="{esc(st.get('anchor_id', 'instagram'))}"
  aria-label="{esc(st.get('title', 'Instagram'))}"
  data-juicer-root data-feed-id="{esc(feed)}" data-per="{per}" data-pages="{pages}">
  <div class="home-juicer__inner">{eyebrow}
    <h2 class="home-juicer__title h2-standard">{esc(st.get('title', ''))}</h2>{body}
    <div class="home-juicer__feed" data-juicer-feed-wrap>
      <ul class="juicer-feed" data-feed-id="{esc(feed)}" data-per="{per}" data-pages="{pages}"></ul>
      <div class="home-juicer__fallback" data-juicer-fallback aria-hidden="false">{cards}</div>
    </div>
    {see_more}
    <a class="home-juicer__cta" href="{esc(st.get('profile_url', ''))}"
      target="_blank" rel="noopener noreferrer"
      >{esc(st.get('cta_text', ''))}</a>
  </div>
</section>
<script>
window.Juicer = window.Juicer || {{}};
window.Juicer.Constants = window.Juicer.Constants || {{}};
window.Juicer.Constants.API_ROOT = 'https://www.juicer.io';
</script>
<script src="https://www.juicer.io/embed/{esc(feed)}/embed-code.js?per={per}&pages={pages}" async></script>
<script>
(function () {{
  var root = document.querySelector('[data-juicer-root]');
  if (!root) return;
  var fallback = root.querySelector('[data-juicer-fallback]');
  var live = false;
  function feedEl() {{ return root.querySelector('.juicer-feed'); }}
  function juicerReady() {{
    var feed = feedEl();
    if (!feed) return false;
    if (feed.classList.contains('j-initialized') || feed.classList.contains('loaded')) return true;
    return !!feed.querySelector('.j-stacker img, .j-image img, img[src*="juicer.io"]');
  }}
  function showLive() {{
    if (live) return;
    live = true;
    root.classList.add('is-juicer-live');
    root.classList.remove('is-fallback');
    if (fallback) fallback.setAttribute('aria-hidden', 'true');
  }}
  function tick() {{ if (juicerReady()) showLive(); }}
  document.addEventListener('juicer:feedLoaded', showLive);
  setInterval(tick, 400);
  setTimeout(tick, 1200);
  setTimeout(function () {{ if (!live && juicerReady()) showLive(); }}, 4000);
}})();
</script>"""


def r_sticky(s, page):
    """The real sticky-atc bar. Pinned open in the harness — in Shopify it slides
    in once the buy box scrolls away, which a static capture can never show."""
    slug, _, _, title, url, price, badge, badge_bg = page
    p = PRODUCTS[slug]
    return f"""
<div class="sticky-atc is-visible qa-sticky" role="complementary" aria-label="Quick add to cart">
  <div class="sticky-atc__inner">
    <div class="sticky-atc__product">
      <img class="sticky-atc__thumb" src="{p['featured']}" alt="" width="40" height="40">
      <div class="sticky-atc__info">
        <span class="sticky-atc__title">{esc(title)}</span>
        <span class="sticky-atc__price">{price}</span>
      </div>
    </div>
    <div class="sticky-atc__actions">
      <span class="sticky-atc__size">Size: M (W 5.5-7.5)</span>
      <button type="button" class="sticky-atc__btn btn btn--primary">Add to Cart — {price}</button>
    </div>
  </div>
</div>"""


# Brand-owned imagery standing in for the Juicer tiles, which only exist at runtime.
JUICER_TILES = [
    "https://barreletics.com/cdn/shop/products/barreletixxjumpingtogether.jpg?v=1619360969&width=600",
    "https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg?v=1710549457&width=600",
    "https://cdn.shopify.com/s/files/1/0045/0612/4391/files/Multi_Image.jpg?v=1768346625&width=600",
    "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/Studio_TopBottom_Pink-1000x1000.jpg?v=1776396965&width=600",
    "https://cdn.shopify.com/s/files/1/0045/0612/4391/files/Purple_45b2348c-f5a1-45a8-a704-88f8afd10414.jpg?v=1776454640&width=600",
    "https://cdn.shopify.com/s/files/1/0045/0612/4391/products/black_desktop_3.jpg?v=1776396965&width=600",
]

# Lifted from sections/variant-grid.liquid so tabs, size filter and See all
# behave exactly as they do in the theme.
VARIANT_GRID_JS = """
<script>
(function () {
  var section = document.getElementById('__ANCHOR__');
  if (!section) return;
  var activeSize = 'M', resizeT;
  function cols() { return window.matchMedia('(max-width: 1024px)').matches ? 2 : 4; }
  function limitFor() {
    var rows = parseInt(section.getAttribute('data-initial-rows') || '2', 10) || 2;
    return rows * cols();
  }
  function grids() { return section.querySelectorAll('.var-grid'); }
  function activeGrid() {
    var list = grids();
    for (var i = 0; i < list.length; i++) {
      if (!list[i].classList.contains('is-grid-hidden')) return list[i];
    }
    return list[0] || null;
  }
  function cardsOf(grid) {
    if (!grid) return [];
    return Array.prototype.filter.call(grid.children, function (el) {
      return el.classList && el.classList.contains('var-card') &&
        !el.classList.contains('is-size-hidden');
    });
  }
  function applySizeFilter() {
    section.querySelectorAll('.var-card').forEach(function (card) {
      var size = (card.getAttribute('data-br-size') || 'M').toUpperCase();
      card.classList.toggle('is-size-hidden', size !== activeSize);
    });
  }
  function applyCollapse() {
    var mode = section.getAttribute('data-see-all') || 'expand';
    var expanded = section.getAttribute('data-variants-expanded') === 'true' || mode === 'off';
    var limit = limitFor();
    var wrap = section.querySelector('.variants-see-all');
    var btn = section.querySelector('[data-variants-see-all]');
    grids().forEach(function (grid) {
      var visibleIdx = 0;
      Array.prototype.forEach.call(grid.children, function (card) {
        if (!card.classList || !card.classList.contains('var-card')) return;
        if (card.classList.contains('is-size-hidden')) {
          card.classList.add('is-variants-hidden');
          return;
        }
        card.classList.toggle('is-variants-hidden', !(expanded || visibleIdx < limit));
        visibleIdx++;
      });
    });
    var total = cardsOf(activeGrid()).length;
    var needs = mode !== 'off' && total > limit;
    if (wrap) { if (needs) wrap.removeAttribute('hidden'); else wrap.setAttribute('hidden', ''); }
    if (btn && mode === 'expand') {
      btn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      var openLabel = btn.getAttribute('data-see-all-label') || 'See all colors & styles';
      btn.textContent = expanded ? 'Show fewer' : openLabel;
    }
  }
  function switchTab(tab) {
    section.setAttribute('data-variants-expanded', 'false');
    grids().forEach(function (grid) {
      grid.classList.toggle('is-grid-hidden',
        !(tab === 'all' || grid.getAttribute('data-grid-tab') === tab));
    });
    section.querySelectorAll('.variants-tab').forEach(function (t) {
      var on = t.getAttribute('data-tab') === tab;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    applyCollapse();
  }
  section.querySelectorAll('.variants-tab').forEach(function (tab) {
    tab.addEventListener('click', function () { switchTab(tab.getAttribute('data-tab')); });
  });
  section.querySelectorAll('[data-size]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      activeSize = btn.getAttribute('data-size');
      section.querySelectorAll('[data-size]').forEach(function (b) {
        b.classList.toggle('is-active', b === btn);
      });
      section.setAttribute('data-variants-expanded', 'false');
      applySizeFilter(); applyCollapse();
    });
  });
  var seeBtn = section.querySelector('[data-variants-see-all]');
  if (seeBtn && (section.getAttribute('data-see-all') || 'expand') === 'expand') {
    seeBtn.addEventListener('click', function () {
      var open = section.getAttribute('data-variants-expanded') === 'true';
      section.setAttribute('data-variants-expanded', open ? 'false' : 'true');
      applyCollapse();
    });
  }
  applySizeFilter(); applyCollapse();
  window.addEventListener('resize', function () {
    clearTimeout(resizeT); resizeT = setTimeout(applyCollapse, 120);
  });
})();
</script>"""

RENDERERS = {
    "pdp-buy-box": r_buybox,
    "value-strip": r_value_strip,
    "pdp-features": r_features,
    "disciplines": r_disciplines,
    "fifty-fifty": r_fifty,
    "fullbleed-statement": r_fullbleed,
    "pdp-sock-math": r_sock_math,
    "pdp-reviews": r_reviews,
    "guarantee-band": r_guarantee,
    "collection-faq": r_faq,
    "variant-grid": r_variant_grid,
    "home-juicer": r_juicer,
    "pdp-sticky-atc": r_sticky,
}

HARNESS_CSS = """
html,body{margin:0;padding:0;background:#fff}
.qa-banner{position:sticky;top:0;z-index:99;background:#1c1916;color:#fff;padding:10px 24px;
  font:600 12px/1.4 Roboto,sans-serif;letter-spacing:.14em;text-transform:uppercase;display:flex;
  justify-content:space-between;gap:16px}
.qa-banner span{color:#e0b9a8;letter-spacing:.06em;text-transform:none;font-weight:400}
/* Buy box uses real .pdp-hero / .pdp-buy / .pdp-buy__swatch from pdp-buy-box.liquid — do not override sizes. */
.qa-url{font:400 11px/1 Roboto,sans-serif;color:#b3aa9d;margin:18px 0 0}
.pdp-buy__accordions{border-top:1px solid #e8e2d8;margin-top:8px}
.qa-admin-flag{font:400 12px/1.55 Roboto,sans-serif!important;color:#8a6d3b!important;
  background:#fdf6e6;border-left:3px solid #d8b45a;padding:8px 10px;margin:10px 0 0!important}
/* Juicer stand-in — mirrors the v19 mock's blocked-feed mosaic so the block reads
   as the real section with filler pictures, never as a broken feed. */
/* Juicer fallback mosaic — REAL juicer.io Instagram media (SEO v37 pattern) */
.home-juicer.is-juicer-live .home-juicer__fallback{display:none!important}
.home-juicer__fallback{
  display:none;columns:3;column-gap:14px;text-align:left;margin:0 auto;max-width:1400px}
.home-juicer.is-fallback:not(.is-juicer-live) .home-juicer__feed{position:relative}
.home-juicer.is-fallback:not(.is-juicer-live) .home-juicer__fallback{
  display:block;position:absolute;left:0;right:0;top:0;z-index:2;background:#fff}
.home-juicer__fallback-card{
  break-inside:avoid;display:block;margin:0 0 12px;background:#f0ede8;
  border-radius:4px;overflow:hidden}
.home-juicer__fallback-card img{
  width:100%;height:auto;aspect-ratio:1;object-fit:cover;display:block}
.home-juicer__fallback-card:nth-child(3n) img{aspect-ratio:3/4}
.home-juicer__fallback-card:nth-child(3n+2) img{aspect-ratio:16/9}
.qa-sticky{position:static!important;transform:none!important;margin-top:0}
/* pdp-reviews — 3 curated photo cards + labelled Judge.me text stand-in */
.qa-rev{padding:var(--section-padding-y) var(--section-padding-x);border-top:1px solid #e8e2d8}
.qa-rev__inner{max-width:1200px;margin:0 auto}
.qa-rev__head{display:flex;align-items:flex-end;justify-content:space-between;
  flex-wrap:wrap;gap:20px;margin-bottom:32px}
.qa-rev__head h2{font:400 clamp(28px,3vw,40px)/1.15 Roboto,sans-serif;margin:0 0 8px;
  letter-spacing:-.02em;color:#1c1916}
.qa-rev__head p{font:400 15px/1.6 Roboto,sans-serif;color:#6b645a;margin:0;max-width:32ch}
.qa-rev__more{font:500 13px/1 Roboto,sans-serif;color:#1c1916;text-decoration:none}
.qa-rev__photo-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.qa-rev__photo-card{background:#fff;border-radius:8px;overflow:hidden;display:flex;flex-direction:column}
.qa-rev__photo-img{width:100%;aspect-ratio:1;object-fit:cover;display:block}
.qa-rev__photo-img--empty{background:#e8e2d8;display:flex;align-items:center;justify-content:center;
  color:#8a8a8a;font:600 12px/1 Roboto,sans-serif;letter-spacing:.06em;text-transform:uppercase}
.qa-rev__photo-pad{padding:22px 24px 24px;display:flex;flex-direction:column;gap:10px;flex:1}
.qa-rev__photo-stars{color:#c45c3f;font-size:14px;letter-spacing:.1em}
.qa-rev__photo-body{font:400 15px/1.55 Roboto,sans-serif;color:#4a4a4a;margin:0;flex:1}
.qa-rev__photo-author{display:block;font:500 13px/1.3 Roboto,sans-serif;color:#1c1916}
.qa-rev__photo-loc{display:block;font:400 12px/1.3 Roboto,sans-serif;color:#8a8a8a}
.qa-rev__community-label{font:400 11px/1 Roboto,sans-serif;text-transform:uppercase;
  letter-spacing:.08em;color:#8a8a8a;text-align:center;margin:48px 0 24px}
.qa-rev__standin{border:2px dashed #c9a227;background:#fffdf5;padding:22px;text-align:center}
.qa-rev__standin-flag{display:inline-block;margin:0 0 12px;padding:6px 12px;background:#f6e7b8;
  color:#8a6d3b;font:700 10px/1 Roboto,sans-serif;letter-spacing:.16em;text-transform:uppercase}
.qa-rev__standin-copy{margin:0 auto;max-width:70ch;font:400 13px/1.6 Roboto,sans-serif;color:#6b645a}
@media (max-width:768px){
  .qa-buy{grid-template-columns:1fr;gap:28px;
    padding:var(--space-8) var(--section-padding-x-mobile)}
  .qa-rev{padding:var(--section-padding-y-mobile) var(--section-padding-x-mobile)}
  .qa-rev__photo-grid{grid-template-columns:1fr;gap:16px}
  .qa-banner{padding:8px 14px;font-size:10px;flex-direction:column;gap:2px}
  .home-juicer__fallback{columns:2}
}
"""

SHELL = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}/design-tokens.css">
<link rel="stylesheet" href="{assets}/barreletics-base.css">
<style>{section_css}</style>
<style>{harness_css}</style>
</head><body>
<div class="qa-banner"><strong>{label}</strong><span>{template}</span></div>
{body}
</body></html>
"""


def build(page):
    slug, tpl, label, title, url, price, badge, badge_bg = page
    t = json.load(open(os.path.join(TEMPLATES, tpl)))
    body = []
    for key in t["order"]:
        s = t["sections"][key]
        fn = RENDERERS.get(s["type"])
        if fn:
            body.append(fn(s, page))
    return SHELL.format(title="%s — PDP variant QA" % label, assets=ASSETS,
                        section_css=collect_css(), harness_css=HARNESS_CSS,
                        label=label, template="shopify-build/templates/" + tpl,
                        body="\n".join(body))


# ----------------------------------------------------------------------- capture

HARNESS = ('<!doctype html><html><head><meta charset="utf-8">'
           '<style>html,body{{margin:0;padding:0;background:#fff}}'
           'iframe{{display:block;border:0;margin:0}}</style></head>'
           '<body><iframe width="{width}" height="{height}" src="{src}"></iframe></body></html>')


def run_chrome(args):
    return subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--allow-file-access-from-files", "--force-device-scale-factor=1"] + args,
        capture_output=True, text=True, timeout=420)


def shoot_desktop(path, out_png, width=1440, height=12000):
    run_chrome(["--window-size=%d,%d" % (width, height), "--virtual-time-budget=15000",
                "--screenshot=" + out_png, path])


def shoot_mobile(path, out_png, width=390, height=18000):
    harness = os.path.join(HERE, "__shot-harness.html")
    with open(harness, "w") as fh:
        fh.write(HARNESS.format(width=width, height=height, src=os.path.basename(path)))
    tmp = os.path.join(tempfile.gettempdir(), "pdpvar-raw.png")
    try:
        run_chrome(["--window-size=%d,%d" % (max(width + 120, 500), height),
                    "--virtual-time-budget=15000", "--screenshot=" + tmp, harness])
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


def compose(paths, out_png, gap=28, label_h=54):
    from PIL import Image, ImageDraw, ImageFont
    ims = [Image.open(p).convert("RGB") for p, _ in paths]
    h = max(i.height for i in ims)
    w = sum(i.width for i in ims) + gap * (len(ims) - 1)
    canvas = Image.new("RGB", (w, h + label_h), "#ffffff")
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)
    except Exception:
        font = ImageFont.load_default()
    d = ImageDraw.Draw(canvas)
    x = 0
    for im, (_, name) in zip(ims, paths):
        d.text((x + 14, 14), name, fill="#1c1916", font=font)
        canvas.paste(im, (x, label_h))
        x += im.width + gap
    canvas.save(out_png)
    return out_png


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-shots", action="store_true")
    a = ap.parse_args()

    made = {}
    for page in PAGES:
        slug = page[0]
        path = os.path.join(HERE, "preview-%s.html" % slug)
        with open(path, "w") as fh:
            fh.write(build(page))
        made[slug] = path
        print("built %s" % os.path.relpath(path, REPO))

    if a.no_shots:
        return

    for width, tag, shooter in ((1440, "1440", shoot_desktop), (390, "390", shoot_mobile)):
        shots = []
        for page in PAGES:
            slug, _, label = page[0], page[1], page[2]
            out = os.path.join(HERE, "%s-%s.png" % (slug, tag))
            shooter(made[slug], out)
            print("  shot %s" % os.path.basename(out))
            shots.append((out, label))
        combo = os.path.join(HERE, "SIDE-BY-SIDE-%spx.png" % tag)
        compose(shots, combo)
        print("composed %s" % os.path.basename(combo))


if __name__ == "__main__":
    main()
