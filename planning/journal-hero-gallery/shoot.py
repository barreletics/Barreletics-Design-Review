#!/usr/bin/env python3
"""
Journal / blog hero gallery — crop the hero (masthead) of every Journal, blog and
article mock that has existed in this repo so they can be compared side by side.

Read-only: target mocks are never written to. Mock-only scaffolding (the
`.pg-tab-strip` version switcher that sits above the design in the May 2026
handoff files) is hidden with injected CSS at render time so the crops start on
the real page chrome.

Why CDP rather than `--window-size`: headless Chrome on macOS clamps its window
to a 500px minimum, so a 390px window silently renders at 500px.
`Emulation.setDeviceMetricsOverride` gives a real viewport at any width. Same
approach as `planning/header-type-qa/probe.py`.

Usage:
    python3 planning/journal-hero-gallery/shoot.py            # all targets, 1440 + 390
    python3 planning/journal-hero-gallery/shoot.py --only journal-v5
"""

import argparse
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
import urllib.parse

import websocket  # websocket-client

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTDIR = os.path.join(REPO, "planning", "journal-hero-gallery", "crops")

HANDOFF = "barreletics-design-review/design_handoff_barreletics 2/pages"
GALLERY_SRC = "planning/journal-hero-gallery/sources"

# `end` is the last element the hero crop should contain. For the index pages that
# is the featured-post card, which is what reads as the hero band; for the article
# templates it is the hero image itself.
TARGETS = [
    {
        "key": "01-legacy-blog",
        "title": "Legacy Blog.html — May 2026 handoff",
        "path": "%s/Barreletics Blog.html" % HANDOFF,
        "end": ".pg-feature",
        "mobile": True,
    },
    {
        "key": "02-legacy-article",
        "title": "Legacy Article.html — May 2026 handoff",
        "path": "%s/Barreletics Article.html" % HANDOFF,
        "end": ".pg-article-hero",
        "mobile": True,
    },
    {
        "key": "03-journal-v1",
        "title": "Journal Definitive-v1",
        "path": "%s/Journal-Definitive-v1.html" % GALLERY_SRC,
        "end": "article.feature",
        "mobile": False,
    },
    {
        "key": "04-journal-v2",
        "title": "Journal Definitive-v2",
        "path": "%s/Journal-Definitive-v2.html" % GALLERY_SRC,
        "end": "article.feature",
        "mobile": False,
    },
    {
        "key": "05-journal-v3",
        "title": "Journal Definitive-v3",
        "path": "%s/Journal-Definitive-v3.html" % GALLERY_SRC,
        "end": "article.feature",
        "mobile": False,
    },
    {
        "key": "06-journal-v4",
        "title": "Journal Definitive-v4",
        "path": "docs/Barreletics Journal - Definitive-v4.html",
        "end": "article.feature",
        "mobile": False,
    },
    {
        "key": "07-journal-v5",
        "title": "Journal Definitive-v5 (hub Locked)",
        "path": "docs/Barreletics Journal - Definitive-v5.html",
        "end": "article.feature",
        "mobile": True,
    },
    {
        "key": "08-journal-v6",
        "title": "Journal Definitive-v6 (footer fix)",
        "path": "docs/Barreletics Journal - Definitive-v6.html",
        "end": "article.feature",
        "mobile": True,
    },
    {
        "key": "09-shipping-blog",
        "title": "Shipping blog-listing.liquid",
        "path": "planning/blog-about-type-qa/preview-blog.html",
        "end": ".blog-listing__grid .article-card:first-child, .blog-listing__grid > *:first-child",
        "mobile": True,
    },
    {
        "key": "10-shipping-article",
        "title": "Shipping article-content.liquid",
        "path": "planning/blog-about-type-qa/preview-article.html",
        "end": ".article__hero-image",
        "mobile": True,
    },
]

# Version-switcher chrome that only exists so a reviewer can hop between mock files.
HIDE_CSS = (".pg-tab-strip, .mock-banner, .qa-strip, .mock-strip "
            "{ display: none !important; }")

MEASURE = r"""
(() => {
  const sels = __END__;
  let el = null;
  for (const s of sels) { el = document.querySelector(s); if (el) break; }
  if (!el) return { error: 'no end element', tried: sels };
  const r = el.getBoundingClientRect();
  const bottom = r.bottom + window.scrollY;
  return {
    bottom: Math.ceil(bottom),
    docWidth: document.documentElement.clientWidth,
    matched: el.className || el.tagName
  };
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
        self.profile = tempfile.mkdtemp(prefix="jhg-")
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
                # http.client, not urllib: urllib honours HTTP(S)_PROXY, which sends
                # loopback DevTools requests to a proxy that cannot answer them.
                conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
                conn.request("GET", "/json/list")
                raw = conn.getresponse().read()
                conn.close()
                for t in json.loads(raw):
                    if t.get("type") == "page":
                        self.ws = websocket.create_connection(
                            t["webSocketDebuggerUrl"], timeout=60,
                            max_size=128 * 1024 * 1024)
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


def file_url(rel):
    return "file://" + urllib.parse.quote(os.path.join(REPO, rel))


def shoot(target, width, mobile, settle):
    abspath = os.path.join(REPO, target["path"])
    if not os.path.exists(abspath):
        return {"key": target["key"], "width": width, "error": "missing file"}

    ch = Chrome(max(width, 520) + 140, 1100)
    try:
        ch.send("Page.enable")
        ch.send("Runtime.enable")
        ch.send("Emulation.setDeviceMetricsOverride",
                {"width": width, "height": 1000, "deviceScaleFactor": 2,
                 "mobile": mobile})
        ch.send("Page.addScriptToEvaluateOnNewDocument", {
            "source": "document.addEventListener('DOMContentLoaded', () => {"
                      " const s = document.createElement('style');"
                      " s.textContent = %s; document.head.appendChild(s); });"
                      % json.dumps(HIDE_CSS)})
        ch.send("Page.navigate", {"url": file_url(target["path"])})
        time.sleep(settle)

        sels = [s.strip() for s in target["end"].split(",") if s.strip()]
        m = evaluate(ch, MEASURE.replace("__END__", json.dumps(sels)))
        if not m or m.get("error"):
            return {"key": target["key"], "width": width,
                    "error": "end selector not found: %s" % target["end"]}

        # Remote images may 404 offline; report so a blank block is not read as design.
        broken = evaluate(ch, "Array.from(document.images)"
                              ".filter(i => i.complete && i.naturalWidth === 0)"
                              ".map(i => i.currentSrc || i.src).slice(0, 6)") or []

        height = min(m["bottom"] + 28, 6000)
        # scale 1, not 2: clip.scale multiplies on top of deviceScaleFactor.
        shot = ch.send("Page.captureScreenshot",
                       {"format": "png",
                        "clip": {"x": 0, "y": 0, "width": width,
                                 "height": height, "scale": 1},
                        "captureBeyondViewport": True})
        os.makedirs(OUTDIR, exist_ok=True)
        png = os.path.join(OUTDIR, "%s-%dpx.png" % (target["key"], width))
        with open(png, "wb") as fh:
            fh.write(base64.b64decode(shot["data"]))
        return {"key": target["key"], "title": target["title"],
                "source": target["path"], "width": width, "heroHeight": height,
                "png": os.path.relpath(png, REPO), "brokenImages": broken}
    finally:
        ch.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None, help="substring match on target key")
    ap.add_argument("--settle", type=float, default=3.0)
    ap.add_argument("--no-mobile", action="store_true")
    a = ap.parse_args()

    results = []
    for t in TARGETS:
        if a.only and a.only not in t["key"]:
            continue
        r = shoot(t, 1440, False, a.settle)
        results.append(r)
        print(json.dumps(r), file=sys.stderr)
        if t["mobile"] and not a.no_mobile:
            r = shoot(t, 390, True, a.settle)
            results.append(r)
            print(json.dumps(r), file=sys.stderr)

    manifest = os.path.join(os.path.dirname(OUTDIR), "manifest.json")
    with open(manifest, "w") as fh:
        json.dump(results, fh, indent=1)
    print(manifest)


if __name__ == "__main__":
    main()
