#!/usr/bin/env python3
"""
Sticky / fixed behaviour probe for the shipping theme (shopify-build/).

Renders a fixture that reproduces the DOM Shopify actually emits for a PDP —
section-group wrappers included — loads the real theme CSS, scrolls the document,
and measures whether the sticky header and the fixed sticky-ATC bar hold position.

Reuses the iframe technique from mqa.py: headless Chrome on macOS clamps windows to
500px, so a 390px iframe inside a 500px window is the only way to get a true 390px
viewport. The harness asserts the measured viewport width and fails loudly otherwise.

Usage:
    python3 planning/mobile-qa/sticky-probe.py            # 390px + 1280px
    python3 planning/mobile-qa/sticky-probe.py --width 390
"""

import argparse
import json
import os
import re
import subprocess

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTDIR = os.path.join(REPO, "planning", "mobile-qa")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ASSETS = "../../shopify-build/assets"


def liquid_css(relpath, section_id):
    """Pull the <style> blocks out of a .liquid file and resolve them to plain CSS."""
    with open(os.path.join(REPO, "shopify-build", relpath)) as fh:
        src = fh.read()
    css = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    css = css.replace("{{ section.id }}", section_id)
    css = re.sub(r"\{%-?.*?-?%\}", "", css, flags=re.S)   # {% if %} etc.
    css = re.sub(r"\{\{.*?\}\}", "0", css, flags=re.S)     # leftover settings values
    return css


def filler(n, label):
    return "\n".join(
        '<div style="padding:40px 16px;border-bottom:1px solid #eee">%s block %d</div>' % (label, i)
        for i in range(n)
    )


# Mirrors layout/theme.liquid + sections/header-group.json + templates/product.json.
# Shopify wraps every section in <div id="shopify-section-…" class="shopify-section …">,
# and section-group members additionally get .shopify-section-group-<group>.
FIXTURE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{assets}/design-tokens.css">
<link rel="stylesheet" href="{assets}/barreletics-base.css">
<link rel="stylesheet" href="{assets}/chrome.css">
<style>{extra}</style>
</head>
<body class="template-product">
<a href="#main-content" class="skip-link">Skip to content</a>

{header}

<main id="main-content" role="main">
  <div id="shopify-section-pdp-buy-box" class="shopify-section">
    <section id="buy" class="pdp-hero" data-buy-box>
      <div class="pdp-gallery">
        <div class="pdp-gallery__hero" style="background:#ddd"></div>
        <div class="pdp-gallery__thumbs">
          <button class="pdp-gallery__thumb"></button>
          <button class="pdp-gallery__thumb"></button>
          <button class="pdp-gallery__thumb"></button>
          <button class="pdp-gallery__thumb"></button>
        </div>
      </div>
      <div class="pdp-buy">{buyfill}</div>
    </section>
  </div>
  <div id="shopify-section-body" class="shopify-section">{bodyfill}</div>
  <div id="shopify-section-pdp-sticky-atc" class="shopify-section">
    <div id="sticky-atc" class="sticky-atc is-visible" aria-hidden="false">
      <div class="sticky-atc__inner">
        <div class="sticky-atc__product"><span class="sticky-atc__title">Product</span></div>
        <div class="sticky-atc__actions"><button class="sticky-atc__btn">Add to Cart</button></div>
      </div>
    </div>
  </div>
</main>

<div id="shopify-section-footer" class="shopify-section shopify-section-group-footer-group">
  <footer class="site-footer"><div class="site-footer__body">footer</div></footer>
</div>
</body></html>
"""

HEADER_WRAPPED = """<div id="shopify-section-sections--main__announcement_strip" class="shopify-section shopify-section-group-header-group announcement-strip-section">
  <div class="announcement-strip"><div class="announcement-strip__inner">
    <span class="announcement-strip__item">Free Shipping Over $150</span>
  </div></div>
</div>
<div id="shopify-section-sections--main__header" class="shopify-section shopify-section-group-header-group header-section">
  <header class="site-header" data-site-header role="banner">
    <div class="site-header__inner">
      <a href="#" class="site-header__logo"><span class="site-header__logo-text">Barreletics</span></a>
      <div class="site-header__actions"><a href="#" class="site-header__action--text">Cart</a></div>
    </div>
  </header>
</div>"""

# Control: same header with no section wrapper, i.e. a direct child of body.
HEADER_BARE = re.sub(
    r'<div id="shopify-section-sections--main__header"[^>]*>\s*(.*?)\s*</div>\s*$',
    r"\1",
    HEADER_WRAPPED,
    flags=re.S,
)

PROBE = r"""
function probe(doc, win) {
  var out = { vw: doc.documentElement.clientWidth, vh: doc.documentElement.clientHeight };
  var header = doc.querySelector('.site-header');
  var atc = doc.querySelector('.sticky-atc');
  var gallery = doc.querySelector('.pdp-gallery');

  function boxes() {
    return {
      scrollY: Math.round(win.scrollY),
      headerTop: header ? Math.round(header.getBoundingClientRect().top) : null,
      atcBottom: atc ? Math.round(atc.getBoundingClientRect().bottom) : null,
      galleryTop: gallery ? Math.round(gallery.getBoundingClientRect().top) : null
    };
  }

  out.headerPos = header ? win.getComputedStyle(header).position : null;
  out.atcPos = atc ? win.getComputedStyle(atc).position : null;
  out.galleryPos = gallery ? win.getComputedStyle(gallery).position : null;
  out.htmlOverflowX = win.getComputedStyle(doc.documentElement).overflowX;
  out.bodyOverflowX = win.getComputedStyle(doc.body).overflowX;
  out.docHeight = doc.documentElement.scrollHeight;

  // Walk sticky/fixed ancestors and record anything that would break containment.
  function chain(el) {
    var rows = [], p = el ? el.parentElement : null;
    while (p) {
      var cs = win.getComputedStyle(p);
      var bad = [];
      if (/(hidden|auto|scroll)/.test(cs.overflowX + ' ' + cs.overflowY)) bad.push('overflow:' + cs.overflowX + '/' + cs.overflowY);
      if (cs.transform !== 'none') bad.push('transform');
      if (cs.filter !== 'none') bad.push('filter');
      if (cs.perspective !== 'none') bad.push('perspective');
      if (cs.willChange !== 'auto') bad.push('will-change:' + cs.willChange);
      if (cs.contain !== 'none' && cs.contain !== '') bad.push('contain:' + cs.contain);
      var r = p.getBoundingClientRect();
      rows.push({
        sel: p.tagName.toLowerCase() + (p.id ? '#' + p.id : '') +
             (p.className && p.className.split ? '.' + p.className.split(/\s+/).filter(Boolean).slice(0,2).join('.') : ''),
        h: Math.round(r.height),
        breakers: bad
      });
      p = p.parentElement;
    }
    return rows;
  }
  out.headerAncestors = header ? chain(header) : [];
  out.atcAncestors = atc ? chain(atc) : [];

  // barreletics-base.css sets html { scroll-behavior: smooth }, which makes scrollTo
  // async and silently returns scrollY=0 to a synchronous probe. Force instant.
  var prevBehavior = doc.documentElement.style.scrollBehavior;
  doc.documentElement.style.scrollBehavior = 'auto';

  out.atRest = boxes();
  win.scrollTo(0, 1500);
  out.at1500 = boxes();
  win.scrollTo(0, 3000);
  out.at3000 = boxes();
  win.scrollTo(0, out.docHeight);
  out.atBottom = boxes();
  win.scrollTo(0, 0);

  doc.documentElement.style.scrollBehavior = prevBehavior;
  return out;
}
"""

HARNESS = """<!doctype html>
<html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0}}iframe{{display:block;border:0}}</style></head>
<body><iframe id="f" width="{w}" height="{h}" src="{src}"></iframe>
<script>
{probe}
window.addEventListener('load', function () {{
  setTimeout(function () {{
    var s = document.createElement('script');
    s.type = 'application/json'; s.id = 'result';
    var f = document.getElementById('f');
    var o;
    try {{ o = probe(f.contentDocument, f.contentWindow); }} catch (e) {{ o = {{ error: String(e) }}; }}
    s.textContent = JSON.stringify(o).replace(/</g, '\\\\u003c');
    document.body.appendChild(s);
  }}, 600);
}});
</script></body></html>
"""


def run(width, height, variant, extra_css):
    header = HEADER_BARE if variant.startswith("bare") else HEADER_WRAPPED
    section_css = (liquid_css("snippets/sticky-atc.liquid", "pdp-sticky-atc")
                   + "\n" + liquid_css("sections/pdp-buy-box.liquid", "pdp-buy-box")
                   + "\n" + extra_css)
    fx = os.path.join(OUTDIR, "__fixture-%s.html" % variant)
    with open(fx, "w") as fh:
        fh.write(FIXTURE.format(assets=ASSETS, header=header, extra=section_css,
                                buyfill=filler(12, "buy"), bodyfill=filler(40, "page")))
    hn = os.path.join(OUTDIR, "__harness-%s.html" % variant)
    with open(hn, "w") as fh:
        fh.write(HARNESS.format(w=width, h=height, src=os.path.basename(fx), probe=PROBE))
    try:
        r = subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             "--allow-file-access-from-files", "--force-device-scale-factor=1",
             "--window-size=%d,%d" % (max(width + 110, 500), height + 40),
             "--virtual-time-budget=6000", "--dump-dom", hn],
            capture_output=True, text=True, timeout=180)
        m = re.search(r'<script type="application/json" id="result">(.*?)</script>', r.stdout, re.S)
        if not m:
            return {"error": "no payload", "stderr": r.stderr[-600:]}
        return json.loads(m.group(1).replace("\\u003c", "<"))
    finally:
        for f in (fx, hn):
            if os.path.exists(f):
                os.remove(f)


def report(name, res, want_width):
    print("\n=== %s ===" % name)
    if res.get("error"):
        print("  ERROR", res["error"], res.get("stderr", ""))
        return
    vw = res["vw"]
    flag = "OK" if vw == want_width else "HARNESS BROKEN — NOT A REAL VIEWPORT"
    print("  viewport %dx%d  [%s]   doc height %d" % (vw, res["vh"], flag, res["docHeight"]))
    print("  html overflow-x=%s   body overflow-x=%s" % (res["htmlOverflowX"], res["bodyOverflowX"]))
    print("  computed position: header=%s  sticky-atc=%s  pdp-gallery=%s"
          % (res["headerPos"], res["atcPos"], res["galleryPos"]))
    for k in ("atRest", "at1500", "at3000", "atBottom"):
        b = res[k]
        print("   scrollY=%-5d headerTop=%-7s atcBottom=%-7s galleryTop=%s"
              % (b["scrollY"], b["headerTop"], b["atcBottom"], b["galleryTop"]))
    for label, rows in (("header", res["headerAncestors"]), ("sticky-atc", res["atcAncestors"])):
        print("  %s ancestors:" % label)
        for r in rows:
            print("    %-62s h=%-6d %s" % (r["sel"][:62], r["h"], ",".join(r["breakers"]) or "-"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=None)
    a = ap.parse_args()
    widths = [a.width] if a.width else [390, 1280]
    results = {}
    for w in widths:
        h = 844 if w < 900 else 900
        for variant, css in (("wrapped", ""), ("bare", "")):
            key = "%s@%dpx" % (variant, w)
            res = run(w, h, "%s-%d" % (variant, w), css)
            results[key] = res
            report(key, res, w)
        # Reproduce the FAQ-mock defect on purpose to validate the probe detects it.
        key = "wrapped+overflowhidden@%dpx" % w
        res = run(w, h, "ovh-%d" % w, "html,body{overflow-x:hidden}")
        results[key] = res
        report(key, res, w)
        # TE "Sticky header" unchecked — header.liquid scopes the wrapper back to static.
        key = "stickyOffToggle@%dpx" % w
        res = run(w, h, "toggleoff-%d" % w,
                  "#shopify-section-sections--main__header{position:static}"
                  ".site-header--static{position:relative}")
        results[key] = res
        report(key, res, w)
    with open(os.path.join(OUTDIR, "sticky-probe-results.json"), "w") as fh:
        json.dump(results, fh, indent=1)


if __name__ == "__main__":
    main()
