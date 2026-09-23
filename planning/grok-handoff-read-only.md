# Grok handoff — READ ONLY (2026-09-10)

**Status:** Ingest only. Do **not** edit, commit, push, publish, or request write access until Andrew says so.  
**Push stays in Cursor** on Andrew’s machine.  
**Grok:** read this note + the listed repo paths. Confirm what you can reach. Stop.

---

## Minimum viable (one screen)

| Item | Value |
|---|---|
| Design Review | https://github.com/barreletics/Barreletics-Design-Review |
| Default branch | `main` |
| Cursor working branch | `finish-home-collections` |
| Store | `barreletics.myshopify.com` · primary domain **barreletics.com** |
| QA draft (only push target) | **`187144929571`** · `🔥🔥 Redesign — Latest` / M4 Visual QA · **never publish** |
| Live (forbidden) | **`185687998755`** |
| Retired draft (dead) | `187143618851` — do not use |
| Auth | Lives in **Cursor / Andrew’s Shopify CLI login**. Not Theme Access. Not a repo token. **Grok: no store auth yet.** |
| Preview pattern | `https://barreletics.com{path}?preview_theme_id=187144929571` — **never** paste myshopify preview URLs (301 drops the cookie) |
| Home | https://barreletics.com/?preview_theme_id=187144929571 |
| Shop All | https://barreletics.com/collections/barre-pilates-yoga-shoe-sock-footwear?preview_theme_id=187144929571 |
| Closed PDP | https://barreletics.com/products/best-reformer-pilates-legree-workout-shoes?preview_theme_id=187144929571 |
| Open PDP | https://barreletics.com/products/studio-performance-skin-footwear?preview_theme_id=187144929571 |
| Editor | https://admin.shopify.com/store/barreletics/themes/187144929571/editor |
| Ops repo | https://github.com/barreletics/barreletics-ops — **separate · read-only for Grok** · not the theme |
| Top 3 to inventory first | `fifty-fifty` · Open `product.in-studio-template.json` vs `product.open-sole.json` · `pdp-sock-math` |

---

## 1. Shopify MCP / store access

### What Cursor already has vs what Grok needs

| Channel | What it does | Enough for draft-theme reality? |
|---|---|---|
| Shopify **dev** MCP (`learn_shopify_api`, `search_docs_chunks`, `validate_theme`, Liquid validate) | Docs + static theme check | **No.** Cannot see TE state, cannot push, cannot three-way compare draft vs repo |
| Shopify **store** MCP (`user-shopify-store`) | Products / orders / customers | Not the theme |
| **Shopify CLI** on Andrew’s Mac (`shopify` **3.94.3**) | `theme pull` / `theme push` against a named theme ID | **Yes.** This is how draft QA works |

### Auth today

- **Shopify CLI staff/Partner login** on Andrew’s machine (session in Shopify CLI kit config).  
- **Not** a Theme Access password in the repo.  
- **Not** a custom-app Admin token checked into Design Review.  
- **Default for Grok:** *Auth still lives in Cursor. Grok read-only until Andrew sets Theme Access (or equivalent) for read.*  
- Cursor keeps **all push**. Grok does not get write.

### Only allowed theme target

```
Store:  barreletics.myshopify.com
Push:   --theme 187144929571 --path shopify-build
Live:   185687998755  → NEVER pull, push, publish, or “backcopy”
```

Andrew must **name `187144929571` in the same message** before any CLI mutation. No ID → no push.

### Exact CLI (Cursor)

From repo root. **One `--only` per file.** Never space-separate multiple `--only` patterns (silent drop). Read **all** stdout — success box can hide `─ error ─`.

```bash
# Pull one TE-owned JSON (Shopify → repo). Never the whole theme.
shopify theme pull --theme 187144929571 --path shopify-build --only templates/product.in-studio-template.json

# Push one code file (repo → draft). Typical: liquid only.
shopify theme push --theme 187144929571 --path shopify-build --only sections/fifty-fifty.liquid

# Then another file if needed
shopify theme push --theme 187144929571 --path shopify-build --only templates/product.in-studio-template.json
```

Verify (cookie jar required — first hit sets preview cookie):

```bash
curl -s -c /tmp/m4.txt -o /dev/null -L "https://barreletics.com/?preview_theme_id=187144929571"
curl -s -b /tmp/m4.txt -o /tmp/p.html -L "https://barreletics.com/products/studio-performance-skin-footwear?preview_theme_id=187144929571"
```

### Push exclude / never-touch (blast radius)

**Never push unless Andrew names that exact file in the CURRENT message:**

- `templates/index.json` (Home LOCKED)
- `templates/product.json` (Closed spine)
- `templates/collection.json` (Shop All SIGNED)
- any other `templates/*.json`
- `config/settings_data.json`
- whole-theme push / pull

**Never, even if named casually:**

- Live theme `185687998755`
- Publish / rename / delete theme
- `git restore` / checkout of `shopify-build/sections/**` or `templates/**` without Andrew saying **`restore X`**
- Local donor `/Users/andrewnehra/barreletics-theme-live-apr2026` as a push target

**Radioactive (fix-forward only, no “rollback to older freeze”):**  
`home-juicer.liquid` · `proof-numbers.liquid` · `value-strip.liquid` · `footer.liquid` · `pdp-buy-box.liquid` · `index.json` · `product.json`

### Theme Check

- Documented as **`shopify theme check`** (`docs/24-known-technical-debt.md`).  
- **No** `.theme-check.yml` in `shopify-build/`.  
- Cursor does **not** run Theme Check on every push.  
- Shopify MCP `validate_theme` is the optional static check.  
- Schema trap: omit empty `"default": ""` — Shopify rejects blank defaults.

### Preview / Editor (use these)

```
Storefront:  https://barreletics.com/<path>?preview_theme_id=187144929571
Editor:      https://admin.shopify.com/store/barreletics/themes/187144929571/editor
Editor+path: https://admin.shopify.com/store/barreletics/themes/187144929571/editor?previewPath=%2Fproducts%2Fstudio-performance-skin-footwear
```

CLI prints `barreletics.myshopify.com?preview_theme_id=…` — **rewrite to barreletics.com**. myshopify 301 drops the preview param and serves **live**.

Tell Andrew to reload once: first hit may still look live.

---

## 2. Design Review repo

| | |
|---|---|
| URL | https://github.com/barreletics/Barreletics-Design-Review |
| Default | `main` |
| Active work | `finish-home-collections` (tracks `origin/finish-home-collections`) |
| Theme code | `shopify-build/` |
| Hub mocks | `docs/` (Locked HTML — never overwrite v16/v19/WORKING Home/Collection v18 in place) |
| Freeze | `planning/m4-section-freeze.md` |
| Page map | `planning/page-template-registry.md` |

**How Cursor talks to GitHub:** local `git` + `gh` on Andrew’s Mac, remote `origin` = that HTTPS URL. Cloud-agent PRs later need GitHub write — **not granted**. Grok: no commit, no PR, no force-push.

**barreletics-ops:** https://github.com/barreletics/barreletics-ops · disk `/Users/andrewnehra/barreletics-ops` · branch `main`. Returns / 3PL / manufacturing / social. **Not the theme. Read-only for Grok.** Do not mix ops tasks into Design Review theme edits.

---

## 3. Operating system

### Source of truth

| Layer | Wins | Loses |
|---|---|---|
| **Repo `shopify-build/` Liquid / CSS / JS / snippets** | Design System master | — |
| **Draft TE JSON** on `187144929571` (images, crop, copy, order, section settings) | **User-owned** while QA’ing. Pull into repo after approve. | Stale local `templates/*.json` |
| **Andrew’s CURRENT message** | Beats freeze docs and older commits | Older freeze rows |
| **Shopify live** | Brian integrates from approved repo | Agents |
| **GitHub** | Code history | Visual approval (Andrew cannot approve from a PR alone) |
| **barreletics-ops** | Ops / fulfillment / ads ops | Theme sections |

**Sync rule (HARD):**

1. During tweaks: push **liquid/CSS/JS only**. Do not push template JSON over TE.  
2. Before a JSON edit: `theme pull --only` **that one file**, diff, keep his media.  
3. After `approved` / `lock it`: pull that JSON into the repo; commit only if he asked.  
4. Never “fix drift” by pushing stale repo JSON or `git restore`.  
5. No passphrase (`photos stuck` etc.). Agent pulls.

Open Sole live Admin suffix is **`in-studio-template`** → file `templates/product.in-studio-template.json`. Keep `product.open-sole.json` key-identical. Do not flip Admin to `open-sole` without a letter.

### Architecture conventions

- One capability = one `sections/*.liquid` + schema + presets. No coupling. Shared bits = `snippets/` + `assets/`.  
- Contract: `planning/m4-section-library-CONTRACT.md`.  
- **Do not** merge `pdp-features` into `fifty-fifty`.  
- `fifty-fifty.liquid` is **shared** (Home / Shop All / Apparel / PDP). A Liquid change hits many templates.

**Breakpoints / media (current practice):**

| Surface | Desktop media | Phone media | Notes |
|---|---|---|---|
| Home 50/50 | min **640** | often **320** (some 480) | Home `fit` **may resize** the frame |
| Apparel 50/50 | **640** | **530** | Schema defaults |
| **PDP 50/50 (Open+Closed)** | min **560** (text may grow) | **550** (Liquid force) | Phone text pad **104/104** · side **20** |
| Home split-hero | **92vh** · split **62/38** · crop **50/22** · cover | same crop | Do not grow the box to fit the photo |
| Fullbleed wow | height **80** desktop / **60** phone | — | TRANSFORM / lifestyle |

**Image recipes (do not flip):**

- Default / fill / sock-era desktop / Stef / Coperni tiles → **`cover` · scale 100 · X/Y only**  
- “Whole photo / don’t crop” → **`fit` · 100** inside the **locked frame**  
- Open **Never slip in chair pose** → **`fit` · 100 · NEVER cover**. Frame stays 550 / 560-min  

Theme Editor sidebar crop **lies** on `cover` (narrow pane ≠ 1440). Approve at **1440** storefront, sidebar closed. Rule: `.cursor/rules/te-sidebar-crop-lies.mdc`.

**Media vs text:** same section, independent TE keys *when Liquid honors them*. On **product** pages Liquid **ignores** phone photo height, phone text pad, phone section gap (locked 550 / 104 / 0). Working: Media fit, Custom X/Y (only if focal = Custom), desktop pad / gap. See `.cursor/rules/pdp-fifty-fifty-te-controls.mdc`.

**Schema:** one `--only` file; no blank `"default": ""`; range increments already in each section schema. Do not invent a fourth `object-fit`.

### Safety / blast radius (shared files)

Change once → many pages:

- `sections/fifty-fifty.liquid`  
- `sections/fullbleed-statement.liquid`  
- `sections/pdp-buy-box.liquid` (Closed + Open + Outdoor + one-offs)  
- `sections/home-juicer.liquid`  
- `sections/footer.liquid` + header-group  
- `assets/chrome.css` · `assets/design-tokens.css` · `assets/split-hero.css`

**Do-not-touch list (expand):**

- Live `185687998755`  
- Locked mocks: `docs/Barreletics PDP - Definitive-v16.html`, `…-v19.html`, Home `Definitive-WORKING.html`, Collection v18, SEO v36  
- `pdp-buy-box` layout/CSS without a buy-box letter  
- Home `split-hero` + Coperni in the same turn  
- Chair Pose → Cover  
- Pool / dishwasher / “fully enclosed” copy  
- Dead URLs: `/blogs/journal` · `/pages/help` as a product · `/collections/open-sole|closed-sole|outdoor`

### Known inconsistent (inventory first)

1. **`fifty-fifty`** — one Liquid, three families (Home 640/320 · PDP 560/550 · Apparel 640/530). TE sliders lie on PDP. Open vs Closed pads were being twinned then un-twinned. Fit vs Cover fight.  
2. **Open PDP templates** — live file is `product.in-studio-template.json`; `product.open-sole.json` must match named keys. Agents keep pushing the wrong one.  
3. **`pdp-sock-math`** — not a 50/50. Open pad/unframed photo ≠ Closed. Do not “match” it to 550/560.

Also hot: Chair Pose yellow lock vs “make all photos the same size.”

### QA checklist (already used)

**Viewports:** **1440** desktop (TE sidebar closed) · **390** phone. Optional TE-narrow ~900 to know cover will differ.

**Code bug vs image geometry:**

- Frame size / pad / type wrong on **both** Open and Closed → Liquid.  
- One heading’s crop / face / letterbox → that section’s `media_fit` + Custom X/Y only.  
- “Doesn’t match Closed” but Closed itself has mixed TE pads (32 / 80 / 120) → ask, don’t copy outliers unless named.  
- Never claim done from Theme Editor with sidebar open.

**Done (before human visual review):**

1. Named heading / one surface  
2. Pulled TE if JSON touched  
3. Measured that block at 1440 + 390  
4. Preview + Editor links on `barreletics.com`  
5. Stop. Wait for `approved` / `looks good`  
6. Then freeze **forward** + commit only signed files  

Cycle: `.cursor/rules/finish-approve-lock.mdc`

### Canonical paths (read these)

```
planning/grok-handoff-read-only.md          ← this file
planning/m4-section-freeze.md
planning/page-template-registry.md
planning/m4-section-library-CONTRACT.md
docs/02-theme-architecture.md
docs/09-PRODUCT-KNOWLEDGE.md
docs/10-DECISIONS.md
docs/11-CANONICAL-ANSWERS.md
docs/24-known-technical-debt.md
specs/frozen/pdp.md
specs/frozen/homepage.md
.cursor/rules/shopify-draft-theme-only.mdc
.cursor/rules/te-user-state-sync.mdc
.cursor/rules/anti-revert-fail-closed.mdc
.cursor/rules/always-give-a-verified-link.mdc
.cursor/rules/image-in-the-frame.mdc
.cursor/rules/chair-pose-yellow-fit.mdc
.cursor/rules/pdp-fifty-fifty-te-controls.mdc
.cursor/rules/heading-is-the-target.mdc
.cursor/rules/click-the-thing-he-sees.mdc
.cursor/skills/barreletics-page-qa/SKILL.md
.cursor/skills/barreletics-anti-revert/SKILL.md
shopify-build/DEPLOYMENT_CHECKLIST.md
```

No root `AGENTS.md`. No dedicated push runbook file — CLI rules live in `always-give-a-verified-link.mdc` + `te-user-state-sync.mdc`.

---

## Grok first reply (required)

1. What you can open (GitHub Design Review / ops / Shopify).  
2. What you cannot (draft theme files, TE, CLI).  
3. Confirm: **no edit, no commit, no push** until Andrew approves.  
4. Then wait.
