/**
 * Checkout-safety regression: merged fresh baseline vs pre-patch baseline.
 * Does not prove live Shopify draft behavior — static DOM/JS contract only.
 */
const assert = require('assert');
const { test } = require('node:test');
const fs = require('fs');
const path = require('path');

const BASELINE = process.env.CART_BASELINE_ROOT || '/tmp/fresh-draft';
const MERGED = process.env.CART_MERGED_ROOT || '/tmp/merge-out';

function read(rel) {
  return fs.readFileSync(path.join(MERGED, rel), 'utf8');
}

function readBaseline(rel) {
  return fs.readFileSync(path.join(BASELINE, rel), 'utf8');
}

function extractCartDrawerFooter(liquid) {
  const m = liquid.match(
    /<footer class="cart-drawer__footer"[\s\S]*?<\/footer>/
  );
  assert.ok(m, 'cart-drawer footer block missing');
  return m[0];
}

function extractMainCartSummary(liquid) {
  const m = liquid.match(
    /<aside class="main-cart__summary">[\s\S]*?<\/aside>/
  );
  assert.ok(m, 'main-cart summary block missing');
  return m[0];
}

test('cart-drawer checkout footer unchanged vs fresh baseline', () => {
  const b = extractCartDrawerFooter(readBaseline('snippets/cart-drawer.liquid'));
  const m = extractCartDrawerFooter(read('snippets/cart-drawer.liquid'));
  assert.equal(m, b);
});

test('main-cart checkout summary unchanged vs fresh baseline', () => {
  const b = extractMainCartSummary(readBaseline('sections/main-cart.liquid'));
  const m = extractMainCartSummary(read('sections/main-cart.liquid'));
  assert.equal(m, b);
});

test('no footer estimated-total or checkout interception hooks in merged theme files', () => {
  const files = [
    'snippets/cart-drawer.liquid',
    'sections/main-cart.liquid',
    'assets/cart.js',
    'assets/cart-bundle-promo.js'
  ];
  const forbidden = [
    'cart-drawer-estimated-row',
    'cart-estimated-total',
    'cart-page-estimated-row',
    'toggleEstimatedFooter',
    'formatMoneyExact',
    'is-bundle-active',
    'cart-ship-preview-line',
    '/discount',
    '/checkout?'
  ];
  files.forEach((rel) => {
    const text = read(rel);
    forbidden.forEach((needle) => {
      assert.ok(
        !text.includes(needle),
        rel + ' must not contain ' + needle
      );
    });
  });
});

test('merged cart.js keeps baseline checkout-critical handler patterns', () => {
  const base = readBaseline('assets/cart.js');
  const merged = read('assets/cart.js');
  const mustKeep = [
    'form[action*="/cart/add"]',
    'change.js',
    'cart/add.js',
    'fetchCart',
    'updateShippingBar',
    'shipping-save2-note',
    'data-qty-change',
    'data-remove-item'
  ];
  mustKeep.forEach((needle) => {
    assert.ok(base.includes(needle), 'baseline missing ' + needle);
    assert.ok(merged.includes(needle), 'merged missing ' + needle);
  });
  assert.match(merged, /updateBundlePromo/);
  assert.match(merged, /cart-bundle-promo-mount/);
  assert.ok(!merged.includes('toggleEstimatedFooter'));
});

test('cart.js does not attach listeners to checkout links', () => {
  const merged = read('assets/cart.js');
  assert.ok(!merged.includes('cart-drawer__checkout'));
  assert.ok(!merged.includes('main-cart__checkout'));
  assert.ok(!merged.includes('[href="/checkout"]'));
});

test('bundle preview is isolated region with disclaimer', () => {
  const js = read('assets/cart-bundle-promo.js');
  assert.ok(js.includes('not checkout pricing'));
  assert.ok(js.includes('previewDisclaimer'));
  assert.ok(!js.includes('cart-bundle-promo__earned'));
  assert.ok(!js.includes('Complimentary US shipping over'));
});

test('theme script order: bundle assets gated; cart.js defer preserved', () => {
  const theme = read('layout/theme.liquid');
  const cartIdx = theme.indexOf("{{ 'cart.js' | asset_url }}");
  const chromeIdx = theme.indexOf("{{ 'chrome.js' | asset_url }}");
  assert.ok(cartIdx > -1 && chromeIdx > cartIdx);
  if (theme.includes('cart-bundle-promo.js')) {
    const bundleIdx = theme.indexOf('cart-bundle-promo.js');
    assert.ok(bundleIdx < cartIdx, 'bundle promo must load before cart.js');
    assert.ok(theme.includes('cart_bundle_promo_enabled'));
  }
});
