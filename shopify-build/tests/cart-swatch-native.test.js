'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var path = require('path');
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

test('missing native map uses text swatch, not invented CSS color', function () {
  var mod = installDom();
  var container = document.createElement('div');
  document.body.appendChild(container);
  var config = mod.mergeConfig({
    enabled: true,
    fetchProductJson: function () {
      return Promise.resolve({ product: PRODUCT });
    },
    colorSwatchImages: {
      'Copper Swirl': 'https://cdn.shopify.com/s/files/1/0045/0612/4391/files/swatch-copper-swirl.png'
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
        assert.ok(copper.getAttribute('data-swatch-src').indexOf('swatch-copper-swirl') !== -1);
        resolve();
      });
    });
  });
});
