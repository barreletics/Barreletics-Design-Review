/**
 * Guards against Shopify CLI upload rejections seen on 2026-11-08 partial push.
 */
const assert = require('assert');
const { test } = require('node:test');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');

test('cart-bundle-promo-config: no Liquid tags inside default filter string literals', () => {
  const liquid = fs.readFileSync(
    path.join(ROOT, 'snippets/cart-bundle-promo-config.liquid'),
    'utf8'
  );
  const bad = liquid.match(
    /\|\s*default:\s*'[^']*\{\{[^']*'/
  );
  assert.ok(!bad, 'nested {{ }} inside quoted default: string');
  assert.ok(
    liquid.includes('default_pants_headline'),
    'headline default must use assign concatenation'
  );
  assert.equal(liquid.indexOf('{% raw %}'), -1, 'must not contain raw tag token in file');
});

test('settings_schema: url setting cart_bundle_pant_product_url has no relative-path default', () => {
  const schema = JSON.parse(
    fs.readFileSync(path.join(ROOT, 'config/settings_schema.json'), 'utf8')
  );
  const group = schema.find((g) => g.name === 'Cart bundle preview (Nov08)');
  assert.ok(group);
  const urlSetting = group.settings.find((s) => s.id === 'cart_bundle_pant_product_url');
  assert.ok(urlSetting && urlSetting.type === 'url');
  assert.ok(
    !Object.prototype.hasOwnProperty.call(urlSetting, 'default'),
    'url type must not use shop-relative default'
  );
});
