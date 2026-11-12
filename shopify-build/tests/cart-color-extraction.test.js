'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

var LIVE = bundle.mergeConfig({ enabled: true });
var VARIANT = { offerArm: 'variant' };

test('named Color option wins over Blue / Small variant_title', function () {
  var item = {
    variant_title: 'Blue / Small',
    options_with_values: [{ name: 'Color', value: 'Blue' }, { name: 'Size', value: 'Small' }]
  };
  assert.equal(bundle.extractColorFromLineItem(item), 'Blue');
});

test('Color before Size in options_with_values (ColorFirst fixture)', function () {
  var item = {
    variant_title: 'Small / Navy',
    options_with_values: [
      { name: 'Color', value: 'Navy' },
      { name: 'Size', value: 'Small' }
    ]
  };
  assert.equal(bundle.extractColorFromLineItem(item), 'Navy');
});

test('Size / Color variant_title (ColorLast fixture)', function () {
  var item = {
    variant_title: 'M (W 5.5-7.5) / Coral',
    options_with_values: []
  };
  assert.equal(bundle.extractColorFromLineItem(item), 'Coral');
});

test('colorsUsedInCart blocks duplicate Blue across soles', function () {
  var cart = [
    {
      quantity: 1,
      final_line_price: 7400,
      product_title: 'Closed Sole',
      url: '/products/best-reformer-pilates-legree-workout-shoes',
      variant_title: 'Blue / Small',
      options_with_values: [{ name: 'Color', value: 'Blue' }]
    },
    {
      quantity: 1,
      final_line_price: 7400,
      product_title: 'Open Sole',
      url: '/products/studio-performance-skin-footwear',
      variant_title: 'Black / M',
      options_with_values: [{ name: 'Color', value: 'Black' }]
    }
  ];
  var used = bundle.colorsUsedInCart(cart, LIVE);
  assert.equal(used.blue, true);
  assert.equal(used.black, true);
  var product = {
    options: [
      { name: 'Size', position: 1, values: ['M'] },
      { name: 'Color', position: 2, values: ['Blue', 'White', 'Coral'] }
    ],
    variants: []
  };
  var meta = bundle.colorValuesForProduct(product, used);
  assert.deepEqual(meta.colors, ['White', 'Coral']);
});

test('unknown color string does not invent alias', function () {
  var item = { variant_title: 'MysteryTone / M', options_with_values: [] };
  var c = bundle.extractColorFromLineItem(item);
  assert.equal(c, 'MysteryTone');
  assert.equal(bundle.normalizeColorLabel(c), 'mysterytone');
});

test('isLikelySizeToken rejects Small and single-letter sizes', function () {
  assert.equal(bundle.isLikelySizeToken('Small'), true);
  assert.equal(bundle.isLikelySizeToken('M'), true);
  assert.equal(bundle.isLikelySizeToken('Blue'), false);
});
