# Handoff: Barreletics Site Redesign

This bundle is the full output of a multi-week design study for the Barreletics
storefront — audit, exploration, maturation, and final "matured" page designs
for the Home, PDP, Collection, Article, and Blog templates.

It is intended to be opened in **Cursor (or Claude Code)** as the source of
truth for a developer rebuilding the storefront in the live Shopify theme.

---

## About the Design Files

The files in `pages/` are **design references created in HTML, CSS, and a
small amount of vanilla JS / React-via-Babel**. They are prototypes showing
intended look, copy, layout, density, and behavior — **not** production code to
copy directly.

The task on the engineering side is to **recreate these designs inside the
existing Barreletics Shopify theme** (Liquid sections, snippets, the existing
`settings_data.json` schema, the current section-rendering API) using the
theme's established patterns. Do not lift the HTML wholesale; reproduce the
component contracts and tokens defined here, in the Liquid section structure
the theme already uses.

If a section in the design has no equivalent today, add a new Shopify section
with editor-friendly schema (block types, settings) that mirrors the
variations shown in this bundle.

---

## Fidelity

**High-fidelity (hifi).** Every page is a pixel-level mock with final
typography, spacing, color, copy, and component layout. The tokens at the
top of `pages/audit-styles.css` and `pages/maturation-styles.css` are the
canonical design system — match them exactly. Photography is placeholder/CDN
imagery that the brand team will swap in production.

---

## What's in this bundle

```
design_handoff_barreletics/
├── README.md                ← you are here
└── pages/
    ├── Barreletics Audit.html              ← Design audit + token catalog
    ├── Barreletics Wireframes.html         ← Lo-fi structural exploration
    ├── Barreletics Maturation Study.html   ← Current vs. matured comparison
    │
    ├── Barreletics Home - Matured.html     ★ CANONICAL Home
    ├── Barreletics PDP - Matured.html      ★ CANONICAL Product page
    ├── Barreletics Collection - Matured.html ★ CANONICAL Collection page
    │
    ├── Barreletics Article.html            ← Article template
    ├── Barreletics Article 02–06 *.html    ← 5 article variants (founder,
    │                                          Coperni, teacher, retire, barefoot)
    ├── Barreletics Blog.html               ← Blog index template
    │
    ├── Barreletics Home v2…v11.html        ← Exploration history (reference only)
    ├── Barreletics PDP v2.html             ← Earlier PDP exploration
    ├── Barreletics Collection.html         ← Earlier Collection exploration
    ├── Section 15 - Variant Grid v28.html  ← Standalone variant-grid study
    │
    ├── audit-styles.css                    ← PRIMARY token + component stylesheet
    ├── maturation-styles.css               ← Matured-direction stylesheet
    ├── home-matured.css                    ← Home-only matured overrides
    ├── pdp-styles.css                      ← PDP-only styles
    ├── pages-extras.css                    ← Cross-page extras (tab strip, etc.)
    ├── wireframes-styles.css               ← Wireframe stylesheet (lo-fi only)
    ├── section-mocks.css                   ← Section catalog styles
    │
    ├── audit-behavior.js                   ← Vanilla JS for audit chrome
    ├── ticker.js                           ← Announcement-bar rotator
    ├── tweaks-panel.jsx                    ← Tweaks panel host (review tool)
    ├── audit-tweaks.jsx                    ← Audit tweaks
    ├── home-tweaks.jsx                     ← Home tweaks
    ├── pdp-tweaks.jsx                      ← PDP tweaks
    │
    ├── barreletics-logo.png                ← Wordmark
    └── barreletics-mark.png                ← Favicon mark
```

The three `* - Matured.html` files are the **final direction**. All other
home/PDP/collection versions are kept as exploration history — they show what
was tried and rejected, which is useful when the build runs into a tradeoff
that's already been thought through.

The `pg-tab-strip` at the top of most pages is a **review aid** (a nav strip
that links between mockups). **Strip it from production output.** It lives in
`pages-extras.css` under the `.pg-tab-strip` class.

Likewise, the **Tweaks panel** (`*-tweaks.jsx` + `tweaks-panel.jsx`) is a
preview-time controls panel for design review. It is not part of the
production site and should not be carried over.

---

## Design Tokens

These are pulled from the live Shopify `settings_data.json` and calibrated
against the live site (the cream/plum palette in settings is dead code; the
real palette is white, ink, light-grey, with a single coral accent).

### Color

| Token | Hex | Usage |
|---|---|---|
| `--br-bg` | `#ffffff` | Page background |
| `--br-alt-bg` | `#f9f9f9` | Soft section background |
| `--br-alt-bg-2` | `#f3f3f3` | Slightly deeper grey (media-text-split) |
| `--br-text` | `#050505` | Primary ink |
| `--br-text-soft` | `#4a4a4a` | Secondary ink |
| `--br-text-mute` | `#8a8a8a` | Tertiary / metadata |
| `--br-line` | `#e6e6e6` | Hairline borders |
| `--br-line-soft` | `#efefef` | Softer hairlines |
| `--br-accent` | `#f97250` | **Coral — cart badge ONLY** (restraint is the point) |
| `--br-accent-hover` | `#e85e3c` | Coral hover |
| `--br-sale` | `#050505` | Sale price is ink-bold, not red |
| `--br-star` | `#fbc02d` | Review stars |
| `--br-info` | `#3a8de8` | Sale banner blue + LE chip |
| `--br-le` | `#3a8de8` | "Limited Edition" chip text |
| `--br-le-bg` | `#eaf3fc` | "Limited Edition" chip background |
| `--br-button` | `#050505` | Primary button fill |
| `--br-button-text` | `#ffffff` | Primary button text |

**Accent discipline:** Do not paint CTAs, headings, or section backgrounds in
`--br-accent`. The coral exists for the cart badge and nothing else. This is
the single biggest correction the matured direction makes to the live site.

### Typography

One family, one ramp: **Roboto** (Google Fonts, weights 300/400/500/600/700),
with `JetBrains Mono` reserved for technical eyebrows and grip-spec captions
on the matured direction only.

| Token | Size | Notes |
|---|---|---|
| `--t-eyebrow` | 12px | UPPERCASE, `letter-spacing: 0.08em`, weight 600 |
| `--t-body-sm` | 14px | Captions, metadata |
| `--t-body` | 16px | Body |
| `--t-body-lg` | 18px | Lede, large body |
| `--t-h6` | 18px | |
| `--t-h5` | 22px | |
| `--t-h4` | 28px | |
| `--t-h3` | 36px | |
| `--t-h2` | 44px | |
| `--t-h1` | 56px | Section opener |
| `--t-display` | 72px | Hero |
| `--t-h1-mobile` | 36px | clamp() floor for hero |
| `--t-display-mobile` | 44px | clamp() floor for display |

### Spacing scale

```
--sp-1: 4px   --sp-2: 8px   --sp-3: 12px   --sp-4: 16px   --sp-5: 24px
--sp-6: 32px  --sp-7: 48px  --sp-8: 64px   --sp-9: 96px   --sp-10: 128px
```

### Buttons

One primary, one secondary, one tertiary. No drop shadows, no gradients,
no rounded corners.

```
--btn-text-size: 14px;
--btn-pad-y:     14px;
--btn-pad-x:     28px;
--btn-radius:    0px;    /* square, matches Shopify "button_style":"square" */
--btn-letter:    0.06em;
--btn-weight:    600;
```

Variants: `primary` = ink fill / white text; `secondary` = ink outline /
ink text on bg; `tertiary` = text + arrow, no border.

### Hairlines & radii

Borders are 1px solid `--br-line`. Cards have **no radius** by default. Where
the matured direction uses radius (rare), it is 2px or 4px — never the
12–16px pill-card look from the live site.

---

## Pages

### 1. Home — `Barreletics Home - Matured.html` ★

**Purpose.** Convert reformer/barre/Pilates practitioners (and gift buyers) by
leading with category leadership ("best grippy shoes") and editorial proof,
not slogan soup.

**Section order (top → bottom).**
1. **Announcement ticker** — 3-slide rotator (promo, USA-made/shipping, social proof). 4s interval, fades.
2. **Header** — Center-logo nav. Left: category links. Right: account + cart with coral dot. Sticky on scroll.
3. **Hero (media split)** — 50/50 split: full-bleed studio image left, eyebrow + H1 + body + 2 CTAs right.
4. **Pillar strip** — 5 horizontal benefits with dot dividers: 360° Grip · Stay Secure · No Sock Fuss · Rinse & Reuse · No Latex / No Silicone.
5. **Why-it-works** — Editorial 50/50 explaining the grip system. Includes interactive sock ⇄ skin toggle on desktop.
6. **Variant grid** — Choose-your-skin: editorial 3-up of Closed Sole / Open Sole / Limited Edition with prices and "Shop →" links.
7. **Coperni + Free People association strip** — Light, restrained logo lockup with a single line of credibility copy. Do **not** scatter collab tiles like v1.
8. **Sock-math** — Dark band, single editorial slogan with one rotating proof line. Not the stacked-claim soup of the live site.
9. **Testimonial** — One editorial proof with citation and a supporting stat row. Not a dense tile wall.
10. **Founder note** — Dark editorial proposal block.
11. **Disciplines index** — Typographic index (barre / reformer / Pilates / Megaformer / Lagree / yoga) with one-line descriptors.
12. **Closing statement** — Restrained newsletter band on dark.
13. **Footer** — Standard Shopify columns.

**Variants explored (history, in `pages/Barreletics Home v2.html` … `v11.html`).**
v2 cinematic · v3 multi-tile · v4 hybrid · v5a Coperni-led · v5b no-collab · v6 editorial · v7 video hero · v8 ed+video · v9 image-led · v10/v11 maturation iterations. **The team chose the matured editorial direction. Build that. The others are decision history.**

---

### 2. PDP — `Barreletics PDP - Matured.html` ★

**Purpose.** Reduce sock-vs-skin objection, convert with confidence.

**Section order.**
1. Ticker + header (same as Home).
2. **Gallery / buy box split** — Sticky buy box on right. Image-stack left.
3. **Variant + size picker** — Closed/Open sole toggle, colorway swatches, size pills, qty stepper, primary CTA + secondary "Add to cart".
4. **Trust row** — Free shipping · 30-day returns · 90-day warranty.
5. **Pillar strip** (shared component).
6. **"Sock vs. skin" comparison** — Editorial 2-col, not a table of red Xs and green checks.
7. **Spec / materials accordion** — Plain text, no icon spam.
8. **Reviews summary + 3 selected quotes** — Plus a single "read all reviews" link. Resist the temptation to ship a full reviews wall on the PDP.
9. **Cross-sell** — 3-up of complementary skins.
10. Footer.

**Key copy rules:** sale price is ink-bold, not red. "Limited Edition" chip uses `--br-le` blue. Free-shipping threshold is `$150` site-wide (the live `$75` is being raised).

---

### 3. Collection — `Barreletics Collection - Matured.html` ★

**Purpose.** Help shoppers choose Closed Sole vs. Open Sole, then pick a colorway.

**Section order.**
1. Ticker + header.
2. **Collection hero** — Eyebrow + H1 + 1 line of intent copy.
3. **Sole-type chooser** — Two big editorial cards (Closed Sole / Open Sole) explaining the use case for each.
4. **Filter row** — Discipline, sole type, colorway, price. Inline, not a sidebar.
5. **Product grid** — 3-up desktop, 2-up tablet, 1-up mobile. Each card: square image, name, sole type, price, swatch row. No badges except "Limited Edition" where applicable.
6. **Editorial break** — One quote/proof tile every 9 cards to break monotony.
7. Footer.

---

### 4. Articles — `Barreletics Article*.html`

Six article templates representing the editorial range:
- `Barreletics Article.html` — Default template
- `02 Founder` — Founder voice, dark headlines, full-bleed portrait
- `03 Coperni` — Collaboration story, image-heavy
- `04 Teacher` — Instructor profile, Q&A blocks
- `05 Retire` — Sock-retirement narrative
- `06 Barefoot` — Discipline-focused

All share: 720px content column, JetBrains Mono eyebrows for section labels,
H2 = 36px, body = 18px, generous 32–48px paragraph spacing, pull-quotes on
hairlines (no quote-marks SVG).

### 5. Blog index — `Barreletics Blog.html`

Editorial card grid. Featured article top (full-width media + 2-col title/dek),
then 2-up cards beneath.

### 6. Audit + Maturation Study + Wireframes (reference)

- **`Barreletics Audit.html`** — The audit that produced this token system. Read it for rationale: why coral is restricted, why slogan soup got cut, why the section count was halved.
- **`Barreletics Maturation Study.html`** — Side-by-side Current vs. Matured for 11 hero moments. Use this to argue any "but the live site does it this way" debate.
- **`Barreletics Wireframes.html`** — Lo-fi blockouts. Useful when discussing IA only.

---

## Interactions & Behavior

| Component | Behavior |
|---|---|
| **Ticker** | 3-slide auto-rotator, 4s interval, opacity crossfade 320ms ease. Pause on hover. `ticker.js`. |
| **Header** | Sticky on scroll. Adds a 1px bottom hairline (`--br-line`) on scroll > 8px. Cart badge dot (`--br-accent`) visible only when items > 0. |
| **Hero CTAs** | Primary: `Shop performance skins` → Collection. Secondary: `See how it grips` → in-page anchor `#why-it-works`. |
| **Sock ⇄ Skin toggle** | Cross-fade between two image states + swap two stat figures. 240ms ease-out. State persists via aria-pressed. |
| **Variant card hover** | Image scales 1.02 over 320ms ease-out. Caption underline draws in. |
| **PDP gallery** | Click thumbnail → swap main. Pinch/double-tap to zoom on touch. Keyboard ←/→ to advance. |
| **PDP size picker** | Size pills toggle aria-pressed; out-of-stock = strikethrough + cursor not-allowed. |
| **Accordion (PDP specs)** | One open at a time. 200ms height transition. |
| **Reviews "Load more"** | Append next 6 reviews; no full pagination. |
| **Collection filter row** | Inline chips, multi-select within a facet, exclusive between facets. URL-syncs via query params. |
| **Article pull-quotes** | Static. No animation. |

**Reduced motion.** All animations gate on `@media (prefers-reduced-motion: no-preference)`. Final state must be visible without animation.

---

## State (storefront)

The site is Shopify. State needed:
- Cart (line items, total) — Shopify cart API.
- Variant selection per product (sole type, colorway, size) — standard Shopify variant routing.
- Filter state on Collection — URL query params, no client state required.
- Ticker slide index — local JS only.
- Sock ⇄ Skin toggle — local JS only.

No app-level state library required.

---

## Assets

- `barreletics-logo.png` — Wordmark, used in header. Use SVG version from the brand kit in production.
- `barreletics-mark.png` — Favicon + folded "B" mark.
- All photography is **placeholder** — pulled from `barreletics.com/cdn/...` or stand-in CDNs. The brand team will provide final art-directed photography per page before launch.

---

## Out of scope for this handoff

- The `pg-tab-strip` review-only nav (strip it).
- The Tweaks panel + `*-tweaks.jsx` files (review-only).
- The `Audit`, `Maturation Study`, `Wireframes` HTML files — reference docs only.
- The numbered `Home v2…v11` files — exploration history, not the build target.

---

## Suggested implementation order

1. **Tokens first.** Port `audit-styles.css` `:root` variables into the
   theme's `settings_data.json` + `css-variables.liquid` snippet. Verify the
   coral is genuinely confined to the cart badge.
2. **Header + footer.** Centered logo, hairline borders, no shadows.
3. **PDP** — highest-revenue page. Get the variant + size + buy box right
   before anything else.
4. **Home** — section by section, top to bottom. Reuse the PDP buy-CTA
   styles for variant cards.
5. **Collection** — once Home variant cards are built, Collection cards are
   the same component.
6. **Articles + Blog.**
7. **Strip review chrome** (`pg-tab-strip`, tweaks).

---

## Questions for the developer

- Is the theme currently on **Online Store 2.0** (sections everywhere)? The
  designs assume yes. If not, the Home and Collection page templates need to
  be ported to OS 2.0 sections first.
- Confirm the `$150` free-shipping threshold change with the brand team
  before shipping the announcement copy.
- Confirm SKU availability for the **Closed Sole / Open Sole / Limited Edition**
  taxonomy used in the variant grid.
