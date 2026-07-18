# ADR Candidates — Additional Architectural Conflicts

**Status:** INVENTORY  
**Date:** 2026-07-13  
**Scope:** Conflicts BEYOND ADR-01 through ADR-07  
**Method:** Cross-document comparison of APPROVED and PENDING REVIEW docs

---

## CANDIDATE ADR-08: Pillar Strip Content Count (5 vs 6 items)

**Severity:** High  
**Conflict:** docs/03 specifies 5 pillars; docs/04 specifies 6 pillars with different naming  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 207 — "5 horizontal benefits with dot dividers: 360° Grip · Stay Secure · No Sock Fuss · Rinse & Reuse · No Latex / No Silicone"  
**Source B:** docs/04-COMPONENT-LIBRARY.md, lines 121–127 — "6 pillars: 360° Grip, Two Surfaces, No Adjustments, Rinse & Reuse, No Latex, Barefoot"  
**Source C:** docs/05-PDP-ARCHITECTURE.md, lines 2378–2383 — PDP implementation uses 5 items: "360° Grip, Stay Secure, No Sock Fuss, Rinse & Reuse, No Latex / No Silicone"  
**Impact:** A developer building the Pillar Strip component doesn't know whether to build a 5-column or 6-column grid, and doesn't know which labels to use. Three documents give three different content lists.  
**Recommendation:** ADR required

---

## CANDIDATE ADR-09: PDP Primary CTA Font Size (14px vs 16px)

**Severity:** High  
**Conflict:** Design System specifies button text at 14px; PDP Architecture uses 16px  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 176 — `--btn-text-size: 14px`; docs/04-COMPONENT-LIBRARY.md, line 15 — "Buttons: Font weight 600 / letter-spacing 0.06em / 14px size"  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 46 — `.pdp-buy__cta { font-size: 16px; font-weight: 600; }`  
**Impact:** A developer implementing the PDP Add to Cart button would use 14px from the design system or 16px from the APPROVED PDP spec. The two sizes create different visual weight and may affect conversion.  
**Recommendation:** ADR required

---

## CANDIDATE ADR-10: PDP Primary CTA Padding (14px y / 28px x vs 18px uniform)

**Severity:** Medium  
**Conflict:** Design System specifies button padding 14px vertical / 28px horizontal; PDP uses 18px uniform  
**Source A:** docs/03-DESIGN-SYSTEM.md, lines 177–178 — `--btn-pad-y: 14px; --btn-pad-x: 28px;`  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 46 — `.pdp-buy__cta { padding: 18px; }` (uniform, no separate x/y)  
**Impact:** Button height and width proportions differ between PDP and all other pages. Inconsistent touch targets.  
**Recommendation:** ADR required

---

## CANDIDATE ADR-11: Product Card Hover Scale Factor (1.02x vs 1.03x vs 1.04x vs 1.05x)

**Severity:** Medium  
**Conflict:** Four different scale values specified for the same product card hover interaction  
**Source A:** docs/04-COMPONENT-LIBRARY.md, line 194 — "Image scales 1.02x over 320ms ease-out" (also lines 717, 922, 1000)  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 124 — `.pdp-variants__card:hover .card-img { transform: scale(1.03); }`  
**Source C:** docs/05-PDP-ARCHITECTURE.md, line 360+ (inline styles) — `transform='scale(1.04)'`  
**Source D:** docs/05-PDP-ARCHITECTURE.md, line 64 — `.pdp-variants__grid img { transform: scale(1.05); }`  
**Impact:** Same interaction (product card image hover) produces different zoom levels depending on which spec a developer follows. Visually inconsistent storefront.  
**Recommendation:** ADR required

---

## CANDIDATE ADR-12: Product Card Hover Transition Duration (320ms vs 400ms vs 450ms)

**Severity:** Medium  
**Conflict:** Three different transition durations for the same card hover animation  
**Source A:** docs/04-COMPONENT-LIBRARY.md, line 194 — "320ms ease-out"  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 125 — `.card-img { transition: transform 0.4s ease; }` (400ms)  
**Source C:** docs/05-PDP-ARCHITECTURE.md, line 362+ (inline styles) — `transition:transform 0.45s ease` (450ms)  
**Impact:** Animation speed inconsistency on product cards across pages. Minor visual but indicates system divergence.  
**Recommendation:** Can be resolved as remediation ticket (align to the Component Library's 320ms)

---

## CANDIDATE ADR-13: PDP CTA Coral Hover vs Coral Restraint Rule

**Severity:** High  
**Conflict:** Coral (#c45c3f / #f97250) is used on PDP button hover, contradicting the "coral is cart badge ONLY" rule  
**Source A:** docs/03-DESIGN-SYSTEM.md, lines 137–139 — "Do not paint CTAs, headings, or section backgrounds in --br-accent. The coral exists for the cart badge and nothing else."  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 47 — `.pdp-buy__cta:hover { background: #c45c3f; }` (also line 100: newsletter button hover → #c45c3f)  
**Impact:** The PDP's highest-conversion element (Add to Cart) uses coral on hover. If enforcing the restraint rule, this must change. If preserving PDP behavior, the restraint rule needs an exception. Blocking decision for any developer touching button styles.  
**Recommendation:** ADR required

---

## CANDIDATE ADR-14: PDP Section Title Font Size (42px vs 44px token --t-h2)

**Severity:** Medium  
**Conflict:** PDP section titles use 42px; the typography ramp defines h2 as 44px  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 157 — `--t-h2: 44px`  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 56 — `.pdp-section__title { font-size: 42px; }`  
**Impact:** If building from tokens, you'd use 44px. If building from PDP spec, 42px. 2px difference at this size is subtle but represents a values-vs-spec divergence that compounds across the system.  
**Recommendation:** Can be resolved as remediation ticket (likely snap to 44px token)

---

## CANDIDATE ADR-15: Homepage Section Count / Architecture (13 sections vs 16 sections)

**Severity:** High  
**Conflict:** docs/03 specifies 13 sections for the matured homepage; docs/04 specifies 16 sections with different ordering  
**Source A:** docs/03-DESIGN-SYSTEM.md, lines 203–216 — 13 sections: Ticker, Header, Hero, Pillar, Why-it-works, Variant grid, Coperni+FP, Sock-math, Testimonial, Founder note, Disciplines, Closing statement, Footer  
**Source B:** docs/04-COMPONENT-LIBRARY.md, lines 931–947 — 16 sections: Ticker, Header, Hero, Pillar strip, Split 1, Product grid, Promo tiles, Sock Math, Split 2, Disciplines, Split 3, Reviews, Coperni, Journal, Guarantee, Newsletter/FAQ/Social/Footer  
**Impact:** A developer doesn't know how many sections to build, or in what order. Missing 3 sections (Split 2, Split 3, Journal/Articles) from the matured spec, or 3 extra sections in the Component Library. Significantly different user experience.  
**Recommendation:** ADR required

---

## CANDIDATE ADR-16: Soft Text Color (#4a4a4a vs #6a6a6a)

**Severity:** Medium  
**Conflict:** Secondary/soft text color differs between Design System and Component Library  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 123 / docs/06-HOMEPAGE-ARCHITECTURE.md, line 43 — `--br-text-soft: #4a4a4a`  
**Source B:** docs/04-COMPONENT-LIBRARY.md, line 24 — "Text (soft): #6a6a6a"  
**Impact:** Body copy, descriptions, and secondary text will have noticeably different contrast depending on which spec is followed. #4a4a4a is significantly darker than #6a6a6a (4.5:1 vs 3.4:1 contrast on white — WCAG compliance difference).  
**Recommendation:** ADR required (accessibility implications)

---

## CANDIDATE ADR-17: Muted Text Color (#8a8a8a vs #999999)

**Severity:** Medium  
**Conflict:** Tertiary/muted text color differs between Design System and Component Library  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 124 / docs/06-HOMEPAGE-ARCHITECTURE.md, line 44 — `--br-text-mute: #8a8a8a`  
**Source B:** docs/04-COMPONENT-LIBRARY.md, line 25 — "Text (muted): #999999"  
**Impact:** Metadata, captions, and tertiary text appear at different lightness. Both values likely fail WCAG AA for normal text on white.  
**Recommendation:** Can be resolved as remediation ticket (pick one, verify WCAG)

---

## CANDIDATE ADR-18: Border/Line Color (#e6e6e6 vs #e5e2db)

**Severity:** Medium  
**Conflict:** Hairline/border color is cool grey in Design System, warm grey in Component Library  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 125 / docs/06-HOMEPAGE-ARCHITECTURE.md, line 45 — `--br-line: #e6e6e6`  
**Source B:** docs/04-COMPONENT-LIBRARY.md, lines 26, 29 — "Line (border): #e5e2db", "Borders: 1px solid var(--br-line) (#e5e2db)"  
**Impact:** Every card, divider, and section border will be either cool-neutral or warm-tinted. Mixing them creates a visually incoherent palette. This is part of the broader warm-vs-cool palette question.  
**Recommendation:** ADR required (systemic palette decision — bundle with ADR-01 or resolve separately)

---

## CANDIDATE ADR-19: PDP Accent Color (#f97250 vs #c45c3f)

**Severity:** High  
**Conflict:** PDP uses a darker terracotta (#c45c3f) where the design system specifies coral (#f97250) for accent  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 127 / docs/04-COMPONENT-LIBRARY.md, line 21 — `--br-accent: #f97250`  
**Source B:** docs/05-PDP-ARCHITECTURE.md, lines 40, 47, 59, 80, 81, 100, 396 — Uses `#c45c3f` for badges, benefit numbers, justifier borders, LE badges, CTA hover  
**Impact:** PDP accent (terracotta) is visually distinct from the rest of the site (coral). If both colors appear across the storefront, it reads as a palette error, not a design choice. CEO's Implementation Roadmap also references #c45c3f ("Terracotta") as the accent.  
**Recommendation:** ADR required (this is the PDP's warm-palette equivalent of what ADR-01 addresses for backgrounds)

---

## CANDIDATE ADR-20: PDP Internal Shipping Threshold Inconsistency ($75 vs $150 within same document)

**Severity:** Critical  
**Conflict:** The APPROVED PDP Architecture contains BOTH $75 and $150 free shipping thresholds in different sections  
**Source A:** docs/05-PDP-ARCHITECTURE.md, line 195 — Buy box meta: "free shipping over $150"  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 264 — Accordion: "Free shipping on orders over $75"  
**Source C:** docs/05-PDP-ARCHITECTURE.md, line 2295 — v2 buy box: "free shipping over $75"  
**Source D:** docs/05-PDP-ARCHITECTURE.md, line 2197 — v2 meta description: "Free shipping over $75"  
**Source E:** docs/05-PDP-ARCHITECTURE.md, line 2212 — Ticker: "Free shipping over $150"  
**Impact:** Even though ADR-02 addresses the cross-document $75 vs $150 question, the APPROVED PDP Architecture document itself is internally contradictory. A developer building from this document will implement conflicting copy on the same page. The buy box says $150, the accordion says $75.  
**Recommendation:** ADR required (or remediation of the APPROVED document once ADR-02 is resolved)

---

## CANDIDATE ADR-21: Eyebrow Font Weight (600 vs 700)

**Severity:** Medium  
**Conflict:** Eyebrow font-weight disagrees between Design System and Component Library/Research Bible  
**Source A:** docs/03-DESIGN-SYSTEM.md, line 149 — `--t-eyebrow: 12px; /* uppercase, 0.08em, 600 */`; docs/06-HOMEPAGE-ARCHITECTURE.md, line 76 — same comment  
**Source B:** docs/04-COMPONENT-LIBRARY.md, line 12 — "Eyebrows (labels): 12px / font-weight 700"; Research Bible Section 7 — "12px/700/0.14em/uppercase"  
**Impact:** Eyebrows are ubiquitous (every section has one). Weight 600 vs 700 is visually different on Roboto. Compounds with ADR-04 (letter-spacing conflict) into a complete eyebrow styling disagreement.  
**Recommendation:** ADR required (should be bundled with ADR-04 as "Eyebrow Complete Styling Specification")

---

## CANDIDATE ADR-22: PDP Gallery/Image Border Radius (8px vs max 4px rule)

**Severity:** Medium  
**Conflict:** PDP gallery hero and motion video use 8px radius; system max is 4px  
**Source A:** docs/03-DESIGN-SYSTEM.md, lines 189–191 — "Cards have no radius by default. Where matured direction uses radius (rare), 2px or 4px — never 12–16px"  
**Source B:** docs/05-PDP-ARCHITECTURE.md, line 36 — `.pdp-gallery__hero { border-radius: 8px; }`; line 76 — `.pdp-motion__video { border-radius: 8px; }`  
**Impact:** Gallery images and motion videos use a radius not permitted by the design system. 8px is between the allowed max (4px) and the already-flagged 12px (ADR-06). Requires a radius policy decision.  
**Recommendation:** Can be resolved as remediation ticket (snap to 4px or expand permitted set via ADR-06 resolution)

---

## DESIGN TOKEN AUDIT (DT-01 through DT-15) — ADR Escalation Assessment

The `planning/design-token-audit.md` identifies 15 decisions (DT-01 through DT-15). Cross-referencing with the ADRs:

| DT ID | Question | Already Covered by ADR? | Needs New ADR? |
|-------|----------|------------------------|----------------|
| DT-01 | Primary text #050505 vs #1c1916 | ADR-05 | No |
| DT-02 | Accent #f97250 vs #c45c3f | **CANDIDATE ADR-19 above** | Yes |
| DT-03 | Star #fbc02d vs #d4af37 | ADR-07 | No |
| DT-04 | Alt bg #f9f9f9 vs #f9f7f2 | ADR-01 | No |
| DT-05 | Soft text #4a4a4a vs #6a6a6a | **CANDIDATE ADR-16 above** | Yes |
| DT-06 | Muted text #8a8a8a vs #999999 | **CANDIDATE ADR-17 above** | Yes |
| DT-07 | Border #e6e6e6 vs #e5e2db | **CANDIDATE ADR-18 above** | Yes |
| DT-08 | Eyebrow letter-spacing | ADR-04 | No |
| DT-09 | Eyebrow font-weight | **CANDIDATE ADR-21 above** | Yes |
| DT-10 | Radius policy 0/2/4 vs expanded | ADR-06 covers 12px; 8px is CANDIDATE ADR-22 | Partial |
| DT-11 | PDP button radius 0 vs 6px | ADR-03 | No |
| DT-12 | Spacing scale gaps | No — off-scale values are implementation detail, not doc disagreement | No |
| DT-13 | Container max-widths | No — multiple values coexist by design (different contexts) | No |
| DT-14 | Transition 200ms vs 320ms | **CANDIDATE ADR-12 above** (partial) | Borderline |
| DT-15 | Tablet breakpoint | No — only one value exists (768px); question is "add one?" not "which is right?" | No |

---

## SUMMARY

**New architectural conflicts found beyond ADR-01–07:** 15 candidates documented above (ADR-08 through ADR-22).

**ADR Required (developer-blocking, two APPROVED/PENDING REVIEW docs genuinely disagree):**
- ADR-08: Pillar Strip content (5 vs 6 items, different labels)
- ADR-09: PDP CTA font size (14px vs 16px)
- ADR-11: Product card hover scale (1.02x vs 1.03x vs 1.04x)
- ADR-13: Coral on PDP CTA hover vs restraint rule
- ADR-15: Homepage section count (13 vs 16, different architecture)
- ADR-16: Soft text color (#4a4a4a vs #6a6a6a — accessibility)
- ADR-18: Border color warm vs cool (#e6e6e6 vs #e5e2db)
- ADR-19: PDP accent terracotta vs coral (#c45c3f vs #f97250)
- ADR-20: PDP internal $75/$150 contradiction (APPROVED doc is self-conflicting)
- ADR-21: Eyebrow font-weight (600 vs 700)

**Remediation tickets (not blocking, resolvable without Architect decision):**
- ADR-10: PDP CTA padding (snap to system tokens)
- ADR-12: Card hover duration (align to 320ms)
- ADR-14: PDP section title size (snap 42px → 44px token)
- ADR-17: Muted text color (pick one value)
- ADR-22: PDP gallery 8px radius (fold into ADR-06 resolution)

---

**Last Updated:** 2026-07-13
