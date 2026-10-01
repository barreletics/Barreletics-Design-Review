# Partner pages — visual + accessibility QA

**Date:** 2026-08-08 · **Result:** clean at 1440px and 390px after three fixes 
**Surfaces:** `templates/page.{ambassador,studio-program,wholesale,partners}.json`

Repo-only QA. Nothing was pushed to Shopify; no theme command was run.

---

## What the harness does

`build.py` renders each template for real rather than mocking it. It reads
`templates/page.*.json`, feeds the JSON in as `section.settings` / `section.blocks`, and
runs the section Liquid through `python-liquid` with the four Shopify-only constructs
shimmed (`{% schema %}` stripped, `{% form 'contact' %}` → a real `<form>`,
`{% render 'button' %}` inlined, `form.posted_successfully?` forced false). Stylesheets
are linked live out of `shopify-build/assets`, so a preview always reflects the working
tree — edit a section, re-run, re-shoot.

A sticky header stand-in carrying the real `.header-section` / `.site-header` classes sits
above the page so the in-page "Apply" anchors can be checked against sticky chrome.

**Mobile width.** macOS headless Chrome clamps windows to 500px, so 390px comes from a CDP
`Emulation.setDeviceMetricsOverride` on an oversized window rather than `--window-size` —
the same approach as `planning/header-type-qa/probe.py`. Chrome's throwaway profile is
written inside this directory, because the system temp dir is not always writable to the
process running the script.

```
python3 planning/partner-pages-qa/build.py            # render + shoot + audit
python3 planning/partner-pages-qa/build.py --no-shots # audit only
python3 planning/partner-pages-qa/compose.py          # readable contact sheets
```

Requires `python-liquid`, `websocket-client`, `pillow`.

## What it checks

| Check | Method |
|---|---|
| Horizontal overflow | every painted element whose box crosses the viewport edge |
| Tap targets | interactive elements under 44×44, measured on the wrapping `<label>` where one exists, since that is the hit area a finger actually gets |
| Text under 12px | computed `font-size` on elements that paint their own text nodes |
| Sticky overlap | for each `href="#…"`, whether the target's first heading clears the sticky band once `scroll-margin-top` is applied |

---

## Result

| Page | Width | Height | Overflow | Tap < 44px | Text < 12px | Sticky clash |
|---|---|---|---|---|---|---|
| partners | 1440 | 2900 | 0 | 0 | 11 | 0 |
| partners | 390 | 3229 | 0 | 0 | 11 | 0 |
| ambassador | 1440 | 4573 | 0 | 0 | 28 | 0 |
| ambassador | 390 | 6400 | 0 | 0 | 28 | 0 |
| studio-program | 1440 | 3918 | 0 | 0 | 26 | 0 |
| studio-program | 390 | 4947 | 0 | 0 | 26 | 0 |
| wholesale | 1440 | 4392 | 0 | 0 | 33 | 0 |
| wholesale | 390 | 5746 | 0 | 0 | 33 | 0 |

**Every remaining "text < 12px" hit is the Type OS label role** — eyebrows, form field
labels, and fieldset labels at 11px / uppercase / 0.08em, which is the settled
`--fs-label` token and matches `page-contact.liquid` across the rest of the theme. No
sentence-case paragraph copy renders below 13px.

## Fixes this pass found and applied

1. **Checkbox rows were 21–41.6px tall** — under the 44px floor on the wholesale sales-channel
   and product-interest lists, the studio styles-of-interest list, and both consent
   checkboxes. Gave `.page-*__check` and `.page-*__consent` `min-height: 44px` plus vertical
   padding, so the whole label is the hit area.
2. **Hero CTAs jumped under the sticky header at 390px.** `#ambassador-apply`,
   `#studio-apply`, and `#wholesale-apply` put the form heading 48px below the section top
   against a 57px sticky band. Added `scroll-margin-top: 96px`, scoped inside each section's
   own `<style>` so no shared asset is touched.
3. **11px sentence-case fine print.** Terms notes, field hints, pricing notes, and consent
   text were using `--text-sm`, which resolves to the 11px *label* token. Moved to
   `--type-trust-size` (13px), the token the theme already uses for fine print. Uppercase
   micro-labels stay at 11px to match the rest of the theme.

## Known deviation, not fixed here

`contact-cta.liquid` hardcodes `32px/700`, `15px`, and `11px/700` instead of Type OS tokens.
It is a shared section used by FAQ and other pages, so changing it is a sitewide type change
that belongs to whoever owns that section — flagged, not touched.

## Files

- `build.py` — renderer, screenshotter, auditor
- `compose.py` — contact sheets from the full-page shots
- `preview-*.html` — rendered pages, openable directly in a browser
- `<page>-<width>px.png` — full-page screenshots
- `<page>-<width>px.json` — per-page audit detail
- `_sheet-<page>-<width>.jpg` — sliced contact sheets for review
- `audit-summary.json` — the table above, machine-readable
