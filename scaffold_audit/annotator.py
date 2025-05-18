## In one sentence, what this file does
"""Annotates DXF drawings with audit issues.

This is currently a *very* thin wrapper that simply copies the original file –
future versions will insert a dedicated ``AI_AUDIT`` layer with cloud bubbles
and leader notes at each issue.
"""

from __future__ import annotations

import pathlib
import shutil
from typing import Iterable

from .core import Issue


def annotate_drawing(
    source: str | pathlib.Path,
    destination: str | pathlib.Path,
    issues: Iterable[Issue],
):
    """Create an annotated copy of *source* at *destination*.

    For now this is a simple file copy.  The implementation will evolve to use
    *ezdxf* for actual markup.
    """

    src = pathlib.Path(source)
    dst = pathlib.Path(destination)

    # TODO: Replace with real annotation logic.
    shutil.copy(src, dst)
