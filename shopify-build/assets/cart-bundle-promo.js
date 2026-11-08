/**
 * Cart bundle preview — mirrors approved 2026-11-07 mock math/copy (checkout unchanged).
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
    tierThreeMin: 3,
    pantsMinPairs: 2,
    pantsPercent: 35,
    pantsProposedPriceCents: 9800,
    footwearOfferTemplate: 'Buy 2+ Closed Sole pairs. Save {{percent}}%.',
    pantsOfferTemplate:
      'Save {{percent}}% on one pair of yoga pants with 2+ Closed Sole pairs.',
    pantsHeadline: 'Save {{percent}}% on one pair of yoga pants with 2+ Closed Sole pairs.',
    pantsQualTemplate: 'Add 1 more Closed Sole pair for {{percent}}% off yoga pants',
    nudgeAddPairTemplate: 'Add {{count}} {{unit}}. Save {{percent}}%.',
    savingsTemplate: 'You save {{amount}}.',
    draftDisplayMode: 'qualification_test',
    previewNotice:
      'Draft test: savings show when cart qualifies. Codes are not auto-applied—use checkout or an offer link below when configured.',
    previewDisclaimer:
      'Theme does not change cart prices. Savings lines are estimates unless a configured discount link is used.',
    footwearDiscountCode: '',
    pantsDiscountCode: '',
    footwearCodeLinkLabel: 'Apply footwear offer code at checkout',
    pantsCodeLinkLabel: 'Apply yoga pants offer code at checkout',
    pantsProductTitle: 'Lightly Padded Knee Yoga Pant',
    pantsImageUrl:
      'https://cdn.shopify.com/s/files/1/0045/0612/4391/files/IMG_2914.jpg?v=1741040643',
    pantsAddLabel: 'Add yoga pants',
    pantsProductHandle: 'lightly-padded-knee-yoga-pant-black',
    pantsProductUrl: '/products/lightly-padded-knee-yoga-pant-black',
    pantsDefaultVariantId: 0,
    freeShippingThresholdCents: 15000,
    skinHandleNeedles: ['closed-sole'],
    skinTitleNeedles: ['Closed Sole', 'Performance Skin'],
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
    if (pairCount >= config.tierThreeMin) {
      return config.tierThreePlusPercent;
    }
    return config.tierTwoPercent;
  }

  function pairsNeededForNextTier(pairCount, config) {
    if (config.pairPromoMode === 'live_2for15') {
      if (pairCount < 2) {
        return { add: 2 - pairCount, savePct: config.livePairPercent };
      }
      return null;
    }
    if (pairCount < 2) {
      return { add: 2 - pairCount, savePct: config.tierTwoPercent };
    }
    if (pairCount < config.tierThreeMin) {
      return { add: config.tierThreeMin - pairCount, savePct: config.tierThreePlusPercent };
    }
    return null;
  }

  function nudgeCopy(pairCount, config) {
    var next = pairsNeededForNextTier(pairCount, config);
    if (!next || next.add <= 0) return '';
    var unit = next.add === 1 ? 'pair' : 'pairs';
    return fillTemplate(config.nudgeAddPairTemplate, {
      count: next.add,
      unit: unit,
      percent: next.savePct
    });
  }

  function estimatePairSavings(pairQty, pairSubtotalCents, config) {
    if (pairQty < 2) return 0;
    var pct = pairTierPercent(pairQty, config);
    return Math.round(pairSubtotalCents * (pct / 100));
  }

  function pantsSaleCents(config) {
    return Math.round(config.pantsProposedPriceCents * (1 - config.pantsPercent / 100));
  }

  function computeBundlePromo(cartItems, rawConfig, cartTotalCents) {
    var config = mergeConfig(rawConfig);
    var items = cartItems || [];

    if (!config.enabled) {
      return { enabled: false, showPanel: false, totalSavingsCents: 0 };
    }

    var skin = sumEligible(items, function (item) {
      return isClosedSoleSkin(item, config);
    });
    var pants = sumEligible(items, function (item) {
      return isEligiblePant(item, config);
    });

    var pairSavingsCents = estimatePairSavings(skin.quantity, skin.subtotalCents, config);
    var pantsSavingsCents = 0;
    if (pants.quantity > 0 && skin.quantity >= config.pantsMinPairs) {
      pantsSavingsCents =
        Math.round(config.pantsProposedPriceCents * (config.pantsPercent / 100)) *
        Math.min(pants.quantity, 1);
    }

    var totalSavingsCents = pairSavingsCents + pantsSavingsCents;
    var subtotalCents = typeof cartTotalCents === 'number' ? cartTotalCents : skin.subtotalCents + pants.subtotalCents;
    var estimatedTotalCents = Math.max(0, subtotalCents - totalSavingsCents);
    var afterPairOnlyCents = Math.max(0, subtotalCents - pairSavingsCents);

    var nudge =
      config.pairPromoMode === 'future_tiers' && skin.quantity > 0
        ? nudgeCopy(skin.quantity, config)
        : '';
    var savingsLine =
      totalSavingsCents > 0
        ? fillTemplate(config.savingsTemplate, { amount: formatMoney(totalSavingsCents) })
        : '';

    var footwearPct =
      config.pairPromoMode === 'live_2for15'
        ? config.livePairPercent
        : config.tierTwoPercent;
    var footwearOfferLine =
      skin.quantity > 0
        ? fillTemplate(config.footwearOfferTemplate || 'Buy 2+ Closed Sole pairs. Save {{percent}}%.', {
            percent: footwearPct
          })
        : '';

    var showPantsOffer = skin.quantity >= 1 && pants.quantity === 0;
    var pantsQualOnly = showPantsOffer && skin.quantity < config.pantsMinPairs;
    var pantsPickerVisible = showPantsOffer && !pantsQualOnly;

    var qualNote = '';
    if (pantsQualOnly) {
      var need = config.pantsMinPairs - skin.quantity;
      qualNote = fillTemplate(config.pantsQualTemplate, {
        percent: config.pantsPercent,
        count: need,
        unit: need === 1 ? 'pair' : 'pairs'
      });
    }

    var pantsTemplate = config.pantsOfferTemplate || config.pantsHeadline;
    var pantsOfferLine = fillTemplate(pantsTemplate, { percent: config.pantsPercent });
    var isQualTest = config.draftDisplayMode === 'qualification_test';
    var footwearCode = String(config.footwearDiscountCode || '').trim();
    var pantsCode = String(config.pantsDiscountCode || '').trim();
    var showFootwearCodeLink = isQualTest && footwearCode && skin.quantity >= 2;
    var showPantsCodeLink =
      isQualTest && pantsCode && skin.quantity >= config.pantsMinPairs && pants.quantity === 0;

  var shippingGapCents = 0;
    var shippingEarned = false;
    if (skin.quantity > 0) {
      if (afterPairOnlyCents >= config.freeShippingThresholdCents) {
        shippingEarned = true;
      } else {
        shippingGapCents = config.freeShippingThresholdCents - afterPairOnlyCents;
      }
    }

    return {
      enabled: true,
      showPanel: skin.quantity > 0,
      pairCount: skin.quantity,
      pantCount: pants.quantity,
      pairSavingsCents: pairSavingsCents,
      pantsSavingsCents: pantsSavingsCents,
      totalSavingsCents: totalSavingsCents,
      subtotalCents: subtotalCents,
      estimatedTotalCents: estimatedTotalCents,
      nudge: nudge,
      footwearOfferLine: footwearOfferLine,
      previewNotice: config.previewNotice,
      draftDisplayMode: config.draftDisplayMode,
      isQualificationTest: isQualTest,
      showFootwearCodeLink: showFootwearCodeLink,
      showPantsCodeLink: showPantsCodeLink,
      footwearDiscountCode: footwearCode,
      pantsDiscountCode: pantsCode,
      savingsLine: savingsLine,
      showPantsOffer: showPantsOffer,
      pantsQualOnly: pantsQualOnly,
      pantsPickerVisible: pantsPickerVisible,
      pantsOfferLine: pantsOfferLine,
      pantsHeadline: pantsOfferLine,
      pantsQualNote: qualNote,
      pantsWasCents: config.pantsProposedPriceCents,
      pantsSaleCents: pantsSaleCents(config),
      disclaimer: config.previewDisclaimer,
      shippingGapCents: shippingGapCents,
      shippingEarned: shippingEarned,
      freeShippingThresholdCents: config.freeShippingThresholdCents,
      config: config
    };
  }

  function sanitizeDiscountCode(code) {
    var c = String(code || '').trim();
    if (!c || !/^[A-Za-z0-9_-]+$/.test(c)) return '';
    return c;
  }

  function discountLink(code, redirectPath) {
    var safe = sanitizeDiscountCode(code);
    if (!safe) return '';
    var redir = redirectPath || '/cart';
    return '/discount/' + encodeURIComponent(safe) + '?redirect=' + encodeURIComponent(redir);
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderPromoHtml(result) {
    if (!result || !result.showPanel) return '';

    var cfg = result.config;
    var simMode = !result.isQualificationTest;
    var html =
      '<div class="cart-bundle-promo" data-cart-bundle-promo role="region" aria-label="Cart bundle offer draft test">';
    html +=
      '<p class="cart-bundle-promo__notice">' + escapeHtml(result.previewNotice) + '</p>';

    if (result.footwearOfferLine) {
      html +=
        '<p class="cart-bundle-promo__footwear-offer">' + escapeHtml(result.footwearOfferLine) + '</p>';
    }

    if (result.nudge) {
      html += '<div class="cart-bundle-promo__progress">' + escapeHtml(result.nudge) + '</div>';
    }

    if (result.savingsLine) {
      html += '<div class="cart-bundle-promo__savings">';
      if (simMode) {
        html += '<span class="cart-bundle-promo__preview-tag">Simulation</span> ';
      }
      html += '<span>' + escapeHtml(result.savingsLine) + '</span></div>';
    }

    if (result.showFootwearCodeLink) {
      var fwHref = discountLink(result.footwearDiscountCode, '/cart');
      html +=
        '<p class="cart-bundle-promo__code-offer"><a class="cart-bundle-promo__code-link" href="' +
        escapeHtml(fwHref) +
        '">' +
        escapeHtml(cfg.footwearCodeLinkLabel) +
        ' (' +
        escapeHtml(result.footwearDiscountCode) +
        ')</a></p>';
    }

    if (result.showPantsOffer) {
      html += '<div class="cart-bundle-promo__pants' + (result.pantsQualOnly ? ' is-qual-only' : '') + '">';
      if (!result.pantsQualOnly) {
        html += '<p class="cart-bundle-promo__pants-headline">' + escapeHtml(result.pantsOfferLine) + '</p>';
      }
      if (result.pantsQualNote) {
        html += '<p class="cart-bundle-promo__pants-qual">' + escapeHtml(result.pantsQualNote) + '</p>';
      }
      html +=
        '<div class="cart-bundle-promo__pants-row">' +
        '<img src="' +
        escapeHtml(cfg.pantsImageUrl) +
        '" alt="" width="56" height="56" loading="lazy" class="cart-bundle-promo__pants-img" />' +
        '<div class="cart-bundle-promo__pants-copy">' +
        '<span class="cart-bundle-promo__pants-title">' +
        escapeHtml(cfg.pantsProductTitle) +
        '</span>' +
        '</div>' +
        '<div class="cart-bundle-promo__pants-prices">' +
        '<span class="cart-bundle-promo__pants-was">' +
        formatMoney(result.pantsWasCents) +
        '</span>' +
        '<strong class="cart-bundle-promo__pants-sale">' +
        formatMoney(result.pantsSaleCents) +
        (simMode ? ' <span class="cart-bundle-promo__preview-tag">simulation</span>' : '') +
        '</strong>' +
        '</div></div>';
      if (result.showPantsCodeLink) {
        var ptHref = discountLink(result.pantsDiscountCode, '/cart');
        html +=
          '<p class="cart-bundle-promo__code-offer"><a class="cart-bundle-promo__code-link" href="' +
          escapeHtml(ptHref) +
          '">' +
          escapeHtml(cfg.pantsCodeLinkLabel) +
          ' (' +
          escapeHtml(result.pantsDiscountCode) +
          ')</a></p>';
      }
      if (result.pantsPickerVisible) {
        html +=
          '<div class="cart-bundle-promo__pants-picker" data-bundle-pants-picker hidden>' +
          '<div class="cart-bundle-promo__pants-selects" data-pants-selects></div>' +
          '<button type="button" class="cart-bundle-promo__pants-add" data-bundle-add-pant disabled>' +
          escapeHtml(cfg.pantsAddLabel) +
          '</button>' +
          '<a class="cart-bundle-promo__pants-link" data-pants-fallback href="' +
          escapeHtml(cfg.pantsProductUrl || '/products/' + (cfg.pantsProductHandle || '')) +
          '">Choose on product page</a>' +
          '</div>';
      }
      html += '</div>';
    }

    html +=
      '<p class="cart-bundle-promo__disclaimer">' + escapeHtml(result.disclaimer) + '</p></div>';
    return html;
  }

  function mountPromo(container, cartItems, config, cartTotalCents) {
    if (!container) return null;
    var result = computeBundlePromo(cartItems, config, cartTotalCents);
    if (!result.showPanel) {
      container.innerHTML = '';
      container.setAttribute('hidden', 'hidden');
      return result;
    }
    container.removeAttribute('hidden');
    container.innerHTML = renderPromoHtml(result);
    if (result.pantsPickerVisible) {
      initPantsPicker(container, result.config);
    }
    return result;
  }

  function resolveVariantFromOptions(variants, selected) {
    if (!variants || !variants.length) return null;
    for (var i = 0; i < variants.length; i++) {
      var v = variants[i];
      var match = true;
      if (selected.option1 !== undefined && v.option1 !== selected.option1) match = false;
      if (selected.option2 !== undefined && v.option2 !== selected.option2) match = false;
      if (selected.option3 !== undefined && v.option3 !== selected.option3) match = false;
      if (match) return v;
    }
    return null;
  }

  function initPantsPicker(root, config) {
    var block = root.querySelector('[data-bundle-pants-picker]');
    if (!block) return;
    var selectsWrap = block.querySelector('[data-pants-selects]');
    var addBtn = block.querySelector('[data-bundle-add-pant]');
    var fallback = block.querySelector('[data-pants-fallback]');
    var handle = config.pantsProductHandle;
    if (!handle) {
      block.hidden = false;
      return;
    }

    var overrideId = parseInt(config.pantsDefaultVariantId, 10) || 0;
    if (overrideId > 0 && addBtn) {
      block.hidden = false;
      addBtn.disabled = false;
      addBtn.setAttribute('data-variant-id', String(overrideId));
      if (selectsWrap) selectsWrap.innerHTML = '<p class="cart-bundle-promo__pants-note">Using theme default variant — change in theme settings.</p>';
      return;
    }

    fetch('/products/' + encodeURIComponent(handle) + '.js', {
      headers: { Accept: 'application/json' }
    })
      .then(function (res) {
        if (!res.ok) throw new Error('product-js-failed');
        return res.json();
      })
      .then(function (data) {
        var product = data.product || data;
        var variants = product.variants || [];
        if (!variants.length) throw new Error('no-variants');
        var options = product.options || [];
        block.hidden = false;
        if (fallback) fallback.hidden = true;
        selectsWrap.innerHTML = '';
        var selected = {};

        options.forEach(function (opt, idx) {
          var name = opt.name;
          var position = opt.position || idx + 1;
          var key = 'option' + position;
          var sel = document.createElement('select');
          sel.className = 'cart-bundle-promo__pants-select';
          sel.setAttribute('aria-label', name);
          sel.dataset.optionKey = key;
          var placeholder = document.createElement('option');
          placeholder.value = '';
          placeholder.textContent = name;
          placeholder.disabled = true;
          placeholder.selected = true;
          sel.appendChild(placeholder);
          (opt.values || []).forEach(function (val) {
            var o = document.createElement('option');
            o.value = val;
            o.textContent = val;
            sel.appendChild(o);
          });
          sel.addEventListener('change', function () {
            selected[key] = sel.value || undefined;
            updatePantsAddButton(addBtn, variants, selected);
          });
          selectsWrap.appendChild(sel);
        });

        updatePantsAddButton(addBtn, variants, selected);
      })
      .catch(function () {
        block.hidden = false;
        if (selectsWrap) {
          selectsWrap.innerHTML =
            '<p class="cart-bundle-promo__pants-note">Could not load sizes here. Use product page.</p>';
        }
        if (addBtn) addBtn.hidden = true;
        if (fallback) fallback.hidden = false;
      });
  }

  function updatePantsAddButton(btn, variants, selected) {
    if (!btn) return;
    var need = {};
    var keys = Object.keys(selected);
    if (keys.length === 0) {
      btn.disabled = true;
      btn.removeAttribute('data-variant-id');
      return;
    }
    keys.forEach(function (k) {
      if (selected[k]) need[k] = selected[k];
    });
    var resolved = resolveVariantFromOptions(variants, need);
    if (resolved && resolved.id) {
      btn.disabled = false;
      btn.setAttribute('data-variant-id', String(resolved.id));
    } else {
      btn.disabled = true;
      btn.removeAttribute('data-variant-id');
    }
  }

  return {
    DEFAULTS: DEFAULTS,
    mergeConfig: mergeConfig,
    computeBundlePromo: computeBundlePromo,
    renderPromoHtml: renderPromoHtml,
    mountPromo: mountPromo,
    initPantsPicker: initPantsPicker,
    resolveVariantFromOptions: resolveVariantFromOptions,
    isClosedSoleSkin: isClosedSoleSkin,
    isEligiblePant: isEligiblePant,
    pantsSaleCents: pantsSaleCents
  };
});
