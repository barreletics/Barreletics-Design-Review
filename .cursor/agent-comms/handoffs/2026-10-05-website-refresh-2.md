# Website bot refresh handoff #2 (2026-10-05, ~10:15 PM ET)
Old bot: Website 7ca22a9b-c17f-43cd-96f2-4e5cb0169533 (keep visible until Grok Bot says). Name "Website", no title. Description: see old profile (draft storefront tester + theme spacing/layout work).
Section/routines/group chats: no routines on this bot; no group chats known; sidebar section same as old bot.

## Standing rules
- Draft theme 187144929571 ONLY. Never touch live 185687998755; never publish unless Andrew says "publish".
- Push via Shopify CLI on Andrew's Mac (machineId b9c0e142-7e3d-4710-856d-c6a9caf6d9cf, --store barreletics.myshopify.com): temp dir, pull, backup, minimal edit, push --only <file> --nodelete, pull-verify. No templates/*.json unless Andrew names it.
- Design-Review repo main is BEHIND the draft (PR #43 Shared-frame unmerged; press gap + spacing pass pushed directly). Never push a branch built off main as-is. PR #44 (press) is stale; PRs #45-47 are report-only audits.
- Test-order guardrails (shared memory): never delete/archive/fulfill/send to eFS; only touch orders the bot just placed; tag TEST ORDER, cancel, refund to gift card 671805505827, restock, no customer notice. Shop Pay/Apple Pay checks not needed.
- Andrew: plain words, no jargon, mocks before new sections, mobile first, white over cream (no new cream), don't touch 50/50s / press layout / Our Story values / Instagram grid. Lean tokens.

## Done today
- Press-row gap 10->24px (draft, approved).
- Sitewide phone spacing pass (13 files, pull-verified). Sliders: Theme settings > Layout > "Spacing (phones)" defaults 40/24/56. Backup + rollback: Mac /Users/andrewnehra/tmp-spacing-pass-20261005-215935/. Mocks/screens: /workspace/mocks/spacing-pass-2026-10-05/.

## Open / waiting on Andrew
- His phone check of the spacing pass (preview https://barreletics.com/?preview_theme_id=187144929571). Small side effects he may want undone: grid spacing now on product pages too; Shop All mosaic +12px; "Built for the work" spacing on tops/pants PDPs.
- Optional: FAQ cream background -> white (not done); ~18px cream strip above some 50/50 media; origin-statement Shared-frame pass; Open Sole swatch "Rivian Green" vs coral image; Size Guide "FIT GUIDE" eyebrow left-aligned vs centered title.
- Go-live: optional real-phone checkout sanity check; check live pages after publish.
