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
| **Footer A+** | Sitewide footer (all pages unless page-specific exception) | **APPROVED / SETTLED** 2026-07-31 | *(update to freeze commit SHA on ship)* · lineage `70561b5` → `a59ff4a` → no blurb → no checklist | Black/charcoal simplified **Join the list** (headline + form; optional privacy; no marketing paragraph) · Shop/Learn/Support/Connect columns · Made in USA · Connect · **no brand blurb** · **no ✓ / value checklist** · **no 10%** | `shopify-build/sections/footer.liquid`, `footer-group.json`, `assets/chrome.css` |
| **Type OS** | Typography system | **SETTLED** | See `planning/m4-type-hierarchy.md` | Family/size/weight/tracking; no per-section `font_picker` | Type tokens + TE policy |
| **Home WORKING** | Homepage layout authority | **WORKING** (layout authority — not a free redesign surface) | Home WORKING mocks / draft match commits | Agents must not invent alternate homepage composition; match WORKING unless Andrew approves change in-message | `templates/index.json` + home sections |

Update the **Fingerprint** column with the freeze commit SHA after each freeze ship.

---

## Footer A+ — settled detail (CLEAN)

- **Scope:** Default footer for all pages.
- **Keep:** Dark newsletter band (“Join the list” — headline + form only) · four link columns (Shop / Learn / Support / Connect; WORKING link fallbacks if menus empty / flat) · Made in USA · copyright.
- **Removed / forbidden without Andrew letter in CURRENT message:**
  - Barreletics **brand blurb** (Andrew 2026-07-31: busy with sections above)
  - **✓ value checklist** under Join the list (Andrew 2026-07-31: “yes go ahead” remove)
  - 10% first-order offer
  - Impulse/live dark footers; gallery options B–H as live replacements
- **Do not restore blurb or checklist** because an older freeze note, commit (`56d1998`), or forked agent claimed otherwise — latest Andrew letter wins.
- **Gallery:** `docs/footer-version-gallery.html` is historical comparison only — CLEAN A+ is the only deployable footer.

---

## How to add a freeze

1. Visual QA on disposable draft (`187144929571` unless Andrew names another ID).
2. Andrew says approve / freeze / settle (or equivalent letter).
3. Add/update row in this registry + CONTRACT §8.
4. Add `FROZEN` banner comment at top of the section Liquid if useful.
5. Commit + push; deploy draft only if code changed and ID named.
