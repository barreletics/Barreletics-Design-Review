'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

var LIVE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var VARIANT = { offerArm: 'variant' };

function skinLine(qty, originalEach, finalEach, discountEach) {
  var line = {
    quantity: qty,
    original_line_price: originalEach * qty,
    final_line_price: finalEach * qty,
    product_title: 'Closed Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: 'Purple · M (W 5.5-7.5)',
    url: '/products/best-reformer-pilates-legree-workout-shoes'
  };
  if (discountEach) {
    line.line_level_discount_allocations = [{ amount: discountEach * qty }];
  }
  return line;
}

test('discounted cart: 2×$74 with 15% applied shows $22.20 savings (not $18.87)', function () {
  var items = [skinLine(2, 7400, 6290, 1110)];
  var r = bundle.computeBundlePromo(items, LIVE, 12580, VARIANT);
  assert.equal(r.pairSavingsCents, 2220);
  assert.equal(r.savingsLine, 'You save $22.20.');
  assert.equal(r.pairSavingsMode, 'applied');
  assert.equal(r.savingsTag, 'Applied');
  assert.equal(r.estimatedTotalCents, 12580);
});

test('preview cart: undiscounted 2×$74 shows $22.20 preview savings', function () {
  var items = [skinLine(2, 7400, 7400, 0)];
  var r = bundle.computeBundlePromo(items, LIVE, 14800, VARIANT);
  assert.equal(r.pairSavingsCents, 2220);
  assert.equal(r.pairSavingsMode, 'preview');
  assert.equal(r.savingsTag, 'Preview');
  assert.equal(r.estimatedTotalCents, 12580);
});

test('mixed: discount only on qualifying skin lines, pants ignored for pair alloc', function () {
  var items = [
    skinLine(2, 7400, 6290, 1110),
    {
      quantity: 1,
      original_line_price: 8900,
      final_line_price: 8900,
      product_title: 'Yoga Pant',
      url: '/products/lightly-padded-knee-yoga-pant-black'
    }
  ];
  var r = bundle.computeBundlePromo(items, LIVE, 12580 + 8900, VARIANT);
  assert.equal(r.pairSavingsCents, 2220);
  assert.equal(r.pairSavingsMode, 'applied');
});

test('at 2+ variant: footwear confirmation uses applied tag when discount present', function () {
  var items = [skinLine(2, 7400, 6290, 1110)];
  var r = bundle.computeBundlePromo(items, LIVE, 12580, VARIANT);
  assert.match(r.footwearConfirmationLine, /Save 15%/);
  assert.equal(r.savingsTag, 'Applied');
  assert.equal(r.showPantsOffer, true);
});
