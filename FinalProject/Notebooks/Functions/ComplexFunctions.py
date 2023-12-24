import pandas as pd
import numpy as np


def y_pred_log(Series_x: pd.Series, Series_y: pd.Series) -> np.ndarray:
    if type(Series_x) != pd.Series:
        raise TypeError("Series_x must be a type of pd.Series")

    if type(Series_y) != pd.Series:
        raise TypeError("Series_y must be a type of pd.Series")

    if len(Series_x) != len(Series_y):
        raise ValueError("Both series must be the same length")

    if len(Series_x) <= 0:
        raise ValueError("Series_x must have at least 1 element")

    if len(Series_y) <= 0:
        raise ValueError("Series_y must have at least 1 element")

    if any(Series_x == 0):
        raise ValueError("Series_x contains 0. Can't take a log value of 0.")
    if any(Series_y == 0):
        raise ValueError("Series_y contains 0. Can't take a log value of 0.")

    X = np.column_stack((np.ones_like(Series_y), Series_y))
    # Creates a matrix X by stacking two columns, where the first column consists of ones (for the intercept term) and the second column contains the values from the 'HDI' column of the DataFrame.

    y_log = np.log(Series_x)  # applies natural log to the whole GNI column

    theta = np.linalg.inv(X.T @ X) @ X.T @ y_log
    # uses formula for normal equation (https://www.datacamp.com/tutorial/tutorial-normal-equation-for-linear-regression or https://www.geeksforgeeks.org/ml-normal-equation-in-linear-regression/)
    # theta is a 2x1 matrix which are coefficients

    # Predicts the logarithmically transformed values of 'GNI'
    return X @ theta
