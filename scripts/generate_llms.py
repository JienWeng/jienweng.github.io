#!/usr/bin/env python3
"""Generate public AI-readable profile files from the website's current content."""
import argparse
import hashlib
import json
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = [
    ('Experience', 'experiences'), ('Education', 'education'), ('Awards', 'awards'),
    ('Certifications', 'certifications'), ('Grants', 'grants'),
    ('Open Source', 'opensource'), ('Volunteering', 'volunteering'),
    ('Memberships', 'memberships'), ('Publications', 'publication'),
]


def read(relative):
    return tomllib.loads((ROOT / relative).read_text())


def generate():
    config = read('config.toml')
    base = config['base_url'].rstrip('/')
    extra = config['extra']
    sections = {label: read(f'content/cv/{name}.toml')['collection'] for label, name in SECTIONS}
    projects = read('content/projects/items.toml')['collection']

    def link(label, path):
        return f'[{label}]({base}/{path.lstrip("/")})'

    def entry(item):
        lines = [f'### {item["title"]}']
        for field in ('date', 'subtitle', 'issuer', 'authors', 'venue', 'status', 'content'):
            if item.get(field):
                prefix = {'issuer': 'Issuer: ', 'authors': 'Authors: ', 'venue': 'Venue: ', 'status': 'Status: '}.get(field, '')
                lines.append(prefix + item[field])
        if item.get('link'):
            lines.append(f'Link: {item["link"]}')
        if item.get('tags'):
            lines.append('Topics: ' + ', '.join(item['tags']))
        return '\n\n'.join(lines)

    socials = '\n'.join(f'- [{label}]({extra[key]})' for label, key in [
        ('LinkedIn', 'linkedin'), ('GitHub', 'github'), ('X', 'x'),
        ('Google Scholar', 'scholar'), ('ORCID', 'orcid')])
    intro = f'# Jien Weng Lai\n\n> {config["description"]}\n\n'
    source = f'Official public profile: {base}/\nCurrent CV: {base}/cv/\nContact: {extra["email"]}\n'
    bio = (ROOT / 'content/bio.md').read_text().split('+++', 2)[2].strip()
    # Resolve Zola content links into public URLs in the plain-text version.
    def resolve(match):
        path = match.group(1).removesuffix('.md').removesuffix('/_index')
        return f']({base}/{path}/)'
    bio = re.sub(r'\]\(@/([^)]*)\)', resolve, bio)
    full = intro + source + '\n## Profile\n\n' + bio + '\n\n## Social and research profiles\n\n' + socials
    for label, _ in SECTIONS:
        full += f'\n\n## {label}\n\n' + '\n\n'.join(entry(item) for item in sections[label])
    full += '\n\n## Public projects\n\n' + '\n\n'.join(
        entry(item) + ('\n\nCase study: ' + base + '/' + item['case_study'] if item.get('case_study') else '')
        for item in projects)
    full += '\n\nGenerated from the public website content; no private CV information is included.\n'

    summary = intro + 'Official personal website and public professional information. The text CV contains the complete current public CV and project summaries. Publication statuses below distinguish published work from manuscripts under review.\n\n## Profile and full CV\n\n'
    summary += '\n'.join('- ' + link(label, path) for label, path in [
        ('About', 'bio/'), ('Current CV', 'cv/'), ('Complete text CV', 'cv/profile.txt'),
        ('Public CV PDF', 'cv/jien-weng-lai-public-cv.pdf'), ('Work with me', 'services/'), ('Current priorities', 'now/')])
    summary += '\n\nContact: ' + extra['email'] + '\n\n' + socials
    summary += '\n\n## Current roles\n\n' + '\n'.join(
        f'- {item["title"]} ({item.get("date", "")}): {item.get("content", "")}'
        for item in sections['Experience'] if 'Present' in item.get('date', ''))
    summary += '\n\n## Education\n\n' + '\n'.join(
        f'- {item["title"]} ({item.get("date", "")}): {item.get("content", "")}' for item in sections['Education'])
    summary += '\n\n## Research\n\n' + '- ' + link('Publications', 'publications/') + '\n'
    summary += '\n'.join(f'- {item["title"]} — {item["status"]}, {item["venue"]}, {item["date"]}.' +
                         (f' {item["link"]}' if item.get('link') else '') for item in sections['Publications'])
    summary += '\n\n## Public projects\n\n' + '- ' + link('Work index', 'projects/') + '\n'
    summary += '\n'.join(f'- [{item["title"]}]({base + "/" + item["case_study"] if item.get("case_study") else item["link"]}): {item["content"]}' for item in projects)
    summary += '\n\n## Writing and discovery\n\n' + '\n'.join('- ' + link(label, path) for label, path in [
        ('Writing and technical notes', 'notes/'), ('Blog', 'blog/'), ('Atom feed', 'atom.xml'), ('Sitemap', 'sitemap.xml')])
    summary += '\n\nThe full text CV also includes awards, certifications, grants, open-source contributions, volunteering, and memberships. Both text files are generated from the same public content as this website.\n'
    public_fields = ('title', 'date', 'subtitle', 'issuer', 'authors', 'venue', 'status', 'content', 'link', 'tags')
    profile = {
        'schemaVersion': 2,
        'source': base + '/cv/',
        'sourceDigest': hashlib.sha256(full.encode()).hexdigest(),
        'basics': {'name': 'Jien Weng Lai', 'email': extra['email'], 'website': base,
                   **{key: extra[key] for key in ('linkedin', 'github', 'x', 'orcid', 'scholar')}},
        'headline': 'Product Manager & Researcher',
        'summary': config['description'],
        'sections': {label: [{key: item[key] for key in public_fields if key in item}
                             for item in items] for label, items in sections.items()},
        'projects': [{key: item[key] for key in public_fields + ('case_study',) if key in item}
                     for item in projects],
    }
    return {'static/llms.txt': summary, 'static/cv/profile.txt': full,
            'static/cv/public-profile.json': json.dumps(profile, ensure_ascii=False, indent=2) + '\n'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if committed output is out of date')
    args = parser.parse_args()
    stale = []
    for relative, content in generate().items():
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(f'Generated {relative}')
    if stale:
        parser.exit(1, 'Outdated public profiles: ' + ', '.join(stale) + '\nRun python3 scripts/generate_llms.py\n')


if __name__ == '__main__':
    main()
