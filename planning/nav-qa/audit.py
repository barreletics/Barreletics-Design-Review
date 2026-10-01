#!/usr/bin/env python3
"""
M4 navigation audit — drives planning/nav-qa/harness.html in headless Chrome and asserts
the whole two-level menu actually behaves, at 390 / 768 / 1024 / 1440.

It exercises the shipped assets/chrome.js (hamburger, accordion, Escape) rather than
simulating them, and reads geometry back off the live layout: dropdown position and
clipping, empty-dropdown artifacts on childless parents, drawer tap-target heights, and
horizontal overflow.

    python3 planning/nav-qa/audit.py

Writes report.json plus a PNG per scenario into this directory. Exit code is 1 if any
check fails, so it can gate a change to header.liquid / chrome.css.
"""

import base64
import http.client
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

import websocket  # websocket-client

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTDIR = os.path.dirname(os.path.abspath(__file__))
HARNESS = "file://" + os.path.join(OUTDIR, "harness.html")
WIDTHS = [390, 768, 1024, 1440]
MIN_TAP = 44


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Chrome:
    def __init__(self, width, height):
        self.port = free_port()
        self.profile = tempfile.mkdtemp(prefix="navqa-")
        self.proc = subprocess.Popen(
            [CHROME, "--headless=new", "--disable-gpu", "--no-first-run",
             "--no-default-browser-check", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--allow-file-access-from-files",
             "--remote-debugging-port=%d" % self.port, "--remote-allow-origins=*",
             "--user-data-dir=" + self.profile,
             "--window-size=%d,%d" % (width, height), "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.ws = None
        self._id = 0
        self._connect()

    def _connect(self):
        deadline = time.time() + 45
        last = None
        while time.time() < deadline:
            try:
                # http.client, not urllib: urllib honours HTTP(S)_PROXY, which would send
                # loopback DevTools requests to a proxy that cannot answer them.
                conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
                conn.request("GET", "/json/list")
                raw = conn.getresponse().read()
                conn.close()
                for t in json.loads(raw):
                    if t.get("type") == "page":
                        self.ws = websocket.create_connection(
                            t["webSocketDebuggerUrl"], timeout=45,
                            max_size=64 * 1024 * 1024)
                        return
            except Exception as e:  # noqa: BLE001 — retry until the port answers
                last = e
                time.sleep(0.4)
        raise RuntimeError("could not attach to headless Chrome: %r" % (last,))

    def send(self, method, params=None):
        self._id += 1
        mid = self._id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError("%s: %s" % (method, msg["error"]))
                return msg.get("result", {})

    def close(self):
        try:
            if self.ws:
                self.ws.close()
        finally:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except Exception:  # noqa: BLE001
                self.proc.kill()
            shutil.rmtree(self.profile, ignore_errors=True)


def evaluate(ch, expr):
    r = ch.send("Runtime.evaluate", {"expression": expr, "returnByValue": True,
                                     "awaitPromise": True})
    if r.get("exceptionDetails"):
        raise RuntimeError(json.dumps(r["exceptionDetails"])[:800])
    return r["result"].get("value")


def shot(ch, name, width, height):
    clip = {"x": 0, "y": 0, "width": width, "height": height, "scale": 1}
    data = ch.send("Page.captureScreenshot",
                   {"format": "png", "clip": clip, "captureBeyondViewport": True})
    path = os.path.join(OUTDIR, name)
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(data["data"]))
    return path


def shot_fixed(ch, name, width, height, mobile):
    """Screenshot a position:fixed layer (the drawer).

    captureBeyondViewport paints a taller page than the layout viewport, which leaves
    fixed elements anchored to the original viewport and produces a torn image. Growing
    the emulated viewport instead and capturing it directly keeps the drawer intact.
    """
    ch.send("Emulation.setDeviceMetricsOverride",
            {"width": width, "height": height, "deviceScaleFactor": 2, "mobile": mobile})
    time.sleep(0.5)
    data = ch.send("Page.captureScreenshot",
                   {"format": "png", "captureBeyondViewport": False})
    path = os.path.join(OUTDIR, name)
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(data["data"]))
    return path


# --- browser-side helpers -----------------------------------------------------------

HELPERS = r"""
window.__nav = {
  rect: function (el) {
    var r = el.getBoundingClientRect();
    return { x: Math.round(r.x), y: Math.round(r.y),
             w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10,
             right: Math.round(r.right), bottom: Math.round(r.bottom) };
  },
  // A dropdown can be "open" in CSS yet invisible because an ancestor clips it or a
  // higher-stacked element covers it. Hit-testing the painted centre of a row is the
  // only check that catches both.
  hitOk: function (el) {
    var r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) return false;
    var x = r.x + r.width / 2, y = r.y + r.height / 2;
    if (x < 0 || y < 0 || x > innerWidth || y > innerHeight) return false;
    var hit = document.elementFromPoint(x, y);
    return !!hit && (hit === el || el.contains(hit) || hit.contains(el));
  },
  overlaps: function (a, b) {
    var p = a.getBoundingClientRect(), q = b.getBoundingClientRect();
    return !(p.right <= q.left + 0.5 || q.right <= p.left + 0.5 ||
             p.bottom <= q.top + 0.5 || q.bottom <= p.top + 0.5);
  }
};
true
"""

# Structural facts that hold at every width.
STRUCTURE = r"""
(() => {
  const out = { items: [], plainItemsWithSubnav: [], help: null };
  document.querySelectorAll('.site-header__nav-item').forEach(li => {
    const a = li.querySelector(':scope > a');
    const sub = li.querySelector(':scope > .site-header__subnav');
    const entry = {
      label: a ? a.textContent.trim() : null,
      href: a ? a.getAttribute('href') : null,
      hasSubClass: li.classList.contains('site-header__nav-item--has-sub'),
      childCount: sub ? sub.querySelectorAll('li > a').length : 0,
      children: sub ? Array.from(sub.querySelectorAll('li > a')).map(
        c => ({ label: c.textContent.trim(), href: c.getAttribute('href') })) : []
    };
    out.items.push(entry);
    // An empty-dropdown artifact = a subnav element on an item with no children, or a
    // has-sub class with nothing under it.
    if (sub && entry.childCount === 0) out.plainItemsWithSubnav.push(entry.label);
    if (!sub && entry.hasSubClass) out.plainItemsWithSubnav.push(entry.label + ' (class only)');
  });
  const help = document.querySelector('.site-header__help');
  if (help) {
    const a = help.querySelector('.site-header__action--help');
    out.help = {
      label: a ? a.textContent.replace(/\s+/g, ' ').trim() : null,
      caret: !!help.querySelector('.site-header__caret'),
      children: Array.from(help.querySelectorAll('.site-header__subnav--help li > a'))
        .map(c => ({ label: c.textContent.trim(), href: c.getAttribute('href') }))
    };
  }
  out.drawer = {
    parents: Array.from(document.querySelectorAll('.mobile-menu__item--parent')).map(li => ({
      label: li.querySelector('.mobile-menu__toggle').textContent.trim(),
      children: Array.from(li.querySelectorAll('.mobile-menu__sub li > a'))
        .map(c => ({ label: c.textContent.trim(), href: c.getAttribute('href') }))
    })),
    plain: Array.from(document.querySelectorAll('.mobile-menu__item:not(.mobile-menu__item--parent)'))
      .map(li => {
        const a = li.querySelector('a');
        return { label: a.textContent.trim(), href: a.getAttribute('href') };
      }),
    utility: Array.from(document.querySelectorAll('.mobile-menu__utility li > a'))
      .map(a => ({ label: a.textContent.trim(), href: a.getAttribute('href') }))
  };
  return out;
})()
"""

# Desktop dropdowns are opened one at a time through the :focus-within path (which is
# also the keyboard path) and measured after the opacity transition has settled — reading
# the computed style in the same tick returns the transition's start value, not its end.
FOCUS_DROPDOWN = r"""
(() => {
  const parents = Array.from(document.querySelectorAll('.site-header__nav-item--has-sub'))
    .filter(li => li.querySelector(':scope > .site-header__subnav'));
  const help = document.querySelector('.site-header__help');
  const idx = __INDEX__;
  const el = idx < parents.length ? parents[idx] : help;
  if (!el) return null;
  const a = el.querySelector(':scope > a') || el.querySelector('.site-header__action--help');
  document.activeElement && document.activeElement.blur();
  a.focus();
  return a.textContent.replace(/\s+/g, ' ').trim();
})()
"""

MEASURE_DROPDOWN = r"""
(() => {
  const parents = Array.from(document.querySelectorAll('.site-header__nav-item--has-sub'))
    .filter(li => li.querySelector(':scope > .site-header__subnav'));
  const help = document.querySelector('.site-header__help');
  const idx = __INDEX__;
  const container = idx < parents.length ? parents[idx] : help;
  if (!container) return null;
  const a = container.querySelector(':scope > a')
    || container.querySelector('.site-header__action--help');
  const sub = container.querySelector(':scope > .site-header__subnav');
  const rows = Array.from(sub.querySelectorAll('li > a'));
  const cs = getComputedStyle(sub);
  const r = window.__nav.rect(sub);
  return {
    label: a.textContent.replace(/\s+/g, ' ').trim(),
    opacity: cs.opacity,
    pointerEvents: cs.pointerEvents,
    rect: r,
    withinViewport: r.x >= 0 && r.right <= innerWidth,
    belowParent: r.y >= Math.round(container.getBoundingClientRect().bottom) - 2,
    rowCount: rows.length,
    firstRowHit: rows.length ? window.__nav.hitOk(rows[0]) : false,
    lastRowHit: rows.length ? window.__nav.hitOk(rows[rows.length - 1]) : false,
    rowLabels: rows.map(a2 => a2.textContent.trim()),
    rowHeights: rows.map(a2 => Math.round(a2.getBoundingClientRect().height))
  };
})()
"""


def dropdown_count(ch):
    # .site-header__help carries the --has-sub class too, so this one selector already
    # covers Grippy Shoes, Apparel and Help.
    return evaluate(ch, "document.querySelectorAll("
                        "'.site-header__nav-item--has-sub >"
                        " .site-header__subnav').length")


def open_and_measure(ch, index):
    evaluate(ch, FOCUS_DROPDOWN.replace("__INDEX__", str(index)))
    time.sleep(0.45)
    return evaluate(ch, MEASURE_DROPDOWN.replace("__INDEX__", str(index)))

# Nothing may spill past the viewport, and the three header regions must not touch.
LAYOUT = r"""
(() => {
  const doc = document.documentElement;
  const logo = document.querySelector('.site-header__logo');
  const nav = document.querySelector('.site-header__nav');
  const actions = document.querySelector('.site-header__actions');
  const inner = document.querySelector('.site-header__inner');
  const navVisible = nav && getComputedStyle(nav).display !== 'none';
  const out = {
    viewport: innerWidth,
    scrollWidth: doc.scrollWidth,
    horizontalOverflow: doc.scrollWidth > innerWidth + 1,
    hamburgerVisible: getComputedStyle(
      document.querySelector('.site-header__hamburger')).display !== 'none',
    navVisible: navVisible,
    helpActionVisible: getComputedStyle(
      document.querySelector('.site-header__action--help')).display !== 'none',
    innerRect: window.__nav.rect(inner),
    logoRect: window.__nav.rect(logo),
    actionsRect: window.__nav.rect(actions),
    collisions: []
  };
  if (navVisible) {
    out.navRect = window.__nav.rect(nav);
    if (window.__nav.overlaps(logo, nav)) out.collisions.push('logo/nav');
    if (window.__nav.overlaps(nav, actions)) out.collisions.push('nav/actions');
    // Flex can shrink children below their content: the row fits while the labels
    // themselves are clipped. Compare scroll width against painted width.
    const navList = document.querySelector('.site-header__nav-list');
    out.navListClipped = navList.scrollWidth > navList.clientWidth + 1;
    out.actionsClipped = actions.scrollWidth > actions.clientWidth + 1;
    const navRight = nav.getBoundingClientRect().right;
    const actionsLeft = actions.getBoundingClientRect().left;
    out.navToActionsGap = Math.round((actionsLeft - navRight) * 10) / 10;
    // The last nav label and the first action label are the real collision pair.
    const lastLink = document.querySelector(
      '.site-header__nav-item:last-child > a');
    const firstAction = document.querySelector('.site-header__actions > *');
    out.lastNavToFirstActionGap = Math.round(
      (firstAction.getBoundingClientRect().left -
       lastLink.getBoundingClientRect().right) * 10) / 10;
  }
  if (window.__nav.overlaps(logo, actions)) out.collisions.push('logo/actions');
  return out;
})()
"""

# Mobile: open the drawer and every accordion through the shipped script, then measure.
DRAWER = r"""
(() => {
  const out = { steps: [] };
  const toggle = document.querySelector('[data-mobile-menu-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  const drawer = document.querySelector('.mobile-menu__drawer');
  toggle.click();
  out.opened = menu.classList.contains('is-open');
  out.ariaHidden = menu.getAttribute('aria-hidden');
  out.toggleExpanded = toggle.getAttribute('aria-expanded');
  out.bodyLocked = document.body.style.overflow === 'hidden';

  const parents = Array.from(document.querySelectorAll('.mobile-menu__item--parent'));
  out.beforeExpand = parents.map(li => ({
    label: li.querySelector('.mobile-menu__toggle').textContent.trim(),
    subDisplay: getComputedStyle(li.querySelector('.mobile-menu__sub')).display,
    expandedAttr: li.getAttribute('data-expanded')
  }));

  parents.forEach(li => li.querySelector('.mobile-menu__toggle').click());

  out.afterExpand = parents.map(li => ({
    label: li.querySelector('.mobile-menu__toggle').textContent.trim(),
    subDisplay: getComputedStyle(li.querySelector('.mobile-menu__sub')).display,
    expandedAttr: li.getAttribute('data-expanded'),
    ariaExpanded: li.querySelector('.mobile-menu__toggle').getAttribute('aria-expanded'),
    childCount: li.querySelectorAll('.mobile-menu__sub li > a').length
  }));

  const drawerRect = drawer.getBoundingClientRect();
  out.drawerRect = window.__nav.rect(drawer);
  out.drawerScrolls = drawer.scrollHeight > drawer.clientHeight + 1;
  out.contentHeight = drawer.scrollHeight;

  // Tap targets: every interactive row in the drawer, measured as painted.
  const targets = Array.from(drawer.querySelectorAll(
    '.mobile-menu__toggle, .mobile-menu__item > a, .mobile-menu__sub li > a,' +
    ' .mobile-menu__utility li > a, .mobile-menu__close'));
  out.tapTargets = targets.map(el => {
    const r = el.getBoundingClientRect();
    return {
      label: (el.getAttribute('aria-label') || el.textContent).replace(/\s+/g, ' ').trim(),
      h: Math.round(r.height * 10) / 10,
      w: Math.round(r.width * 10) / 10,
      overflowsDrawer: r.right > drawerRect.right + 0.5
    };
  });
  out.minTapHeight = Math.min.apply(null, out.tapTargets.map(t => t.h));
  out.overflowingRows = out.tapTargets.filter(t => t.overflowsDrawer).map(t => t.label);
  out.utilityCount = drawer.querySelectorAll('.mobile-menu__utility li > a').length;
  return out;
})()
"""

ESCAPE_CLOSE = r"""
(() => {
  document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
  const menu = document.querySelector('[data-mobile-menu]');
  return { closed: !menu.classList.contains('is-open'),
           ariaHidden: menu.getAttribute('aria-hidden'),
           bodyUnlocked: document.body.style.overflow === '' };
})()
"""


def load(ch, width, height, mobile):
    ch.send("Emulation.setDeviceMetricsOverride",
            {"width": width, "height": height, "deviceScaleFactor": 2, "mobile": mobile})
    ch.send("Page.navigate", {"url": HARNESS})
    time.sleep(1.4)
    evaluate(ch, HELPERS)


def main():
    report = {"harness": HARNESS, "widths": {}, "failures": []}
    fail = report["failures"].append

    ch = Chrome(1600, 1100)
    try:
        ch.send("Page.enable")
        ch.send("Runtime.enable")

        for width in WIDTHS:
            mobile = width <= 768
            height = 900 if width > 768 else 844
            load(ch, width, height, mobile)
            w = {}

            structure = evaluate(ch, STRUCTURE)
            layout = evaluate(ch, LAYOUT)
            w["structure"] = structure
            w["layout"] = layout

            if layout["horizontalOverflow"]:
                fail("%dpx: horizontal overflow (scrollWidth %d > %d)"
                     % (width, layout["scrollWidth"], layout["viewport"]))
            if layout["collisions"]:
                fail("%dpx: header regions collide: %s"
                     % (width, ", ".join(layout["collisions"])))
            if layout.get("navListClipped"):
                fail("%dpx: nav labels clipped inside .site-header__nav-list" % width)
            if layout.get("actionsClipped"):
                fail("%dpx: utility actions clipped" % width)
            gap = layout.get("lastNavToFirstActionGap")
            if gap is not None and gap < 12:
                fail("%dpx: only %.1fpx between last nav link and first action"
                     % (width, gap))

            if structure["plainItemsWithSubnav"]:
                fail("%dpx: empty dropdown artifact on %s"
                     % (width, ", ".join(structure["plainItemsWithSubnav"])))

            expected_parents = {"Grippy Shoes": 5, "Apparel": 3}
            for item in structure["items"]:
                want = expected_parents.get(item["label"])
                if want is not None and item["childCount"] != want:
                    fail("%dpx: %s has %d children, expected %d"
                         % (width, item["label"], item["childCount"], want))
                if want is None and item["childCount"]:
                    fail("%dpx: %s should be a plain link but has %d children"
                         % (width, item["label"], item["childCount"]))

            if layout["navVisible"]:
                drops = [open_and_measure(ch, i)
                         for i in range(dropdown_count(ch))]
                drops = [d for d in drops if d]
                w["dropdowns"] = drops
                for d in drops:
                    if d["opacity"] != "1" or d["pointerEvents"] == "none":
                        fail("%dpx: %s dropdown did not open on focus (opacity %s)"
                             % (width, d["label"], d["opacity"]))
                    if not d["withinViewport"]:
                        fail("%dpx: %s dropdown spills outside the viewport (%s)"
                             % (width, d["label"], d["rect"]))
                    if not d["belowParent"]:
                        fail("%dpx: %s dropdown is not positioned under its parent"
                             % (width, d["label"]))
                    if not (d["firstRowHit"] and d["lastRowHit"]):
                        fail("%dpx: %s dropdown rows are clipped or covered"
                             % (width, d["label"]))
                # Open Grippy Shoes and Help for the record shots.
                evaluate(ch, "document.querySelector("
                             "'.site-header__nav-item--has-sub > a').focus()")
                time.sleep(0.4)
                w["shot_dropdown"] = os.path.basename(
                    shot(ch, "nav-%dpx-grippy-open.png" % width, width, 420))
                evaluate(ch, "document.querySelector('.site-header__action--help').focus()")
                time.sleep(0.4)
                w["shot_help"] = os.path.basename(
                    shot(ch, "nav-%dpx-help-open.png" % width, width, 420))
                evaluate(ch, "document.activeElement.blur()")
                time.sleep(0.3)
                w["shot_bar"] = os.path.basename(
                    shot(ch, "nav-%dpx-bar.png" % width, width, 200))
            else:
                if not layout["hamburgerVisible"]:
                    fail("%dpx: nav is hidden but the hamburger is not shown" % width)
                w["shot_bar"] = os.path.basename(
                    shot(ch, "nav-%dpx-bar.png" % width, width, 200))
                drawer = evaluate(ch, DRAWER)
                w["drawer"] = drawer
                if not drawer["opened"]:
                    fail("%dpx: hamburger did not open the drawer" % width)
                if drawer["ariaHidden"] != "false" or drawer["toggleExpanded"] != "true":
                    fail("%dpx: drawer ARIA state wrong after opening" % width)
                for before in drawer["beforeExpand"]:
                    if before["subDisplay"] != "none":
                        fail("%dpx: %s sub-items are visible before tapping (not an "
                             "accordion)" % (width, before["label"]))
                for after in drawer["afterExpand"]:
                    if after["subDisplay"] == "none":
                        fail("%dpx: %s did not expand on tap" % (width, after["label"]))
                    if after["ariaExpanded"] != "true":
                        fail("%dpx: %s aria-expanded not updated" % (width, after["label"]))
                short = [t for t in drawer["tapTargets"] if t["h"] < MIN_TAP]
                if short:
                    fail("%dpx: tap targets under %dpx: %s"
                         % (width, MIN_TAP,
                            ", ".join("%s (%.1f)" % (t["label"], t["h"]) for t in short)))
                if drawer["overflowingRows"]:
                    fail("%dpx: drawer rows overflow the panel: %s"
                         % (width, ", ".join(drawer["overflowingRows"])))
                if drawer["utilityCount"] != 4:
                    fail("%dpx: Help items missing from the drawer (%d of 4)"
                         % (width, drawer["utilityCount"]))
                w["shot_drawer"] = os.path.basename(
                    shot_fixed(ch, "nav-%dpx-drawer-expanded.png" % width, width,
                               min(max(drawer["contentHeight"] + 40, height), 1600),
                               mobile))
                esc = evaluate(ch, ESCAPE_CLOSE)
                w["escape"] = esc
                if not esc["closed"]:
                    fail("%dpx: Escape did not close the drawer" % width)
                if not esc["bodyUnlocked"]:
                    fail("%dpx: body scroll stayed locked after closing" % width)

            report["widths"][str(width)] = w

        # Narrow desktop sweep: the row between the drawer breakpoint and 1024 is where
        # 18px title-case nav is tightest, so walk it rather than trusting four widths.
        sweep = []
        for width in range(769, 1025, 8):
            load(ch, width, 900, False)
            layout = evaluate(ch, LAYOUT)
            entry = {"width": width,
                     "mode": "desktop nav" if layout["navVisible"] else "drawer",
                     "gap": layout.get("lastNavToFirstActionGap"),
                     "overflow": layout["horizontalOverflow"],
                     "collisions": layout["collisions"],
                     "navListClipped": layout.get("navListClipped"),
                     "actionsClipped": layout.get("actionsClipped")}
            sweep.append(entry)
            if not layout["navVisible"] and not layout["hamburgerVisible"]:
                fail("%dpx (sweep): nav hidden with no hamburger" % width)
            if entry["overflow"] or entry["collisions"] or entry["navListClipped"] \
                    or entry["actionsClipped"]:
                fail("%dpx (sweep): %s" % (width, json.dumps(entry)))
            elif entry["gap"] is not None and entry["gap"] < 12:
                fail("%dpx (sweep): only %.1fpx between nav and actions"
                     % (width, entry["gap"]))
        report["narrow_desktop_sweep"] = sweep
    finally:
        ch.close()

    with open(os.path.join(OUTDIR, "report.json"), "w") as fh:
        json.dump(report, fh, indent=1)

    if report["failures"]:
        print("FAIL (%d)" % len(report["failures"]))
        for f in report["failures"]:
            print("  - " + f)
        return 1
    print("PASS — all navigation checks green at %s"
          % ", ".join("%dpx" % w for w in WIDTHS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
