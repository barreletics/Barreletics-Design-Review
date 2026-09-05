#!/usr/bin/env python3
"""Find live 11px uppercase label/eyebrow rules still at weight 700 or 500.

A rule counts as "live" only when its class also appears in a class= attribute,
so dead CSS is reported separately instead of being flagged as a defect.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(os.path.dirname(os.path.dirname(HERE)), "docs")

FILES = [
    "Barreletics Collection - Definitive-v19.html",
    "Barreletics SEO - Best Grippy Socks - Definitive-v37.html",
    "Barreletics Journal - Definitive-v6.html",
    "Barreletics Help - Definitive-v4.html",
]

RULE = re.compile(r"(\.[a-zA-Z0-9_-]+)\s*(?:,[^{]*)?\{([^}]*)\}", re.S)

for name in FILES:
    with open(os.path.join(DOCS, name)) as fh:
        html = fh.read()
    used = set(re.findall(r'class="([^"]*)"', html))
    used = {c for group in used for c in group.split()}

    live, dead = [], []
    for sel, body in RULE.findall(html):
        if "uppercase" not in body:
            continue
        size = re.search(r"font-size:\s*(\d+)px", body)
        weight = re.search(r"font-weight:\s*(\d+)", body)
        if not size or not weight:
            continue
        if int(size.group(1)) > 12 or weight.group(1) not in ("700", "500"):
            continue
        row = "      %-34s %spx / %s" % (sel, size.group(1), weight.group(1))
        (live if sel[1:] in used else dead).append(row)

    print("\n== %s" % name)
    print("   LIVE off-role labels:")
    print("\n".join(live) if live else "      none")
    if dead:
        print("   dead CSS (not rendered):")
        print("\n".join(dead))
