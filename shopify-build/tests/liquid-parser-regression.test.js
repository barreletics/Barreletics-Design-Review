/**
 * Shopify Liquid parse regression (Ruby liquid gem — same class of failure as theme upload).
 */
const assert = require('assert');
const { test } = require('node:test');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const RUBY = process.env.LIQUID_RUBY || 'ruby';
const VALIDATOR = path.join(ROOT, 'scripts/validate-snippet-liquid.rb');
const SNIPPET = path.join(ROOT, 'snippets/cart-bundle-promo-config.liquid');
const BROKEN = path.join(
  ROOT,
  'tests/fixtures/cart-bundle-promo-config-broken-raw-in-comment.liquid'
);

function parseLiquid(filePath) {
  return execFileSync(RUBY, [VALIDATOR, filePath], {
    encoding: 'utf8',
    env: {
      ...process.env,
      GEM_HOME: process.env.GEM_HOME || `${process.env.HOME}/.local/share/gem/ruby/3.2.0`,
      PATH: `${process.env.HOME}/.local/share/gem/ruby/3.2.0/bin:${process.env.PATH}`
    }
  });
}

test('Ruby Liquid parses deployment snippet bytes (exit 0)', () => {
  const artifactBytes = fs.readFileSync(SNIPPET);
  const out = parseLiquid(SNIPPET);
  assert.match(out, /liquid_parse_ok/);
  assert.ok(artifactBytes.indexOf('{% raw %}') === -1, 'snippet must not contain {% raw %} token');
});

test('broken fixture reproduces raw-never-closed parse error', () => {
  assert.throws(
    () => parseLiquid(BROKEN),
  (err) => {
      const msg = (err.stderr || err.message || '').toString();
      return msg.includes('raw') && msg.includes('never closed');
    },
    'expected Liquid::SyntaxError for raw in comment'
  );
});
