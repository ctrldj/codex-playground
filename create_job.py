"""CLI to create job folders and copy templates."""

from __future__ import annotations

import argparse
import csv
import shutil
from datetime import datetime
from pathlib import Path

TEMPLATE_DIR = Path("/workspace/templates")
CLIENTS_DIR = Path("/workspace/clients")
SHAREPOINT_DIR = Path("/workspace/sharepoint")

TEMPLATES = {
    "[Gear List]-Blank ALTA Gear List.xlsx": "GearList.xlsx",
    "[Quote][SingleStage][NewClient]-Template.docx": "Quote.docx",
    "ASWHS005 SWMS Version 13 2022.docx": "SWMS.docx",
    "Blank ALTA Handover_Inspection Report 2024.pdf": "HandoverInspection.pdf",
    "Project Plan-Blank ALTA Project Plan.docx": "ProjectPlan.docx",
}


def _sanitise(name: str) -> str:
    """Replace characters illegal in Windows paths."""
    for ch in '/\\:*?"<>|':
        name = name.replace(ch, "-")
    return name


def _copy_templates(dest: Path) -> None:
    """Copy template files into *dest* with new names."""
    dest.mkdir(parents=True, exist_ok=True)
    for src_name, dest_name in TEMPLATES.items():
        src = TEMPLATE_DIR / src_name
        target = dest / dest_name
        if src.exists():
            shutil.copyfile(src, target)
        else:
            target.touch()


def _log(client: str, job: str, result: str) -> None:
    """Append a CSV entry to job_creation.log."""
    log_path = Path("job_creation.log")
    timestamp = datetime.utcnow().isoformat()
    with log_path.open("a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, client, job, result])


def create_job(client: str, job: str, sharepoint: bool = False) -> Path:
    """Create job folder and return its path."""
    client_s = _sanitise(client)
    job_s = _sanitise(job)
    job_path = CLIENTS_DIR / client_s / "Jobs" / job_s

    if job_path.exists():
        _log(client_s, job_s, "exists")
        raise FileExistsError(f"Job already exists: {job_path}")

    _copy_templates(job_path)
    if sharepoint:
        sp_path = SHAREPOINT_DIR / client_s / "Jobs" / job_s
        _copy_templates(sp_path)
    _log(client_s, job_s, "created")
    return job_path


def main() -> None:
    """Parse arguments and create the job folder."""
    parser = argparse.ArgumentParser(description="Create a new job folder")
    parser.add_argument("client")
    parser.add_argument("job")
    parser.add_argument("--sharepoint", action="store_true")
    args = parser.parse_args()

    try:
        path = create_job(args.client, args.job, args.sharepoint)
        print(f"Created job at {path}")
    except FileExistsError as exc:
        print(str(exc))


if __name__ == "__main__":  # pragma: no cover
    main()
