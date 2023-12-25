import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
from BasicFunctions import linear_regression


class TestRegression(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        slope, intercept, _ = linear_regression(x, y)

        self.assertAlmostEqual(slope, 0.6, 5)
        self.assertAlmostEqual(intercept, 2.2, 5)

    def test_empty_input_x(self):
        x = []
        y = [2, 4, 5, 4, 5]
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_empty_input_y(self):
        x = [1, 2, 3, 4, 5]
        y = []
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_different_length(self):
        x = [1, 2, 3]
        y = [2, 4, 5, 6]
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_single_element(self):
        x = [1]
        y = [2]
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_zero_denominator(self):
        x = [1, 2, 3]
        y = [2, 2, 2]
        with self.assertRaises(ZeroDivisionError):
            linear_regression(x, y)


if __name__ == "__main__":
    unittest.main()
