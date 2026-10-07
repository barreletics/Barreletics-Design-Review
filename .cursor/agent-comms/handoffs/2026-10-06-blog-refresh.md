# Blog refresh — 2026-10-06 ~6:40 PM ET
Old bot: Blog `bec64e87-ca86-4ca2-99f1-c8773f115ed9` (serverId 5829589). ~1,724 messages — overdue.

## Role / lane
Barreletics Journal only (Shopify blog handle `news`). Write SEO/brand posts; create/update via Admin GraphQL as inactive unless Andrew says publish. Does NOT touch draft theme 187144929571, Home, PDP, or About layout — those go to active Website `1cc40bf6-99eb-41ac-ba63-0f5b3991f508` (Site Design). Sibling to Marketing / Site Design. Not Email Templates or Partner codes.

## Sidebar / routines / groups
- Section: put new bot in **Marketing** (`section-mu3yyrzg-4`) unless Front Desk sees the old row elsewhere; this agent folder has no section field on disk.
- Routines: none.
- Group chats: none known.

## How to push Journal changes
Andrew's Mac `b9c0e142-7e3d-4710-856d-c6a9caf6d9cf` (`/Users/andrewnehra`). Copy GraphQL + vars with CopyFromBox, run `shopify store execute --store barreletics.myshopify.com [--allow-mutations] --query-file … --variable-file …`, delete temp files. Mutation: `articleUpdate` (see `/workspace/barreletics-blog-drafts/itsliquid-restore-2026-10-04/update.graphql`). SEO: upsert metafields `global.title_tag` / `global.description_tag`. Cloudflare often blocks admin publish from bots — Andrew can flip live himself. Prefer Mac CLI over navigating his Mac UI (token burn).

## Guardrails (copy / brand)
- Style D body: `<h2 class="article-dek">`, then `<p class="article-lead">`, plain `<p>`; no inline styles; no in-body eyebrow; featured image after title with variety (avoid overused red/coral + pink shoe).
- Founder: first mention "Founder Stefanie Miller" (f spelling), then "she". Never "Miller" alone. Link her posts when relevant.
- Conversational editorial, never press-release tone. No placeholders/TBD/invented quotes. Research public facts yourself.
- Double Failure lock: sock never really grips the floor AND foot slides inside (like underwear two sizes too big). Never say the sock grips the floor while the foot slides inside.
- ITSLIQUID = international art platform (Venice, London, Barcelona…), not "Italy/Italian" in titles. Biennale: "at the Venice Biennale" OK; no award claim; Ghost Performance Skin = prototype only, never for sale / never in Venice title.
- "No latex. No silicone." approved. "patented" allowed (as of 2026-10-04).
- Complete SEO (title, description, tags, summary), featured index image, alt on every image. Titles: fit ≤2 lines at 390 and 1440 (Roboto 700).
- Keep replies short; batch work; few screenshots. Andrew often can't re-read full drafts — verify against all checks and give a concise all-clear.

## Draft / backup locations
- Working drafts: `/workspace/barreletics-blog-drafts/`
- Git backup (barreletics-ops): branch `blog-backups-2026-10-06` (origin), commits `9affd55` (full folder under `blog-backups/`) + `1781829` (Double Failure prep). Open a PR if none exists; do not merge/force-push.

## OPEN — Double Failure Journal push (BLOCKED on Mac 2026-10-06)
Live still wrong as of 6:35 PM ET curl: title still Italy/Italian SEO; body still "could grip the floor".
Prep ready in `/workspace/barreletics-blog-drafts/double-failure-fix-2026-10-06/` (`build_updates.py`, `all.graphql`, `update.graphql`). When Mac is reachable:
1. Pull all articles+pages → `all-pull-before.json`; commit to backup branch.
2. Push exact replaces for:
   - ITSLIQUID `614612631843`: title → `ITSLIQUID on the End of the Grip Sock`; SEO title → `International Art Platform ITSLIQUID on the End of the Grip Sock`; Double Failure sentence → never-really-gripped / two-sizes-too-big wording (pre-edited body also in `itsliquid-restore-2026-10-04/body.html`; keep `body.v2-pre-2026-10-06.html`).
   - Anthropologie `614545064227`: "Those dots can grip a surface…" → never-really-grip-the-floor wording in build_updates.py.
   - Beyond Yoga Socks `614544965923`: "Grip underneath a sock can hold the sock to the floor…" → never-really-holds wording in build_updates.py.
3. Verify pull + live URLs. Scan other article/page hits; leave Grip Socks "needs to grip the surface" and foot exercise cues alone unless Andrew asks.
Theme/pages sitewide sweep: active Website `1cc40bf6` (already briefed; hit list to Andrew before push).

## Other open items
- Barre Anywhere `555660771431`: 3 approved edits in `barre-anywhere-2026-09-30/proposed.html` — NOT live; wait for Andrew.
- Free People: replace second chocolate pour still with a regular product shot (`fp-product`).
- Grip socks + Anthropologie: missing dek on some posts historically — confirm live.
- Flag to Stefanie: "feel more confident and secure"; "barefoot-like" (INTERNI).
- Unsourced "officially recognized at the Venice Biennale" in Kraiburg email / Help Scout — don't spread.
- Earmarked line for Website: "Questioning something everyone else accepted" (ITSLIQUID heading).

## Live Journal anchors (verify before edit)
- ITSLIQUID live: https://barreletics.com/blogs/news/barreletics-itsliquid-performance-skin (article `614612631843`)
- Venice, Coperni, Free People, Anthropologie, Beyond Yoga Socks, Grip socks, INTERNI — IDs/bodies under the draft folders above.

## First message for new bot
Read `/workspace/handoffs/2026-10-06-blog-refresh.md`. Do not rescan or re-audit. Priority: finish Double Failure Shopify pushes when Mac is online. Then wait for one task.
