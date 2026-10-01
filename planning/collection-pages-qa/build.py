#!/usr/bin/env python3
"""
Collection template QA harness.

The five collection templates had no preview anywhere under planning/, which is why the
broken video source and the grey placeholder panels were never seen on screen. This renders
each collection template's sections for real from shopify-build/ so the output HTML can be
read and grepped instead of trusting the source JSON.

Shopify `collection` / `product` objects are not available outside the storefront, so
product-driven markup (variant cards, Admin collection titles) renders empty here. Everything
that comes from template settings — headings, body copy, links, media URLs — is real.

    python3 planning/collection-pages-qa/build.py
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "returns-pages-qa"))

import build as R  # noqa: E402  (returns harness: Liquid env, tag stripping, renderer)

TEMPLATES = R.TEMPLATES
ASSETS = os.path.relpath(R.ASSETS, HERE) if os.path.isabs(R.ASSETS) else R.ASSETS

PAGES = {
    "collection": "collection.json",
    "hot-kits": "collection.hot-kits.json",
    "outdoor": "collection.outdoor.json",
    "open-sole": "collection.open-sole.json",
    "closed-sole": "collection.closed-sole.json",
    "gift-cards": "collection.gift-cards.json",
    "limited-editions": "collection.limited-editions.json",
    "new-arrivals": "collection.new-arrivals.json",
    "one-offs": "collection.one-offs.json",
    "sale": "collection.sale.json",
}


def _handleize(value):
    return re.sub(r"[^a-z0-9]+", "-", str(value or "").lower()).strip("-")


class Settings(dict):
    """Unset Shopify settings resolve to nil, which `!= blank` treats as empty. python-liquid
    would otherwise report them Undefined and take the wrong branch — which is what made the
    image/video fallback chain in fifty-fifty render an empty media column."""

    def __missing__(self, key):
        return ""


def build(name, template):
    from liquid import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader(R.SNIPPETS, ext=".liquid"))
    env.filters["json"] = lambda v: json.dumps(v if isinstance(v, (str, int, float, bool, list, dict)) or v is None else str(v))
    # Storefront-only filters. Shopify image objects do not exist here; every collection
    # template supplies its media through the *_url string settings instead.
    env.filters.setdefault("image_url", lambda v, **kw: "")
    env.filters.setdefault("image_tag", lambda v, **kw: "")
    env.filters.setdefault("money", lambda v: v)
    env.filters.setdefault("asset_url", lambda v: v)
    env.filters.setdefault("handleize", _handleize)
    env.filters.setdefault("handle", _handleize)
    env.filters.setdefault("video_tag", lambda v, **kw: "")
    env.filters.setdefault("img_url", lambda v, *a, **kw: "")
    env.filters.setdefault("within", lambda v, *a: v)
    env.filters.setdefault("link_to", lambda v, *a: v)

    tpl = json.load(open(os.path.join(TEMPLATES, template)))
    for conf in tpl["sections"].values():
        conf["settings"] = Settings(conf.get("settings", {}))
        for block in conf.get("blocks", {}).values():
            block["settings"] = Settings(block.get("settings", {}))
    body = "\n".join(
        R.render_section(env, tpl["sections"][sid]["type"], tpl["sections"][sid], None)
        for sid in tpl["order"]
    )
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — collection pages QA</title>
<link rel="stylesheet" href="{ASSETS}/design-tokens.css">
<link rel="stylesheet" href="{ASSETS}/barreletics-base.css">
<link rel="stylesheet" href="{ASSETS}/chrome.css">
</head><body>
{body}
</body></html>
"""


def main():
    for name, template in PAGES.items():
        html = build(name, template)
        out = os.path.join(HERE, "preview-%s.html" % name)
        with open(out, "w") as fh:
            fh.write(html)
        print("built %s (%d KB)" % (os.path.relpath(out), len(html) // 1024))


if __name__ == "__main__":
    main()
