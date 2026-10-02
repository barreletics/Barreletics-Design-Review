# Cursor Recovery Checklist — Apparel PDP Pages

**Goal:** Restore v-neck-tops and yoga-pants pages to draft theme without risk.

## AJ rules (2026-10-02) — non‑negotiable

1. **Do not edit `shopify-build/sections/pdp-buy-box.liquid`** (no liquid, no schema, no buy-box “fixes”).
2. **Do not `shopify theme push`** to draft `187144929571` (or any theme) until AJ has reviewed built pages locally and approved in writing on the PR.
3. Build/review on Mac first: `docs/apparel_preview.html` + template JSON only.

---

## Role Clarity

- **Cursor:** Steps 1–9 (create branch, restore files, commit, merge to main)
- **AJ:** Steps 10, 12, 13 (verify content, check preview, approve all Shopify pushes)
- **Cursor:** Step 11 (push to draft — ONLY after AJ approval in Step 10)

**Key Rule:** Cursor cannot execute any Shopify push without explicit AJ approval comment on GitHub.

---

## Pre-Recovery (AJ or Cursor)

- [ ] Read CURSOR_HANDOFF_APPAREL_PAGES.md for full context
- [ ] Confirm draft theme ID: `187144929571`
- [ ] Confirm commit with original files: `fed5cf0` (Oct 1, 2026)

---

## Step 1: Create Recovery Branch

```bash
git checkout main
git pull origin main
git checkout -b recovery/apparel-pdp-restore
```

**Verify branch created:** `git branch` should show `* recovery/apparel-pdp-restore`

---

## Step 2: Restore Files from Git History

**Check if files exist in current repo:**
```bash
ls -la shopify-build/templates/product.v-neck-tops.json
ls -la shopify-build/templates/product.yoga-pants.json
```

**If files are missing**, restore from commit fed5cf0:
```bash
git show fed5cf0:shopify-build/templates/product.v-neck-tops.json > shopify-build/templates/product.v-neck-tops.json
git show fed5cf0:shopify-build/templates/product.yoga-pants.json > shopify-build/templates/product.yoga-pants.json
```

**If files already exist**, skip restoration. Just verify content:
```bash
git diff shopify-build/templates/product.v-neck-tops.json
git diff shopify-build/templates/product.yoga-pants.json
```

**Status check:** Should see `modified` status if restored.

---

## Step 3: Verify Liquid Sections Exist

All these must be in `shopify-build/sections/`:
```bash
ls shopify-build/sections/pdp-features.liquid
ls shopify-build/sections/fifty-fifty.liquid
ls shopify-build/sections/variant-grid.liquid
ls shopify-build/sections/pdp-reviews.liquid
ls shopify-build/sections/value-strip.liquid
ls shopify-build/sections/pdp-sticky-atc.liquid
ls shopify-build/sections/pdp-buy-box.liquid
```

**If any are missing**, they need to be checked out from main or commit fed5cf0.

---

## Step 4: Commit Changes

```bash
git add shopify-build/templates/product.v-neck-tops.json
git add shopify-build/templates/product.yoga-pants.json
git commit -m "Recovery: Restore apparel PDP templates from fed5cf0

These templates were overwritten in draft theme 187144929571 with
wrong content (Closed Sole PDP copy). Restored from original commit
fed5cf0 (Oct 1, 2026).

- product.v-neck-tops.json (V-Neck Tops)
- product.yoga-pants.json (Yoga Pants)

Refs: commit fed5cf0
See: CURSOR_HANDOFF_APPAREL_PAGES.md for full recovery context"
```

**Verify commit:** `git log --oneline -1` should show your new commit.

---

## Step 5: Push to GitHub

```bash
git push origin recovery/apparel-pdp-restore
```

**Verify:** Check GitHub — branch should appear in the web UI.

---

## Step 6: Create Pull Request

**On GitHub:**
1. Go to Pull Requests
2. Create PR from `recovery/apparel-pdp-restore` → `main`
3. Title: `Recovery: Restore Apparel PDP pages (v-neck-tops, yoga-pants)`
4. Description: Paste full CURSOR_HANDOFF_APPAREL_PAGES.md content
5. Add comment: "Ready for review before pushing to draft theme"

**Do NOT merge yet.** Wait for review/approval.

---

## Step 7: Get Approval

**AJ reviews the PR:**
- [ ] Commit message is clear
- [ ] Only apparel PDP templates changed
- [ ] No unintended files added
- [ ] Approve PR

---

## Step 8: Merge to Main

**After approval:**
```bash
# Merge via GitHub UI (preferred) or:
git checkout main
git pull origin main
git merge recovery/apparel-pdp-restore
git push origin main
```

**Verify:** `git log --oneline` should show your recovery commit.

---

## Step 9: STOP — Wait for AJ Approval

⚠️ **DO NOT PUSH TO SHOPIFY YET.**

**Comment on the GitHub PR:**
```
@AJ — Ready for approval. Files merged to main. Waiting for your 
sign-off before pushing to draft theme.
```

**Then WAIT for AJ's explicit approval comment. Do not proceed until you hear back.**

---

## Step 10: AJ's Verification (AJ ONLY — Not Cursor)

**AJ will:**
1. Review the PR on GitHub
2. Check the merged files match commit `fed5cf0`
3. Open this HTML preview file to see what the pages should look like:
   - `apparel_preview.html` (includes mockups of both pages)
4. Confirm content matches expectations
5. Post approval comment on GitHub PR:
   ```
   ✅ APPROVED TO PUSH TO DRAFT THEME
   
   Files verified. Content matches fed5cf0.
   You may now push to draft theme 187144929571 ONLY.
   Use the exact command below — no variations.
   ```

**If AJ finds issues:** Request changes. Do not push.

---

## Step 11: Push to Draft Theme (ONLY AFTER AJ APPROVAL)

**Cursor — only execute this if AJ posted the approval comment above.**

⚠️ **CRITICAL: Draft theme (187144929571) only. Do NOT push to live theme.**

```bash
# Copy-paste this exactly. Do not modify.
shopify theme push --theme 187144929571 \
  --only templates/product.v-neck-tops.json,templates/product.yoga-pants.json
```

**Output should say:**
```
Deploying to theme "Draft" (ID: 187144929571)...
Uploading templates/product.v-neck-tops.json
Uploading templates/product.yoga-pants.json
✓ Push complete
```

**If it says "live" or any other theme ID, STOP immediately and contact AJ.**

---

## Step 12: Post-Push Verification (AJ ONLY)

**AJ verifies in Shopify draft theme:**

Open preview links:
1. `https://barreletics.com/products/v-neck-tops?preview_theme_id=187144929571`
2. `https://barreletics.com/products/yoga-pants?preview_theme_id=187144929571`

**Checklist:**

Tops Page:
- [ ] Hero: "Softness. Versatility. Comfort." appears
- [ ] Subtext: "Lightweight. Doesn't pill." appears
- [ ] Benefits bar: Made in USA, Free exchanges, 30-day returns, Doesn't pill
- [ ] "Why these tees" section with 4 features
- [ ] Product grid with color variants
- [ ] Reviews section
- [ ] FAQ section
- [ ] No errors in browser console

Bottoms Page:
- [ ] Hero: "Focus on your workout." appears
- [ ] Subtext: "High-rise compression." appears
- [ ] Benefits bar: Made in USA, Free exchanges, 30-day returns, Doesn't pill
- [ ] "Why these pants" section with 4 features (high-rise, reinforced knees, etc.)
- [ ] Product grid with color variants
- [ ] Reviews section
- [ ] FAQ section
- [ ] No errors in browser console

**If everything looks good:**
- [ ] Post comment on GitHub: "✅ Draft theme verified. Pages render correctly."
- [ ] Pages are now live in draft — ready for final approval before going live

**If anything is broken or missing:**
- [ ] Post issue on GitHub PR with screenshot/details
- [ ] Cursor investigates and fixes
- [ ] Repeat verification

---

## Step 13: Final Approval to Go Live

**Only after Step 12 verification passes:**

AJ posts final approval:
```
✅ FINAL APPROVAL — Ready for live theme

Draft pages verified. Content is correct. 
You may now push to LIVE theme if needed.
```

Cursor waits for this message before any live push.

---

## Rollback Plan (If Anything Goes Wrong)

If the draft push causes issues:

```bash
# Revert the Shopify draft theme to previous state
shopify theme push --theme 187144929571 --force
# This re-uploads the theme from your local repo
```

Or simply re-upload the previous working versions from backup.

---

## Summary

| Step | Action | Owner | Gate |
|------|--------|-------|------|
| 1 | Create recovery branch | Cursor | — |
| 2 | Restore files from git | Cursor | — |
| 3 | Verify Liquid sections | Cursor | — |
| 4 | Commit with clear message | Cursor | — |
| 5 | Push to GitHub | Cursor | — |
| 6 | Create PR | Cursor | — |
| 7 | Review & approve | AJ | ✅ **AJ APPROVAL REQUIRED** |
| 8 | Merge to main | Cursor | — |
| 9 | ⛔ STOP — Wait for AJ | Cursor | ✅ **WAIT FOR AJ COMMENT** |
| 10 | Verify files & content | AJ | ✅ **AJ CHECKS MOCKUPS** |
| 11 | Push to draft theme | Cursor | ✅ **ONLY IF AJ APPROVED** |
| 12 | Verify draft preview | AJ | ✅ **AJ MUST VERIFY** |
| 13 | Final approval for live | AJ | ✅ **AJ MUST SIGN OFF** |

---

## Questions?

- **Where did these come from?** GitHub commit `fed5cf0` (Oct 1, 2026)
- **Why were they lost?** Someone/something overwrote them in the Shopify draft theme
- **Is this safe?** Yes — draft-only push, reviewed, verified before live
- **Can we rollback?** Yes — anytime before or after live publish

---

**Start here. Follow the checklist step by step. No skipping.**
