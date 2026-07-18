# Consistency Remediation Plan

**Date:** 2026-07-13  
**Source:** planning/knowledge-base-consistency-audit.md (30 findings)  
**Purpose:** Implementation tickets for every finding — frozen until assigned

---

## CRITICAL TICKETS

---

### TICKET CRIT-001: Resolve Color Palette Disagreement Between docs/04 and docs/06

**Priority:** Critical  
**Affected files:** docs/04-COMPONENT-LIBRARY.md (lines 23–26), docs/06-HOMEPAGE-ARCHITECTURE.md (lines 40–45), docs/10-DECISIONS.md (D-007)  
**Root cause:** docs/04 was written from a different source (design handoff summary with warm tones) while docs/06 was extracted from the actual CSS :root tokens. The two were never reconciled.  
**Recommended fix:** Update docs/04 lines 23–26 to match the docs/06 :root values (#f9f9f9, #4a4a4a, #8a8a8a, #e6e6e6). Add a note that the warm #f9f7f2/#e5e2db values are from an earlier design pass and were superseded.  
**Dependencies:** Architect decision — which set of values is canonical?  
**Complexity:** S  
**ChatGPT approval required:** Yes — modifies APPROVED document and requires design decision  
**Groupable with:** CRIT-003, HIGH-002, HIGH-005, HIGH-006 (all involve reconciling docs/04 vs docs/05/06 values)

---

### TICKET CRIT-002: Remove Outdated $75 Shipping Threshold from docs/05

**Priority:** Critical  
**Affected files:** docs/05-PDP-ARCHITECTURE.md (lines 264, 2197, 2295, 2360)  
**Root cause:** The PDP specification was written when the threshold was $75. When the business changed it to $150, only some instances were updated. The document preserves raw HTML verbatim, so the outdated copy remained.  
**Recommended fix:** Replace all 4 instances of "$75" with "$150" in docs/05. Add an inline annotation: `<!-- Updated 2026-07-13: threshold changed from $75 to $150 per BZ-005 -->` at first instance.  
**Dependencies:** None — this is already resolved per docs/10 (C-010) and confirmed by live site.  
**Complexity:** S  
**ChatGPT approval required:** Yes — modifies APPROVED document  
**Groupable with:** None (standalone text replacement)

---

### TICKET CRIT-003: Resolve Button Border-Radius Contradiction

**Priority:** Critical  
**Affected files:** docs/04-COMPONENT-LIBRARY.md (line 37), docs/05-PDP-ARCHITECTURE.md (lines 46, 230–231), docs/10-DECISIONS.md (D-003, CONFLICT-001)  
**Root cause:** The Component Library declares a system-wide rule (0px square) while the PDP mock was designed with 6px radius on CTAs and size pills. Neither document acknowledges the other's rule.  
**Recommended fix:** Two options:  
- (A) Declare PDP CTA/size buttons as an explicit exception to D-003 in docs/04 and docs/10.  
- (B) Update docs/05 PDP CSS to use 0px radius, matching the system rule.  
Requires Architect decision on which is the intended production behavior.  
**Dependencies:** Architect decision. Blocks implementation of PDP.  
**Complexity:** S (text change) or M (if PDP mock needs visual re-evaluation)  
**ChatGPT approval required:** Yes — design decision between two APPROVED docs  
**Groupable with:** CRIT-001, HIGH-005 (all radius/color reconciliation between docs/04 and docs/05)

---

## HIGH TICKETS

---

### TICKET HIGH-001: Resolve Eyebrow Letter-Spacing to One Canonical Value

**Priority:** High  
**Affected files:** docs/04-COMPONENT-LIBRARY.md (lines 12, 576, 668), docs/03-DESIGN-SYSTEM.md (lines 371, 395–398), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS throughout), docs/10-DECISIONS.md (D-018, C-002)  
**Root cause:** Multiple source documents (Research Bible, design handoff README, homepage CSS, component-specific sections) each defined eyebrow styling independently. No single authority was established.  
**Recommended fix:** Architect decides the canonical eyebrow spec (one value). Update docs/04 line 12 to be the system rule. Document that component-specific variations (0.18em for manifesto, 0.06em for closing CTAs) are intentional per-component overrides — not the system default. Resolve C-002 in docs/10.  
**Dependencies:** Architect decision on canonical value (0.08em or 0.14em).  
**Complexity:** M  
**ChatGPT approval required:** Yes — design decision  
**Groupable with:** HIGH-002 (both involve resolving design token conflicts)

---

### TICKET HIGH-002: Resolve PDP Text Color (#1c1916 vs #050505)

**Priority:** High  
**Affected files:** docs/04-COMPONENT-LIBRARY.md (line 20), docs/05-PDP-ARCHITECTURE.md (line 24+), docs/06-HOMEPAGE-ARCHITECTURE.md (line 4207), docs/10-DECISIONS.md (D-036, C-004)  
**Root cause:** The matured direction intentionally uses a warmer ink (#1c1916) but this was never formalized as a system-level decision. The base token `--br-text` remains #050505.  
**Recommended fix:** Two options:  
- (A) Change system token to #1c1916 (since both PDP and matured homepage use it).  
- (B) Document #1c1916 as the "matured override" that replaces #050505 everywhere.  
Update docs/04, resolve C-004 in docs/10.  
**Dependencies:** Architect decision — is #050505 dead code?  
**Complexity:** M  
**ChatGPT approval required:** Yes — modifies APPROVED documents + design decision  
**Groupable with:** HIGH-001, HIGH-006 (all design token reconciliation)

---

### TICKET HIGH-003: Add Cross-References TO docs/07-COPY-GUIDE.md

**Priority:** High  
**Affected files:** docs/01-BRAND-NORTH-STAR.md, docs/02-BRAND-SYSTEM.md, docs/09-PRODUCT-KNOWLEDGE.md, docs/10-DECISIONS.md  
**Root cause:** docs/07 was built as a raw HTML archive and other documents were written without referencing it. It contains the actual source copy that other docs describe in structured form.  
**Recommended fix:** Add a cross-reference line to docs/01, 02, 09, and 10 headers: `**Copy archive:** docs/07-COPY-GUIDE.md (complete HTML source for all approved copy)`  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — structural edit (auto-approve per WORKFLOW.md)  
**Groupable with:** HIGH-004, MED-006, MED-007 (all cross-reference additions)

---

### TICKET HIGH-004: Add Cross-Reference Headers to docs/05 and docs/06

**Priority:** High  
**Affected files:** docs/05-PDP-ARCHITECTURE.md, docs/06-HOMEPAGE-ARCHITECTURE.md  
**Root cause:** These documents were migrated as raw HTML specifications. No cross-reference section was added because they are "source of truth" artifacts rather than structured knowledge docs.  
**Recommended fix:** Add a `## RELATED DOCUMENTS` section at the top of each (after the header):  
```
## RELATED DOCUMENTS
- Design tokens: docs/03-DESIGN-SYSTEM.md
- Component specs: docs/04-COMPONENT-LIBRARY.md
- Decision log: docs/10-DECISIONS.md
- Product data: docs/09-PRODUCT-KNOWLEDGE.md
```  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** Yes — modifies APPROVED documents (but content-neutral addition)  
**Groupable with:** HIGH-003, MED-006, MED-007 (all cross-reference work)

---

### TICKET HIGH-005: Resolve PDP Review Card 12px Radius Contradiction

**Priority:** High  
**Affected files:** docs/04-COMPONENT-LIBRARY.md (lines 31–33), docs/05-PDP-ARCHITECTURE.md (line 67), docs/10-DECISIONS.md (D-038, CONFLICT-003)  
**Root cause:** Same as CRIT-003 — PDP mock was designed with rounded cards while system rule says no radius.  
**Recommended fix:** Architect decides: is 12px on review cards an intentional PDP exception or a design system violation? Document the decision in docs/10 (resolve C-003). If exception, add it to docs/04 as a documented PDP-specific override.  
**Dependencies:** Architect decision. Related to CRIT-003.  
**Complexity:** S  
**ChatGPT approval required:** Yes — design decision  
**Groupable with:** CRIT-003 (same class of conflict)

---

### TICKET HIGH-006: Resolve Star/Rating Color (#fbc02d vs #d4af37)

**Priority:** High  
**Affected files:** docs/04-COMPONENT-LIBRARY.md (line 22), docs/05-PDP-ARCHITECTURE.md (line 41), docs/06-HOMEPAGE-ARCHITECTURE.md (line 55), docs/10-DECISIONS.md (D-007)  
**Root cause:** PDP mock (v36) uses a darker gold (#d4af37) while the design system and homepage both use #fbc02d. Likely the PDP was designed separately without referencing the token.  
**Recommended fix:** Align PDP to system token (#fbc02d) OR formalize #d4af37 as the new canonical value. Update docs/10 D-007 to reflect whichever is chosen.  
**Dependencies:** Architect decision — visual preference.  
**Complexity:** S  
**ChatGPT approval required:** Yes — design decision + modifies APPROVED doc  
**Groupable with:** HIGH-002, CRIT-001 (all color token reconciliation)

---

## MEDIUM TICKETS

---

### TICKET MED-001: Standardize Status Line Format

**Priority:** Medium  
**Affected files:** docs/05-PDP-ARCHITECTURE.md (line 7), docs/06-HOMEPAGE-ARCHITECTURE.md (line 7), docs/07-COPY-GUIDE.md (line 8)  
**Root cause:** docs/05, 06, 07 were written before the bold-key format convention was established. They use plain `Status: VALUE`.  
**Recommended fix:** Change to `**Status:** VALUE` in all three files. Standardize footer format to `**STATUS:** VALUE` (all caps key) for document closers.  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** Yes — modifies APPROVED documents (but format-only)  
**Groupable with:** MED-002, LOW-001 (all formatting standardization)

---

### TICKET MED-002: Standardize Document Header Structure

**Priority:** Medium  
**Affected files:** docs/04-COMPONENT-LIBRARY.md, docs/05-PDP-ARCHITECTURE.md, docs/06-HOMEPAGE-ARCHITECTURE.md, docs/07-COPY-GUIDE.md, docs/08-LIVE-SITE-COPY-AUDIT.md  
**Root cause:** Documents were created at different times with different conventions. No header template was established until the later builds.  
**Recommended fix:** Define a canonical header template in WORKFLOW.md. Retrofit all documents to include: Status, Purpose, Primary Source, and Build Date. For lossless HTML docs (05, 06, 07), add these as a structured block above the CRITICAL warning.  
**Dependencies:** None  
**Complexity:** M  
**ChatGPT approval required:** Yes — modifies APPROVED documents  
**Groupable with:** MED-001, LOW-001 (all header/format work)

---

### TICKET MED-003: Deduplicate "Double Failure" Concept

**Priority:** Medium  
**Affected files:** docs/01-BRAND-NORTH-STAR.md (line 31), docs/02-BRAND-SYSTEM.md (line 145), docs/10-DECISIONS.md (B-008)  
**Root cause:** Each document was built independently with lossless extraction from the same source (Research Bible Section 1). The concept was included wherever it appeared relevant.  
**Recommended fix:** Designate docs/02 Section 4 as canonical location. In docs/01 and docs/10, replace verbatim text with: `See docs/02-BRAND-SYSTEM.md Section 4 (Double Failure Concept)` after a brief one-line reference.  
**Dependencies:** None — content remains in docs/02  
**Complexity:** S  
**ChatGPT approval required:** No — structural edit (reduces duplication without changing meaning)  
**Groupable with:** MED-004, MED-005 (all deduplication work)

---

### TICKET MED-004: Deduplicate Brand Positioning Block

**Priority:** Medium  
**Affected files:** docs/01-BRAND-NORTH-STAR.md (lines 38–40), docs/02-BRAND-SYSTEM.md (lines 159–161), docs/10-DECISIONS.md (B-001, B-002, B-011)  
**Root cause:** Same as MED-003 — parallel extraction from same source.  
**Recommended fix:** Keep full text in docs/02 (Section 4 — Brand Intelligence). In docs/01, add cross-reference: `Cross-reference: Full positioning rules in docs/02-BRAND-SYSTEM.md Section 4`. In docs/10, decisions B-001/B-002/B-011 should cite docs/02 as canonical (already do — no change needed there).  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — structural edit  
**Groupable with:** MED-003, MED-005 (all deduplication)

---

### TICKET MED-005: Add Cross-Reference Notes for Duplicated Price Math

**Priority:** Medium  
**Affected files:** docs/01-BRAND-NORTH-STAR.md (line 77), docs/02-BRAND-SYSTEM.md (lines 151–153)  
**Root cause:** Price math ($144–$336/year comparison) is repeated in structured docs. In HTML docs (04, 05, 06) it's embedded copy and cannot be deduplicated.  
**Recommended fix:** In docs/01 and docs/02 where price math appears, add: `Cross-reference: Complete pricing and comparison data in docs/09-PRODUCT-KNOWLEDGE.md`. Do NOT remove from HTML docs (they are lossless archives).  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — structural edit  
**Groupable with:** MED-003, MED-004 (all deduplication)

---

### TICKET MED-006: Add Cross-References from docs/01 to docs/10

**Priority:** Medium  
**Affected files:** docs/01-BRAND-NORTH-STAR.md  
**Root cause:** docs/01 was built before docs/10 existed.  
**Recommended fix:** Add to docs/01 header Sources line: `, docs/10-DECISIONS.md (brand decisions B-001–B-016)`. Add inline cross-references where competitive landscape and positioning decisions are discussed.  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — structural edit  
**Groupable with:** HIGH-003, HIGH-004, MED-007 (all cross-reference additions)

---

### TICKET MED-007: Add Cross-References from docs/02 to Related Documents

**Priority:** Medium  
**Affected files:** docs/02-BRAND-SYSTEM.md  
**Root cause:** docs/02 was built early and only references docs/06. Later documents (01, 04, 10) overlap significantly.  
**Recommended fix:** Update docs/02 Sources header to include: `docs/01-BRAND-NORTH-STAR.md (brand positioning), docs/04-COMPONENT-LIBRARY.md (slogan implementation), docs/10-DECISIONS.md (brand decisions catalog)`.  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — structural edit  
**Groupable with:** HIGH-003, HIGH-004, MED-006 (all cross-reference additions)

---

### TICKET MED-008: Correct docs/04 Alt-Background to Match System Token

**Priority:** Medium  
**Affected files:** docs/04-COMPONENT-LIBRARY.md (line 23)  
**Root cause:** docs/04 uses #f9f7f2 (warm cream), but docs/06 CSS explicitly labels the cream/plum palette as "dead code" and uses #f9f9f9.  
**Recommended fix:** Change docs/04 line 23 from `#f9f7f2` to `#f9f9f9`. This is part of CRIT-001 but specifically addresses the "dead code" contradiction.  
**Dependencies:** CRIT-001 resolution (same fix)  
**Complexity:** S  
**ChatGPT approval required:** Yes — modifies APPROVED document  
**Groupable with:** CRIT-001 (same fix scope)

---

### TICKET MED-009: Establish Product Terminology Hierarchy

**Priority:** Medium  
**Affected files:** docs/10-DECISIONS.md (N-006), potentially docs/02-BRAND-SYSTEM.md  
**Root cause:** N-006 defines the SEO vs brand split for "Grippy Shoes" vs "performance skin" but doesn't address the 5 other variants.  
**Recommended fix:** Expand N-006 in docs/10 to include a complete terminology table:  
| Context | Term | Usage |  
|---------|------|-------|  
| Body copy / brand | performance skin | Always |  
| SEO titles | Grippy Shoes | Shopify titles |  
| Collections | Grippy Footwear | Nav/categories |  
| Founder story | Performance Skin Grippy Shoes | Verbatim quote |  
| Customer-facing FAQ | Performance Skin Footwear | Full name |  
| Slogans | grip shoe | Casual/creative |  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — expanding existing decision documentation  
**Groupable with:** None (standalone)

---

### TICKET MED-010: Add Line Reference for Typography Table in docs/03

**Priority:** Medium  
**Affected files:** docs/03-DESIGN-SYSTEM.md (line 395)  
**Root cause:** The SOURCE CONFLICTS section references "This document, Typography table (--t-eyebrow)" but the README content above doesn't have explicit line numbers visible to readers.  
**Recommended fix:** Add a specific line reference: "This document, line ~149 (--t-eyebrow token definition)" so readers can locate it. Or add a markdown anchor `### Typography Tokens` before that section for cross-reference clarity.  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — structural/navigational improvement  
**Groupable with:** None (standalone)

---

## LOW TICKETS

---

### TICKET LOW-001: Standardize Date Field Format

**Priority:** Low  
**Affected files:** docs/01, 02, 03, 04, 05, 06, 07, 08, 09, 10  
**Root cause:** No convention was established before documents were built.  
**Recommended fix:** Add `**Build Date:** YYYY-MM-DD` to all document headers. Remove "Last Updated" / "BUILD COMPLETE" / "Audit Date" variations. Define format in WORKFLOW.md.  
**Dependencies:** MED-002 (header standardization)  
**Complexity:** S  
**ChatGPT approval required:** Yes — modifies APPROVED documents (format only)  
**Groupable with:** MED-001, MED-002 (all formatting work)

---

### TICKET LOW-002: Standardize Citation Format

**Priority:** Low  
**Affected files:** docs/04-COMPONENT-LIBRARY.md  
**Root cause:** docs/04 uses `**HTML Source:**` and `**Source:**` (bold) while all other docs use plain `Source:`.  
**Recommended fix:** Change docs/04 bold source labels to plain `Source:` to match convention. Define canonical format in WORKFLOW.md.  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** Yes — modifies APPROVED document (format only)  
**Groupable with:** LOW-001, MED-001 (all formatting)

---

### TICKET LOW-003: Create Section Number Cross-Reference Map

**Priority:** Low  
**Affected files:** docs/10-DECISIONS.md (Section Decisions), docs/04-COMPONENT-LIBRARY.md  
**Root cause:** The decision matrix uses numbered sections (01–29) while the Component Library describes sections by name. No mapping exists.  
**Recommended fix:** Add a cross-reference table to docs/10 (after the Section Decisions block) mapping section numbers to section names: `| 01 | Hero | 03 | 50/50 Progress | ...`  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — additive documentation  
**Groupable with:** LOW-004 (both section numbering issues)

---

### TICKET LOW-004: Add Internal Section Numbering Note to docs/02

**Priority:** Low  
**Affected files:** docs/02-BRAND-SYSTEM.md  
**Root cause:** The internal "Section 1–5" headings in docs/02 are unrelated to the homepage Section 01–29 system.  
**Recommended fix:** Add a note at top of docs/02: `Note: Section numbers (1–5) in this document are internal chapter headings, not related to homepage section numbers (01–29) used in the decision matrix.`  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — navigational clarification  
**Groupable with:** LOW-003 (both numbering clarity)

---

### TICKET LOW-005: Standardize Discount Code Casing

**Priority:** Low  
**Affected files:** docs/09-PRODUCT-KNOWLEDGE.md (line 25), docs/10-DECISIONS.md (BZ-006)  
**Root cause:** Different source documents used different casing. Shopify codes are case-insensitive.  
**Recommended fix:** Standardize to uppercase `SAVE15` everywhere (matches how it appears in site announcements per docs/08-LIVE-SITE-COPY-AUDIT.md: "Use save15"). Alternatively, standardize to lowercase `save15` (matches live announcement bar copy).  
**Dependencies:** Verify live site casing preference.  
**Complexity:** S  
**ChatGPT approval required:** No — documentation consistency  
**Groupable with:** None (standalone text fix)

---

### TICKET LOW-007: Reconcile Large Women's Size Range in docs/09

**Priority:** Low  
**Affected files:** docs/09-PRODUCT-KNOWLEDGE.md (summary vs footwear table)  
**Root cause:** The summary states L = "W 8–11" but the detailed table says L = "W 7.5–11". Different source documents (ManyChat KB vs Shopify) use different boundaries.  
**Recommended fix:** Verify against live size chart. Update summary to match the table (7.5–11 if that's what Shopify shows) OR note that 7.5 is a crossover size: "Medium fits up to 7.5; Large fits 7.5–11 (7.5 can go either way)."  
**Dependencies:** Live site verification  
**Complexity:** S  
**ChatGPT approval required:** No — factual correction  
**Groupable with:** None (standalone)

---

### TICKET LOW-008: Clarify "1,000's" vs "1,000+" Claim

**Priority:** Low  
**Affected files:** docs/02-BRAND-SYSTEM.md, docs/06-HOMEPAGE-ARCHITECTURE.md  
**Root cause:** Most locations use "1,000's" (brand copy from manychat-kb) but some homepage HTML uses "1,000+". These are equivalent claims but differ in presentation.  
**Recommended fix:** Note in docs/10 or docs/02 that both forms are approved variants of the same claim. No need to force-standardize since they appear in different contexts (structured copy vs HTML embed).  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — documentation note  
**Groupable with:** None (standalone)

---

### TICKET LOW-009: Reconcile Review Count in docs/09

**Priority:** Low  
**Affected files:** docs/09-PRODUCT-KNOWLEDGE.md (lines 652, 902, 917)  
**Root cause:** Review count was pulled from different sources at different times. 297+ is from one section; 294 from another. Both are from the same crawl date so this is likely a counting discrepancy between two source URLs.  
**Recommended fix:** Verify current count via live site or Shopify/JudgeMe. Update to single consistent number with `(as of YYYY-MM-DD)` qualifier.  
**Dependencies:** Live data verification  
**Complexity:** S  
**ChatGPT approval required:** No — factual correction  
**Groupable with:** None (standalone)

---

### TICKET LOW-010: Fix Imprecise Source Range in docs/10 Header

**Priority:** Low  
**Affected files:** docs/10-DECISIONS.md (line 6)  
**Root cause:** Shorthand "docs/02–09" was used for brevity but implies all 8 documents. In reality, decisions were not sourced from docs/07 or docs/08-LIVE.  
**Recommended fix:** Replace `docs/02–09` with explicit list: `docs/02, 03, 04, 05, 06, 09`.  
**Dependencies:** None  
**Complexity:** S  
**ChatGPT approval required:** No — accuracy correction  
**Groupable with:** None (standalone)

---

### TICKET LOW-011: Add Inventory Status Note for Coperni Product

**Priority:** Low  
**Affected files:** docs/09-PRODUCT-KNOWLEDGE.md, docs/10-DECISIONS.md (P-001)  
**Root cause:** Coperni is documented at $115 with full variant details, but Shopify shows 0 inventory across all variants. No note about whether this is discontinued, sold out, or seasonal.  
**Recommended fix:** Add a `Status: 0 inventory across all variants (as of 2026-07-13). May be seasonal/sold out/discontinued.` note to the Coperni section in docs/09 and a parenthetical in docs/10 P-001.  
**Dependencies:** Business verification — is Coperni active?  
**Complexity:** S  
**ChatGPT approval required:** No — factual annotation  
**Groupable with:** None (standalone)

---

## IMPLEMENTATION BATCHES

---

### BATCH 1: Design Token Reconciliation (BLOCKED — requires Architect decisions)

**Tickets:** CRIT-001, CRIT-003, HIGH-001, HIGH-002, HIGH-005, HIGH-006, MED-008  
**Theme:** Resolve all color, radius, and typography conflicts between APPROVED documents

**Files affected:**
- docs/04-COMPONENT-LIBRARY.md (lines 12, 20, 22, 23–26, 31–33, 37)
- docs/05-PDP-ARCHITECTURE.md (lines 41, 46, 67, 230–231)
- docs/06-HOMEPAGE-ARCHITECTURE.md (lines 40–45, 55, 4207)
- docs/03-DESIGN-SYSTEM.md (lines 371, 395–398)
- docs/10-DECISIONS.md (D-003, D-007, D-018, D-036, D-038, C-001–C-006)

**Dependencies:**
- ADR-01 through ADR-07 decisions from ChatGPT
- All 7 conflicts must be resolved before any implementation begins

**Required approvals:** ChatGPT approval for ALL changes (modifies APPROVED documents + design decisions)

**Safe execution order:**
1. Color palette alignment (CRIT-001 + MED-008) — single commit
2. Typography reconciliation (HIGH-001) — single commit
3. Text color decision (HIGH-002) — single commit
4. Button radius decision (CRIT-003 + HIGH-005) — single commit
5. Star color alignment (HIGH-006) — single commit

**Rollback risk:** LOW — all changes are text edits to markdown specifications. Git revert restores previous state.

**Validation steps:**
- Grep all hex values in docs/ after each change to confirm consistency
- Cross-check docs/10 Conflicts Register — resolved items should be marked RESOLVED
- Verify no new conflicts introduced

---

### BATCH 2: Critical Factual Correction

**Tickets:** CRIT-002  
**Theme:** Remove outdated $75 shipping threshold from APPROVED PDP doc

**Files affected:**
- docs/05-PDP-ARCHITECTURE.md (lines 264, 2197, 2295, 2360)

**Dependencies:** None — already confirmed resolved per live site and docs/10 C-010

**Required approvals:** ChatGPT (modifies APPROVED document)

**Safe execution order:**
1. Replace 4 instances of "$75" with "$150"
2. Add inline annotation at first instance

**Rollback risk:** NONE — simple text replacement; change is factually correct

**Validation steps:**
- Grep docs/05 for "$75" — should return 0 results
- Grep docs/05 for "$150" — should return 6 results (2 existing + 4 new)
- Confirm consistency with docs/08, docs/09, docs/10

---

### BATCH 3: Cross-Reference Network

**Tickets:** HIGH-003, HIGH-004, MED-006, MED-007  
**Theme:** Add missing cross-references between documents

**Files affected:**
- docs/01-BRAND-NORTH-STAR.md (header Sources line)
- docs/02-BRAND-SYSTEM.md (header Sources line)
- docs/05-PDP-ARCHITECTURE.md (add RELATED DOCUMENTS section)
- docs/06-HOMEPAGE-ARCHITECTURE.md (add RELATED DOCUMENTS section)
- docs/09-PRODUCT-KNOWLEDGE.md (add cross-reference to docs/07)
- docs/10-DECISIONS.md (add cross-reference to docs/07)

**Dependencies:** None

**Required approvals:** ChatGPT for docs/05 and docs/06 (APPROVED). docs/01, 02, 09, 10 are PENDING REVIEW — can be modified without approval.

**Safe execution order:**
1. Update PENDING REVIEW docs first (01, 02, 09, 10) — single commit
2. Update APPROVED docs (05, 06) — single commit after approval

**Rollback risk:** NONE — additive only (no content removed)

**Validation steps:**
- Every docs/ file should reference at least 2 other docs/ files
- docs/07 should be referenced by at least 3 other documents
- No broken references (filenames must match actual files)

---

### BATCH 4: Content Deduplication

**Tickets:** MED-003, MED-004, MED-005  
**Theme:** Replace repeated verbatim content with cross-references

**Files affected:**
- docs/01-BRAND-NORTH-STAR.md (lines 31, 38–40, 77)
- docs/10-DECISIONS.md (B-008)

**Dependencies:** Batch 3 should complete first (cross-references in place)

**Required approvals:** None — structural edits to PENDING REVIEW documents

**Safe execution order:**
1. Add cross-reference notes below each duplicated block (do NOT remove content — add "See also:" lines)
2. Single commit for all 3 tickets

**Rollback risk:** NONE — additive annotations only

**Validation steps:**
- Verify the canonical source (docs/02 Section 4, docs/09 comparison) still contains the full text
- Verify cross-reference text accurately points to correct section

---

### BATCH 5: Format Standardization

**Tickets:** MED-001, MED-002, LOW-001, LOW-002  
**Theme:** Unified header, status, date, and citation formatting

**Files affected:**
- docs/05-PDP-ARCHITECTURE.md (header)
- docs/06-HOMEPAGE-ARCHITECTURE.md (header)
- docs/07-COPY-GUIDE.md (header)
- docs/04-COMPONENT-LIBRARY.md (Source: labels)
- WORKFLOW.md (add header template)

**Dependencies:** Batch 2 and 3 should complete first (don't format-fix then content-fix)

**Required approvals:** ChatGPT for docs/04, 05, 06 (APPROVED). docs/07 is PENDING REVIEW.

**Safe execution order:**
1. Define canonical header template in WORKFLOW.md
2. Update PENDING REVIEW docs (07) — single commit
3. Update APPROVED docs (04, 05, 06) — single commit after approval

**Rollback risk:** NONE — formatting changes only

**Validation steps:**
- Every docs/ file should have `**Status:** VALUE` on line 3
- Every docs/ file should have `**Purpose:**` field
- Every docs/ file should have `**Build Date:**` field
- Grep for plain "Status:" (without bold) should return 0 in docs/

---

### BATCH 6: Standalone Fixes (No Dependencies)

**Tickets:** MED-009, MED-010, LOW-003, LOW-004, LOW-005, LOW-007, LOW-008, LOW-009, LOW-010, LOW-011  
**Theme:** Independent corrections that can be done in any order

**Files affected:**
- docs/10-DECISIONS.md (N-006, section number map, header fix)
- docs/09-PRODUCT-KNOWLEDGE.md (review count, size range, Coperni status, discount code)
- docs/02-BRAND-SYSTEM.md (section numbering note)
- docs/03-DESIGN-SYSTEM.md (line reference fix)

**Dependencies:** None — all independent

**Required approvals:** None — all PENDING REVIEW documents

**Safe execution order:**
1. docs/10 fixes (LOW-003, LOW-010, MED-009) — single commit
2. docs/09 fixes (LOW-005, LOW-007, LOW-009, LOW-011) — single commit
3. docs/02 fix (LOW-004) — single commit
4. docs/03 fix (MED-010) — single commit
5. LOW-008 — documentation note only, no file change needed

**Rollback risk:** NONE — minor text corrections

**Validation steps:**
- Grep for "docs/02–09" should return 0 after LOW-010
- Grep for "save15" should return consistent casing after LOW-005
- Review count should be single value after LOW-009

---

## EXECUTION SUMMARY

| Batch | Tickets | Complexity | Blocked By | Approvals |
|-------|---------|-----------|------------|-----------|
| 1 | 7 | M | ADR decisions | ChatGPT (all) |
| 2 | 1 | S | None | ChatGPT |
| 3 | 4 | S | None (partial approval) | ChatGPT (docs/05, 06 only) |
| 4 | 3 | S | Batch 3 | None |
| 5 | 4 | S | Batch 2, 3 | ChatGPT (docs/04, 05, 06) |
| 6 | 10 | S | None | None |

**Total commits if all batches execute:** 10–12 commits  
**Total files modified:** 10 documents + WORKFLOW.md  
**Blocking path:** Batch 1 requires 7 Architect decisions before ANY implementation fix can proceed.

---

## RECOMMENDED EXECUTION ORDER

1. **Batch 6** — no blockers, no approvals, immediate value
2. **Batch 2** — single critical fix, requires one approval
3. **Batch 3** — cross-references, partial approval needed
4. **Batch 4** — deduplication, depends on Batch 3
5. **Batch 5** — formatting, depends on Batches 2+3
6. **Batch 1** — BLOCKED until ADR decisions received from Architect

---

**END OF REMEDIATION PLAN**
