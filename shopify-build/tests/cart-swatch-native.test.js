'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var path = require('path');
var fs = require('fs');
var { parseHTML } = require('linkedom');
var bundle = require('../assets/cart-bundle-promo.js');

function installDom() {
  var parsed = parseHTML('<!DOCTYPE html><html><body></body></html>');
  globalThis.window = parsed.window;
  globalThis.document = parsed.document;
  delete require.cache[path.join(__dirname, '../assets/cart-bundle-promo.js')];
  return require('../assets/cart-bundle-promo.js');
}

var PRODUCT = {
  options: [
    { name: 'Size', position: 1, values: ['M (W 5.5-7.5)'] },
    { name: 'Color', position: 2, values: ['Purple', 'Copper Swirl'] }
  ],
  variants: [
    { id: 101, option1: 'M (W 5.5-7.5)', option2: 'Purple', available: true },
    { id: 102, option1: 'M (W 5.5-7.5)', option2: 'Copper Swirl', available: true }
  ]
};

test('snippet config must not contain fabricated Onyx/Dusty Rose hex map', function () {
  var liquid = fs.readFileSync(
    path.join(__dirname, '../snippets/cart-bundle-promo-config.liquid'),
    'utf8'
  );
  assert.equal(liquid.indexOf('"Onyx": "#050505"'), -1);
  assert.ok(liquid.includes('pdp-buy-box.liquid:653-684'));
  assert.ok(liquid.includes('nativeProductSwatches'));
});

test('missing native map uses text swatch, not invented CSS color', function () {
  var mod = installDom();
  var container = document.createElement('div');
  document.body.appendChild(container);
  var config = mod.mergeConfig({
    enabled: true,
    fetchProductJson: function () {
      return Promise.resolve({ product: PRODUCT });
    },
    nativeProductSwatches: {
      'best-reformer-pilates-legree-workout-shoes': {
        'Copper Swirl': {
          backgroundColor: '#574535',
          imageUrl: 'https://cdn.shopify.com/s/files/1/0045/0612/4391/files/swatch-copper-swirl.png',
          source: 'sections/pdp-buy-box.liquid:668-670'
        }
      }
    }
  });
  mod.mountPromo(
    container,
    [
      {
        quantity: 1,
        final_line_price: 7400,
        product_title: 'Closed Sole Performance Skin',
        variant_title: 'Black · M',
        url: '/products/best-reformer-pilates-legree-workout-shoes'
      }
    ],
    config,
    7400,
    { offerArm: 'variant' }
  );
  container.querySelector('[data-sole-choice="closed"]').click();
  return new Promise(function (resolve) {
    setImmediate(function () {
      setImmediate(function () {
        var purple = container.querySelector('[data-swatch-color="Purple"]');
        var copper = container.querySelector('[data-swatch-color="Copper Swirl"]');
        assert.ok(purple);
        assert.equal(purple.getAttribute('data-swatch-kind'), 'text');
        assert.match(purple.textContent, /Purple/);
        assert.equal(purple.style.backgroundColor, '');
        assert.ok(copper);
        assert.equal(copper.getAttribute('data-swatch-kind'), 'native-image');
        assert.equal(copper.getAttribute('data-swatch-source'), 'sections/pdp-buy-box.liquid:668-670');
        assert.ok(copper.getAttribute('data-swatch-src').indexOf('swatch-copper-swirl') !== -1);
        resolve();
      });
    });
  });
});

test('product option swatch.color used when present in product JSON', function () {
  var mod = installDom();
  var product = {
    options_with_values: [
      {
        name: 'Color',
        values: [{ name: 'Rivian Green', swatch: { color: '#5a7a6a' } }]
      }
    ],
    options: [
      { name: 'Size', position: 1, values: ['M'] },
      { name: 'Color', position: 2, values: ['Rivian Green'] }
    ],
    variants: [{ id: 9, option1: 'M', option2: 'Rivian Green', available: true }]
  };
  var container = document.createElement('div');
  document.body.appendChild(container);
  var config = mod.mergeConfig({
    enabled: true,
    closedSoleProductHandle: 'best-reformer-pilates-legree-workout-shoes',
    fetchProductJson: function () {
      return Promise.resolve({ product: product });
    },
    nativeProductSwatches: { 'best-reformer-pilates-legree-workout-shoes': {} }
  });
  mod.mountPromo(
    container,
    [
      {
        quantity: 1,
        final_line_price: 7400,
        product_title: 'Closed Sole Performance Skin',
        variant_title: 'Black · M',
        url: '/products/best-reformer-pilates-legree-workout-shoes'
      }
    ],
    config,
    7400,
    { offerArm: 'variant' }
  );
  container.querySelector('[data-sole-choice="closed"]').click();
  return new Promise(function (resolve) {
    setImmediate(function () {
      setImmediate(function () {
        var sw = container.querySelector('[data-swatch-color="Rivian Green"]');
        assert.ok(sw);
        assert.equal(sw.getAttribute('data-swatch-kind'), 'native-pdp');
        assert.equal(sw.getAttribute('data-swatch-source'), 'product.options_with_values[].swatch.color');
        resolve();
      });
    });
  });
});
