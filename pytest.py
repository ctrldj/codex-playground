## In one sentence, what this file does
"""Minimal pytest stub that discovers and runs unittest tests."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

# Ensure the scaffold-audit package is importable during local testing
sys.path.insert(0, str(Path("alta-monorepo/apps/scaffold-audit/src")))


def main() -> int:
    """Discover and run tests from the given directory."""
    args = sys.argv[1:]
    # Default to the monorepo folder so all apps are discovered
    start_dir = Path(args[0]) if args else Path("alta-monorepo")
    suite = unittest.TestLoader().discover(str(start_dir))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
