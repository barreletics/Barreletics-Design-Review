#!/usr/bin/env python3
"""
Header typography probe — reads *computed* styles off a rendered header.

Why a clean headless profile: an ordinary browser that has ever previewed a Shopify
draft keeps a `preview_theme_id` cookie, so barreletics.com silently renders the draft
instead of the published theme. A throwaway --user-data-dir guarantees production.

Usage:
    python3 planning/header-type-qa/probe.py --url https://barreletics.com --width 1440 \
        --label live-desktop --selectors ".site-nav__link,.site-nav__dropdown-link"
    python3 planning/header-type-qa/probe.py --url file:///.../harness.html --width 390 \
        --label ours-mobile --click ".site-header__hamburger"
"""

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import base64

import websocket  # websocket-client

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTDIR = os.path.dirname(os.path.abspath(__file__))

PROBE = r"""
(() => {
  const SELECTORS = __SELECTORS__;
  const out = { vw: innerWidth, dpr: devicePixelRatio, groups: [] };
  const rootCs = getComputedStyle(document.documentElement);
  out.rootVars = {};
  for (const v of ['--typeBaseSize','--typeBaseSpacing','--typeBasePrimary','--typeBaseWeight',
                   '--type-nav-size','--type-nav-weight','--type-nav-tracking','--type-nav-gap',
                   '--header-nav-size','--header-nav-gap']) {
    const val = rootCs.getPropertyValue(v).trim();
    if (val) out.rootVars[v] = val;
  }
  const bodyCs = getComputedStyle(document.body);
  out.body = { fontFamily: bodyCs.fontFamily, fontSize: bodyCs.fontSize,
               fontWeight: bodyCs.fontWeight, letterSpacing: bodyCs.letterSpacing };
  out.theme = (document.documentElement.innerHTML
    .match(/Shopify\.theme\s*=\s*(\{[^}]*\})/) || [])[1] || null;

  for (const sel of SELECTORS) {
    const els = Array.from(document.querySelectorAll(sel));
    const group = { selector: sel, count: els.length, items: [] };
    for (const el of els.slice(0, 8)) {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      // `textContent` is the authored label; if it is mixed case but the element paints
      // uppercase, the capitals come from CSS, not from the Shopify menu title.
      const raw = el.textContent.replace(/\s+/g, ' ').trim();
      group.items.push({
        rawText: raw,
        rawIsUpper: raw.length > 1 && raw === raw.toUpperCase(),
        fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight,
        letterSpacing: cs.letterSpacing, textTransform: cs.textTransform,
        lineHeight: cs.lineHeight, padding: cs.padding, color: cs.color,
        display: cs.display, visible: r.width > 0 && r.height > 0,
        box: { x: Math.round(r.x), y: Math.round(r.y),
               w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10 }
      });
    }
    // Horizontal whitespace actually seen between adjacent painted labels.
    const painted = els.filter(e => {
      const r = e.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && r.top < 260;
    }).sort((a, b) => a.getBoundingClientRect().x - b.getBoundingClientRect().x);
    group.gaps = [];
    for (let i = 1; i < painted.length; i++) {
      const p = painted[i - 1].getBoundingClientRect(), c = painted[i].getBoundingClientRect();
      group.gaps.push(Math.round((c.x - (p.x + p.width)) * 10) / 10);
    }
    if (painted.length) {
      const f = painted[0].getBoundingClientRect();
      const l = painted[painted.length - 1].getBoundingClientRect();
      group.paintedSpan = Math.round((l.x + l.width - f.x) * 10) / 10;
    }
    out.groups.push(group);
  }
  return out;
})()
"""


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Chrome:
    def __init__(self, width, height):
        self.port = free_port()
        self.profile = tempfile.mkdtemp(prefix="hdrqa-")
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
        import http.client
        deadline = time.time() + 45
        last = None
        while time.time() < deadline:
            try:
                # http.client, not urllib: urllib honours HTTP(S)_PROXY, which sends
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
            except Exception as e:
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
            except Exception:
                self.proc.kill()
            shutil.rmtree(self.profile, ignore_errors=True)


def evaluate(ch, expr):
    r = ch.send("Runtime.evaluate", {"expression": expr, "returnByValue": True,
                                     "awaitPromise": True})
    if r.get("exceptionDetails"):
        raise RuntimeError(json.dumps(r["exceptionDetails"])[:600])
    return r["result"].get("value")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--mobile", action="store_true")
    ap.add_argument("--label", required=True)
    ap.add_argument("--selectors", required=True,
                    help="comma-separated CSS selectors to measure")
    ap.add_argument("--click", default=None, help="selector to click before probing")
    ap.add_argument("--settle", type=float, default=2.5)
    ap.add_argument("--shot-height", type=int, default=None,
                    help="crop the screenshot to this many px tall")
    a = ap.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)
    ch = Chrome(max(a.width, 500) + 120, a.height + 140)
    try:
        ch.send("Page.enable")
        ch.send("Runtime.enable")
        ch.send("Emulation.setDeviceMetricsOverride",
                {"width": a.width, "height": a.height, "deviceScaleFactor": 2,
                 "mobile": a.mobile})
        ch.send("Page.navigate", {"url": a.url})
        time.sleep(a.settle)
        if a.click:
            evaluate(ch, "(() => { const e = document.querySelector(%s);"
                         " if (e) { e.click(); return true; } return false; })()"
                     % json.dumps(a.click))
            time.sleep(0.8)

        sels = [s.strip() for s in a.selectors.split(",") if s.strip()]
        data = evaluate(ch, PROBE.replace("__SELECTORS__", json.dumps(sels)))
        data["_meta"] = {"url": a.url, "width": a.width, "mobile": a.mobile,
                         "label": a.label, "clicked": a.click}

        # scale 1, not 2: clip.scale multiplies on top of deviceScaleFactor, so 2 here
        # would emit 4x files.
        clip = {"x": 0, "y": 0, "width": a.width,
                "height": a.shot_height or min(a.height, 900), "scale": 1}
        shot = ch.send("Page.captureScreenshot",
                       {"format": "png", "clip": clip, "captureBeyondViewport": True})
        png = os.path.join(OUTDIR, "%s-%dpx.png" % (a.label, a.width))
        with open(png, "wb") as fh:
            fh.write(base64.b64decode(shot["data"]))

        jsonp = os.path.join(OUTDIR, "%s-%dpx.json" % (a.label, a.width))
        with open(jsonp, "w") as fh:
            json.dump(data, fh, indent=1)
        print(json.dumps(data, indent=1))
        print("\nPNG:  %s\nJSON: %s" % (png, jsonp), file=sys.stderr)
    finally:
        ch.close()


if __name__ == "__main__":
    main()
