# Cart offer A/B — theme-only URL switch (no Shopify native A/B)

## Arms

| Query param | Behavior |
|-------------|----------|
| *(absent)*, `br_cart_offer=control`, invalid | **CONTROL** — matches deployed `5a01277` (closed-sole count, pants photo at 1 pair, preview notice). |
| `br_cart_offer=variant` | **VARIANT** — COPY03 inline sole → color → size → Add pair; pants only at 2+ pairs; open/closed mixed count. |

**No** `sessionStorage`, `localStorage`, or cookies. Navigating to any URL **without** `br_cart_offer=variant` returns **control** (no sticky variant).

During AJAX cart refresh on the **same page**, arm is re-read from `window.location.search` on each `mountPromo` call.

### Optional link decoration (variant only)

When the current URL includes `br_cart_offer=variant`, `[data-cart-trigger]` and `/cart` links may get the param appended (checkout links untouched). If a tester opens cart without the param, they see **control** — not a silent variant stick.

## Preview URL patterns (parent fills theme id after push)

Replace `{DRAFT_THEME_ID}` with the unpublished theme id from Admin or `shopify theme list` (not stored in this repo):

```
https://barreletics.com/?preview_theme_id={DRAFT_THEME_ID}&br_cart_offer=control
https://barreletics.com/?preview_theme_id={DRAFT_THEME_ID}&br_cart_offer=variant
```

Cart drawer on any qualifying PDP/collection URL: same params on that page URL before opening cart.

**Source phase:** links are patterns only until parent uploads the three theme files.

## Draft role guard

When `window.Shopify.theme.role` is present and not `main`, preview is on an unpublished/draft theme. No theme id hardcoding in code.

## VARIANT UX notes (Baymard guidance — not retailer proof)

Parent cited [inline cart recommendations](https://baymard.com/research-articles/product-recommendations-cart) and [cross-sell step type](https://baymard.com/checkout-usability/benchmark/step-type/cross-sell): prefer **clearly labeled inline** cross-sells; avoid **blocking** separate upsell steps. VARIANT implements:

- Inline progressive picker (no modal/popup).
- Labels: “Recommended add-on (inline)”, “Optional add-on (inline, preview)”.
- Simple **pair counter** text only (not a shipping progress bar).
- Prominent preview disclaimer; preview prices tagged; **no** earned/applied checkout discount claims.

CONTROL unchanged.

## Manual metric (not auto-collected)

**Success signal for comparison:** eligible **1-pair** cart → **successful second Performance Skin add** (native cart line count increases), per assigned arm. Manual QA or parent tooling — **not** instrumented in this deliverable.

### Existing cart events (native `cart.js`)

| Event | When | Captures arm? | Captures promo add success? |
|-------|------|---------------|-----------------------------|
| `cart:item-added` | After `BarreleticsCart.add` | **No** | **Yes** (variant add-pair uses same API) |
| `cart:updated` | Qty change/remove | **No** | Partial |

**Not verified / not installed:** GA4, Amplitude, or arm impression pixels. Firing `CustomEvent` alone does **not** mean analytics records conversion lift.

Paid order conversion requires real discounts + traffic — out of scope for this preview draft.

## Cost

No paid A/B app, no custom app, no additional services — only shared theme asset edits.
