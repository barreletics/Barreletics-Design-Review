# QA Review: 01-BRAND-NORTH-STAR.md

**Reviewer:** Cursor (Build Engineer)  
**Date:** 2026-07-13  
**Document:** docs/01-BRAND-NORTH-STAR.md  
**Status:** PENDING REVIEW  
**Lines:** 249

---

## Document Purpose

Brand vision, mission, core values, origin, and positioning — the foundational WHY document. Contains founder story, brand positioning, category ownership, brand promise, core values, target audience, market context, competitive landscape, brand credibility, customer pain/delight points, and brand rules.

---

## Source Coverage

**Sources listed in header:** Shopify product descriptions, Barreletics_Research_Bible.md, manychat-kb/, docs/08-LIVE-SITE-COPY-AUDIT.md

**Sources actually referenced in body:**
- Shopify product description body HTML (Open Sole, Closed Sole, Yoga Tight) — ✓
- Barreletics_Research_Bible.md Sections 1, 4, 5, 6 — ✓
- manychat-kb/05-why-better-than-socks.md — ✓
- docs/08-LIVE-SITE-COPY-AUDIT.md — ✓
- docs/09-PRODUCT-KNOWLEDGE.md — ✓ (referenced in line 17)
- docs/03-DESIGN-SYSTEM.md — ✓ (referenced in line 243)
- docs/02-BRAND-SYSTEM.md — ✓ (referenced in line 42)

**Verdict:** Sources header is incomplete — docs/09, docs/03, and docs/02 are cited in the body but not listed in the header Sources field.

---

## Citation Coverage

**Total sections:** 12 major sections  
**Sections with Source: citations:** 12/12  
**Individual block citations:** Every code-fenced block has a Source: line immediately following.

**Coverage quality:** Excellent. This is one of the best-cited documents in the repository.

---

## Missing Sources

1. **Header Sources field** should include docs/09-PRODUCT-KNOWLEDGE.md, docs/02-BRAND-SYSTEM.md, and docs/03-DESIGN-SYSTEM.md (all three are cited in the body but omitted from header).

---

## Contradictions

### CRITICAL: Review Count — "297+" vs "294"

| Location | Value | Source cited |
|----------|-------|-------------|
| Line 195 (Brand Credibility) | "297+ reviews (as of 2026-07-12)" | Research Bible + docs/08 |
| Line 203 (Pain Points header) | "from 294 reviews" | Research Bible Section 5 |
| Line 218 (Delight Points header) | "from 294 reviews" | Research Bible Section 5 |

**Analysis:** "297+" appears to be the live review count as of 2026-07-12. "294" appears to be the count from the Research Bible's analysis (likely from an earlier date). Both coexist without explanation. This same discrepancy exists in docs/09.

### MINOR: ClassPass/Lagree Trend Claim

Line 166: "Lagree named fastest-growing fitness trend in US by ClassPass (2019), still expanding" — sourced only to Research Bible Section 5. The original ClassPass study is not independently verifiable from within the repository. The "(2019)" date makes this 7 years old.

---

## Duplications

| Content | Also appears in | Severity |
|---------|----------------|----------|
| Double Failure concept (line 31) | docs/02-BRAND-SYSTEM.md Section 4 (line 145) | Medium |
| Brand positioning / product positioning (lines 28–42) | docs/02-BRAND-SYSTEM.md Section 4 (lines 157–163) | Medium |
| Price math (lines 77–79, 132–136) | docs/02-BRAND-SYSTEM.md Section 4 (lines 150–155), docs/09 Sock Math section | Medium |
| Customer pain/delight points (lines 203–229) | docs/09-PRODUCT-KNOWLEDGE.md (lines 902–928) | Low (expected) |
| Target audience (lines 148–155) | docs/09-PRODUCT-KNOWLEDGE.md (lines 890–898) | Low (expected) |

**Analysis:** The overlaps with docs/02 are the most concerning — the Brand Positioning and Brand Intelligence sections in docs/02 substantially duplicate docs/01's core content. The overlaps with docs/09 are expected given different document purposes.

---

## Unsupported Claims

1. **"Megaformer has 200+ patents, 30+ countries, 250+ exercises"** (line 167) — sourced to Research Bible, but the Research Bible is the terminal source. These are third-party manufacturer claims not independently verified.
2. **"Lagree named fastest-growing fitness trend in US by ClassPass (2019)"** (line 166) — 7-year-old claim, cited to Research Bible only.
3. **"Trusted by 1,000's of instructors"** (line 194) — used as marketing copy throughout. The "'s" implies thousands but the specific number is never substantiated.

**Note:** Items 1–2 are fair to keep as Research Bible claims since this is a brand document, not an external-facing fact sheet. Item 3 is approved marketing copy. Flag but do not fail.

---

## Known Gaps

1. No reference to docs/10-DECISIONS.md (the decision log documents many brand-level decisions that this doc establishes).
2. No explicit cross-reference explaining the relationship between docs/01 and docs/02 (what belongs where).
3. No "How to Use This Document" guidance — what is docs/01 for vs docs/02?

---

## Exact Fixes Required

1. **Line 6** — Add docs/09-PRODUCT-KNOWLEDGE.md, docs/02-BRAND-SYSTEM.md, docs/03-DESIGN-SYSTEM.md to Sources field.
2. **Line 195** — Either change "297+" to "294+" to match pain/delight sections, or add a note: "(297+ total on live site; 294 analyzed in Research Bible)".
3. **Lines 203, 218** — If keeping both numbers, add a parenthetical explaining "294" is the Research Bible analysis count.
4. **Line 166** — Add "(2019 data)" caveat or note age of ClassPass claim.
5. **Line 167** — Add "per manufacturer claims" qualifier to Megaformer stats.

---

## Final Recommendation

**CONDITIONAL**

The document is well-structured, thoroughly cited, and genuinely useful as a foundational brand reference. The review count discrepancy (297+ vs 294) is the only issue that could cause downstream confusion — it propagates to docs/09 and any future document that references review counts. Fix the five items above and this passes.
