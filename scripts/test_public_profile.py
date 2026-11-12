#!/usr/bin/env python3
"""The export verifier must reject stale PDF descriptions, not only stale titles."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PdfConsistencyTests(unittest.TestCase):
    def test_changed_education_content_requires_pdf_regeneration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in ('config.toml', 'content/bio.md', 'content/now.md',
                             'content/projects/items.toml', 'scripts/generate_llms.py',
                             'scripts/generate_cv_pdf.py',
                             'scripts/check_public_profile.py',
                             'static/cv/jien-weng-lai-public-cv.pdf'):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            shutil.copytree(ROOT / 'content/cv', root / 'content/cv')
            subprocess.run([sys.executable, str(root / 'scripts/generate_cv_pdf.py')],
                           check=True, capture_output=True, env=os.environ.copy())
            source = root / 'content/cv/education.toml'
            lines = source.read_text().splitlines()
            index = next(i for i, line in enumerate(lines) if line.startswith('content = '))
            lines[index] = 'content = "A newly corrected qualification description."'
            source.write_text('\n'.join(lines) + '\n')
            subprocess.run([sys.executable, str(root / 'scripts/generate_llms.py')],
                           check=True, capture_output=True, env=os.environ.copy())
            result = subprocess.run([sys.executable, str(root / 'scripts/check_public_profile.py')],
                                    capture_output=True, text=True, env=os.environ.copy())
            self.assertNotEqual(result.returncode, 0, 'A stale PDF description was accepted.')
            self.assertIn('Education', result.stderr)
            self.assertIn('content', result.stderr)


if __name__ == '__main__':
    unittest.main()
