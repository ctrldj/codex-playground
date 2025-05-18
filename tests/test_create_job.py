"""Tests for the create_job CLI utility."""

from __future__ import annotations

import shutil
import subprocess
import sys
import timeit
from pathlib import Path

import create_job


def setup_module(module):
    """Ensure directories and template files exist for tests."""
    create_job.CLIENTS_DIR.mkdir(parents=True, exist_ok=True)
    create_job.TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
    for name in create_job.TEMPLATES:
        path = create_job.TEMPLATE_DIR / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("template")


def teardown_module(module):
    """Clean up created directories."""
    shutil.rmtree(create_job.CLIENTS_DIR, ignore_errors=True)
    shutil.rmtree(create_job.TEMPLATE_DIR, ignore_errors=True)
    shutil.rmtree(create_job.SHAREPOINT_DIR, ignore_errors=True)
    if Path("job_creation.log").exists():
        Path("job_creation.log").unlink()


def test_cli_creates_job(tmp_path):
    result = subprocess.run(
        [sys.executable, "create_job.py", "Acme", "ALT-N-9999 - Demo"],
        capture_output=True,
        text=True,
        check=True,
    )
    job_path = create_job.CLIENTS_DIR / "Acme" / "Jobs" / "ALT-N-9999 - Demo"
    assert job_path.exists()
    for dest in create_job.TEMPLATES.values():
        assert (job_path / dest).exists()
    assert "Created job" in result.stdout


def test_cli_existing_job():
    subprocess.run(
        [sys.executable, "create_job.py", "Acme", "ALT-N-9999 - Demo"],
        check=True,
    )
    result = subprocess.run(
        [sys.executable, "create_job.py", "Acme", "ALT-N-9999 - Demo"],
        capture_output=True,
        text=True,
    )
    assert "Job already exists" in result.stdout


def test_benchmark():
    stmt = "create_job.create_job('Acme', 'ALT-N-9999 - Benchmark', False)"
    timer = timeit.Timer(stmt=stmt, globals={'create_job': create_job})
    duration = min(timer.repeat(repeat=3, number=100))
    assert duration < 1
