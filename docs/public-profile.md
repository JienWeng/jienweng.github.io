# Public profile exports

`/llms.txt` provides a concise professional overview and links to the public website. `/cv/profile.txt` includes all nine current CV sections, the About profile, social links, and public project summaries. `/cv/public-profile.json` exposes those public CV sections as structured data (schema version 2). `/cv/jien-weng-lai-public-cv.pdf` is the downloadable full public CV. The CV page links to the text and PDF versions.

All formats use `content/cv/*.toml` and `config.toml`; the text/JSON profiles also include About content and public projects. The PDF and JSON are generated outputs, not independent sources. Publication status is preserved, and private CV data is excluded. JSON's `sourceDigest` identifies its source text without a misleading review timestamp.

Regenerate after editing the source content:

```sh
python3 -m pip install -r scripts/requirements-profile.txt
python3 scripts/generate_llms.py
python3 scripts/generate_cv_pdf.py
python3 scripts/check_public_profile.py
```

Production and pull request preview builds regenerate and verify these files before Zola copies them into the published site. Text/JSON generation itself requires only Python's standard library; PDF creation and verification use the pinned dependencies above.

These files make public information easier to retrieve and summarize. They do not guarantee search indexing, rankings, or adoption by AI services.
