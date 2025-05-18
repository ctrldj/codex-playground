## Job Folder Automation

This repo also provides a simple script to create job folders from a set of templates.

### Setup
- Place template files in `/workspace/templates`.
- Ensure `/workspace/clients` exists for new jobs.
- (Optional) create `/workspace/sharepoint` if you use the `--sharepoint` flag.

### How to run
```bash
python create_job.py "Acme" "ALT-N-9999 - Demo"
python create_job.py "Acme" "ALT-N-9999 - Demo" --sharepoint
```

### Extending templates
Edit the `TEMPLATES` mapping in `create_job.py` to add or remove files.

### Glossary
- **Template**: A file copied into each new job folder.
- **SharePoint**: Optional second location mirroring the job folder.