#!/usr/bin/env python3
"""
Viewport sweep — finds the width where the nav and the utility actions collide.

One Chrome instance, device metrics changed per step, so a 40-width sweep costs one
browser launch instead of forty.

Usage:
    python3 planning/header-type-qa/sweep.py 18 22
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe import Chrome, evaluate  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = "file://" + HERE.replace(" ", "%20") + "/harness.html"

MEASURE = r"""
(() => {
  const nav = document.querySelector('.site-header__nav-list');
  const act = document.querySelector('.site-header__actions');
  const logo = document.querySelector('.site-header__logo-img');
  const inner = document.querySelector('.site-header__inner');
  const nb = nav.getBoundingClientRect(), ab = act.getBoundingClientRect();
  const lb = logo.getBoundingClientRect(), ib = inner.getBoundingClientRect();
  const navVisible = getComputedStyle(nav.parentElement).display !== 'none';
  return {
    vw: innerWidth,
    navVisible: navVisible,
    headroom: Math.round((ab.x - (nb.x + nb.width)) * 10) / 10,
    navW: Math.round(nb.width * 10) / 10,
    actW: Math.round(ab.width * 10) / 10,
    logoW: Math.round(lb.width * 10) / 10,
    innerW: Math.round(ib.width * 10) / 10,
    // Any horizontal scroll means the bar no longer fits at all.
    docOverflow: Math.max(0, document.documentElement.scrollWidth - innerWidth)
  };
})()
"""


def main():
    sizes = [int(a) for a in sys.argv[1:]] or [18, 22]
    widths = list(range(1440, 1180, -40)) + list(range(1180, 740, -20))
    results = {}

    for size in sizes:
        ch = Chrome(1600, 900)
        try:
            ch.send("Page.enable")
            ch.send("Runtime.enable")
            ch.send("Emulation.setDeviceMetricsOverride",
                    {"width": 1440, "height": 400, "deviceScaleFactor": 1, "mobile": False})
            ch.send("Page.navigate", {"url": "%s?size=%d" % (HARNESS, size)})
            time.sleep(2.5)
            rows = []
            for w in widths:
                ch.send("Emulation.setDeviceMetricsOverride",
                        {"width": w, "height": 400, "deviceScaleFactor": 1,
                         "mobile": False})
                time.sleep(0.12)
                rows.append(evaluate(ch, MEASURE))
            results[size] = rows
        finally:
            ch.close()

    for size, rows in results.items():
        desktop = [r for r in rows if r["navVisible"]]
        print("\n=== nav_link_size %d ===" % size)
        need = desktop[0]["logoW"] + desktop[0]["navW"] + desktop[0]["actW"] + 48
        print("logo %.1f + nav %.1f + actions %.1f + 2x24 gap = %.1f px of content"
              % (desktop[0]["logoW"], desktop[0]["navW"], desktop[0]["actW"], need))
        print("%-7s %-9s %-9s %-9s %s" % ("vw", "innerW", "headroom", "overflow", "state"))
        prev = None
        for r in desktop:
            state = "ok"
            if r["headroom"] <= 24.5:
                state = "AT GAP FLOOR"
            if r["docOverflow"] > 0 or r["headroom"] < 0:
                state = "COLLIDE / OVERFLOW"
            # Only print the interesting band plus the anchors.
            if r["vw"] in (1440, 1200) or state != "ok" or (prev and prev != state):
                print("%-7s %-9s %-9s %-9s %s"
                      % (r["vw"], r["innerW"], r["headroom"], r["docOverflow"], state))
            prev = state
        floor = [r for r in desktop if r["headroom"] <= 24.5]
        bad = [r for r in desktop if r["docOverflow"] > 0 or r["headroom"] < 0]
        print("first width at 24px gap floor : %s" % (floor[0]["vw"] if floor else "none >=760"))
        print("first width that overflows    : %s" % (bad[0]["vw"] if bad else "none >=760"))
        print("nav hidden below              : 768px (drawer takes over)")

    with open(os.path.join(HERE, "collision-sweep.json"), "w") as fh:
        json.dump(results, fh, indent=1)
    print("\nJSON: planning/header-type-qa/collision-sweep.json")


if __name__ == "__main__":
    main()
