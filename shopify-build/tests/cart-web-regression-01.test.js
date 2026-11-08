'use strict';

/**
 * WEB-CART-REGRESSION-01 — behavioral regressions against COPY03 module (f72cf96 production frozen).
 * Category A: control / 5a01277 eligibility parity.
 * Category B: Color-first extraction (Color and Colour), size must not parse as color.
 * Category C: unknown cart color — expected RED on unchanged f72cf96 until product fix ships.
 */

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');
var baseline = require('./fixtures/cart-bundle-promo-5a01277-baseline.js');

var CTRL_CFG = baseline.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var COPY03_CFG = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var VARIANT = { offerArm: 'variant' };

var CLOSED_SOLE_PRODUCT_FIXTURE = {
  options: [
    { name: 'Size', position: 1, values: ['M (W 5.5-7.5)', 'L (W 8-11)'] },
    { name: 'Color', position: 2, values: ['Purple', 'Black', 'White'] }
  ],
  variants: [
    { id: 101, option1: 'M (W 5.5-7.5)', option2: 'Purple', available: true },
    { id: 102, option1: 'M (W 5.5-7.5)', option2: 'Black', available: true },
    { id: 103, option1: 'M (W 5.5-7.5)', option2: 'White', available: true }
  ]
};

function cartLine(overrides) {
  return Object.assign(
    {
      quantity: 1,
      final_line_price: 7400,
      product_title: '',
      product_type: '',
      variant_title: '',
      url: '',
      options_with_values: []
    },
    overrides
  );
}

function hasUnresolvedPerformanceSkinColor(items, config) {
  return (items || []).some(function (item) {
    return bundle.isPerformanceSkin(item, config) && !bundle.extractColorFromLineItem(item);
  });
}

// --- Category A: control eligibility parity (PASS on f72cf96) ---

test('WEB-CART-REGRESSION-01 A: best-reformer handle + Performance Skins title excluded in control (5a)', function () {
  var item = cartLine({
    product_title: 'Performance Skins',
    url: '/products/best-reformer-pilates-legree-workout-shoes',
    variant_title: 'Purple · M'
  });
  assert.equal(bundle.isClosedSoleSkin5a(item, CTRL_CFG), false);
  var b = baseline.computeBundlePromo([item], CTRL_CFG, 7400);
  var c = bundle.computeBundlePromo([item], CTRL_CFG, 7400);
  assert.equal(b.showPanel, false);
  assert.equal(c.showPanel, false);
  assert.equal(c.showPanel, b.showPanel);
});

test('WEB-CART-REGRESSION-01 A: control parity does not broaden closed-sole handle eligibility vs baseline', function () {
  var item = cartLine({
    product_title: 'Performance Skins',
    url: '/products/best-reformer-pilates-legree-workout-shoes',
    variant_title: 'Black / Small',
    options_with_values: [{ name: 'Color', value: 'Black' }, { name: 'Size', value: 'Small' }]
  });
  var b = baseline.computeBundlePromo([item], CTRL_CFG, 7400);
  var c = bundle.computeBundlePromo([item], CTRL_CFG, 7400);
  assert.equal(c.showPanel, b.showPanel);
  assert.equal(c.showPanel, false);
});

// --- Category B: Color / Colour extraction (PASS on f72cf96) ---

test('WEB-CART-REGRESSION-01 B: named Colour option wins over Blue / Small variant_title', function () {
  var item = {
    variant_title: 'Blue / Small',
    options_with_values: [{ name: 'Colour', value: 'Navy' }, { name: 'Size', value: 'Small' }]
  };
  assert.equal(bundle.extractColorFromLineItem(item), 'Navy');
});

test('WEB-CART-REGRESSION-01 B: Color option before Size in options_with_values', function () {
  var item = {
    variant_title: 'Small / Coral',
    options_with_values: [
      { name: 'Color', value: 'Coral' },
      { name: 'Size', value: 'Small' }
    ]
  };
  assert.equal(bundle.extractColorFromLineItem(item), 'Coral');
});

test('WEB-CART-REGRESSION-01 B: Size before Color in options_with_values', function () {
  var item = {
    variant_title: 'M (W 5.5-7.7) / Dusty Blue',
    options_with_values: [
      { name: 'Size', value: 'M (W 5.5-7.5)' },
      { name: 'Color', value: 'Dusty Blue' }
    ]
  };
  assert.equal(bundle.extractColorFromLineItem(item), 'Dusty Blue');
});

test('WEB-CART-REGRESSION-01 B: variant_title Small alone is not parsed as a color', function () {
  var item = {
    variant_title: 'Small',
    options_with_values: [{ name: 'Size', value: 'Small' }]
  };
  assert.equal(bundle.extractColorFromLineItem(item), '');
  assert.equal(bundle.isLikelySizeToken('Small'), true);
});

test('WEB-CART-REGRESSION-01 B: variant_title Blue / Small without options uses Blue not Small', function () {
  var item = { variant_title: 'Blue / Small', options_with_values: [] };
  assert.equal(bundle.extractColorFromLineItem(item), 'Blue');
});

// --- Category C: unknown cart color (RED on f72cf96) ---

test('WEB-CART-REGRESSION-01 C: unresolved cart color must not silently offer full differentiated color list', function () {
  var cart = [
    cartLine({
      product_title: 'Performance Skins — Closed Sole',
      product_type: 'Grippy Shoes',
      url: '/products/studio-performance-skin-closed-sole',
      variant_title: 'Small',
      options_with_values: [{ name: 'Size', value: 'Small' }]
    })
  ];
  assert.equal(hasUnresolvedPerformanceSkinColor(cart, COPY03_CFG), true);
  var used = bundle.colorsUsedInCart(cart, COPY03_CFG);
  assert.deepEqual(used, {});
  var meta = bundle.colorValuesForProduct(CLOSED_SOLE_PRODUCT_FIXTURE, used);
  var r = bundle.computeBundlePromo(cart, COPY03_CFG, 7400, VARIANT);
  assert.equal(r.showAddPairStage, true);

  var catalogColorCount = CLOSED_SOLE_PRODUCT_FIXTURE.options[1].values.length;
  var silentlyOffersEveryColor =
    meta.colors.length === catalogColorCount && !r.unknownCartColorNotice && !r.addPairColorUnresolvedNotice;

  var honestHandling =
    meta.colors.length === 0 ||
    Boolean(r.unknownCartColorNotice) ||
    Boolean(r.addPairColorUnresolvedNotice);

  assert.ok(
    honestHandling,
    'expected unknown/unavailable color notice or withheld picker colors when cart color is unresolved; ' +
      'got full color list (' +
      meta.colors.join(', ') +
      ') with no notice fields on computeBundlePromo'
  );
  assert.equal(silentlyOffersEveryColor, false);
});
