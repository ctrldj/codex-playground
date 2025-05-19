## In one sentence, what this file does
"""DXF/DWG/PDF ingest and semantic entity extraction.

This module is intentionally *very* lightweight at the moment – it only parses
DXF files using *ezdxf* and exposes a small :class:`ParsedDrawing` dataclass
that can be consumed by the rule engine.  Geometry recognition and advanced
layer/block heuristics will be added incrementally.
"""

from __future__ import annotations

import pathlib
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Optional *ezdxf* import – we provide a minimal stub for environments where the
# dependency is unavailable (e.g. during CI sandboxing).  The stub only
# implements the subset of the public API used by this package.
# ---------------------------------------------------------------------------
from typing import List, Tuple

try:
    import ezdxf  # type: ignore
except ModuleNotFoundError:  # pragma: no cover – stub fallback

    class _ModelSpace(list):
        def __iter__(self):  # noqa: D401 – generator
            return super().__iter__()

    class _DocStub:
        def modelspace(self):
            return _ModelSpace()

    class _EzDxfStub:  # noqa: D401 – simple stub
        @staticmethod
        def readfile(_path: str):
            return _DocStub()

        @staticmethod
        def new(_version: str = "R2010", *, setup: bool = False):
            return _DocStub()

    ezdxf = _EzDxfStub()  # type: ignore  # noqa: N806



################################################################################
# Public data structures                                                       #
################################################################################


@dataclass(slots=True)
class ScaffoldElement:
    """Base class for extracted scaffold components."""

    entity: ezdxf.entities.dxfgfx.GraphicEntity

    @property
    def location(self) -> Tuple[float, float, float]:  # pragma: no cover
        """Return world-space coordinates of the element (approx.)."""

        try:
            return tuple(self.entity.dxf.insert)  # type: ignore[arg-type]
        except AttributeError:
            return (0.0, 0.0, 0.0)


@dataclass(slots=True)
class ParsedDrawing:
    """Lightweight container holding all geometry relevant to auditing."""

    path: pathlib.Path
    elements: List[ScaffoldElement]


################################################################################
# Public helpers                                                               #
################################################################################


def parse_drawing(path: str | pathlib.Path) -> ParsedDrawing:
    """Parse *path* and return a :class:`ParsedDrawing`.

    Currently only DXF files are supported.  A :class:`NotImplementedError` is
    raised for DWG/PDF input, as conversion pipelines are non-trivial.
    """

    p = pathlib.Path(path)
    suffix = p.suffix.lower()

    if suffix not in {".dxf"}:  # TODO: support more formats via external tools
        raise NotImplementedError(
            f"Unsupported file type '{suffix}'. Only DXF is currently supported."
        )

    doc = ezdxf.readfile(str(p))

    msp = doc.modelspace()

    elements: list[ScaffoldElement] = []

    # Very naive: treat **everything** in modelspace as a scaffold element for
    # now.  Future builds will look at layers / block names etc.
    for e in msp:
        elements.append(ScaffoldElement(entity=e))

    return ParsedDrawing(path=p, elements=elements)
