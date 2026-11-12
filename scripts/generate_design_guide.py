"""Build the licensed Checklist Design snapshot and original review guide."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/checklist-design'
CATEGORIES = {'Design system': 'design-system', 'Web app': 'web-app',
              'Mobile app': 'mobile', 'Website': 'website', 'Flows': 'flows'}


def generate_design_resources(base):
    manifest = json.loads((DATA / 'manifest.json').read_text())
    license_text = (DATA / 'LICENSE').read_text().strip()
    entries = manifest['checklists']
    files = {p.name for p in (DATA / 'checklists').glob('*.md')}
    if files != {entry['file'] for entry in entries}:
        raise ValueError('Checklist manifest and snapshot files differ')
    if len(entries) != manifest['checklistCount']:
        raise ValueError('Checklist count differs from manifest')
    attribution = (f"Checklist Design collection: {manifest['repository']}\n"
                   f"Snapshot: {manifest['commit']} · Imported: {manifest['importedOn']}\n"
                   'Republished under the MIT License. Original checklist text belongs to Checklist Design.\n')
    notice = '\n\n## License for the Checklist Design collection\n\n' + attribution + '\n' + license_text + '\n'
    groups = {name: [] for name in CATEGORIES}
    output = {'static/design/LICENSE.txt': license_text + '\n',
              'static/design/manifest.json': json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'}
    total = 0
    for entry in entries:
        raw = (DATA / 'checklists' / entry['file']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != entry['sha256']:
            raise ValueError('Checklist snapshot hash mismatch: ' + entry['file'])
        text = raw.decode().strip()
        count = len(re.findall(r'^### ', text, re.M))
        if count != entry['itemCount'] or count == 0:
            raise ValueError('Checklist item count mismatch: ' + entry['file'])
        total += count
        path = 'design/checklists/' + entry['file']
        output['static/' + path] = text + notice
        # Preserve source descriptions, item hierarchy, and tips in human-readable disclosures.
        body = text.split('\n', 1)[1].replace('\n## Items\n', '\n')
        groups[entry['category']].append({**entry, 'url': base + '/' + path, 'body': body})
    if total != manifest['itemCount']:
        raise ValueError('Total checklist item count mismatch')

    catalog = {'checklistCount': len(entries), 'itemCount': total,
               'commit': manifest['commit'], 'importedOn': manifest['importedOn'],
               'license': license_text, 'categories': []}
    page = (ROOT / 'content/design.md').read_text().split('+++', 2)[2].strip()
    original = page.split('<!-- GUIDE_START -->', 1)[1].strip().replace('](/design/', '](' + base + '/design/')
    bundle = []
    index = (f'# Design Guide for AI\n\n> {len(entries)} Checklist Design checklists and {total} items, '
             'plus review instructions by Jien Weng.\n\n'
             f"Snapshot: {manifest['commit']}\n\n"
             + original + '\n\n'
             + '## Start here\n\n'
             f'- [Complete guide and all checklist items]({base}/design/guide.txt): One-file edition; large context.\n'
             f'- [Snapshot and coverage manifest]({base}/design/manifest.json): Source commit, counts, URLs, and checksums.\n'
             f'- [MIT license]({base}/design/LICENSE.txt): Checklist Design copyright and permission notice.\n')
    for name, slug in CATEGORIES.items():
        items = sorted(groups[name], key=lambda entry: entry['title'].casefold())
        section = f'## {name}\n\n'
        for item in items:
            section += f"- [{item['title']}]({item['url']}): {item['itemCount']} items.\n"
        index += '\n' + section
        raw_texts = [(DATA / 'checklists' / item['file']).read_text().strip() for item in items]
        # Add a level to every source heading to nest each original checklist under its category.
        combined = '\n\n'.join(re.sub(r'^(#+) ', r'#\1 ', text, flags=re.M) for text in raw_texts)
        bundle.append(f'## Checklist Design · {name}\n\n' + re.sub(r'^(#+) ', r'#\1 ', combined, flags=re.M))
        catalog['categories'].append({'name': name, 'slug': slug, 'count': len(items), 'checklists': items})

    full = (f'# Design Guide for AI\n\n> {len(entries)} checklists · {total} source items · Version 2.1\n\n'
            'This file contains original review instructions followed by the complete pinned MIT-licensed '
            'Checklist Design collection, including every bundled item description and tip. '
            'It is a snapshot, not a promise of future live-site parity.\n\n' + attribution + '\n'
            + original + '\n\n' + '\n\n'.join(bundle) + notice)
    output.update({'data/checklist-design/catalog.json': json.dumps(catalog, ensure_ascii=False, indent=2) + '\n',
                   'static/design/guide.txt': full, 'static/design/llms.txt': index})
    return output
