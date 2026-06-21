/* global React, ReactDOM */
/* Tweaks panel — global type / CTA system toggles for the audit doc */

const { useState, useEffect } = React;

const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "displayWeight": 400,
  "headlineCase": "sentence",
  "bodyScale": 1.0,
  "ctaSize": "default",
  "ctaCase": "uppercase",
  "ctaRadius": 0,
  "palette": "brand",
  "showAuditChrome": true
}/*EDITMODE-END*/;

function AuditTweaks() {
  const [t, setTweak] = useTweaks(TWEAK_DEFAULTS);

  /* Apply tweaks to CSS variables */
  useEffect(() => {
    const r = document.documentElement;
    r.style.setProperty('--t-body', (16 * t.bodyScale) + 'px');
    r.style.setProperty('--t-body-lg', (18 * t.bodyScale) + 'px');

    const sizes = {
      compact: { y: '11px', x: '22px', f: '13px' },
      default: { y: '14px', x: '28px', f: '14px' },
      bold:    { y: '17px', x: '34px', f: '15px' },
    };
    const s = sizes[t.ctaSize] || sizes.default;
    r.style.setProperty('--btn-pad-y', s.y);
    r.style.setProperty('--btn-pad-x', s.x);
    r.style.setProperty('--btn-text-size', s.f);
    r.style.setProperty('--btn-radius', t.ctaRadius + 'px');

    /* CTA case */
    document.querySelectorAll('.br-btn').forEach(b => {
      b.style.textTransform = t.ctaCase;
      b.style.letterSpacing = t.ctaCase === 'uppercase' ? '0.06em' : '0.02em';
    });

    /* Headline case */
    document.querySelectorAll('.br-display, .br-h1, .br-h2').forEach(h => {
      h.style.textTransform = t.headlineCase === 'uppercase' ? 'uppercase' : 'none';
      h.style.letterSpacing = t.headlineCase === 'uppercase' ? '0.02em' : '-0.015em';
    });

    /* Display weight */
    document.querySelectorAll('.br-display, .br-h1').forEach(h => {
      h.style.fontWeight = t.displayWeight;
    });

    /* Audit chrome */
    document.querySelectorAll('.au-chrome').forEach(el => {
      el.style.display = t.showAuditChrome ? '' : 'none';
    });
  }, [t]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Typography">
        <TweakRadio
          label="Headline case"
          value={t.headlineCase}
          onChange={v => setTweak('headlineCase', v)}
          options={[
            { value: 'sentence', label: 'Sentence' },
            { value: 'uppercase', label: 'Uppercase' },
          ]}
        />
        <TweakSelect
          label="Display weight"
          value={t.displayWeight}
          onChange={v => setTweak('displayWeight', Number(v))}
          options={[
            { value: 300, label: 'Light · 300' },
            { value: 400, label: 'Regular · 400' },
            { value: 500, label: 'Medium · 500' },
            { value: 700, label: 'Bold · 700' },
          ]}
        />
        <TweakSlider
          label="Body scale"
          min={0.9} max={1.15} step={0.05}
          value={t.bodyScale}
          onChange={v => setTweak('bodyScale', v)}
          unit="x"
        />
      </TweakSection>

      <TweakSection label="Call-to-action">
        <TweakRadio
          label="CTA size"
          value={t.ctaSize}
          onChange={v => setTweak('ctaSize', v)}
          options={[
            { value: 'compact', label: 'Compact' },
            { value: 'default', label: 'Default' },
            { value: 'bold',    label: 'Bold' },
          ]}
        />
        <TweakRadio
          label="CTA case"
          value={t.ctaCase}
          onChange={v => setTweak('ctaCase', v)}
          options={[
            { value: 'uppercase', label: 'Uppercase' },
            { value: 'none',      label: 'Sentence' },
          ]}
        />
        <TweakSlider
          label="CTA radius"
          min={0} max={24} step={2}
          value={t.ctaRadius}
          onChange={v => setTweak('ctaRadius', v)}
          unit="px"
        />
      </TweakSection>

      <TweakSection label="Audit view">
        <TweakToggle
          label="Show audit chrome"
          value={t.showAuditChrome}
          onChange={v => setTweak('showAuditChrome', v)}
        />
      </TweakSection>
    </TweaksPanel>
  );
}

ReactDOM.createRoot(document.getElementById('tweaks-root')).render(<AuditTweaks />);
