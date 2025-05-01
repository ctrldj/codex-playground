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

## 3️⃣ Automation rules

| Category | Codex may **do automatically** | Codex **must ask** first |
|----------|-------------------------------|--------------------------|
| Code / Docs | • Generate CRUD endpoints in `/apps/api/`<br>• Refactor code in `/src/**`<br>• Add / update Markdown docs (`README.md`, `CONTRIBUTING.md`) | • Modify anything under `/libs/shared/` API surface |
| Shell commands | — | • Any command that installs software or touches the registry |
| Infrastructure | — | • Create cloud resources<br>• Any changes in `/infra/terraform/` or migrations under `/infra/` |
| Scripts | — | • Anything inside `/scripts/production/` |

## 4️⃣ Environment context Codex should know
* **Windows-first** project—prefer PowerShell examples.
* CI/CD via **Azure Pipelines** (config in `.azure-pipelines/`).
* Repository is hosted in **GitHub** and mirrored to **Azure Repos** nightly.

## 5️⃣ House-keeping preferences
* If a task touches >20 files, ask for confirmation even in `auto-edit`.
* After generating code, run `npm run lint --fix`.
