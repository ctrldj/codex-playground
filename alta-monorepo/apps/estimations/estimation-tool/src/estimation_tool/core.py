"""## In one sentence, what this file does
Core math functions for scaffold estimations."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Component:
    """Represents a scaffolding component with weight data."""

    weight_per_unit: float
    quantity: int

    def total_weight(self) -> float:
        """Return the total weight for this component."""
        if self.quantity < 0 or self.weight_per_unit < 0:
            raise ValueError("weight_per_unit and quantity must be non-negative")
        return self.weight_per_unit * self.quantity


def calculate_tonnage(components: Iterable[Component]) -> float:
    """Sum the weights of all components in tonnes."""
    total_kg = sum(c.total_weight() for c in components)
    return total_kg / 1000


def calculate_complexity_multiplier(
    h_factor: float = 1.0,
    a_factor: float = 1.0,
    s_factor: float = 1.0,
    t_factor: float = 1.0,
) -> float:
    """Multiply the provided complexity factors."""
    for factor in (h_factor, a_factor, s_factor, t_factor):
        if factor <= 0:
            raise ValueError("complexity factors must be positive")
    return h_factor * a_factor * s_factor * t_factor


def calculate_quote(
    base_tonnage: float,
    material_rate: float,
    setup_hours: float,
    daily_rate: float,
    duration: int,
    distance: float,
    transport_rate: float,
    transport_premium: float,
    equipment_daily_rate: float,
    profit_percentage: float,
    complexity_multiplier: float,
) -> float:
    """Return the final quote amount."""
    if any(x < 0 for x in (
        base_tonnage,
        material_rate,
        setup_hours,
        daily_rate,
        duration,
        distance,
        transport_rate,
        transport_premium,
        equipment_daily_rate,
        profit_percentage,
        complexity_multiplier,
    )):
        raise ValueError("all inputs must be non-negative")

    material_cost = (base_tonnage * material_rate) * complexity_multiplier
    labor_cost = (setup_hours + daily_rate * duration) * complexity_multiplier
    transport_cost = distance * transport_rate + transport_premium
    equipment_cost = duration * equipment_daily_rate
    subtotal = material_cost + labor_cost + transport_cost + equipment_cost
    profit_margin = subtotal * profit_percentage
    return subtotal + profit_margin
