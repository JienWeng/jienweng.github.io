# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Primary: hiring managers and recruiters for full-time product manager roles.** They arrive from a CV, LinkedIn, or an application and need to decide quickly whether Jien Weng can define and deliver product work, then find the CV and contact.
- **Secondary: readers.** People who come for the writing (product decisions, mathematics, statistics, reinforcement learning) or the AI design guide, and return for new notes. Success is reading, following via RSS, and reputation over time; there is no direct ask.
- Research peers and potential consulting clients also visit. They are served by the research and services pages, but they are not what the homepage is optimised for.

## Product Purpose

The personal site of Jien Weng: product manager and researcher working on Web3 payments, business systems, and applied AI. It exists to land a full-time PM role and to build a reputation through published writing. Success means a hiring manager reaches the CV or emails, and readers find and finish notes.

## Positioning

A PM who does the maths. Applied mathematics and research rigour (statistics, stochastic modelling, reinforcement learning, published and under-review papers) applied to product decisions such as defining payment states, settlement criteria, and acceptance criteria. A neighbouring PM portfolio cannot truthfully copy the combination of shipped product delivery and maths/research output.

## Operating Context

- Visitors evaluate from links in applications, the CV, LinkedIn, X, Google Scholar, and ORCID; many arrive on a phone.
- Readers arrive from search, RSS (`/atom.xml`), and shared links to individual notes.
- AI agents read the site through `/llms.txt` and the design guide's `/design/llms.txt`.

## Capabilities and Constraints

- Static site built with Zola (Tera templates), deployed to GitHub Pages from `main` via `.github/workflows/deploy.yml`. KaTeX loads per page for maths; remark.js for slides; giscus comments; GoatCounter analytics.
- Content sections: projects, writing (notes and blog), publications, CV, slides, about, now, services, colophon, and the Design Guide for AI (`/design/`).
- **Client confidentiality:** publish only what is already public. No internal metrics, client data, or business details beyond the published case studies (CryptoRails, Quandatics CRM). Case studies already state that product-specific details remain confidential.

## Brand Commitments

- Name: Jien Weng. Role line in use: "Product Manager & Researcher".
- **Voice:** plain, first person ("I"), factual. No hype or sales language.
- **Diagrams as evidence:** hand-drawn Excalidraw-style diagrams (Excalifont) are the main way work is shown, e.g. the CryptoRails deposit-to-settlement flow and the CRM deal-to-cash flow.

## Evidence on Hand

- Case studies: `content/blog/product-manager-between-business-and-delivery.md` (CryptoRails payments), `content/blog/quandatics-crm-business-transformation.md` (CRM).
- Diagrams: `static/img/projects/cryptorails-deposit-flow-excalidraw.svg`, `static/img/blog/quandatics/deal-to-cash-excalidraw.svg`.
- Projects: `content/projects/items.toml` (VideoFlow, PolyArb, Monash Water Platform, and others), with media under `static/img/projects/`.
- Research: three papers in `content/cv/publication.toml` (one published on SSRN, one under review, one in manuscript resubmission). Statuses must be shown as recorded, never upgraded.
- CV data: `content/cv/*.toml` (experience, education, awards, certifications, grants, volunteering, open source).
- Portrait: `static/img/profile.webp`. Now page dated in `content/now.md`.
- Absent and not to be fabricated: testimonials, client logos, quantified business outcomes, and employer endorsements.

## Product Principles

1. **Lead with the decision, not the title.** Show the specific product decisions made (what counts as a completed payment, why build a CRM internally) rather than claiming skills.
2. **Rigour is the differentiator.** Let the maths and research show up as precision in how work is presented, not as decoration.
3. **Evidence over claims.** Every statement links to a case study, diagram, paper, or note; confidential work is described at the level already published.
4. **Two paths, one page.** Hiring managers reach the CV and email within seconds; readers reach the writing just as easily.
5. **Plain words.** Write as Jien speaks: first person, specific, no hype.
