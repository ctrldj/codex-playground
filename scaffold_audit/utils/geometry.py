"""Geometry helpers (placeholder)."""

from __future__ import annotations

import math
from typing import Tuple


def distance(p1: Tuple[float, float, float], p2: Tuple[float, float, float]) -> float:
    """Return Euclidean distance between 3-D points *p1* and *p2*."""

    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
