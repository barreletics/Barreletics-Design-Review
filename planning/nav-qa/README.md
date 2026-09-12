# Navigation QA — M4 header + footer

Evidence for the M4 navigation sign-off, 2026-08-08. Everything here is QA only; nothing
in this folder ships. The Admin steps that make the nav live are in
`planning/navigation-menu-spec.md` §0.

## Run it

```
python3 planning/nav-qa/audit.py        # header behaviour + geometry, exits 1 on defect
python3 planning/nav-qa/link-check.py   # every internal href the theme ships
```

`audit.py` needs Chrome at `/Applications/Google Chrome.app` and the `websocket-client`
package. `link-check.py` shells out to `curl` and hits the storefront.

## What each file is

| File | What it is |
|---|---|
| `harness.html` | `sections/header.liquid`'s markup with the complete reconciled M4 Menu and Help menu, wired to the real `design-tokens.css` / `chrome.css` / `chrome.js`. Behaviour is the shipped script, so the accordion and drawer are exercised rather than simulated. |
| `footer-harness.html` | `sections/footer.liquid`'s fallback-column output, for reading the repointed link targets and confirming the frozen composition. |
| `audit.py` | Drives the harness at 390 / 768 / 1024 / 1440 plus a 769→1024 sweep. Writes `report.json` and the `nav-*.png` shots. |
| `link-check.py` | Extracts hrefs from the shipped section files (Liquid comments stripped) and requests each. Writes `link-check.json`. |
| `report.json` | Full measurements — dropdown rects, drawer tap-target heights, sweep results. |
| `link-check.json` | Status code per URL, split into live / pending-Admin. |
| `nav-<w>px-bar.png` | Header bar at that width. |
| `nav-<w>px-grippy-open.png` / `-help-open.png` | Dropdowns open (desktop widths only). |
| `nav-<w>px-drawer-expanded.png` | Drawer with both accordions expanded (drawer widths only). |
| `footer-<w>px.png` | Footer at that width. |

## What the audit asserts

- Grippy Shoes (5 children) and Apparel (3) open on hover and keyboard focus, land under
  their parent, stay inside the viewport, and every row survives a hit test — so a clipped
  or covered dropdown fails the run.
- Collaborations and Journal render no `<ul>` and no `--has-sub` class: no empty dropdown.
- Help ▾ opens on desktop and its four items appear in the drawer on mobile.
- The drawer's parents are collapsed until tapped, then expand inline with `aria-expanded`
  tracking; Escape closes and unlocks body scroll.
- Every interactive drawer row is ≥44px.
- No horizontal overflow and no region collision at any tested width.

## Defects this caught

The header row needs ~873px for logo + four title-case 18px labels + Help/Account/Cart,
but the drawer only took over at 768px — so 769–865px pushed the whole page into
horizontal scroll. The breakpoint moved to 900px in `assets/chrome.css`. The approved type
values (18px / 400 / 0.025em / title case) were not touched.
