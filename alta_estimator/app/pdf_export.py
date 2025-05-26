"""## In one sentence, what this file does
Utility to export estimation results to a PDF file."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from .estimator import EstimationResult

OUTPUT_DIR = Path("estimates")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_to_pdf(result: EstimationResult) -> Path:
    """Save the estimation result to a timestamped PDF."""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    pdf_path = OUTPUT_DIR / f"EST_{timestamp}.pdf"
    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    textobject = c.beginText(40, 800)
    text_lines = [
        f"Labour Cost: ${result.labour_cost:,.0f} ({result.workers} workers ",
        f"\u00d7 {result.hours} h @ $80/hr)",
        f"Hire Cost: ${result.hire_cost:,.0f} ({result.tonnes} tonnes @ $35/t)",
        f"Transportation Cost: ${result.transport_cost:,.0f} ({result.transport_type} truck)",
        f"Additional Costs: ${result.additional_costs:,.0f} ({', '.join(result.additional_reasons)})",
        f"Total Estimated Cost: ${result.total:,.0f}",
        "",
        "Estimation Notes:",
        "",
        "Assumption 1: ...",
        "",
        "Assumption 2: ...",
    ]
    for line in text_lines:
        textobject.textLine(line)
    c.drawText(textobject)
    c.showPage()
    c.save()
    return pdf_path
