#!/usr/bin/env python3
"""Validate an agent's JSON design audit against the pinned checklist items."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUSES = ('Present', 'Partial', 'Missing', 'Not applicable', 'Unverified')
EVIDENCE_TYPES = ('source', 'screenshot', 'browser', 'user', 'none')


def checklist_items():
    return {p.stem: {f'{p.stem}:{i:02d}': title for i, title in enumerate(
        re.findall(r'^### (.+)$', p.read_text(), re.M), 1)}
        for p in (ROOT / 'data/checklist-design/checklists').glob('*.md')}


def validate(report):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())
    require(isinstance(report, dict), 'Report must be an object')
    if not isinstance(report, dict):
        return errors
    for field in ('scope', 'snapshot'):
        require(nonempty(report.get(field)), f'{field} is required')
    manifest = json.loads((ROOT / 'data/checklist-design/manifest.json').read_text())
    require(report.get('snapshot') == manifest['commit'], 'Snapshot must match the pinned source commit')
    selected = report.get('selected', [])
    require(isinstance(selected, list) and bool(selected), 'Select at least one checklist')
    if not isinstance(selected, list):
        return errors
    definitions = checklist_items()
    expected = {}
    keys = []
    for entry in selected:
        if not isinstance(entry, dict):
            errors.append('Each selected checklist must be an object')
            continue
        key = entry.get('checklist')
        require(key in definitions, f'Unknown checklist: {key}')
        require(nonempty(entry.get('reason')), f'Selection needs a reason: {key}')
        keys.append(key)
        expected.update(definitions.get(key, {}))
    require(len(keys) == len(set(keys)), 'Selected checklists must be unique')
    exclusions = report.get('excluded')
    require(isinstance(exclusions, list), 'excluded must list relevant candidates excluded with reasons')
    if isinstance(exclusions, list):
        for entry in exclusions:
            require(isinstance(entry, dict) and nonempty(entry.get('checklist')) and nonempty(entry.get('reason')),
                    'Each excluded candidate needs checklist and reason')
    rows = report.get('items', [])
    require(isinstance(rows, list), 'items must be a list')
    if not isinstance(rows, list):
        return errors
    ids = []
    statuses = Counter()
    for row in rows:
        if not isinstance(row, dict):
            errors.append('Each item must be an object')
            continue
        item_id = row.get('id')
        require(item_id in expected, f'Unexpected item ID: {item_id}')
        require(row.get('title') == expected.get(item_id), f'Item title must match source: {item_id}')
        ids.append(item_id)
        status = row.get('status')
        require(status in STATUSES, f'Invalid status: {item_id}')
        if status in STATUSES:
            statuses[status] += 1
        kind = row.get('evidenceType')
        require(kind in EVIDENCE_TYPES, f'Invalid evidenceType: {item_id}')
        require(kind != 'none' or status in ('Unverified', 'Not applicable'), f'Observed status requires evidence: {item_id}')
        for field in ('location', 'evidence', 'reason'):
            require(nonempty(row.get(field)), f'{item_id} needs {field}')
        if status in ('Partial', 'Missing'):
            require(row.get('severity') in ('Critical', 'High', 'Medium', 'Low'), f'{item_id} needs severity')
            for field in ('impact', 'fix', 'verify'):
                require(nonempty(row.get(field)), f'{item_id} needs {field}')
        if status == 'Unverified':
            require(nonempty(row.get('verify')), f'{item_id} needs a verification step')
    require(len(ids) == len(set(ids)), 'Duplicate item IDs')
    remaining = sorted(set(expected) - set(ids))
    coverage = report.get('coverage', {})
    require(isinstance(coverage, dict), 'coverage must be an object')
    if isinstance(coverage, dict):
        require(coverage.get('expected') == len(expected), 'Incorrect expected count')
        require(coverage.get('reported') == len(rows), 'Incorrect reported count')
        require(isinstance(coverage.get('remaining'), list) and coverage['remaining'] == remaining, 'remaining must list all unreported IDs in sorted order')
        require(coverage.get('complete') is (not remaining), 'Incorrect coverage.complete')
        verification_complete = not remaining and statuses['Unverified'] == 0
        require(coverage.get('verificationComplete') is verification_complete, 'Incorrect verificationComplete')
        require(coverage.get('totals') == {status: statuses[status] for status in STATUSES}, 'Incorrect status totals')
    limitations = report.get('limitations')
    require(isinstance(limitations, list) and all(nonempty(x) for x in limitations), 'limitations must be a list of nonempty strings')
    if statuses['Unverified']:
        require(bool(limitations), 'Unverified results require limitations')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    try:
        errors = validate(json.loads(args.report.read_text()))
    except (ValueError, TypeError, KeyError) as exc:
        parser.exit(1, f'Invalid audit: {exc}\n')
    if errors:
        parser.exit(1, '\n'.join(errors) + '\n')
    print('Audit structure and item coverage verified. Evidence accuracy still requires review.')


if __name__ == '__main__':
    main()
