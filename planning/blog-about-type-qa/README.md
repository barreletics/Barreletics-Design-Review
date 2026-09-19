# Blog / Article / About — Type OS alignment QA

**Date:** 2026-08-08 · **Authority:** `planning/m4-type-hierarchy.md` + `shopify-build/assets/design-tokens.css` (SETTLED 2026-07-29) 
**Trigger:** owner letter — "the blog and about us font is not correct." 
**Scope:** type alignment only. No redesign, no new scale, no layout moves.

These three surfaces were missed by the 2026-07-31 Type OS pass
(`planning/type-os-audit-2026-07-31.md`) and were still on the pre-Type-OS
`--text-*` legacy aliases with 700-weight headings.

## What was wrong

| File | Drift | Fix |
|---|---|---|
| `sections/blog-listing.liquid` | Mobile `.blog-listing__title: var(--text-3xl)` (32px) overrode `.type-hero` mobile clamp; subtitle 16/1.6; card title on **H2 Standard** (26–32) inside a 3-up card; excerpt 16/1.6; tag 11/**700**/0.04em; meta + page info 11px; author 500; eyebrow flush against H1 (no cadence gap) | Hero/mobile left to `.type-hero`; lede tokens; card title → **H3 role**; body tokens; label tokens; trust 13; `--gap-a` |
| `sections/article-content.liquid` | Same mobile hero override; `.article__body h2` 28/**700**, `h3` 21/**700** (weight rises with size — inverted governing rule); body 16/1.7; `related-title` 28/**700**; `related-name` 16/**700**; category 11/700/0.04em; tag 0.04em; meta/date/share 11px; RTE lists lost their markers to the global reset | H2 Standard / H3 / body / label / trust tokens; `.h2-standard` on Keep Reading; `list-style: revert` + link, `strong`, `blockquote` rules for `article.content` |
| `sections/page-about.liquid` | Same mobile hero override; intro 16/1.7 (should be lede); **manifesto dark band 28px fixed, lh 1.6, ls −0.028em, shrinking to 21px on mobile** instead of the Statement role; value titles 18/**700**; value + USA body 16/1.6; mobile `--text-2xl` override on a heading whose clamp already handles mobile | Lede tokens; `.type-statement` on the blockquote; H3 role on value titles; body tokens; mobile overrides removed |

Common thread: every heading was **700** regardless of size, which inverts the
governing rule (*weight falls as size rises*), and every hero shrank to a flat
32px on mobile instead of the Type OS `clamp(34px, 9vw, 44px)`.

## Verified computed values (after)

`python3 planning/blog-about-type-qa/verify.py`

Hero 72/700/1.06/−0.028em (mobile 35.1) · H2 Standard 32/600/1.22/−0.012em
(mobile 24) · Statement 36/500/1.12/−0.022em (mobile 28) · H3 22/600/1.25 ·
lede 17/400/1.60 · body 16/400/1.72 · label 11/600/0.08em. All Roboto.

## Harness

The three surfaces ship as Liquid, so they cannot be opened in a browser.
`build.py` lifts each section's real `<style>` block out of the `.liquid` file and
wraps it around static markup mirroring the Liquid output, with copy from the
matching `templates/*.json`. Stylesheets are linked live from
`shopify-build/assets`, so a rebuild always reflects the working tree.

```
python3 planning/blog-about-type-qa/build.py --label after
python3 planning/blog-about-type-qa/verify.py --width 390
```

Mobile shots use an iframe inside a wider window — headless Chrome on macOS
clamps windows to 500px (same technique as `planning/mobile-qa/mqa.py`).

Screenshots: `{blog,article,about}-{before,after}-{1440,390}.png`. 
Previews (generated, safe to delete): `preview-{blog,article,about}.html`.

## Open items for the owner

1. **`docs/Barreletics Journal - Definitive-v5.html` (hub-locked) has the same
   drift** — line 360 `.journal-title { font-size: 32px }` on mobile, line 103
   FAQ title tracking −0.028em where H2 Standard is −0.012em, lines 197/234
   uppercase meta at weight 700/500 where the label role is 600. Not touched:
   locked mocks are never edited in place, and a `-v6` would be a hub-authority
   change. Needs a `LOCK THIS` letter if you want the mock brought forward.
2. **`sections/geo-section.liquid`** (on the About page) has hardcoded 12/14px
   accordion UI. Shared with PDP and Collection, so it is not an About-specific
   defect — changing it moves those pages too. Left alone.
3. The About hero band and founder band are `fifty-fifty` (already aligned in the
   July pass); this sweep covered the About-specific `page-about` section.
