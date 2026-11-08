# Cart + bundles implementation source bundle (read-only)

**Created:** 2026-11-08 ~12:57 PM ET (cloud save after Andrew closure-gate decision)  
**Purpose:** Pass authoritative planning/register context to a Design Review–scoped agent that cannot read `alternate-projects`.

## Contents
| Path | Role |
|------|------|
| `docs/bots/BOOT.md` | Load order |
| `docs/bots/GROUND-ZERO-README.md` | Private ops pointer (full doc not in bundle) |
| `docs/bots/THEMES.md` | **Only file in bundle that may contain numeric theme IDs** |
| `docs/bots/STATUS.md` | Status board |
| `docs/bots/RULES.md` | Global P0 rules |
| `docs/bots/shopify-theme/HOME.md` | Lane SAFETY HOLD + scoped DRAFT go |
| `docs/bots/shopify-theme/DECISIONS.md` | Lane decisions incl. closure gate + 35% pants |
| `docs/bots/shopify-theme/HISTORY.md` | Append-only lane history |
| `docs/bots/shopify-theme/BUILD-PLAN-MIX-MATCH-ROTATION-2026-11-07.md` | Build plan + §4.1 Admin sync |

## Authorized scope (unchanged)
- **DRAFT row** Nov 08 · Cart + bundles only (see THEMES.md).
- Pants **35%** on proposed **$98 → $63.70**; feature flag default **off**; preserve **2FOR15** and separate **variant-selector** color-sync.
- No LIVE publish, test orders, global Admin discounts, or live price changes without separate goes.

## Execution evidence (parent-reported + partial verify)
- Design Review PR #48 open; 10 math tests pass; **not** deployed to Shopify **DRAFT row**.
- **Blocker:** deployment Mac with Shopify CLI offline; no private workers connected at bundle time.

## Gate validation
Bundle satisfies **(3) exact BLOCKED** with supporting docs for **(2)** continue on PR #48 + deploy when CLI path returns — not setup-only closure.
