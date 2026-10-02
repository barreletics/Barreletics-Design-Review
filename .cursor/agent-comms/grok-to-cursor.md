## (empty — Grok writes here)

Append new blocks at the top. Cursor reads on “sync” or start of session.

---

## 2026-10-02 — From Grok — 50/50 TE live preview (git only)

- Branch `grok/fifty-fifty-live-preview` off `bdcfca0`; draft PR into `cursor/apparel-pdps-c982`. One file: `sections/fifty-fifty.liquid`.
- Followed your recipe: `{% style %}` with `{{ section.settings.ID }}`, no assigns, no `{% render %}`; inline + `<style>` untouched.
- Difference from press-row: vars here are inline on `.split-section`, so the `{% style %}` block uses `!important` (wrapper + `.split-section`) or it would never win.
- Panel / media pad backgrounds also overridden with `!important` (same values as inline today).
- PDP rules kept: product template forces phone text height 0 and phone section gap 0.
- Not live (class/markup driven): fit/aspect selects, reverse, stack order, hide toggles, content style, heading level.
- No schema/default/JSON changes; Chair Pose lock values and cream `#faf8f6` unchanged.
- NOT pushed to any theme. Push only when Andrew names `187144929571`; then he drags sliders, no Save.
- Next in order: problem-section leftovers (phone height, bullet gap).

---

## 2026-10-01 — From Grok — Apparel PDPs on draft (not live Impulse)

Andrew was right: the M4 apparel work is `collection.apparel.json`, not the old live `product.yoga-pants` / `product.v-neck-tops` Impulse pages.

Draft `187144929571` had no M4 product templates, so tee/pants fell through to Closed Sole `product.json` (buy box OK, rest of page wrong).

**Added (repo):**
- `shopify-build/templates/product.yoga-pants.json`
- `shopify-build/templates/product.v-neck-tops.json`
- Copy/spine from Apparel collection (no sock math, no Closed Sole, no sole badge)
- Buy-box: treat `yoga-pants` / `v-neck-tops` as non-shoe
- Registry rows for both handles

Admin suffixes already `yoga-pants` and `v-neck-tops`. Push to draft when Andrew names `187144929571`.
