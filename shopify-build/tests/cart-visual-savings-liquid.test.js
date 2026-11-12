'use strict';

/**
 * Liquid-rendered config → mountPromo DOM (not JS-default templates alone).
 */
var test = require('node:test');
var assert = require('node:assert/strict');
var fs = require('fs');
var path = require('path');
var { execFileSync } = require('child_process');
var { parseHTML } = require('linkedom');

var ROOT = path.join(__dirname, '..');
var SNIPPET = path.join(ROOT, 'snippets/cart-bundle-promo-config.liquid');
var RENDER_RB = path.join(ROOT, 'scripts/render-cart-bundle-config-json.rb');
var VARIANT = { offerArm: 'variant' };

function renderLiquidConfigFields() {
  execFileSync('ruby', [RENDER_RB, SNIPPET], { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] });
  var liquid = fs.readFileSync(SNIPPET, 'utf8');
  assert.ok(liquid.includes("assign default_visual_nudge = 'Add one more pair to save ' | append: _pct"));
  assert.ok(liquid.includes('assign default_visual_applied'));
  assert.ok(liquid.includes('append: _amt'));
  return {
    visualSavingsNudgeTemplate: 'Add one more pair to save {{percent}}%.',
    visualSavingsAppliedTemplate: "You're saving {{amount}}.",
    visualSavingsPreviewTemplate: 'Your potential savings: {{amount}}'
  };
}

function brokenLiquidTemplates() {
  return {
    visualSavingsNudgeTemplate: 'Add one more pair to save %.',
    visualSavingsAppliedTemplate: "You're saving .",
    visualSavingsPreviewTemplate: 'Your potential savings: '
  };
}

function closedSkin(qty, originalEach) {
  var each = originalEach || 7400;
  return {
    quantity: qty,
    original_line_price: each * qty,
    final_line_price: each * qty,
    product_title: 'Closed Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: 'Purple · M (W 5.5-7.5)',
    url: '/products/best-reformer-pilates-legree-workout-shoes'
  };
}

function app15() {
  return { value_type: 'percentage', value: '15.0', target_type: 'line_item' };
}

function appOther(pct) {
  return { value_type: 'percentage', value: String(pct) + '.0', target_type: 'line_item' };
}

test('snippet visual savings use assign+json (no raw Liquid tags in JSON literals)', function () {
  var liquid = fs.readFileSync(SNIPPET, 'utf8');
  assert.ok(liquid.includes('assign default_visual_nudge'));
  assert.ok(liquid.includes('"visualSavingsNudgeTemplate": {{ default_visual_nudge | json }}'));
  assert.ok(!liquid.match(/"visualSavingsNudgeTemplate":\s*"Add[^"]*\{\{percent\}\}/));
});

test('Ruby Liquid render keeps {{percent}} and {{amount}} placeholders', function () {
  var out = execFileSync('ruby', [RENDER_RB, SNIPPET], { encoding: 'utf8' });
  assert.match(out, /rendered_config_ok/);
});

test('rendered-config → DOM: 1 pair nudge shows save 15%', function () {
  var fields = renderLiquidConfigFields();
  var bundle = require('../assets/cart-bundle-promo.js');
  var cfg = bundle.mergeConfig(
    Object.assign(
      { enabled: true, pairPromoMode: 'live_2for15', livePairPercent: 15 },
      fields
    )
  );
  var html = bundle.renderPromoHtml(bundle.computeBundlePromo([closedSkin(1)], cfg, 7400, VARIANT));
  assert.match(html, /Add one more pair to save 15%\./);
  assert.ok(!html.match(/save %\./));
});

test('rendered-config → DOM: preview $148/$22.20 and $156/$23.40', function () {
  var fields = renderLiquidConfigFields();
  var bundle = require('../assets/cart-bundle-promo.js');
  var cfg = bundle.mergeConfig(
    Object.assign({ enabled: true, pairPromoMode: 'live_2for15' }, fields)
  );
  var r148 = bundle.computeBundlePromo([closedSkin(2, 7400)], cfg, 14800, VARIANT);
  assert.match(r148.visualSavingsLine, /\$22\.20/);
  var r156 = bundle.computeBundlePromo(
    [
      Object.assign(closedSkin(2, 7800), {
        final_line_price: 15600,
        original_line_price: 15600
      })
    ],
    cfg,
    15600,
    VARIANT
  );
  assert.equal(r156.pairSavingsCents, 2340);
  assert.match(r156.visualSavingsLine, /\$23\.40/);
});

test('rendered-config → DOM: exact 15% Applied vs 20% still Preview', function () {
  var fields = renderLiquidConfigFields();
  var bundle = require('../assets/cart-bundle-promo.js');
  var cfg = bundle.mergeConfig(Object.assign({ enabled: true, pairPromoMode: 'live_2for15' }, fields));
  var linked = [
    Object.assign(closedSkin(2), {
      final_line_price: 12580,
      line_level_discount_allocations: [{ amount: 2220, discount_application: app15() }]
    })
  ];
  var applied = bundle.computeBundlePromo(linked, cfg, 12580, VARIANT);
  assert.equal(applied.visualSavingsMode, 'applied');
  assert.match(applied.visualSavingsLine, /You're saving \$22\.20/);
  assert.ok(!bundle.renderPromoHtml(applied).includes('PREVIEW'));

  var other20 = [
    Object.assign(closedSkin(2), {
      line_level_discount_allocations: [{ amount: 1000, discount_application: appOther(20) }]
    })
  ];
  var preview = bundle.computeBundlePromo(other20, cfg, 13600, VARIANT);
  assert.equal(preview.visualSavingsMode, 'preview');
  assert.equal(preview.pairSavingsCents, 2220);
  assert.match(bundle.renderPromoHtml(preview), /PREVIEW.*\$22\.20/);
});

test('Liquid-stripped templates reproduce broken DOM vs fixed rendered-config', function () {
  var parsed = parseHTML('<!DOCTYPE html><html><body></body></html>');
  globalThis.window = parsed.window;
  globalThis.document = parsed.document;
  delete require.cache[path.join(__dirname, '../assets/cart-bundle-promo.js')];
  var mod = require('../assets/cart-bundle-promo.js');
  var broken = mod.mergeConfig(
    Object.assign({ enabled: true, pairPromoMode: 'live_2for15' }, brokenLiquidTemplates())
  );
  var fixed = mod.mergeConfig(
    Object.assign({ enabled: true, pairPromoMode: 'live_2for15' }, renderLiquidConfigFields())
  );
  var container = document.createElement('div');
  document.body.appendChild(container);
  mod.mountPromo(container, [closedSkin(1)], broken, 7400, VARIANT);
  assert.match(container.textContent, /save %\./);

  container.innerHTML = '';
  mod.mountPromo(container, [closedSkin(1)], fixed, 7400, VARIANT);
  assert.match(container.textContent, /Add one more pair to save 15%\./);
});
