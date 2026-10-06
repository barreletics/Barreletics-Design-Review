# Website bot refresh handoff #3 (2026-10-06, ~9:20 AM ET)
Old bot: Website c26abd74-aac4-4412-bb15-5d308182c631 (Site Design section). Name "Website", title "Website". No routines, no group chats. Previous handoff: /workspace/handoffs/2026-10-05-website-refresh-2.md (rules there still apply).

## Standing rules
- Draft theme 187144929571 ONLY. Never touch live 185687998755, never publish. NOTHING that affects live: no Admin Pages, blog, product tag/alt/description edits (Admin product.description = Founder story, never edit).
- Push via Shopify CLI on Andrew's Mac (machineId b9c0e142-7e3d-4710-856d-c6a9caf6d9cf, --store barreletics.myshopify.com): fresh temp dir, pull, backup, minimal diff, push --only <file> --nodelete, pull-verify, phone 390 DPR2 + desktop 1440 render with cache-buster. One change at a time. No rollbacks/reverts (Andrew is in go-live QC).
- Andrew: plain words, short replies, batch, few screenshots (token budget is tight: 24% used, 7 days left). Mocks before new sections. Keep both second-skin text blocks where they are. Keep the 10-05 phone spacing.
- Decisions 10-06: remove all "antimicrobial"; keep "Trusted by Lagree-certified instructors"; kids sizes coming but never say "coming soon" (keep Kids' 2-5 mentions); Large range (7.5-11 vs 8-11) still undecided.

## Done 10-06 (all draft, verified)
- PDP Description accordion = buy-box setting description_accordion_body (not Admin). sections/pdp-buy-box.liquid line ~638 now lets <em> through (italics). Final copy: /workspace/copy/sole-descriptions-final-2026-10-06.md (Open v2 8:25, Closed + Coperni same text, "yoga on or off the mat").
- Templates: Open Sole = product.in-studio-template.json (studio-performance-skin-footwear); Closed = product.json (best-reformer-pilates-legree-workout-shoes); Coperni = product.coperni.json. product.open-sole.json is unused.
- FAQ page care-2 drying line -> "Wash with warm soapy water and dry in seconds."
- 50/50 restores from live (draft fifty-fifty type, live media/copy): Closed: Yoga socks are useless, Never loses shape, Built to breathe, Our Founder (hidden value-strip removed). Open: Yoga socks are useless, Our Founder. Both templates now at Shopify's 25-section cap. Backups /Users/andrewnehra/tmp-5050-restore/.
- Shop Pay banner is Shopify native and correct ($6.68/mo = 12 mo at 15% APR; 4 x $18.50). Wording only changes via Admin Shop Pay Installments settings; Andrew is asking Sidekick.
- FAQ audit: /workspace/copy/faq-audit-2026-10-06.md; proposed fixes: /workspace/copy/faq-fixes-proposed-2026-10-06.md.

## In flight at handoff (old bot will report result before hiding)
- Applying theme-only FAQ fixes + code fixes (apparel PDPs hide shoe care/warranty, keep shipping/returns; "or 4 x" card line only at $50+) on draft.

## Open / waiting on Andrew
- Admin Pages text (air dry, antimicrobial, old returns policy, Kids') is live-affecting: do only at publish time if Andrew says.
- "Redefine movement" band mock (/workspace/pdp-5050-debug/mock-think-band/) not pushed; Andrew unsure. Edits pdpcopy-think eyebrow+subhead only (no new section, fits the cap).
- Large size range decision. Unfound "antimicrobial" in a Closed Sole hidden/SEO field.
- Older backlog from handoff #2 (spacing side effects, FAQ cream->white, etc.).
- Cost: run routine, already-decided pushes and verify renders on low-effort background workers; reserve high effort for diagnosis and code changes.
- 9:41 AM: FAQ + code fix job DONE on draft (19 files pushed and verified). Backups Mac /Users/andrewnehra/tmp-faq-apply-20261006-090912/backup/, screens /workspace/copy/screens-2026-10-06/. Shopify auto-dropped unused leftover settings on collection.json, page.best-grippy-socks.json (50/50s), one-off templates, page.about.json: no visual change. Skipped: compare pages product_a_desc/product_b_desc (ask Andrew), Admin items, Large range.
