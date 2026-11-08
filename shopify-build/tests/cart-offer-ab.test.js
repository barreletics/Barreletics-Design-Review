'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');
var baseline = require('./fixtures/cart-bundle-promo-5a01277-baseline.js');

var LIVE = baseline.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var VARIANT = { offerArm: 'variant' };

function skinItem(qty, priceCents) {
  return {
    quantity: qty,
    final_line_price: priceCents * qty,
    product_title: 'Performance Skins — Closed Sole',
    product_type: 'Grippy Shoes',
    variant_title: 'Purple · M',
    url: '/products/studio-performance-skin-closed-sole'
  };
}

test('parseCartOfferArm: missing or invalid defaults control', function () {
  assert.equal(bundle.parseCartOfferArm(''), 'control');
  assert.equal(bundle.parseCartOfferArm('?foo=1'), 'control');
  assert.equal(bundle.parseCartOfferArm('?br_cart_offer=control'), 'control');
  assert.equal(bundle.parseCartOfferArm('?br_cart_offer=CONTROL'), 'control');
  assert.equal(bundle.parseCartOfferArm('?br_cart_offer=garbage'), 'control');
  assert.equal(bundle.parseCartOfferArm('?br_cart_offer=variant'), 'variant');
});

test('variant URL then absent search resets to control (same-tab, no storage)', function () {
  assert.equal(bundle.resolveOfferArm({ search: '?br_cart_offer=variant' }), 'variant');
  assert.equal(bundle.resolveOfferArm({ search: '' }), 'control');
  assert.equal(bundle.resolveOfferArm({}), 'control');
});

test('control arm matches 5a01277 compute for 1 pair', function () {
  var items = [skinItem(1, 7400)];
  var b = baseline.computeBundlePromo(items, LIVE, 7400);
  var c = bundle.computeBundlePromo(items, LIVE, 7400);
  assert.equal(c.offerArm, 'control');
  assert.equal(b.showPantsOffer, c.showPantsOffer);
  assert.equal(b.pantsQualOnly, c.pantsQualOnly);
  assert.equal(b.pantsPickerVisible, c.pantsPickerVisible);
  assert.equal(b.footwearOfferLine, c.footwearOfferLine);
  assert.equal(b.pantsQualNote, c.pantsQualNote);
});

test('control arm HTML includes pants photo at 1 pair (COPY02 parity)', function () {
  var r = bundle.computeBundlePromo([skinItem(1, 7400)], LIVE, 7400);
  var html = bundle.renderPromoHtml(r);
  assert.equal(r.offerArm, 'control');
  assert.match(html, /cart-bundle-promo__pants-img/);
  assert.ok(!html.includes('data-bundle-add-pair'));
  assert.ok(!html.includes('cart-bundle-promo--variant'));
});

test('variant arm at 1 pair: add-pair only', function () {
  var r = bundle.computeBundlePromo([skinItem(1, 7400)], LIVE, 7400, VARIANT);
  var html = bundle.renderPromoHtml(r);
  assert.equal(r.offerArm, 'variant');
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, false);
  assert.match(html, /cart-bundle-promo--variant/);
  assert.match(html, /data-bundle-add-pair/);
  assert.ok(!html.includes('cart-bundle-promo__pants-img'));
});

test('hrefWithOfferArm decorates cart links only for variant', function () {
  assert.equal(bundle.hrefWithOfferArm('/cart', 'control'), '/cart');
  var v = bundle.hrefWithOfferArm('/cart?foo=1', 'variant');
  assert.match(v, /br_cart_offer=variant/);
  assert.match(v, /foo=1/);
  assert.equal(bundle.hrefWithOfferArm('/checkout', 'variant'), '/checkout');
});

test('no session/cookie keys in bundle source', function () {
  var fs = require('fs');
  var path = require('path');
  var js = fs.readFileSync(path.join(__dirname, '../assets/cart-bundle-promo.js'), 'utf8');
  assert.ok(!js.includes('sessionStorage'));
  assert.ok(!js.includes('localStorage'));
  assert.ok(!js.includes('document.cookie'));
});
