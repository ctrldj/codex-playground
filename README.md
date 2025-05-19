## In one sentence, what this file does
Simple instructions for installing and using the scaffold audit tools.

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
  # Optional: install pythonocc-core if you need 3D features
  ```powershell
  pip install pythonocc-core==7.6
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
  # Provide paths if the defaults do not match your system
  python -m folder_automation "ClientName" "JobName" \
    --base-dir C:\path\to\Clients --template-dir C:\path\to\Templates
  ```
  # Or launch the graphical interface
  ```powershell
  python -m folder_automation.gui
  ```
- Build a Windows ``.exe`` (requires `pyinstaller`)
  ```powershell
  pip install pyinstaller
  python -m folder_automation.build_exe
  ```
- After building, run the executable without Python
  ```powershell
  dist\folder_automation_gui.exe
  ```
- If you see an ``ImportError`` running ``build_exe.py`` directly, run it as a module instead:
  ```powershell
  python -m folder_automation.build_exe
  ```

## Glossary

- **DXF** – Drawing Exchange Format used by many CAD programs.
- **Audit** – Automatic check of a drawing against safety rules.
- **Stub** – Lightweight placeholder module used when a dependency is missing.
- **Template** – A starter document copied into each new job folder.
- **GUI** – Graphical User Interface that lets you interact via buttons instead of the command line.

## Monorepo layout

The `alta-monorepo/` folder contains all future tools. Each app lives under `apps/` with its own `src/` and `tests/` folders. Reusable modules are kept in `libs/`.
The **folder-automation** module was moved from the `libs/` directory and now lives in `alta-monorepo/apps/estimations/folder-automation`.
