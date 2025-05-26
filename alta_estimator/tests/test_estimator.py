"""## In one sentence, what this file does
Unit tests for the estimation logic."""

import unittest

from alta_estimator.app.estimator import EstimationInput, MissingDataError, estimate


class EstimatorTests(unittest.TestCase):
    def test_estimate_happy_path(self):
        input_data = EstimationInput(
            dimensions="3x3\n4x2",
            number_of_returns=2,
            access_type="ladder",
            project_details="basic project",
            site_conditions="flat",
            project_complexities="none",
            risks_hazards="none",
        )
        result = estimate(input_data)
        self.assertGreater(result.total, 0)
        self.assertGreaterEqual(result.workers, 1)

    def test_estimate_missing_data(self):
        input_data = EstimationInput(
            dimensions="",
            number_of_returns=1,
            access_type="ladder",
            project_details="",
            site_conditions="",
            project_complexities="",
            risks_hazards="",
        )
        with self.assertRaises(MissingDataError) as ctx:
            estimate(input_data)
        self.assertIn("dimensions", str(ctx.exception))

    def test_extreme_dimensions(self):
        dims = "\n".join(["10x10"] * 50)
        input_data = EstimationInput(
            dimensions=dims,
            number_of_returns=5,
            access_type="stretcher-stair",
            project_details="big project",
            site_conditions="rough/terrain",
            project_complexities="hazard/hazard",
            risks_hazards="risk/risk",
        )
        result = estimate(input_data)
        self.assertGreater(result.tonnes, 0)
        self.assertGreater(result.total, result.labour_cost)


if __name__ == "__main__":
    unittest.main()
