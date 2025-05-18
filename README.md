# ALTA Scaffolding – Job-Folder Automation

This repository provides a small utility to create pre-populated job folders for ALTA Scaffolding.

## Usage

```bash
python create_job.py "Acme" "ALT-N-9999 - Demo" --sharepoint
```

This will create a new job directory under `/workspace/clients/Acme/Jobs/ALT-N-9999 - Demo/` containing copies of the standard templates. If `--sharepoint` is supplied an identical folder hierarchy is created under `/workspace/sharepoint`.

### Extending the template list
Edit the `TEMPLATES` dictionary in `create_job.py` to add or remove files. Keys are source template names located in `/workspace/templates` and values are the desired file names in the new job folder.

## Development

Run all tests with:

```bash
pytest
```

The benchmark test asserts that creating 100 jobs averages under one second.
