"""A fully reconciled partial audit must not pass a completed-trial gate."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class TrialScoring(unittest.TestCase):
    def test_omitted_non_sentinel_item_fails_trial(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'results'
            shutil.copytree(ROOT / 'tests/design-guide/results', target)
            file = target / 'empty-screenshot.json'
            data = json.loads(file.read_text())
            removed = next(row for row in data['items'] if row['id'] == 'design-system-button:01')
            data['items'].remove(removed)
            data['coverage'].update(reported=len(data['items']), remaining=[removed['id']], complete=False,
                                    verificationComplete=False)
            data['coverage']['totals'][removed['status']] -= 1
            file.write_text(json.dumps(data))
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_design_trials.py'),
                                     '--results-dir', str(target)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, 'Incomplete audit incorrectly passed a completed trial')
            self.assertIn('Trial requires complete item coverage', result.stderr)


if __name__ == '__main__':
    unittest.main()
