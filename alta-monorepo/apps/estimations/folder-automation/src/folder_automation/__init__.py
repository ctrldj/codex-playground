"""## In one sentence, what this file does
Package initializer for folder automation."""

from .gui import run_gui
from .main import create_job_structure, main

__all__ = ["create_job_structure", "main", "run_gui"]
