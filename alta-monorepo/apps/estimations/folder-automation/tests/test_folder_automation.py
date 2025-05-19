"""## In one sentence, what this file does
Unit tests for the folder-automation tool.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# Make the package importable during tests
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from folder_automation.main import TEMPLATES, create_job_structure


class TestJobFolderAutomation(unittest.TestCase):
    def setUp(self) -> None:
        # Create temporary directories for base and templates
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name) / "Clients"
        self.template_dir = Path(self.temp_dir.name) / "Templates"
        self.base_dir.mkdir()
        self.template_dir.mkdir()

        # Create dummy template files
        for name in TEMPLATES.keys():
            (self.template_dir / name).write_text("template")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_create_job_structure_creates_files(self) -> None:
        files = create_job_structure(
            "Acme", "Job1", base_dir=self.base_dir, template_dir=self.template_dir
        )
        expected = {
            self.base_dir
            / "Acme"
            / "Job1"
            / pattern.format(job="Job1")
            for pattern in TEMPLATES.values()
        }
        self.assertEqual(set(files), expected)
        for f in expected:
            self.assertTrue(f.exists())

    def test_create_job_structure_is_idempotent(self) -> None:
        create_job_structure(
            "Acme", "Job2", base_dir=self.base_dir, template_dir=self.template_dir
        )
        # Run again; no files should be reported created
        files = create_job_structure(
            "Acme", "Job2", base_dir=self.base_dir, template_dir=self.template_dir
        )
        self.assertEqual(files, [])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
