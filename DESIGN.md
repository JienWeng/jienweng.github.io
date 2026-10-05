---
name: Jien Weng Portfolio
description: A practical editorial portfolio with work evidence at its center.
colors:
  paper: "#f6f3ec"
  paper-2: "#eee9df"
  accent-soft: "#eed1bd"
  ink: "#20201e"
  ink-soft: "#494944"
  accent: "#b83e12"
  rule: "#a6a49d"
  white: "#ffffff"
typography:
  display:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(4rem, 8.3vw, 8.3rem)"
    fontWeight: 900
    lineHeight: 0.93
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(2rem, 3.65vw, 3.6rem)"
    fontWeight: 850
    lineHeight: 1.05
    letterSpacing: "-0.035em"
  title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 750
    lineHeight: 1.15
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
    fontWeight: 750
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  reading-h3:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.3
  article-title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(2rem, 4vw, 4rem)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  collection-title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 550
    lineHeight: 1.4
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
    letterSpacing: "0.14em"
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.white}"
    rounded: "{rounded.square}"
    padding: "10px 20px"
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
  project-rail:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.white}"
    padding: "14px 20px 22px"
  workflow:
    padding: "8px 14px 16px"
---

# Design System: Jien Weng Portfolio

## Overview

**Creative North Star: "Practical Editorial Portfolio"**

The homepage uses a confident editorial composition: oversized type, warm paper, charcoal rules, and rust numbered work rails. Practical evidence and direct navigation carry the professional identity. The same Archivo, warm paper, charcoal, and rust identity extends across template-based content and collection pages. Standalone slide decks retain their own designs.

The approved visual reference is `.impeccable/mocks/desktop-recommended.png`, with the headline “Business needs. Buildable products.” Implementation sources are `templates/base.html`, `templates/partials/portfolio-header.html`, `templates/home.html`, `templates/page.html`, `static/site.css`, `static/portfolio.css`, and `static/portfolio.js`. The base template preloads Archivo and loads the shared portfolio CSS and menu script on every template-based page.

**Key Characteristics:**
- Oversized, tightly set sans-serif display type.
- Flat paper surfaces, thin rules, and square corners.
- Numbered rust rails paired with work evidence.
- Responsive semantic diagrams and direct text links.

## Colors

Primary rust marks actions, headline punctuation, and project numbering. Neutral warm paper is the canvas; charcoal carries text and major rules. Soft ink supports secondary prose and diagram outlines, while the lighter rule separates writing entries. White text sits on filled rust controls and rails. Inset paper supports code blocks and the restyled diagram’s alternating lanes. Soft rust identifies the diagram’s management band; it is an artifact color rather than a general surface fill.

**The Evidence Rule.** Color organizes the reading sequence; evidence remains understandable without color.

## Typography

Archivo is self-hosted as a variable WOFF2 font with weights 100–900 and `font-display: swap`. Display type uses the heaviest weight; body text stays plain and readable. Uppercase, tracked labels are reserved for small annotations and the wordmark.

The display size becomes `clamp(3.75rem, 9.7vw, 6.6rem)` at 1100px and below, then `clamp(2.35rem, 10.5vw, 4.2rem)` with 0.98 line height at 640px and below. Mobile allows natural headline wrapping. Intro copy is limited to 66ch. Reading prose uses 17px type and 1.75 line height, reducing to 16px at 920px and below. Reading h2 and h3 have their own restrained scale. Captions and collection dates use the caption role; article dates, topic notes, and contents links use reading-meta. Back links use their named role, and collection titles use the collection-title role. The 1.15rem size also serves the mobile wordmark. These are intentional role sizes rather than a uniform mathematical scale.

## Layout

The shell is capped at 100rem with fluid horizontal padding; mobile uses 20px gutters. Desktop work sections use a 110px rail, a 40px gap, and an evidence area split between artifact and role. At 1100px and below, rails narrow to 70px with a 24px gap, evidence stacks, and the hero margin annotation disappears. At 640px and below, rails become horizontal, navigation becomes a native details menu, and all work sections form one column. Writing and contact align with the desktop work content edge.

Reading and collection shells are capped at 92rem. Their desktop layout pairs a minimum 210px, 25% rail with a flexible content column and a 48px gap. At 920px and below, the layout becomes one column with a 28px gap. Article headings span both columns, have a ruled bottom edge, and limit the title to 30ch. Article contents use a native “On this page” disclosure. Wide tables scroll within the reading column.

The original homepage verification found no horizontal overflow at 320, 390, 768, and 1536px. This observation does not certify every subsequent page.

## Elevation & Depth

Flat surfaces and thin borders provide separation. The mobile navigation overlays content using stacking order, warm paper, and a charcoal border. There are no shadows.

## Shapes

Square controls, rectangular workflow stages, and straight rules establish the geometry. Arrows use simple strokes; work rails form the recurring accent shape. Avoid adding rounded containers to this template-page vocabulary.

## Components

Primary links use filled rust rectangles, white labels, and a right arrow; hover changes the fill to charcoal. Text actions are underlined and move their arrow 4px over 180ms ease-out on hover. Interactive links and menu summaries use a 2px rust focus outline with a 5px offset. Reduced-motion preference disables transitions.

Desktop navigation uses plain text links with a minimum 44px height. The mobile details summary has the same minimum; menu links use 48px. Native details provides disclosure semantics, while JavaScript closes the menu on link selection, outside click, and Escape; Escape restores focus to the summary.

Numbered work rails identify the work sequence. The payment illustration uses a semantic ordered list of four stages and a clearly labeled review note; it stacks vertically on mobile. The CRM figure uses `static/img/blog/quandatics/deal-to-cash-portfolio.png`, a generated palette and typography restyle of the original eight-step workflow, and offers a full-size link. The original image is retained; the adjacent `.png.json` records the full generation prompt and text correction. Treat it as a restyled source artifact, not a new product screenshot. Writing entries use ruled rows with a title, date, and arrow, moving the date below the title on mobile. The shared header marks the current destination with rust text and an underline. Article contents use a native details summary with a 44px minimum height. Tags and collection links are plain textual navigation, with current minimum heights of 32px and 36px respectively; inline reading links retain natural text sizing.

## Do's and Don'ts

- Do preserve visible keyboard focus and the 44px minimum for primary actions and disclosure controls.
- Do label the payment workflow as illustrative and retain provenance for the restyled CRM workflow.
- Do retain the native mobile menu and reduced-motion behavior.
- Do use the shared Archivo identity across template pages and preserve standalone slide designs.
- Do make each label and sentence explain a destination, role, decision, or piece of evidence.

- Don't introduce shadows, rounded card grids, or decorative technology imagery across template pages.
- Don't present illustrative workflows as product screenshots.
- Don't treat this documentation as a passed formal quantitative build-state specification.
