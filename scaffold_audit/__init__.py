"""Top-level package for Scaffold Audit Tool.

Contains version information and central exports.
"""

from importlib import metadata


__all__: list[str] = [
    "__version__",
]


def _get_version() -> str:  # pragma: no cover
    """Return the package version from metadata.

    Falls back to "0.0.0" if distribution metadata is unavailable (e.g. during
    editable installs without a build backend).
    """

    try:
        return metadata.version(__name__)
    except metadata.PackageNotFoundError:
        # Local, editable install – version is unknown.
        return "0.0.0"


__version__: str = _get_version()


################################################################################
# Convenience re-exports (for typers’ delight)                                #
################################################################################

# The main public API lives behind these names so that users can simply do:
# `from scaffold_audit import audit_file`

from .core import audit_file as audit_file  # noqa: E402  (import after __version__)
