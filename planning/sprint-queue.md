# Sprint queue — parallel workflow (awake + overnight)

**Repo:** ★ Barreletics-Design-Review · `shopify-build/`  
**Theme:** M4 Visual QA **`187144929571`** only — never publish · never other theme IDs  
**OS:** anti-revert · freeze · Finish → Approve → Lock → Next · CURRENT MESSAGE WINS  
**Protocol:** `planning/cloud-night-protocol.md`

**Statuses:** `QUEUED` → `IN PROGRESS` → `AWAITING ANDREW` → `APPROVED` → `LOCK`

**Parallel law:** Different rows / files only. **One writer per surface per turn.** Never touch LOCKED surfaces without Andrew letter.

**Preview base:** `https://barreletics.myshopify.com{path}?preview_theme_id=187144929571`  
**Editor:** `https://admin.shopify.com/store/barreletics/themes/187144929571/editor`

---

## Track A — Help menu pages

| ID | Page / section | Owner | Status | Preview / artifact | Notes |
|----|----------------|-------|--------|--------------------|-------|
| A0 | Decide board | desktop | **AUTHORITY** | `docs/HELP-OPEN-ME.html` · `planning/help-family-type-law.md` · cloud prompt | Help v8 · type law HARD |
| A-help | Help hub | desktop | **LOCKED 2026-08-15** | `/pages/help` | Andrew: lock help |
| A1 | About Us `/pages/our-story` | desktop | **LOCKED 2026-08-13** | Mock v25 | Do not thrash |
| A2 | FAQ `/pages/faq` | desktop | **LOCKED 2026-08-15** | FAQ | Andrew: lock help |
| A3 | Contact | desktop | **LOCKED 2026-08-15** | `/pages/contact-us-form` | Do not thrash |
| A4 | Policy `/pages/returns` | desktop | **LOCKED 2026-08-14** | `/pages/returns` | Full page lock |
| A5 | Size chart | desktop | **LOCKED 2026-08-12** | Size guide signed | Do not thrash |
| A6 | Returns portal | desktop | **LOCKED 2026-08-15** | `/pages/returns-portal` | Andrew: lock help |

---

## Track B — PDP pages (section-by-section)

| ID | Page / section | Owner | Status | Preview / artifact | Notes |
|----|----------------|-------|--------|--------------------|-------|
| B0 | Closed Sole — content micro-check | desktop | **IN PROGRESS** | `/products/best-reformer-pilates-legree-workout-shoes` | Copy conflicts fixed 2026-08-15. Layout already approved. |
| B1 | Closed — reviews photo cards → Judge.me Leslie / B P. / Tracie | — | QUEUED | same | Photos + copy; do not thrash LOCKED buy-box |
| B2 | Closed — commit video (TBD) | — | QUEUED | same | No recycled brand clips until new asset |
| B3 | Open Sole walk | — | QUEUED | `/products/studio-performance-skin-footwear` | After Closed AWAITING clear enough |
| B4 | Outdoor walk + earmarked videos | — | QUEUED | `/products/aquatic-performance-skins` | Live A/B + d57 earmarked |
| B5 | One-off Closed / Open polish | — | QUEUED | one-off handles | Respect one-off-buy-box-lock |

---

## Track C — Global PDP sync

| ID | Page / section | Owner | Status | Preview / artifact | Notes |
|----|----------------|-------|--------|--------------------|-------|
| C0 | Changelog log | any | **IN PROGRESS** | `planning/pdp-global-changelog.md` | Append on every global PDP change |
| C1 | Sync sweep (when triggered) | — | QUEUED | all `product*.json` | Only after a logged global change |

---

## Track D — Home page

| ID | Page / section | Owner | Status | Preview / artifact | Notes |
|----|----------------|-------|--------|--------------------|-------|
| D0 | Home final refinement | — | QUEUED | `/` | **BLOCKED** until B+C have no open AWAITING for PDP globals |

---

## Track E — Ambassador links

| ID | Page / section | Owner | Status | Preview / artifact | Notes |
|----|----------------|-------|--------|--------------------|-------|
| E0 | Research + recommendation | **cloud** | **AWAITING ANDREW** | `planning/ambassador-program-recommendation.md` · [Review +149 −1](bc-f59087ec-9ea5-47ff-a171-b9d0788b3684#changes) · [PR #21](https://github.com/barreletics/Barreletics-Design-Review/pull/21) | Decision brief ready — no app install · no theme edit until Andrew approves plan |

---

## How to claim a row

1. Set **Owner** = `desktop` | `cloud` | agent id  
2. Status → `IN PROGRESS`  
3. Work only that row’s files  
4. Stop at `AWAITING ANDREW` with M4 preview link (or artifact path for research)  
5. Andrew: `approved` / `fix X` → agent locks → next row  

---

## Locked — do not touch without letter

Header nav #2 · v20d fold chrome · Closed buy-box fold/ATC · Description accordion TE · value-strip + pdp-features · TRANSFORM · Closed badge default rust · Definitive-v16/v19 HTML · signed freeze rows in `planning/m4-section-freeze.md`
