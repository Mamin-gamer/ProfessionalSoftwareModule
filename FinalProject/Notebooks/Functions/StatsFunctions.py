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


def linear_regression(x: list, y: list):
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")

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


def mean(x: list):
    return round(sum(x) / len(x), 5)
