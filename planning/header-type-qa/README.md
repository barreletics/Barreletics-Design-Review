# Header type QA — Aug 8 2026

Owner: *“The font in the header is not good or right. Look at the live site, it’s much better.”*

## The reference trap

Two reference sources were wrong and cost time. Both are recorded here so nobody repeats them.

1. **The on-disk theme copy is not the live theme.** `/Users/andrewnehra/barreletics-theme-live-apr2026`
   is a *different theme* from what is published. Published =
   `185687998755` **“Live Barreletics - Brian Go Live”** (Streamline 7.0), confirmed from
   `Shopify.theme` in the storefront HTML. Always measure the storefront.
2. **A normal browser tab lies.** Any browser that has previewed a Shopify draft keeps a
   `preview_theme_id` cookie, so `barreletics.com` silently renders the **draft**. A tab used
   for this task was serving our own QA theme `187144929571` while showing the live URL.
   `probe.py` therefore launches headless Chrome with a throwaway `--user-data-dir`.

A screenshot circulated as “the live header” (small **UPPERCASE** nav, wide tracking,
`Help ▾ / Account / Cart` text actions, coral cart badge) was in fact **one of our own
artifacts** — the labels `Hot Pilates & Yoga Kits` / `Journal` and the text actions exist only
in `docs/Barreletics Home - Definitive-WORKING.html` and our header chrome. Live has
`Grippy Footwear · Apparel · Collaborations · Blog · About Us` in **title case** with icon
actions. Compare `live-desktop-1440px.png` against `ours-BEFORE-desktop-1440px.png`.

## Measured values

See the `*.json` files for full computed output.

| | Live (published) | Ours before | Ours after |
|---|---|---|---|
| Desktop nav | 21.96px / 400 / 0.45px / none / 1.6 · padding 7.5px 15px | 13px / 600 / 1.82px / uppercase | 18px / 400 / 0.45px / none / 1.6 |
| Drawer link | 22px / 400 / normal / none | 15px / 600 | 18px / 400 / normal |
| Family | Roboto 400 | Roboto | Roboto |

Live's sticky nav computes 18.96px; our header is permanently sticky, so 18px is the honest
analogue of the live at-rest 22px.

## 18px vs 22px — owner decision aid (Aug 8, second pass)

Committed default stays **18**. 22 is rendered as a **preview variant only** (`?size=22`).

| Comparison image | Shows |
|---|---|
| `COMPARE-desktop-1440px.png` | ours 18px · ours 22px · live (22px at rest), stacked |
| `COMPARE-mobile-bar-390px.png` | closed bar, 18 vs 22 — identical by design |
| `COMPARE-mobile-drawer-390px.png` | drawer, 18 vs 22 |

Individual full-width shots: `size-18-desktop-1440px.png`, `size-22-desktop-1440px.png`,
`size-{18,22}-mobile-bar-390px.png`, `size-{18,22}-mobile-drawer-390px.png`.
Bar-only crops used by the composites: `band-{18,22}-{desktop,mobile}-*.png`.

### Horizontal room at 1440px

Content box is `max-width: 1200px` minus `2 × 40px` padding = **1120px**, so headroom is
constant for any viewport ≥ 1200px.

| | nav width | headroom, last nav item → utility actions |
|---|---|---|
| 18px | 453.0px | **172.3px** |
| 22px | 521.1px | **137.9px** |

### Where the two groups collide

`.site-header__inner` has a 24px `gap` floor. Free space runs out when
`logo + nav + actions + 2 × 24` exceeds the content box.

| | needs | gap collapses to 24px floor at | horizontal overflow at | nav hidden below |
|---|---|---|---|---|
| 18px | 823.5px | ≤ 900px | ≤ 860px | 768px |
| 22px | 891.6px | ≤ 960px | ≤ 920px | 768px |

So both sizes are clean on desktop and clean on phones; **both** crowd in the 768–960px
tablet band, 22px by about 60px more than 18px. Sweep data: `collision-sweep.json`
(`sweep.py` re-runs it).

### Mobile at 390px

No overflow, no collision, no label wrapping at **either** size:

- The desktop nav does not render below 768px, so `nav_link_size` never paints on the closed
  bar — the two rows are identical, with `Cart` ending at 374px inside a 374px content box.
- Drawer links go 18px → 22px (they follow `--type-nav-size`). Panel is 300px wide; the
  longest label, *Shop All Grippy Shoes*, stays on one line at both sizes.
- With Grippy Shoes expanded on a 390×844 viewport the whole drawer still fits without
  scrolling: last utility item bottoms out at 766.8px (18px) / 788.8px (22px).

## Reproduce

```bash
# live production, clean session
python3 planning/header-type-qa/probe.py --url https://barreletics.com --width 1440 \
  --label live-desktop --selectors ".site-navigation .site-nav__item > .site-nav__link"

# our header, from the real design-tokens.css + chrome.css
python3 planning/header-type-qa/probe.py \
  --url "file://$PWD/planning/header-type-qa/harness.html" --width 1440 \
  --label ours-AFTER-desktop --selectors ".site-header__nav-item > a"
```

`harness.html` mirrors `sections/header.liquid` output with `header-group.json`'s settings and
the reconciled **M4 Menu** labels (`planning/navigation-menu-spec.md` §1) — *Grippy Shoes ·
Apparel · Collaborations · Journal*, not the legacy live-only set. Params: `?before=1` replays
the pre-fix values without reverting any tracked file, `?size=22` previews an alternate nav
size, `?drawer=1` opens the mobile drawer, `?nostrip=1` hides the announcement bar.

`compose.py` builds the `COMPARE-*.png` composites; it halves the 2× captures so rows read at
true CSS pixel size.

## Help action — labelled, Aug 8 (third pass)

Size is **settled at 18px / 400 / title case**. This pass only fixed Help's discoverability.

The branches were inverted: the **correctly configured** state (secondary menu assigned) drew
a bare 18×18 question-mark SVG and ignored `show_action_labels`, while the **misconfigured**
state (no menu) drew a nice "Help ▾" text link pointing at `/pages/help`, which **404s**.
So configuring the header properly made the UI less discoverable.

Now both branches render a label when `show_action_labels` is on and the question-mark icon
when it's off. Help, Account and Cart share one type treatment (14px / 400 / 0.025em, title
case). The dropdown, `aria-label`, and `aria-haspopup` are unchanged.

- **Caret** only on the assigned-menu branch (`.site-header__caret`, 0.8em at 0.7 opacity).
  The fallback has no dropdown, so a caret there would promise a menu that does not exist.
- **Dead link:** fallback repointed to `/pages/faq` (verified **200**; `/pages/help` returns
  **404**) via a single `help_fallback_url` assign. Chosen over suppressing Help entirely
  because a Theme-Editor-added header with no menu yet should still offer a support route —
  suppression would make the "unconfigured" state look intentional and hide the affordance.
- **Mobile drawer:** previously rendered the utility list *only* when a menu was assigned, so
  an unconfigured header left phone users with no support link at all (the desktop Help action
  is hidden below 768px). Now falls back to a single Help → `/pages/faq` item, gated on the
  `show_help` setting so turning Help off still turns it off everywhere.

### Verified with a help menu assigned

| Check | Result |
|---|---|
| Label renders | `Help ▾` beside Account and Cart — `help-label-desktop-1440px.png` |
| Dropdown opens | About Us · FAQ · Contact Us · Returns & Exchanges, right-aligned under Help — `help-dropdown-open-desktop-1440px.png` |
| Collision at 1440px | none. Headroom **167.7px** (was 172.3px with the icon) |
| 390px | Help correctly `display: none`; no horizontal scroll (`scrollWidth` 390 = viewport) |

Headroom moved only 4.6px because `.site-header__action` enforces a 44px min tap target, and
`Help ▾` is narrower than that anyway — the label is free. The actions group grew 183.8 →
192.9px, almost all of it from the cart-badge fix below, not from the Help label.

Updated collision thresholds (`sweep.py`): at 18px the gap floor is reached at ≤900px and
overflow at ≤860px — unchanged. At 22px the floor moved 960 → 980px.

The bar's intrinsic minimum width is now **377px** (was ~368px before the badge fix). At 390px
there is 13px of slack. Below 377px the layout viewport widens rather than clipping, so a
360px Android zooms out very slightly instead of scrolling — pre-existing behaviour, 9px worse
than before, in exchange for the count no longer sitting on the word "Cart".

## Fixed in passing

The inline cart count sat **on top of** the "Cart" label. `.site-header__cart-badge--inline`
declares `position: static`, but the base `.site-header__cart-badge` (`position: absolute`) is
declared ~35 lines *later* at equal specificity, so it won on order. The modifier is now
`.site-header__cart-badge.site-header__cart-badge--inline`. Pre-existing, visible in the
`ours-BEFORE-*` shots, unrelated to type sizing.

## Known, pre-existing, left alone

At 390px the announcement strip still overflows horizontally (`overflow-x: auto`,
`white-space: nowrap`) — untouched.

Both sizes crowd in the 768–960px tablet band (see the table above). A mid-breakpoint would
be the real fix; not attempted here, since it is a layout change rather than a type change.
