# Graphite Sketch website design

## Intent and scope
Apply the supplied Graphite Sketch brief recursively to the existing Zola personal website: homepage, biography, writing indexes, articles, technical notes, publications, projects and details, CV, design guide, taxonomy pages, utility pages, 404, and the bundled standalone slide deck. Preserve content, routes, navigation labels, SEO metadata, math rendering, search/filter controls, and project evidence.

## Visual direction
Bright white paper, graphite type, quiet editorial serif headings, generous whitespace, fine rules, restrained controls, and real pencil illustrations. Use the existing local Latin Modern Roman fonts for editorial typography and Archivo for functional labels. Use no decorative motion or simulated paper tint. Keep responsive navigation and visible keyboard focus.

Only palette names: paper (#FFFFFF), graphite (#2B2B2B), soft graphite (#7A7A7A), light hatching (#C9C9C9). Use graphite for readable body copy and small labels; reserve soft graphite for larger secondary elements and light hatching for nonessential rules. Paper remains white throughout, including code blocks and slides.

## Approach
Recommended: revise shared tokens and add one final shared theme layer after page-specific styles, then repair page-family exceptions and standalone slides. This provides consistent recursive coverage while retaining existing behavior.

Alternative: rewrite individual page layouts. This offers greater composition freedom but increases duplication and regression risk without improving fidelity to this illustration-focused brief.

Alternative: change illustrations alone. This preserves the current beige/brown UI and therefore fails the requested whole-site direction.

## Illustrations and evidence
Generate a small coherent set of original graphite illustrations using the supplied recipe verbatim, changing only its subject. Use one quiet metaphor per image: a researcher at a desk with a branching seedling for the home hero; a pencil tracing a path through an open notebook for writing and docs; a carefully constructed bridge for projects. Reuse deliberately across related page families rather than generating arbitrary decoration for every URL. Record prompts and asset roles for maintenance.

Generate a graphite portrait from the existing portrait reference, preserving the person's likeness. Use an appropriate graphite illustration for the default social preview. Keep explanatory diagrams, screenshots, charts, logos, and documentary photographs as factual source material; do not invent replacements that alter their information. Place them on white surfaces without decorative colored frames. Any monochrome treatment must preserve chart distinctions and readability.

## Implementation boundaries
Keep the current Zola/Tera stack and local fonts. Audit base templates, all page-specific styles, syntax highlighting, favicon/theme metadata, comment integration, and the independent remark slide styles. Update the colophon to describe the resulting design accurately. Leave generated public output to the build process. Do not deploy or commit automatically.

## Verification
Build with Zola. Run existing source/export consistency checks affected by template or colophon changes. Inspect desktop and narrow mobile versions of the homepage, biography, writing index, article with code/math, project detail, CV, design guide, taxonomy, 404, and slide deck. Check navigation, filters, disclosures, focus visibility, overflow, asset loading, and print CV readability. Audit the built HTML for consistent theme inclusion across every generated route.

## Builder decisions
The typography pairing, shared final theme layer, low motion, modest illustration reuse, and preservation of factual source imagery are proposed implementation choices. The supplied illustration style clauses and named palette are fixed user requirements.
