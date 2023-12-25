import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
from BasicFunctions import mean


class TestMean(unittest.TestCase):
    def test_valid_input_integer(self):
        x = [1, 2, 3, 4, 5]
        result = mean(x)
        self.assertAlmostEqual(result, 3.0, 5)

    def test_valid_input_float(self):
        x = [1.5, 2.5, 3.5, 4.5, 5.5]
        result = mean(x)
        self.assertAlmostEqual(result, 3.5, 5)

    def test_valid_input_mixed_types(self):
        x = [1, 2.5, 3, 4.5, 5]
        result = mean(x)
        self.assertAlmostEqual(result, 3.2, 5)

    def test_valid_input_negative_values(self):
        x = [-1, -2, -3, -4, -5]
        result = mean(x)
        self.assertAlmostEqual(result, -3.0, 5)

    def test_empty_input(self):
        x = []
        with self.assertRaises(ValueError):
            mean(x)


if __name__ == "__main__":
    unittest.main()
