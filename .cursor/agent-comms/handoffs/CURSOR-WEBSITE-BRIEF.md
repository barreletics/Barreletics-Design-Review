# Barreletics website: brief for the Cursor agent

You help Andrew with copy changes and small section tweaks on the Barreletics Shopify site before launch. Andrew is low on tokens, so keep replies short and make minimal edits.

## Hard rules
1. Work ONLY on the DRAFT theme **187144929571**. Never touch or publish the LIVE theme **185687998755**, and never edit Admin Pages, blog posts, or products unless Andrew says so.
2. Always start fresh: `shopify theme pull --theme 187144929571` into a clean folder first. Do NOT edit from the Barreletics-Design-Review repo `main` or any PR branch. Those are behind the draft, and pushing from them reverts live fixes.
3. Back up every file before you edit it (copy it to a `backup-<date>/` folder).
4. Change only the lines needed, then show Andrew the diff.
5. Push one file at a time: `shopify theme push --theme 187144929571 --only <file> --nodelete`
6. Verify after pushing by pulling the file back and checking the md5 matches your local copy.
7. Don't overwrite Andrew's Theme Editor work. If a JSON template changed in the editor, pull it again right before you edit it.
8. Copy style: plain, warm, short, no hype. Never use the word "gotten". Retail orders get free shipping at $150+ (the 10-item rule applies to wholesale only).

## Typical flow for a copy change
pull draft, find the text (in `templates/*.json`, `sections/*.liquid`, or `locales/en.default.json`), back it up, edit, diff, push `--only`, pull-verify, then tell Andrew the preview link so he can check it on his phone.

## When to stop and ask Andrew
- Any change to the live theme, publishing, checkout, apps, or products/prices.
- Any edit that touches more than a few files.
