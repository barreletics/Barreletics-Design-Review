import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const promo = require('../assets/cart-bundle-promo.js');

const baseConfig = {
  enabled: true,
  tier2Percent: 10,
  tier3Percent: 15,
  pantsPercent: 35,
  pantsPreviewCents: 9800,
  skinMatch: 'Closed Sole',
  skinExclude: 'open sole',
  pantsMatch: 'yoga pant'
};

function skin(qty, priceCents) {
  return {
    product_title: 'Studio Performance Skin — Closed Sole · Onyx',
    quantity: qty,
    original_line_price: priceCents * qty,
    price: priceCents
  };
}

function pants(qty, unitCents) {
  return {
    product_title: 'Lightly Padded Knee Yoga Pant — Black',
    quantity: qty,
    original_line_price: unitCents * qty,
    price: unitCents
  };
}

function openSole(qty) {
  return {
    product_title: 'Studio Performance Skin — Open Sole · Onyx',
    quantity: qty,
    original_line_price: 7400 * qty,
    price: 7400
  };
}

describe('cart bundle promo computeBundlePromo', () => {
  it('flag off hides promo', () => {
    const state = promo.computeBundlePromo({ items: [skin(2, 7400)] }, { ...baseConfig, enabled: false });
    assert.equal(state.visible, false);
    assert.equal(state.enabled, false);
  });

  it('0 qualifying pairs — no tier messaging', () => {
    const state = promo.computeBundlePromo({ items: [openSole(2)] }, baseConfig);
    assert.equal(state.qualifyingPairs, 0);
    assert.equal(state.tierPercent, 0);
    assert.equal(state.messages.length, 0);
  });

  it('1 pair — nudge toward 10% tier', () => {
    const state = promo.computeBundlePromo({ items: [skin(1, 7400)] }, baseConfig);
    assert.equal(state.qualifyingPairs, 1);
    assert.ok(state.messages.some((m) => m.includes('Add 1 pair') && m.includes('10')));
    assert.equal(state.tierPercent, 0);
  });

  it('2 pairs — 10% tier savings and nudge for third', () => {
    const state = promo.computeBundlePromo({ items: [skin(2, 7400)] }, baseConfig);
    assert.equal(state.qualifyingPairs, 2);
    assert.equal(state.tierPercent, 10);
    assert.ok(state.messages.some((m) => m.includes('You save $14.80')));
    assert.ok(state.messages.some((m) => m.includes('Add 1 pair')));
  });

  it('3+ pairs — 15% cap, no fourth tier', () => {
    const state = promo.computeBundlePromo({ items: [skin(4, 7400)] }, baseConfig);
    assert.equal(state.qualifyingPairs, 4);
    assert.equal(state.tierPercent, 15);
    assert.ok(state.messages.some((m) => m.includes('You save $44.40')));
    assert.ok(!state.messages.some((m) => m.includes('Add ')));
  });

  it('2+ pairs with pants — 35% on one pants unit only', () => {
    const state = promo.computeBundlePromo(
      { items: [skin(2, 7400), pants(2, 8900)] },
      baseConfig
    );
    assert.ok(state.messages.some((m) => m.includes('$31.15')));
  });

  it('2+ pairs without pants — pants CTA copy', () => {
    const state = promo.computeBundlePromo({ items: [skin(2, 7400)] }, baseConfig);
    assert.ok(state.messages.some((m) => m.toLowerCase().includes('yoga pants')));
  });

  it('respects edited tier percents from settings', () => {
    const state = promo.computeBundlePromo(
      { items: [skin(3, 10000)] },
      { ...baseConfig, tier3Percent: 12 }
    );
    assert.equal(state.tierPercent, 12);
    assert.ok(state.messages.some((m) => m.includes('$36.00')));
  });

  it('qty transition 3→2 drops tier percent', () => {
    const atThree = promo.computeBundlePromo({ items: [skin(3, 7400)] }, baseConfig);
    const atTwo = promo.computeBundlePromo({ items: [skin(2, 7400)] }, baseConfig);
    assert.equal(atThree.tierPercent, 15);
    assert.equal(atTwo.tierPercent, 10);
  });

  it('remove last qualifying line clears savings', () => {
    const empty = promo.computeBundlePromo({ items: [] }, baseConfig);
    assert.equal(empty.qualifyingPairs, 0);
    assert.equal(empty.savingsCents, 0);
  });

  it('open sole does not count toward pair tiers', () => {
    const state = promo.computeBundlePromo(
      { items: [openSole(3), skin(1, 7400)] },
      baseConfig
    );
    assert.equal(state.qualifyingPairs, 1);
  });
});
