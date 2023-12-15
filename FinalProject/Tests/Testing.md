# Test Cases Description

## PMCC Testing
### test_pmcc_1

Input:

```Python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
```
Expected Output:
MF.pmcc(x, y) should be approximately `0.9999999999999998` (rounded to 5 decimal places)

### test_pmcc_2

Input:
```Python
x = [1, 4, 7]
y = [2, 5, 8]
```
Expected Output:
MF.pmcc(x, y) should be `1` (rounded to 5 decimal places)

### test_pmcc_3

Input:
```Python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8]
```
Expected Output:
The function should raise a `ValueError`.


## PMCC Testing

### test_linear_regression_1

Input:
```Python 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
```
Expected Output:
MF.linear_regression(x, y) should return `slope = 2` and `intercept = 0` (both rounded to 5 decimal places)

### test_linear_regression_2

Input:
```Python 
x = [-1000, 0, 1000, 2000, 3000]
y = [0, 1e-10, 1e-5, 1e-3, 1e-1]
```
Expected Output:
MF.linear_regression(x, y) should return `slope = 2.009999999e-05` and `intercept = 0.00010200003000000041 `(both rounded to 5 decimal places)

### test_linear_regression_3

Input:
```Python 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8]
```
Expected Output:
The function should raise a `ValueError`.

## Mean Testing

### test_mean_1

Input:
```Python 
x = [0.4431219067559732, 0.9955325046011141, 0.4895360803525731, 0.7094668559199586, 0.7391678412763674, 0.14965917230966297, 0.22124855781227304, 0.7254636445908721, 0.04848459269099137, 0.5076379582407878]
```
Expected Output:
MF.mean(x) should be approximately `0.5029319114550573` (rounded to 5 decimal places)

test_mean_2

Input:
```Python 
x = [0.7213127433569494, 0.2766652914354414, 0.2608910855294788, 0.8345933892394475, 0.24364970031686872, 0.15553127837184544, 0.7979897288103084, 0.5692230611901159, 0.5774091691791065, 0.358296576788254]
```
Expected Output:
MF.mean(x) should be approximately `0.47955620242178154` (rounded to 5 decimal places)


