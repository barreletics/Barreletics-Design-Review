# Returns · size chart · compare · Free People · reviews — draft-theme 404 fix + QA

---
document: Returns pages QA
version: 1.0
status: Built + locally verified — nothing pushed, nothing committed
date: 2026-08-08
theme: M4 Visual QA `187144929571` (unpublished; push only when Andrew names the ID)
inputs: planning/help-returns-inventory.md (investigation) · live storefront curl · live theme reference /Users/andrewnehra/barreletics-theme-live-apr2026
---

## Why six pages 404'd on the draft

Shopify 404s a page whose assigned **template suffix** does not exist in the active theme.
Those six pages carry suffixes baked into the old live theme years ago — two of them
misspelled — and `shopify-build/` never had files under those names.

Verified with the QA preview cookie on the primary domain (`cdn/shop/t/141` = QA theme):

| Page | Admin suffix (live theme file) | Was | Now renders via |
|---|---|---|---|
| `/pages/returns` | `shipping-retruns` *(typo: "retruns")* | 404 | `templates/page.shipping-retruns.json` |
| `/pages/returns-portal` | `start-a-retrun` *(typo: "retrun")* | 404 | `templates/page.start-a-retrun.json` |
| `/pages/performance-skins-size-chart` | `size-chart` | 404 | `templates/page.size-chart.json` |
| `/pages/compare-open-closed-sole` | `compare-open-vs-closed` | 404 | `templates/page.compare-open-vs-closed.json` |
| `/pages/free-people` | `free-people` | 404 | `templates/page.free-people.json` |
| `/pages/reviews` | `judgeme_all_reviews` | 404 | `templates/page.judgeme_all_reviews.json` |

Suffixes were derived from the live theme's template filenames and confirmed per page by
matching the rendered `shopify-section-template--<id>__<section>` fingerprints back to
those files — not guessed from the URL.

**Approach taken: (a) for all six.** Adding the file Admin already asks for means Andrew
clicks nothing to get a preview. A misspelled filename is invisible to customers and lives
only in the theme. Clean-named aliases were added alongside so the Admin clean-up in
option (b) is a one-dropdown change later, with no second build:

| Typo / legacy name | Clean alias also added | Admin clean-up |
|---|---|---|
| `page.shipping-retruns.json` | — (see returns caveat below) | **do not re-point yet** |
| `page.start-a-retrun.json` | `page.returns-portal.json` | suffix → `returns-portal` |
| `page.size-chart.json` | `page.size-guide.json` (already existed) | suffix → `size-guide` |
| `page.compare-open-vs-closed.json` | `page.compare.json` (already existed) | suffix → `compare` |
| `page.judgeme_all_reviews.json` | `page.reviews.json` | suffix → `reviews` |

## The missing `main-page` section — root cause behind the returns risk

`shopify-build/templates/page.json` (the default page template) referenced section type
`main-page`, and **`sections/main-page.liquid` did not exist in the repo at all**. So the
Design System had no way to render a Shopify page's own body content.

That absence is what pushed the returns templates toward hardcoded copy — and hardcoded
copy is what would have deleted ReturnZap.

`sections/main-page.liquid` is now built: page title (optional) + `{{ page.content }}` in
the design-system frame, with width / background / inset controls, a preset, and styling
scoped so a hand-authored Admin body keeps its own layout. It also repairs the default
`page.json`, which was silently broken for every suffix-less page on the theme.

## 🚨 ReturnZap — the returns portal is Admin body content, not theme code

Fetched and confirmed on the live site:

- `/pages/returns-portal` body is **589 bytes**: an `<h1>` from `page.title`, then
  `<script src="https://portal.returnzap.com/v2.js" async></script>` and
  `<return-zap shop-id="AWfBVmPxpdsnFDKeoeCBpP"></return-zap>`. Nothing else. The entire
  portal is a web component pasted into the Shopify Admin page body.
- `/pages/returns` body is **66 KB** of hand-authored HTML: shipping windows, the $7.95
  flat-rate return fee, 72-hour refund inspection, exchange flow, defect handling, the
  90-day warranty, an FAQ — and **six links into `/pages/returns-portal`**.

**The repo's `page.returns.json` used to describe a different process** — step 1 "Contact
Support — email our support team", "we'll send you a prepaid return label", refunds in
5–7 days, free exchange shipping — and `page-returns.liquid` contained zero links. Shipping
that template as the returns page would have deleted the ReturnZap entry point and
contradicted the live fee and timing on a policy page. **Fixed forward 2026-08-08:** it now
renders `main-page`, and `sections/page-returns.liquid` is deleted.

**Answer to the direct question: yes — the returns and portal templates must render
`{{ page.content }}`, not bespoke section copy.** That is exactly how both are now built
(`main-page`), and it is verified, not assumed:

- `preview-returns-portal.html` contains `<return-zap shop-id="AWfBVmPxpdsnFDKeoeCBpP">`
  plus the portal script, and the widget **actually loaded and rendered its own "Find your
  order" form** in the headless run (`returns-portal-1440px.png`).
- `preview-returns.html` renders all six "Start a Return / Start an Exchange" links
  (`portalLinks: 6` in the audit JSON).

**All four returns templates are rendered here, not just the two named for the Admin
suffix.** Each live page has a suffix-named template and a handle-named one, and either can
be selected from the Admin template dropdown, so both get audited:

| Preview | Template | Live page |
|---|---|---|
| `preview-returns.html` | `page.shipping-retruns.json` | `/pages/returns` |
| `preview-returns-handle-template.html` | `page.returns.json` | `/pages/returns` |
| `preview-returns-portal.html` | `page.start-a-retrun.json` | `/pages/returns-portal` |
| `preview-returns-portal-handle-template.html` | `page.returns-portal.json` | `/pages/returns-portal` |

The two returns renders are byte-identical and the two portal renders are byte-identical, so
the Admin dropdown can no longer produce a page that contradicts the portal.

The returns policy copy itself is not rewritten here. It lives in the Admin page body, which
is the source — that is deliberate, because the ReturnZap embed only exists there.

## Andrew's Admin checklist

Nothing below is required to *preview* — all six render once the theme is pushed. These
are the store-side items no repo change can cover.

1. **Purge pool language from the `/pages/returns` Admin body.** The live body contains
   "tidal pools", "poolside yoga", "Boating and poolside", "Rocky shorelines &
   shell-covered beaches" — all retired by the 2026-08-07 owner letter. Because the
   template now renders the Admin body, this copy shows up on the draft preview as-is.
   Admin → Pages → Shipping & Returns → edit body HTML.
2. **301 the doorway pages** → `/pages/returns`: `/pages/returns-and-exchanges` and
   `/pages/30-day-returns`. Both render the shared legacy doorway template with no returns
   content. Admin → Online Store → Navigation → URL Redirects.
3. **Decide `/pages/reviews`.** Live is Judge.me's full review list; the draft now shows a
   curated `social-proof` section instead. See "Judge.me gap" below.
4. **Decide `/pages/free-people`.** It renders now, but blank — see below.
5. *(Optional, later)* re-point the four clean suffixes in the table above. Admin → Pages →
   [page] → Theme template dropdown.
6. **Do not touch** `/policies/refund-policy` — separate legal surface, referenced at
   checkout.

## Local verification

Harness: `planning/returns-pages-qa/build.py` — renders each template for real (template
JSON in as `section.settings` / `section.blocks`, section Liquid through python-liquid with
snippets resolved from `shopify-build/snippets`, stylesheets linked live out of
`shopify-build/assets`). It validates every section type and every setting key against the
section's `{% schema %}` before rendering, and fails closed if anything is unknown. The
two page-body templates pull the real live Admin bodies so the ReturnZap check is real.

```
python3 planning/returns-pages-qa/build.py            # validate, render, shoot 1440 + 390
python3 planning/returns-pages-qa/build.py --offline   # reuse cached live bodies
```

Screenshots at 1440px and 390px per page, plus a `-fold` crop of the first 1400px.
Mobile width comes from a CDP `Emulation.setDeviceMetricsOverride` — headless Chrome on
macOS clamps windows to 500px, so `--window-size` alone cannot produce 390px.

Result: **0 horizontal overflow and 0 unrendered Liquid** on all six pages at both widths.
Tap targets are clean on five of six; `/pages/returns` reports **19 links under 44px**, all
of them inline links inside the pasted Admin body HTML (its own font sizing), none from a
Design System section. That is another reason to eventually move the returns copy into
`page-returns.liquid` settings. Per-page numbers in `audit-summary.json`.

Preview URLs (static server already running on port 8787, repo root):

- http://127.0.0.1:8787/planning/returns-pages-qa/preview-returns.html
- http://127.0.0.1:8787/planning/returns-pages-qa/preview-returns-portal.html
- http://127.0.0.1:8787/planning/returns-pages-qa/preview-size-chart.html
- http://127.0.0.1:8787/planning/returns-pages-qa/preview-compare-open-vs-closed.html
- http://127.0.0.1:8787/planning/returns-pages-qa/preview-free-people.html
- http://127.0.0.1:8787/planning/returns-pages-qa/preview-reviews.html

`.cache/` holds the two live Admin page bodies fetched verbatim as rendering evidence.
It is a snapshot of live copy — **including the retired pool language** — and is never a
source for new copy.

## Copy law fixed forward on the compare page

`templates/page.compare.json` carried banned wording: *"Full coverage — heel enclosed"*,
*"Enclosed — slightly warmer"*, and a discipline split (*"Best For: Barre, yoga, mat
work"* vs *"Reformer, Lagree, Megaformer"*), plus GEO answers steering reformer users to
Closed and barre users to Open. All of that is retired by `sole-description-language.mdc`
(P-003 / P-013).

Both compare templates now carry the sanctioned wording only: Closed Sole = "Heel and foot
fully covered", Open Sole = "Heel exposed, mid-foot breathing hole. More grounded, barefoot
feel. Natural toe splay", and "Both perform identically — same grip, same stability" with
identical studio uses on both sides. `sections/page-compare.liquid` needed no change — its
schema defaults were already clean.

CTAs point at `/collections/open-sole` and `/collections/closed-sole`, matching the handles
the rest of the repo already uses. Note those collections do not exist in Admin yet, so
they 404 today — as does `/collections/grippy-shoes`, which the template used before.

## Reported, not fixed

**Judge.me gap on `/pages/reviews`.** Live renders `templates/page.judgeme_all_reviews.liquid`,
which calls `{% render 'judgeme_all_reviews' %}` — a snippet the Judge.me app installs into
the theme. `shopify-build/snippets/` has no such file, so a faithful rebuild is impossible
from the repo alone. The new template instead renders the design-system `social-proof`
section with the nine reviews already approved in `templates/index.json`. That is a
different thing from the live page: curated highlights, not the full app-backed review
list. Andrew's call — keep curated, or have Brian add the Judge.me snippet so the app list
renders on the production theme.

**`/pages/free-people` renders blank.** The live page's content lives entirely in
app sections (`ss_hero_15`, `br_variants`, `advanced_content`) — its live template has no
page-body section at all, so there is nothing in `page.content` to render. The template
un-404s the URL and shows the title; there is nothing to visually approve. There is no
Free People mock in `docs/`. Recommend a keep-and-design vs retire-and-301 decision before
any build. No collab hero was invented.

**Returns portal has no navigation entry.** Confirmed again: not in the header, not in the
footer, not in `help-menu`, and zero references to `returns-portal` / `returnzap` anywhere
in `shopify-build/`. The only path is landing on `/pages/returns` and clicking a body
button. Recommended: add **Start a return** to the Help dropdown (fourth item, next to
Returns & Exchanges) and to the footer's support column, both pointing at
`/pages/returns-portal`. The Help menu is the right home — it is the surface customers open
when something is wrong, and it keeps the policy page and the action one click apart
instead of two.

**`docs/Barreletics Returns Portal - Definitive-v1.html` does not describe the live page.**
The mock designs a bespoke order-number + email form plus a separate Track Order form with
a JS toast. The live page is a ReturnZap web component that renders its own UI, including
its own order lookup. Building the mock either replaces ReturnZap outright or has to be
re-skinned around a third-party component that Barreletics does not control. Needs an
explicit decision; the current template deliberately does neither.

**`page-faq.liquid` is three mock versions behind.** The shipping FAQ is a plain
category-grouped accordion — no search field, no topic row. FAQ v5 / v6 / v7 exist only in
`docs/`, and v7 is still awaiting "LOCK THIS". Not rebuilt here, as instructed.

**Eleven more pages 404 on the draft theme** — a full sweep of `sitemap_pages_1.xml`
against the QA theme found more than the six:

| Page | Live template id | Verdict |
|---|---|---|
| `/pages/30-day-returns` · `/pages/returns-and-exchanges` | `26590735368483` | 301 → `/pages/returns` (item 2 above) |
| `/pages/care` · `/pages/sizing` · `/pages/t-shirts-and-tank-top-sizing` · `/pages/yoga-pants-size-guide` · `/pages/yoga-pants-t-shirt-size-guide` · `/pages/data-sharing-opt-out` · `/pages/best-barre-pilates-yoga-grippy-socks` | `26590735368483` | same shared doorway template — renders a hardcoded product landing, no unique content. Needs a keep/301 decision each. `data-sharing-opt-out` may have a legal obligation — check before redirecting. |
| `/pages/sale` | `26590735040803` | own template; keep/retire decision |
| `/pages/shop-performance-skins` | `26590735663395` | own template; keep/retire decision |

Nine of those eleven share one legacy doorway suffix (best match `outdoor` in the live
theme), which is why the group 404s together. Confirm each page's actual suffix in the
Admin template dropdown before acting — the local live-theme copy is an April donor and may
be stale.

**Nine more `main-*` sections are missing from the repo**, the same class of bug as
`main-page`: `main-404`, `main-list-collections`, `main-password`, and the six
`customers/*` templates (`main-account`, `main-login`, `main-register`, `main-addresses`,
`main-order`, `main-activate-account`, `main-reset-password`). Every one of those templates
references a section file that does not exist, so account, login, search-empty and password
pages have no content on the draft theme. Outside this task's surfaces — flagged only.

**Stale setting keys** found while validating: `collection.gift-cards.json`,
`collection.limited-editions.json`, `collection.new-arrivals.json` and
`collection.sale.json` pass `collection` / `products_per_page` / `view_all_url` to
`variant-grid`, and `index.json` passes `bg_color` / `text_color` / `body_color` to
`split-hero`. None of those keys are in the sections' schemas, so they are silently
ignored. Other agents' surfaces — not touched.

## Files added / changed

Added:
- `shopify-build/sections/main-page.liquid`
- `shopify-build/templates/page.shipping-retruns.json`
- `shopify-build/templates/page.start-a-retrun.json` + alias `page.returns-portal.json`
- `shopify-build/templates/page.size-chart.json`
- `shopify-build/templates/page.compare-open-vs-closed.json`
- `shopify-build/templates/page.free-people.json`
- `shopify-build/templates/page.judgeme_all_reviews.json` + alias `page.reviews.json`
- `planning/returns-pages-qa/` (harness, previews, screenshots, audit JSON)

Changed:
- `shopify-build/templates/page.compare.json` — copy law fixed forward (see above)

Untouched on purpose: `templates/page.returns.json`, `sections/page-returns.liquid`,
`sections/page-faq.liquid`, and every file named in the collision-safety list.

No commits. No `shopify theme` commands. No store mutations.
