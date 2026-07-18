# ADR Validation Report

**Generated:** 2026-07-13  
**Scope:** ADR-01 through ADR-07 validated against docs/03, docs/04, docs/05, docs/06, docs/07, docs/09, docs/10

---

## ADR-01: Color Palette Values

### Confirmed References

| Claim | File | Line(s) | Verified Value |
|-------|------|---------|----------------|
| Alt background `#f9f7f2` | docs/04-COMPONENT-LIBRARY.md | 23 | ✓ `- **Alt background:** #f9f7f2` |
| Text (soft) `#6a6a6a` | docs/04-COMPONENT-LIBRARY.md | 24 | ✓ `- **Text (soft):** #6a6a6a` |
| Text (muted) `#999999` | docs/04-COMPONENT-LIBRARY.md | 25 | ✓ `- **Text (muted):** #999999` |
| Line (border) `#e5e2db` | docs/04-COMPONENT-LIBRARY.md | 26 | ✓ `- **Line (border):** #e5e2db` |
| Alt background `#f9f9f9` | docs/06-HOMEPAGE-ARCHITECTURE.md | 40 | ✓ `--br-alt-bg: #f9f9f9;` |
| Text (soft) `#4a4a4a` | docs/06-HOMEPAGE-ARCHITECTURE.md | 43 | ✓ `--br-text-soft: #4a4a4a;` |
| Text (muted) `#8a8a8a` | docs/06-HOMEPAGE-ARCHITECTURE.md | 44 | ✓ `--br-text-mute: #8a8a8a;` |
| Line (border) `#e6e6e6` | docs/06-HOMEPAGE-ARCHITECTURE.md | 45 | ✓ `--br-line: #e6e6e6;` |
| D-007 uses docs/06 values | docs/10-DECISIONS.md | 63 | ✓ `alt-bg=#f9f9f9, text-soft=#4a4a4a, text-mute=#8a8a8a, line=#e6e6e6` |
| docs/03 uses docs/06 values | docs/03-DESIGN-SYSTEM.md | 120–125 | ✓ All four tokens match docs/06 |
| Dead code comment | docs/06-HOMEPAGE-ARCHITECTURE.md | 37–38 | ✓ "cream + plum in settings_data.json is dead code" |

### Corrected References

| Claim | ADR Says | Actual |
|-------|----------|--------|
| Dead code statement line | Line 38 | Spans lines 37–38 (minor — content is correct) |

### NEW References Found (not in original ADR)

| Token | File | Line(s) | Context |
|-------|------|---------|---------|
| `#f9f7f2` | docs/04-COMPONENT-LIBRARY.md | 130 | "Light background (var(--alt-bg), #f9f7f2)" |
| `#f9f7f2` | docs/07-COPY-GUIDE.md | 3898, 6256, etc. (80+ occurrences) | `.v11-split__copy { background: #f9f7f2 }` repeated in HTML templates |
| `#f9f7f2` | docs/06-HOMEPAGE-ARCHITECTURE.md | 3897, 9452 | `.v11-split__copy { background: #f9f7f2 }` in HTML markup |
| `#f9f9f9` | docs/05-PDP-ARCHITECTURE.md | 36, 76, 161–164, 231, 289, 502, 536 | Gallery bg, motion video, thumbnails, size button, JS, section bg |
| `#f9f9f9` | docs/03-DESIGN-SYSTEM.md | 120 | Token table: `--br-alt-bg` |
| `#4a4a4a` | docs/05-PDP-ARCHITECTURE.md | 43, 61, 72, 77, 82, 174, 250, 257, 264, 268, 307–322, 350, 539 | Used extensively as secondary text throughout PDP |
| `#8a8a8a` | docs/05-PDP-ARCHITECTURE.md | 45, 55, 76, 176, 195, 202, 230–231, 239, 352, 354, 493, 495, 542, 562 | Price meta, section labels, size pills, trust row |
| `#e6e6e6` | docs/05-PDP-ARCHITECTURE.md | 67, 92, 162–164, 193, 199, 224, 230, 239, 247–266, 276, 287, 341, 541, 554, 561 | Borders throughout PDP |
| `#e6e6e6` | docs/03-DESIGN-SYSTEM.md | 125 | Token table: `--br-line` |

### Missing References

None — all cited files and line numbers exist and match.

---

## ADR-02: Free Shipping Threshold

### Confirmed References

| Claim | File | Line | Verified Value |
|-------|------|------|----------------|
| $150 (updated) | docs/05-PDP-ARCHITECTURE.md | 195 | ✓ "free shipping over $150" |
| $75 (stale) | docs/05-PDP-ARCHITECTURE.md | 264 | ✓ "Free shipping on orders over $75" |
| $75 (stale) | docs/05-PDP-ARCHITECTURE.md | 2197 | ✓ meta description "Free shipping over $75" |
| $150 (updated) | docs/05-PDP-ARCHITECTURE.md | 2212 | ✓ ticker "Free shipping over $150" |
| $75 (stale) | docs/05-PDP-ARCHITECTURE.md | 2295 | ✓ "free shipping over $75" |
| $75 (stale) | docs/05-PDP-ARCHITECTURE.md | 2360 | ✓ "Free shipping on orders over $75" |
| C-010 resolved at $150 | docs/10-DECISIONS.md | 1085 | ✓ "RESOLVED — $150 is current" |

### Corrected References

None — all line numbers match exactly.

### NEW References Found (not in original ADR)

| Value | File | Line(s) | Context |
|-------|------|---------|---------|
| $150 | docs/09-PRODUCT-KNOWLEDGE.md | 24 | "Free over $150 / $9.95 flat rate under $150" |
| $150 | docs/09-PRODUCT-KNOWLEDGE.md | 965–966 | "Free shipping on orders over $150" |
| $150 | docs/03-DESIGN-SYSTEM.md | 239 | "Free-shipping threshold is `$150` site-wide" |
| $150 | docs/03-DESIGN-SYSTEM.md | 402–404 | "The live site now shows $150" |
| $150 | docs/10-DECISIONS.md | 575–579 | BZ-004: "Free shipping over $150" |
| $150 | docs/10-DECISIONS.md | 583–587 | BZ-005: "Raised from $75 to $150" |
| $150 | docs/06-HOMEPAGE-ARCHITECTURE.md | 4294 | ticker "Free shipping over $150" |
| $75 ref | docs/03-DESIGN-SYSTEM.md | 239 | "(the live `$75` is being raised)" — historical note |

### Missing References

- ADR cites `docs/08-LIVE-SITE-COPY-AUDIT.md` — file exists, confirmed $150 at lines 27, 1566.

---

## ADR-03: Button Border-Radius

### Confirmed References

| Claim | File | Line | Verified Value |
|-------|------|------|----------------|
| All buttons square `0px` | docs/04-COMPONENT-LIBRARY.md | 37 | ✓ "all square (border-radius: 0px, no drop shadows, no gradients)" |
| CTA `border-radius: 6px` | docs/05-PDP-ARCHITECTURE.md | 46 | ✓ `.pdp-buy__cta { ... border-radius: 6px; }` |
| Size selectors `6px` | docs/05-PDP-ARCHITECTURE.md | 230–231 | ✓ `border-radius:6px` in inline styles |

### Corrected References

None — all exact.

### NEW References Found (not in original ADR)

| Value | File | Line(s) | Context |
|-------|------|---------|---------|
| `border-radius: 0` | docs/03-DESIGN-SYSTEM.md | 372 | "Buttons: Square (radius 0), black #050505" |
| `border-radius: 0px` | docs/10-DECISIONS.md | 30–34 | D-003: "Buttons: Square (radius 0)" |
| `6px` | docs/05-PDP-ARCHITECTURE.md | 46 only | CTA is the only `border-radius: 6px` in the file |

### Missing References

None.

---

## ADR-04: Eyebrow Letter-Spacing

### Confirmed References

| Claim | File | Line | Verified Value |
|-------|------|------|----------------|
| System rule `0.14em / 700` | docs/04-COMPONENT-LIBRARY.md | 12 | ✓ "letter-spacing 0.14em / uppercase" with "font-weight 700" |
| Research Bible `0.14em / 700` | docs/03-DESIGN-SYSTEM.md | 371 | ✓ "Eyebrows: 12px/700/0.14em/uppercase" |
| Homepage token `0.08em / 600` | docs/06-HOMEPAGE-ARCHITECTURE.md | 76 | ✓ `--t-eyebrow: 12px; /* uppercase, 0.08em, 600 */` |
| PDP badge `0.08em` | docs/05-PDP-ARCHITECTURE.md | 40 | ✓ `letter-spacing: 0.08em` |
| PDP section label `0.08em` | docs/05-PDP-ARCHITECTURE.md | 55 | ✓ `letter-spacing: 0.08em` |
| Manifesto `0.18em` | docs/04-COMPONENT-LIBRARY.md | 576 | ✓ "all-caps eyebrow (11px, 0.18em letter-spacing)" |
| Closing CTA `0.06em / 600` | docs/04-COMPONENT-LIBRARY.md | 668 | ✓ "12px, 600 weight, 0.06em letter-spacing, uppercase" |
| Conflict flagged | docs/03-DESIGN-SYSTEM.md | 395–398 | ✓ Conflict table at lines 394–398 |

### Corrected References

| Claim | ADR Says | Actual |
|-------|----------|--------|
| Homepage token location | "CSS `--t-eyebrow` token" (no line) | Line 76 of docs/06 |
| docs/03 conflict flag | "line 396–398" | Lines 394–398 (table starts at 394) |

### NEW References Found (not in original ADR)

| Value | File | Line(s) | Context |
|-------|------|---------|---------|
| `0.08em` | docs/05-PDP-ARCHITECTURE.md | 59 | `.pdp-benefit__num { letter-spacing: 0.08em }` |
| `0.08em` | docs/05-PDP-ARCHITECTURE.md | 81 | `.pdp-justifier__tag { letter-spacing: 0.08em }` |
| `0.08em` | docs/03-DESIGN-SYSTEM.md | 149 | Token table: `--t-eyebrow` described as `0.08em, weight 600` |
| `0.14em` | docs/06-HOMEPAGE-ARCHITECTURE.md | 872, 1078, 1344, 1630, 1673, 1943, 2487, 2813, 3010, 3129, 3207, 3320, 3359, 3419, 3592, 3862, 3908, 4016 | Extensively used in CSS class definitions |
| `0.14em` | docs/05-PDP-ARCHITECTURE.md | 763, 1029, 1315, 1358, 1628, 2015, 2502 | Matured PDP CSS and inline styles |
| `0.18em` | docs/06-HOMEPAGE-ARCHITECTURE.md | 156, 220, 501, 557, 910, 978, 3783, 3834, 3998, etc. | 30+ occurrences in matured homepage CSS |
| `0.06em` | docs/06-HOMEPAGE-ARCHITECTURE.md | 1173, 1545, 1572, 3271, 3701, 3965, etc. | 16+ occurrences |
| `0.06em` | docs/05-PDP-ARCHITECTURE.md | 126, 858, 1230, 1257, 1853, 2396, 2573 | Card hover, variant CTAs, disclaimers |
| `0.14em` | docs/10-DECISIONS.md | 1077 | C-002 conflict entry |

### Missing References

- ADR lists `docs/05` lines 59 and 81 in "Source Files" section but doesn't include them in the evidence table. Values confirmed present (both `0.08em`).

---

## ADR-05: PDP Text Color

### Confirmed References

| Claim | File | Line | Verified Value |
|-------|------|------|----------------|
| `#050505` primary text | docs/04-COMPONENT-LIBRARY.md | 20 | ✓ `- **Text (primary):** #050505` |
| `#050505` Research Bible | docs/03-DESIGN-SYSTEM.md | 374 | ✓ `text=#050505` |
| `--br-text: #050505` base | docs/06-HOMEPAGE-ARCHITECTURE.md | 42 | ✓ `--br-text: #050505;` |
| `--br-text: #1c1916` matured | docs/06-HOMEPAGE-ARCHITECTURE.md | 4210 | ✓ `--br-text: #1c1916;` in `[data-matured="on"]` |
| PDP body `#1c1916` | docs/05-PDP-ARCHITECTURE.md | 24 | ✓ `body { ... color: #1c1916 ... }` |
| `.pdp-buy__name` | docs/05-PDP-ARCHITECTURE.md | 42 | ✓ `color: #1c1916` |
| `.pdp-buy__price-now` | docs/05-PDP-ARCHITECTURE.md | 44 | ✓ `color: #1c1916` |
| `.pdp-section__title` | docs/05-PDP-ARCHITECTURE.md | 56 | ✓ `color: #1c1916` |

### Corrected References

| Claim | ADR Says | Actual |
|-------|----------|--------|
| Matured block location | "lines 4206–4210" | ✓ Confirmed: block starts line 4206, `--br-text: #1c1916` at line 4210 |

### NEW References Found (not in original ADR)

| Value | File | Line(s) | Context |
|-------|------|---------|---------|
| `#1c1916` | docs/05-PDP-ARCHITECTURE.md | 25, 31, 46, 51, 60, 73, 83, 88, 94, 97, 99, 161, 227, 231, 240–243 | Pervasive throughout PDP (links, hover states, CTA bg, swatch borders, FAQ, newsletter, checkmarks) |
| `#050505` | docs/06-HOMEPAGE-ARCHITECTURE.md | 42, 60, 2645, 2689, 2736, 2767, 2825, 3074, 3163, 3883, 4001, 4773, 5597, 5615, 8200+ | Button backgrounds and text color in homepage |
| `#050505` | docs/03-DESIGN-SYSTEM.md | 122 | Token table: `--br-text` |
| `#050505` | docs/10-DECISIONS.md | 63 | D-007: `text=#050505` |

### Missing References

None — all cited locations verified.

---

## ADR-06: Review Card Radius

### Confirmed References

| Claim | File | Line | Verified Value |
|-------|------|------|----------------|
| No radius by default | docs/04-COMPONENT-LIBRARY.md | 30 | ✓ "Border radius: No radius by default" |
| Cards: 0px | docs/04-COMPONENT-LIBRARY.md | 31 | ✓ "Cards: 0px (square)" |
| 2px or 4px only | docs/04-COMPONENT-LIBRARY.md | 32 | ✓ "Where matured direction uses radius: 2px or 4px only" |
| Never 12–16px | docs/04-COMPONENT-LIBRARY.md | 33 | ✓ "Never use pill-card style (12–16px radius)" |
| Square aesthetic | docs/03-DESIGN-SYSTEM.md | 372 | ✓ "Buttons: Square (radius 0), black #050505" |
| `.review-card` 12px | docs/05-PDP-ARCHITECTURE.md | 67 | ✓ `.review-card { ... border-radius: 12px ... }` |
| `.pdp-justifier__card` 12px | docs/05-PDP-ARCHITECTURE.md | 80 | ✓ `.pdp-justifier__card { ... border-radius: 12px ... }` |
| Gallery hero 8px | docs/05-PDP-ARCHITECTURE.md | 36 | ✓ `.pdp-gallery__hero { ... border-radius: 8px; }` |
| Motion video 8px | docs/05-PDP-ARCHITECTURE.md | 76 | ✓ `.pdp-motion__video { ... border-radius: 8px; }` |
| CTA 6px | docs/05-PDP-ARCHITECTURE.md | 46 | ✓ `.pdp-buy__cta { ... border-radius: 6px; }` |

### Corrected References

None — all exact.

### NEW References Found (not in original ADR)

| Value | File | Line(s) | Context |
|-------|------|---------|---------|
| `12px` decision recorded | docs/10-DECISIONS.md | 285–290 | D-038: "Review cards on PDP use border-radius: 12px" with conflict note |
| `12px` in comparison cards | docs/05-PDP-ARCHITECTURE.md | 541, 561 | Inline style `border-radius:12px` on comparison table cards |
| `8px` decision recorded | docs/10-DECISIONS.md | 292–294 | D-039: "PDP gallery hero image uses border-radius: 8px" |

### Missing References

None.

---

## ADR-07: Star/Rating Color

### Confirmed References

| Claim | File | Line | Verified Value |
|-------|------|------|----------------|
| `#fbc02d` system token | docs/04-COMPONENT-LIBRARY.md | 22 | ✓ `- **Star (rating):** #fbc02d` |
| `#fbc02d` Research Bible | docs/03-DESIGN-SYSTEM.md | 374 | ✓ `star=#fbc02d` |
| `--br-star: #fbc02d` | docs/06-HOMEPAGE-ARCHITECTURE.md | 55 | ✓ `--br-star: #fbc02d; /* gold star color */` |
| PDP stars `#d4af37` | docs/05-PDP-ARCHITECTURE.md | 41 | ✓ `.pdp-buy__stars { ... color: #d4af37 ... }` |
| Review stars `#d4af37` | docs/05-PDP-ARCHITECTURE.md | 71 | ✓ `.review-stars { ... color: #d4af37 ... }` |

### Corrected References

None — all exact.

### NEW References Found (not in original ADR)

| Value | File | Line(s) | Context |
|-------|------|---------|---------|
| `#d4af37` | docs/05-PDP-ARCHITECTURE.md | 552 | Used as label color for "Barreletics" in comparison card (not star-related) |
| `#fbc02d` | docs/03-DESIGN-SYSTEM.md | 130 | Token table: `--br-star` |
| `#fbc02d` | docs/10-DECISIONS.md | 63 | D-007: `star=#fbc02d` |
| `#fbc02d` | docs/06-HOMEPAGE-ARCHITECTURE.md | 5610 | Duplicate `:root` block (second homepage version) |

### Missing References

None.

---

## Summary

| ADR | All Line Refs Accurate | All Files Exist | New References Found | Missing Refs |
|-----|----------------------|-----------------|---------------------|--------------|
| ADR-01 | ✓ (1 minor: line 38 spans 37–38) | ✓ | Yes — docs/07 has 80+ `#f9f7f2` occurrences; docs/05 uses docs/06 values extensively | None |
| ADR-02 | ✓ All exact | ✓ | Yes — docs/09, docs/03, docs/06 contain $150 references | None |
| ADR-03 | ✓ All exact | ✓ | Yes — docs/03 line 372, docs/10 D-003 | None |
| ADR-04 | ✓ (1 minor: docs/06 token line is 76) | ✓ | Yes — extensive `0.14em` usage in docs/06 CSS; `0.18em` in docs/06 | None |
| ADR-05 | ✓ All exact | ✓ | Yes — 15+ additional `#1c1916` occurrences in docs/05 | None |
| ADR-06 | ✓ All exact | ✓ | Yes — docs/10 D-038/D-039 record these; comparison cards also use 12px | None |
| ADR-07 | ✓ All exact | ✓ | Yes — `#d4af37` used once non-star (line 552); extra `#fbc02d` in docs/03 token table | None |
