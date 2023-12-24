import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
from BasicFunctions import pmcc


class TestPmcc(unittest.TestCase):
    def test_pmcc_valid(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        self.assertAlmostEqual(pmcc(x, y), 0.9999999999999998, 5)

    def test_pmcc_empty(self):
        x = []
        y = []
        with self.assertRaises(ValueError):
            pmcc(x, y)

    def test_pmcc_different_length(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8]
        with self.assertRaises(ValueError):
            pmcc(x, y)


if __name__ == "__main__":
    unittest.main()
