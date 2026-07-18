# Knowledge Base Consistency Audit

**Date:** 2026-07-13  
**Scope:** All APPROVED and PENDING REVIEW documents  
**Method:** Cross-document comparison of status, terminology, values, citations, cross-references, and structure

---

## CRITICAL

### CRIT-001: Color Palette Values Disagree Between APPROVED Documents

Two APPROVED documents declare different color values for the same design tokens:

| Token | docs/04-COMPONENT-LIBRARY.md (line 23–26) | docs/06-HOMEPAGE-ARCHITECTURE.md (CSS :root, lines 40–45) |
|-------|----|----|
| Alt background | `#f9f7f2` | `#f9f9f9` |
| Text (soft) | `#6a6a6a` | `#4a4a4a` |
| Text (muted) | `#999999` | `#8a8a8a` |
| Line (border) | `#e5e2db` | `#e6e6e6` |

docs/10-DECISIONS.md (D-007) uses the docs/06 values. docs/03-DESIGN-SYSTEM.md uses the docs/06 values (via Research Bible).

**Impact:** Any implementation following docs/04 will produce a different visual result from one following docs/06.

### CRIT-002: Free Shipping Threshold — $75 Still Present in APPROVED Doc

`docs/05-PDP-ARCHITECTURE.md` (APPROVED) contains BOTH values:
- Line 195: "free shipping over $150" ✓
- Line 264: "Free shipping on orders over $75" ✗ (outdated)
- Line 2197: "Free shipping over $75" ✗ (outdated)
- Line 2295: "free shipping over $75" ✗ (outdated)
- Line 2360: "Free shipping on orders over $75" ✗ (outdated)
- Line 2212: "Free shipping over $150" ✓

`docs/10-DECISIONS.md` (C-010) declares this RESOLVED at $150. `docs/08-LIVE-SITE-COPY-AUDIT.md` confirms $150. Yet 4 instances of $75 remain in `docs/05`.

**Impact:** Anyone reading the PDP spec will encounter contradictory shipping thresholds within the same document.

### CRIT-003: Button Border-Radius Contradiction in APPROVED Documents

- `docs/04-COMPONENT-LIBRARY.md` (APPROVED, line 37): "all square (border-radius: 0px)"
- `docs/05-PDP-ARCHITECTURE.md` (APPROVED, line 46): `border-radius: 6px` on `.pdp-buy__cta`
- `docs/05-PDP-ARCHITECTURE.md` (APPROVED, lines 230–231): `border-radius: 6px` on size buttons

Both documents are APPROVED. They directly contradict each other. `docs/10-DECISIONS.md` (D-003, CONFLICT-001) documents this but does not resolve it.

**Impact:** A developer must choose which APPROVED document to follow.

---

## HIGH

### HIGH-001: Eyebrow Letter-Spacing — Four Different Values in Knowledge Base

| Source | letter-spacing | weight | Status |
|--------|---------------|--------|--------|
| docs/04-COMPONENT-LIBRARY.md (line 12) | 0.14em | 700 | APPROVED |
| docs/03-DESIGN-SYSTEM.md (line 371) | 0.14em | 700 | PENDING REVIEW |
| docs/06-HOMEPAGE-ARCHITECTURE.md (CSS) | 0.08em, 0.12em, 0.15em, 0.18em (varies) | varies | APPROVED |
| docs/04-COMPONENT-LIBRARY.md (line 576) | 0.18em | — | APPROVED |
| docs/04-COMPONENT-LIBRARY.md (line 668) | 0.06em | 600 | APPROVED |

The APPROVED Component Library itself uses 3 different letter-spacing values (0.14em at line 12, 0.18em at line 576, 0.06em at line 668) in different component contexts.

### HIGH-002: PDP Text Color Divergence in APPROVED Document

- `docs/04-COMPONENT-LIBRARY.md` (APPROVED, line 20): Text primary = `#050505`
- `docs/06-HOMEPAGE-ARCHITECTURE.md` (APPROVED, line 42): `--br-text: #050505`
- `docs/06-HOMEPAGE-ARCHITECTURE.md` (APPROVED, line 4207): `[data-matured="on"]` override sets `--br-text: #1c1916`
- `docs/05-PDP-ARCHITECTURE.md` (APPROVED, line 24): body color = `#1c1916`

The PDP mock uses `#1c1916` and the Homepage has a matured override that also switches to `#1c1916`. The base token remains `#050505`. Both are APPROVED. Documented in docs/10 (CONFLICT-004) but not resolved.

### HIGH-006: Star/Rating Color Disagrees Between APPROVED Documents

- `docs/04-COMPONENT-LIBRARY.md` (APPROVED, line 22): Star rating = `#fbc02d`
- `docs/06-HOMEPAGE-ARCHITECTURE.md` (APPROVED, line 55): `--br-star: #fbc02d`
- `docs/05-PDP-ARCHITECTURE.md` (APPROVED, line 41): Stars = `#d4af37`

The PDP uses a distinctly different gold (`#d4af37`) from the design system gold (`#fbc02d`).

### HIGH-003: No Document References docs/07-COPY-GUIDE.md

`docs/07-COPY-GUIDE.md` (217,636 lines, PENDING REVIEW) is the largest document in the knowledge base. No other document in the `docs/` directory references it. It is effectively orphaned from the cross-reference graph.

### HIGH-004: docs/05 and docs/06 Have Zero Outbound Cross-References

Both APPROVED documents (`docs/05-PDP-ARCHITECTURE.md`, `docs/06-HOMEPAGE-ARCHITECTURE.md`) are raw HTML specifications with no cross-references to:
- docs/03 (Design System they implement)
- docs/04 (Component Library they draw from)
- docs/10 (Decisions that govern them)

### HIGH-005: PDP Review Card Radius Contradicts APPROVED Design System

- `docs/04-COMPONENT-LIBRARY.md` (APPROVED, lines 31–33): "No radius by default. Where matured uses radius: 2px or 4px only. Never use 12–16px."
- `docs/05-PDP-ARCHITECTURE.md` (APPROVED, line 67): Review cards use `border-radius: 12px`

Documented in docs/10 (CONFLICT-003) but both remain APPROVED without resolution.

---

## MEDIUM

### MED-001: Status Line Format Inconsistency

Three different formats across knowledge base documents:

| Format | Documents |
|--------|-----------|
| `**Status:** VALUE` (bold key) | 01, 02, 03, 04, 08-LIVE, 08-CREATIVE, 09, 10, 00, INDEX |
| `Status: VALUE` (plain text) | 05, 06, 07 |
| `**STATUS:** VALUE` (bold, ALL CAPS key) | 03 (line 410), 10 (line 1090) — used as document footer |

### MED-002: Document Header Format Inconsistency

| Format | Documents |
|--------|-----------|
| **Status** + **Purpose** + **Sources/Method** | 01, 02, 03, 09, 10 |
| **CRITICAL** warning + Status (no Purpose/Sources) | 05, 06, 07 |
| **Status** + **Purpose** (no Sources) | 04 |
| **Status** + Audit Date + Method + Source | 08-LIVE |

### MED-003: Duplicate "Double Failure" Concept Across 3 Documents

The exact concept "Your foot moves in the sock. The sock moves on the floor. Now neither does." appears in:
- `docs/01-BRAND-NORTH-STAR.md` (line 31)
- `docs/02-BRAND-SYSTEM.md` (line 145)
- `docs/10-DECISIONS.md` (B-008, line 370)

Could be replaced with one canonical location + cross-references.

### MED-004: Duplicate Brand Positioning Block

The block containing "Product: $74 'performance skin' — NOT a sock" + "Voice priority" + "Hero body" appears nearly verbatim in:
- `docs/01-BRAND-NORTH-STAR.md` (lines 38–40)
- `docs/02-BRAND-SYSTEM.md` (lines 159–161)
- `docs/10-DECISIONS.md` (B-001, B-002, B-011)

### MED-005: Duplicate Price Math

"Grip socks = $144–$336/year" comparison math appears in:
- `docs/01-BRAND-NORTH-STAR.md` (line 77)
- `docs/02-BRAND-SYSTEM.md` (lines 151–153)
- `docs/04-COMPONENT-LIBRARY.md` (HTML embeds)
- `docs/05-PDP-ARCHITECTURE.md` (HTML embeds)
- `docs/06-HOMEPAGE-ARCHITECTURE.md` (HTML embeds)
- `docs/09-PRODUCT-KNOWLEDGE.md` (comparison section)

### MED-006: Missing Cross-References in docs/01

`docs/01-BRAND-NORTH-STAR.md` discusses brand positioning, competitive landscape, and customer pain points — all of which are also covered in `docs/10-DECISIONS.md` (B-001 through B-016). No cross-reference exists between them.

### MED-007: Missing Cross-References in docs/02

`docs/02-BRAND-SYSTEM.md` references only `docs/06-HOMEPAGE-ARCHITECTURE.md` (line 17). Does not cross-reference:
- `docs/01-BRAND-NORTH-STAR.md` (overlapping content)
- `docs/10-DECISIONS.md` (where its decisions are cataloged)
- `docs/04-COMPONENT-LIBRARY.md` (which implements its slogan system)

### MED-008: docs/04 Component Library Uses #f9f7f2 While Noting Warm Palette Is "Dead Code"

`docs/06-HOMEPAGE-ARCHITECTURE.md` (line 38) explicitly states: "cream/plum palette in Shopify settings_data.json is dead code." Yet `docs/04-COMPONENT-LIBRARY.md` (line 23) uses `#f9f7f2` for alt-background, which is a warm cream tone closer to the "dead code" palette than the correct `#f9f9f9`.

### MED-009: Terminology Variance for Core Product

Multiple terms used interchangeably without a canonical hierarchy:
- "performance skin" (brand copy term)
- "Performance Skin" (title case, Shopify descriptions)
- "Grippy Shoes" (Shopify product title, founder story)
- "grip shoe" (slogan: "A new kind of grip shoe")
- "Grippy Footwear" (Shopify collection/category)
- "Performance Skin Footwear" (FAQ copy)
- "Performance Skin Grippy Shoes" (founder story)

`docs/10-DECISIONS.md` (N-006) addresses this partially but doesn't establish a hierarchy for all 7 variants.

### MED-010: docs/03 Design System Typography Table — Not Visible in Document

`docs/03-DESIGN-SYSTEM.md` references a "Typography table" for the --t-eyebrow spec (0.08em), but this is from the verbatim README source which contains a Markdown table. The actual table content specifying 0.08em is in the README block but the source conflict section (line 395) calls it "This document, Typography table (--t-eyebrow)" without a visible line reference within the document body above.

---

## LOW

### LOW-001: "Last Updated" vs "BUILD COMPLETE" vs "Audit Date"

| Document | Date Field Format |
|----------|-------------------|
| 05, 06, 07 | `Last Updated: 2026-07-12` |
| 03, 10 | `**BUILD COMPLETE:** 2026-07-13` (footer) |
| 08-LIVE | `**Audit Date:** 2026-07-12` |
| 01, 02, 04, 09 | No date field |

### LOW-002: Citation Format — "Source:" Placement Varies

- docs/01, 02, 09: `Source:` on its own line below a code block
- docs/03 (line 366): `Source:` below a section heading
- docs/10: `Source:` below a code block (consistent with 01/02/09)
- docs/04: Uses `**HTML Source:**` and `**Source:**` (bold key, different label)

### LOW-003: "Section" Numbering Convention Inconsistency

- `docs/03-DESIGN-SYSTEM.md` and decision matrix use section numbers 01–29
- `docs/04-COMPONENT-LIBRARY.md` uses unnamed section sequences (lines 931–959)
- No single canonical list maps both naming systems

### LOW-004: docs/02 Section Numbering Doesn't Match Other Documents

`docs/02-BRAND-SYSTEM.md` uses internal section numbers (1–5) which are not related to the section numbers used in the decision matrix (01–29) or the homepage section order in docs/03.

### LOW-005: Discount Code Casing Mismatch

- `docs/09-PRODUCT-KNOWLEDGE.md` (line 25): `save15` (lowercase)
- `docs/10-DECISIONS.md` (BZ-006): `SAVE15` (uppercase)

Shopify discount codes are case-insensitive, but documentation should be consistent.

### LOW-007: Shopify Size Range — Minor Variance

- `docs/09-PRODUCT-KNOWLEDGE.md`: "Medium (W 5.5–7.5) and Large (W 8–11 / M up to 10.5)"
- `docs/09-PRODUCT-KNOWLEDGE.md` (footwear table, line 36): Large = W 7.5–11
- `docs/05-PDP-ARCHITECTURE.md` (line 230–231): "Women 5–7.5 · Men 6–8" (M), "Women 8–10 · Men 8.5–11" (L)

Internal to docs/09: the summary says L = "W 8–11" but the footwear table says L = "W 7.5–11". Men's range in docs/05 is more specific than the KB entry.

### LOW-008: "Trusted by 1,000's" — Apostrophe Variance

- docs/02 (line 13, 45): "1,000's"
- docs/04 (line 109–114): "1,000's" 
- Some HTML in docs/06: "1,000+" (different claim)

### LOW-009: Review Count Internal Discrepancy (docs/09)

- `docs/09-PRODUCT-KNOWLEDGE.md` (line 652): "297+ reviews"
- `docs/09-PRODUCT-KNOWLEDGE.md` (lines 902, 917): "294 reviews"

### LOW-010: docs/10 References "docs/02–09" in Header

`docs/10-DECISIONS.md` (line 6) lists sources as "docs/02–09" which is a range reference. This is imprecise — it doesn't actually source from docs/07 (Copy Guide, which is raw HTML) or docs/08-LIVE (which is audit evidence, not decisions).

### LOW-011: Coperni Price — $115 Stated Without SKU Source

`docs/10-DECISIONS.md` (P-001) and `docs/09-PRODUCT-KNOWLEDGE.md` both state Coperni = $115. The Shopify data shows this price but the product has 0 inventory across all variants. No note that this product may be inactive.

---

## OPPORTUNITIES TO REPLACE DUPLICATION WITH CROSS-REFERENCES

| Duplicated Content | Appears In | Canonical Location | Action |
|----|----|----|-----|
| Double Failure concept | 01, 02, 10 | docs/02 (Section 4) | Others should cite docs/02 |
| Brand positioning block ($74, not a sock, voice priority) | 01, 02, 10 | docs/02 (Section 4) | Others should cite docs/02 |
| Price Math ($144–$336/year comparison) | 01, 02, 04, 05, 06, 09 | docs/09 (Comparison section) | Structured docs should cite docs/09 |
| Hero eyebrow 5 slogans | 02, 04, 10 | docs/02 (Section 2) | Others should cite docs/02 |
| Color palette values | 03, 04, 06, 10 | docs/06 (:root CSS) or docs/03 | Resolve disagreement first |
| Sizing info (M/L ranges) | 05, 09 | docs/09 (Size Chart) | docs/05 is raw spec; no change needed |
| Shipping/returns policy details | 09, 10 | docs/09 (Shipping section) | docs/10 should cite docs/09 |

---

## SUMMARY

| Severity | Count |
|----------|-------|
| Critical | 3 |
| High | 6 |
| Medium | 10 |
| Low | 11 |
| **Total** | **30** |

The 3 Critical findings all involve contradictions between APPROVED documents where a developer would receive conflicting instructions. These should be resolved before implementation begins.

---

**END OF AUDIT**
