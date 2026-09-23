# Lock-candidate QA — Type OS cleanup on four unlocked mocks

**Date:** 2026-08-08 · **Status:** candidates cleaned, awaiting owner `LOCK THIS` letter

These four files are **new, unlocked candidates** created earlier this session with the retired
newsletter discount copy purged. They were copied from older locked mocks and inherited
pre-Type-OS typography drift. This pass fixes the drift **in the candidates only**.

| Candidate | Derived from (LOCKED — untouched) |
|---|---|
| `docs/Barreletics Collection - Definitive-v19.html` | Collection v18 |
| `docs/Barreletics SEO - Best Grippy Socks - Definitive-v37.html` | SEO v36 |
| `docs/Barreletics Journal - Definitive-v6.html` | Journal v5 |
| `docs/Barreletics Help - Definitive-v4.html` | Help v3 |

No locked original was read-modified. No file in `shopify-build/` was touched. No PDP mock was
touched. Nothing was restored from an older commit. `docs/index.html` hub cards are unchanged —
promotion remains the owner's call.

---

## Authority

`planning/m4-type-hierarchy.md` + `shopify-build/assets/design-tokens.css`.
Governing rule: **weight falls as size rises.**

| Role | Size | Weight | LH | Tracking |
|---|---|---|---|---|
| Hero | `clamp(50px, 6.4vw, 72px)` | 700 | 1.06 | −0.028em |
| H2 Standard | `clamp(26px, 2.9vw, 32px)` | 600 | 1.22 | −0.012em |
| Statement | `clamp(28px, 3vw, 36px)` | 500 | 1.12 | −0.022em |
| H3 | 22px | 600 | 1.25 | — |
| Lede / Body | 17px / 16px | 400 | 1.60 / 1.72 | — |
| Label / eyebrow | 11px | 600 | — | 0.08em |

Footer newsletter heading authority is `docs/footer-join-the-list-LOCK.html`:
`clamp(22px, 2.5vw, 28px)` / 400 / 1.15 / −0.02em.

---

## How this was verified

Measured, not read. `probe.py` renders each candidate inside a fixed-width iframe and reads
`getComputedStyle` back out of the frame. Headless Chrome on macOS clamps the browser window to a
500px minimum, so the iframe is what makes 390px a genuine 390px viewport.

```
python3 planning/lock-candidate-qa/probe.py --tag before --shots
python3 planning/lock-candidate-qa/probe.py --tag after  --shots
```

Artifacts: `measurements-before.json`, `measurements-after.json`, and
`<page>-<before|after>-<1440|390>px.png`.

`sweep_labels.py` is a second, independent check: it walks every uppercase rule at ≤12px in all four
files and reports which are still at weight 700/500, separating rules whose class actually appears
in the body from dead CSS. It caught one live label (`.sock-math-col__label` in SEO v37) that the
selector-list probe did not cover. Re-run it after any future edit:

```
python3 planning/lock-candidate-qa/sweep_labels.py
```

It now reports only CTAs/buttons and the header trust strip, both intentionally out of scope.

---

## Result summary

All live headings in all four candidates now resolve to role tokens at both widths.

**At 1440px** — Hero `72 / 700 / 76.32 (1.06) / −2.016 (−0.028em)` · H2 Standard
`32 / 600 / 39.04 (1.22) / −0.384 (−0.012em)` · Statement `36 / 500 / 40.32 (1.12) / −0.792 (−0.022em)`
· labels `11 / 600`.

**At 390px** — Hero `38 / 700 / 40.28 / −1.064` · H2 Standard `24 / 600 / 29.28 / −0.288` ·
Statement `28 / 500 / 31.36 / −0.616` · labels `11 / 600`.

All four candidates now measure **identically** for hero, H2, statement, label and footer heading.

---

## Per file

### Collection v19

| What was wrong | Before → After (1440) | Before → After (390) |
|---|---|---|
| `.coll-hero__title` declared `letter-spacing` **twice** — `var(--ls-hero)` then a stray `-0.03em` that won | ls −2.16 → **−2.016** | ls −1.14 → **−1.064** |
| Six H2 Standard titles used correct size/weight vars but hardcoded hero tracking `-0.028em` and LH 1.12/1.15 | ls −0.896 → **−0.384**, lh 35.84/36.8 → **39.04** | ls −0.784/−0.728 → **−0.288**, size 28/26 → **24** |
| `.disciplines-proof__headline` was an off-role `clamp(28px,3.5vw,40px)` at weight **400** | 40px/400 → **36px/500**, ls −1.12 → **−0.792** | 26px/400 → **28px/500** |
| `.dp-item__discipline` eyebrow at weight **700** | 700 → **600** | 700 → **600** |
| Footer `.fn-signup h2` pinned flat **28px** — no mobile downscale at all | 28/400 lh 42 → **28/400 lh 32.2** | **28px → 22px** |
| Mobile H2 overrides pinned flat 26/28px, ignoring the file's own unused `--fs-h2-standard-mobile` | — | now **24px** uniformly |

10% purge: **held.**

### SEO — Best Grippy Socks v37

| What was wrong | Before → After (1440) | Before → After (390) |
|---|---|---|
| **`.hero-fullbleed__title` at weight 400** — the page's largest element, three roles light of the Hero spec, and the only one of the four candidates not at 700 | **400 → 700**, ls −2.16 → −2.016, lh 77.76 → **76.32** | **400 → 700**, lh 41.04 → **40.28** |
| Seven H2 Standard titles hardcoded `-0.028em` + LH 1.12/1.15 | ls −0.896 → **−0.384**, lh → **39.04** | 26/28px → **24px** |
| `.faq-head__title` had **no** tracking or LH at all — inherited body 1.5 | lh 48 (1.5) → **39.04 (1.22)**, ls normal → **−0.384** | lh 39 → **29.28** |
| `.sock-math-col__label` — a live 11px/0.08em label at weight **700** | 700 → **600** | 700 → **600** |
| Footer `.fn-signup h2` pinned flat **28px** | lh 42 → **32.2** | **28px → 22px** |
| Only `.split-text h2` had a mobile override; the rest fell to the 26px clamp floor | — | all H2s now **24px** |

10% purge: **held.**

### Journal v6 — the file Agent B flagged

| What was wrong | Before → After (1440) | Before → After (390) |
|---|---|---|
| **`.journal-title` pinned to flat `32px` on mobile**, overriding the hero clamp, while the file defined `--fs-hero-mobile` and never used it — the reported bug | 72/700 unchanged | **32px → 38px**, lh 33.92 → **40.28**, ls −0.896 → **−1.064** |
| A blanket rule applied `400 / -0.028em / 1.15` to five unrelated headings at once — the root cause of the whole file's drift. Reduced to `font-family` only; each heading now carries its real role | — | — |
| `.feature__title` was statement-sized (`clamp(28px,3vw,36px)`) but weight **400** with hero tracking | 36/400 → **36/500**, ls −1.008 → **−0.792**, lh 41.4 → **40.32** | 28/400 → **28/500** |
| `.article-card__title` H3 at weight **400**, LH inherited | 22/400 lh 25.3 → **22/600 lh 27.5 (1.25)** | same |
| `.variants-head__title` ("Shop all colors & styles" — Standard per the homepage audit) was an ad-hoc `clamp(28px,3.2vw,36px)` at 400 | → **32/600/39.04/−0.384** | → **24px** |
| `.journal-faq h2` hardcoded `-0.028em`, LH inherited body 1.6 | lh 51.2 → **39.04**, ls −0.896 → **−0.384** | lh 41.6 → **29.28**, 26px → **24px** |
| `.journal-eyebrow` **700**, `.feature__meta` **700**, `.article-card__meta` **500** — same role, two different weights inside one file | all → **600** | all → **600** |
| Footer `.fn-signup h2` tracking −0.028em vs lock's −0.02em | ls −0.784 → **−0.56** | ls −0.616 → **−0.44** |

10% purge: **held.**

### Help v4

| What was wrong | Before → After (1440) | Before → After (390) |
|---|---|---|
| `.page-eyebrow` at **700** | 700 → **600** | 700 → **600** |
| `.hub-card__label` at **700** | 700 → **600** | 700 → **600** |
| Footer `.fn-signup h2` used **H2 Standard tokens (32px/600)** — a different role from the other three candidates and from the footer lock | 32/600/−0.64 → **28/400/−0.56** | 26/600 → **22/400** |

10% purge: **held.** Hero and mobile hero were already correct.

---

## 10% purge verification

Grepped all four for `10%`, `first pair`, `first order`, and the copy-law banned terms.

- **No customer-facing discount copy survives.** All four footers read `Join the list` +
  "New drops… never spam." — no discount, no brand blurb.
- No banned location terms present.
- The only `10%` occurrences are Agent A's build annotations inside `<title>`, e.g.
  `Barreletics Collection — Definitive-v19 (footer 10% purge)`. Not customer copy, and not the
  phrase "10% off". **Left as-is** because it is the owner's file-labelling. Worth renaming before
  promotion, since the title renders in the browser tab.

---

## Not changed — deliberate, listed for the owner

**Header territory.** `.site-nav__*` and `.trust-strip__*` were left alone in all four files; a
separate agent is working header typography and touching them here would collide.

**CTAs and buttons.** `.fn-btn`, `.split-cta`, `.pose-band__cta`, `.hero-fullbleed__cta` etc. stay
at 700 uppercase. The type hierarchy treats "quiet uppercase UI" as its own casing row with no
weight spec, so these are not label-role violations.

**Dead CSS.** These rules still carry old values but render nothing — their sections are not in the
body, confirmed by measurement (`MISSING`) and by grep:
Collection `.coll-hero__eyebrow` `.sole-card__tag` `.sole-card__title` ·
SEO `.seo-problem-line__title` `.discipline-film__line` `.disciplines-proof__headline`
`.dp-item__discipline` `.hero-fullbleed__eyebrow` `.coll-hero__title` ·
Journal `.journal-geo__eyebrow` · Help `.page-cta__title`.
Left untouched to keep the diff reviewable. Anything re-enabled from these needs a type pass first.

**Minor off-role body copy, left alone as design intent rather than drift:**
Help `.page-lede` 16px where the lede role is 17px · SEO `.hero-fullbleed__lede`
`clamp(15px,1.6vw,18px)` · Collection `.coll-hero__body` LH 1.6 where body role is 1.72 ·
Collection `.var-card__name` 18px/700 and Help `.hub-card__title` 18px/500 (small card names,
below the H3 size, so consistent with weight-falls-as-size-rises).

---

## ⚠️ Authority conflict the owner should rule on — BZ-020 vs Type OS

Two of the candidates carry an **in-file banner asserting weight 400**, which directly contradicts
the Type OS role table this pass was told to enforce. This is the single most important finding
here, so flagging rather than burying it.

| Source | Date | Says |
|---|---|---|
| BZ-020 "type calm" — `planning/COLLECTION-WORKING-ENTRY.md`, `planning/SEO-LANDING-ENTRY.md`, `planning/HERO-FULLBLEED.md` | 2026-07-25 · marked **Locked**, "shop-wide BZ-020 balance" | Hero H1 `clamp(40–64)` / **400** · display / section / statement **400** · **700 for CTAs only** |
| Type OS — `planning/m4-type-hierarchy.md` | 2026-07-29 · marked **SETTLED** | Hero **700** / max **72** · H2 Display 500 · H2 Standard 600 · Statement **500** |

The candidates' banners still read `SEO v36 · Locked balance — opening H1 ~64 / 400 title case` and
`Collection v18 — BZ-020 type calm (400 display · Home-sized H1)`.

**I proceeded on Type OS.** The reasoning, so it can be overruled cheaply:

- Type OS is **four days later** and marked SETTLED, and it explicitly raised the hero cap from
  BZ-020's 64 to **72**.
- Its scope section names **`Collection v18` and `SEO v36`** — the exact locked originals these
  candidates came from — as authority mocks it governs.
- The files were already **half-migrated**: Collection's H1 measured `72px / 700` before this pass,
  and SEO's H1 already used the Type OS `--fs-hero` token (72px) while keeping BZ-020's 400 weight.
  That mixed state is what "inherited drift" looks like.
- The task brief for this pass specified Hero 72/700 as the target.

**If BZ-020 is still the ruling decision for these two pages, say so and I will fix forward in a v38
/ v20** — the changes are two declarations. What should *not* stand is the current situation where
the banner and the CSS disagree.

Affected by this specific question:

- **SEO v37 `.hero-fullbleed__title`** — 400 → **700** (also the largest visual change in the pass;
  it noticeably darkens the headline over the dark full-bleed image)
- **Collection v19 `.disciplines-proof__headline`** — 400 → **500**, `clamp(28,3.5vw,40)` → statement clamp

Nothing else in this pass depends on that question — H2 tracking, line-heights, label weights, the
mobile hero pin and the footer heading are all uncontested corrections.

---

## Also stale, not fixed — banner version labels

Agent A did not bump the mock banners when creating the candidates, so each banner names its
predecessor: v19 says "Collection v18", v37 says "SEO v36", v6 says "JOURNAL v4", v4 says "HELP v3".
Left alone because banner text is the owner's labelling, but they should be bumped before promotion
or the hub will show a v19 page announcing itself as v18.

Same for the `<title>` build annotations noted above.

---

## Promotion recommendation

**No candidate should be withheld. Nothing here is blocking.** All four are clean on copy and now
measure on-role at both widths.

Before a `LOCK THIS` letter, two things want the owner's eyes on the `after` screenshots:

1. **The BZ-020 vs Type OS question above** — a real decision, not a defect.
2. **All four footer headings now match `footer-join-the-list-LOCK.html`.** Help v4's in particular
   dropped from 32px/600 to 28px/400. This aligns the candidates to the documented footer lock and
   fixes a real mobile bug on Collection and SEO, where the heading was pinned at 28px with no
   downscale — but it does change how the footer reads.

Journal v6 — the candidate Agent B flagged — is the most improved and has **no** competing lock note
of its own, so it can be promoted on typography without reservation.
