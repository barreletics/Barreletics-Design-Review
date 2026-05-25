/* global React, ReactDOM */
const { useEffect } = React;

const HOME_TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "variantCta": "link",
  "featuredTiles": "compare-color",
  "articleHero": "image-overlay"
}/*EDITMODE-END*/;

function HomeTweaks() {
  const [t, setTweak] = useTweaks(HOME_TWEAK_DEFAULTS);

  useEffect(() => {
    const root = document.documentElement;
    root.dataset.variantCta = t.variantCta;
    root.dataset.featuredTiles = t.featuredTiles;
    root.dataset.articleHero = t.articleHero;
  }, [t]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Variant cards · CTA">
        <TweakRadio
          label="Add to cart"
          value={t.variantCta}
          onChange={v => setTweak('variantCta', v)}
          options={[
            { value: 'off',    label: 'Off' },
            { value: 'link',   label: 'Text link' },
            { value: 'hover',  label: 'On hover' },
            { value: 'always', label: 'Always' },
          ]}
        />
      </TweakSection>

      <TweakSection label="Featured tile strip">
        <TweakSelect
          label="Combo"
          value={t.featuredTiles}
          onChange={v => setTweak('featuredTiles', v)}
          options={[
            { value: 'compare-color', label: 'Compare open/closed + Featured color' },
            { value: 'yoga-color',    label: 'Yoga pant + Featured color' },
            { value: 'le-color',      label: 'Limited edition + Featured color' },
            { value: 'compare-yoga',  label: 'Compare + Yoga pant' },
          ]}
        />
      </TweakSection>

      <TweakSection label="Article hero">
        <TweakRadio
          label="Style"
          value={t.articleHero}
          onChange={v => setTweak('articleHero', v)}
          options={[
            { value: 'image-overlay', label: 'A · Image' },
            { value: 'centered',      label: 'B · Centered' },
          ]}
        />
      </TweakSection>
    </TweaksPanel>
  );
}

ReactDOM.createRoot(document.getElementById('home-tweaks-root')).render(<HomeTweaks />);
