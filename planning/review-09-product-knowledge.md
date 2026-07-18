# QA Review: 09-PRODUCT-KNOWLEDGE.md

**Reviewer:** Cursor (Build Engineer)  
**Date:** 2026-07-13  
**Document:** docs/09-PRODUCT-KNOWLEDGE.md  
**Status:** PENDING REVIEW  
**Lines:** 1,227

---

## Document Purpose

Every product fact, specification, variant, claim, and decision — sourced and cited. Contains the full product catalog (7 products), cross-product knowledge, competitive landscape, objection handling, production-ready reviews, studio terminology, customer demographics, asset inventory, shipping, live Shopify catalog data, and a source conflicts register.

---

## Source Coverage

**Sources listed in header:** Method and Conflicts fields listed but no explicit **Sources:** field. Sources are distributed throughout the body.

**Sources actually referenced in body:**
- docs/08-LIVE-SITE-COPY-AUDIT.md — heavily referenced (dozens of citations)
- manychat-kb/ (02, 03, 04, 05, 06, 07, 08, 10, 11, 14, 15) — ✓
- Barreletics_Research_Bible.md (Sections 1, 3, 5, 8) — ✓
- docs/04-COMPONENT-LIBRARY.md — ✓ (lines 117, 537, 562)
- docs/05-PDP-ARCHITECTURE.md — ✓ (lines 63, 89)
- Shopify catalog (live pull) — ✓ (lines 988–1205)
- barreletics.com homepage (live crawl) — ✓ (line 378)

**Verdict:** Excellent breadth of sources. The document pulls from nearly every repository source. Missing a **Sources:** field in the header but compensates with thorough per-section citations.

---

## Citation Coverage

**Total major sections:** 16  
**Sections with Source: citations:** 16/16  
**Individual block citations:** Nearly every code-fenced block and table has a Source: line.

**Coverage quality:** Excellent. This is the most comprehensively cited document in the repository.

---

## Missing Sources

1. **docs/10-DECISIONS.md** — not referenced anywhere. Product decisions (P-001 through P-011) from docs/10 directly mirror this document's content.
2. **docs/02-BRAND-SYSTEM.md** — not referenced. Brand positioning context is relevant.
3. **docs/03-DESIGN-SYSTEM.md** — not referenced. Design system naming conventions (Onyx, Stone) are documented here but not cross-referenced.

---

## Contradictions

### CRITICAL: Review Count — "297+" vs "294"

| Location | Value | Context |
|----------|-------|---------|
| Line 652 (Brand Credibility) | "297+ reviews" | Stated as of 2026-07-12 |
| Line 902 (Pain Points header) | "from 294 reviews" | Research Bible analysis |
| Line 917 (Delight Points header) | "from 294 reviews" | Research Bible analysis |

Same discrepancy as docs/01. No explanation for the gap.

### CRITICAL: Large Size Range — W 7.5–11 vs W 8–11

| Location | Value | Context |
|----------|-------|---------|
| Line 36 (Closed Sole size table) | L: W 7.5–11 | Main size table |
| Line 278 (Aquatic Performance Skins) | L (W 8–11) | Water shoes section |
| docs/10 P-002 | "Large (W 8–11 / M up to 10.5)" | Decision log |
| manychat-kb/03-sizing-chart.md | L: W 7.5–11 | Source material |

**Analysis:** The Closed Sole and Open Sole sizing table (line 36) shows L = W 7.5–11 (sourced from manychat-kb). The Aquatic section (line 278) says L = W 8–11. The L range starts at either 7.5 or 8 depending on where you look. This is an internal discrepancy within docs/09 AND a cross-document discrepancy with docs/10.

### MEDIUM: Discount Code Casing — "save15" vs "SAVE15"

| Location | Value |
|----------|-------|
| Line 25 (docs/09) | "code: save15" (lowercase) |
| docs/10 BZ-006 | "Code: SAVE15" (uppercase) |

Shopify discount codes are typically case-insensitive, but documentation should be consistent.

---

## Duplications

| Content | Also appears in | Severity |
|---------|----------------|----------|
| Customer pain/delight points (lines 902–928) | docs/01 lines 203–229 | Low (expected) |
| Target audience (lines 890–898) | docs/01 lines 148–155 | Low (expected) |
| Competitive landscape (lines 619–657) | docs/01 lines 175–199 | Low (expected) |
| Sock math (lines 539–562) | docs/01 lines 132–136; docs/02 lines 150–155 | Low (expected) |

**Analysis:** Duplications are expected and intentional — docs/09 is the product knowledge hub and should contain complete product context. Cross-references would be helpful but the duplication itself is not harmful.

---

## Unsupported Claims

1. **"Trusted by 1,000's of instructors & studios"** (line 651) — marketing claim, never substantiated with actual count.
2. **"4+ years proven durability"** (line 654) — supported by one customer anecdote (Kimberly), not systematic testing.

These are established marketing claims used throughout the brand. Flag but do not fail.

---

## Known Gaps

### Data Gaps

1. **Blue Heaven price missing.** Line 227 shows Blue Heaven with "—" for price. The Data Quality Flags section (line 1205) notes "0/-1 inventory, not visible on live site" but doesn't flag the missing price in the variant table. Should either show $74 (consistent with other colors) or explicitly note "DISCONTINUED — no active price."

2. **Coperni M inventory = -1.** Line 1107 shows -1 inventory. The Data Quality Flags section (line 1199) notes "Low" severity. The main Product 4 section (line 336) shows "Sold Out." However, neither section explicitly flags this as potentially requiring Shopify admin cleanup (negative inventory = oversold).

3. **No Sources field in header.** The header has Status, Purpose, Method, Conflicts — but no **Sources:** field listing the source documents.

### Cross-reference Gaps

4. **No reference to docs/10-DECISIONS.md** — product decisions P-001 through P-011 directly mirror this document.
5. **No reference to docs/02-BRAND-SYSTEM.md** — brand positioning context.
6. **No reference to docs/03-DESIGN-SYSTEM.md** — design naming conventions.

### Conflicts Register Gaps

7. **Size range conflict not in register.** The L size range discrepancy (W 7.5–11 vs W 8–11) is not listed in the Source Conflicts Register (lines 1210–1222). It should be.

---

## Exact Fixes Required

1. **Line 652** — Reconcile "297+" with "294" at lines 902/917, or add explanatory note: e.g., "297+ total (as of 2026-07-12); 294 analyzed in Research Bible."

2. **Line 278** — Change "L (W 8–11)" to "L (W 7.5–11)" to match the main sizing table at line 36, OR add a conflict entry to the register explaining the discrepancy.

3. **Line 25** — Standardize discount code to "SAVE15" (uppercase) to match docs/10, or verify live site casing and update both documents.

4. **Line 227** — Change Blue Heaven price from "—" to "$74 (DISCONTINUED)" or add a footnote explaining the missing price.

5. **Lines 1210–1222 (Conflicts Register)** — Add entry for size range discrepancy:
   ```
   | L size range | W 7.5–11 (manychat/size table) | W 8–11 (Aquatic section, docs/10) | Internal discrepancy |
   ```

6. **Header (after line 6)** — Add Sources field:
   ```
   **Sources:** docs/08-LIVE-SITE-COPY-AUDIT.md, manychat-kb/, Barreletics_Research_Bible.md, docs/04-COMPONENT-LIBRARY.md, docs/05-PDP-ARCHITECTURE.md, Shopify catalog (live pull 2026-07-13)
   ```

7. **Add cross-references** to docs/10, docs/02, docs/03 (anywhere appropriate — header or a dedicated Cross-References section).

---

## Final Recommendation

**CONDITIONAL**

This is the strongest document in the repository — comprehensive, well-structured, and thoroughly cited. The live Shopify data integration and Source Conflicts Register show excellent engineering discipline. The seven fixes above are all addressable: the size range discrepancy (W 7.5–11 vs W 8–11) is the most important because it directly affects customer-facing sizing guidance. Fix these and this passes cleanly.
