# Scaffold Audit Tool

Automated 2-D scaffold drawing auditor compliant with **AS/NZS 4576** and **TG20:21**.

```bash
python -m scaffold_audit path/to/drawing.dxf
```

## Features

* Ingests DXF drawings (DWG/PDF support coming).
* Extensible rule-set via YAML.
* Generates annotated DXF + HTML report.
* JSON summary to `stdout` for CI pipelines.

## Installation (development)

```bash
poetry install
pytest
```

---

⚠️  Work-in-progress – geometry analysis still a stub.
