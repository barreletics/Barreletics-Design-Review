#!/usr/bin/env python3
"""Wire SETTLED Type OS tokens into Shopify section heading CSS/markup."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "shopify-build" / "sections"

# Page H1 title selectors → type-hero tokens
HERO_TITLE_CSS = """
    font-size: var(--type-hero-size);
    font-weight: var(--type-hero-weight);
    line-height: var(--type-hero-leading);
    letter-spacing: var(--type-hero-tracking);
    text-transform: none;
""".strip()

SECTION_TITLE_CSS = """
    font-size: var(--type-section-size);
    font-weight: var(--type-section-weight);
    line-height: var(--type-section-leading);
    letter-spacing: var(--type-section-tracking);
    text-transform: none;
""".strip()

DISPLAY_TITLE_CSS = """
    font-size: var(--type-h2-display-size);
    font-weight: var(--type-h2-display-weight);
    line-height: var(--type-h2-display-leading);
    letter-spacing: var(--type-h2-display-tracking);
    text-transform: none;
""".strip()


def replace_block_props(text: str, selector: str, props: str) -> str:
    """Replace font-size/weight/line-height/letter-spacing inside a CSS rule for selector."""
    pattern = re.compile(
        rf"({re.escape(selector)}\s*\{{)([^}}]*)(\}})",
        re.M,
    )

    def repl(m: re.Match) -> str:
        body = m.group(2)
        # strip old type props
        body = re.sub(r"\s*font-size:[^;]+;", "", body)
        body = re.sub(r"\s*font-weight:[^;]+;", "", body)
        body = re.sub(r"\s*line-height:[^;]+;", "", body)
        body = re.sub(r"\s*letter-spacing:[^;]+;", "", body)
        body = re.sub(r"\s*text-transform:[^;]+;", "", body)
        indent = "    "
        injected = "\n" + "\n".join(indent + line for line in props.splitlines()) + "\n"
        # keep remaining props
        body = body.strip("\n")
        if body and not body.endswith("\n"):
            body = body + "\n"
        return m.group(1) + injected + body + m.group(3)

    new, n = pattern.subn(repl, text, count=1)
    return new if n else text


def add_class(html: str, tag_class: str, extra: str) -> str:
    """Add class token if missing: class="foo" → class="foo extra"."""
    pat = re.compile(rf'(class=")([^"]*\b{re.escape(tag_class)}\b[^"]*)(")')

    def repl(m: re.Match) -> str:
        classes = m.group(2)
        if extra in classes.split():
            return m.group(0)
        return f'{m.group(1)}{classes} {extra}{m.group(3)}'

    return pat.sub(repl, html, count=1)


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    name = path.name

    # Universal: kill 800/900 on display-ish type
    text = text.replace("font-weight: 800;", "font-weight: var(--fw-hero);")
    text = text.replace("font-weight: 900;", "font-weight: var(--fw-emphasis);")

    # Per-section wiring
    if name == "collection-hero.liquid":
        text = replace_block_props(text, ".coll-hero__title", HERO_TITLE_CSS)
        text = add_class(text, "coll-hero__title", "type-hero")
        text = text.replace(
            "font-weight: var(--weight-bold);\n    margin: 0 0 var(--space-3);",
            "font-weight: var(--type-label-weight);\n    margin: 0 0 var(--gap-a);",
            1,
        )
        # eyebrow already has uppercase — align weight/tracking via label tokens
        text = replace_block_props(
            text,
            ".coll-hero__eyebrow",
            "font-size: var(--type-label-size);\n    font-weight: var(--type-label-weight);\n    letter-spacing: var(--type-label-tracking);\n    text-transform: uppercase;",
        )
        text = text.replace(
            "margin: 0 0 var(--space-4);",
            "margin: 0 0 var(--gap-b);",
            1,
        )

    elif name == "hero-alt.liquid":
        text = replace_block_props(text, ".hero__title", HERO_TITLE_CSS)
        text = add_class(text, "hero__title", "type-hero")
        text = replace_block_props(
            text,
            ".hero__eyebrow",
            "font-size: var(--type-label-size);\n    font-weight: var(--type-label-weight);\n    letter-spacing: var(--type-label-tracking);\n    text-transform: uppercase;",
        )
        text = text.replace(
            ".hero__title {\n      font-size: 34px;\n    }",
            ".hero__title {\n      font-size: var(--type-hero-size-mobile);\n    }",
        )

    elif name == "pdp-sock-math.liquid":
        text = replace_block_props(text, ".sock-math__headline", DISPLAY_TITLE_CSS)
        text = add_class(text, "sock-math__headline", "h2-display")
        # Price numerals can stay bold but not 800 — already replaced
        text = text.replace(
            ".sock-math__ours {\n    font-size: 56px;\n    font-weight: var(--fw-hero);",
            ".sock-math__ours {\n    font-size: 56px;\n    font-weight: var(--fw-emphasis);",
        )

    elif name == "pdp-features.liquid":
        text = replace_block_props(text, ".pdp-features__title", SECTION_TITLE_CSS)
        text = add_class(text, "pdp-features__title", "h2-standard")

    elif name == "pdp-buy-box.liquid":
        # Product name is page H1
        if ".pdp-buy__seo-title" in text or ".pdp-buy__name" in text:
            for sel in (".pdp-buy__seo-title", ".pdp-buy__name"):
                if sel in text:
                    text = replace_block_props(text, sel, HERO_TITLE_CSS)
        text = add_class(text, "pdp-buy__seo-title", "type-hero")

    elif name == "page-about.liquid":
        text = replace_block_props(text, ".page-about__title", HERO_TITLE_CSS)
        text = add_class(text, "page-about__title", "type-hero")
        for sel in (".page-about__values-title", ".page-about__usa-title"):
            text = replace_block_props(text, sel, SECTION_TITLE_CSS)
            text = add_class(text, sel.lstrip("."), "h2-standard")

    elif name == "page-faq.liquid":
        text = replace_block_props(text, ".page-faq__title", HERO_TITLE_CSS)
        text = add_class(text, "page-faq__title", "type-hero")
        for sel in (".page-faq__category-title", ".page-faq__category-heading"):
            text = replace_block_props(text, sel, SECTION_TITLE_CSS)
            text = add_class(text, sel.lstrip("."), "h2-standard")

    elif name == "page-compare.liquid":
        text = replace_block_props(text, ".page-compare__title", HERO_TITLE_CSS)
        text = add_class(text, "page-compare__title", "type-hero")
        text = replace_block_props(text, ".page-compare__product-name", SECTION_TITLE_CSS)

    elif name == "page-size-guide.liquid":
        text = replace_block_props(text, ".page-size__title", HERO_TITLE_CSS)
        text = add_class(text, "page-size__title", "type-hero")
        text = replace_block_props(text, ".page-size__section-title", SECTION_TITLE_CSS)
        text = add_class(text, "page-size__section-title", "h2-standard")

    elif name == "page-grip-comparison.liquid":
        text = replace_block_props(text, ".page-grip__hero-title", HERO_TITLE_CSS)
        text = add_class(text, "page-grip__hero-title", "type-hero")
        text = replace_block_props(text, ".page-grip__section-title", SECTION_TITLE_CSS)
        text = add_class(text, "page-grip__section-title", "h2-standard")
        text = replace_block_props(text, ".page-grip__cta-title", DISPLAY_TITLE_CSS)
        text = add_class(text, "page-grip__cta-title", "h2-display")

    elif name == "page-technology.liquid":
        text = replace_block_props(text, ".page-tech__title", HERO_TITLE_CSS)
        text = add_class(text, "page-tech__title", "type-hero")
        text = replace_block_props(text, ".page-tech__section-title", SECTION_TITLE_CSS)
        text = add_class(text, "page-tech__section-title", "h2-standard")

    elif name == "page-contact.liquid":
        for sel in (".page-contact__title", ".contact__title", ".page-contact h1"):
            if sel in text or (sel.startswith(".") and sel[1:] in text):
                text = replace_block_props(text, sel if sel.startswith(".") else "h1", HERO_TITLE_CSS)
        # generic class hunt
        for cls in ("page-contact__title", "contact-page__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "page-returns.liquid":
        for cls in ("page-returns__title", "returns__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "page-shipping.liquid":
        for cls in ("page-shipping__title", "shipping__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "page-warranty.liquid":
        for cls in ("page-warranty__title", "warranty__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "page-ambassador.liquid":
        for cls in ("page-ambassador__title", "ambassador__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "page-partners.liquid":
        for cls in ("page-partners__title", "partners__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "page-wholesale.liquid":
        for cls in ("page-wholesale__title", "wholesale__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "page-studio-program.liquid":
        for cls in ("page-studio__title", "studio-program__title", "page-studio-program__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "blog-listing.liquid":
        text = replace_block_props(text, ".blog-listing__title", HERO_TITLE_CSS)
        text = add_class(text, "blog-listing__title", "type-hero")
        text = replace_block_props(text, ".blog-card__title", SECTION_TITLE_CSS)

    elif name == "main-cart.liquid":
        text = replace_block_props(text, ".main-cart__title", SECTION_TITLE_CSS)
        text = add_class(text, "main-cart__title", "h2-standard")

    elif name == "article-content.liquid":
        for cls in ("article-content__title", "article__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", HERO_TITLE_CSS)
                text = add_class(text, cls, "type-hero")

    elif name == "search-results.liquid":
        for cls in ("search-results__title", "search__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", SECTION_TITLE_CSS)
                text = add_class(text, cls, "h2-standard")

    elif name == "recently-viewed.liquid":
        text = replace_block_props(text, ".recently-viewed__heading", SECTION_TITLE_CSS)
        text = add_class(text, "recently-viewed__heading", "h2-standard")

    elif name == "recommendations.liquid":
        for cls in ("recommendations__title", "recommendations__heading"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", SECTION_TITLE_CSS)
                text = add_class(text, cls, "h2-standard")

    elif name == "collection-faq.liquid":
        for cls in ("collection-faq__title", "coll-faq__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", SECTION_TITLE_CSS)
                text = add_class(text, cls, "h2-standard")

    elif name == "pdp-reviews.liquid":
        for cls in ("pdp-reviews__title", "reviews__title"):
            if cls in text:
                text = replace_block_props(text, f".{cls}", SECTION_TITLE_CSS)
                text = add_class(text, cls, "h2-standard")

    # Eyebrow weight 700 → label 600 where using weight-bold on eyebrow-ish
    # (narrow — only common pattern)
    text = re.sub(
        r"(\.[\w-]*(?:eyebrow|label)[^{]*\{[^}]*font-weight:\s*)var\(--weight-bold\)",
        r"\1var(--type-label-weight)",
        text,
    )

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = []
    for path in sorted(SECTIONS.glob("*.liquid")):
        if patch_file(path):
            changed.append(path.name)
            print(f"OK {path.name}")
    print(f"\nUpdated {len(changed)} sections")


if __name__ == "__main__":
    main()
