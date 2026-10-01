#!/usr/bin/env python3
"""
Asserts the header bar does not cause horizontal scroll at a given width.

`right edge past the padding` is not the same as `overflow`: the 16px mobile padding
absorbs a few px before anything clips. This checks the document, not the box.

Usage:
    python3 planning/header-type-qa/overflow-check.py 390 360 320
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe import Chrome, evaluate  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = "file://" + HERE.replace(" ", "%20") + "/harness.html"

CHECK = r"""
(() => {
  const de = document.documentElement;
  const cart = document.querySelector('.site-header__cart');
  const inner = document.querySelector('.site-header__inner');
  const cb = cart.getBoundingClientRect(), ib = inner.getBoundingClientRect();
  const cs = getComputedStyle(inner);
  return {
    vw: innerWidth,
    scrollWidth: de.scrollWidth,
    docOverflow: Math.max(0, de.scrollWidth - innerWidth),
    innerPadRight: cs.paddingRight,
    cartRight: Math.round(cb.right * 10) / 10,
    innerRight: Math.round(ib.right * 10) / 10,
    slackToViewport: Math.round((innerWidth - cb.right) * 10) / 10
  };
})()
"""


def main():
    widths = [int(a) for a in sys.argv[1:]] or [390]
    out = []
    ch = Chrome(600, 900)
    try:
        ch.send("Page.enable")
        ch.send("Runtime.enable")
        ch.send("Emulation.setDeviceMetricsOverride",
                {"width": widths[0], "height": 700, "deviceScaleFactor": 1, "mobile": True})
        ch.send("Page.navigate", {"url": HARNESS})
        time.sleep(2.5)
        for w in widths:
            ch.send("Emulation.setDeviceMetricsOverride",
                    {"width": w, "height": 700, "deviceScaleFactor": 1, "mobile": True})
            time.sleep(0.2)
            r = evaluate(ch, CHECK)
            out.append(r)
            print("vw=%-5s scrollWidth=%-5s overflow=%-4s cartRight=%-7s "
                  "padRight=%-5s slackToViewport=%s"
                  % (r["vw"], r["scrollWidth"], r["docOverflow"], r["cartRight"],
                     r["innerPadRight"], r["slackToViewport"]))
    finally:
        ch.close()
    with open(os.path.join(HERE, "overflow-check.json"), "w") as fh:
        json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
