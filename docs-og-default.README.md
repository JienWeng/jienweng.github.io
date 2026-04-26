# Default Open Graph image

Place a file here named `og-default.png` (1200x630, < 1 MB) for default
social-media previews. Per-page overrides can be set in front matter:

```toml
[extra]
cover = "img/posts/your-cover.png"
```

The path is resolved via Zola's `get_url(path=...)` and should live under
`static/`. Recommended size 1200x630, PNG or JPG.
