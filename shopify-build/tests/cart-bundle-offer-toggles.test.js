'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

var LIVE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var VARIANT = { offerArm: 'variant' };

function closedSkin(qty, color) {
  return {
    quantity: qty,
    final_line_price: 7400 * qty,
    product_title: 'Closed Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: (color || 'Purple') + ' · M (W 5.5-7.5)',
    url: '/products/best-reformer-pilates-legree-workout-shoes'
  };
}

function cfg(overrides) {
  return bundle.mergeConfig(Object.assign({ enabled: true }, overrides || {}));
}

test('toggle matrix: both ON at 1 pair shows add-pair only (variant)', function () {
  var c = cfg({ addPairOfferEnabled: true, pantsOfferEnabled: true });
  var r = bundle.computeBundlePromo([closedSkin(1)], c, 7400, VARIANT);
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, false);
  assert.equal(r.showPanel, true);
});

test('toggle matrix: add OFF, pants ON at 1 pair hides panel (variant)', function () {
  var c = cfg({ addPairOfferEnabled: false, pantsOfferEnabled: true });
  var r = bundle.computeBundlePromo([closedSkin(1)], c, 7400, VARIANT);
  assert.equal(r.showAddPairStage, false);
  assert.equal(r.showPantsOffer, false);
  assert.equal(r.showPanel, false);
});

test('toggle matrix: add ON, pants OFF at 2 pairs shows add-pair only', function () {
  var c = cfg({ addPairOfferEnabled: true, pantsOfferEnabled: false });
  var r = bundle.computeBundlePromo([closedSkin(2)], c, 14800, VARIANT);
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, false);
  assert.equal(r.showPanel, true);
});

test('toggle matrix: both ON at 2 pairs shows add-pair and pants', function () {
  var c = cfg({ addPairOfferEnabled: true, pantsOfferEnabled: true });
  var r = bundle.computeBundlePromo([closedSkin(2)], c, 14800, VARIANT);
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, true);
  assert.equal(r.showPanel, true);
});

test('toggle matrix: add OFF, pants ON at 2 pairs shows pants only', function () {
  var c = cfg({ addPairOfferEnabled: false, pantsOfferEnabled: true });
  var r = bundle.computeBundlePromo([closedSkin(2)], c, 14800, VARIANT);
  assert.equal(r.showAddPairStage, false);
  assert.equal(r.showPantsOffer, true);
  assert.equal(r.showPanel, true);
});

test('toggle matrix: both OFF at 2 pairs leaves panel hidden (variant)', function () {
  var c = cfg({ addPairOfferEnabled: false, pantsOfferEnabled: false });
  var r = bundle.computeBundlePromo([closedSkin(2)], c, 14800, VARIANT);
  assert.equal(r.showPanel, false);
  var html = bundle.renderPromoHtml(r);
  assert.equal(html, '');
});

test('2→1 removal: pants stage hides when back to 1 pair with both ON', function () {
  var c = cfg({ addPairOfferEnabled: true, pantsOfferEnabled: true });
  var two = bundle.computeBundlePromo([closedSkin(2)], c, 14800, VARIANT);
  assert.equal(two.showPantsOffer, true);
  var one = bundle.computeBundlePromo([closedSkin(1)], c, 7400, VARIANT);
  assert.equal(one.showPantsOffer, false);
  assert.equal(one.showAddPairStage, true);
});

test('explicit false in mergeConfig is honored (not coerced)', function () {
  var c = bundle.mergeConfig({ enabled: true, pantsOfferEnabled: false, addPairOfferEnabled: false });
  assert.equal(c.pantsOfferEnabled, false);
  assert.equal(c.addPairOfferEnabled, false);
});

test('control arm: pants OFF hides pants block at 2 pairs', function () {
  var item = {
    quantity: 2,
    final_line_price: 14800,
    product_title: 'Performance Skins — Closed Sole',
    url: '/products/studio-performance-skin-closed-sole',
    variant_title: 'Purple · M'
  };
  var c = cfg({ pantsOfferEnabled: false });
  var r = bundle.computeBundlePromo([item], c, 14800, { offerArm: 'control' });
  assert.equal(r.showPantsOffer, false);
});
