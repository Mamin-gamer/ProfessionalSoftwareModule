import numpy as np


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


x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
print(MyFunctions.pmcc(x, y))
print(np.corrcoef(x, y))
