"""HTML report generation via *Jinja2*."""

from __future__ import annotations

import pathlib
from typing import Iterable

from jinja2 import Environment, PackageLoader, select_autoescape

from .core import Issue
from .parser import ParsedDrawing


_env = Environment(
    loader=PackageLoader("scaffold_audit"),
    autoescape=select_autoescape(["html", "xml"]),
)

_TEMPLATE_NAME = "report_template.html.j2"


def generate_html_report(
    output: str | pathlib.Path,
    drawing: ParsedDrawing,
    issues: Iterable[Issue],
):
    """Render an HTML report to *output*.*"""

    template = _env.get_template(_TEMPLATE_NAME)
    html = template.render(
        drawing=str(drawing.path),
        issues=list(issues),
        issue_count=len(list(issues)),
    )

    pathlib.Path(output).write_text(html, encoding="utf-8")
