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
