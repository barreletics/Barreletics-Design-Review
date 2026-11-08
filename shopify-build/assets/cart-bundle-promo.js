/**
 * Cart bundle / mix-match promo — theme preview only (Nov 2026).
 * Does not create or apply Shopify discounts; estimates savings for UX when enabled.
 */
(function (root, factory) {
  var api = factory();
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
  }
  root.BarreleticsCartBundlePromo = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  function normalizeConfig(raw) {
    raw = raw || {};
    return {
      enabled: !!raw.enabled,
      tier2Percent: clampPercent(parseInt(raw.tier2Percent, 10), 10),
      tier3Percent: clampPercent(parseInt(raw.tier3Percent, 10), 15),
      pantsPercent: clampPercent(parseInt(raw.pantsPercent, 10), 35),
      pantsPreviewCents: parseInt(raw.pantsPreviewCents, 10) || 9800,
      skinMatch: (raw.skinMatch || 'Closed Sole').toLowerCase(),
      skinExclude: (raw.skinExclude || 'open sole').toLowerCase(),
      pantsMatch: (raw.pantsMatch || 'yoga pant').toLowerCase(),
      copyAddPair: raw.copyAddPair || 'Add {count} pair. Save {percent}%.',
      copyYouSave: raw.copyYouSave || 'You save {amount}.',
      copyPantsCta: raw.copyPantsCta || 'Complete your set. Save {percent}% on yoga pants.',
      copyPreview: raw.copyPreview || 'Preview only — checkout discounts are configured separately in Shopify.',
      collectionCta: raw.collectionCta || '/collections/closed-sole'
    };
  }

  function clampPercent(n, fallback) {
    if (isNaN(n) || n < 0) return fallback;
    if (n > 100) return 100;
    return n;
  }

  function itemTitle(item) {
    return (item && (item.product_title || item.title) || '').toLowerCase();
  }

  function isQualifyingSkin(item, config) {
    var title = itemTitle(item);
    if (title.indexOf(config.skinMatch) === -1) return false;
    if (config.skinExclude && title.indexOf(config.skinExclude) !== -1) return false;
    return true;
  }

  function isPants(item, config) {
    return itemTitle(item).indexOf(config.pantsMatch) !== -1;
  }

  function lineOriginalCents(item) {
    if (item.original_line_price != null) return item.original_line_price;
    if (item.line_price != null) return item.line_price;
    return (item.price || 0) * (item.quantity || 1);
  }

  function unitOriginalCents(item) {
    var qty = item.quantity || 1;
    if (item.original_price != null) return item.original_price;
    if (item.price != null) return item.price;
    return Math.round(lineOriginalCents(item) / qty);
  }

  /**
   * Pure cart analysis — exported for unit tests.
   */
  function computeBundlePromo(cart, rawConfig) {
    var config = normalizeConfig(rawConfig);
    var empty = {
      enabled: config.enabled,
      visible: false,
      qualifyingPairs: 0,
      tierPercent: 0,
      messages: [],
      savingsCents: 0,
      previewNotice: config.copyPreview
    };

    if (!config.enabled) return empty;

    var items = (cart && cart.items) || [];
    var qualifyingPairs = 0;
    var skinSubtotalCents = 0;
    var pantsLines = [];

    items.forEach(function (item) {
      if (isQualifyingSkin(item, config)) {
        qualifyingPairs += item.quantity || 0;
        skinSubtotalCents += lineOriginalCents(item);
      }
      if (isPants(item, config)) {
        pantsLines.push(item);
      }
    });

    if (qualifyingPairs === 0 && pantsLines.length === 0) {
      return empty;
    }

    var tierPercent = 0;
    if (qualifyingPairs >= 3) {
      tierPercent = config.tier3Percent;
    } else if (qualifyingPairs >= 2) {
      tierPercent = config.tier2Percent;
    }

    var skinSavingsCents = Math.round(skinSubtotalCents * (tierPercent / 100));

    var pantsSavingsCents = 0;
    var pantsCta = false;
    if (qualifyingPairs >= 2) {
      if (pantsLines.length > 0) {
        var pantsItem = pantsLines[0];
        pantsSavingsCents = Math.round(unitOriginalCents(pantsItem) * (config.pantsPercent / 100));
      } else {
        pantsCta = true;
        pantsSavingsCents = Math.round(config.pantsPreviewCents * (config.pantsPercent / 100));
      }
    }

    var savingsCents = skinSavingsCents + (qualifyingPairs >= 2 ? pantsSavingsCents : 0);
    var messages = [];

    if (qualifyingPairs === 1) {
      messages.push(
        formatCopy(config.copyAddPair, {
          count: '1',
          percent: String(config.tier2Percent)
        })
      );
    } else if (qualifyingPairs === 2) {
      messages.push(
        formatCopy(config.copyAddPair, {
          count: '1',
          percent: String(config.tier3Percent)
        })
      );
    }

    if (tierPercent > 0 && skinSavingsCents > 0) {
      messages.push(
        formatCopy(config.copyYouSave, { amount: formatMoney(skinSavingsCents) })
      );
    }

    if (qualifyingPairs >= 2) {
      if (pantsCta) {
        messages.push(
          formatCopy(config.copyPantsCta, { percent: String(config.pantsPercent) })
        );
      } else if (pantsSavingsCents > 0) {
        messages.push(
          formatCopy(config.copyYouSave, { amount: formatMoney(pantsSavingsCents) })
        );
      }
    }

    return {
      enabled: true,
      visible: messages.length > 0 || qualifyingPairs > 0,
      qualifyingPairs: qualifyingPairs,
      tierPercent: tierPercent,
      messages: messages,
      savingsCents: savingsCents,
      previewNotice: config.copyPreview,
      showCollectionLink: qualifyingPairs > 0 && qualifyingPairs < 2
    };
  }

  function formatCopy(template, vars) {
    return template.replace(/\{(\w+)\}/g, function (_, key) {
      return vars[key] != null ? vars[key] : '';
    });
  }

  function formatMoney(cents) {
    return '$' + (cents / 100).toFixed(2);
  }

  function readConfig() {
    var el = document.getElementById('cart-bundle-promo-config');
    if (!el) return normalizeConfig({});
    try {
      return normalizeConfig(JSON.parse(el.textContent));
    } catch (e) {
      return normalizeConfig({});
    }
  }

  function renderPromo(root, state, config) {
    if (!root) return;
    if (!state.enabled || !state.visible) {
      root.hidden = true;
      root.innerHTML = '';
      return;
    }
    root.hidden = false;
    var html = '<div class="cart-bundle-promo__inner">';
    html += '<p class="cart-bundle-promo__label">Performance Skin pairs</p>';
    html += '<ul class="cart-bundle-promo__messages">';
    state.messages.forEach(function (msg) {
      html += '<li>' + escapeHtml(msg) + '</li>';
    });
    html += '</ul>';
    html += '<p class="cart-bundle-promo__notice">' + escapeHtml(state.previewNotice) + '</p>';
    if (state.showCollectionLink && config.collectionCta) {
      html += '<a class="cart-bundle-promo__link" href="' + escapeHtml(config.collectionCta) + '">Shop Closed Sole Performance Skins</a>';
    }
    html += '</div>';
    root.innerHTML = html;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function update(cart) {
    var config = readConfig();
    var state = computeBundlePromo(cart, config);
    document.querySelectorAll('[data-cart-bundle-promo]').forEach(function (root) {
      renderPromo(root, state, config);
    });
    return state;
  }

  return {
    computeBundlePromo: computeBundlePromo,
    normalizeConfig: normalizeConfig,
  update: update
  };
});
