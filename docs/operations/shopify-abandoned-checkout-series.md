# Shopify abandoned checkout email series — live status & testing

**Store:** barreletics  
**Platform:** Shopify Email (Marketing → Automations), optional Shopify Flow + customer metafield for unique codes  
**Last known strategy snapshot:** July 31, 2026 (3-step live + planned 4-step unique-code upgrade)

This file is the **Git backup of the intended design and verification steps**. Automations themselves live only in Shopify admin unless exported manually (screenshots + this doc).

---

## Automated admin audit (Oct 1, 2026)

Read-only Chrome audit completed after admin login. See **Consent line (Oct 1, 2026)** below.

**To finish verification**, complete the testing checklist at the bottom (test send + real abandon). Optional: authenticate **Shopify CLI** on a machine with store access (`shopify store auth --store barreletics.myshopify.com`) for future read-only checks.

### Consent line & live series (Oct 1, 2026)

**What Grok rebuilt (the “other choice”):** Abandoned **checkout** automation (not cart), with **simple** 3-email templates and **To: All customers** — stored as `[GROK] DRAFT – All-customers abandoned checkout test`. That was the version meant for people **not** subscribed to marketing.

**Problem found:** The **Active** series was still `[GROK] Abandoned Checkout – Unique 10% (3-email)` with **To: Customers subscribed to email marketing** on all 3 steps — so non-subscribers were blocked.

**Fix applied (Oct 1, 2026 — admin only, theme untouched):**

| Automation | Status after fix |
|---|---|
| `[GROK] Abandoned Checkout – All customers (3-email)` | **Active** — To: **All customers** (renamed Oct 1, 2026) |
| `[GROK] Abandoned Checkout – Unique 10% (3-email)` | **Inactive** (was marketing-subscribers-only) |

**Timing (active series):** ~4h wait → Email 1 → 20h → Email 2 → 24h → Email 3.

**Flow:** Unique 10% codes via Shopify Flow (`discountCodeBasicCreate`, customer tags) — verified attached to active path.

**Still inactive:** `[GROK] TEMP – copy of 3-email for all-customers build`, old cart series, OLD – not used rows.

**E2E test (Oct 1, 2026, no marketing opt-in):** `barreletics.abandon.test+cursor2026@gmail.com` — checkout ~$157.95 abandoned ~2:16 PM UTC; marketing checkbox **unchecked**. Email 1 expected ~4h later (~6:16 PM UTC same day). Confirm in **Orders → Abandoned checkouts** and inbox.

---

## GitHub backup status

As of October 2026, **this repository does not contain** exported automation JSON, email HTML, or Flow definitions for abandoned checkout. Configuration is **admin-only**. Use this document + periodic admin screenshots as the repo record.

---

## Expected automations (baseline — 3 emails)

| Admin name (typical) | Delay | Discount | Notes |
|----------------------|-------|----------|--------|
| Abandoned Checkout — 4 Hours | 4h after abandon | None | Soft reminder; do not disable when upgrading |
| Abandoned Checkout — 10 Hours | 10h | SAVE10 (legacy) or unique 10% | Best historical performer |
| Abandoned Checkout — 24 Hours | 24h | Same as 10h email | Urgency |

Generic duplicate **“Abandoned checkout”** automation should stay **inactive**.

---

## Target state (unique-code upgrade — 4 emails)

| Touch | Delay | Code |
|-------|-------|------|
| Email 1 | 4h | None |
| Email 2 | 10h | Unique 10%, single-use, 72h expiry from send |
| Email 3 | 24h | Same code as email 2 |
| Email 4 | 58h | Expiry reminder (24h before code expires) |

**Technical (when upgrade is complete):**

1. **Shopify Flow** — on checkout abandonment: create unique discount, save code to **customer metafield**.
2. **Shopify Email** — 10h / 24h / 58h templates reference that metafield (not hard-coded SAVE10).
3. **Rollout:** New flows tested → turn off **old** 10h and 24h only after new ones verified.

**Discount rules (target):** 10% off, single-use, no minimum, applies to sale items, expires 72h after 10h send.

---

## Admin verification checklist (5 minutes)

Open: [Marketing → Automations](https://admin.shopify.com/store/barreletics/marketing/automations)

- [ ] List every automation whose trigger is **abandoned checkout / cart**.
- [ ] Record each **status**: Active, Draft, or Paused.
- [ ] Confirm **no duplicate active** 10h/24h pairs (old + “copy” both sending).
- [ ] Confirm **4h** automation is Active.
- [ ] Note whether **58h** automation exists (upgrade complete vs baseline 3 only).
- [ ] Open **10h** email: static **SAVE10** vs dynamic customer metafield / personalization.
- [ ] Open **24h** email: same check.

Optional:

- [ ] **Settings → Custom data → Customers** — metafield for recovery / abandon code exists and is used in templates.
- [ ] **Apps → Shopify Flow** — active workflow for unique discount on abandon.

Fill in **as-found** table when auditing:

| Automation name | Status | Delay | Code type | Last edited |
|-----------------|--------|-------|-----------|-------------|
| **[GROK] Abandoned Checkout – All customers (3-email)** | **Active** | 4h + 20h + 24h | Unique 10% (Flow) | Oct 1, 2026 — **To: All customers** |
| [GROK] Abandoned Checkout – Unique 10% (3-email) | Inactive | was 4h/24h/48h | Unique 10% | Was marketing-subscribers-only |
| **[GROK] Welcome Series** | **Active** | — | — | Same |
| [GROK] Abandoned Cart – Unique 10% Series | Inactive | — | — | Do not enable without review (duplicate naming) |
| [GROK] TEMP – copy of 3-email for all-customers build | Inactive | — | — | Build copy |
| [GROK] TEST Abandoned Checkout – Unique Code | Inactive | — | — | Test |
| OLD – not used [GROK] Abandoned Checkout – Unique 10% (…) | Inactive | — | — | Retired |
| OLD – not used [GROK] TEST Abandoned Cart – Unique 10% … | Inactive | — | — | Retired (4 sent in Aug window on dashboard) |
| OLD – not used [NEW] Abandoned Cart - 58 Hours | Inactive | 58h | — | 4-email upgrade **not** live |
| OLD – not used [NEW] Abandoned Cart - 24 Hours | Inactive | 24h | — | Retired |
| OLD – not used [NEW] Abandoned Cart - 10 Hours | Inactive | 10h | — | Retired |

**Dashboard metrics (Aug 1–31, 2026, all automations):** 408 sent, 9.33% click rate, 8 orders, 15.38% conversion rate — not attributable to a single flow from this list view alone.

---

## Testing checklist (must pass before calling “live”)

### A. Shopify test send (copy & links)

For each **Active** automation email step:

- [ ] Use **Send test email** in the automation editor to a real inbox you control.
- [ ] Subject line, branding, and **cart link** render correctly.
- [ ] Discount email shows the **expected** code behavior (static SAVE10 vs unique placeholder in test — unique may need a real abandon + Flow run).

### B. End-to-end abandon test (recommended)

Use a **test customer email** you can read (not a production customer).

1. [ ] Log out or use incognito; add product to cart on barreletics.com.
2. [ ] Enter email at checkout, **do not pay** — wait for abandon to register.
3. [ ] In admin: **Orders → Abandoned checkouts** — confirm the checkout appears.
4. [ ] Wait for **4h** email (or temporarily use a **duplicate automation in Draft** with a 10-minute delay for QA only — do not leave short-delay copies Active in production).
5. [ ] Confirm email 1 received; no unintended discount on 4h if that is the rule.
6. [ ] For 10h/24h/58h: confirm code matches Flow/metafield rules; code works once at checkout; second use fails.

### C. Analytics sanity check

Marketing → Automations → open each automation → review **sent / opened / clicked / orders** (or attributed sales). Zero sends with Active status for 7+ days may mean trigger misconfiguration or no abandons.

---

## If something is Draft or missing

| Situation | Action |
|-----------|--------|
| Upgrade automations still **Draft** | Finish template + metafield tags, test send, then Activate; keep legacy Active until one successful real abandon test on new path |
| Only 3 emails, still SAVE10 | Baseline is live; unique-code upgrade not finished |
| Two Active 10h or 24h | Pause/remove duplicate to avoid double emails |
| No Flow / metafield but emails promise “your unique code” | Emails will break or show blanks — fix Flow first or revert copy to SAVE10 until Flow works |

---

## Backing up to GitHub (going forward)

After each change in Shopify admin, update:

1. This file — **as-found** table and date.
2. `docs/operations/shopify-abandoned-checkout-screenshots/` (optional) — PNG of automation list and 10h email editor (create folder when needed).

Shopify does not sync automations to theme git; **manual documentation is the backup**.

---

## Owners

- **Shopify Email / Flow implementation:** Brian Bolli (per internal handoff) or store admin  
- **Copy / strategy:** Andrew / marketing  
- **Verification:** Run checklist above after any automation edit
