# SEO and site quality review · 6 October 2026

Implemented:

- Consistent homepage browser, Open Graph, and Twitter titles using Product Manager & Researcher.
- Specific About, CV, Projects, and homepage descriptions.
- Correct tag/category titles, descriptions, and self-referencing canonical URLs. Previously these 45 archives inherited homepage canonical URLs.
- About ProfilePage schema rather than Article schema; Article markup limited to dated content.
- Person schema aligned with the visible role, portrait, and social profiles.
- Article author links and reading times; corrected breadcrumb positions without repeating Home.
- Noindex on the 404 page.
- Deferred shared JavaScript.
- Social preview converted to a 113 KB JPEG from the previous roughly 1.1 MB PNG; source PNG retained.
- Automated generated-page metadata, JSON-LD, headings, image-alt, and local-link checks before production deployment.

Validation:

```sh
zola build
python3 scripts/check_site_seo.py public
```

88 portfolio pages passed the checks with no issues. Standalone slide decks and redirect documents are outside this check. This is a structural audit, not a Lighthouse score or proof of search rankings.

Performance scores remain unmeasured: the PageSpeed API returned HTTP 429/quota exceeded, and the collaborative browser was unavailable for rendering. Changes are local until deployed.

## Recommended next work

1. Verify the property in Google Search Console, submit `/sitemap.xml`, and inspect Home, About, Projects, and the CRM case study. Review impressions, queries, clicks, and indexing after deployment.
2. Give VideoFlow and Monash individual project pages with real screenshots, your role, technical decisions, and source/live links. Their current detail anchors share one archive URL. Add these pages to the homepage and project archive.
3. Build on existing content rather than adding generic keyword pages: internal CRM handoffs, Web3 settlement states, Go/Electron video orchestration, and wastewater monitoring. Add contextual links between case studies and related technical notes.
4. Measure mobile and desktop Lighthouse on Home, About, Projects, CV, and one mathematical article after deployment. Check field Core Web Vitals when enough traffic exists. Prioritize real loading and interaction problems over chasing a perfect score.
5. Convert the video preview to an efficient animated WebP or muted video after measuring its impact; retain playback controls, reduced-motion fallback, and the original GIF download.
6. Keep project status and publication status current. Add factual outcomes only when supported by public evidence or approved figures. Seek relevant links through project READMEs, published work, and your existing profiles.

Sources:

- https://developers.google.com/search/docs/fundamentals/get-started-developers
- https://developers.google.com/search/docs/appearance/structured-data/profile-page
- https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- https://developers.google.com/search/docs/monitor-debug/search-console-start
- https://web.dev/articles/vitals

## Follow-up completed

Dedicated VideoFlow and Monash Water Platform pages are implemented, linked from the homepage and archive, and included in the generated sitemap. Contextual links connect the payment case studies and CryptoRails technical note; MLOps and VideoFlow link to each other. Google and Bing verification meta tags were already configured. Search Console opened its public landing page, so account-side property verification and sitemap submission were not completed. In Search Console, select the URL-prefix property `https://jienweng.github.io/`, verify using the existing HTML tag, and submit `sitemap.xml` after deployment.

## Project keyword and indexing refinement

VideoFlow targets AI video orchestration, Go/SvelteKit, Electron, storyboard workflows, local storage, and FFmpeg. Monash targets wastewater monitoring, CitizenFlood Android reporting, operator dashboards, and Monash University Malaysia research. These terms appear naturally in titles, headings, descriptions, and project content. Project pages include WebPage and breadcrumb structured data, a visible breadcrumb trail, and descriptive incoming links. Updated dates reflect the October 2026 edit. This establishes crawlability and topic signals; it does not confirm Google indexing or rankings.
