# Barreletics — Cloud Agent playbook

## Split of work (non‑negotiable)

| Task | Who |
|------|-----|
| **Shopify Flow** (enable, wait steps, run history, save) | **Merchant admin + Sidekick** in `admin.shopify.com/store/barreletics` |
| **Abandoned checkout / discount / customer reads** | **Cloud agent** via Admin API (see below) |
| **Recovery email + checkout UX** | **Phone or private window** on the real email link (2 min) |
| **Theme / GitHub** | **Cloud agent** (live theme `187143618851` only when editing theme) |

Do **not** use computer-use / Chrome for Shopify admin unless the user explicitly says they logged in on the **cloud** browser in this session.

## Store API (required for admin tasks)

Set these in [Cloud environment secrets](https://cursor.com/dashboard/cloud-agents/environments) (never commit tokens):

- `SHOPIFY_STORE` = `barreletics.myshopify.com`
- `SHOPIFY_ADMIN_ACCESS_TOKEN` = custom app Admin API token (`read_orders`, `read_customers`, `read_discounts`, `read_checkouts` minimum)

**First action** on any Shopify admin diagnosis task:

```bash
./scripts/shopify-admin-gql.sh '{ shop { name } }'
```

If that fails → tell the user secrets are missing; **do not** loop on Shopify login pages.

Optional: `shopify store auth` / `shopify store execute` after CLI is installed via `install` in `.cursor/environment.json`.

## Abandoned checkout QA (short path)

1. API: latest abandoned checkout for test email (GraphQL `abandonedCheckouts`).
2. Sidekick: Flow ON, first wait **4 hours** after tests, run history errors.
3. Device: one recovery click from inbox; confirm SAVE10 in email, checkout **empty** discount field, paste SAVE10 manually.

## Sidekick paste (when Flow/UI is the question)

Keep it to **symptoms + checkout id + email + what you need** — Sidekick already built the workflow; don’t re-spec the whole Flow.

## Influencer codes vs SAVE10

If desktop shows `0-ANDREAMINSKI` but **phone is clean**, treat as **local discount cookie / session**, not broken Flow. Compare “Return to cart” URLs; clear `barreletics.com` + checkout cookies on desktop.
