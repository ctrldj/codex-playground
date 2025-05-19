"""## In one sentence, what this file does
Build a standalone executable for the GUI using PyInstaller.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> None:
    """Package the GUI as an executable using PyInstaller."""
    gui_path = Path(__file__).resolve().parent / "gui.py"
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        str(gui_path),
    ], check=True)


if __name__ == "__main__":  # pragma: no cover - manual execution only
    main()
