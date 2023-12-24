import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
import BasicFunctions as BF


class TestRegression(unittest.TestCase):
    def test_linear_regression_1(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        slope, intercept, _ = BF.linear_regression(x, y)
        self.assertAlmostEqual(slope, 2, 5)
        self.assertAlmostEqual(intercept, 0, 5)

    def test_linear_regression_2(self):
        x = [-1000, 0, 1000, 2000, 3000]
        y = [0, 1e-10, 1e-5, 1e-3, 1e-1]
        slope, intercept, _ = BF.linear_regression(x, y)
        self.assertAlmostEqual(slope, 2.009999999e-05, 5)
        self.assertAlmostEqual(intercept, 0.00010200003000000041, 5)

    def test_linear_regression_3(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8]

        with self.assertRaises(ValueError):
            BF.linear_regression(x, y)


if __name__ == "__main__":
    unittest.main()
