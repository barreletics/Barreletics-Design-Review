#!/usr/bin/env python3
"""Extract every image/video/link from shopify-build templates+sections and HTTP-check them."""
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TPL = os.path.join(ROOT, "shopify-build", "templates")
SEC = os.path.join(ROOT, "shopify-build", "sections")
LIVE = "https://barreletics.com"

MEDIA_RE = re.compile(r"https?://[^\s\"'<>)\\]+?\.(?:jpg|jpeg|png|webp|gif|avif|mp4|mov)(?:\?[^\s\"'<>)\\]*)?", re.I)
HREF_RE = re.compile(r"[\"'](/[a-zA-Z0-9][^\s\"'<>{}]*)[\"']")


def head(url, timeout=25):
    try:
        out = subprocess.run(
            ["curl", "-sS", "-o", "/dev/null", "-L", "--max-time", str(timeout),
             "-w", "%{http_code}", "-A", "Mozilla/5.0 (audit)", url],
            capture_output=True, text=True, timeout=timeout + 10)
        return out.stdout.strip() or "ERR"
    except Exception as e:
        return "ERR:" + type(e).__name__


def main():
    media = defaultdict(set)   # url -> set(files)
    links = defaultdict(set)

    targets = []
    for d in (TPL, SEC):
        for dp, _, ns in os.walk(d):
            for n in ns:
                if n.endswith((".json", ".liquid")):
                    targets.append(os.path.join(dp, n))

    for p in sorted(targets):
        rel = os.path.relpath(p, ROOT)
        src = open(p, encoding="utf-8", errors="replace").read()
        for m in MEDIA_RE.findall(src):
            pass
        for m in MEDIA_RE.finditer(src):
            media[m.group(0).replace("\\/", "/")].add(rel)
        for m in HREF_RE.finditer(src):
            u = m.group(1)
            if u.startswith("//") or u.startswith("/cdn/"):
                continue
            if any(c in u for c in "{}"):
                continue
            links[u].add(rel)

    print(f"media urls: {len(media)}  internal links: {len(links)}", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=12) as ex:
        murls = sorted(media)
        mcodes = list(ex.map(head, murls))
        lurls = sorted(links)
        lcodes = list(ex.map(head, [LIVE + u for u in lurls]))

    res = {
        "media": [{"url": u, "code": c, "files": sorted(media[u])} for u, c in zip(murls, mcodes)],
        "links": [{"path": u, "code": c, "files": sorted(links[u])} for u, c in zip(lurls, lcodes)],
    }
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "asset-report.json"), "w"), indent=2)

    print("\n=== MEDIA NOT 200 ===")
    for r in res["media"]:
        if r["code"] != "200":
            print(f"  [{r['code']}] {r['url']}\n        used in: {', '.join(r['files'])}")
    print("\n=== INTERNAL LINKS NOT 200 ===")
    for r in res["links"]:
        if r["code"] != "200":
            print(f"  [{r['code']}] {r['path']}\n        used in: {', '.join(r['files'])}")
    print(f"\nmedia ok: {sum(1 for r in res['media'] if r['code']=='200')}/{len(res['media'])}")
    print(f"links ok: {sum(1 for r in res['links'] if r['code']=='200')}/{len(res['links'])}")


if __name__ == "__main__":
    main()
