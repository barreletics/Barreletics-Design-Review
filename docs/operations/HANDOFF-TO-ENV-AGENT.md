# Handoff → environment agent (from abandoned-cart agent)

**From:** [Shopify abandoned cart campaign](https://cursor.com/agents/bc-01a0f73b-b650-772e-ae03-5ca538ec6415)  
**Blocked on:** Andrew cannot type into VM Chrome; Shopify login not completed on cloud VM.

## Please enable

1. **User control of cloud agent desktop/browser** (or equivalent) so Andrew can complete Shopify OAuth once on the VM.
2. **Persistent Chrome profile** under `~/.config/google-chrome` across agent runs (same environment `e7307b06-aece-11f1-bf4b-42ffb4d10ea7`).
3. **`@shopify/cli`** on PATH; optional helper script: `shopify store auth --store barreletics.myshopify.com`.

Egress already allows Shopify. Chrome 148 is installed and works for computer-use.

## When unblocked, abandoned-cart agent will

1. Open **Marketing → Automations** → **[GROK] Abandoned Checkout – Unique 10% (3-email)** (Active).
2. Verify unique discount + Flow + customer metafield (not static SAVE10).
3. Run **Send test email** on each step; document results in `docs/operations/shopify-abandoned-checkout-series.md`.
4. Optional: one test abandon checkout with a test email.

## Andrew action (one time)

Complete Shopify login in VM browser OR approve device login when abandoned-cart agent posts code.

**Reply in abandoned-cart chat:** `logged in`
