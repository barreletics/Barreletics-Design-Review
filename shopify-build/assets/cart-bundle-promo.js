/**
 * Cart bundle preview — URL arm ?br_cart_offer=control|variant (default control).
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
    footwearOfferTemplate: 'Buy 2+ pairs of Performance Skins. Save {{percent}}%.',
    pantsOfferTemplate:
      'Save {{percent}}% on one pair of yoga pants with 2+ Performance Skin pairs.',
    pantsHeadline:
      'Save {{percent}}% on one pair of yoga pants with 2+ Performance Skin pairs.',
    pantsQualTemplate: 'Add 1 more Closed Sole pair for {{percent}}% off yoga pants',
    nudgeAddPairTemplate: 'Add {{count}} {{unit}}. Save {{percent}}%.',
    savingsTemplate: 'You save {{amount}}.',
    previewNotice: "Preview only—offers aren't applied at checkout.",
    previewDisclaimer:
      'Preview estimate only. Your cart still uses live Shopify prices; checkout discounts are not applied by this theme preview.',
    pantsProductTitle: 'Lightly Padded Knee Yoga Pant',
    pantsImageUrl:
      'https://cdn.shopify.com/s/files/1/0045/0612/4391/files/IMG_2914.jpg?v=1741040643',
    pantsAddLabel: 'Add yoga pants',
    pantsProductHandle: 'lightly-padded-knee-yoga-pant-black',
    pantsProductUrl: '/products/lightly-padded-knee-yoga-pant-black',
    pantsDefaultVariantId: 0,
    freeShippingThresholdCents: 15000,
    openSoleProductHandle: 'studio-performance-skin-footwear',
    closedSoleProductHandle: 'best-reformer-pilates-legree-workout-shoes',
    addPairHeadline: 'Add one more pair of Performance Skins',
    openSoleAddLabel: 'Add Open Sole',
    closedSoleAddLabel: 'Add Closed Sole',
    addPairSubmitLabel: 'Add pair to cart',
    skinHandleNeedles: [
      'closed-sole',
      'open-sole',
      'performance-skin',
      'reformer-pilates',
      'studio-performance',
      'studio-performance-skin-footwear',
      'best-reformer-pilates-legree-workout-shoes'
    ],
    skinTitleNeedles: ['Closed Sole', 'Open Sole', 'Performance Skin', 'Grippy Shoes'],
    pantHandleNeedles: ['pant', 'yoga-pant'],
    pantTitleNeedles: ['Yoga Pant', 'Pant'],
    skinRequireClosedSole: false
  };

  var CART_OFFER_PARAM = 'br_cart_offer';

  function parseCartOfferArm(searchString) {
    var q = String(searchString || '');
    if (q.charAt(0) !== '?' && q.indexOf(CART_OFFER_PARAM) !== -1) {
      q = '?' + q.replace(/^[?&]/, '');
    }
    var val = '';
    if (typeof URLSearchParams !== 'undefined') {
      try {
        val = new URLSearchParams(q.charAt(0) === '?' ? q.slice(1) : q).get(CART_OFFER_PARAM) || '';
      } catch (e) {
        val = '';
      }
    } else {
      var m = q.match(new RegExp('[?&]' + CART_OFFER_PARAM + '=([^&]+)', 'i'));
      val = m ? m[1] : '';
    }
    val = String(val || '')
      .toLowerCase()
      .trim();
    if (val === 'variant') return 'variant';
    return 'control';
  }

  function resolveOfferArm(opts) {
    if (opts && opts.offerArm === 'variant') return 'variant';
    if (opts && opts.offerArm === 'control') return 'control';
    var search = opts && opts.search;
    if (!search && typeof window !== 'undefined' && window.location) {
      search = window.location.search || '';
    }
    return parseCartOfferArm(search || '');
  }

  function controlConfigForArm(rawConfig) {
    var base = mergeConfig(rawConfig);
    return mergeConfig(
      Object.assign({}, base, {
        footwearOfferTemplate: 'Buy 2+ Closed Sole pairs. Save {{percent}}%.',
        pantsOfferTemplate:
          'Save {{percent}}% on one pair of yoga pants with 2+ Closed Sole pairs.',
        pantsHeadline:
          'Save {{percent}}% on one pair of yoga pants with 2+ Closed Sole pairs.',
        pantsQualTemplate: 'Add 1 more Closed Sole pair for {{percent}}% off yoga pants',
        skinHandleNeedles: ['closed-sole'],
        skinTitleNeedles: ['Closed Sole', 'Performance Skin'],
        skinRequireClosedSole: true
      })
    );
  }

  function isUnpublishedThemeRole() {
    if (typeof window === 'undefined') return null;
    var theme = window.Shopify && window.Shopify.theme;
    if (!theme || !theme.role) return null;
    return theme.role !== 'main';
  }

  function hrefWithOfferArm(href, arm) {
    if (arm !== 'variant' || !href || String(href).indexOf('/checkout') !== -1) return href;
    try {
      var base =
        typeof window !== 'undefined' && window.location ? window.location.origin : 'https://example.com';
      var url = new URL(href, base);
      if (url.pathname.indexOf('/checkout') === 0) return href;
      url.searchParams.set(CART_OFFER_PARAM, 'variant');
      return url.pathname + url.search + url.hash;
    } catch (e) {
      return href;
    }
  }

  function decorateCartOfferNavLinks(arm) {
    if (arm !== 'variant' || typeof document === 'undefined') return;
    if (parseCartOfferArm(typeof window !== 'undefined' && window.location && window.location.search) !== 'variant') {
      return;
    }
    var sel = ['[data-cart-trigger]', 'a[href="/cart"]', 'a[href^="/cart?"]'];
    sel.forEach(function (q) {
      document.querySelectorAll(q).forEach(function (el) {
        var href = el.getAttribute('href');
        if (!href || el.dataset.cartOfferDecorated === '1') return;
        if (href.indexOf('/checkout') !== -1) return;
        var next = hrefWithOfferArm(href, 'variant');
        if (next && next !== href) {
          el.setAttribute('href', next);
        }
        el.dataset.cartOfferDecorated = '1';
      });
    });
  }

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

  function normalizeColorLabel(raw) {
    var s = String(raw || '')
      .toLowerCase()
      .replace(/[·•/]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
    s = s.replace(/\blight\s*grey\b/g, 'light grey');
    s = s.replace(/\bdark\s*grey\b/g, 'dark grey');
    s = s.replace(/\blightgrey\b/g, 'light grey');
    s = s.replace(/\bdarkgrey\b/g, 'dark grey');
    return s;
  }

  function extractColorFromLineItem(item) {
    if (!item) return '';
    var vt = String(item.variant_title || item.title || '');
    if (vt.indexOf('/') !== -1) {
      var parts = vt.split('/');
      if (parts.length >= 2) return parts[parts.length - 1].trim();
    }
    if (vt.indexOf('·') !== -1) {
      return vt.split('·')[0].trim();
    }
    var opts = item.options_with_values || item.options || [];
    if (Array.isArray(opts)) {
      for (var i = 0; i < opts.length; i++) {
        var o = opts[i];
        if (o && String(o.name || '').toLowerCase().indexOf('color') !== -1) {
          return o.value || '';
        }
      }
    }
    return '';
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
    var closedNeedle = ['closed sole', 'closed-sole'];
    return (
      needlesMatch(title, closedNeedle) ||
      needlesMatch(handle, ['closed-sole', config.closedSoleProductHandle]) ||
      needlesMatch(productType, closedNeedle) ||
      handle === String(config.closedSoleProductHandle || '').toLowerCase()
    );
  }

  function isPerformanceSkin(item, config) {
    if (isEligiblePant(item, config)) return false;
    var handle = itemHandle(item);
    var openH = String(config.openSoleProductHandle || '').toLowerCase();
    var closedH = String(config.closedSoleProductHandle || '').toLowerCase();
    if (openH && handle === openH) return true;
    if (closedH && handle === closedH) return true;
    var handles = parseNeedles(config.skinHandleNeedles);
    var titles = parseNeedles(config.skinTitleNeedles);
    var title = (item.product_title || item.title || '') + ' ' + (item.variant_title || '');
    var productType = item.product_type || '';
    var matchesSkin =
      needlesMatch(handle, handles) ||
      needlesMatch(title, titles) ||
      needlesMatch(productType, titles);
    if (!matchesSkin) return false;
    if (config.skinRequireClosedSole) {
      return isClosedSoleSkin(item, config);
    }
    return true;
  }

  function colorsUsedInCart(items, config) {
    var used = {};
    var list = items || [];
    for (var i = 0; i < list.length; i++) {
      if (!isPerformanceSkin(list[i], config)) continue;
      var c = extractColorFromLineItem(list[i]);
      if (c) used[normalizeColorLabel(c)] = true;
    }
    return used;
  }

  function optionIndexByName(options, namePart) {
    namePart = String(namePart || '').toLowerCase();
    for (var i = 0; i < (options || []).length; i++) {
      if (String(options[i].name || '').toLowerCase().indexOf(namePart) !== -1) {
        return options[i].position || i + 1;
      }
    }
    return 0;
  }

  function colorValuesForProduct(product, usedColors) {
    var options = product.options || [];
    var colorPos = optionIndexByName(options, 'color');
    if (!colorPos) return { colors: [], colorKey: 'option2' };
    var colorKey = 'option' + colorPos;
    var opt = null;
    for (var i = 0; i < options.length; i++) {
      if ((options[i].position || i + 1) === colorPos) opt = options[i];
    }
    var values = (opt && opt.values) || [];
    var out = [];
    var used = usedColors || {};
    for (var j = 0; j < values.length; j++) {
      var norm = normalizeColorLabel(values[j]);
      if (!used[norm]) out.push(values[j]);
    }
    return { colors: out, colorKey: colorKey, sizeKey: colorPos === 1 ? 'option2' : 'option1' };
  }

  function sizesForColor(variants, colorKey, colorValue, sizeKey) {
    var sizes = [];
    var seen = {};
    for (var i = 0; i < (variants || []).length; i++) {
      var v = variants[i];
      if (v[colorKey] !== colorValue) continue;
      var sizeVal = v[sizeKey];
      if (!sizeVal || seen[sizeVal]) continue;
      var available = v.available !== false;
      seen[sizeVal] = true;
      sizes.push({ value: sizeVal, available: available, variant: v });
    }
    return sizes;
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

  function computeBundlePromoControl(cartItems, rawConfig, cartTotalCents) {
    var config = controlConfigForArm(rawConfig);
    var items = cartItems || [];

    if (!config.enabled) {
      return { enabled: false, showPanel: false, totalSavingsCents: 0, offerArm: 'control' };
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
    var subtotalCents =
      typeof cartTotalCents === 'number' ? cartTotalCents : skin.subtotalCents + pants.subtotalCents;
    var estimatedTotalCents = Math.max(0, subtotalCents - totalSavingsCents);
    var afterPairOnlyCents = Math.max(0, subtotalCents - pairSavingsCents);

    var nudge =
      config.pairPromoMode === 'future_tiers' && skin.quantity > 0
        ? nudgeCopy(skin.quantity, config)
        : '';
    var footwearPct =
      config.pairPromoMode === 'live_2for15' ? config.livePairPercent : config.tierTwoPercent;
    var footwearOfferLine =
      skin.quantity > 0
        ? fillTemplate(
            config.footwearOfferTemplate || 'Buy 2+ Closed Sole pairs. Save {{percent}}%.',
            { percent: footwearPct }
          )
        : '';
    var savingsLine =
      totalSavingsCents > 0
        ? fillTemplate(config.savingsTemplate, { amount: formatMoney(totalSavingsCents) })
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
      offerArm: 'control',
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
      savingsLine: savingsLine,
      showAddPairStage: false,
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

  function computeBundlePromoVariant(cartItems, rawConfig, cartTotalCents) {
    var config = mergeConfig(rawConfig);
    var items = cartItems || [];

    if (!config.enabled) {
      return { enabled: false, showPanel: false, totalSavingsCents: 0, offerArm: 'variant' };
    }

    var skin = sumEligible(items, function (item) {
      return isPerformanceSkin(item, config);
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
    var subtotalCents =
      typeof cartTotalCents === 'number' ? cartTotalCents : skin.subtotalCents + pants.subtotalCents;
    var estimatedTotalCents = Math.max(0, subtotalCents - totalSavingsCents);
    var afterPairOnlyCents = Math.max(0, subtotalCents - pairSavingsCents);

    var nudge =
      config.pairPromoMode === 'future_tiers' && skin.quantity > 0
        ? nudgeCopy(skin.quantity, config)
        : '';
    var footwearPct =
      config.pairPromoMode === 'live_2for15' ? config.livePairPercent : config.tierTwoPercent;
    var showAddPairStage = skin.quantity === 1 && pants.quantity === 0;
    var showPantsOffer = skin.quantity >= config.pantsMinPairs && pants.quantity === 0;
    var pantsPickerVisible = showPantsOffer;
    var pantsQualOnly = false;

    var footwearOfferLine = '';
    if (skin.quantity >= config.pantsMinPairs) {
      footwearOfferLine = fillTemplate(
        config.footwearOfferTemplate || 'Buy 2+ pairs of Performance Skins. Save {{percent}}%.',
        { percent: footwearPct }
      );
    }

    var savingsLine =
      totalSavingsCents > 0
        ? fillTemplate(config.savingsTemplate, { amount: formatMoney(totalSavingsCents) })
        : '';

    var qualNote = '';
    var pantsTemplate = config.pantsOfferTemplate || config.pantsHeadline;
    var pantsOfferLine = fillTemplate(pantsTemplate, { percent: config.pantsPercent });

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
      offerArm: 'variant',
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
      savingsLine: savingsLine,
      showAddPairStage: showAddPairStage,
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
      addPairHeadline: config.addPairHeadline,
      config: config
    };
  }

  function computeBundlePromo(cartItems, rawConfig, cartTotalCents, opts) {
    var arm = resolveOfferArm(opts || {});
    if (arm === 'variant') {
      return computeBundlePromoVariant(cartItems, rawConfig, cartTotalCents);
    }
    return computeBundlePromoControl(cartItems, rawConfig, cartTotalCents);
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderPromoHtmlControl(result) {
    if (!result || !result.showPanel) return '';

    var html =
      '<div class="cart-bundle-promo" data-cart-bundle-promo data-offer-arm="control" role="region" aria-label="Cart bundle preview — not checkout pricing">';
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
      html +=
        '<div class="cart-bundle-promo__savings"><span class="cart-bundle-promo__preview-tag">Preview</span> ' +
        '<span>' +
        escapeHtml(result.savingsLine) +
        '</span></div>';
    }

    if (result.showPantsOffer) {
      var cfg = result.config;
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
        ' <span class="cart-bundle-promo__preview-tag">preview</span></strong>' +
        '</div></div>';
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

  function renderPromoHtmlVariant(result) {
    if (!result || !result.showPanel) return '';

    var html =
      '<div class="cart-bundle-promo cart-bundle-promo--variant" data-cart-bundle-promo data-offer-arm="variant" role="region" aria-label="Cart bundle preview — not checkout pricing">';
    html +=
      '<p class="cart-bundle-promo__notice">' + escapeHtml(result.previewNotice) + '</p>';

    if (result.pairCount > 0) {
      html +=
        '<p class="cart-bundle-promo__pair-count" data-bundle-pair-count>Performance Skin pairs in cart: ' +
        escapeHtml(String(result.pairCount)) +
        '</p>';
    }

    if (result.showAddPairStage) {
      var cfg = result.config;
      html +=
        '<p class="cart-bundle-promo__cross-sell-label" id="cart-bundle-add-pair-label">Recommended add-on (inline)</p>';
      html +=
        '<div class="cart-bundle-promo__add-pair" data-bundle-add-pair role="group" aria-labelledby="cart-bundle-add-pair-label">';
      html +=
        '<p class="cart-bundle-promo__add-pair-headline">' +
        escapeHtml(result.addPairHeadline || cfg.addPairHeadline) +
        '</p>';
      html += '<div class="cart-bundle-promo__sole-row">';
      html +=
        '<button type="button" class="cart-bundle-promo__sole-btn" data-sole-choice="open">' +
        escapeHtml(cfg.openSoleAddLabel) +
        '</button>';
      html +=
        '<button type="button" class="cart-bundle-promo__sole-btn" data-sole-choice="closed">' +
        escapeHtml(cfg.closedSoleAddLabel) +
        '</button>';
      html += '</div>';
      html +=
        '<div class="cart-bundle-promo__add-pair-picker" data-add-pair-picker hidden>' +
        '<p class="cart-bundle-promo__add-pair-status" data-add-pair-status hidden></p>' +
        '<div class="cart-bundle-promo__add-pair-selects" data-add-pair-selects></div>' +
        '<button type="button" class="cart-bundle-promo__add-pair-submit" data-bundle-add-skin-pair disabled>' +
        escapeHtml(cfg.addPairSubmitLabel) +
        '</button>' +
        '</div></div>';
    }

    if (result.footwearOfferLine) {
      html +=
        '<p class="cart-bundle-promo__footwear-offer">' + escapeHtml(result.footwearOfferLine) + '</p>';
    }

    if (result.nudge) {
      html += '<div class="cart-bundle-promo__progress">' + escapeHtml(result.nudge) + '</div>';
    }

    if (result.savingsLine) {
      html +=
        '<div class="cart-bundle-promo__savings"><span class="cart-bundle-promo__preview-tag">Preview</span> ' +
        '<span>' +
        escapeHtml(result.savingsLine) +
        '</span></div>';
    }

    if (result.showPantsOffer) {
      var cfgP = result.config;
      html +=
        '<p class="cart-bundle-promo__cross-sell-label" id="cart-bundle-pants-label">Optional add-on (inline, preview)</p>';
      html += '<div class="cart-bundle-promo__pants" role="group" aria-labelledby="cart-bundle-pants-label">';
      html += '<p class="cart-bundle-promo__pants-headline">' + escapeHtml(result.pantsOfferLine) + '</p>';
      html +=
        '<div class="cart-bundle-promo__pants-row">' +
        '<img src="' +
        escapeHtml(cfgP.pantsImageUrl) +
        '" alt="" width="56" height="56" loading="lazy" class="cart-bundle-promo__pants-img" />' +
        '<div class="cart-bundle-promo__pants-copy">' +
        '<span class="cart-bundle-promo__pants-title">' +
        escapeHtml(cfgP.pantsProductTitle) +
        '</span>' +
        '</div>' +
        '<div class="cart-bundle-promo__pants-prices">' +
        '<span class="cart-bundle-promo__pants-was">' +
        formatMoney(result.pantsWasCents) +
        '</span>' +
        '<strong class="cart-bundle-promo__pants-sale">' +
        formatMoney(result.pantsSaleCents) +
        ' <span class="cart-bundle-promo__preview-tag">preview</span></strong>' +
        '</div></div>';
      if (result.pantsPickerVisible) {
        html +=
          '<div class="cart-bundle-promo__pants-picker" data-bundle-pants-picker hidden>' +
          '<div class="cart-bundle-promo__pants-selects" data-pants-selects></div>' +
          '<button type="button" class="cart-bundle-promo__pants-add" data-bundle-add-pant disabled>' +
          escapeHtml(cfgP.pantsAddLabel) +
          '</button>' +
          '<a class="cart-bundle-promo__pants-link" data-pants-fallback href="' +
          escapeHtml(cfgP.pantsProductUrl || '/products/' + (cfgP.pantsProductHandle || '')) +
          '">Choose on product page</a>' +
          '</div>';
      }
      html += '</div>';
    }

    html +=
      '<p class="cart-bundle-promo__disclaimer">' + escapeHtml(result.disclaimer) + '</p></div>';
    return html;
  }

  function renderPromoHtml(result) {
    if (!result || !result.showPanel) return '';
    if (result.offerArm === 'variant') return renderPromoHtmlVariant(result);
    return renderPromoHtmlControl(result);
  }

  function defaultFetchProduct(handle) {
    return fetch('/products/' + encodeURIComponent(handle) + '.js', {
      headers: { Accept: 'application/json' }
    }).then(function (res) {
      if (!res.ok) throw new Error('product-js-failed');
      return res.json();
    });
  }

  function defaultAddToCart(variantId) {
    if (typeof window !== 'undefined' && window.BarreleticsCart && window.BarreleticsCart.add) {
      return window.BarreleticsCart.add(variantId, 1);
    }
    return Promise.reject(new Error('cart-add-unavailable'));
  }

  function initAddPairFlow(root, config, cartItems) {
    var block = root.querySelector('[data-bundle-add-pair]');
    if (!block) return;
    var picker = block.querySelector('[data-add-pair-picker]');
    var selectsWrap = block.querySelector('[data-add-pair-selects]');
    var statusEl = block.querySelector('[data-add-pair-status]');
    var submitBtn = block.querySelector('[data-bundle-add-skin-pair]');
    var usedColors = colorsUsedInCart(cartItems, config);
    var state = {
      handle: null,
      product: null,
      variants: [],
      colorKey: 'option2',
      sizeKey: 'option1',
      selected: {},
      pending: false
    };

    function setStatus(msg, isError) {
      if (!statusEl) return;
      if (!msg) {
        statusEl.hidden = true;
        statusEl.textContent = '';
        return;
      }
      statusEl.hidden = false;
      statusEl.textContent = msg;
      statusEl.classList.toggle('is-error', !!isError);
    }

    function setSoleActive(sole) {
      block.querySelectorAll('[data-sole-choice]').forEach(function (btn) {
        var on = btn.getAttribute('data-sole-choice') === sole;
        btn.classList.toggle('is-active', on);
        btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
    }

    function clearPicker() {
      state.product = null;
      state.variants = [];
      state.selected = {};
      if (selectsWrap) selectsWrap.innerHTML = '';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.removeAttribute('data-variant-id');
      }
    }

    function renderPicker(product) {
      var meta = colorValuesForProduct(product, usedColors);
      if (!meta.colors.length) {
        setStatus('No other colors available for this sole type.', true);
        if (picker) picker.hidden = true;
        return;
      }
      setStatus('');
      if (picker) picker.hidden = false;
      if (!selectsWrap) return;
      selectsWrap.innerHTML = '';
      state.colorKey = meta.colorKey;
      state.sizeKey = meta.sizeKey;

      var colorSel = document.createElement('select');
      colorSel.className = 'cart-bundle-promo__add-pair-select';
      colorSel.setAttribute('aria-label', 'Color');
      var colorPh = document.createElement('option');
      colorPh.value = '';
      colorPh.textContent = 'Choose color';
      colorPh.disabled = true;
      colorPh.selected = true;
      colorSel.appendChild(colorPh);
      meta.colors.forEach(function (c) {
        var o = document.createElement('option');
        o.value = c;
        o.textContent = c;
        colorSel.appendChild(o);
      });

      var sizeSel = document.createElement('select');
      sizeSel.className = 'cart-bundle-promo__add-pair-select';
      sizeSel.setAttribute('aria-label', 'Size');
      sizeSel.disabled = true;
      function sizePlaceholder() {
        var ph = document.createElement('option');
        ph.value = '';
        ph.textContent = 'Choose size';
        ph.disabled = true;
        ph.selected = true;
        return ph;
      }
      sizeSel.appendChild(sizePlaceholder());

      function syncSubmit() {
        if (!submitBtn) return;
        if (!state.selected.color || !state.selected.size) {
          submitBtn.disabled = true;
          submitBtn.removeAttribute('data-variant-id');
          return;
        }
        var match = null;
        for (var i = 0; i < state.variants.length; i++) {
          var v = state.variants[i];
          if (v[state.colorKey] === state.selected.color && v[state.sizeKey] === state.selected.size) {
            match = v;
            break;
          }
        }
        if (match && match.available !== false && match.id) {
          submitBtn.disabled = false;
          submitBtn.setAttribute('data-variant-id', String(match.id));
          setStatus('');
        } else if (match && match.available === false) {
          submitBtn.disabled = true;
          submitBtn.removeAttribute('data-variant-id');
          setStatus('That size is out of stock.', true);
        } else {
          submitBtn.disabled = true;
          submitBtn.removeAttribute('data-variant-id');
        }
      }

      colorSel.addEventListener('change', function () {
        state.selected.color = colorSel.value || '';
        state.selected.size = '';
        sizeSel.innerHTML = '';
        sizeSel.appendChild(sizePlaceholder());
        sizeSel.disabled = !state.selected.color;
        if (!state.selected.color) {
          syncSubmit();
          return;
        }
        var sizes = sizesForColor(state.variants, state.colorKey, state.selected.color, state.sizeKey);
        sizes.forEach(function (row) {
          var o = document.createElement('option');
          o.value = row.value;
          o.textContent = row.available ? row.value : row.value + ' (out of stock)';
          o.disabled = !row.available;
          sizeSel.appendChild(o);
        });
        syncSubmit();
      });

      sizeSel.addEventListener('change', function () {
        state.selected.size = sizeSel.value || '';
        syncSubmit();
      });

      selectsWrap.appendChild(colorSel);
      selectsWrap.appendChild(sizeSel);
      syncSubmit();
    }

    function loadProduct(handle, sole) {
      if (state.pending) return;
      state.handle = handle;
      setSoleActive(sole);
      clearPicker();
      setStatus('Loading…', false);
      if (picker) picker.hidden = true;
      var fetchFn = config.fetchProductJson || defaultFetchProduct;
      state.pending = true;
      block.querySelectorAll('[data-sole-choice]').forEach(function (b) {
        b.disabled = true;
      });
      fetchFn(handle)
        .then(function (data) {
          var product = data.product || data;
          state.product = product;
          state.variants = product.variants || [];
          if (!state.variants.length) throw new Error('no-variants');
          renderPicker(product);
        })
        .catch(function () {
          setStatus('Could not load product options. Try again.', true);
        })
        .finally(function () {
          state.pending = false;
          block.querySelectorAll('[data-sole-choice]').forEach(function (b) {
            b.disabled = false;
          });
        });
    }

    block.querySelectorAll('[data-sole-choice]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (state.pending) return;
        var sole = btn.getAttribute('data-sole-choice');
        var handle =
          sole === 'open' ? config.openSoleProductHandle : config.closedSoleProductHandle;
        if (!handle) return;
        loadProduct(handle, sole);
      });
    });

    if (submitBtn && !submitBtn.dataset.boundAddPair) {
      submitBtn.dataset.boundAddPair = 'true';
      submitBtn.addEventListener('click', function () {
        if (submitBtn.disabled || state.pending) return;
        var vid = parseInt(submitBtn.getAttribute('data-variant-id'), 10);
        if (!vid) return;
        state.pending = true;
        submitBtn.disabled = true;
        var prev = submitBtn.textContent;
        submitBtn.textContent = 'Adding…';
        var addFn = config.addToCartFn || defaultAddToCart;
        addFn(vid)
          .catch(function () {
            setStatus('Could not add this pair. Try again.', true);
          })
          .finally(function () {
            state.pending = false;
            submitBtn.textContent = prev;
          });
      });
    }
  }

  function mountPromo(container, cartItems, config, cartTotalCents, opts) {
    if (!container) return null;
    var arm = resolveOfferArm(opts || {});
    var result = computeBundlePromo(cartItems, config, cartTotalCents, Object.assign({}, opts, { offerArm: arm }));
    if (!result.showPanel) {
      container.innerHTML = '';
      container.setAttribute('hidden', 'hidden');
      return result;
    }
    container.removeAttribute('hidden');
    container.innerHTML = renderPromoHtml(result);
    if (result.offerArm === 'variant' && result.showAddPairStage) {
      initAddPairFlow(container, mergeConfig(config), cartItems);
    }
    if (result.pantsPickerVisible) {
      initPantsPicker(container, result.config);
    }
    decorateCartOfferNavLinks(arm);
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
      if (selectsWrap) {
        selectsWrap.innerHTML =
          '<p class="cart-bundle-promo__pants-note">Using theme default variant — change in theme settings.</p>';
      }
      return;
    }

    var fetchFn = config.fetchProductJson || defaultFetchProduct;
    fetchFn(handle)
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

  if (typeof document !== 'undefined' && document.readyState !== 'loading') {
    decorateCartOfferNavLinks(resolveOfferArm({}));
  } else if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', function () {
      decorateCartOfferNavLinks(resolveOfferArm({}));
    });
  }

  return {
    CART_OFFER_PARAM: CART_OFFER_PARAM,
    DEFAULTS: DEFAULTS,
    mergeConfig: mergeConfig,
    parseCartOfferArm: parseCartOfferArm,
    resolveOfferArm: resolveOfferArm,
    controlConfigForArm: controlConfigForArm,
    decorateCartOfferNavLinks: decorateCartOfferNavLinks,
    hrefWithOfferArm: hrefWithOfferArm,
    isUnpublishedThemeRole: isUnpublishedThemeRole,
    computeBundlePromo: computeBundlePromo,
    computeBundlePromoControl: computeBundlePromoControl,
    computeBundlePromoVariant: computeBundlePromoVariant,
    renderPromoHtml: renderPromoHtml,
    mountPromo: mountPromo,
    initPantsPicker: initPantsPicker,
    initAddPairFlow: initAddPairFlow,
    resolveVariantFromOptions: resolveVariantFromOptions,
    isClosedSoleSkin: isClosedSoleSkin,
    isPerformanceSkin: isPerformanceSkin,
    isEligiblePant: isEligiblePant,
    normalizeColorLabel: normalizeColorLabel,
    extractColorFromLineItem: extractColorFromLineItem,
    colorsUsedInCart: colorsUsedInCart,
    colorValuesForProduct: colorValuesForProduct,
    sizesForColor: sizesForColor,
    pantsSaleCents: pantsSaleCents
  };
});
