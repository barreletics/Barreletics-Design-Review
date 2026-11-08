/**
 * Cart bundle / mix-match promo — preview estimates only (no checkout discounts).
 * Shared logic for Node tests and browser (BarreleticsCartBundle).
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.BarreleticsCartBundle = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var DEFAULTS = {
    enabled: false,
    pairPromoMode: 'live_2for15',
    livePairPercent: 15,
    tierTwoPercent: 10,
    tierThreePlusPercent: 15,
    pantsMinPairs: 2,
    pantsPercent: 35,
    pantsProposedPriceCents: 9800,
    pantsHeadline: 'Complete your set. Save 35% on yoga pants.',
    nudgeAddPairTemplate: 'Add 1 pair. Save {{percent}}%.',
    savingsTemplate: 'You save {{amount}}.',
    previewDisclaimer:
      'Preview estimate only. Your cart still uses live Shopify prices; checkout discounts are not applied by this theme preview.',
    skinHandleNeedles: ['closed-sole'],
    skinTitleNeedles: ['Closed Sole'],
    pantHandleNeedles: ['pant', 'yoga-pant'],
    pantTitleNeedles: ['Yoga Pant', 'Pant'],
    skinRequireClosedSole: true
  };

  function mergeConfig(config) {
    var out = {};
    var key;
    for (key in DEFAULTS) {
      if (Object.prototype.hasOwnProperty.call(DEFAULTS, key)) {
        out[key] = DEFAULTS[key];
      }
    }
    if (config) {
      for (key in config) {
        if (Object.prototype.hasOwnProperty.call(config, key) && config[key] !== undefined && config[key] !== null) {
          out[key] = config[key];
        }
      }
    }
    return out;
  }

  function parseNeedles(raw) {
    if (!raw) return [];
    if (Array.isArray(raw)) return raw;
    return String(raw)
      .split(',')
      .map(function (s) {
        return s.trim();
      })
      .filter(Boolean);
  }

  function itemHandle(item) {
    if (!item || !item.url) return '';
    var match = String(item.url).match(/\/products\/([^/?#]+)/);
    return match ? match[1].toLowerCase() : '';
  }

  function needlesMatch(text, needles) {
    var hay = String(text || '').toLowerCase();
    for (var i = 0; i < needles.length; i++) {
      if (hay.indexOf(String(needles[i]).toLowerCase()) !== -1) return true;
    }
    return false;
  }

  function isClosedSoleSkin(item, config) {
    var handles = parseNeedles(config.skinHandleNeedles);
    var titles = parseNeedles(config.skinTitleNeedles);
    var handle = itemHandle(item);
    var title = (item.product_title || item.title || '') + ' ' + (item.variant_title || '');
    var productType = item.product_type || '';
    var matchesSkin =
      needlesMatch(handle, handles) ||
      needlesMatch(title, titles) ||
      needlesMatch(productType, titles);
    if (!matchesSkin) return false;
    if (config.skinRequireClosedSole) {
      var closedNeedle = ['closed sole', 'closed-sole'];
      return (
        needlesMatch(title, closedNeedle) ||
        needlesMatch(handle, ['closed-sole']) ||
        needlesMatch(productType, closedNeedle)
      );
    }
    return true;
  }

  function isEligiblePant(item, config) {
    var handles = parseNeedles(config.pantHandleNeedles);
    var titles = parseNeedles(config.pantTitleNeedles);
    var handle = itemHandle(item);
    var title = (item.product_title || item.title || '') + ' ' + (item.variant_title || '');
    var productType = item.product_type || '';
    return (
      needlesMatch(handle, handles) ||
      needlesMatch(title, titles) ||
      needlesMatch(productType, titles)
    );
  }

  function sumEligible(items, predicate) {
    var qty = 0;
    var subtotal = 0;
    for (var i = 0; i < items.length; i++) {
      if (predicate(items[i])) {
        var q = items[i].quantity || 0;
        qty += q;
        subtotal += items[i].final_line_price || items[i].line_price || 0;
      }
    }
    return { quantity: qty, subtotalCents: subtotal };
  }

  function formatMoney(cents) {
    return '$' + (cents / 100).toFixed(2);
  }

  function fillTemplate(template, vars) {
    var out = template;
    var key;
    for (key in vars) {
      if (Object.prototype.hasOwnProperty.call(vars, key)) {
        out = out.split('{{' + key + '}}').join(String(vars[key]));
      }
    }
    return out;
  }

  function pairTierPercent(pairCount, config) {
    if (pairCount < 2) return 0;
    if (config.pairPromoMode === 'live_2for15') {
      return config.livePairPercent;
    }
    if (pairCount >= 3) return config.tierThreePlusPercent;
    return config.tierTwoPercent;
  }

  function nextPairNudgePercent(pairCount, config) {
    if (config.pairPromoMode === 'live_2for15') {
      return config.livePairPercent;
    }
    if (pairCount === 0) return config.tierTwoPercent;
    if (pairCount === 1) return config.tierTwoPercent;
    return config.tierThreePlusPercent;
  }

  function estimatePairSavings(pairQty, pairSubtotalCents, config) {
    if (pairQty < 2) return 0;
    var pct = pairTierPercent(pairQty, config);
    return Math.round(pairSubtotalCents * (pct / 100));
  }

  function computeBundlePromo(cartItems, rawConfig) {
    var config = mergeConfig(rawConfig);
    var items = cartItems || [];

    if (!config.enabled) {
      return { enabled: false, totalSavingsCents: 0, lines: [], showPanel: false };
    }

    var skin = sumEligible(items, function (item) {
      return isClosedSoleSkin(item, config);
    });
    var pants = sumEligible(items, function (item) {
      return isEligiblePant(item, config);
    });

    var lines = [];
    var totalSavingsCents = 0;

    var activePairPct = pairTierPercent(skin.quantity, config);

    if (skin.quantity === 0) {
      lines.push({
        type: 'pair',
        variant: 'empty',
        message: null
      });
    } else if (skin.quantity === 1) {
      var nudgePct = nextPairNudgePercent(1, config);
      lines.push({
        type: 'pair',
        variant: 'nudge',
        message: fillTemplate(config.nudgeAddPairTemplate, { percent: nudgePct })
      });
    } else {
      var pairSave = estimatePairSavings(skin.quantity, skin.subtotalCents, config);
      totalSavingsCents += pairSave;
      lines.push({
        type: 'pair',
        variant: 'active',
        message:
          config.pairPromoMode === 'live_2for15'
            ? 'Pair offer (live): save ' + activePairPct + '% on eligible Performance Skins pairs.'
            : 'Pair offer: save ' + activePairPct + '% on eligible Performance Skins pairs.',
        savingsCents: pairSave,
        pairCount: skin.quantity
      });
    }

    if (skin.quantity >= config.pantsMinPairs) {
      var pantsSave = 0;
      if (pants.quantity > 0) {
        var discountedUnits = Math.min(pants.quantity, 1);
        pantsSave = Math.round(config.pantsProposedPriceCents * (config.pantsPercent / 100)) * discountedUnits;
        totalSavingsCents += pantsSave;
      }
      lines.push({
        type: 'pants',
        variant: pants.quantity > 0 ? 'active' : 'eligible',
        message: fillTemplate(config.pantsHeadline, { percent: config.pantsPercent }),
        savingsCents: pantsSave,
        previewUnitPriceCents: Math.round(config.pantsProposedPriceCents * (1 - config.pantsPercent / 100))
      });
    }

    if (totalSavingsCents > 0) {
      lines.push({
        type: 'total',
        variant: 'savings',
        message: fillTemplate(config.savingsTemplate, { amount: formatMoney(totalSavingsCents) })
      });
    }

    return {
      enabled: true,
      showPanel: true,
      pairCount: skin.quantity,
      pantCount: pants.quantity,
      totalSavingsCents: totalSavingsCents,
      lines: lines,
      disclaimer: config.previewDisclaimer,
      estimatedSubtotalCents: null
    };
  }

  function renderPromoHtml(result) {
    if (!result || !result.showPanel) return '';

    var html =
      '<div class="cart-bundle-promo" data-cart-bundle-promo role="region" aria-label="Bundle savings preview">' +
      '<p class="cart-bundle-promo__badge">Preview estimate</p>';

    for (var i = 0; i < result.lines.length; i++) {
      var line = result.lines[i];
      if (!line.message) continue;
      var mod = 'cart-bundle-promo__line--' + line.type;
      if (line.variant) mod += ' cart-bundle-promo__line--' + line.variant;
      html +=
        '<p class="cart-bundle-promo__line ' +
        mod +
        '">' +
        escapeHtml(line.message) +
        '</p>';
    }

    html +=
      '<p class="cart-bundle-promo__disclaimer">' + escapeHtml(result.disclaimer) + '</p></div>';
    return html;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function mountPromo(container, cartItems, config) {
    if (!container) return null;
    var result = computeBundlePromo(cartItems, config);
    if (!result.showPanel) {
      container.innerHTML = '';
      container.setAttribute('hidden', 'hidden');
      return result;
    }
    container.removeAttribute('hidden');
    container.innerHTML = renderPromoHtml(result);
    return result;
  }

  return {
    DEFAULTS: DEFAULTS,
    mergeConfig: mergeConfig,
    computeBundlePromo: computeBundlePromo,
    renderPromoHtml: renderPromoHtml,
    mountPromo: mountPromo,
    isClosedSoleSkin: isClosedSoleSkin,
    isEligiblePant: isEligiblePant
  };
});
