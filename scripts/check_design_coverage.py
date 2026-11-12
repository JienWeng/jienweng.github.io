#!/usr/bin/env python3
"""Verify complete licensed snapshot coverage in every published guide edition."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT / 'scripts/generate_llms.py'), '--check'], check=True)
manifest = json.loads((ROOT / 'data/checklist-design/manifest.json').read_text())
catalog = json.loads((ROOT / 'data/checklist-design/catalog.json').read_text())
full = (ROOT / 'static/design/guide.txt').read_text()
index = (ROOT / 'static/design/llms.txt').read_text()
license_text = (ROOT / 'data/checklist-design/LICENSE').read_text().strip()
assert license_text in full and license_text in catalog['license']
seen = set()
count = 0
for category in catalog['categories']:
    assert category['count'] == len(category['checklists'])
    for item in category['checklists']:
        assert '-'.join(item['source'].split('/')[-2:]) == Path(item['file']).stem, 'Offline audit key must match source URL'
        assert item['file'] not in seen
        seen.add(item['file'])
        source = (ROOT / 'data/checklist-design/checklists' / item['file']).read_text().strip()
        published = (ROOT / 'static/design/checklists' / item['file']).read_text()
        assert published.startswith(source + '\n'), item['file']
        assert license_text in published, item['file']
        assert item['url'] in index, item['file']
        # Only heading depth changes in combined files; descriptions and tips stay exact.
        nested_once = re.sub(r'^(#+) ', r'#\1 ', source, flags=re.M)
        nested_twice = re.sub(r'^(#+) ', r'#\1 ', nested_once, flags=re.M)
        assert nested_twice in full, item['file']
        assert item['itemCount'] == len(re.findall(r'^### ', source, re.M)), item['file']
        count += item['itemCount']
assert seen == {p.name for p in (ROOT / 'static/design/checklists').glob('*.md')}
assert len(seen) == manifest['checklistCount'] == catalog['checklistCount']
assert count == manifest['itemCount'] == catalog['itemCount']
assert not manifest['missingFromSnapshot'], 'Live catalog has uncovered pages'
assert manifest['liveCatalogCount'] == len(seen)
assert (ROOT / 'static/design/checklists/design-system-spacing-and-grid.md').exists()
print(f'Complete snapshot verified: {len(seen)} checklists, {count} items, all descriptions/tips and license notices preserved.')
