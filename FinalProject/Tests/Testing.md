# Test Cases Description

This file contains descripton for test cases in `StatsFunctionTest` folder

## PMCC

The function takes 2 arrays as parameters: x and y and returns a float that represents a correlation coefficient.


--- 

The formula for Pearson's correlation coefficient:

$$ r =
  \frac{ \sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y}) }{%
        \sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}}

$$


Where:

- n is the number of data points.
- $x_i$ and $y_i$ are the individual data points.
- $\bar{x}$ and $\bar{y}$ are the means of x and y respectively
 


---
### test_pmcc_valid
Input data:
```Python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
```
**Expected result**: the function should return `0.9999999999999998` and throw no errors, as the numbers in both arrays are not erroneous.


### test_pmcc_empty
Input data:
```Python
x = []
y = []
```

**Expected result**: the function should throw a `ValueError`, as both arrays are empty, hence the coreation coefficient cannot be calculated

### test_pmcc_different_length
Input data:
```Python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8]
```
**Expected result** : the function should throw a `ValueError`, as arrays aren't the same size, hence the correlation coefficient cannot be calculated.


### test_zero_denominator
Input data: 
```Python
x = [1, 2, 3]
y = [2, 2, 2]
```

**Expected result**: the function should throw a `ZeroDivisionError`, as values of X array increase, but values in Y array stay constant. In this example $(x_i-\bar{x})^2$  and $(y_i-\bar{y})^2$ are all equal to 1, as the difference between each data point and the mean is 1. This results in both the numerator and denominator being 0. Hence, `ZeroDivisionError`

### test_empty_input_x
Input data: 
```Python 
x = []
y = [2, 4, 5, 4, 5]
```

**Expected Result**: the function should throw a `ValueError`, as it is impossible to calculate the correlation coefficient with different sizes arrays.

### test_single_element

Input data: 
```Python
x = [1]
y = [2]
```

**Expected Result**: the function should throw a `ValueErrow`, as calculating a correlation coefficient with only one data point can lead to issues. The denominators involve the squared differences from the mean, and with only one element, the difference is zero


## Linear Regression

The formula for linear regression:
$$
slope=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}\\
$$

$$
intercept = \bar y - slope * \bar x
$$

The function takes 2 arrays as parameters: x and y and returns a tuple of floats: slope, intercept and correlation coefficient using PMCC function.


### test_valid_input
Input data: 
```Python
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
```

**Expected Result**: the function should return slope of `0.6`, intercecpt of `2.2` and a correlation coefficient, which we don't test for, as testing for PMCC function has been done 

### test_empty_input_x

Input data:

```python
x = []
y = [2, 4, 5, 4, 5]
```
**Expected Result**: the function should throw a `ValueError`, as arrays must be the same size to calculate a linear regression


### test_empty_input_y

Input data:

```python
x = [1, 2, 3, 4, 5]
y = []
```
**Expected Result**: the function should throw a `ValueError`, as arrays must be the same size to calculate a linear regression

### test_different_length

Input data:

```python
x = [1, 2, 3]
y = [2, 4, 5, 6]
```
**Expected Result**: the function should throw a `ValueError`, as arrays must be the same size to calculate a linear regression



### test_different_length

Input data:

```python
x = [1, 2, 3]
y = [2, 4, 5, 6]
```
**Expected Result**: the function should throw a `ValueError`, as arrays must be the same size to calculate a linear regression


### test_single_element
Input data:

```python
x = [1]
y = [2]
```
**Expected Result**: the function should throw a `ValueError`, as there must be more than 1 element in each array to calculate linear regression


### test_zero_denominator
Input data:

```python
x = [1, 2, 3]
y = [2, 2, 2]
```
**Expected Result**: the function should throw a `ZeroDivisionError`, as the denominator of slope will be 0, as $(x_i-\bar x)^2$ is 0 due to $\bar x$ and $x$ are the same value.


## Mean

Formula for mean:

$$
\hat{x} = \frac{\sum{x}}{N}
$$
where N is number of elements in the array

### test_valid_input_integer
Input data:

```python
x = [1, 2, 3, 4, 5]
```
**Expected Result**: the function should return `3.0`.

### test_valid_input_float
Input data:

```python
x = [1, 2, 3, 4, 5]
```
**Expected Result**: the function should return `3.5`.


### test_valid_input_mixed_types
Input data:

```python
x = [1, 2.5, 3, 4.5, 5]
```
**Expected Result**: the function should return `3.2`.


### test_valid_input_negative_values
Input data:

```python
 x = [-1, -2, -3, -4, -5]
```
**Expected Result**: the function should return `-3.0`.


### test_valid_input_negative_values
Input data:

```python
x = []
```
**Expected Result**: the function should throw a `ValueError`, as to calculate mean there must be at least 1 element in the array



## Filter dictionary

I needed to write a function to filter dictionary for keyword arguments that aren't in visualisation tools functions' parameters.

The function takes a dictionary and an iterable or a string that needs to be filered out from that dictionary. 

### test_valid_input
Input data:

```python
input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_filter = ["b", "d"]
```
**Expected Result**: 
```py
{"a": 1, "c": 3}
```

### test_empty_input_dict
Input data:

```python
input_dict = {}
keys_to_filter = ["b", "d"]
```
**Expected Result**: 
```py
{}
```

### test_empty_keys_to_filter
Input data:

```python
input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_filter = []
```
**Expected Result**: 
```py
{"a": 1, "b": 2, "c": 3, "d": 4}
```

### test_keys_not_in_dict
Input data:

```python
input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_filter = ["b", "e"]
```
**Expected Result**: 
```py
{"a": 1, "c": 3, "d": 4}
```

### test_invalid_keys_type
Input data:

```python
input_dict = {"a": 1, "b": 2, "c": 3}
keys_to_filter = ["a", 123]
```
**Expected Result**: The function should throw a `ValueError`, as one of the elements in `keys_to_filter` is an integer



## Logarithmic scaling

I created a function that predicts coefficients for liear regression model using normal equation formula using matrix manipulation with numpy in order to adjust the line of best fit when the graph is scaled logarithmically

The function takes 2 pandas series as parameters and outputs a numpy ndarray.

### test_valid_input
Input data:

```python
series_x = pd.Series([1, 2, 3, 4, 5])
series_y = pd.Series([2, 4, 5, 4, 5])
```
**Expected Result**: the type of returned variable is `numpy.ndarray`


### test_series_x_not_pd_series
Input data:

```python
series_x = [1, 2, 3]
series_y = pd.Series([2, 4, 5])
```
**Expected Result**: the function throws a `TypeError` as `series_x` isn't a type of `numpy.ndarray`

### test_series_y_not_pd_series
Input data:

```python
series_x = pd.Series([1, 2, 3])
series_y = [2, 4, 5]
```
**Expected Result**: the function throws a `TypeError` as `series_y` isn't a type of `numpy.ndarray`

### test_different_length
Input data:

```python
series_x = pd.Series([1, 2, 3])
series_y = pd.Series([2, 4, 5, 6])
```
**Expected Result**: the function throws a `ValueError` arrays aren't the same size


### test_empty_series_x
Input data:

```python
series_x = pd.Series([])
series_y = pd.Series([2, 4, 5])
```
**Expected Result**: the function throws a `ValueError` arrays aren't the same size



### test_empty_series_y
Input data:

```python
series_x = pd.Series([1, 2, 3])
series_y = pd.Series([])
```
**Expected Result**: the function throws a `ValueError` arrays aren't the same size



### test_series_x_contains_zero
Input data:

```python
series_x = pd.Series([1, 2, 3, 0, 5])
series_y = pd.Series([2, 4, 5, 4, 5])
```
**Expected Result**: the function throws a `ValueError` as one of the elements is 0 and a value of $\log{0}$ is undefined



### test_series_y_contains_zero
Input data:

```python
series_x = pd.Series([1, 2, 3, 4, 5])
series_y = pd.Series([2, 4, 0, 4, 5])
```
**Expected Result**: the function throws a `ValueError` as one of the elements is 0 and a value of $\log{0}$ is undefined





