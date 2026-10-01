# M4 Theme Production — Master Directive Alignment

**Date:** 2026-07-26  
**Plan source:** `.cursor/plans/m4_theme_production_44c3b5db.plan.md`  
**Coordinator review:** Hybrid shell + br-* port vs Master Directive

---

## Verdict

**Aligned in architecture; conditional on br-* refactor pass.**

Clean `shopify-build/` shell + surgical port of 3 live `br-*` sections + rebuild from locked HTML mocks matches the Master Directive. Raw copy of 8,787 lines of live section code **conflicts** with the performance mandate — Phase 2a refactor is mandatory before port.

---

## Alignment matrix

| Directive pillar | Plan mapping | Status |
|------------------|--------------|--------|
| Clean Shopify shell | Phase 1 from `shopify-build/` (40 sections, 34 templates) | ✅ |
| Port only 3 approved sections | br-variants (4,534), br-media-text-split (1,656), br-multi-box-hero (2,597) | ✅ |
| Everything else from HTML mocks | Phase 3: Home WORKING, SEO v36, Collection v18, PDP v16 | ✅ |
| Shopify-native / no hardcoded content | Section settings, menus, collections | ✅ |
| Modular + Theme Editor | ~20 marketing sections; one `hero-fullbleed` with alignment | ✅ |
| Locked BZ-020 type | H1 ~64/400 v6 title case; sections sentence case | ✅ |
| Performance foundation | Shell lean; live br-* has inline CSS/JS bloat | ⚠️ Refactor required |
| Mobile-first | Mocks mobile-first; verify on port | ⚠️ |
| A11y / Lighthouse / GEO | M4C roadmap exists; not yet in build phases | ⚠️ Added to plan todos |

---

## br-* size reality

| Section | Live | Shell prototype |
|---------|------|-----------------|
| br-variants | 4,534 lines | variant-grid.liquid (272) |
| br-media-text-split | 1,656 lines (57 ai_gen_id blocks) | fifty-fifty.liquid (211) |
| br-multi-box-hero | 2,597 lines (74 ai_gen_id blocks) | *(missing — needs visual-mosaic)* |

**Mitigation:** Preserve Liquid logic + schema IDs. Extract CSS/JS to assets. Replace ai_gen_id scoping with BEM + design tokens. Not a rewrite.

---

## Top risks

1. **br-variants performance conflict** — 4,534 lines + inline JS; raw port violates directive. Refactor pass required.
2. **Schema ID drift** — Changing setting IDs breaks live template JSON reconnection.
3. **Two repos + template orphans** — Design Review vs live donor; shell has 9+ collection JSON templates pre-mock.

---

## Top gaps (added to plan todos)

1. Lighthouse/CWV gate (M4C.6: Perf ≥90, A11y ≥95) — was roadmap-only
2. Metafields inventory (sole_type, Judge.me, GEO) — before content freeze
3. Image loading + WCAG checklist — not explicit in build phases

---

## Phase 1 readiness

**YES** — after Phase 0 ChatGPT (Chad) sign-off on hybrid + refactor-pass requirement.  
**NOT ready:** Raw br-* port or publish without Phase 2a approved.

---

## ChatGPT paste block

See plan file section "Master Directive Alignment" for full detail. Short paste:

> Reviewing Barreletics M4 hybrid plan: push clean shopify-build/ shell (40 sections, token CSS, integrations) as unpublished draft; port exactly 3 live br-* sections (variants 4534 lines, media-text-split 1656, multi-box-hero 2597) with schema ID preservation but mandatory refactor pass to extract inline CSS/JS and lock to BZ-020 tokens; rebuild all other sections from locked HTML mocks (Home WORKING, SEO v36, Collection v18, PDP v16). One hero-fullbleed section with left|center alignment; Home/Collection split heroes separate. Main risk: raw br-variants port conflicts with performance mandate. Main gaps: Lighthouse gate, metafields list, image loading strategy not yet in build phases. Phase 1 shell push OK after your sign-off; br-* port waits on refactor plan. Aligned or concerns?
