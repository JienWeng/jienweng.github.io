# jienweng.github.io

Personal site of Jien Weng — research notes, essays, publications, projects, and CV. Live at [jienweng.github.io](https://jienweng.github.io).

## Stack

- [Zola](https://www.getzola.org/) static site generator (Tera templates)
- Deployed to GitHub Pages via `.github/workflows/deploy.yml` (builds on push to `main`)
- KaTeX for math (loaded per-page via `math = true` front matter), remark.js for slide decks, giscus for comments, GoatCounter for analytics

## Local development

```sh
zola serve    # dev server at http://127.0.0.1:1111
zola build    # writes the site to public/
```

## Layout

- `content/` — pages and sections
  - `notes/` — technical notes and derivations (set `draft = true` to keep unpublished)
  - `blog/` — essays and event write-ups
  - `cv/`, `publications/`, `projects/`, `slides/` — data-driven sections backed by `items.toml` / per-section `.toml` files rendered by the `collection` shortcode
- `templates/` — Tera templates (`base.html` holds all head/SEO markup)
- `static/` — CSS, images, favicons, and standalone slide decks under `static/slides/<year>/<slug>/`

## Design Guide for AI

`content/design.md` is the article and original review workflow at `/design/`. The pinned MIT-licensed Checklist Design snapshot lives in `data/checklist-design/`, including the upstream license and a manifest with the source commit, SHA-256 hashes, and per-checklist item counts. It contains 138 checklists and 908 items. The 138 bundled source URLs matched the live catalog on November 12, 2026; item text is from the pinned repository commit, not a live feed.

Edit the article, then run `python3 scripts/generate_llms.py`. This generates the complete `/design/guide.txt`, individual Markdown checklists, internal catalogue data, scoped discovery index, and root discovery link. The page renders the catalogue through `templates/shortcodes/design_catalog.html`. Keep the `<!-- GUIDE_START -->` marker separating the catalogue from the original workflow. Deployment already runs this generator.

Verify with `python3 scripts/generate_llms.py --check` and `python3 scripts/check_design_coverage.py`. Generation validates snapshot hashes and counts. To update the upstream snapshot, review the desired commit of `https://github.com/Checklist-Design/skills`, preserve its MIT license, replace `skills/checklist-design/references/checklists/` in the data folder, and update every manifest entry, checksum, count, source commit, and catalog-check date before regenerating. Do not describe a snapshot as live coverage without checking the current catalog. No upstream code is executed during site generation.

Agent reviews start at `/design/llms.txt`, which includes the same review protocol as the article and full guide. It specifies checklist selection, evidence/status definitions, snapshot-scoped item IDs, full coverage accounting, partial-audit continuation, and optional JSON output. Validate an audit with `python3 scripts/check_design_audit.py report.json`; structural validation does not certify evidence accuracy or design quality.

Run `python3 -m unittest discover -s tests/design-guide -p 'test_*.py'` for negative report-validation checks, and `python3 scripts/check_design_trials.py` to score saved independent-agent trials. See `tests/design-guide/README.md` for evidence boundaries and blind rerun instructions. CI replays saved trial outputs; it does not call models.
