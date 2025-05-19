## In one sentence, what this file does
"""HTML report generation via *Jinja2*."""

from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING, Iterable

try:
    from jinja2 import Environment, PackageLoader, select_autoescape
except ModuleNotFoundError:  # pragma: no cover – fallback when Jinja2 missing
    class _DummyEnv:
        def __init__(self, *args: str, **kwargs: str) -> None:  # noqa: D401
            """Ignore all arguments."""

        def get_template(self, _name: str):
            def render(**_kwargs: str) -> str:
                return "<html><body><p>Report generation unavailable.</p></body></html>"

            return type("_Template", (), {"render": staticmethod(render)})()

    Environment = _DummyEnv  # type: ignore
    class PackageLoader:  # type: ignore
        def __init__(self, *args: str, **kwargs: str) -> None:
            pass

    def select_autoescape(*_args: str, **_kwargs: str) -> None:
        """Fallback select_autoescape that does nothing."""
        return None

if TYPE_CHECKING:  # pragma: no cover - imports for type hints only
    from .core import Issue
    from .parser import ParsedDrawing
else:  # pragma: no cover - keep names for runtime type checks
    Issue = ParsedDrawing = object

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
