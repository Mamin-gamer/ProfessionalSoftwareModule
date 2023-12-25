def pmcc(x: list, y: list) -> float:
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")

    # Calculate the correlation coefficient
    num_points = len(x)
    if num_points <= 1:
        raise ValueError("Input arrays must have at least 2 element")

    # Calculate means
    mean_x = sum(x) / num_points
    mean_y = sum(y) / num_points

    # Calculate numerator and denominators
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(num_points))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(num_points)) ** 0.5
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(num_points)) ** 0.5

    denominator = denominator_x * denominator_y
    if denominator == 0:
        raise ZeroDivisionError(
            "The denominator in the slope calculation is zero. Cannot perform linear regression."
        )
    # Calculate correlation coefficient
    correlation_coefficient = numerator / denominator
    return correlation_coefficient


# calculates slope, intercept and correlation coefficient of 2 arrays
def linear_regression(x: list, y: list) -> tuple[float, float, float]:
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")

    if len(x) <= 1:
        raise ValueError("Input array x must have at least 2 elements")
    if len(y) <= 1:
        raise ValueError("Input array y must have at least 2 elements")

    # Calculate the means of x and y
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # Calculate the slope and intercept using least squares method
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(len(x)))

    # Avoid division by zero
    if denominator == 0:
        raise ZeroDivisionError(
            "The denominator in the slope calculation is zero. Cannot perform linear regression."
        )

    slope = numerator / denominator
    intercept = mean_y - slope * mean_x

    return slope, intercept, pmcc(x, y)


# calculates the mean of an array
def mean(x: list) -> float:
    if len(x) <= 0:
        raise ValueError("Input array must have at least 1 element")
    return round(sum(x) / len(x), 5)


# filters values from dictionary besed on keys specified
def filter_dict(dictionary: dict, keys: list[str] or tuple[str] or str) -> dict:
    if type(keys) not in [list, str, tuple]:
        raise ValueError("Keys must be a list, a tupe or a string")

    if type(keys) in [list, tuple]:
        for key in keys:
            if type(key) != str:
                raise ValueError("One of the elements of iterable is integer")

    return {key: value for key, value in dictionary.items() if key not in keys}
