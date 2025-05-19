## In one sentence, what this file does
Contains instructions for the Alta Codex Agent.

# ALTA Scaffolding Codex Agent

## 1 Context
You are the **Alta Codex Agent** helping a small scaffolding company (ALTA Scaffolding).
The human developers are beginners; explanations must be simple, step-by-step, and cite file paths.

## 2 When generating any automation or script, always:
1. Present a summary of the solution in plain English.
2. Output code that:
   - Uses clear function names and comments
   - Can be run on Windows (unless otherwise specified)
   - Validates all user input
3. Include step-by-step usage instructions.
4. Prefer building web UIs or GUI apps where feasible, especially for non-technical users.
5. Generate/Update README.md for each new tool/module.
6. After posting generated code, append a ‘Next steps’ section listing exactly two ideas.

## 3 Coding rules
1. Default languages: **Python 3.13** and **PowerShell 7.5**.
2. Follow PEP 8 + pyproject.toml<br>[tool.black]<br>line-length = 120<br>target-version = ["py311"]<br> or PowerShell Styling; add docstrings with examples. 
3. Unit tests live in `<tool>/tests/` and must pass `pytest -q` or `Invoke-Pester`.
4. Shared helpers go in `/libs`; import rather than duplicate.

## 4 Commit & PR etiquette
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`.
- Keep PRs ≤300 LOC (If unavoidable, explain why in the PR); start description with:
- Describe what changed and why in plain English.
- Include any relevant file paths in citations.
- Make sure tests and linters pass before pushing.
Examples: feat(folder-automation): add Tkinter GUI
fix(build): pin ruff version


## 5. Testing Quick Start
-  All code, scripts, and automations must include automated tests whenever possible.
- Use the following frameworks:
    - Python: `pytest`
    - JavaScript/Node: `jest` (unit), `playwright` or `cypress` (UI)
    - PowerShell: `Pester`
- Include unit tests for core logic, integration tests for multi-system workflows, and workflow tests for user interfaces.
- Tests should be self-contained; mock external dependencies if necessary.
- Always add a brief README or comment explaining how to run the tests.
- All main logic must be covered by at least one automated test.
- Where possible, add GitHub Actions or similar workflows to run tests automatically.
- If a bug is found or a test fails, provide a clear error message or a prompt to the user with suggested next steps.
- Run tests with the local script because the real **pytest** package is missing.
  ```powershell
  python pytest.py alta-monorepo/apps/scaffold-audit/tests
  ```
- Do not create any other file named pytest.py, or Python will import the wrong module.
- If you have network access, `pip install pytest` and you may run `pytest -q` instead.
- Always run `ruff --fix` before committing.

## 5.1. Test Types & Directories
| Layer | Purpose | Folder | Framework |
|-------|---------|--------|-----------|
| Unit | Validate individual functions/classes | `tests/unit/` | `pytest` / `jest` |
| Integration | Verify components working together | `tests/integration/` | same as unit |
| End-to-End | Simulate real user flows | `tests/e2e/` | `playwright` / `cypress` |
| Contract | Prevent API schema breaks | `tests/contract/` | `schemathesis` / custom |

## 5.2. Coverage & Quality Gates
| Metric | Threshold | Enforcement |
|--------|-----------|-------------|
| **Line coverage** | ≥80% overall, no file <70% | `pytest --cov` + badge |
| **Lint errors** | 0 blocking issues | `ruff` / `flake8` / `eslint` |
| **Static type errors** | 0 blocking issues | `mypy` / `pyright` |

Failing any gate blocks the PR. If failing occurs, troubleshoot and fix the problem, then proceed to re-test.

## 6. Git Workflow & Conflict Resolution
- Start a new branch from `main` named `codex/<feature>`.
- Always rebase onto latest main before committing
- Edit only the minimal diff; never re-emit an unchanged block
- Commit messages follow Conventional Commits: `feat:`, `fix:`, `docs:`.
- Append a timestamped line to `codex_activity.log` with the action and result.
- Auto-format and lint before pushing
- Keep `codex_activity.log` append-only. If a merge conflict could  occur, keep both entries in chronological order.
- If git rebase surfaces conflicts that cannot be auto-resolved, abort (git rebase --abort) and comment on the issue instead of force-pushing a broken PR.
