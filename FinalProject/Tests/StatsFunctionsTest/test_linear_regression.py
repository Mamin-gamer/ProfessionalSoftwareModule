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
        # self.assertAlmostEqual(result[2], 0.9593663743374382, 7)

    def test_empty_input_x(self):
        # Test with empty input array x
        x = []
        y = [2, 4, 5, 4, 5]
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_empty_input_y(self):
        # Test with empty input array y
        x = [1, 2, 3, 4, 5]
        y = []
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_different_length(self):
        # Test when input arrays have different lengths
        x = [1, 2, 3]
        y = [2, 4, 5, 6]
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_single_element(self):
        # Test with input arrays containing a single element
        x = [1]
        y = [2]
        with self.assertRaises(ValueError):
            linear_regression(x, y)

    def test_zero_denominator(self):
        # Test when denominator is zero
        x = [1, 2, 3]
        y = [2, 2, 2]
        with self.assertRaises(ZeroDivisionError):
            linear_regression(x, y)


if __name__ == "__main__":
    unittest.main()
