## In one sentence, what this file does
"""Helper to package the GUI as a standalone Windows executable."""

from __future__ import annotations

import subprocess
from pathlib import Path


def build_exe() -> None:
    """Run PyInstaller to create ``folder_automation_gui.exe`` in ``dist/``."""

    script_path = Path(__file__).resolve().parent / "gui.py"
    subprocess.run(
        [
            "pyinstaller",
            "--onefile",
            "--name",
            "folder_automation_gui",
            str(script_path),
        ],
        check=True,
    )


if __name__ == "__main__":  # pragma: no cover - manual execution only
    build_exe()
