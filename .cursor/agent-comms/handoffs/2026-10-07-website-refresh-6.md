# Website bot handoff — refresh #6 (2026-10-07 ~12:30 PM ET)
From: Website bot 9230b3b5 (Site Design). Prior handoff: /workspace/handoffs/2026-10-06-website-refresh-5.md (read it too).

## Hard rules
- Draft theme 187144929571 ONLY. Never touch/publish live 185687998755. No live-affecting Admin Pages/blog/product/variant edits unless Andrew says so at publish.
- Push via Shopify CLI on Andrew's Mac (machineId b9c0e142-7e3d-4710-856d-c6a9caf6d9cf, store barreletics.myshopify.com). Per file: mktemp → fresh pull --only <file> → .bak → string edit only (never re-serialize JSON) → validate JSON (strip leading /* */) → diff -u → re-pull right before push, md5 must equal .bak (else redo on newest) → `push --theme 187144929571 --only <file> --nodelete` → pull-verify md5 → curl/screenshot preview. Never push from Design-Review main/PR branches.
- Don't overwrite Andrew's Theme Editor work. Stale editor tabs caused today's Open Sole reverts; give him a fresh editor link before he edits: https://admin.shopify.com/store/barreletics/themes/187144929571/editor
- Show plan before saving for layout/spacing work. No reverts. Precision.
- Don't message Andrew unless he messaged first or it's a true blocker. Never send external messages unasked.
- Secret: process.env.SHOPIFY_CLI_THEME_TOKEN on the box. Never print it. Forwarding secrets to cloud agents is disabled for this account.
- Ignore the stray code Andrew pasted (t150u); told him to change it if it was a password.

## Andrew style
Very short replies, low tokens, bottom line only when frustrated. Say "on the draft", never "live" for draft. Capture every point he gives.
Copy rules: Pilates/barre first, TRX/yoga as extras; keep "360° grip system" + "Classical Pilates"; "ships fast" (not standard/express); no grand claims, never "peel"/"flake"/"engineered for hot yoga"; link size guide /pages/performance-skins-size-chart instead of listing sizes; keep city keywords in FAQ titles (GEO/SEO); Nike/Lulu/Alo voice. Apply approved copy SITEWIDE with per-page wording variation; flag duplicates.

## Locks (do not regress)
- Phone spacing sliders: sections 40 / inner 24 / page intro 56. 50/50 mobile text pads 96/96. Cream #faf8f6. Global image sizing + breathing room = top priority.
- PDP phone buy box: trust strip + h1 above gallery at ≤768px (sections/pdp-buy-box.liquid, class pdp-hero--m-title-top, setting mobile_title_above_gallery default true). Andrew loved it. Locked.
- Open Sole (templates/product.in-studio-template.json): Barefoot feel fifty-fifty-lifestyle mobile_media_height 550, image P5A4949, center, image_mobile removed; text_pad_y_mobile 96 on sock-era/commit/tired-socks/numbers/lifestyle; buy-box pad 32; sock-era show_trust_strip true; fullbleed-statement image_fit_mobile cover; keep new controls focal_x/y_mobile + image_position_mobile and the "Footwear that outperforms…" subhead. Short FAQ answers restored (fit block removed; short returns answer). Skill barreletics-chair-pose-yellow still says 360 for Barefoot feel — outdated; 550 is approved.

## Done + verified today (all on draft)
- FAQ links underlined; studio_faq_14_q = "Do you ship Pilates grip shoes to London, Melbourne, and worldwide?"
- Open Sole stale-save restore (above) + short FAQ versions.
- All size charts (page.size-chart.json [the one /pages/performance-skins-size-chart uses], page.performance-skins-size-chart.json, page.size-guide.json): Kids M "2–5 (Women's 4–5)"; "How to place them": "Position the front edge where your toes meet the ball of your foot. Gently tug the top edge at the ankle to seat them correctly."
- Buy box kids label "Kids 2 to 5 · Women 4 to 5" (kids still hidden).
- Sitewide FAQ alignment: collection.json, page.best-grippy-socks.json, page.faq.json (removed fit-1/returns-2/warranty-1), page.grip-comparison.json (unattached), product.outdoor.json.
- PDP phone title-above-gallery (above).

## IN FLIGHT — pick up
- Open Sole phone text padding (Andrew approved "Open Sole only" ~12:28 PM). Executor sand-subagent-1c8c1fec-f08a-d4d1-8ff5-0fc98825ebca is pushing: new slider Theme settings > Layout > Spacing (phones) > "Text block padding (phones)" (id text_pad_mobile, default 96); theme.liquid outputs --text-pad-mobile only when template.suffix == 'in-studio-template'; fifty-fifty/statement-band/problem-section/pdp-sock-math phone rules use var(--text-pad-mobile, <current value>) so other pages don't move; Open Sole pdpcopy-description bg_preset custom → white (fixes Engineered blending with cream). Verify Open Sole all 96/96 at 390 + no regression on Home/Closed Sole/collection. Screens: /workspace/opensole-text-pad-push-20261007/. Audit: /workspace/opensole-text-audit-20261007/. When done: send Andrew the Open Sole preview link to check on phone: https://barreletics.myshopify.com/products/studio-performance-skin-footwear?preview_theme_id=187144929571 . Going sitewide later = delete that one `if` in theme.liquid (Andrew wants them all to match eventually; ask first).

## Open items
- Unanswered offer to Andrew: fix remaining FAQ flags the same way (page.faq price-1 "class 1,000", shipping-1/2 "Expedited"/"overnight", fit-3/fit-6 size numbers, fit-5 "Medium"; f8 "Yoga flows" on Shop All + best-grippy puts yoga level with barre/Pilates; verbatim duplicate answers across pages; grip-comparison "peel, flake… 6-8 weeks"; "Trusted by 1,000s" banners; outdoor "Standard… express"). Don't act unless he says yes.
- "Barefoot feel image swap" question: per Grok Bot it's pending with Andrew; I have no newer decision — 550 + P5A4949 is current.

## Cursor cloud agent bc-a21d31fa-85b3-4260-b80b-66869490e776
https://cursor.com/agents/bc-a21d31fa-85b3-4260-b80b-66869490e776 — Website bot owns coordination. It CANNOT push: SHOPIFY_CLI_THEME_TOKEN isn't injected (Cursor My Secrets entry is scoped "barreletics-design-review & 11 others"; All Repositories wouldn't save; run #18 still unset). So the Website bot pushes everything from the Mac. Andrew may move Cursor back to the Mac. Sent so far: refresh-5 handoff, CURSOR-WEBSITE-BRIEF.md, website-earmarks.md, website-guardrails/*.md (no-revert guard, lock scan, no-drift push gate); repo /workspace/hrepo = github.com/barreletics/Barreletics-Design-Review (design history). Its queued tasks (FAQ retitle, Open Sole restore) were done by me instead.

## Routines / groups
None owned by this bot.
