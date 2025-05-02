"""Core auditing logic – orchestrates parsing, rule evaluation & reporting."""

from __future__ import annotations

import json
import pathlib
import sys
from dataclasses import dataclass
from typing import Any, Iterable, List

# External deps – imported lazily where possible to keep startup time low.
import ezdxf  # type: ignore  # noqa: F401  # (ensure hard dep is declared)

from .parser import ParsedDrawing, parse_drawing
from .rules import Rule, RuleEngine, load_rules
from .report import generate_html_report

__all__: list[str] = [
    "Issue",
    "AuditResult",
    "audit_file",
]


@dataclass(slots=True, frozen=True)
class Issue:
    """A rule breach detected during auditing."""

    id: str
    rule: str
    location: tuple[float, float, float] | tuple[float, float]
    description: str
    suggested_fix: str | None = None

    def to_json(self) -> dict[str, Any]:
        """Convert :class:`Issue` to JSON-serialisable dict."""

        return {
            "id": self.id,
            "rule": self.rule,
            "location": self.location,
            "description": self.description,
            "suggested_fix": self.suggested_fix,
        }


@dataclass(slots=True, frozen=True)
class AuditResult:
    """Container holding the outcome of an audit run."""

    drawing: pathlib.Path
    issues: List[Issue]

    def to_json(self) -> dict[str, Any]:
        return {
            "drawing": str(self.drawing),
            "issues": [issue.to_json() for issue in self.issues],
            "issue_count": len(self.issues),
        }


def audit_file(
    drawing_path: str | pathlib.Path,
    *,
    rules_path: str | pathlib.Path | None = None,
    output_dir: str | pathlib.Path | None = None,
) -> AuditResult:
    """Run the audit pipeline for a single drawing file.

    Parameters
    ----------
    drawing_path:
        Path to the DXF/DWG/PDF file to audit.
    rules_path:
        Optional YAML file defining audit rules.  If omitted, the built-in
        ``config/default_rules.yaml`` will be used.
    output_dir:
        Directory where the annotated DXF and HTML report should be written.  If
        *None*, the files will be placed next to *drawing_path*.
    """

    path = pathlib.Path(drawing_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(path)

    rules_file = (
        pathlib.Path(rules_path).expanduser().resolve()
        if rules_path is not None
        else pathlib.Path(__file__).with_suffix("").parent.parent
        / "config"
        / "default_rules.yaml"
    )

    parsed: ParsedDrawing = parse_drawing(path)

    rule_engine = RuleEngine(load_rules(rules_file))
    issues = rule_engine.evaluate(parsed)

    # Save outputs
    out_dir = (
        pathlib.Path(output_dir).expanduser().resolve()
        if output_dir is not None
        else path.parent
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    # Annotate DXF in place on a copy.
    annotated_dxf_path = out_dir / f"{path.stem}_AUDIT.dxf"
    try:
        from .annotator import annotate_drawing

        annotate_drawing(path, annotated_dxf_path, issues)
    except Exception as exc:  # pragma: no cover – this is non-critical
        print(f"[WARN] Failed to annotate DXF: {exc}", file=sys.stderr)

    # Generate HTML report (non-fatal on error).
    report_path = out_dir / f"REPORT_{path.stem}.html"
    try:
        generate_html_report(report_path, parsed, issues)
    except Exception as exc:  # pragma: no cover – this is non-critical
        print(f"[WARN] Failed to generate HTML report: {exc}", file=sys.stderr)

    return AuditResult(drawing=path, issues=issues)
