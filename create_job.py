import argparse
import csv
import os
import shutil
from datetime import datetime

TEMPLATE_DIR = os.environ.get('TEMPLATE_DIR', r'/workspace/templates')
CLIENTS_DIR = os.environ.get('CLIENTS_DIR', r'/workspace/clients')
SHAREPOINT_DIR = os.environ.get('SHAREPOINT_DIR', r'/workspace/sharepoint')

TEMPLATES = {
    '[Gear List]-Blank ALTA Gear List.xlsx': 'GearList.xlsx',
    '[Quote][SingleStage][NewClient]-Template.docx': 'Quote.docx',
    'ASWHS005 SWMS Version 13 2022.docx': 'SWMS.docx',
    'Blank ALTA Handover_Inspection Report 2024.pdf': 'HandoverInspection.pdf',
    'Project Plan-Blank ALTA Project Plan.docx': 'ProjectPlan.docx',
}

INVALID_CHARS = '/\\:*?"<>|'
LOG_PATH = os.path.join(os.path.dirname(__file__), 'job_creation.log')


def sanitize(name: str) -> str:
    """Replace invalid Windows path characters with hyphens."""
    return ''.join('-' if c in INVALID_CHARS else c for c in name)


def log_run(client: str, job: str, result: str) -> None:
    """Append a run entry to the log file."""
    ts = datetime.now().isoformat()
    new_entry = [ts, client, job, result]
    is_new = not os.path.exists(LOG_PATH)
    with open(LOG_PATH, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(['timestamp', 'client', 'job', 'result'])
        writer.writerow(new_entry)


def copy_templates(dest_path: str) -> None:
    """Copy template files into destination folder."""
    for src_name, dest_name in TEMPLATES.items():
        src = os.path.join(TEMPLATE_DIR, src_name)
        dest = os.path.join(dest_path, dest_name)
        shutil.copyfile(src, dest)


def create_job(client_name: str, job_name: str, sharepoint: bool = False) -> str:
    """Create a job folder populated with templates."""
    client = sanitize(client_name)
    job = sanitize(job_name)
    job_path = os.path.join(CLIENTS_DIR, client, 'Jobs', job)

    if os.path.exists(job_path):
        msg = f'Job already exists: {job_path}'
        log_run(client, job, msg)
        return msg

    os.makedirs(job_path)
    copy_templates(job_path)

    if sharepoint:
        sp_path = os.path.join(SHAREPOINT_DIR, client, 'Jobs', job)
        if not os.path.exists(sp_path):
            os.makedirs(sp_path)
            copy_templates(sp_path)

    result = f'Created job at {job_path}'
    log_run(client, job, result)
    return result


def main() -> None:
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(description='Create job folder with templates.')
    parser.add_argument('client', help='Client name')
    parser.add_argument('job', help='Job code and site address')
    parser.add_argument('--sharepoint', action='store_true', help='Also create SharePoint copy')
    args = parser.parse_args()
    msg = create_job(args.client, args.job, sharepoint=args.sharepoint)
    print(msg)


if __name__ == '__main__':
    main()
