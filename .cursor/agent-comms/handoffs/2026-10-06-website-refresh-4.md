# Website bot refresh #4 — 2026-10-06 2:35 PM ET (old bot 182eed19)
Rules: everything in 2026-10-06-website-refresh-3.md and 2026-10-05-website-refresh-2.md still applies. Draft 187144929571 ONLY; never touch, mention or publish live 185687998755. Push via Shopify CLI on Andrew's Mac b9c0e142: fresh pull, back up, minimal diff, push --only <file> --nodelete, md5 pull-verify, render at 390 and 1440. NEVER push from repo main or PR branches (behind the draft; commit 2345c7e reverted fixes on 10-05). Don't overwrite Andrew's editor work: push section code only unless he says otherwise. Don't touch the Description accordion copy. Short, plain replies; low-effort workers for routine pushes; don't rescan or re-audit.

Done today (verified):
- PDP restore + copy (Redefine movement 50/50s, second-skin trims, "The sock cycle"), FAQ sweep, size-chart Large range.
- Theme Editor live preview restored in 15 PDP sections; independent check PASS 1:23 PM. md5 manifests are in Mac /Users/andrewnehra/tmp-live-preview-fix-20261006-120443/r4, r5, r6. Rule: {% style %} reads section.settings.* directly, checks inside the block, no outer emit gates.
- pdp-sock-math has a "Custom phone padding" toggle (off by default). fifty-fifty phone "space after section" and phone media width now work on PDPs (r6, md5 d39afe8e).
- Swatch hiding: metafield custom.hide_from_storefront OR (setting "Hide sold-out colors" + all non-Kids sizes sold out). Outdoor excluded via setting "Never auto-hide on (product handles)". Closed 8, Open 8, Outdoor 7. Rollback: Mac /Users/andrewnehra/tmp-swatch-push-20261006-141331/.
- Told the site bots and Grok Bot aa3b203e about the no-push-from-main rule and the live-preview fix details.

Open / waiting on Andrew:
- He's hand-checking editor controls now. Known quirk: in variant-grid, pdp-reviews, disciplines and guarantee-band, the phone padding slider shows a lower saved value (24/24/48/24) than renders (40/40/64/48, the sitewide minimum), so nothing moves until he passes it.
- Fit tips block for the 3 size-chart templates: ON HOLD until he confirms; also Dark Grey vs Subterranean. Draft text is in the refresh-3 summary.
- Outdoor auto-hide (would drop to 4 swatches): he hasn't decided.
- Next: Andrew's site copy read-through; batch his edits.
- Publish-day Admin items are listed in refresh-3.
No routines.
