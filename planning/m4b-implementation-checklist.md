# M4B Implementation Checklist

---
document: M4B Implementation Checklist
status: 🟡 In Progress
created: 2026-07-18
depends_on: [m4b-integration-plan.md, MILESTONES-4-5-6-ROADMAP §M4B]
---

## Builder-Independent Work (No Credentials Required)

### Analytics & Tracking Snippets
- [x] `snippets/analytics-head.liquid` — GA4 gtag.js container (Property 300437005)
- [x] `snippets/analytics-events.liquid` — Enhanced ecommerce event layer
- [x] `snippets/meta-pixel.liquid` — Meta Pixel base + standard events + dedup
- [x] `snippets/pinterest-tag.liquid` — Pinterest base tag + events
- [x] `snippets/clarity.liquid` — Microsoft Clarity script
- [x] Include all snippets in `layout/theme.liquid`

### Judge.me Theme Hooks
- [x] Verify `sections/pdp-reviews.liquid` metafield references
- [x] Verify `snippets/review-card.liquid` metafield references
- [x] Document Judge.me JavaScript widget hooks needed
- [ ] Verify structured data pulls Judge.me metafield values

### Support Documentation
- [x] `planning/m4b-helpscout-alignment.md` — Saved reply mapping
- [x] `planning/m4b-tidio-knowledge-base.md` — Q&A pairs for AI training

### Search & Merchant
- [ ] Verify sitemap generation (Shopify auto `/sitemap.xml`)
- [ ] Verify canonical tags in `theme.liquid`
- [ ] Document GSC setup steps
- [ ] Document GMC setup steps

### Contact Form Verification
- [ ] `page-contact.liquid` form routes to correct endpoint
- [ ] `page-partners.liquid` form routes to correct endpoint

---

## Owner-Dependent Work (Requires Credentials)

### Judge.me
- [ ] Confirm metafield sync active
- [ ] Disable default widget rendering
- [ ] Verify review data populates

### GA4
- [ ] Confirm data stream ID
- [ ] Verify events in GA4 Realtime
- [ ] Mark conversion events

### Meta Pixel + CAPI
- [ ] Provide Pixel ID (replace placeholder)
- [ ] Configure CAPI via Shopify Meta channel
- [ ] Verify in Events Manager

### Pinterest
- [ ] Provide Tag ID (replace placeholder)
- [ ] Verify events in Pinterest dashboard

### Microsoft Clarity
- [ ] Provide Project ID (replace placeholder)
- [ ] Verify recordings appear

### Help Scout
- [ ] Configure email forwarding
- [ ] Create saved replies from alignment doc
- [ ] Install Beacon widget (if applicable)

### Tidio
- [ ] Import knowledge base from training doc
- [ ] Configure conversation flows
- [ ] Set handoff rules
- [ ] Style widget to brand

### Google Search Console
- [ ] Verify domain ownership
- [ ] Submit sitemap
- [ ] Record index baseline

### Google Merchant Center
- [ ] Confirm account and product sync
- [ ] Verify no disapprovals

---

## Blockers Log

See `planning/m4b-blockers.md` for any blockers encountered during implementation.
