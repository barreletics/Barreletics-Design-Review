(function () {
  'use strict';

  var M = window.BarreleticsMockCart;
  var state = M.initialState();

  function el(sel) {
    return document.querySelector(sel);
  }

  function money(n) {
    return '$' + (n * 74).toFixed(2).replace(/\.00$/, '');
  }

  function subtotal() {
    var base = M.pairCount(state) * 74;
    var pants = state.pants ? 89 : 0;
    return base + pants;
  }

  function renderLines() {
    var lines = state.pairs.map(function (p, i) {
      return (
        '<li class="cart-line" data-idx="' +
        i +
        '"><span class="cart-line__name">' +
        escape(p.label) +
        '</span><span class="cart-line__meta">' +
        escape(p.size) +
        ' · illustrative</span><span class="cart-line__price">' +
        money(1) +
        '</span></li>'
      );
    });
    if (state.pants) {
      lines.push(
        '<li class="cart-line cart-line--pants"><span class="cart-line__name">Yoga Pant</span>' +
          '<span class="cart-line__meta">illustrative</span><span class="cart-line__price">$89</span></li>'
      );
    }
    return lines.join('');
  }

  function escape(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;');
  }

  function isSoftCard() {
    return document.body && document.body.getAttribute('data-design') === 'soft-card';
  }

  var SWATCH_HEX = {
    Black: '#1c1916',
    White: '#f3f3f1',
    Coral: '#e8847c',
    'Rivian Green': '#5a7a6a',
    'Dusty Blue': '#8aa4b8',
    Purple: '#6b4c8a',
    'Deep Teal': '#2d5a5a',
    'Bright Yellow': '#e8c547'
  };

  function soleLabel(sole) {
    if (isSoftCard()) return sole === 'open' ? 'Open Sole' : 'Closed Sole';
    return M.CATALOG[sole].label;
  }

  function renderColorField(colors) {
    if (isSoftCard()) {
      var html =
        '<div class="offer__field"><span class="offer__field-label">Color</span>' +
        '<div class="offer__swatch-row" role="listbox" aria-label="Color">';
      colors.forEach(function (c) {
        var on = state.pick.color === c;
        var hex = SWATCH_HEX[c] || '#ccc';
        html +=
          '<button type="button" class="offer__swatch' +
          (on ? ' is-active' : '') +
          '" role="option" aria-label="' +
          escape(c) +
          '" aria-selected="' +
          (on ? 'true' : 'false') +
          '" data-swatch-color="' +
          escape(c) +
          '" style="background:' +
          hex +
          '"><span class="visually-hidden">' +
          escape(c) +
          '</span></button>';
      });
      html += '</div>';
      if (state.pick.color) {
        html += '<p class="offer__swatch-name">' + escape(state.pick.color) + '</p>';
      }
      html += '</div>';
      return html;
    }
    var sel =
      '<label class="offer__field">Color<select data-color><option value="">Choose color</option>';
    colors.forEach(function (c) {
      sel +=
        '<option value="' +
        escape(c) +
        '"' +
        (state.pick.color === c ? ' selected' : '') +
        '>' +
        escape(c) +
        '</option>';
    });
    sel += '</select></label>';
    return sel;
  }

  function addPairButtonLabel() {
    return isSoftCard() ? 'Add pair' : 'Add to cart (simulated)';
  }

  function renderOffer() {
    var st = M.stage(state);
    var html = '';
    if (st === 'add-pair') {
      html += '<section class="offer offer--benefit-first" aria-live="polite">';
      html += '<p class="offer__notice">' + escape(M.NOTICE) + '</p>';
      html += '<h2 class="offer__headline">Buy 2 or more pairs. Get 15% off.</h2>';
      var n = M.pairCount(state);
      html +=
        '<p class="offer__support">You have ' +
        n +
        ' pair' +
        (n === 1 ? '' : 's') +
        '. Add another to qualify.</p>';
      if (!state.addPickerOpen) {
        html +=
          '<button type="button" class="offer__submit" data-open-add-pickers>Add another pair</button>';
      } else {
        html += '<div class="offer__pickers-wrap" data-pickers-wrap>';
        html += '<div class="offer__sole-row offer__sole-row--pills">';
        ['open', 'closed'].forEach(function (sole) {
          var on = state.pick.sole === sole;
          html +=
            '<button type="button" class="offer__sole-btn offer__sole-btn--pill' +
            (on ? ' is-active' : '') +
            '" data-sole="' +
            sole +
            '">' +
            escape(soleLabel(sole)) +
            '</button>';
        });
        html += '</div>';
        if (state.pick.sole) {
          var colors = M.availableColors(state, state.pick.sole);
          html += '<div class="offer__pickers">';
          if (!colors.length) {
            html +=
              '<p class="offer__status offer__status--warn">No illustrative colors in fixture for this sole.</p>';
          } else {
            html += renderColorField(colors);
            html += '<label class="offer__field">Size<select data-size' + (state.pick.color ? '' : ' disabled') + '>';
            html += '<option value="">Choose size</option>';
            if (state.pick.color) {
              M.CATALOG[state.pick.sole].sizes.forEach(function (sz) {
                html +=
                  '<option value="' +
                  escape(sz) +
                  '"' +
                  (state.pick.size === sz ? ' selected' : '') +
                  '>' +
                  escape(sz) +
                  '</option>';
              });
            }
            html += '</select></label>';
            html +=
              '<button type="button" class="offer__submit offer__submit--add-pair" data-add-pair' +
              (M.canAddPair(state) ? '' : ' disabled') +
              '>' +
              escape(addPairButtonLabel()) +
              '</button>';
          }
        }
        html += '</div></div>';
      }
      html += '</section>';
    } else if (st === 'pants-offer') {
      html += '<section class="offer offer--stage-two offer--outfit" aria-live="polite">';
      html += '<p class="offer__notice">' + escape(M.NOTICE) + '</p>';
      html += '<h2 class="offer__headline">Complete your outfit.</h2>';
      html += '<p class="offer__support">Get 35% off one pair of yoga pants.</p>';
      html += '<div class="offer__pants">';
      html += '<img src="' + M.PANTS_IMG + '" alt="" width="72" height="72" loading="lazy" />';
      html += '<div><p class="offer__pants-title">Lightly Padded Knee Yoga Pant</p>';
      html += '<p class="offer__pants-price"><s>$98.00</s> <strong>$63.70</strong> <span class="tag">preview</span></p>';
      html += '<p class="offer__fine">Illustrative catalog image · not live stock</p></div></div>';
      html += '<button type="button" class="offer__submit" data-add-pants>Choose yoga pants</button>';
      html += '<button type="button" class="offer__ghost" data-remove-pair>Remove last pair</button>';
      html += '</section>';
    } else {
      html += '<section class="offer">';
      html += '<p class="offer__notice">' + escape(M.NOTICE) + '</p>';
      html += '<p class="offer__done">Simulated cart: 2 pairs + 1 pant. Preview math only.</p>';
      html += '<button type="button" class="offer__ghost" data-reset>Reset demo</button>';
      html += '</section>';
    }
    return html;
  }

  var interactionsBound = false;

  function paint() {
    var root = el('#mock-cart-root');
    if (!root) return;
    el('#cart-lines').innerHTML = renderLines();
    el('#cart-subtotal').textContent = money(subtotal() / 74);
    el('#offer-mount').innerHTML = renderOffer();
    bindInteractionsOnce();
  }

  function bindInteractionsOnce() {
    if (interactionsBound) return;
    interactionsBound = true;
    var root = el('#mock-cart-root');
    if (!root) return;
    root.addEventListener('click', function (e) {
      var t = e.target;
      if (!(t instanceof HTMLElement)) return;
      if (t.matches('[data-open-add-pickers]')) {
        state.addPickerOpen = true;
        paint();
        return;
      }
      if (t.matches('[data-swatch-color]')) {
        state.pick.color = t.getAttribute('data-swatch-color') || '';
        state.pick.size = '';
        paint();
        return;
      }
      if (t.matches('[data-sole]')) {
        state.pick.sole = t.getAttribute('data-sole');
        state.pick.color = '';
        state.pick.size = '';
        paint();
        return;
      }
      if (t.matches('[data-add-pair]')) {
        if (!M.canAddPair(state)) return;
        state = M.addPair(state);
        paint();
        return;
      }
      if (t.matches('[data-remove-pair]')) {
        state = M.removeLastPair(state);
        paint();
        return;
      }
      if (t.matches('[data-add-pants]')) {
        state = M.addPants(state);
        paint();
        return;
      }
      if (t.matches('[data-reset]')) {
        state = M.resetAll();
        paint();
      }
    });
    root.addEventListener('change', function (e) {
      var t = e.target;
      if (!(t instanceof HTMLElement)) return;
      if (t.matches('[data-color]')) {
        state.pick.color = t.value || '';
        state.pick.size = '';
        paint();
      }
      if (t.matches('[data-size]')) {
        state.pick.size = t.value || '';
        paint();
      }
    });
  }

  document.addEventListener('DOMContentLoaded', paint);
  window.__mockCartTestApi = {
    getState: function () {
      return state;
    },
    setState: function (s) {
      state = s;
      paint();
    },
    runAddFlow: function () {
      state.addPickerOpen = true;
      state.pick = { sole: 'open', color: 'Black', size: 'M (W 5.5-7.5)' };
      state = M.addPair(state);
      paint();
    },
    reset: function () {
      state = M.resetAll();
      paint();
    }
  };
})();
