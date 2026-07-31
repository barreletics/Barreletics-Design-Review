# M4 Section Freeze Registry — APPROVED / SETTLED

**Status:** ACTIVE  
**Authority:** Companion to `planning/m4-section-library-CONTRACT.md` §8  
**Guardrail:** `.cursor/rules/section-freeze-no-drift.mdc`  
**Rule:** Frozen sections must not drift, revert, or be replaced without **explicit Andrew approval in the CURRENT message**.

---

## What “APPROVED / FROZEN” means

1. Andrew visually approved the composition (Shopify draft preview and/or named letter).
2. Structure is locked in `shopify-build/` (repo = master).
3. Agents may fix bugs / TE copy / schema labels **only if** they do not change layout structure, visual system, or swap to an alternate design.
4. Agents must **not**:
   - `git checkout` older section files without current-message approval
   - Replace with live / Impulse / dark Phase 1 / gallery pick without a letter
   - Invent alternate footers, heroes, or chrome “improvements”
   - Silently restore removed elements (brand blurb, value checklist / ✓ list, 10% offer)

---

## Frozen registry

| ID | Surface | Status | Fingerprint (lineage) | Locked composition | Files |
|----|---------|--------|------------------------|--------------------|-------|
| **Footer A+** | Sitewide footer (all pages unless page-specific exception) | **LOCKED / APPROVED / FROZEN** 2026-07-31 (Andrew: “footer is correct lock it in”) | `6fcba348bfdcc82abfcf7cd1fcfb93e3da4cffbe` (lock commit; composition lineage 19b8fe6 — no blurb · no checklist · no 10%) | Charcoal/black simplified **Join the list** (little text) · link columns → Made in USA (+ Connect) · **NO brand blurb** · **NO checkmark checklist** · **NO 10%** | `shopify-build/sections/footer.liquid`, `footer-group.json`, `assets/chrome.css` |
| **PDP** | Product template + buy-box | **INDEX LOCK = Definitive-v16** — not frozen for visual QA. Agents must not swap to July 17 without Andrew letter. | Draft on `187144929571` — see `planning/PDP-WORKING-ENTRY.md` | Authority: `docs/Barreletics PDP - Definitive-v16.html` (`docs/index.html` tag **v16 · Locked**). Juicer still open. | `templates/product.json`, `sections/pdp-buy-box.liquid`, PDP companions |
| **Type OS** | Typography system | **SETTLED** | See `planning/m4-type-hierarchy.md` | Family/size/weight/tracking; no per-section `font_picker` | Type tokens + TE policy |
| **Home WORKING** | Homepage layout authority | **WORKING** (layout authority — not a free redesign surface) | Home WORKING mocks / draft match commits | Agents must not invent alternate homepage composition; match WORKING unless Andrew approves change in-message | `templates/index.json` + home sections |

Update the **Fingerprint** column with the freeze commit SHA after each freeze ship.

---

## Footer A+ — LOCKED detail (CLEAN · law)

- **Andrew letter (2026-07-31):** “footer is correct lock it in please update all documents and github. and the operating system please”
- **Scope:** Default footer for all pages.
- **Exact stack (law):**
  1. Charcoal/black **Join the list** (simplified, little text — headline + form; optional privacy; empty marketing paragraph)
  2. Link columns → Made in USA (+ Connect as in current good state)
  3. **NO** brand blurb
  4. **NO** checkmark / value checklist
  5. **NO** 10%
- **Composition lineage:** `19b8fe6` — if later commits re-add blurb/checklist, revert those parts only to match this clean stack.
- **Draft QA theme:** `187144929571` (M4 Visual QA) — never live.
- **Removed / forbidden without Andrew letter in CURRENT message:**
  - Barreletics **brand blurb**
  - **✓ value checklist** under Join the list
  - 10% first-order offer
  - Impulse/live dark footers; gallery options B–H as live replacements
- **Do not restore blurb or checklist** because an older freeze note, commit (`56d1998`), or forked agent claimed otherwise — latest Andrew letter wins.
- **Gallery:** `docs/footer-version-gallery.html` — CLEAN A+ is **APPROVED / current**; B–H historical only.

---

## PDP — INDEX LOCK = Definitive-v16 (visual QA open)

- **Source of truth from INDEX:** `docs/index.html` → Shop → **PDP · v16 · Locked** → `docs/Barreletics PDP - Definitive-v16.html`
- **2026-07-31 thrash:** Agents swapped to July 17 / mixed stacks; Andrew said completely wrong. Restore = **v16 mock spine + current section implementations**.
- **On draft now:** v16-ordered `product.json` on theme `187144929571` — see `planning/PDP-WORKING-ENTRY.md`
- **Clarify:** v16 mock uses **variant tabs** (Closed/Open/One-Offs/Outdoor) — `use_current_product` OFF on PDP for that match.
- **Do not freeze** until Andrew visual-OKs draft vs v16 mock.
- **Do not touch** frozen Footer A+ while working PDP.
- July 17 HTML = prior/architecture note only — **not** the INDEX locked page.

---

## How to add a freeze

1. Visual QA on disposable draft (`187144929571` unless Andrew names another ID).
2. Andrew says approve / freeze / settle / lock (or equivalent letter).
3. Add/update row in this registry + CONTRACT §8.
4. Add `APPROVED / FROZEN` banner comment at top of the section Liquid if useful.
5. Commit + push; deploy draft only if code changed and ID named.
