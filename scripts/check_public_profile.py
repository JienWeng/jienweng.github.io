#!/usr/bin/env python3
"""Check that public text, JSON, and PDF exports contain the current CV entries."""
import json
import re
import subprocess
import sys
from pypdf import PdfReader
from generate_llms import ROOT, SECTIONS, read


def normalized(value):
    return re.sub(r'\s+', ' ', value).strip()


def main():
    subprocess.run([sys.executable, str(ROOT / 'scripts/generate_llms.py'), '--check'], check=True)
    text = (ROOT / 'static/cv/profile.txt').read_text()
    profile = json.loads((ROOT / 'static/cv/public-profile.json').read_text())
    reader = PdfReader(ROOT / 'static/cv/jien-weng-lai-public-cv.pdf')
    pdf = normalized(' '.join(page.extract_text() for page in reader.pages))
    count = 0
    for label, name in SECTIONS:
        items = read(f'content/cv/{name}.toml')['collection']
        assert len(profile['sections'][label]) == len(items), label
        for item in items:
            for key in ('title', 'date', 'subtitle', 'status'):
                if item.get(key):
                    assert item[key] in text, (label, key, 'text')
                    assert normalized(item[key]) in pdf, (label, key, 'PDF')
            count += 1
    assert '@/' not in text
    assert reader.metadata.title == 'Jien Weng Lai - Public Curriculum Vitae'
    print(f'Public profiles verified: {count} CV entries, {len(reader.pages)} PDF pages.')


if __name__ == '__main__':
    main()
