# Barreletics Journal gift guides 2026: index and plan

Drafted Fri Oct 23, 2026 (America/Detroit). Draft only. Nothing was published, sent, posted or changed on Shopify or the theme. Shopify access was read only (products, collections, prices, stock).

## 1. The three guides

| # | Title | Slug | URL after publish | Body words (incl. FAQ) | SEO title | Meta |
|---|---|---|---|---|---|---|
| 1 | Gifts for Pilates Lovers: 7 Ideas They Will Actually Use (flagship) | `gifts-for-pilates-lovers` | https://barreletics.com/blogs/news/gifts-for-pilates-lovers | 1,197 | Gifts for Pilates Lovers: 7 Useful Ideas (40) | 153 chars |
| 2 | Gifts for Barre and Yoga People: 9 Ideas That Get Used | `gifts-for-barre-and-yoga-people` | https://barreletics.com/blogs/news/gifts-for-barre-and-yoga-people | 1,092 | Gifts for Barre and Yoga People: 9 Ideas (40) | 142 chars |
| 3 | Stocking Stuffers and Secret Santa Gifts Under $50 | `stocking-stuffers-and-secret-santa-gifts-under-50` | https://barreletics.com/blogs/news/stocking-stuffers-and-secret-santa-gifts-under-50 | 999 | Stocking Stuffers and Secret Santa Under $50 (44) | 150 chars |

Files: `01-gifts-for-pilates-lovers.md`, `02-gifts-for-barre-and-yoga-people.md`, `03-stocking-stuffers-and-secret-santa-gifts-under-50.md`. Each file has: Shopify fields, outline, body HTML, FAQ and ItemList JSON-LD, internal link plan, pitch paragraph, image brief with alt text, facts to confirm, QA checks.

Publish all three together. They link to each other, and two of those links return 404 until the others exist.

## 2. What the Blog bot should do (after Stefanie clears section 6)

1. Create each as an inactive article in blog `news` with the body HTML, SEO title and description (`global.title_tag`, `global.description_tag`), excerpt, tags, handle and the featured image with alt text. Use the Mac CLI route from the 2026-10-06 handoff.
2. Check the live preview at 390 and 1440 wide: title fits two lines, dek and lead styles show, no stray styles.
3. Andrew flips them live (Cloudflare often blocks bot publishing).
4. After live: view source for one BlogPosting block (theme) plus the FAQPage and ItemList blocks, with no duplicate Article block.

## 3. Product and price facts used (Shopify Admin API, Oct 23, 2026)

* Closed Sole `best-reformer-pilates-legree-workout-shoes`: $74, limited colors Turquoise and Purple $78.
* Open Sole `studio-performance-skin-footwear`: $74.
* Performance Fabric T Shirt or Tank Top `barreletics-performance-fabric-yoga-t-shirts`: V neck $39, tank $34.
* Super High Rise Reinforced Knee Yoga Tight `lightly-padded-knee-yoga-pant-black`: $89.
* Collections used: `/collections/barre-pilates-yoga-shoe-sock-footwear` (Grip Shoes), `/collections/apparel`, `/collections/all`. Pages used: `/pages/performance-skins-size-chart`, `/pages/yoga-pants-t-shirt-size-guide`, `/pages/compare-open-closed-sole`, `/blogs/news`. All returned 200.
* Not used: Coperni Closed Sole ($115, Medium sold out), Outdoor water shoes (house rule: no water claims, and its inventory shows negative numbers), test and sample items.
* The store has no gift card product, so no guide recommends a Barreletics gift card.
* The store sells almost nothing under $50 except the tee and tank, so guide 3 is honest about that and adds a group gift idea. Non Barreletics ideas have no brand names and no prices on purpose.

## 4. Keyword targets (verified by WebSearch on Oct 23, 2026, no volumes)

I did not find or invent search volumes. The phrases below are ones I saw used in page titles or headings of results for those searches. After two weeks, add real impressions and clicks from Search Console.

| Guide | Primary | Secondary (seen in results) |
|---|---|---|
| 1 | gifts for Pilates lovers | Pilates gifts, Pilates gift ideas, gift ideas for Pilates lovers, Pilates Christmas gifts |
| 2 | gifts for barre and yoga | gifts for yoga lovers, barre gift guide, yoga Pilates and barre gift guide, barre socks gift guide, Pilates and barre gifts |
| 3 | Pilates stocking stuffers | Pilates Secret Santa gift, Pilates gifts under $50, stocking stuffers for Pilates lovers |

Honest read on competition: pages dated Oct 2026 already rank for these phrases (for example Pilates Verdict, Oct 6, 2026, and Pilates Collective Club's stocking stuffer list, prices checked Oct 14, 2026). Head terms are crowded. Long tail pages, social and email will likely carry more traffic than organic search in the first weeks. Do not promise a ranking.

## 5. Schema

* Article: the theme already prints BlogPosting JSON-LD with author, dates, image and mainEntityOfPage. Do not add a second one. Confirm the author name (live posts show Stefanie Miller).
* ItemList and FAQPage: ready in each file, matching visible text. Search check (Oct 23, 2026): Google stopped showing FAQ rich results on May 7, 2026 and removed the docs in June 2026. Google's carousel markup does not apply to article lists. Keep the markup because it is valid and harmless, keep the visible FAQ because readers use it, and expect no rich result. Skip them if adding them needs a theme change; they are not worth a push.

## 6. Facts for Stefanie to confirm (master list)

Left out of every guide because unconfirmed:
1. "Made in USA" (site says it; the Oct 23 press playbook flags USA versus Detroit).
2. Materials and fabric claims: "Under Armour Fabric", moisture wicking, no pilling, "Italian" stretch on the tights.
3. Counts: "thousands" or "1,000+" instructors and studios, "1,000+ classes on one pair".
4. Retail launch dates and partners (Anthropologie, Free People, Coperni) and any award or Biennale claim.
5. Warranty wording and the water or pool use of the Outdoor shoe.

Used in the guides, so please confirm:
6. Founder line: "designed it after she could not get a grip during barre practice" and "built the grip into the sole instead of adding dots" (from the product page copy). Also whether she wants to be the named author.
7. Closed Sole and Open Sole "same grip, same stability" (product pages) and "yoga on or off the mat".
8. Shipping and returns: free over $150, $9.95 flat under $150 in the continental US, 30 day returns (clean, like new, indoor try on), free size exchanges within 30 days of delivery, apparel returns unworn, unwashed with tags. Guide 3's $43.95 and $48.95 totals depend on the $9.95.
9. Tights: "reinforced knees for kneeling and floor work" and "suggests sizing down". The admin has compare at $129, the shop shows $89; guides state $89 only.
10. Naming: guides say "grip shoes" and "Performance Skin" (matches the site and Journal). Help Scout rules say never "shoes" in customer replies. Confirm for the Journal.
11. Size conflict to fix on the site: the Closed Sole page says Large is "Women 7.5 to 11 · Men to 10.5", while the Shopify variant says "W 8-11". The guides list no sizes and link to the size chart.
12. Stock: tank sizes were low on Oct 23 (S 2, M 3, L 2, XL sold out). Check before publish and in early December.
13. Whether to mention the "Buy 2, Save 10% · Code SAVE2" banner offer or holiday shipping cutoff dates. Neither is in the guides.
14. Sample availability and a gifting policy for editors and creators (not in any pitch paragraph).

## 7. Where to link the guides (after publish)

Owners: Blog bot (articles), Website bot (theme and pages; every theme edit needs Andrew's go), Andrew or Stefanie (sending and posting).

| Place | What | Owner | Note |
|---|---|---|---|
| Journal index `/blogs/news` | Appears automatically; make guide 1 the first card | Blog bot | Featured image needed for the card |
| Existing Journal posts | One line at the end of "Why Grip Socks Fall Short" linking to guide 1; link guide 2 from "7 Barre and Pilates Technique Mistakes" | Blog bot | Edits to live posts need Andrew's go |
| Homepage | One "Gift guides" text link or card | Website bot | Needs a go; home sections are locked, name the section first |
| Footer | The Learn column already has Journal. Add "Gift guides" only if Andrew wants it | Website bot | Needs a go |
| Collection pages | One line under the intro of the Grip Shoes collection (guide 1, 3) and Apparel (guides 2, 3) | Website bot | Needs a go |
| Product pages | None. Keep product pages clean | none | |
| Pinterest | Two vertical pins per guide (pin copy is in each file). Link to the guide with UTMs | Andrew | Install Pinterest for Shopify first, per the Oct 23 playbook |
| Email | One block in the next customer email: guide 1 to everyone, guide 2 to barre and yoga segments, guide 3 in early December | Andrew or Stefanie | Email tool not identified |
| Instagram and Facebook | Bio link, Stories link and one post per guide, UTM tagged, organic only | Stefanie | No TikTok |

## 8. How to submit each guide to roundups and creators (after publish, a human sends everything)

Timing, from the Oct 23 playbook: national print is closed for 2026. Digital commerce editors are mostly closed. Newsletters and affiliate roundups need 3 to 6 weeks. Niche Pilates sites, local media and creators are still open. Key dates: Black Friday Fri Nov 27, Cyber Monday Mon Nov 30, Christmas Fri Dec 25, 2026. So send in the week of Oct 29 to Nov 6.

Steps:
1. Build a list of 15 to 25 targets by hand: authors of 2025 and 2026 Pilates, barre and yoga gift lists, Pilates teacher newsletters, Detroit and Michigan "gift ideas" writers, and instructors with audiences. Examples seen in search that update their lists: Pilates Collective Club (says it will refresh prices before the holidays), Pilates Verdict, and niche Pilates sites. PilatesStyle lists admin@pilatesstyle.com for editorial (verified in the playbook). Verify every contact on its own page first.
2. Match the guide to the target. Guide 1 for Pilates lists. Guide 2 for barre and yoga lists. Guide 3 for office swap, Secret Santa and local roundups.
3. Send one short email each, from Andrew or Stefanie. Under 150 words, one guide, a plain subject, the exact list or article of theirs you read, and the link. Offer the guide as a source or to take a pick, not a link swap. Do not offer anything for a link.
4. One follow up after 5 to 7 days, only if there is something new (for example a sold out color is back). Then stop.
5. Creators and instructors: share the guide for their students. If you send a free pair, they must disclose it under FTC rules. Ask for honest use only, not a positive review. Add rel sponsored or nofollow if a link is part of a gift.
6. Track every send, reply and link in a sheet. Check unlinked mentions weekly and ask for a plain link if the guide is used without one.
7. Women's Health and other award forms are separate. The Fitness Awards deadline was today, Oct 23, 11:59 p.m. ET (see the playbook).

Draft outreach email (not sent). Personalize the first sentence by hand with the exact piece you read.

Subject: Pilates gift guide for your list: seven useful picks with real prices

Hi,

I read your Pilates gift guide and thought this one might help when you next update it. The Barreletics Journal just published Gifts for Pilates Lovers: seven picks with notes on size, budget and what to skip. One pick is our own grip shoe, and the guide says so. Prices are real: $74 for most colors, $78 for a few limited colors.

You are welcome to use it as a source or take any pick that fits. Link: https://barreletics.com/blogs/news/gifts-for-pilates-lovers

Thanks for reading,
Andrew John
Barreletics | barreletics.com

For guides 2 and 3, swap the title, the one line of what is inside and the link. Pitch paragraphs for each guide are in the article files (section 6).

## 9. Timeline

* Oct 26 to 27: Stefanie clears section 6.
* Oct 28: Blog bot creates the three drafts; Andrew checks previews.
* Oct 29: Andrew flips live; request indexing in Search Console (human); first 10 pitches.
* Oct 31 to Nov 6: pins, first email block, IG and FB posts, one follow up round.
* Nov 27 to Nov 30: IG and FB push for guide 3 and guide 1.
* Dec 1: refresh check. Prices, stock, the limited colors, any shipping dates. Update the "at the time of writing" lines if they changed.
* Next year: publish the 2027 version in June to August.
