## Setup

- Create and activate a virtual environment
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
- Install the package in editable mode
  ```powershell
  pip install -e .
  ```

## How to run

- Audit a drawing
  ```powershell
  python -m scaffold_audit path\to\drawing.dxf
  ```
- Execute the tests
  ```powershell
  python pytest.py alta-monorepo/apps/scaffold-audit/tests
  ```
- Create a job folder
  ```powershell
  python -m folder_automation "ClientName" "JobName"
  ```

## Glossary

- **DXF** – Drawing Exchange Format used by many CAD programs.
- **Audit** – Automatic check of a drawing against safety rules.
- **Stub** – Lightweight placeholder module used when a dependency is missing.
- **Template** – A starter document copied into each new job folder.

## Monorepo layout

The `alta-monorepo/` folder contains all future tools. Each app lives under `apps/` with its own `src/` and `tests/` folders. Reusable modules are kept in `libs/`.
The **folder-automation** module was moved from the `libs/` directory and now lives in `alta-monorepo/apps/estimations/folder-automation`.
