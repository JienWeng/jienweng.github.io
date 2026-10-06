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

90 portfolio pages passed the checks with no issues. Standalone slide decks and redirect documents are outside this check. This is a structural audit, not a Lighthouse score or proof of search rankings.

The initial PageSpeed API attempt was quota-limited. Local Lighthouse measurements are now available in [the quality report](site-quality-2026-10-06.md); the latest follow-up changes remain local until merged and deployed.

## Recommended next work

1. Search Console setup is complete (confirmed by the user). Review impressions, queries, clicks, and indexing over time.
2. Completed: VideoFlow and Monash have individual project pages, linked from Home and Projects, with roles, technical decisions, public outputs, and limitations. VideoFlow now includes a real workflow recording.
3. Build on existing content rather than adding generic keyword pages: internal CRM handoffs, Web3 settlement states, Go/Electron video orchestration, and wastewater monitoring. Add contextual links between case studies and related technical notes.
4. Measure mobile and desktop Lighthouse on Home, About, Projects, CV, and one mathematical article after deployment. Check field Core Web Vitals when enough traffic exists. Prioritize real loading and interaction problems over chasing a perfect score.
5. Completed: use the real 75,904-byte workflow video for visible-only previews and controlled playback, respecting reduced motion; retain the original illustrative GIF as a source asset.
6. Keep project status and publication status current. Add factual outcomes only when supported by public evidence or approved figures. Seek relevant links through project READMEs, published work, and your existing profiles.

Sources:

- https://developers.google.com/search/docs/fundamentals/get-started-developers
- https://developers.google.com/search/docs/appearance/structured-data/profile-page
- https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- https://developers.google.com/search/docs/monitor-debug/search-console-start
- https://web.dev/articles/vitals

## Follow-up completed

Dedicated VideoFlow and Monash Water Platform pages are implemented, linked from the homepage and archive, and included in the generated sitemap. Contextual links connect the payment case studies and CryptoRails technical note; MLOps and VideoFlow link to each other. Google and Bing verification meta tags were already configured. The user confirmed that Search Console setup is complete. Account-side setup is no longer an outstanding task.

## Project keyword and indexing refinement

VideoFlow targets AI video orchestration, Go/SvelteKit, Electron, storyboard workflows, local storage, and FFmpeg. Monash targets wastewater monitoring, CitizenFlood Android reporting, operator dashboards, and Monash University Malaysia research. These terms appear naturally in titles, headings, descriptions, and project content. Project pages include WebPage and breadcrumb structured data, a visible breadcrumb trail, and descriptive incoming links. Updated dates reflect the October 2026 edit. This establishes crawlability and topic signals; it does not confirm Google indexing or rankings.
