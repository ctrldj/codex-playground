# Codex guidelines for ALTA Scaffold Automation Suite

## 1️⃣ Architecture you should know
* Monorepo layout:
  * `/apps/cli/`
  * `/apps/api/`
  * `/libs/shared/`
  * `/infra/terraform/`
  * Critical scripts live in `/scripts/`
* Do **NOT** edit Terraform modules automatically.

## 2️⃣ Code style
* All TypeScript **must** pass `npm run lint` before commit.
* Use Prettier defaults (2-space indent, single quotes).
* Absolute imports with the `@/*` alias.
* Commit messages follow **Conventional Commits** (`feat:`, `fix:`, `docs:` …).
* Default languages: **Python 3.13** and **PowerShell 7.5**.
* Follow PEP 8 + pyproject.toml<br>[tool.black]<br>line-length = 120<br>target-version = ["py311"]<br> or PowerShell Styling; add docstrings with examples. 
* Unit tests live in `<tool>/tests/` and must pass `pytest -q` or `Invoke-Pester`.
* Shared helpers go in `/libs`; import rather than duplicate.

## 5️⃣ House-keeping preferences
* If a task touches >20 files, ask for confirmation even in `auto-edit`.
* After generating code, run `npm run lint --fix`.
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`.
- Keep PRs ≤300 LOC (If unavoidable, explain why in the PR); start description with:
- Describe what changed and why in plain English.
- Include any relevant file paths in citations.
- All code, scripts, and automations must include automated tests whenever possible.
- Use the following frameworks:
    - Python: `pytest`
    - JavaScript/Node: `jest` (unit), `playwright` or `cypress` (UI)
    - PowerShell: `Pester`
- Make sure tests and linters pass before pushing.
Examples: feat(folder-automation): add Tkinter GUI
fix(build): pin ruff version