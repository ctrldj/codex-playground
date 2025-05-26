"""## In one sentence, what this file does
Core cost estimation logic for scaffolding projects."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class EstimationInput:
    """Container for user inputs."""

    dimensions: str
    number_of_returns: int
    access_type: str
    project_details: str
    site_conditions: str
    project_complexities: str
    risks_hazards: str


@dataclass
class EstimationResult:
    """Container for formatted estimation results."""

    labour_cost: float
    workers: int
    hours: int
    hire_cost: float
    tonnes: float
    transport_cost: float
    transport_type: str
    additional_costs: float
    additional_reasons: List[str]
    total: float


# Estimation Logic
# 1. Identify missing details -> prompt user with a pop-up if critical info absent.
# 2. Labour
#    rate_per_worker = 80 # $/hour
#    workers, hours = derive_from_scope(dimensions, complexities, site_conditions)
#    labour_cost = workers * hours * rate_per_worker
# 3. Hire
#    hire_rate_per_tonne = 35
#    tonnes = estimate_tonnage(dimensions, complexities)
#    hire_cost = tonnes * hire_rate_per_tonne
# 4. Transport
#    if tonnes < 2.5: transport_cost = 280
#    elif tonnes < 7: transport_cost = 380
#    else: transport_cost = 480
# 5. Additional costs = sum(costs_from_complexities, costs_from_hazards)
# 6. Total = labour + hire + transport + additional

RATE_PER_WORKER = 80
HIRE_RATE_PER_TONNE = 35


class MissingDataError(Exception):
    """Raised when required input fields are missing."""


def derive_from_scope(dimensions: str, complexities: str, site_conditions: str) -> tuple[int, int]:
    """Very naive scope derivation to keep example simple."""

    base_hours = max(len(dimensions.splitlines()), 1) * 8
    hours = base_hours + complexities.count("/") * 2 + site_conditions.count("/") * 2
    workers = 2 if "stretcher" in complexities.lower() else 1
    return workers, hours


def estimate_tonnage(dimensions: str, complexities: str) -> float:
    """Rough tonnage estimation based on dimensions length."""

    lines = dimensions.splitlines()
    total_length = sum(len(line) for line in lines)
    complexity_factor = 1.5 if complexities else 1.0
    return round(max(total_length / 10, 1) * complexity_factor, 2)


def costs_from_complexities(complexities: str) -> float:
    return complexities.count("hazard") * 100


def costs_from_hazards(hazards: str) -> float:
    return hazards.count("risk") * 150


def estimate(input_data: EstimationInput) -> EstimationResult:
    """Run the estimation algorithm and return structured results."""

    missing_fields = [field for field, value in input_data.__dict__.items() if value is None or value == ""]
    if missing_fields:
        raise MissingDataError(f"Missing input(s): {', '.join(missing_fields)}")

    workers, hours = derive_from_scope(
        input_data.dimensions, input_data.project_complexities, input_data.site_conditions
    )
    labour_cost = workers * hours * RATE_PER_WORKER

    tonnes = estimate_tonnage(input_data.dimensions, input_data.project_complexities)
    hire_cost = tonnes * HIRE_RATE_PER_TONNE

    if tonnes < 2.5:
        transport_cost = 280
        truck = "small"
    elif tonnes < 7:
        transport_cost = 380
        truck = "medium"
    else:
        transport_cost = 480
        truck = "large"

    additional_complexities = costs_from_complexities(input_data.project_complexities)
    additional_hazards = costs_from_hazards(input_data.risks_hazards)
    additional_total = additional_complexities + additional_hazards
    reasons = []
    if additional_complexities:
        reasons.append("complexities")
    if additional_hazards:
        reasons.append("hazards")

    total = labour_cost + hire_cost + transport_cost + additional_total

    return EstimationResult(
        labour_cost=labour_cost,
        workers=workers,
        hours=hours,
        hire_cost=hire_cost,
        tonnes=tonnes,
        transport_cost=transport_cost,
        transport_type=truck,
        additional_costs=additional_total,
        additional_reasons=reasons,
        total=total,
    )
