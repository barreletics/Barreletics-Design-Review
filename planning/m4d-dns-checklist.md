# M4D — DNS Checklist

**Domain:** barreletics.com  
**Purpose:** Verify DNS configuration is correct before and after theme launch. A Shopify theme change does NOT require DNS changes, but verification ensures nothing is misconfigured.

---

## Important Context

A Shopify theme publish **does not** modify DNS records. This checklist exists to:
1. Document the current DNS state as a pre-launch baseline
2. Verify that SSL, email, and CDN remain functional after publish
3. Provide a reference if any connectivity issues arise post-launch

---

## Pre-Launch DNS Snapshot

Capture and record the current state before any changes.

### A / CNAME Records

- [ ] Document current A record(s) for `barreletics.com`
  - Expected: Shopify IP (`23.227.38.65`) or CNAME to `shops.myshopify.com`
- [ ] Document current CNAME for `www.barreletics.com`
  - Expected: `shops.myshopify.com`
- [ ] Screenshot DNS configuration from registrar dashboard
- [ ] Record DNS provider/registrar: `________________`

### SSL Certificate

- [ ] Verify SSL certificate is active for `barreletics.com`
  - Check: `https://barreletics.com` — padlock icon in browser
- [ ] Verify SSL for `www.barreletics.com`
- [ ] Note certificate issuer (Shopify uses Let's Encrypt auto-renewal)
- [ ] Certificate expiration date: `________________`

### Email DNS Records

Theme changes do NOT affect email, but verify these are intact:

- [ ] MX records documented
  - Current MX: `________________`
- [ ] SPF record present (TXT record)
  - Current SPF: `________________`
- [ ] DKIM record present (if configured)
  - Current DKIM: `________________`
- [ ] DMARC record present (if configured)
  - Current DMARC: `________________`

### CDN Configuration

- [ ] Shopify CDN handles all asset delivery automatically — no configuration needed
- [ ] Verify assets load from `cdn.shopify.com` (check any image URL in DevTools → Network tab)
- [ ] No third-party CDN configured (confirm)

### Subdomains

- [ ] Document any active subdomains:
  - `www.barreletics.com` → `________________`
  - Other: `________________`
- [ ] Verify no subdomains point to deprecated services

---

## Post-Launch DNS Verification

Run these checks within 1 hour of theme publish:

- [ ] `barreletics.com` resolves correctly (loads the site)
- [ ] `www.barreletics.com` resolves correctly (redirects or loads)
- [ ] SSL certificate still valid (padlock icon, no warnings)
- [ ] Email sending/receiving still works (send a test email)
- [ ] Assets loading from Shopify CDN (check Network tab)
- [ ] No mixed content warnings (HTTP resources on HTTPS page)

### Quick DNS Check Commands

```bash
# Verify A record
dig barreletics.com A +short

# Verify CNAME
dig www.barreletics.com CNAME +short

# Verify MX records
dig barreletics.com MX +short

# Verify SPF
dig barreletics.com TXT +short

# Check SSL certificate
echo | openssl s_client -servername barreletics.com -connect barreletics.com:443 2>/dev/null | openssl x509 -noout -dates
```

---

## If DNS Issues Arise

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Site not loading after publish | Unrelated to theme — check Shopify status page | Wait / contact Shopify support |
| SSL warning in browser | Certificate renewal issue | Shopify admin → Domains → check SSL status |
| Email stopped working | MX records accidentally modified | Restore MX records at registrar |
| Mixed content warnings | Theme references HTTP assets | Fix asset URLs in theme code (use `//` or `https://`) |
| CDN assets not loading | Shopify CDN issue (rare) | Check Shopify status page; assets self-heal |
