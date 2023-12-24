import pandas as pd
import numpy as np


def pmcc(x: list, y: list) -> float:
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")

    # Calculate the correlation coefficient
    num_points = len(x)
    if num_points <= 0:
        raise ValueError("Input arrays must have at least 1 element")

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


def linear_regression(x: list, y: list):
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")

    if len(x) <= 0:
        raise ValueError("Input array x must have at least 1 element")
    if len(y) <= 0:
        raise ValueError("Input array y must have at least 1 element")

    # Calculate the means of x and y
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # Calculate the slope (m) and intercept (b) using least squares method
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(len(x)))

    # Avoid division by zero
    if denominator == 0:
        raise ValueError(
            "The denominator in the slope calculation is zero. Cannot perform linear regression."
        )

    slope = numerator / denominator
    intercept = mean_y - slope * mean_x

    return slope, intercept, pmcc(x, y)


def mean(x: list) -> float:
    if len(x) <= 0:
        raise ValueError("Input array must have at least 1 element")
    return round(sum(x) / len(x), 5)


# make function to check if element in array -> check if 0 there
# check if any 0s -> return can't do it
# check for dimentions?
#


def x_log_scale(Series_x: pd.Series, Series_y: pd.Series) -> np.ndarray:
    if len(Series_x) != len(Series_y):
        raise ValueError("Both series must be the same length")

    if len(Series_x) <= 0:
        raise ValueError("Series_x must have at least 1 element")
    if len(Series_y) <= 0:
        raise ValueError("Series_y must have at least 1 element")

    X = np.column_stack((np.ones_like(Series_x), Series_x))
    # Creates a matrix X by stacking two columns, where the first column consists of ones (for the intercept term) and the second column contains the values from the 'HDI' column of the DataFrame.

    y_log = np.log(Series_y)  # applies natural log to the whole GNI column

    theta = np.linalg.inv(X.T @ X) @ X.T @ y_log
    # uses formula for normal equation (https://www.datacamp.com/tutorial/tutorial-normal-equation-for-linear-regression or https://www.geeksforgeeks.org/ml-normal-equation-in-linear-regression/)
    # theta is a 2x1 matrix which are coefficients

    # Predicts the logarithmically transformed values of 'GNI'
    return X @ theta
