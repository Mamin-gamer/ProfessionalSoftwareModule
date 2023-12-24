import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
import StatsFunctions as MF


class TestMain(unittest.TestCase):
    def test_pmcc_1(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        self.assertAlmostEqual(MF.pmcc(x, y), 0.9999999999999998, 5)

    def test_pmcc_2(self):
        x = [1, 4, 7]
        y = [2, 5, 8]
        self.assertAlmostEqual(MF.pmcc(x, y), 1, 5)

    def test_pmcc_3(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8]
        with self.assertRaises(ValueError):
            MF.pmcc(x, y)

    def test_linear_regression_1(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        slope, intercept, _ = MF.linear_regression(x, y)
        self.assertAlmostEqual(slope, 2, 5)
        self.assertAlmostEqual(intercept, 0, 5)

    def test_linear_regression_2(self):
        x = [-1000, 0, 1000, 2000, 3000]
        y = [0, 1e-10, 1e-5, 1e-3, 1e-1]
        slope, intercept, _ = MF.linear_regression(x, y)
        self.assertAlmostEqual(slope, 2.009999999e-05, 5)
        self.assertAlmostEqual(intercept, 0.00010200003000000041, 5)

    def test_linear_regression_3(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8]

        with self.assertRaises(ValueError):
            MF.linear_regression(x, y)

    def test_mean_1(self):
        x = [
            0.4431219067559732,
            0.9955325046011141,
            0.4895360803525731,
            0.7094668559199586,
            0.7391678412763674,
            0.14965917230966297,
            0.22124855781227304,
            0.7254636445908721,
            0.04848459269099137,
            0.5076379582407878,
        ]
        self.assertAlmostEqual(MF.mean(x), (0.5029319114550573), 5)

    def test_mean_2(self):
        x = [
            0.7213127433569494,
            0.2766652914354414,
            0.2608910855294788,
            0.8345933892394475,
            0.24364970031686872,
            0.15553127837184544,
            0.7979897288103084,
            0.5692230611901159,
            0.5774091691791065,
            0.358296576788254,
        ]
        self.assertAlmostEqual(MF.mean(x), (0.47955620242178154), 5)


if __name__ == "__main__":
    unittest.main()
