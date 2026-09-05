#!/usr/bin/env python3
"""Apply SETTLED Type OS (hero max 72) across authority docs mocks."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

TYPE_OS_ROOT = """
    /* === TYPE OS SETTLED 2026-07-29 — single source (see planning/m4-type-hierarchy.md) === */
    :root {
      --fw-hero: 700;
      --fw-h2-display: 500;
      --fw-h2-standard: 600;
      --fw-statement: 500;
      --fw-body: 400;
      --fw-label: 600;
      --fw-emphasis: 700;
      --fs-hero: clamp(50px, 6.4vw, 72px);
      --fs-hero-mobile: clamp(38px, 9vw, 50px);
      --fs-h2-display: clamp(38px, 4.6vw, 52px);
      --fs-h2-display-mobile: clamp(32px, 7vw, 40px);
      --fs-h2-standard: clamp(26px, 2.9vw, 32px);
      --fs-h2-standard-mobile: clamp(24px, 5vw, 28px);
      --fs-statement: clamp(28px, 3vw, 36px);
      --fs-statement-mobile: clamp(24px, 5.5vw, 30px);
      --fs-lede: 17px;
      --fs-body: 16px;
      --fs-label: 11px;
      --ls-hero: -0.028em;
      --ls-h2-display: -0.028em;
      --ls-h2-standard: -0.012em;
      --ls-statement: -0.022em;
      --ls-label: 0.08em;
      --lh-hero: 1.06;
      --lh-h2-display: 1.10;
      --lh-h2-standard: 1.22;
      --lh-lede: 1.60;
      --lh-body: 1.72;
      --gap-a: 16px;
      --gap-b: 20px;
      --gap-c: 32px;
    }
    .em { font-weight: var(--fw-emphasis); }
"""

# Authority mocks (current) — not historical priors
AUTHORITY = [
    "Barreletics Home - Definitive-WORKING.html",
    "Barreletics Collection - Definitive-v18.html",
    "Barreletics SEO - Best Grippy Socks - Definitive-v36.html",
    "Barreletics PDP - Definitive-v16.html",
    "Barreletics Journal - Definitive-v5.html",
    "Barreletics Help - Definitive-v3.html",
    "Barreletics Hero - Centered Fullbleed - Pattern-v2.html",
    "Barreletics FAQ - Definitive-v4.html",
    "Barreletics Contact - Definitive-v1.html",
    "Barreletics Returns - Definitive-v3.html",
    "Barreletics Size Chart - Definitive-v1.html",
    "Barreletics Track Order - Definitive-v1.html",
    "Barreletics Returns Portal - Definitive-v1.html",
]

# Common hero title patterns → Type OS hero
HERO_REPLACEMENTS = [
    (
        r"font-size:\s*clamp\(40px,\s*6vw,\s*64px\);\s*font-weight:\s*400;\s*line-height:\s*1\.08(?:;?\s*letter-spacing:\s*-0\.03em)?",
        "font-size: var(--fs-hero); font-weight: var(--fw-hero); line-height: var(--lh-hero); letter-spacing: var(--ls-hero)",
    ),
    (
        r"font-size:\s*clamp\(40px,\s*6vw,\s*64px\);\s*font-weight:\s*400;\s*line-height:\s*1\.08",
        "font-size: var(--fs-hero); font-weight: var(--fw-hero); line-height: var(--lh-hero); letter-spacing: var(--ls-hero)",
    ),
    (
        r"font-size:\s*clamp\(40px,\s*6vw,\s*64px\)",
        "font-size: var(--fs-hero)",
    ),
]

FONT_LINK_OLD = re.compile(
    r"family=Roboto:wght@[^\"'&]+",
)
FONT_LINK_NEW = "family=Roboto:wght@400;500;600;700"


def ensure_root_tokens(css_or_html: str) -> str:
    if "--fs-hero: clamp(50px, 6.4vw, 72px)" in css_or_html and "TYPE OS SETTLED" in css_or_html:
        return css_or_html
    if "--fs-hero: clamp(50px, 6.4vw, 72px)" in css_or_html:
        # Preview already has tokens; stamp SETTLED comment if missing
        return css_or_html.replace(
            "/* weight falls as size rises */",
            "/* TYPE OS SETTLED 2026-07-29 — weight falls as size rises */",
            1,
        )
    # Insert after first <style> or after body rule block start
    m = re.search(r"(<style[^>]*>\s*)", css_or_html, re.I)
    if not m:
        return css_or_html
    return css_or_html[: m.end()] + TYPE_OS_ROOT + css_or_html[m.end() :]


def patch_home_working(text: str) -> str:
    """Home WORKING — map roles per Type OS audit."""
    text = ensure_root_tokens(text)
    text = FONT_LINK_OLD.sub(FONT_LINK_NEW, text)

    # Display group: was 400 → split registers
    text = text.replace(
        """    /* Display — same Roboto family; precision via weight/tracking/size (not a second face). Opening .hero__title = BZ-020 locked 64/400. */
    .vm-tile--hero .vm-tile__title,
    .discipline-film__line,
    .variants-head__title,
    .split-text h2,
    .statement-band__line,
    .fullbleed__statement,
    .problem-title,
    .guarantee-head__title,
    .reviews-section h2,
    .ig-section h2,
    .fn-signup h2,
    .anti-slip__inner h2,
    .hot-kits__text h2,
    .inset-tile__copy h2,
    .studio-trust__line {
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
      font-weight: 400;
      letter-spacing: -0.028em;
      line-height: 1.15;
    }
    /* Display stays 400 (BZ-020 calm — live vibe; 700 = CTAs only) */
    .statement-band__line,
    .fullbleed__statement,
    .problem-title {
      font-weight: 400;
      letter-spacing: -0.03em;
      line-height: 1.12;
    }""",
        """    /* TYPE OS SETTLED — role classes (weight falls as size rises) */
    .h2-display, .problem-title, .split-text h2.h2-display {
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: var(--fs-h2-display);
      font-weight: var(--fw-h2-display);
      letter-spacing: var(--ls-h2-display);
      line-height: var(--lh-h2-display);
      text-transform: none;
    }
    .h2-standard,
    .variants-head__title,
    .reviews-head__title,
    .ig-head__title,
    .fn-signup h2,
    .reviews-section h2,
    .ig-section h2 {
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: var(--fs-h2-standard);
      font-weight: var(--fw-h2-standard);
      letter-spacing: var(--ls-h2-standard);
      line-height: var(--lh-h2-standard);
      text-transform: none;
    }
    .type-statement,
    .statement-band__line,
    .fullbleed__statement,
    .guarantee-head__title {
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: var(--fs-statement);
      font-weight: var(--fw-statement);
      letter-spacing: var(--ls-statement);
      line-height: var(--lh-h2-display);
      text-transform: none;
    }
    .discipline-film__line {
      font-size: var(--fs-label);
      font-weight: var(--fw-label);
      letter-spacing: var(--ls-label);
      text-transform: uppercase;
      color: #6b645a;
      line-height: 1.4;
    }""",
    )

    text = re.sub(
        r"\.hero__title \{\s*font-family:[^}]+?\}",
        """.hero__title {
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: var(--fs-hero); font-weight: var(--fw-hero); line-height: var(--lh-hero);
      color: #1c1916; margin: 0 0 var(--gap-b); letter-spacing: var(--ls-hero);
      text-transform: none;
    }""",
        text,
        count=1,
        flags=re.S,
    )

    text = text.replace(
        ".hero__body {\n      font-size: 17px; font-weight: 400; color: #4a4a4a; line-height: 1.45;\n      margin: 0 0 32px; max-width: 28ch;\n    }",
        ".hero__body {\n      font-size: var(--fs-lede); font-weight: var(--fw-body); color: #4a4a4a; line-height: var(--lh-lede);\n      margin: 0 0 var(--gap-c); max-width: 28ch;\n    }",
    )

    # Specific size overrides that fight OS
    replacements = {
        ".problem-title { font-size: clamp(28px, 3.5vw, 40px); font-weight: 400; line-height: 1.12; color: #1c1916; margin: 0 0 20px; letter-spacing: -0.03em; }":
            ".problem-title { font-size: var(--fs-h2-display); font-weight: var(--fw-h2-display); line-height: var(--lh-h2-display); color: #1c1916; margin: 0 0 var(--gap-b); letter-spacing: var(--ls-h2-display); }",
        ".problem-body { font-size: 16px; color: #4a4a4a; line-height: 1.65; margin: 0; max-width: 38ch; }":
            ".problem-body { font-size: var(--fs-body); color: #4a4a4a; line-height: var(--lh-body); margin: 0; max-width: 38ch; }",
        ".discipline-film__line {\n      font-size: clamp(28px, 3.5vw, 40px); font-weight: 400; color: #1c1916;\n      letter-spacing: -0.028em; line-height: 1.15; margin: 0 0 32px;\n    }":
            ".discipline-film__line {\n      font-size: var(--fs-label); font-weight: var(--fw-label); color: #6b645a;\n      letter-spacing: var(--ls-label); text-transform: uppercase; line-height: 1.4; margin: 0 0 var(--gap-b);\n    }",
        ".variants-head__title { font-size: clamp(28px, 3.2vw, 36px); font-weight: 400; line-height: 1.15; color: #1c1916; margin: 0 0 16px; letter-spacing: -0.028em; }":
            ".variants-head__title { font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard); line-height: var(--lh-h2-standard); color: #1c1916; margin: 0 0 var(--gap-b); letter-spacing: var(--ls-h2-standard); }",
        ".variants-head__eyebrow { font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #c45c3f; font-weight: 700; margin: 0 0 12px; }":
            ".variants-head__eyebrow { font-size: var(--fs-label); text-transform: uppercase; letter-spacing: var(--ls-label); color: #6b645a; font-weight: var(--fw-label); margin: 0 0 var(--gap-a); }",
        ".split-text h2 { font-size: clamp(28px, 3.2vw, 36px); font-weight: 400; line-height: 1.15; color: #1c1916; margin: 0 0 20px; letter-spacing: -0.028em; }":
            ".split-text h2 { font-size: var(--fs-h2-display); font-weight: var(--fw-h2-display); line-height: var(--lh-h2-display); color: #1c1916; margin: 0 0 var(--gap-b); letter-spacing: var(--ls-h2-display); }\n    .split-text h2.h2-standard { font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard); line-height: var(--lh-h2-standard); letter-spacing: var(--ls-h2-standard); }",
        ".fullbleed__statement { font-size: clamp(28px, 3.5vw, 40px); font-weight: 400; color: #fff; text-shadow: 0 2px 24px rgba(0,0,0,0.3); margin: 0 0 32px; line-height: 1.12; letter-spacing: -0.03em; }":
            ".fullbleed__statement { font-size: var(--fs-statement); font-weight: var(--fw-statement); color: #fff; text-shadow: 0 2px 24px rgba(0,0,0,0.3); margin: 0 0 var(--gap-b); line-height: var(--lh-h2-display); letter-spacing: var(--ls-statement); }",
        ".reviews-head__title { font-size: clamp(28px, 3.5vw, 40px); font-weight: 400; color: #1c1916; letter-spacing: -0.028em; margin: 0 0 16px; line-height: 1.15; }":
            ".reviews-head__title { font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard); color: #1c1916; letter-spacing: var(--ls-h2-standard); margin: 0 0 var(--gap-b); line-height: var(--lh-h2-standard); }",
        ".ig-head__title { font-size: clamp(28px, 3.5vw, 40px); font-weight: 400; color: #1c1916; margin: 0 0 12px; letter-spacing: -0.028em; line-height: 1.15; }":
            ".ig-head__title { font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard); color: #1c1916; margin: 0 0 var(--gap-b); letter-spacing: var(--ls-h2-standard); line-height: var(--lh-h2-standard); }",
        ".guarantee-head__title { font-size: clamp(26px, 3vw, 34px); font-weight: 400; color: #1c1916; margin: 0 0 16px; letter-spacing: -0.028em; line-height: 1.15; }":
            ".guarantee-head__title { font-size: var(--fs-statement); font-weight: var(--fw-statement); color: #1c1916; margin: 0 0 var(--gap-b); letter-spacing: var(--ls-statement); line-height: var(--lh-h2-display); }",
        ".fn-signup h2 { font-size: clamp(22px, 2.5vw, 28px); font-weight: 400; color: #1c1916; margin: 0 0 12px; letter-spacing: -0.02em; line-height: 1.15; }":
            ".fn-signup h2 { font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard); color: #1c1916; margin: 0 0 var(--gap-b); letter-spacing: var(--ls-h2-standard); line-height: var(--lh-h2-standard); }",
        ".site-nav__links a { font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.12em; color: #4a4a4a; text-decoration: none; }":
            ".site-nav__links a { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: #4a4a4a; text-decoration: none; }",
        "body {\n      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;\n      font-weight: 400; color: #1c1916; background: #fff;\n      line-height: 1.6; -webkit-font-smoothing: antialiased; overflow-x: hidden;\n    }":
            "body {\n      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;\n      font-weight: 400; font-size: var(--fs-body); color: #1c1916; background: #fff;\n      line-height: var(--lh-body); -webkit-font-smoothing: antialiased; overflow-x: hidden;\n    }",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Mobile hero
    text = text.replace(
        ".hero__title { font-size: clamp(34px, 9vw, 44px); margin-bottom: 16px; }",
        ".hero__title { font-size: var(--fs-hero-mobile); margin-bottom: var(--gap-b); }",
    )
    text = text.replace(
        ".hero__title { font-size: clamp(34px, 9vw, 44px); }",
        ".hero__title { font-size: var(--fs-hero-mobile); }",
    )

    # HTML class wiring for display/standard
    text = text.replace(
        '<h2 class="problem-title">',
        '<h2 class="problem-title h2-display">',
    )
    # Coperni stays standard (named campaign / navigate) — class on split if present
    text = text.replace(
        '<h2 class="reviews-head__title">',
        '<h2 class="reviews-head__title h2-standard">',
    )
    text = text.replace(
        '<h2 class="variants-head__title">',
        '<h2 class="variants-head__title h2-standard">',
    )
    text = text.replace(
        '<h2 class="ig-head__title">',
        '<h2 class="ig-head__title h2-standard">',
    )
    text = text.replace(
        '<h2 class="guarantee-head__title">',
        '<h2 class="guarantee-head__title type-statement">',
    )
    text = text.replace(
        '<h1 class="hero__title">',
        '<h1 class="hero__title type-hero">',
    )

    # Title note
    text = text.replace(
        "<title>Barreletics Home — WORKING (v29)</title>",
        "<title>Barreletics Home — WORKING · Type OS SETTLED</title>",
    )
    return text


def patch_generic_authority(text: str, name: str) -> str:
    text = ensure_root_tokens(text)
    text = FONT_LINK_OLD.sub(FONT_LINK_NEW, text)
    for pat, repl in HERO_REPLACEMENTS:
        text = re.sub(pat, repl, text)

    # Common mid-page clamps → standard/display heuristics
    text = re.sub(
        r"font-size:\s*clamp\(28px,\s*3\.5vw,\s*40px\);\s*font-weight:\s*400",
        "font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard)",
        text,
    )
    text = re.sub(
        r"font-size:\s*clamp\(28px,\s*3\.2vw,\s*36px\);\s*font-weight:\s*400",
        "font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard)",
        text,
    )
    text = re.sub(
        r"font-size:\s*clamp\(26px,\s*3vw,\s*34px\);\s*font-weight:\s*400",
        "font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard)",
        text,
    )
    text = re.sub(
        r"font-size:\s*clamp\(22px,\s*2\.5vw,\s*28px\);\s*font-weight:\s*400",
        "font-size: var(--fs-h2-standard); font-weight: var(--fw-h2-standard)",
        text,
    )

    # Body / lede breathe
    text = re.sub(
        r"line-height:\s*1\.65\b",
        "line-height: var(--lh-body)",
        text,
    )
    text = re.sub(
        r"(font-size:\s*17px[^;]*;\s*[^}]{0,80}?line-height:\s*)1\.45",
        r"\g<1>var(--lh-lede)",
        text,
    )

    # Eyebrow labels → 11/600/0.08em where still 700+0.1em rust labels (keep color)
    text = re.sub(
        r"font-size:\s*11px;\s*text-transform:\s*uppercase;\s*letter-spacing:\s*0\.1(?:0|2|4)?em;\s*[^;]*font-weight:\s*700",
        "font-size: var(--fs-label); text-transform: uppercase; letter-spacing: var(--ls-label); font-weight: var(--fw-label)",
        text,
    )

    # Mobile hero old → settled mobile
    text = text.replace(
        "font-size: clamp(34px, 9vw, 44px)",
        "font-size: var(--fs-hero-mobile)",
    )

    # Pattern-v2 locked note
    if "Pattern-v2" in name:
        text = text.replace(
            "LOCKED opening H1: <code>clamp(40px, 6vw, 64px)</code> / <strong>400</strong>",
            "LOCKED opening H1: <code>clamp(50px, 6.4vw, 72px)</code> / <strong>700</strong> (Type OS SETTLED)",
        )
        text = text.replace(
            "mid-page sentence case 400",
            "mid-page H2 Display 500 / Standard 600",
        )

    return text


def patch_preview(text: str) -> str:
    text = text.replace(
        "<title>Barreletics Home — TYPE OS PREVIEW v2 (elasticity &amp; weight inversion)</title>",
        "<title>Barreletics Home — TYPE OS SETTLED (preview)</title>",
    )
    text = text.replace(
        "TYPE OS PREVIEW · Not Shopify · Not WORKING mock",
        "TYPE OS SETTLED · Not Shopify · Review surface",
    )
    text = text.replace(
        "Tokens from <code>design-tokens.css</code> (v2).",
        "Tokens from <code>design-tokens.css</code> — SETTLED 2026-07-29 (hero max 72).",
    )
    text = text.replace(
        "TYPE OS v2 PREVIEW — static HTML for htmlpreview.github.io",
        "TYPE OS SETTLED — static HTML for htmlpreview.github.io",
    )
    return text


def patch_hub(text: str) -> str:
    text = text.replace(
        "<strong>Type (BZ-020 FINAL)</strong> — Opening H1 <strong>~64 / 400</strong> · mid-page ~28–40 / 400 · CTAs <strong>700 ALL CAPS</strong>. Authorities: Home WORKING · SEO v36 · Pattern-v2 · Collection v18 · PDP v16 · Journal v5 · Help v3.",
        "<strong>Type OS SETTLED 2026-07-29</strong> — Hero <code>clamp(50px, 6.4vw, 72px)</code> / <strong>700</strong> · H2 Display <strong>500</strong> · H2 Standard <strong>600</strong> · Statement <strong>500</strong> · gaps a/b/c · body 16/1.72 · lede 17/1.60 · labels 11/600/0.08em. Review: <strong>Type OS Preview</strong>. Authorities: Home WORKING · SEO v36 · Pattern-v2 · Collection v18 · PDP v16 · Journal v5 · Help v3.",
    )
    text = text.replace(
        "<strong>Casing (BZ-024)</strong> — Opening H1 = <strong>v6 title case</strong> (major words only; short words like <em>is / in / the</em> stay lower). Elsewhere = sentence case. Ex: <em>The Pilates Sock Era is Over</em> · <em>Secure in Every Hold</em>.",
        "<strong>Casing</strong> — Sentence case headings; uppercase labels/CTAs/nav only. No ALL CAPS campaigns. Ex: <em>The Pilates Sock Era is Over</em>.",
    )
    text = text.replace("~64 / 400 · v6 title case", "Type OS hero 72/700")
    text = text.replace("Locked balance · 64/400 open", "Type OS SETTLED")
    text = text.replace("Shop-first · 64/400 open", "Shop-first · Type OS SETTLED")
    text = text.replace("Buy box · 64/400 name", "Buy box · Type OS SETTLED")
    text = text.replace("64/400 · Era is Over (v6 case)", "Type OS SETTLED · Era is Over")
    text = text.replace("same BZ-020 tokens", "Type OS SETTLED tokens")

    # Ensure Type OS Preview is first / featured
    if "Type OS Preview" not in text and "Type OS Preview.html" not in text:
        card = (
            '    <a class="card" href="Barreletics%20Home%20-%20Type%20OS%20Preview.html">'
            '<span class="tag">SETTLED</span><strong>Type OS Preview</strong>'
            "<span>Primary review surface · hero 72/700 · Display/Standard</span></a>\n"
        )
        text = text.replace("<section>\n    <h2>Patterns</h2>\n", "<section>\n    <h2>Type OS</h2>\n" + card + "  </section>\n\n  <section>\n    <h2>Patterns</h2>\n")
    elif "TYPE OS" not in text.upper() or "Type OS Preview" not in text:
        pass
    else:
        # Promote existing card tag
        text = re.sub(
            r'(href="Barreletics%20Home%20-%20Type%20OS%20Preview\.html"[^>]*>.*?<span class="tag">)[^<]+',
            r"\1SETTLED",
            text,
            count=1,
            flags=re.S,
        )

    if 'href="Barreletics%20Home%20-%20Type%20OS%20Preview.html"' not in text:
        card = (
            '    <a class="card" href="Barreletics%20Home%20-%20Type%20OS%20Preview.html">'
            '<span class="tag">SETTLED</span><strong>Type OS Preview</strong>'
            "<span>Primary review surface · hero 72/700 · Display/Standard</span></a>\n"
        )
        text = text.replace("<section>\n    <h2>Patterns</h2>\n", "<section>\n    <h2>Type OS</h2>\n" + card + "  </section>\n\n  <section>\n    <h2>Patterns</h2>\n")
    return text


def main() -> None:
    updated = []
    for name in AUTHORITY:
        path = DOCS / name
        if not path.exists():
            print(f"SKIP missing {name}")
            continue
        original = path.read_text(encoding="utf-8")
        if name == "Barreletics Home - Definitive-WORKING.html":
            text = patch_home_working(original)
        else:
            text = patch_generic_authority(original, name)
        if text != original:
            path.write_text(text, encoding="utf-8")
            updated.append(name)
            print(f"OK {name}")
        else:
            print(f"NOCHANGE {name}")

    preview = DOCS / "Barreletics Home - Type OS Preview.html"
    if preview.exists():
        t0 = preview.read_text(encoding="utf-8")
        t1 = patch_preview(t0)
        if t1 != t0:
            preview.write_text(t1, encoding="utf-8")
            updated.append(preview.name)
            print(f"OK {preview.name}")

    for hub in ("PREVIEW-HUB.html", "index.html"):
        path = DOCS / hub
        if path.exists():
            t0 = path.read_text(encoding="utf-8")
            t1 = patch_hub(t0)
            if t1 != t0:
                path.write_text(t1, encoding="utf-8")
                updated.append(hub)
                print(f"OK {hub}")

    print(f"\nUpdated {len(updated)} files")


if __name__ == "__main__":
    main()
