"""## In one sentence, what this file does
Unit tests for core estimation functions."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from estimation_tool.core import (
    Component,
    calculate_complexity_multiplier,
    calculate_quote,
    calculate_tonnage,
)


class CoreTests(unittest.TestCase):
    """Test calculations for correctness."""

    def test_tonnage(self) -> None:
        component = Component(weight_per_unit=10, quantity=5)
        self.assertEqual(calculate_tonnage([component]), 0.05)

    def test_complexity_multiplier(self) -> None:
        self.assertEqual(calculate_complexity_multiplier(1, 2, 1, 0.5), 1.0)

    def test_calculate_quote(self) -> None:
        component = Component(weight_per_unit=50, quantity=2)
        tonnage = calculate_tonnage([component])
        multiplier = calculate_complexity_multiplier()
        quote = calculate_quote(
            base_tonnage=tonnage,
            material_rate=10,
            setup_hours=1,
            daily_rate=5,
            duration=2,
            distance=1,
            transport_rate=1,
            transport_premium=0,
            equipment_daily_rate=0,
            profit_percentage=0.1,
            complexity_multiplier=multiplier,
        )
        self.assertAlmostEqual(round(quote, 2), 14.3)


if __name__ == "__main__":
    unittest.main()
