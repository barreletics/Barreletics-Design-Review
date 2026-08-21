# Type OS — owner + agent guide

**Status:** WORKING — sign off after `docs/type-os-specimen.html` review  
**Code source:** `shopify-build/assets/design-tokens.css`  
**Deep spec:** `planning/m4-type-hierarchy.md`  
**Visual mock:** `docs/type-os-specimen.html`

---

## One rule

**Weight falls as size rises.** Big type = lighter weight. Small type = can be bolder.

---

## Locked roles (Roboto unless noted)

| Role | Weight | Size | Where |
|------|--------|------|--------|
| **Hero** | 700 | 50–72px | Home hero only |
| **Big 50/50 title** | **500** | **38–52px** | All `fifty-fifty` with `heading_register: display` |
| **Section title** | 600 | 26–32px | Variant grid, wayfinding headings |
| **Statement band** | 500 | 28–36px | TRANSFORM / `fullbleed-statement` |
| **Features block title** | 400 | 28–40px | `pdp-features` main title |
| **Feature row name** | 700 | 26px | Each grip feature label |
| **Body** | 400 | 16px | 50/50 body, FAQ answers, most blurbs |
| **Lede** | 400 | 17px | Reviews header, some intros |
| **Label / eyebrow** | 600 | 11px caps | Eyebrows, small UI labels |
| **Trust strip** | 500 | 12px | Value strip under ATC |

---

## Section → type map (PDP body)

| Section | Title type | Body type |
|---------|------------|-----------|
| `fifty-fifty` | Big 50/50 · 500 · 38–52px | Body · 400 · 16px |
| `pdp-features` | Features title · 400 · 28–40px | Body · 400 · 16px |
| `disciplines` | Label · 500 · 12–14px | — |
| `variant-grid` | Section · 600 · 26–32px | Body · 400 · 16px |
| `fullbleed-statement` | Statement · 500 · 28–36px | Body · 400 · 16px (if any) |
| `pdp-sock-math` | Display or 400 · 36–52px | Body · 14–16px |
| `guarantee-band` | Point · 700 · 14px | Body · 400 · 16px |
| `social-proof` / reviews | Lede · 400 · 17px | Quote · 400 · 14–20px |
| `collection-faq` | Question · 600 · 16px | Answer · 400 · 16px |
| `coperni-crosslink` | **See Coperni row below** | Georgia italic subhead |
| `coperni-pdp-story` | Big 50/50 elsewhere | Body 400 · quote Georgia italic |

---

## Do not unify

| Surface | Type | Why |
|---------|------|-----|
| **Buy-box lede** | Roboto 400 · 30–40px | Product column — own lane |
| **Buy-box desc** | Roboto 400 · 14px | Short, under price |
| **Nav / footer / CTA** | Separate UI tokens | Not page body story type |

---

## Coperni (pending lock)

| Line | Current | Target |
|------|---------|--------|
| Banner title | Roboto 500 · 38–52px (matches 50/50) | **Approve 500** or **switch to 400** |
| Banner subhead | Georgia 400 italic · 14–19px | Keep italic or match body? |
| Story quote | Georgia 400 italic · 22–30px | Keep or Roboto? |
| Runway note | Georgia 400 italic · 19px | Keep or Roboto? |
| 50/50 blocks on Coperni PDP | Same as Closed | **Locked — no change** |

---

## Agent rules

1. **Never** change buy-box lede to match 50/50 titles.
2. **Never** use Georgia / italic on new pages unless Coperni-style exception is approved.
3. **Never** use weight 700 on big display titles (hero excepted).
4. New 50/50 sections: `heading_register: display` · body one short line · no repeat phrases on same page.
5. Copy changes only in JSON TE — type changes in `design-tokens.css` + section CSS with owner letter.

---

## Sign-off checklist

- [ ] Andrew reviewed `docs/type-os-specimen.html`
- [ ] Coperni banner weight picked (500 vs 400)
- [ ] Coperni Georgia italics — keep or kill
- [ ] Update this file status to **LOCKED** + date
- [ ] Add row to `planning/m4-section-freeze.md` if needed
