#!/usr/bin/env python3
"""Score recorded independent-agent trials; --prompt prints a blind rerun brief."""
import argparse
import json
from pathlib import Path
from check_design_audit import validate

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / 'tests/design-guide'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prompt', metavar='CASE', help='Print the brief and artifact paths without exposing expected outcomes')
    parser.add_argument('--results-dir', type=Path, default=TESTS / 'results', help='Directory of recorded outputs to score')
    args = parser.parse_args()
    cases = json.loads((TESTS / 'cases.json').read_text())
    if args.prompt:
        if args.prompt not in cases:
            parser.error('Unknown case')
        case = cases[args.prompt]
        print('Start at static/design/llms.txt and follow its protocol. Fetch only selected local checklist files and the manifest. ' + case['brief'])
        print('Artifacts: ' + ', '.join('tests/design-guide/' + p for p in case['artifacts']))
        print(f'Return the specified JSON report in tests/design-guide/results/{args.prompt}.json and list reference files actually read in {args.prompt}-trace.txt. Do not read cases.json, validators, expected outcomes, other fixtures/results, or guide.txt; do not run validators or add tests. Use the supplied artifacts only.')
        return
    errors = []
    rows = assertions = 0
    for name, case in cases.items():
        report = json.loads((args.results_dir / f'{name}.json').read_text())
        errors.extend(f'{name}: {error}' for error in validate(report))
        if report.get('coverage', {}).get('complete') is not True:
            errors.append(f'{name}: Trial requires complete item coverage')
        selected = {entry['checklist'] for entry in report['selected']}
        missing = set(case['requiredChecklists']) - selected
        if missing:
            errors.append(f'{name}: missed relevant checklists {sorted(missing)}')
        by_id = {item['id']: item for item in report['items']}
        for item_id, statuses in case['expectedStatuses'].items():
            assertions += 1
            observed = by_id.get(item_id, {}).get('status')
            if observed not in statuses:
                errors.append(f'{name}: {item_id}: expected {statuses}, got {observed}')
        for item in report['items']:
            if item['evidenceType'] not in case['allowedEvidence']:
                errors.append(f'{name}: unsupported evidence origin for {item["id"]}')
        trace = (args.results_dir / f'{name}-trace.txt').read_text()
        if 'guide.txt' in trace:
            errors.append(f'{name}: used complete collection despite selective-retrieval constraint')
        for key in selected:
            if key + '.md' not in trace:
                errors.append(f'{name}: no recorded retrieval for {key}')
        rows += len(report['items'])
        print(f'{name}: {len(report["items"])} item rows, {len(case["expectedStatuses"])} expected-status checks')
    if errors:
        parser.exit(1, '\n'.join(errors) + '\n')
    print(f'PASS: {len(cases)} recorded trials, {rows} fully accounted item rows, {assertions} expected-status checks. This replays saved outputs; it does not run new agents.')


if __name__ == '__main__':
    main()
