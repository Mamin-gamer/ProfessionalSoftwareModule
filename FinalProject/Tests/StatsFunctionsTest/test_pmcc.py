import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
import BasicFunctions as BF


class TestPmcc(unittest.TestCase):
    def test_pmcc_1(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        self.assertAlmostEqual(BF.pmcc(x, y), 0.9999999999999998, 5)

    def test_pmcc_2(self):
        x = [1, 4, 7]
        y = [2, 5, 8]
        self.assertAlmostEqual(BF.pmcc(x, y), 1, 5)

    def test_pmcc_3(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8]
        with self.assertRaises(ValueError):
            BF.pmcc(x, y)


if __name__ == "__main__":
    unittest.main()
