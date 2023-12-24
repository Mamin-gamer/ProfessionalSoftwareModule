import unittest
import sys
import pandas as pd
import numpy as np


sys.path.insert(0, "FinalProject/Notebooks/Functions")
import ComplexFunctions as CF


class TestMain(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        series_x = pd.Series([1, 2, 3, 4, 5])
        series_y = pd.Series([2, 4, 5, 4, 5])
        result = CF.y_pred_log(series_x, series_y)
        self.assertIsInstance(result, np.ndarray)

    def test_series_x_not_pd_series(self):
        # Test when Series_x is not a pd.Series
        with self.assertRaises(TypeError):
            CF.y_pred_log([1, 2, 3], pd.Series([2, 4, 5]))

    def test_series_y_not_pd_series(self):
        # Test when Series_y is not a pd.Series
        with self.assertRaises(TypeError):
            CF.y_pred_log(pd.Series([1, 2, 3]), [2, 4, 5])

    def test_different_length(self):
        # Test when Series_x and Series_y have different lengths
        with self.assertRaises(ValueError):
            CF.y_pred_log(pd.Series([1, 2, 3]), pd.Series([2, 4, 5, 6]))

    def test_empty_series_x(self):
        # Test when Series_x is empty
        with self.assertRaises(ValueError):
            CF.y_pred_log(pd.Series([]), pd.Series([2, 4, 5]))

    def test_empty_series_y(self):
        # Test when Series_y is empty
        with self.assertRaises(ValueError):
            CF.y_pred_log(pd.Series([1, 2, 3]), pd.Series([]))

    def test_series_x_contains_zero(self):
        # Test when Series_x contains zero
        with self.assertRaises(ValueError):
            CF.y_pred_log(pd.Series([1, 2, 3, 0, 5]), pd.Series([2, 4, 5, 4, 5]))

    def test_series_y_contains_zero(self):
        # Test when Series_y contains zero
        with self.assertRaises(ValueError):
            CF.y_pred_log(pd.Series([1, 2, 3, 4, 5]), pd.Series([2, 4, 0, 4, 5]))


if __name__ == "__main__":
    unittest.main()
