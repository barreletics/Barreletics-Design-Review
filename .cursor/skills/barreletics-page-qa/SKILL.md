---
name: barreletics-page-qa
description: >-
  Barreletics page QA gate: Locked mock → repo template → live handle → Admin
  theme-template suffix → push only if theme named → verify preview path. Auto-invoke
  BEFORE any edit or deploy involving shopify-build/templates (collection.*, product.*,
  page.*, blog.json), collection/PDP/help/journal/partner pages, Admin template suffix,
  nav URLs, or when the agent might ship Apparel as Shop All, /blogs/journal, /pages/help,
  or open-sole/closed-sole/outdoor collection 404s. One page per turn.
---

# Barreletics Page QA — FAIL CLOSED

**Registry (single source):** `planning/page-template-registry.md`  
**Freeze:** `planning/m4-section-freeze.md`  
**Anti-revert:** `barreletics-anti-revert`  
**Shopify:** push only when Andrew names theme ID in **this** message (default QA `187144929571`)

## Sense it — STOP if any of these thoughts appear

- “Collections page” without checking Shop All vs Apparel handles  
- Linking `/blogs/journal`, `/pages/help`, `/collections/open-sole|closed-sole|outdoor`  
- Editing `collection.json` when the ask was Apparel (or the reverse)  
- Pushing then previewing a **different** handle than the one edited  
- Touching multiple page templates in one turn “while we’re here”

## Mandatory gate (copy into your turn)

```
PAGE QA GATE
- [ ] Read planning/page-template-registry.md row for THIS page
- [ ] Hub Locked mock (or live/spine authority) identified — will not invent layout
- [ ] Repo template path matches the row (not a sibling)
- [ ] Live handle confirmed — not a dead URL
- [ ] Admin theme-template suffix known / noted if still required in Admin
- [ ] ONE page this turn — no drive-by template edits
- [ ] Push ONLY if Andrew named theme ID in CURRENT message
- [ ] After push: verify QA preview path for THAT handle (+ Theme Editor URL)
- [ ] If change hits >1 surface or URLs/copy: update freeze + registry (os-sync rule)
```

## Workflow (strict order)

1. **Locked mock** — Open hub authority from the registry row (`docs/index.html` Locked card). If none Locked, use the registry’s live/spine note. Never overwrite Locked HTML in place.  
2. **Repo template** — Edit only `shopify-build/templates/{file}` from the row (+ shared sections if required). Repo = master.  
3. **Handle** — QA and CTAs use the **canonical URL** in the registry.  
4. **Admin suffix** — After deploy, resource must use the listed Theme template suffix (e.g. Apparel → `apparel`, Open → `open-sole`). If Admin not set, preview will show the wrong stack — say so explicitly.  
5. **Push** — Only if Andrew named a disposable theme ID in **this** message. Never publish. Never invent an ID.  
6. **Verify** — Open preview for the **same** handle you edited. Desktop + mobile. Confirm you did not land on Shop All when testing Apparel (etc.).

## One page per turn

Do **not** batch Shop All + Apparel + Free People + Coperni in one agent turn unless Andrew explicitly lists them as one ordered checklist **and** you still verify **each** handle separately.

## Dead handles (hard refuse)

Never add nav/CTA/docs links to: `/blogs/journal` · `/pages/help` · `/collections/open-sole` · `/collections/closed-sole` · `/collections/outdoor` · `/pages/contact` · `/pages/about`. See registry for replacements.

## Parallel agents

One writer per page template per turn. Do not reclaim another agent’s collection/PDP/page JSON by “fixing” suffixes or restoring older spines.
