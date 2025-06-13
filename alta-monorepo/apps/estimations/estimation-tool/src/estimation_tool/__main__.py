"""## In one sentence, what this file does
Command line interface for quick quotations."""
from __future__ import annotations

import argparse

from .core import (
    Component,
    calculate_complexity_multiplier,
    calculate_quote,
    calculate_tonnage,
)


def build_parser() -> argparse.ArgumentParser:
    """Create argument parser for a minimal demo."""
    parser = argparse.ArgumentParser(description="Simple scaffolding estimator")
    parser.add_argument("weight", type=float, help="Weight per component in kg")
    parser.add_argument("count", type=int, help="Number of components")
    return parser


def main() -> None:
    """Run a basic calculation from the CLI."""
    parser = build_parser()
    args = parser.parse_args()

    component = Component(weight_per_unit=args.weight, quantity=args.count)
    tonnage = calculate_tonnage([component])
    multiplier = calculate_complexity_multiplier()
    quote = calculate_quote(
        base_tonnage=tonnage,
        material_rate=100,
        setup_hours=5,
        daily_rate=50,
        duration=1,
        distance=10,
        transport_rate=1.5,
        transport_premium=0,
        equipment_daily_rate=20,
        profit_percentage=0.1,
        complexity_multiplier=multiplier,
    )
    print(f"Estimated quote: ${quote:.2f}")


if __name__ == "__main__":
    main()
