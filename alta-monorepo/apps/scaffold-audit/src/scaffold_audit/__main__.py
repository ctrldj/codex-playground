"""CLI entrypoint – ``python -m scaffold_audit <drawing.dxf>``."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import audit_file


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scaffold_audit",
        description="Automated scaffold audit tool (AS/NZS 4576 & TG20:21).",
    )
    parser.add_argument(
        "drawing",
        type=Path,
        help="Path to DXF/DWG/PDF drawing to audit.",
    )
    parser.add_argument(
        "--rules",
        type=Path,
        help="Custom YAML rule file (defaults to built-in rules).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory for annotated DXF & report (defaults to drawing folder).",
    )
    return parser


def main(argv: list[str] | None = None) -> None:  # pragma: no cover – CLI only
    parser = _build_parser()
    args = parser.parse_args(argv)

    result = audit_file(
        args.drawing, rules_path=args.rules, output_dir=args.output_dir
    )

    # Dump JSON summary to stdout (always).
    print(json.dumps(result.to_json(), indent=2))

    sys.exit(0 if not result.issues else 1)


if __name__ == "__main__":  # pragma: no cover
    main()
