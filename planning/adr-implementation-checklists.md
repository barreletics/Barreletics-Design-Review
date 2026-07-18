# ADR Implementation Checklists

**Generated:** 2026-07-13  
**Purpose:** Executable checklists for each ADR option, with exact file and line targets

---

## ADR-01: Color Palette Values

### If Option A chosen (Adopt docs/06 neutral values everywhere)

**Files to modify:** docs/04-COMPONENT-LIBRARY.md

- [ ] Update docs/04-COMPONENT-LIBRARY.md line 23: change `#f9f7f2` → `#f9f9f9`
- [ ] Update docs/04-COMPONENT-LIBRARY.md line 24: change `#6a6a6a` → `#4a4a4a`
- [ ] Update docs/04-COMPONENT-LIBRARY.md line 25: change `#999999` → `#8a8a8a`
- [ ] Update docs/04-COMPONENT-LIBRARY.md line 26: change `#e5e2db` → `#e6e6e6`
- [ ] Update docs/04-COMPONENT-LIBRARY.md line 29: change `(#e5e2db)` → `(#e6e6e6)`
- [ ] Update docs/04-COMPONENT-LIBRARY.md line 130: change `#f9f7f2` → `#f9f9f9`
- [ ] Verify: grep `#f9f7f2` in docs/04 returns 0 results
- [ ] Verify: grep `#6a6a6a` in docs/04 returns 0 results
- [ ] Verify: grep `#999999` in docs/04 returns 0 results
- [ ] Verify: grep `#e5e2db` in docs/04 returns 0 results
- [ ] Update docs/10-DECISIONS.md: record decision rationale under D-007

**Note:** docs/07-COPY-GUIDE.md contains 80+ `#f9f7f2` references in HTML templates. Decision needed: update those or document as "pre-matured template code."

### If Option B chosen (Adopt docs/04 warm values everywhere)

**Files to modify:** docs/03-DESIGN-SYSTEM.md, docs/06-HOMEPAGE-ARCHITECTURE.md, docs/10-DECISIONS.md

- [ ] Update docs/03-DESIGN-SYSTEM.md line 120: change `#f9f9f9` → `#f9f7f2`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 123: change `#4a4a4a` → `#6a6a6a`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 124: change `#8a8a8a` → `#999999`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 125: change `#e6e6e6` → `#e5e2db`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 40: change `#f9f9f9` → `#f9f7f2`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 43: change `#4a4a4a` → `#6a6a6a`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 44: change `#8a8a8a` → `#999999`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 45: change `#e6e6e6` → `#e5e2db`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 5595: change `#f9f9f9` → `#f9f7f2`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 5598: change `#4a4a4a` → `#6a6a6a`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 5599: change `#8a8a8a` → `#999999`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 5600: change `#e6e6e6` → `#e5e2db`
- [ ] Update docs/10-DECISIONS.md line 63: change `alt-bg=#f9f9f9, text-soft=#4a4a4a, text-mute=#8a8a8a, line=#e6e6e6` → warm values
- [ ] Verify: grep `#f9f9f9` in docs/06 `:root` blocks returns 0
- [ ] Update docs/10-DECISIONS.md: record decision rationale

**Note:** docs/05-PDP-ARCHITECTURE.md uses `#f9f9f9`, `#4a4a4a`, `#8a8a8a`, `#e6e6e6` extensively in its CSS. If Option B is chosen, those PDP values become wrong and require massive update.

### If Option C chosen (Both valid in different contexts)

- [ ] Add contextual rules section to docs/03-DESIGN-SYSTEM.md (after line 125): define when warm vs neutral palette applies
- [ ] Add note to docs/04-COMPONENT-LIBRARY.md (after line 26): "Warm palette — used for brand storytelling sections"
- [ ] Add note to docs/06-HOMEPAGE-ARCHITECTURE.md (after line 45): "Neutral palette — used for commerce/product sections"
- [ ] Update docs/10-DECISIONS.md: record dual-palette decision with usage rules
- [ ] Verify: both palette sets are documented with clear scope boundaries

---

## ADR-02: Free Shipping Threshold

### If Option A chosen (Replace all $75 with $150)

**Files to modify:** docs/05-PDP-ARCHITECTURE.md

- [ ] Update docs/05-PDP-ARCHITECTURE.md line 264: change `$75` → `$150` in "Free shipping on orders over $75"
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 2197: change `$75` → `$150` in meta description
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 2295: change `$75` → `$150` in "free shipping over $75"
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 2360: change `$75` → `$150` in "Free shipping on orders over $75"
- [ ] Add inline comment referencing C-010 at each updated location
- [ ] Verify: grep `\$75` in docs/05 returns 0 results for shipping context
- [ ] Verify: docs/05 line 195 already says $150 (no change needed)
- [ ] Verify: docs/05 line 2212 already says $150 (no change needed)
- [ ] Update docs/10-DECISIONS.md: note that docs/05 has been reconciled per C-010

### If Option B chosen (Leave as-is, add conflict note)

- [ ] Add header note to docs/05-PDP-ARCHITECTURE.md (after line 7): "NOTE: All $75 free shipping references in this document should be read as $150 per C-010 resolution."
- [ ] Update docs/10-DECISIONS.md: record decision to preserve original document with header note
- [ ] Verify: header note is clearly visible above first $75 occurrence

---

## ADR-03: Button Border-Radius

### If Option A chosen (PDP is explicit exception — 6px allowed)

- [ ] Update docs/04-COMPONENT-LIBRARY.md after line 37: add "Exception: PDP CTA uses `border-radius: 6px` (approved override per ADR-03)"
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 46: add comment noting approved exception
- [ ] Update docs/10-DECISIONS.md D-003: add exception note for PDP CTA
- [ ] Record new decision in docs/10-DECISIONS.md: "D-003-A: PDP CTA button 6px exception approved"
- [ ] Verify: docs/04 system rule still says 0px for all OTHER buttons

### If Option B chosen (System wins — PDP changes to 0px)

- [ ] Update docs/05-PDP-ARCHITECTURE.md line 46: change `border-radius: 6px` → `border-radius: 0px` in `.pdp-buy__cta`
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 230: change `border-radius:6px` → `border-radius:0px` in size button M
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 231: change `border-radius:6px` → `border-radius:0px` in size button L
- [ ] Verify: grep `border-radius: 6px` in docs/05 for button context returns 0
- [ ] Update docs/10-DECISIONS.md: record that system rule prevails, PDP aligned

### If Option C chosen (0px for CTA, 6px for size pills)

- [ ] Update docs/05-PDP-ARCHITECTURE.md line 46: change `border-radius: 6px` → `border-radius: 0px` in `.pdp-buy__cta`
- [ ] Keep docs/05-PDP-ARCHITECTURE.md lines 230–231: size pills retain `border-radius: 6px`
- [ ] Update docs/04-COMPONENT-LIBRARY.md after line 37: add "Exception: Selection pills (non-action affordances) may use up to 6px radius"
- [ ] Update docs/10-DECISIONS.md: record distinction between action buttons (0px) and selection chips (6px)
- [ ] Verify: CTA buttons now 0px, size pills documented as exception

---

## ADR-04: Eyebrow Letter-Spacing

### If Option A chosen (0.14em / 700 as system default)

- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 76: change `/* uppercase, 0.08em, 600 */` → `/* uppercase, 0.14em, 700 */`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 149: change `letter-spacing: 0.08em`, weight 600` → `letter-spacing: 0.14em`, weight 700`
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 40: change `letter-spacing: 0.08em` → `letter-spacing: 0.14em` in `.pdp-buy__badge` (or document as exception)
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 55: change `letter-spacing: 0.08em` → `letter-spacing: 0.14em` in `.pdp-section__label` (or document as exception)
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 59: change `letter-spacing: 0.08em` → `letter-spacing: 0.14em` in `.pdp-benefit__num` (or document as exception)
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 81: change `letter-spacing: 0.08em` → `letter-spacing: 0.14em` in `.pdp-justifier__tag` (or document as exception)
- [ ] Document exceptions for docs/04 line 576 (`0.18em` manifesto) and line 668 (`0.06em` closing CTA)
- [ ] Resolve docs/03-DESIGN-SYSTEM.md lines 394–398 conflict note: mark as RESOLVED
- [ ] Update docs/10-DECISIONS.md: record decision and exception list

### If Option B chosen (0.08em / 600 as system default)

- [ ] Update docs/04-COMPONENT-LIBRARY.md line 12: change `letter-spacing 0.14em` → `letter-spacing 0.08em` and `font-weight 700` → `font-weight 600`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 371: change `0.14em` → `0.08em` and `700` → `600`
- [ ] Document exceptions for docs/04 line 576 (`0.18em`) and line 668 (`0.06em`)
- [ ] Resolve docs/03-DESIGN-SYSTEM.md lines 394–398 conflict note: mark as RESOLVED
- [ ] Update docs/10-DECISIONS.md: record decision
- [ ] Verify: docs/04 line 12 and docs/03 line 371 now agree with docs/06 line 76

### If Option C chosen (Two tiers)

- [ ] Update docs/04-COMPONENT-LIBRARY.md line 12: add tier system — "Hero-grade eyebrows: 0.14em/700; Compact eyebrows: 0.08em/600"
- [ ] Update docs/03-DESIGN-SYSTEM.md line 149: note both values with tier classification
- [ ] Update docs/03-DESIGN-SYSTEM.md line 371: add tier distinction
- [ ] Add lookup table to docs/04 or docs/03: mapping each component to its tier
- [ ] Document docs/04 line 576 (`0.18em`) and line 668 (`0.06em`) status (deprecated? allowed?)
- [ ] Resolve docs/03-DESIGN-SYSTEM.md lines 394–398 conflict note: mark as RESOLVED with tier system
- [ ] Update docs/10-DECISIONS.md: record two-tier decision with component mapping

---

## ADR-05: PDP Text Color

### If Option A chosen (Make #1c1916 canonical — retire #050505)

- [ ] Update docs/04-COMPONENT-LIBRARY.md line 20: change `#050505` → `#1c1916`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 122: change `#050505` → `#1c1916`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 374: change `text=#050505` → `text=#1c1916`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 42: change `--br-text: #050505` → `--br-text: #1c1916`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 5597: change `--br-text: #050505` → `--br-text: #1c1916`
- [ ] Simplify/remove docs/06-HOMEPAGE-ARCHITECTURE.md lines 4206–4210: matured override for `--br-text` no longer needed
- [ ] Update docs/10-DECISIONS.md line 63 (D-007): change `text=#050505` → `text=#1c1916`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 60: change `--br-button: #050505` → `--br-button: #1c1916` (if button color follows text)
- [ ] Verify: grep `#050505` in token definitions returns 0 (note: button bg may stay)
- [ ] Update docs/10-DECISIONS.md: record decision and rationale

### If Option B chosen (Keep #050505 base — formalize #1c1916 as matured override)

- [ ] Update docs/05-PDP-ARCHITECTURE.md line 24: change `color: #1c1916` → `color: var(--br-text)` and add `data-matured="on"` to body
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 42: change `color: #1c1916` → `color: var(--br-text)` in `.pdp-buy__name`
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 44: change `color: #1c1916` → `color: var(--br-text)` in `.pdp-buy__price-now`
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 56: change `color: #1c1916` → `color: var(--br-text)` in `.pdp-section__title`
- [ ] Update docs/05-PDP-ARCHITECTURE.md lines 25, 46, 51, 60, 73, 83, 88, 94, 97, 99: change hardcoded `#1c1916` → `var(--br-text)` or appropriate token
- [ ] Verify: PDP wrapper has `data-matured="on"` attribute
- [ ] Add documentation note about the matured toggle mechanism
- [ ] Update docs/10-DECISIONS.md: record architectural decision

### If Option C chosen (Accept divergence — document intentional difference)

- [ ] Add note to docs/10-DECISIONS.md: "PDP uses #1c1916 by design to complement product photography. Homepage base uses #050505 with matured override to #1c1916."
- [ ] No file changes to docs/03, docs/04, docs/05, or docs/06
- [ ] Verify: divergence is explicitly documented

---

## ADR-06: Review Card Radius

### If Option A chosen (PDP cards are explicit exceptions — allow 12px)

- [ ] Update docs/04-COMPONENT-LIBRARY.md lines 30–33: add exception clause for review/testimonial cards
- [ ] Add annotation to docs/05-PDP-ARCHITECTURE.md line 67: note approved exception
- [ ] Add annotation to docs/05-PDP-ARCHITECTURE.md line 80: note approved exception
- [ ] Update docs/10-DECISIONS.md D-038: mark as approved exception, remove conflict flag
- [ ] Decide on docs/05 lines 36 (8px gallery) and 76 (8px video): approved or separate ADR
- [ ] Decide on docs/05 line 46 (6px CTA): links to ADR-03
- [ ] Update docs/10-DECISIONS.md: record full exception list

### If Option B chosen (System wins — change PDP to 4px max)

- [ ] Update docs/05-PDP-ARCHITECTURE.md line 67: change `border-radius: 12px` → `border-radius: 4px` in `.review-card`
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 80: change `border-radius: 12px` → `border-radius: 4px` in `.pdp-justifier__card`
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 541: change `border-radius:12px` → `border-radius:4px` in inline comparison card
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 561: change `border-radius:12px` → `border-radius:4px` in inline comparison card
- [ ] Flag docs/05 line 36 (`8px` gallery) for resolution: change to 4px
- [ ] Flag docs/05 line 76 (`8px` video) for resolution: change to 4px
- [ ] Update docs/10-DECISIONS.md D-038: mark as overridden by system rule
- [ ] Verify: grep `border-radius: 12px` in docs/05 returns 0

### If Option C chosen (Define "content card" exception tier)

- [ ] Rewrite docs/04-COMPONENT-LIBRARY.md lines 30–33 to: "0px default; 2–4px structural cards; up to 12px for content/testimonial cards"
- [ ] Define qualifying component types in docs/04 (review-card, justifier-card)
- [ ] Add annotation to docs/05 lines 67, 80: "content card tier — 12px permitted"
- [ ] Address docs/05 lines 36, 76 (8px): define which tier gallery/video containers belong to
- [ ] Update docs/10-DECISIONS.md: record tiered system decision
- [ ] Verify: all radius values in docs/05 map to a defined tier

---

## ADR-07: Star/Rating Color

### If Option A chosen (Use #fbc02d everywhere — system token wins)

- [ ] Update docs/05-PDP-ARCHITECTURE.md line 41: change `color: #d4af37` → `color: #fbc02d` (or `color: var(--br-star)`)
- [ ] Update docs/05-PDP-ARCHITECTURE.md line 71: change `color: #d4af37` → `color: #fbc02d` (or `color: var(--br-star)`)
- [ ] Evaluate docs/05-PDP-ARCHITECTURE.md line 552: `#d4af37` used as label color (non-star) — update to appropriate token
- [ ] Verify: grep `#d4af37` in docs/ returns 0 results
- [ ] Update docs/10-DECISIONS.md: record decision — system token prevails

### If Option B chosen (Use #d4af37 everywhere — PDP value wins)

- [ ] Update docs/04-COMPONENT-LIBRARY.md line 22: change `#fbc02d` → `#d4af37`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 130: change `#fbc02d` → `#d4af37`
- [ ] Update docs/03-DESIGN-SYSTEM.md line 374: change `star=#fbc02d` → `star=#d4af37`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 55: change `--br-star: #fbc02d` → `--br-star: #d4af37`
- [ ] Update docs/06-HOMEPAGE-ARCHITECTURE.md line 5610: change `--br-star: #fbc02d` → `--br-star: #d4af37`
- [ ] Update docs/10-DECISIONS.md line 63 (D-007): change `star=#fbc02d` → `star=#d4af37`
- [ ] Verify: grep `#fbc02d` in docs/ returns 0 results
- [ ] Update docs/10-DECISIONS.md: record decision — PDP value adopted as canonical

### If Option C chosen (Keep both — PDP uses darker gold intentionally)

- [ ] Add note to docs/10-DECISIONS.md: "PDP uses #d4af37 to harmonize with #1c1916 text. Homepage uses #fbc02d against #050505 base."
- [ ] Add annotation to docs/05-PDP-ARCHITECTURE.md lines 41, 71: document intentional contextual choice
- [ ] No changes to docs/03, docs/04, or docs/06
- [ ] Update docs/10-DECISIONS.md: record divergence decision
