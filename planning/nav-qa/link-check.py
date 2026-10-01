#!/usr/bin/env python3
"""
Link check for every internal destination the M4 chrome ships.

Hrefs are pulled straight out of the theme files, so this cannot drift from what actually
renders. Liquid comments are stripped first — several of them quote dead handles precisely
to explain why they are not used.

    python3 planning/nav-qa/link-check.py

Non-200 results split two ways:
  * PENDING — documented as waiting on Admin content (kit products, future collections).
    Reported, never fails the run.
  * DEAD    — a link a shopper can click today that goes nowhere. Fails the run.
"""

import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
STORE = "https://barreletics.com"
OUTDIR = os.path.dirname(os.path.abspath(__file__))

SHIPPED = [
    "shopify-build/sections/footer.liquid",
    "shopify-build/sections/header.liquid",
    "shopify-build/sections/pdp-buy-box.liquid",
    "shopify-build/sections/variant-grid.liquid",
    "shopify-build/sections/announcement-strip.liquid",
]
SPEC = "planning/navigation-menu-spec.md"

PATH_RE = re.compile(r"/(?:pages|collections|products|blogs|policies|apps)/[a-z0-9\-]+")
COMMENT_RE = re.compile(r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}", re.S)
LIQUID_HASH_RE = re.compile(r"^\s*#.*$", re.M)

# Destinations that do not exist yet on purpose. Each needs Admin content, not a code fix.
PENDING = {
    "/products/hot-pilates-kit": "Complete the kit — kit product not created (Coming soon)",
    "/products/hot-yoga-kit": "Complete the kit — kit product not created (Coming soon)",
    "/collections/grippy-shoes": "architecture pillar collection — not created",
    "/collections/open-sole": "architecture sub-collection — not created",
    "/collections/closed-sole": "architecture sub-collection — not created",
    "/collections/outdoor": "architecture sub-collection — not created",
    "/collections/collaborations": "architecture collection — not created",
    "/collections/tops": "deferred — one product",
    "/collections/bottoms": "deferred — one product",
    "/collections/accessories": "architecture marks (future)",
    "/collections/sale": "removed 2026-08-08 — nothing on sale",
    "/collections/hot-kits": "legacy live-only kits — excluded",
    "/pages/about": "future target for About Us (/pages/our-story is live)",
    "/pages/contact": "future target for Contact Us (/pages/contact-us-form is live)",
    "/pages/returns-exchanges": "future target (/pages/returns is live)",
    "/pages/help": "never created — header fallback points at /pages/faq instead",
    "/pages/warranty": "page never created",
    "/pages/size-guide": "page never created",
    "/pages/size-chart": "page never created",
    "/pages/shipping": "page never created",
    "/pages/track-your-order": "page never created",
    "/pages/accessibility": "page never created",
    "/pages/how-it-works": "page never created",
    "/pages/compare": "page never created",
    "/pages/shipping-returns": "page never created",
    "/collections/collabs": "candidate handle checked in the spec — does not exist",
    "/collections/collaboration": "candidate handle checked in the spec — does not exist",
    "/pages/collaborations": "candidate handle checked in the spec — does not exist",
    "/pages/coperni": "candidate handle checked in the spec — does not exist",
    "/apps/tracktor": "order tracking app not installed",
    "/products/gift-card": "no gift card product exists — row held out of the footer",
}


def paths_in(rel, strip_comments):
    full = os.path.join(ROOT, rel)
    if not os.path.exists(full):
        return set()
    with open(full, encoding="utf-8") as fh:
        text = fh.read()
    if strip_comments:
        text = COMMENT_RE.sub(" ", text)
        text = LIQUID_HASH_RE.sub(" ", text)
    return set(PATH_RE.findall(text))


def status(path):
    # curl, not urllib: this interpreter has no CA bundle wired up, so urllib fails TLS
    # verification on every request and reports it as if the page were down.
    # Shopify throttles a fast sequential sweep with 429/503, which looks identical to a
    # broken page in the output — back off and retry so those never get reported as dead.
    for attempt in range(4):
        out = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L",
             "--max-time", "25", STORE + path],
            capture_output=True, text=True)
        code = out.stdout.strip() or "ERR"
        if code not in ("429", "503"):
            return code
        time.sleep(2 * (attempt + 1))
    return code


def main():
    shipped = set()
    for rel in SHIPPED:
        shipped |= paths_in(rel, strip_comments=True)
    spec_only = paths_in(SPEC, strip_comments=False) - shipped

    report = {"shipped": {}, "spec_only": {}, "dead": [], "pending": []}

    for group, paths in (("shipped", sorted(shipped)), ("spec_only", sorted(spec_only))):
        for p in paths:
            code = status(p)
            report[group][p] = code
            if code == "200":
                continue
            if p in PENDING:
                report["pending"].append("%s → %s (%s)" % (p, code, PENDING[p]))
            else:
                report["dead"].append("%s → %s [%s]" % (p, code, group))

    with open(os.path.join(OUTDIR, "link-check.json"), "w") as fh:
        json.dump(report, fh, indent=1)

    print("Links shipped by the theme:")
    for p, code in sorted(report["shipped"].items()):
        print("  %-4s %s" % (code, p))
    if report["pending"]:
        print("\nPending Admin content (expected, not a code defect):")
        for p in report["pending"]:
            print("  - " + p)
    if report["dead"]:
        print("\nFAIL — dead links with no documented reason:")
        for d in report["dead"]:
            print("  - " + d)
        return 1
    print("\nPASS — every clickable link resolves, or is a documented Admin gap")
    return 0


if __name__ == "__main__":
    sys.exit(main())
