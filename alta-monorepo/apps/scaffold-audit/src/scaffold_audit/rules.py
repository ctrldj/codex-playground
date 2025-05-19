## In one sentence, what this file does
"""Rule engine – loads YAML rules and evaluates them against a drawing."""

from __future__ import annotations

import importlib
import pathlib
from typing import Callable, Iterable, List

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover – fallback for limited envs

    def safe_load(text: str) -> dict:
        """Very small YAML subset parser used when PyYAML is unavailable."""
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        result: dict[str, list[dict[str, str]]] = {"rules": []}
        current: dict[str, str] | None = None
        for line in lines:
            if line.startswith("rules:"):
                if current:
                    result["rules"].append(current)
                    current = None
                continue
            if line.startswith("-"):
                if current:
                    result["rules"].append(current)
                current = {"id": line.split(":", 1)[1].strip()}
            elif line.startswith("description:") and current is not None:
                current["description"] = line.split(":", 1)[1].strip()
            elif line.startswith("check:") and current is not None:
                current["check"] = line.split(":", 1)[1].strip()
        if current:
            result["rules"].append(current)
        return result

    yaml = type("_YamlStub", (), {"safe_load": staticmethod(safe_load)})()

from .parser import ParsedDrawing

# Type alias for rule check callbacks.
CheckFn = Callable[[ParsedDrawing], Iterable[str]]


class Rule:
    """Represents a single audit rule."""

    def __init__(self, identifier: str, description: str, check: CheckFn):
        self.id = identifier
        self.description = description
        self.check = check

    # For nicer *pytest* assertion diffs.
    def __repr__(self) -> str:  # pragma: no cover
        return f"Rule(id={self.id!r})"


class RuleEngine:
    """Executes a collection of rules against a drawing and gathers issues."""

    def __init__(self, rules: Iterable[Rule]):
        self._rules: list[Rule] = list(rules)

    # Public API ----------------------------------------------------------------

    def evaluate(self, drawing: ParsedDrawing):  # noqa: D401 – returns list
        """Run all rules and return a list of issues (as :class:`str`)."""

        issues: list[str] = []
        for rule in self._rules:
            for message in rule.check(drawing):
                issues.append(f"{rule.id}: {message}")
        return issues


# ---------------------------------------------------------------------------
# YAML loader                                                                 
# ---------------------------------------------------------------------------


def _resolve_check(name: str) -> CheckFn:
    """Resolve dotted ``module:function`` reference to a Python callable."""

    try:
        module_name, func_name = name.rsplit(":", 1)
    except ValueError as exc:  # pragma: no cover – validated at load time
        raise ValueError(
            f"Rule 'check' attribute must be in 'module:function' format (got "
            f"{name!r})."
        ) from exc

    module = importlib.import_module(module_name)
    check = getattr(module, func_name)
    if not callable(check):
        raise TypeError(f"{check!r} is not callable.")

    return check  # type: ignore[return-value]


def load_rules(path: str | pathlib.Path) -> List[Rule]:
    """Load rule definitions from *path* (YAML)."""

    p = pathlib.Path(path)
    data = yaml.safe_load(p.read_text())

    rules: list[Rule] = []
    for raw in data.get("rules", []):
        identifier = raw["id"]
        description = raw.get("description", "")
        check_ref = raw.get("check")
        if check_ref is None:
            raise ValueError(f"Rule {identifier!r} missing 'check'.")

        check = _resolve_check(check_ref)
        rules.append(Rule(identifier, description, check))

    return rules
