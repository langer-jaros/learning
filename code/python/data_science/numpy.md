# NumPy

`2020, Dec. 1st, Jaroslav Langer`

Basically a mathematical library.

## Content

- [Content](#content)
- [Documentation](#documentation)
- [Installation](#installation)
- [Import](#import)
- [Variable types](#variable-types)
- [Math functions](#math-functions)
- [NumPy (N-dimensional) array (ndarray)](#numpy-n-dimensional-array-ndarray)
  - [Sort](#sort)
- [array dtypes (Array-protocol type strings)](#array-dtypes-array-protocol-type-strings)
- [Random](#random)

## Documentation

[NumPy documentation](https://numpy.org/doc/stable/reference/)

## Installation

## Import

```py
import numpy as np
```

## Variable types

```py
# Create NaN
NaN = np.nan

# nans can not be compered with ==, because the undefined things can not be the same
np.nan == np.nan # False

np.isnan(np.nan) # True

# Float
np.float

np.float64
```

## Math functions

```py
# Round number
np.round(theNumber, decimals=2)

# cube-root of one element or every element of an array
np.cbrt(x)
```

- [Round numpy](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.round_.html)
- [cbrt](https://numpy.org/doc/stable/reference/generated/numpy.cbrt.html)

## NumPy (N-dimensional) array (ndarray)

```py
a = np.array([[1,4],[3,1]])
```

- [numpy array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

### Indexing and slicing

```py
# It is possible to use comma instead of brackets
arr[0,1] #= arr[0][1]
```

### Sort

```py
a = np.array([[1,4],[3,1]])
# sort along the last axis
np.sort(a)
```
Output
```out
array([[1, 4],
       [1, 3]])
```

- [numpy sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)

## array dtypes (Array-protocol type strings)

| Character | Type                   |
| --------- | ---------------------- |
| 'b'       | boolean                |
| 'i'       | (signed) integer       |
| 'u'       | unsigned integer       |
| 'f'       | floating-point         |
| 'c'       | complex-floating point |
| 'O'       | (Python) objects       |
| 'S' , 'a' | (byte-)string          |
| 'U'       | Unicode                |
| 'V'       | raw data (void)        |

```py
# Examples
dt = np.dtype('i4')   # 32-bit signed integer ~ dtype('int32')
dt = np.dtype('f8')   # 64-bit floating-point number
dt = np.dtype('c16')  # 128-bit complex floating-point number
```

- [array dtypes source](https://docs.scipy.org/doc/numpy-1.10.1/reference/arrays.dtypes.html)

## Random

```py
numpy.random.seed(seed=42)  # Usually for testing purposes the seed is handy
sample = np.random.Generator.choice(array, size=features_num, replace=False)
```

- [choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice)

