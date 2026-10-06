# Site quality verification - 6 October 2026

## Performance measurements

Lighthouse 13.5.0, local build served at `http://localhost:8766`, Chrome headless, default simulated mobile throttling and the desktop preset. Two measurement processes ran concurrently; scores are indicative local lab results and can vary. The local server has no production compression/cache headers. Third-party production analytics is not exercised from localhost. These are not production field Core Web Vitals or Search Console results.

| Page | Mobile performance | Desktop performance | Mobile LCP |
| --- | ---: | ---: | ---: |
| Home | 99 | 100 | 2.2 s |
| About | 98 | 100 | 2.4 s |
| CV | 99 | 100 | 2.0 s |
| Projects | 97 | 100 | 2.6 s |
| VideoFlow | 99 | 100 | 2.0 s |
| Fokker–Planck article | 96 | 100 | 2.4 s |

All six routes scored 100 for automated accessibility, best practices, and SEO on both device presets. This does not establish complete WCAG compliance or guarantee search rankings.

The initial mobile Projects score was 77 and VideoFlow was 81. Main fixes: replace eagerly loaded screenshot animation with a 75,904-byte real recording, start previews only when visible, pin Archivo's unused width axis (189,340 to 73,456 bytes), and serve compressed Monash screenshots. Preserve normal-width glyphs and variable weights. Native playback on the project page uses `preload="none"` and starts only on request.

Reproduce for each route (omit `--preset=desktop` for mobile):

```sh
npx --yes lighthouse@13.5.0 http://localhost:8766/projects/ \
  --chrome-path=/usr/bin/google-chrome --chrome-flags="--headless --no-sandbox" \
  --only-categories=performance,accessibility,best-practices,seo \
  --preset=desktop --output=json --output-path=/tmp/projects-lighthouse.json
```

## Accessibility and interaction checks

- Browser checks at 1440×900 and 390×844 on Home, About, CV, Projects, VideoFlow, Monash Water, and the Fokker–Planck article: no document overflow or broken images.
- Keyboard: skip link, mobile menu open/Escape/focus restoration, more-work expansion and collapse/focus restoration, diagram opening/Escape/focus restoration, and native video playback.
- Automated syntax contrast failure resolved for code keywords and comments against the warm code-block surface. The article now scores 100 for automated accessibility on both device presets.
- Yappy’s existing GIF now also has a static fallback, pause control, and reduced-motion handling.
- Interaction harness covers offscreen video loading, pause/resume, reduced motion, event whitelisting, local/preview analytics exclusion, and one-time controlled video playback counts.
- PDF: all five pages visually reviewed; section headings stay with their first entry. Text, JSON, and PDF verification covers all 43 CV entries and publication statuses.

```sh
# Use Node 24 or a version supported by jsdom 30.1.2.
npm install --prefix /tmp/portfolio-interaction-check jsdom@30.1.2
NODE_PATH=/tmp/portfolio-interaction-check/node_modules node scripts/check_site_interactions.cjs
python3 scripts/check_public_profile.py
zola build
python3 scripts/check_site_seo.py public
```

Search Console setup is complete according to the user. Live analytics delivery and field performance should be observed after deployment, rather than inferred from these local checks.
