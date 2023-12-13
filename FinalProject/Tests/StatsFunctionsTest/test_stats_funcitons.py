import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
import StatsFunctions as MF


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
        slope, intercept, pmcc = MF.linear_regression(x, y)
        self.assertAlmostEqual(slope, 0.03047138874013559, 5)
        self.assertAlmostEqual(intercept, 6.412805314490436, 5)
        self.assertAlmostEqual(pmcc, 0.9575066230015953, 5)

    def test_linear_regression_2(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        slope, intercept, pmcc = MF.linear_regression(x, y)
        self.assertAlmostEqual(slope, 1.0, 5)
        self.assertAlmostEqual(intercept, 0.0, 5)
        self.assertAlmostEqual(pmcc, 1.0, 5)

    def test_linear_regression_3(self):
        x = [
            0.16503776751270371,
            0.9333554107698349,
            0.06635496373780148,
            0.391925905161544,
            0.2903904906517738,
            0.5026479582027492,
            0.786066430054384,
            0.7531657935752609,
            0.447151232926997,
            0.32274221648060586,
        ]
        y = [
            0.9233610796408839,
            0.5488327294250499,
            0.15987990458726142,
            0.021432404060072185,
            0.7604710484264448,
            0.5531705376078131,
            0.4818162359960605,
            0.4199868183230754,
            0.6592129905082018,
            0.41854571966835763,
        ]

        slope, intercept, pmcc = MF.linear_regression(x, y)
        self.assertAlmostEqual(slope, 0.004009513814945507, 5)
        self.assertAlmostEqual(intercept, 0.4928029792242723, 5)
        self.assertAlmostEqual(pmcc, 0.004244714724793445, 5)

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