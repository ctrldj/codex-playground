"""## In one sentence, what this file does
PySide6 GUI for collecting inputs and displaying scaffold cost estimations."""

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from .estimator import EstimationInput, MissingDataError, estimate
from .pdf_export import save_to_pdf


class EstimatorWindow(QWidget):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Alta Estimator")
        layout = QVBoxLayout(self)

        self.dimensions = QTextEdit()
        self.returns = QLineEdit()
        self.access = QComboBox()
        self.access.addItems(["ladder", "stair", "stretcher-stair"])
        self.project_details = QTextEdit()
        self.site_conditions = QTextEdit()
        self.project_complexities = QTextEdit()
        self.risks_hazards = QTextEdit()
        self.result_block = QLabel("Fill the form and click Estimate")
        self.estimate_button = QPushButton("Estimate")

        layout.addWidget(QLabel("Dimensions"))
        layout.addWidget(self.dimensions)
        layout.addWidget(QLabel("Number of Returns"))
        layout.addWidget(self.returns)
        layout.addWidget(QLabel("Access Type"))
        layout.addWidget(self.access)
        layout.addWidget(QLabel("Project Details"))
        layout.addWidget(self.project_details)
        layout.addWidget(QLabel("Site Conditions"))
        layout.addWidget(self.site_conditions)
        layout.addWidget(QLabel("Project Complexities"))
        layout.addWidget(self.project_complexities)
        layout.addWidget(QLabel("Risks & Hazards"))
        layout.addWidget(self.risks_hazards)
        layout.addWidget(self.estimate_button)
        layout.addWidget(self.result_block)

        self.estimate_button.clicked.connect(self.on_estimate)

    def popup(self, message: str) -> None:
        QMessageBox.warning(self, "Input Error", message)

    def on_estimate(self) -> None:
        try:
            number_returns = int(self.returns.text() or 0)
        except ValueError:
            self.popup("Number of returns must be an integer")
            return

        input_data = EstimationInput(
            dimensions=self.dimensions.toPlainText(),
            number_of_returns=number_returns,
            access_type=self.access.currentText(),
            project_details=self.project_details.toPlainText(),
            site_conditions=self.site_conditions.toPlainText(),
            project_complexities=self.project_complexities.toPlainText(),
            risks_hazards=self.risks_hazards.toPlainText(),
        )

        try:
            result = estimate(input_data)
        except MissingDataError as exc:
            self.popup(str(exc))
            return

        pdf_path = save_to_pdf(result)
        self.result_block.setText(
            f"Labour Cost: ${result.labour_cost:,.0f} ({result.workers} workers \u00d7 {result.hours} h @ $80/hr)\n"
            f"Hire Cost: ${result.hire_cost:,.0f} ({result.tonnes} tonnes @ $35/t)\n"
            f"Transportation Cost: ${result.transport_cost:,.0f} ({result.transport_type} truck)\n"
            f"Additional Costs: ${result.additional_costs:,.0f} ({', '.join(result.additional_reasons)})\n"
            f"Total Estimated Cost: ${result.total:,.0f}\n\n"
            "Estimation Notes:\n\nAssumption 1: ...\n\nAssumption 2: ...\n"
        )
        self.popup(f"PDF saved to {Path(pdf_path).absolute()}")


def main() -> int:
    app = QApplication(sys.argv)
    window = EstimatorWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
