#!/usr/bin/env python3
"""SEO v37 Juicer-section QA shots — 1440px desktop and a true 390px mobile.

Headless Chrome on macOS clamps windows to ~500px wide, and this page has
vh-sized neighbours, so neither `--window-size=390,...` nor the tall-iframe
trick gives an honest mobile render. This drives Chrome over CDP instead:
Emulation.setDeviceMetricsOverride pins a real 390x844 mobile viewport, then
Page.captureScreenshot clips to the measured Juicer box with
captureBeyondViewport so the whole section comes out in one shot.

Also reports horizontal overflow and any image that failed to load, at both
widths.

The page is served over http on :8787 so the real juicer.io embed runs, exactly
as it does in the theme.

Usage:  python3 planning/seo-v37-qa/shoot.py
"""

import base64
import json
import os
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request

import websocket

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAGE = ("http://localhost:8787/docs/"
        "Barreletics%20SEO%20-%20Best%20Grippy%20Socks%20-%20Definitive-v37.html")

MEASURE_JS = r"""
(() => {
  const s = document.getElementById('instagram');
  const r = s.getBoundingClientRect();
  const cs = getComputedStyle(s);
  const clientW = document.documentElement.clientWidth;
  const title = s.querySelector('.home-juicer__title');
  return {
    top: Math.round(r.top + window.scrollY),
    left: Math.round(r.left + window.scrollX),
    width: Math.round(r.width),
    height: Math.ceil(r.height),
    classes: s.className,
    eyebrow: (s.querySelector('.home-juicer__eyebrow') || {}).textContent || null,
    heading: title ? title.textContent : null,
    body: (s.querySelector('.home-juicer__body') || {}).textContent || null,
    seeMore: !!s.querySelector('.home-juicer__see-more'),
    cta: ((s.querySelector('.home-juicer__cta') || {}).textContent || '').trim(),
    padding: cs.padding,
    background: cs.backgroundColor,
    titleFontSize: title ? getComputedStyle(title).fontSize : null,
    titleWeight: title ? getComputedStyle(title).fontWeight : null,
    liveFeed: s.classList.contains('is-juicer-live'),
    liveTiles: s.querySelectorAll('.juicer-feed li, .juicer-feed .j-stacker > *').length,
    fallbackTiles: s.querySelectorAll('.home-juicer__fallback-card').length,
    viewport: clientW,
    docScrollWidth: document.documentElement.scrollWidth,
    horizontalOverflow: document.documentElement.scrollWidth > clientW + 1,
    overflowing: Array.from(document.querySelectorAll('body *')).filter(el => {
      const b = el.getBoundingClientRect();
      return b.width > 0 && b.right > clientW + 1;
    }).slice(0, 15).map(el => el.tagName.toLowerCase() + '.' +
        String(el.className || '').split(' ')[0] +
        ' right=' + Math.round(el.getBoundingClientRect().right)),
    imageCount: document.images.length,
    brokenImages: Array.from(document.images)
      .filter(i => i.complete && i.naturalWidth === 0)
      .map(i => i.currentSrc || i.src)
  };
})()
"""

VIEWS = [
    ("1440px", {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False}),
    ("390px", {"width": 390, "height": 844, "deviceScaleFactor": 1, "mobile": True}),
]


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Chrome:
    def __init__(self):
        self.port = free_port()
        self.profile = tempfile.mkdtemp(prefix="seo-v37-qa-")
        self.proc = subprocess.Popen(
            [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--hide-scrollbars", "--remote-debugging-port=%d" % self.port,
             "--remote-allow-origins=*",
             "--user-data-dir=" + self.profile, "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.ws = websocket.create_connection(self._target(), timeout=90)
        self.msg = 0

    def _target(self):
        for _ in range(100):
            try:
                data = json.load(urllib.request.urlopen(
                    "http://127.0.0.1:%d/json/list" % self.port, timeout=2))
                for t in data:
                    if t.get("type") == "page":
                        return t["webSocketDebuggerUrl"]
            except Exception:
                pass
            time.sleep(0.2)
        raise RuntimeError("chrome devtools never came up")

    def send(self, method, params=None):
        self.msg += 1
        self.ws.send(json.dumps({"id": self.msg, "method": method,
                                 "params": params or {}}))
        while True:
            m = json.loads(self.ws.recv())
            if m.get("id") == self.msg:
                if "error" in m:
                    raise RuntimeError("%s: %s" % (method, m["error"]))
                return m.get("result", {})

    def evaluate(self, expr):
        r = self.send("Runtime.evaluate",
                      {"expression": expr, "returnByValue": True,
                       "awaitPromise": True})
        return r["result"].get("value")

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass
        self.proc.terminate()
        try:
            self.proc.wait(timeout=10)
        except Exception:
            self.proc.kill()
        shutil.rmtree(self.profile, ignore_errors=True)


def capture(c, label, metrics):
    c.send("Emulation.setDeviceMetricsOverride", metrics)
    c.send("Page.enable")
    c.send("Page.navigate", {"url": PAGE})
    # The Juicer embed is a third-party fetch; poll instead of guessing a wait.
    for _ in range(60):
        time.sleep(0.5)
        state = c.evaluate(
            "document.readyState === 'complete' && "
            "!!document.getElementById('instagram') && "
            "document.getElementById('instagram').classList.contains('is-juicer-live')")
        if state:
            break
    time.sleep(2.5)
    m = c.evaluate(MEASURE_JS.strip())
    shot = c.send("Page.captureScreenshot", {
        "format": "png",
        "captureBeyondViewport": True,
        "clip": {"x": m["left"], "y": m["top"], "width": m["width"],
                 "height": m["height"], "scale": 1},
    })
    out = os.path.join(HERE, "juicer-%s.png" % label)
    with open(out, "wb") as fh:
        fh.write(base64.b64decode(shot["data"]))
    m["file"] = os.path.basename(out)
    return m


if __name__ == "__main__":
    c = Chrome()
    report = {}
    try:
        for label, metrics in VIEWS:
            m = capture(c, label, metrics)
            report[label] = m
            print("== %s ==" % label)
            print(json.dumps(m, indent=2))
    finally:
        c.close()
    with open(os.path.join(HERE, "audit.json"), "w") as fh:
        json.dump(report, fh, indent=2)
