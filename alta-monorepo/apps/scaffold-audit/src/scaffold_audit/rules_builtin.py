"""Built-in rule implementations.

Real geometric checks will be added incrementally – at the moment we provide a
single *placeholder* rule that never flags any issues, purely to ensure end-to-
end plumbing works.
"""

from __future__ import annotations

from typing import Iterable

from .parser import ParsedDrawing


def always_pass(_drawing: ParsedDrawing) -> Iterable[str]:
    """Placeholder rule – yields nothing (i.e. no issues)."""

    yield from ()
