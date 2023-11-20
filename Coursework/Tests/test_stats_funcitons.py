import unittest
import sys

sys.path.insert(0, "Coursework/Notebooks/Functions")
from StatsFunctions import MyFunctions as MF


class TestMain(unittest.TestCase):
    def test_pmcc_1(self):
        x = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]
        y = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
        self.assertAlmostEqual(MF.pmcc(x, y), 0.95750662, 7)

    def test_pmcc_2(self):
        x = [1, 4, 7]
        y = [2, 5, 8]
        self.assertAlmostEqual(MF.pmcc(x, y), 1, 7)

    def test_pmcc_3(self):
        x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
        y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
        self.assertAlmostEqual(MF.pmcc(x, y), 0.14499815, 7)

    def test_linear_regression_1(self):
        x = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]
        y = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
        self.assertAlmostEqual(
            MF.linear_regression(x, y), (0.030471388740135587, 6.412805314490438), 5
        )
