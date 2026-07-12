/* global React, ReactDOM */
const { useEffect } = React;

const PDP_TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "quickAddMode": "hover",
  "showVerifiedBadge": true,
  "cardStyle": "clean",
  "ctaSize": "default"
}/*EDITMODE-END*/;

function PdpTweaks() {
  const [t, setTweak] = useTweaks(PDP_TWEAK_DEFAULTS);

  useEffect(() => {
    const root = document.documentElement;
    root.dataset.quickAdd = t.quickAddMode;
    root.dataset.verified = t.showVerifiedBadge ? 'on' : 'off';
    root.dataset.cardStyle = t.cardStyle;
    root.dataset.ctaSize = t.ctaSize;
  }, [t]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Variant grid · Quick Add">
        <TweakRadio
          label="Quick Add behavior"
          value={t.quickAddMode}
          onChange={v => setTweak('quickAddMode', v)}
          options={[
            { value: 'off',    label: 'Off' },
            { value: 'hover',  label: 'On hover' },
            { value: 'always', label: 'Always' },
          ]}
        />
        <TweakRadio
          label="Card style"
          value={t.cardStyle}
          onChange={v => setTweak('cardStyle', v)}
          options={[
            { value: 'clean',  label: 'Clean' },
            { value: 'bordered',label: 'Bordered' },
          ]}
        />
      </TweakSection>

      <TweakSection label="Reviews">
        <TweakToggle
          label="Show 'Verified buyer' badge"
          value={t.showVerifiedBadge}
          onChange={v => setTweak('showVerifiedBadge', v)}
        />
      </TweakSection>

      <TweakSection label="Primary CTA">
        <TweakRadio
          label="Button size"
          value={t.ctaSize}
          onChange={v => setTweak('ctaSize', v)}
          options={[
            { value: 'compact', label: 'Compact' },
            { value: 'default', label: 'Default' },
            { value: 'bold',    label: 'Bold' },
          ]}
        />
      </TweakSection>
    </TweaksPanel>
  );
}

ReactDOM.createRoot(document.getElementById('pdp-tweaks-root')).render(<PdpTweaks />);
