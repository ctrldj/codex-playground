"""## In one sentence, what this file does
Create a job folder and copy templated documents into it.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

# Default locations (Windows paths). Adjust if running on another OS.
BASE_DIR = Path(r"C:\Users\knigh\Sync\ALTA Front\Clients")
TEMPLATE_DIR = Path(r"C:\Users\knigh\Sync\ALTA Front\Templates")

# Mapping of template filename to output filename pattern
TEMPLATES = {
    "[Gear List]-Blank ALTA Gear List.xlsx": "{job}Gearlist.xlsx",
    "[Quote][SingleStage][NewClient]-Template.docx": "{job} Quotation.docx",
    "ASWHS005 SWMS Version 13 2022.docx": "{job} SWMS.docx",
    # Long file name split for readability
    "Blank ALTA Handover_Inspection Report 2024.pdf": (
        "{job} HandoverInspectionCertificate.pdf"
    ),
    "Project Plan-Blank ALTA Project Plan.docx": "{job} ProjectPlan.docx",
}


def create_job_structure(
    client_name: str,
    job_name: str,
    base_dir: Path = BASE_DIR,
    template_dir: Path = TEMPLATE_DIR,
) -> list[Path]:
    """Create directories and copy template files.

    Returns a list of created file paths.
    """
    client_dir = base_dir / client_name
    job_dir = client_dir / job_name

    # Ensure the client directory exists but do not fail if already present
    client_dir.mkdir(parents=True, exist_ok=True)

    # Create the job directory only if it does not already exist
    job_dir.mkdir(exist_ok=True)

    created_files: list[Path] = []

    for template_name, out_pattern in TEMPLATES.items():
        src = template_dir / template_name
        dst = job_dir / out_pattern.format(job=job_name)

        # Skip if the destination file already exists
        if dst.exists():
            continue

        # Skip if the template file is missing
        if not src.exists():
            print(f"Template missing: {src}")
            continue

        # Copy file metadata as well (e.g., modification time)
        shutil.copy2(src, dst)
        created_files.append(dst)

    return created_files


def main(argv: list[str] | None = None) -> None:
    """Entry point allowing future UI integration."""
    parser = argparse.ArgumentParser(description="Create a job folder from templates")
    parser.add_argument("client_name", help="Name of the client")
    parser.add_argument("job_name", help="Name of the job")
    parser.add_argument(
        "--base-dir",
        default=str(BASE_DIR),
        help="Folder that stores all client jobs",
    )
    parser.add_argument(
        "--template-dir",
        default=str(TEMPLATE_DIR),
        help="Folder containing template documents",
    )
    args = parser.parse_args(argv)

    files = create_job_structure(
        args.client_name,
        args.job_name,
        base_dir=Path(args.base_dir),
        template_dir=Path(args.template_dir),
    )

    job_folder = Path(args.base_dir) / args.client_name / args.job_name
    print(f"Created job folder at: {job_folder}")
    for f in files:
        print(f"Copied {f.name}")

    if not files:
        print("No new files were created (they may already exist).")


if __name__ == "__main__":  # pragma: no cover - manual execution only
    main()
