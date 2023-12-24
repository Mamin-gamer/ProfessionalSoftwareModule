import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
from BasicFunctions import mean


class TestMean(unittest.TestCase):
    def test_valid_input_integer(self):
        # Test with valid input (integer values)
        x = [1, 2, 3, 4, 5]
        result = mean(x)
        self.assertAlmostEqual(result, 3.0, 5)

    def test_valid_input_float(self):
        # Test with valid input (float values)
        x = [1.5, 2.5, 3.5, 4.5, 5.5]
        result = mean(x)
        self.assertAlmostEqual(result, 3.5, 5)

    def test_valid_input_mixed_types(self):
        # Test with valid input (mixed integer and float values)
        x = [1, 2.5, 3, 4.5, 5]
        result = mean(x)
        self.assertAlmostEqual(result, 3.2, 5)

    def test_valid_input_negative_values(self):
        # Test with valid input (negative values)
        x = [-1, -2, -3, -4, -5]
        result = mean(x)
        self.assertAlmostEqual(result, -3.0, 5)

    def test_empty_input(self):
        # Test with empty input array
        x = []
        with self.assertRaises(ValueError):
            mean(x)


if __name__ == "__main__":
    unittest.main()
