## (empty — Grok writes here)

Append new blocks at the top. Cursor reads on “sync” or start of session.

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
