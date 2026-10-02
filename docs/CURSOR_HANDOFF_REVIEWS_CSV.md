# Cursor Handoff — Barreletics Reviews CSV

## The Story

AJ found a customer reviews CSV export from Shopify that wasn't being used: **Judgem_publishedreviews_17.csv** (296 published reviews, live customer feedback on Barreletics products).

**Goal:** Build a reviews page/component that displays these reviews on the Barreletics site in a way that converts customers and showcases product trust.

**Why now:** Part of the broader Barreletics redesign — we need to surface social proof and customer testimonials where they matter (PDPs, collections, homepage).

---

## What You Have

**File:** `/mnt/project/Judgem_publishedreviews_17.csv`

**Data structure (16 columns):**
- `title` — Review headline
- `body` — Full review text
- `rating` — 1–5 stars
- `review_date` — When left
- `source` — Where posted (Shopify, third-party, etc.)
- `reviewer_name` — Customer name
- `reviewer_email` — Contact
- `product_id` — Shopify product ID
- `product_handle` — Product slug (e.g., "performance-skins")
- `reply` — AJ's response (if any)
- `reply_date` — When AJ responded
- `picture_urls` — Customer photos (if attached)
- `ip_address` — Reviewer IP
- `location` — Reviewer location
- `metaobject_handle` — Shopify metaobject link
- `curated` — Flag (likely for featured reviews)

**296 rows** of real customer feedback. Untouched.

---

## The Task

1. **Get it locally** — Copy CSV to your working directory + Git
2. **Explore** — Spot-check: data quality, missing fields, review distribution by product
3. **Design a page** — How should reviews be displayed? (Grid? Carousel? Filtered by product? Sorted by rating?)
4. **Build locally** — HTML/React component, test in browser
5. **Preview for AJ** — Share the work before any Shopify push
6. **Push to draft theme only** — Never touch live

---

## Workflow

### Step 1: Copy to Local + Git

```bash
# Copy from project
cp /mnt/project/Judgem_publishedreviews_17.csv ./data/reviews.csv

# Verify
ls -lh ./data/reviews.csv
wc -l ./data/reviews.csv  # Should be 297 (296 rows + header)

# Add to repo
git add data/reviews.csv
git commit -m "Add: Customer reviews CSV (296 reviews) from Shopify export"
git push origin main
```

---

### Step 2: Spot-Check the Data

```bash
# Check for null/empty fields
head -1 ./data/reviews.csv | tr ',' '\n' | nl  # See column headers

# Sample a few rows
head -10 ./data/reviews.csv

# Count by rating
grep -o '"[1-5]"' ./data/reviews.csv | sort | uniq -c  # Rating distribution

# Find reviews with pictures
grep 'http' ./data/reviews.csv | wc -l  # How many have picture_urls?
```

**Report back to AJ:**
- How many 5-star vs lower ratings?
- How many have customer photos?
- How many have AJ's replies?
- Any data gaps (empty cells, malformed dates)?

---

### Step 3: Design the Component

**Options (ask AJ which fits the redesign):**

A. **Hero testimonials** — 3–5 featured reviews on homepage (high-rating, short, punchy)
B. **PDP reviews section** — Show top 5 reviews per product with rating filter
C. **Carousel** — Scrollable set of testimonials with face pics
D. **Full reviews page** — All 296 with filtering by product/rating/date
E. **Trust badges** — "Trusted by 1,000+ customers" + avg rating display

---

### Step 4: Build Locally

**Create component file:**
```bash
# Example: React component that loads CSV
touch src/components/ReviewsSection.jsx

# Or static HTML
touch pages/reviews.html
```

**Load and render the CSV:**
- Parse CSV → JSON
- Sort by rating (or date, or curated flag)
- Render with product link, reviewer name, date, rating, body text
- Optional: display customer photo if available
- Optional: show AJ's reply if present

**Test locally:**
- Open in browser
- Verify reviews load
- Check responsive design (mobile/desktop)
- Click product links (should work if handles are correct)

---

### Step 5: Preview for AJ

**Two options:**

**Option A: Static HTML file**
```bash
# Save as single HTML file
# Push to repo
git add pages/reviews.html
git commit -m "Add: Reviews page component (preview)"
git push origin preview/reviews

# Send AJ the file path
# AJ opens in browser locally
```

**Option B: GitHub branch**
```bash
# Push to preview branch
git checkout -b preview/reviews
git add .
git commit -m "WIP: Reviews component + CSV integration"
git push origin preview/reviews

# AJ reviews code + rendered output on GitHub
```

**Tell AJ:**
- What you built and why
- Any design decisions you made
- What needs approval before Shopify push
- Open questions about filtering/sorting/layout

---

### Step 6: Wait for AJ Approval

⛔ **DO NOT PUSH TO SHOPIFY YET.**

AJ will review:
1. Design (does it fit Barreletics brand?)
2. Data (are all reviews displaying correctly?)
3. Performance (does it load fast?)
4. Functionality (filters working? links correct?)

AJ will comment with approval or request changes.

---

### Step 7: Push to Draft Theme (ONLY AFTER APPROVAL)

**After AJ says ✅ APPROVED:**

```bash
# Merge to main
git checkout main
git merge preview/reviews
git push origin main

# Push to draft theme ONLY
shopify theme push --theme 187144929571 \
  --only pages/reviews.html  # Or whatever your file path is
```

⚠️ **CRITICAL:**
- Never push to live theme (ID doesn't matter, never assume)
- Only push the reviews component, nothing else
- Verify in draft preview before any live publish

---

## Key Rules

✅ **Do this:**
- Work locally first
- Test in browser
- Commit to Git
- Preview for AJ
- Wait for approval
- Only push to draft theme

⛔ **Never do this:**
- Push directly to live Shopify theme
- Upload without AJ seeing it first
- Assume a code change is ready for Shopify
- Skip the preview step

---

## Files & Locations

| Item | Path |
|------|------|
| Source CSV | `/mnt/project/Judgem_publishedreviews_17.csv` |
| Local copy | `./data/reviews.csv` |
| Component | `src/components/ReviewsSection.jsx` (or `pages/reviews.html`) |
| GitHub branch | `preview/reviews` (or push to main after approval) |
| Draft theme | 187144929571 |
| Live theme | ⛔ Never touch |

---

## Questions for Cursor

Before you start building:
1. **Data scope** — Show all 296 reviews or feature a curated set?
2. **Filtering** — By product? By rating? By date range?
3. **Photo display** — Include customer images if available?
4. **Replies** — Show AJ's responses if present?
5. **Layout** — Mobile-first? Desktop-first? Both?
6. **CTA** — Does each review link to the product page?

---

## Next Steps

1. Copy CSV locally + commit to Git
2. Spot-check the data (run the checks above)
3. Report findings to AJ
4. Get design direction from AJ
5. Build component
6. Preview with AJ
7. **Wait for explicit approval before Shopify push**
8. Push to draft theme only
9. Verify in draft preview
10. Final sign-off before live

---

**Start at Step 1. Do not skip steps. Approval gates are there for a reason.**
