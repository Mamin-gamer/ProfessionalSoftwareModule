import numpy as np
from scipy import stats as st


class MyFunctions:
    def pmcc(x: list, y: list):
        if len(x) != len(y):
            raise ValueError("Input arrays must have the same length")

        # Calculate the correlation coefficient
        num_points = len(x)

        # Calculate means
        mean_x = sum(x) / num_points
        mean_y = sum(y) / num_points

        # Calculate numerator and denominators
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(num_points))
        denominator_x = sum((x[i] - mean_x) ** 2 for i in range(num_points)) ** 0.5
        denominator_y = sum((y[i] - mean_y) ** 2 for i in range(num_points)) ** 0.5

        # Calculate correlation coefficient
        correlation_coefficient = numerator / (denominator_x * denominator_y)
        return correlation_coefficient

    def linear_regression(x, y):
        meanx = np.mean(x)
        meany = np.mean(y)
        sigmax = np.std(x)
        sigmay = np.std(y)
        sigmaxy = np.sum(np.multiply(x - meanx, y - meany)) / (len(x))
        m = sigmaxy / (sigmax * sigmax)
        q = meany - m * meanx
        return m, q
