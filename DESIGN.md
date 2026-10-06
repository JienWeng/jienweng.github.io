---
name: Jien Weng Portfolio
description: A practical editorial portfolio with work evidence at its center.
colors:
  paper: "#f6f3ec"
  paper-2: "#eee9df"
  accent-soft: "#eee4da"
  ink: "#35342f"
  ink-soft: "#5f5c54"
  accent: "#875b43"
  rule: "#ddd7cc"
  white: "#ffffff"
typography:
  display:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(3.25rem, 5.3vw, 5rem)"
    fontWeight: 450
    lineHeight: 1.12
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(1.75rem, 3vw, 3rem)"
    fontWeight: 450
    lineHeight: 1.18
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1rem"
    lineHeight: 1.5
  reading:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.0625rem"
    lineHeight: 1.75
  reading-h2:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.65rem"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "-0.025em"
  reading-h3:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 500
    lineHeight: 1.3
  article-title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(1.9rem, 3.4vw, 3.3rem)"
    fontWeight: 450
    lineHeight: 1.16
    letterSpacing: "-0.025em"
  collection-title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 450
    lineHeight: 1.4
  diagram:
    fontFamily: "Excalifont, cursive"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.25
  caption:
    fontFamily: "Archivo, sans-serif"
    fontSize: "0.8125rem"
  reading-meta:
    fontFamily: "Archivo, sans-serif"
    fontSize: "0.875rem"
  back-link:
    fontFamily: "Archivo, sans-serif"
    fontSize: "0.9375rem"
  label:
    fontFamily: "Archivo, sans-serif"
    fontSize: "0.6875rem"
    letterSpacing: "0.08em"
rounded:
  square: "0px"
spacing:
  compact: "12px"
  inset: "20px"
  regular: "24px"
  section: "32px"
  generous: "40px"
components:
  button-primary:
    backgroundColor: "transparent"
    textColor: "{colors.accent}"
    rounded: "{rounded.square}"
    padding: "10px 20px"
  button-primary-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent}"
  project-rail:
    backgroundColor: "transparent"
    textColor: "{colors.ink-soft}"
    padding: "4px 8px 16px"
  workflow:
    padding: "8px 14px 16px"
---

# Design System: Jien Weng Portfolio

## Direction

A quiet editorial portfolio: warm paper, restrained brown accents, readable Archivo typography, and work evidence at its center. The user's October 2026 refinement reduces the heavy type and filled panels across the website while preserving its structure, content, navigation, and square geometry.

Implementation sources are `templates/base.html`, `templates/partials/portfolio-header.html`, `templates/home.html`, `templates/page.html`, `static/site.css`, `static/portfolio.css`, and `static/portfolio.js`. Shared styling covers the homepage, articles, About, CV, services, collections, taxonomies, and error page. Standalone slide decks retain their authored designs.

## Palette

Warm paper (`#f6f3ec`) is the main surface. Ink (`#35342f`) carries text, with soft ink (`#5f5c54`) for supporting information. Muted brown (`#875b43`) is reserved primarily for links and actions. Numbers and headline punctuation use the text palette. Light rules (`#ddd7cc`) separate sections. Accent tint (`#eee4da`) is reserved for selection and hover feedback. Inset paper (`#eee9df`) supports code blocks.

Avoid solid accent panels, black dividers, shadows, and general-purpose decorative fills. Color supports reading order; it does not carry meaning alone.

## Typography

Archivo is self-hosted as a variable WOFF2 font with weights 100–900 and `font-display: swap`. The hero, main section headings, article titles, collection titles, and text actions use weight 450. The wordmark, reading subheadings, and role headings use 500; inline emphasis uses 600; body text uses 400. Hierarchy comes from size and spacing rather than heavy weight.

The hero uses `clamp(3.25rem, 5.3vw, 5rem)`, 1.12 leading, and -0.025em tracking. At 1100px and below it uses `clamp(3rem, 7vw, 4.5rem)`; at 640px and below it uses `clamp(2rem, 8.8vw, 3.25rem)` and 1.1 leading. Mobile headings wrap naturally.

Homepage section headings use `clamp(1.75rem, 3vw, 3rem)` and 1.18 leading, reducing to 1.75rem on phones. Article titles use `clamp(1.9rem, 3.4vw, 3.3rem)` with 1.16 leading and a 30ch maximum. Reading h2 and h3 use 1.65rem and 1.25rem, both at weight 500. Reading prose uses 17px with 1.78 leading, reducing to 16px at 920px and below. The reading measure remains 68ch.

Project annotations and role labels use sentence case with natural spacing; the wordmark remains uppercase. Rail labels use 12px and role labels use 13px for comfortable reading. The hero margin note uses sentence case. Dates, captions, and metadata use their documented roles. Small role-specific sizes in the existing collection and CV layout are intentional.

## Layout

The homepage shell is capped at 100rem with fluid gutters. The hero has 64px top and 56px bottom padding; phones use 40px and 44px. Work sections pair a 110px marker column with an evidence area and use 32px top and 40px bottom padding. Thin rules and generous spacing define the rhythm.

At 1100px and below, the marker column narrows to 70px, evidence stacks, and the hero margin note disappears. At 640px and below, markers become an unfilled horizontal row and content becomes one column with 20px gutters.

Reading and collection shells are capped at 92rem. Desktop uses a minimum 210px, 25% rail and a flexible reading column with a 48px gap. At 920px and below the layout stacks with a 28px gap. Wide tables and equations scroll within the reading column. Article titles span both columns.

The About page uses the existing profile image, displayed in the rail on desktop and above the copy on phones.

## Components and interaction

Primary actions are square outlined links with brown text and a light border. Hover adds an accent tint and brown border. Text links remain underlined, with a 4px arrow movement over 180ms ease-out. Keyboard focus remains a visible 2px accent outline with a 5px offset.

Project markers have transparent backgrounds, muted labels, lightweight neutral numbers, and light rules. The role sidebar uses the same light rule. The header, footer, collection rows, and article sections share light dividers.

Primary actions and menu summaries retain a 44px minimum height; menu links use 48px. The native mobile details menu overlays content on warm paper. JavaScript closes it after navigation, outside click, and Escape, restoring focus after Escape. Current navigation remains marked by an underline and accent text. Reduced-motion preference disables transitions.

Article contents use a native disclosure. Captions can wrap to accommodate full-size and editable-source links. Tags and collection links retain their existing target sizes.

## Diagrams

CRM and CryptoRails workflows are editable `.excalidraw` sources, with portable SVG previews generated by `scripts/generate_excalidraw_diagrams.py` and `scripts/render_excalidraw_diagrams.cjs`. SVGs embed the OFL-licensed Excalifont face for consistent rendering. Excalifont is confined to these source artifacts; the website uses Archivo.

Diagrams use thin warm-gray outlines, muted connectors, light paper fills, and restrained emphasis. They remain illustrative workflows, with full-size links and editable-source downloads. The CryptoRails flow distinguishes browser feedback from verified-webhook settlement and retains its public documentation provenance. Original diagrams remain archived.

## Constraints

- Preserve site content, factual claims, navigation, and artifact provenance.
- Keep readable text contrast and visible focus; lighten decoration rather than fading all content.
- Use typography, spacing, and thin rules for hierarchy.
- Keep the existing square geometry and native disclosure behavior.
- Avoid shadows, rounded card grids, large filled accent panels, and decorative technology imagery.
- Visual checks describe the tested routes and viewports only; this document is not a blanket certification.

The Projects page uses generous two-column editorial rows with contained artifact images, category filters, a labeled search, and native dialog image previews. On mobile, each image precedes its project details. All projects and direct image links remain available without JavaScript. VideoFlow uses the real shared studio interface with illustrative demo content; Monash uses its public platform and actual CitizenFlood reporting screen.

Project row titles use a fluid 1.6rem–2.4rem size, weight 450, and 1.2 line height. Image preview backdrops use rgba(35, 33, 28, .72) to keep the artifact legible.

About uses a portrait and identity column beside a generous biography, followed by three text paths into work, writing, and experience. Writing and Blog use editorial rows: topic/date/read time in a narrow column, title and description in the reading column. All writing combines notes and blog entries; topic and search controls progressively enhance the index. The regression series retains chronological reading order in a native disclosure. VideoFlow has an animated studio overview with a pause control and a reduced-motion still fallback.

The homepage shows two selected work stories, followed by an Explore more work link to the Projects archive, where VideoFlow and Monash remain available. All writing visibly separates Blog posts (product work, systems, and experiences) from Technical notes (mathematics, AI, and research); each group explains its contents before the article rows. Article titles are h3 beneath each collection h2. Filters hide empty groups as well as articles.

View more work on the homepage is a centered native disclosure, collapsed initially. It reveals VideoFlow and Monash in the same editorial evidence layout as the first two projects. The control becomes Show less work when open. VideoFlow animation pauses while the disclosure is closed.

The regression reading path is an inset native disclosure with a title, lesson count, short progression description, and numbered title/summary rows. The CV uses a dedicated template with a sticky section index on desktop and wrapping anchor navigation on mobile, consistent entry spacing, aligned dates, and one page h1. All source CV facts remain intact.

When expanded, the homepage work disclosure places its Show less work control below the newly revealed projects. Closing returns focus to View more work. Without JavaScript, the native summary remains available.

Public diagrams offer an in-page native dialog with fit/actual-size controls, Escape and backdrop dismissal, and focus restoration. Excalidraw source downloads are omitted from visitor-facing captions. SVG previews and the internal editable source files remain available for maintenance.

CV certifications use two columns above 640px, with each logo above its title, issuer, issue date, and credential link. Mobile uses a single column. The certifications collection has an explicit class rather than position-based layout rules.

Dedicated project pages pair a large artifact with concise project context and real action links, then use a narrow contents index beside a 68ch reading column. The layout stacks below 920px. Source descriptions distinguish actual application imagery from the illustrative VideoFlow project and unvalidated Monash scenario outputs.
