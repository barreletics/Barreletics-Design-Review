# Post Image Foundation — Backlog

Items deferred during Image Foundation Steps 1–6. Address AFTER all foundation gates land.

---

## Type OS gate (one deliverable, do together)

- [ ] Build `heading` snippet (like `media-img`): shared header render with `heading_style` param (`eyebrow` | `standard` | `display`) and per-section schema calls.
- [ ] Add site-wide `heading_size_role` control per section.
- [ ] Migrate `press-row.liquid` `heading_style` toggle (commit `8ce514f`) INTO the shared snippet.
- [ ] Remove per-section eyebrow/heading style branches once the shared snippet ships.

**Rule (from Claude, 2026-09-23):** No new per-section heading toggles in the interim.

---

## Step 5 dead-code / cleanup

- [ ] `sections/fifty-fifty.liquid` — clean up inline-style `!important` cascade (deferred from Gate 1 rollout, commit `3379447`).
- [ ] Poster/video-fallback img sweep — migrate to `media-img` together:
  - `sections/fullbleed-statement.liquid` — `<img class="fullbleed-statement__poster-cover">` at L104/137/146.
  - `sections/collab-hero.liquid` — 4 `<img class="collab-hero__video">` at L120/122/176/178 (editorial + stage_grid video-slot fallbacks).
- [ ] `sections/press-feature.liquid` — drop `!important` from `.twin-frame__img` width/height/max/display rules (only if img-only cascade lets us; keep if video needs them).
- [ ] Section CSS audit: consolidate `!important` markers that were carried over during image foundation gates.
- [ ] `.media-fill` retirement — after collab-hero Gate 4 verified. Path: drop `.media-fill*` class from render calls (leaving only `.media-img[--contain]`), then remove `.media-fill` + modifier rules from `barreletics-base.css` and the `.collab-hero--stage_grid .collab-hero__tile .media-fill { object-fit: cover; }` override. Verify tile fit/focus still work via `.media-img[--contain]` + a section-scoped focus system (add object-position vars if needed).

---

## Section restorations (nice-to-have)

### INTERNI single-frame press feature
- **Reason to restore:** dedicated INTERNI editorial moment on Home (currently only lives as card 3 in `press-row`).
- **Restore anchor:** `git show a5c906a:shopify-build/sections/press-feature.liquid` (Sep 18, 2026 — last commit before repurpose to twin-frame). 487 lines.
- **Recommended path:** copy that file to `sections/press-feature-hero.liquid`, migrate its imgs to `media-img` as part of same commit, add to Home order via JSON push (careful of TE overwrites).
- **Owner call needed on:** placement, whether to keep original schema or simplify.
- Not blocking. Content is preserved as press-row card 3.

---

## Mobile pixel sizes for standards table

- [ ] Add mobile min-export px per section family (390px viewport × 3x DPR) to the standards table in `~/.cursor/skills/barreletics-images/SKILL.md`. Claude ruled this during Step 1 handoff.
