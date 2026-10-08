# Draft theme 187144929571 versions, Oct 7 2026 night (pushed from Andrew's Mac via Shopify CLI)

- theme.liquid.pre-tonight-255b4ede: layout/theme.liquid before tonight's typography work
- theme.liquid.tee-pants-fixed-7b725ddb: tee + pants headings restored to Type OS (only features + Made in the USA capped 56/36)
- theme.liquid.current-open-fixed-896714df: CURRENT. Open Sole headings now match Closed Sole (giant-tier override removed; Shop All / Real people / @barreletics / Questions / Built around one obsession back to theme defaults)
- pdp-buy-box.current-4x5-db80f90f.liquid: CURRENT sections/pdp-buy-box.liquid. 4:5 hero frame; square shoe photos contain on #fefefe, apparel cover
- theme.liquid.current-help-fixed-02ceb9a2: CURRENT (10:30 PM ET). Removed #help-heading-unify so /pages/help headings match /pages/returns (H1 44/31, H2 32/24 semibold).
- page-faq.pre-showall-a651aff8.liquid: sections/page-faq.liquid before tonight's FAQ change
- page-faq.showall-2caa2c4d.liquid: CURRENT sections/page-faq.liquid on draft 187144929571 — all FAQ-page questions visible; only geo questions overflow
- theme.liquid.pre-apparel-fabric-02ceb9a2: layout/theme.liquid before Apparel “Fabric that earns its keep” 56/36 (post help fix, 02ceb9a2)
- theme.liquid.apparel-fabric-4f3ff09a: CURRENT layout/theme.liquid — Apparel “Fabric that earns its keep” capped 56/36 (4f3ff09a)
- collection.apparel.pre-hero-img-15a6209f.json: templates/collection.apparel.json before IMG_2914 hero photo (15a6209f)
- collection.apparel.hero-img.json: templates/collection.apparel.json with hero photo IMG_2914 added
- collection.apparel.pre-hero-fit.json: templates/collection.apparel.json after IMG_2914, before 35% column / 720 height fit
- collection.apparel.hero-fit.json: CURRENT templates/collection.apparel.json — hero 35% column, 720 height, natural phone ratio
- collection-hero.pre-phone-e0bac5c7.liquid: sections/collection-hero.liquid before phone ratio for apparel template (e0bac5c7)
- collection-hero.phone-fix.liquid: CURRENT sections/collection-hero.liquid — phone ratio enabled for apparel template (f574eb9b)

Restore any file: copy to the theme path, then `shopify theme push --store barreletics --theme 187144929571 --only <path> --nodelete` and md5 pull-verify.
