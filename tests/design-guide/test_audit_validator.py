"""Catch skipped items, invented IDs, unsupported completion, and missing evidence."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from check_design_audit import checklist_items, validate, STATUSES


def report():
    key = 'web-app-empty-state'
    definitions = checklist_items()[key]
    return {'scope': 'Screenshot-only empty state',
            'snapshot': json.loads((ROOT / 'data/checklist-design/manifest.json').read_text())['commit'],
            'selected': [{'checklist': key, 'reason': 'First-use empty projects screen'}],
            'excluded': [],
            'items': [{'id': key, 'title': title, 'status': 'Unverified', 'evidenceType': 'none',
                       'location': 'Projects', 'evidence': 'Screenshot unavailable',
                       'reason': 'Cannot inspect', 'verify': 'Read the screenshot and inspect the relevant state'}
                      for key, title in definitions.items()],
            'coverage': {'expected': 6, 'reported': 6, 'remaining': [], 'complete': True,
                         'verificationComplete': False,
                         'totals': {s: 6 if s == 'Unverified' else 0 for s in STATUSES}},
            'limitations': ['No screenshot supplied']}


class AuditValidation(unittest.TestCase):
    def test_accounted_but_unverified_is_valid(self):
        self.assertEqual(validate(report()), [])

    def test_missing_row_cannot_claim_complete(self):
        data = report(); data['items'].pop()
        self.assertIn('Incorrect coverage.complete', validate(data))

    def test_duplicate_cannot_replace_missing_item(self):
        data = report(); data['items'][-1] = copy.deepcopy(data['items'][0])
        self.assertIn('Duplicate item IDs', validate(data))

    def test_unverified_cannot_claim_verified(self):
        data = report(); data['coverage']['verificationComplete'] = True
        self.assertIn('Incorrect verificationComplete', validate(data))

    def test_observed_status_requires_evidence(self):
        data = report(); data['items'][0]['status'] = 'Present'
        self.assertTrue(any('Observed status requires evidence' in e for e in validate(data)))

    def test_invented_item_and_title_are_rejected(self):
        data = report(); data['items'][0].update(id='invented:99', title='Invented requirement')
        self.assertTrue(any('Unexpected item ID' in e for e in validate(data)))

    def test_incomplete_report_can_honestly_list_remaining(self):
        data = report(); row = data['items'].pop()
        data['coverage'].update(reported=5, remaining=[row['id']], complete=False)
        data['coverage']['totals']['Unverified'] = 5
        self.assertEqual(validate(data), [])


if __name__ == '__main__':
    unittest.main()
