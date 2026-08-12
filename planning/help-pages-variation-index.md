# Help pages — variation index (PICK SESSION)

**Status:** READY FOR ANDREW  
**Theme:** M4 `187144929571`  
**Authority:** Help menu = About · FAQ · Contact · Returns (`planning/navigation-menu-spec.md` Step 2)  
**Rule:** Do not implement until Andrew marks **USE THIS** (or names the winner in a letter).

**M4 preview pattern:** `https://barreletics.myshopify.com{path}?preview_theme_id=187144929571`  
**Hub:** `docs/index.html` → Help family  

Mark each page: `USE THIS → [variation]` or paste your pick.

---

## Help menu (4)

### 1) About Us — `/pages/our-story`

| | |
|---|---|
| **Repo templates** | `shopify-build/templates/page.our-story.json` · `page.about.json` (confirm Admin assignment) |
| **Admin suffix** | Confirm `our-story` / `about` / default |
| **M4 preview** | https://barreletics.myshopify.com/pages/our-story?preview_theme_id=187144929571 |

| Variation | Hub / path | Role |
|---|---|---|
| A — Live M4 (repo template as assigned) | preview link above | Current runtime |
| B — Brand story mock v1 | `docs/Barreletics Brand - Definitive-v1.html` | Prior / missing on disk — do not overwrite |
| B2 — Brand story mock v2 | `docs/Barreletics Brand - Definitive-v2.html` | **BUILD / REFINE** (A1 cloud) — dual lifestyle + live chapters · see `docs/HELP-OPEN-ME.html` |
| C — Help hub framing | `docs/Barreletics Help - Definitive-v3.html` (Locked Help hub) | Hub links out — not the About body itself |
| D — Help hub footer-fix candidate | `docs/Barreletics Help - Definitive-v4.html` | Footer only candidate; say LOCK THIS to promote |

**Andrew pick:** USE THIS → ___

---

### 2) FAQ — `/pages/faq`

| | |
|---|---|
| **Repo template** | `shopify-build/templates/page.faq.json` |
| **Admin suffix** | `faq` |
| **M4 preview** | https://barreletics.myshopify.com/pages/faq?preview_theme_id=187144929571 |

| Variation | Hub / path | Role |
|---|---|---|
| A — Live M4 | preview above | Current runtime |
| B — FAQ v4 | `docs/Barreletics FAQ - Definitive-v4.html` | **Locked** authority (registry) |
| C — FAQ v5 | `docs/Barreletics FAQ - Definitive-v5.html` | Pool purge copy experiment |
| D — FAQ v6 | `docs/Barreletics FAQ - Definitive-v6.html` | Prior — counts/cards rejected |
| E — FAQ v7 | `docs/Barreletics FAQ - Definitive-v7.html` | Quiet premium head — promote only with LOCK THIS |

**Andrew pick:** USE THIS → ___

---

### 3) Contact Us — `/pages/contact-us-form`

| | |
|---|---|
| **Repo template** | `shopify-build/templates/page.contact-us-form.json` |
| **Admin suffix** | `contact-us-form` |
| **M4 preview** | https://barreletics.myshopify.com/pages/contact-us-form?preview_theme_id=187144929571 |
| **Dead** | `/pages/contact` → 404 · use contact-us-form |

| Variation | Hub / path | Role |
|---|---|---|
| A — Live M4 | preview above | Current runtime |
| B — Contact v1 mock | `docs/Barreletics Contact - Definitive-v1.html` | Hub, not Locked |

**Andrew pick:** USE THIS → ___

---

### 4) Returns & Exchanges — `/pages/returns`

| | |
|---|---|
| **Repo templates** | Live Admin often `page.shipping-retruns.json` *(typo)* · clean `page.returns.json` |
| **Admin suffix** | Often `shipping-retruns` — do not re-point without letter |
| **M4 preview** | https://barreletics.myshopify.com/pages/returns?preview_theme_id=187144929571 |
| **Banner deep link** | `/pages/returns#returns` |

| Variation | Hub / path | Role |
|---|---|---|
| A — Live M4 / Admin body | preview above · hub **Current** | **Canonical** — `docs/REVIEW-2026-08-08.html#returns` |
| B — Returns mock v3 | `docs/Barreletics Returns - Definitive-v3.html` | **Superseded** concept — not store behavior |

**Andrew pick:** USE THIS → ___

---

## Support satellites (not Help ▾ menu, but related)

### 5) Size Chart / Size Guide

| | |
|---|---|
| **Repo templates** | `page.performance-skins-size-chart.json` · `page.size-guide.json` · `page.size-chart.json` |
| **Hub mock** | `docs/Barreletics Size Chart - Definitive-v1.html` |
| **Confirm live handle** | Check Admin before linking |

**Andrew pick:** USE THIS → ___ / skip for later

---

### 6) Returns portal — `/pages/returns-portal`

| | |
|---|---|
| **Repo templates** | Live often `page.start-a-retrun.json` *(typo)* · clean `page.returns-portal.json` |
| **M4 preview** | https://barreletics.myshopify.com/pages/returns-portal?preview_theme_id=187144929571 |
| **Live behavior** | ReturnZap embed (app UI) |
| **Mock** | `docs/Barreletics Returns Portal - Definitive-v1.html` — **superseded** bespoke form |

**Andrew pick:** USE THIS → live ReturnZap / other: ___

---

## Not Help menu (do not confuse)

| Item | Note |
|---|---|
| `/pages/help` | **404** — no `page.help.json`. Help = dropdown, not a page |
| Shipping / warranty templates | Exist in repo (`page.shipping.json`, `page.warranty.json`) — confirm if linked in footer Support |
| Reviews / Judge.me | `/pages/reviews` — not Help menu |
| Ambassador / partners | Track E — not Help pick |

---

## Pick session reply template

Paste back:

```
HELP PICKS
About: USE THIS → …
FAQ: USE THIS → …
Contact: USE THIS → …
Returns: USE THIS → …
Size: USE THIS → … / later
Portal: USE THIS → …
```
