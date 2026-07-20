# M4D — Rollback Procedure

**Purpose:** Step-by-step guide to revert the Barreletics storefront to the previous theme if a critical issue is discovered post-launch.

---

## 1. When to Rollback

Rollback is warranted when ANY of the following are true:

| Trigger | Severity | Action |
|---------|----------|--------|
| Site completely down (500 errors, blank page) | P0 | Rollback immediately |
| Checkout/payment broken | P0 | Rollback immediately |
| Homepage does not load | P0 | Rollback immediately |
| Add to Cart broken | P0 | Rollback immediately |
| Navigation completely non-functional | P0 | Rollback immediately |
| Pricing displays incorrectly | P1 | Rollback within 15 minutes |
| Cart not functioning | P1 | Rollback within 15 minutes |
| Major layout broken on mobile (unreadable) | P1 | Assess — rollback if revenue impacted |

**Do NOT rollback for:**
- Minor styling issues (spacing, color, animation glitches) — fix forward
- Analytics not firing — fix forward (not revenue-impacting)
- One broken page that isn't homepage/PDP/collection — fix forward
- Cosmetic issues on a single browser — fix forward

See `m4d-decision-tree.md` for the full decision flowchart.

---

## 2. Who Can Initiate

| Person | Authority |
|--------|-----------|
| **Owner** | Can initiate rollback at any time for any reason |
| **Builder** | Can initiate rollback for P0 issues without Owner approval. Must notify Owner immediately after. |

For P1 issues, Builder should contact Owner before rolling back unless Owner is unreachable for >15 minutes during active monitoring window.

---

## 3. How to Rollback

### Step-by-step (Shopify Admin):

1. Log into Shopify admin: `barreletics.myshopify.com/admin`
2. Navigate to **Online Store → Themes**
3. Find the backup theme (name and ID documented pre-launch — see `m4d-launch-plan.md`)
4. Click **⋯ (three dots)** next to the backup theme
5. Click **Publish**
6. Confirm the publish action
7. Wait for confirmation message: "Theme published successfully"
8. **Immediately** open `barreletics.com` in a new incognito/private window
9. Verify the old (backup) theme is now live:
   - Homepage loads with previous design
   - Navigation works
   - A product page loads
   - Add to Cart functions
   - Checkout is reachable

### Time to complete: ~2 minutes

---

## 4. Post-Rollback Verification

- [ ] Homepage loads correctly (old theme)
- [ ] Navigation links work
- [ ] At least one PDP loads with correct pricing
- [ ] Add to Cart works
- [ ] Checkout is reachable
- [ ] Mobile site loads
- [ ] No JavaScript console errors
- [ ] Payment processing works (if P0 was payment-related, place a test order)

---

## 5. Communication Plan

### If customers were affected:

| Audience | Channel | Message |
|----------|---------|---------|
| Active customers (saw errors) | Help Scout auto-reply or proactive email | "We experienced a brief technical issue that has been resolved. All orders and accounts are unaffected. We apologize for any inconvenience." |
| Support team | Slack / email | "Site reverted to previous theme at [time]. All customer data and orders are intact. New theme issue is under investigation." |
| Owner | Direct call/text | "Rollback completed at [time]. Issue: [description]. Next steps: [plan]." |

### If NO customers were affected (caught during monitoring window):

- No external communication needed
- Internal note: document what happened and why in rollback incident log

---

## 6. Root Cause Analysis Process

Within 24 hours of rollback:

1. **Document the issue:**
   - What was observed (screenshots, error messages, console output)
   - When it was first noticed
   - How many customers may have been affected
   - Revenue impact estimate (if any)

2. **Identify root cause:**
   - Was it a code issue in the new theme?
   - Was it a Shopify platform issue?
   - Was it a third-party integration issue?
   - Was it a configuration/settings issue?

3. **Fix and re-validate:**
   - Fix the issue on the preview theme (do NOT fix on production)
   - Re-run relevant M4C/M4D validations
   - Document the fix in the Decision Log

4. **Re-launch plan:**
   - Schedule new launch window
   - Follow full `m4d-theme-publish-checklist.md` again
   - Additional monitoring focus on the area that caused rollback

---

## Pre-Launch Preparation

Before launch day, complete these rollback readiness items:

- [ ] Backup theme exported as .zip
- [ ] Backup theme ID recorded: `________________`
- [ ] Backup theme name in Shopify admin: `________________`
- [ ] Verified backup theme can be published (test publish → revert on a staging/dev store if possible)
- [ ] This document reviewed by both Owner and Builder
- [ ] Owner and Builder both have Shopify admin access confirmed
