"""Basic smoke tests using the *unittest* framework (no external deps)."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class TestAuditCLI(unittest.TestCase):
    def _create_dummy_dxf(self, path: Path) -> None:
        # Minimal DXF string (generated via ezdxf once, kept static to avoid
        # runtime dependency).  Contains a single empty modelspace.
        dxf_content = (
            "0\nSECTION\n2\nHEADER\n0\nENDSEC\n0\nSECTION\n2\nTABLES\n0\nENDSEC\n0\nSECTION\n2\nBLOCKS\n0\nENDSEC\n0\nSECTION\n2\nENTITIES\n0\nENDSEC\n0\nSECTION\n2\nOBJECTS\n0\nENDSEC\n0\nEOF\n"
        )

        path.write_text(dxf_content)

    def test_cli_runs_and_outputs_json(self):
        with tempfile.TemporaryDirectory() as tmp_dir_str:
            tmp_dir = Path(tmp_dir_str)
            dxf_path = tmp_dir / "dummy.dxf"
            self._create_dummy_dxf(dxf_path)

            proc = subprocess.run(
                [sys.executable, "-m", "scaffold_audit", str(dxf_path)],
                capture_output=True,
                text=True,
            )

            # Exit code should be 0 as there are no issues.
            self.assertEqual(proc.returncode, 0, proc.stderr)

            # Stdout must be valid JSON with expected keys.
            payload = json.loads(proc.stdout)
            self.assertEqual(payload["issue_count"], 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
