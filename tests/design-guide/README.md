# Agent guide validation

Three fresh-context agent trials were run on November 12, 2026, with the current Codex model (gpt-6.1-sol), once per case. Agents started at the generated `static/design/llms.txt` and selected individual checklist files. They were not given expected outcomes or the validator. Saved JSON outputs and retrieval traces are in `results/`.

The fixtures deliberately limit evidence:

- **form-source:** a newsletter form inspected from HTML only. A persistent field label is absent; submission/loading/error outcomes were not exercised. Optional decorative imagery is explicitly unwanted.
- **empty-screenshot:** a first-use projects component reviewed from a PNG only. Supporting description is absent. The visible CTA's destination and other empty/error states cannot be established. Decorative imagery is explicitly unwanted. `empty-state.html` is the rendering source; the reviewing agent did not read it.
- **modal-observations:** a modal's HTML plus observations recorded in an isolated Chromium fixture. There is no close action; it fits at 1440px but overflows at 390px. Primary action only sets a boolean. The reviewer must attribute supplied browser observations to the user, not claim to have personally executed tests.

All three recorded trials passed: 37 fully accounted item rows across selected checklists; 19 expected-status assertions, including all four planted defects, appropriate treatment of optional decoration, and uncertainty for unavailable behavior. These results are a small smoke test of this model/harness on synthetic fixtures. They do not establish reliability on arbitrary interfaces, other models, repeated runs, or complete accessibility conformance. Coverage completeness does not imply verification completeness or absence of defects.

## Run the deterministic checks

```sh
python3 scripts/check_design_coverage.py
python3 -m unittest discover -s tests/design-guide -p 'test_*.py'
python3 scripts/check_design_trials.py
```

The trial scorer replays saved outputs, checks selected checklist coverage, exact source IDs/titles, expected statuses, and evidence origins. It does not invoke an LLM. The generic report validator catches skipped/duplicate/invented rows, inconsistent totals, unsupported completion claims, and missing evidence/remediation fields. Neither can mechanically verify that prose is truthful or a fix is useful; inspect the artifacts and reports independently.

## Repeat the actual agent trials

For each of `form-source`, `empty-screenshot`, and `modal-observations`, print a blind brief:

```sh
python3 scripts/check_design_trials.py --prompt form-source
```

Give only that output to a fresh-context agent. Do not pass `cases.json`, expected results, validation scripts, previous outputs, or another case. Preserve previous outputs separately if comparing revisions. The agent should write only its named JSON output and retrieval trace. Then run the scorer and review its prose evidence against the artifact. Record the model, date, scope, and any retries. If instructions change materially, run new agent trials rather than describing CI replay as a new behavioral test.
