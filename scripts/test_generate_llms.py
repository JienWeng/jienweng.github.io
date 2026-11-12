#!/usr/bin/env python3
"""Regression tests for facts carried from public source files into exports."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import generate_llms


class PublicExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write('config.toml', '''base_url = "https://example.test"
description = "Public profile"
[extra]
email = "public@example.test"
linkedin = "https://linkedin.com/in/example"
github = "https://github.com/example"
x = "https://x.com/example"
scholar = "https://scholar.google.com/example"
orcid = "https://orcid.org/example"
''')
        for _, name in generate_llms.SECTIONS:
            self.write(f'content/cv/{name}.toml', 'collection = []\n')
        self.write('content/cv/experiences.toml', '''[[collection]]
title = "Current role"
date = "2026 - Present"
content = "Build current systems."
[[collection]]
title = "Earlier role"
date = "2024 - 2025"
content = "Built data pipelines."
''')
        self.write('content/bio.md', '+++\ntitle = "About"\n+++\nPublic bio.\n')
        self.write('content/now.md', '+++\ntitle = "Now"\n+++\nWorking on [Project](@/projects/example.md).\n')
        self.write('content/projects/items.toml', '''[[collection]]
title = "Project"
content = "A public project."
case_study = "projects/example/"
status = "In production"
''')

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def generate(self):
        with patch.object(generate_llms, 'ROOT', self.root):
            return generate_llms.generate()

    def test_previous_experience_is_not_lost_from_site_index(self):
        index = self.generate()['static/llms.txt']
        self.assertIn('## Earlier experience', index)
        self.assertIn('Earlier role (2024 - 2025): Built data pipelines.', index)

    def test_project_status_survives_summary_export(self):
        self.assertIn('In production', self.generate()['static/llms.txt'])

    def test_now_content_is_resolved_and_part_of_profile_digest(self):
        first = self.generate()
        profile = json.loads(first['static/cv/public-profile.json'])
        self.assertEqual(profile.get('currentFocus'), {
            'source': 'https://example.test/now/',
            'content': 'Working on [Project](https://example.test/projects/example/).',
        })
        self.assertIn('## Current focus', first['static/cv/profile.txt'])
        self.assertNotIn('@/', first['static/cv/profile.txt'])
        self.write('content/now.md', '+++\ntitle = "Now"\n+++\nA changed public focus.\n')
        changed = json.loads(self.generate()['static/cv/public-profile.json'])
        self.assertNotEqual(profile['sourceDigest'], changed['sourceDigest'])


if __name__ == '__main__':
    unittest.main()
