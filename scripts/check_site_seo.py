#!/usr/bin/env python3
"""Check a production Zola build for metadata and broken local resources."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []; self.title = ''; self.schema = []; self.capture = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs); self.tags.append((tag, attrs))
        if tag == 'title': self.capture = 'title'
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.capture = 'schema'; self.schema.append('')
    def handle_endtag(self, tag):
        if tag in ('title', 'script'): self.capture = None
    def handle_data(self, text):
        if self.capture == 'title': self.title += text
        if self.capture == 'schema': self.schema[-1] += text
    def values(self, tag, key, value):
        return [a for t, a in self.tags if t == tag and a.get(key) == value]

def check(root):
    errors = []; pages = 0
    for file in sorted(root.rglob('*.html')):
        p = Page(); p.feed(file.read_text()); label = str(file.relative_to(root))
        if not any(t == 'body' and 'portfolio' in a.get('class', '').split() for t, a in p.tags): continue
        pages += 1
        def fail(message): errors.append(f'{label}: {message}')
        if not p.title.strip(): fail('missing title')
        descriptions = p.values('meta', 'name', 'description')
        if len(descriptions) != 1 or not descriptions[0].get('content', '').strip(): fail('missing/duplicate description')
        canonicals = p.values('link', 'rel', 'canonical')
        if len(canonicals) != 1: fail('missing/duplicate canonical'); continue
        canonical = canonicals[0]['href']; origin = urlsplit(canonical).netloc
        if urlsplit(canonical).scheme != 'https': fail('canonical must use production HTTPS')
        expected = '/' + label.removesuffix('index.html')
        if file.name != '404.html' and urlsplit(canonical).path.rstrip('/') != expected.rstrip('/'): fail('canonical points to another page')
        if sum(t == 'h1' for t, _ in p.tags) != 1: fail('expected one h1')
        if not p.schema: fail('missing structured data')
        for source in p.schema:
            try: json.loads(source)
            except json.JSONDecodeError: fail('invalid JSON-LD')
        og = p.values('meta', 'property', 'og:title')
        if file.name != '404.html' and (not og or og[0].get('content') != p.title): fail('social title differs from page title')
        for tag, attrs in p.tags:
            if tag == 'img' and 'alt' not in attrs: fail('image missing alt')
            target = attrs.get('src') if tag in ('img', 'script') else attrs.get('href') if tag in ('a', 'link') else None
            if not target: continue
            url = urlsplit(urljoin(canonical, target))
            if url.scheme not in ('http', 'https') or url.netloc != origin: continue
            path = root / unquote(url.path).lstrip('/')
            if path.is_dir(): path /= 'index.html'
            if not path.exists() and not (path / 'index.html').exists(): fail(f'missing local target {url.path}')
    return pages, sorted(set(errors))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('build', type=Path); args = parser.parse_args()
    pages, errors = check(args.build)
    print(f'Checked {pages} portfolio pages; {len(errors)} issues.')
    for error in errors: print(error)
    raise SystemExit(bool(errors))
