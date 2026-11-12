#!/usr/bin/env node
/**
 * Local proof for cart-offer-previews (run before Pages deploy).
 * Blocks non-allowlisted hosts; pants image uses public CDN once per page.
 */
import { chromium, devices } from 'playwright';
import { createServer } from 'http';
import { readFileSync, existsSync, mkdirSync } from 'fs';
import { join, extname } from 'path';
import { fileURLToPath } from 'url';
import assert from 'node:assert/strict';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const ROOT = join(__dirname, '..');
const OUT = '/opt/cursor/artifacts/cart-offer-previews-proof';
mkdirSync(OUT, { recursive: true });

const MIME = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.css': 'text/css'
};

function serveFile(urlPath, res) {
  const safe = urlPath === '/' ? '/index.html' : urlPath;
  const file = join(ROOT, safe.replace(/^\//, ''));
  if (!file.startsWith(ROOT) || !existsSync(file)) {
    res.writeHead(404);
    res.end('not found');
    return;
  }
  res.writeHead(200, { 'Content-Type': MIME[extname(file)] || 'text/plain' });
  res.end(readFileSync(file));
}

const server = createServer((req, res) => serveFile(req.url.split('?')[0], res));
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const port = server.address().port;
const base = `http://127.0.0.1:${port}`;

const pages = [
  { slug: '01-minimal-line-item', file: '01-minimal-line-item.html' },
  { slug: '02-soft-card', file: '02-soft-card.html' },
  { slug: '03-editorial', file: '03-editorial.html' }
];

const forbiddenHosts = [];
let browser = await chromium.launch();
const log = [];

async function addSecondPair(page, colorLabel, sole) {
  await page.click(`[data-sole="${sole}"]`);
  await page.waitForSelector('[data-color]');
  await page.selectOption('[data-color]', { label: colorLabel });
  await page.waitForSelector('[data-size]:not([disabled])');
  await page.selectOption('[data-size]', { label: 'M (W 5.5-7.5)' });
  await page.waitForFunction(() => {
    const btn = document.querySelector('[data-add-pair]');
    return btn && !btn.disabled;
  });
  await page.click('[data-add-pair]');
  await page.waitForFunction(() => document.querySelectorAll('.cart-line').length >= 2);
}

async function runFlow(page, slug, viewport) {
  const blocked = [];
  await page.route('**/*', (route) => {
    const url = route.request().url();
    if (url.startsWith(base)) return route.continue();
    if (url.includes('cdn.shopify.com/s/files/')) return route.continue();
    blocked.push(url);
    return route.abort();
  });
  await page.setViewportSize(viewport);
  await page.goto(`${base}/${pages.find((p) => p.slug === slug).file}`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: join(OUT, `${slug}-${viewport.width}x${viewport.height}-initial.png`) });

  await addSecondPair(page, 'Purple', 'closed');
  await page.waitForSelector('[data-add-pants], .offer__qual', { timeout: 8000 });
  assert.equal(await page.locator('.cart-line').count(), 2, 'expected two line items');
  await page.screenshot({ path: join(OUT, `${slug}-${viewport.width}x${viewport.height}-same-color-two-pairs.png`) });

  await page.click('[data-remove-pair]');
  await page.waitForTimeout(250);
  await addSecondPair(page, 'Black', 'open');
  await page.screenshot({ path: join(OUT, `${slug}-${viewport.width}x${viewport.height}-diff-color-two-pairs.png`) });

  await page.click('[data-remove-pair]');
  await page.waitForTimeout(200);
  await page.screenshot({ path: join(OUT, `${slug}-${viewport.width}x${viewport.height}-reset.png`) });

  if (blocked.some((u) => !u.includes('cdn.shopify.com'))) {
  }
  const nonCdn = blocked.filter((u) => !u.includes('cdn.shopify.com'));
  log.push({ slug, viewport: `${viewport.width}x${viewport.height}`, blockedCount: blocked.length, forbidden: nonCdn });
}

for (const p of pages) {
  for (const viewport of [{ width: 390, height: 844 }, { width: 1280, height: 800 }]) {
    const ctx = await browser.newContext({ ...devices['Desktop Chrome'], viewport });
    const page = await ctx.newPage();
    await runFlow(page, p.slug, viewport);
    await ctx.close();
  }
}
await browser.close();
server.close();

const summary = {
  baseUrl: base,
  artifactsDir: OUT,
  runs: log,
  pass: log.every((r) => r.forbidden.length === 0)
};
import { writeFileSync } from 'fs';
writeFileSync(join(OUT, 'proof-log.json'), JSON.stringify(summary, null, 2));
console.log(JSON.stringify(summary, null, 2));
process.exit(summary.pass ? 0 : 1);
