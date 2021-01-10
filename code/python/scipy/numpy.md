# NumPy

The fundamental package for scientific computing with Python.

`2021 Jan 09, Jaroslav Langer`

## Content

- [References](#references)
- [Installation](#installation)
- [Import](#import)
- [Variable types](#variable-types)
- [Math functions](#math-functions)
- [Randomness](#randomness)
- [NumPy (N-dimensional) array (ndarray)](#numpy-n-dimensional-array-ndarray)
  - [Create numpy array](#create-numpy-array)
  - [Too big array problem](#too-big-array-problem)
  - [Array basics](#array-basics)
  - [Array dtypes (Array-protocol type strings)](#array-dtypes-array-protocol-type-strings)
  - [Indexing and slicing](#indexing-and-slicing)
  - [Copy](#copy)
  - [Useful functions](#useful-functions)
  - [Matrix functions](#matrix-functions)
- [Linear Algebra](#linear-algebra)
- [Statistics](#statistics)
- [Binary Operations](#binary-operations)
- [Logic](#logic)

## References

- [Tentative_NumPy_Tutorial](https://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial)
- [NumPy documentation](https://numpy.org/doc/stable/reference/)

## Installation

If i recall it properly it was necessary to install the numpy outside of the virtual environment.

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

## Randomness

```py
# the generator approach
rg = np.random.default_rng(42)
rg.choice([1,2,3,4], size=2, replace=False)     # array([1, 4])
rg.choice([1,2,3,4], size=2, replace=False)     # array([3, 2])
sample = rng.choice(array, size=features_num, replace=False)

# The old way
numpy.random.seed(seed=42)  # Usually for testing purposes the seed is handy

np.random.choice(5, 3)
```

- [np.random.Generator](https://numpy.org/devdocs/reference/random/generator.html#numpy.random.Generator)
- [choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice)

## NumPy (N-dimensional) array (ndarray)

### Create numpy array

```py
# Create from list
np.array([[1,4],[3,1]])

# Create array by shape
np.ndarray((2,2))   # array([[1.07917455e-316, 6.93631821e-310], [6.93631821e-310, 3.39285907e-310]])

# Create 0s array (filled with zeros)
np.zeros((2,2,1))   # array([[[0.], [0.]], [[0.], [0.]]])

# Create 1s array (filled with ones)
np.ones((2,1,2))    # array([[[1., 1.]], [[1., 1.]]])

# Create array of evenly spaced values (i.e. 1, 2, 3)
np.arange(4)        # array([0, 1, 2, 3])
```

- [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
- [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
- [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)

### Too big array problem

Be careful, when array is created with zeros(), ones() etc. the array is not really initialized, so you can create array bigger than can fit to the memory. It will crash as you will need to use the values. It was not clear to me from the beginning.

- [ Why doesn't numpy.zeros allocate all of its memory on creation? And how can I force it to?](https://stackoverflow.com/questions/51314255/why-doesnt-numpy-zeros-allocate-all-of-its-memory-on-creation-and-how-can-i-fo)

### Array basics

```py
# Shape - Return the shape of an array.
arr.shape               # (2, 2)

# Delete item(s) - delte first column
arr = np.delete(arr, 0, axis=1)     # array([[4], [1]])

# Reshape array arr. arr.shape == (2, 2) -> (2, 1, 2)
arr = np.reshape(arr, (2, 1, 2))    # array([[[1, 4]], [[3, 1]]])

# Append items to the array
np.append([[1, 2], [3, 4]], [[5], [6]], axis=1) # array([[1, 2, 5], [3, 4, 6]])
```

- [np.delete](https://numpy.org/doc/stable/reference/generated/numpy.delete.html)
- [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
- [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html)

### Array dtypes (Array-protocol type strings)

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

Smallest data type has 1 byte per value. [stackoverflow](https://stackoverflow.com/questions/53999299/specifying-numpy-arrays-with-2-bit-dtype)

Examples:

```py
# 32-bit signed integer ~ dtype('int32')
np.dtype('i4')                              # dtype('int32')
np.zeros((2,2), dtype='i4').dtype           # dtype('int32')

# 64-bit floating-point number
np.ones((2,2), dtype=np.dtype('f8')).dtype  # dtype('float64')
np.ones((2,2), dtype='f4').dtype            # dtype('float32')

# 128-bit complex floating-point number
np.eye(2, dtype='c16').dtype                # dtype('complex128')
```

- [array dtypes source](https://docs.scipy.org/doc/numpy-1.10.1/reference/arrays.dtypes.html)

### Indexing and slicing

- [Indexing (numpy.org)](https://numpy.org/devdocs/reference/arrays.indexing.html)

```py
arr = np.array([[1,4,7],[2,5,8],[3,6,9]])
# Indices and slices works the same as the classical list
arr[0][1] # 4       - return second item of the first row

arr[:][0] # [1,4,7] - [:] does nothing, equivalent to a[0]
# Numpy enables to acessing slices of all the axis not only the last one
arr[:,0]  # [1,2,3] - [:,0] this specifies all items along axis=0 and first indices along axis=1
```

- [numpy indexing (stackoverflow](https://stackoverflow.com/questions/38113994/why-does-indexing-numpy-arrays-with-brackets-and-commas-differ-in-behavior)

### Copy

```py
# Copy - classics a = b will be the same matrix
a = np.array([[1,2,3],[3,4,5]])
b = a;
a[0][0] = 666
print(b[0][0])  # 666

a = np.array([[1,2,3],[3,4,5]])
b = a.copy();
a[0][0] = 666
print(b[0][0])  # 1
```

- [copy (numpy.org)](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html)

### Useful functions

```py
# Sum - sum of array elements over a given axis.
np.sum([[3,4], [2,1]], axis=1)      # array([7, 3])

# Mean - mean elements over given axis (mean of all element if axis not given)
np.mean([[3,4], [2,1]], axis=0)      # array([2.5, 2.5])

# Max - return the maximal number
np.array([[3,4], [1,5]]).max()      # 5
np.max([[3,4], [1,5]])              # 5

# Argmax - returns the index of the maximal value(s) along an axis.
np.argmax([[3,4], [2,1]], axis=1)   # array([1, 0])

# Elementwise check for NaNs
np.isnan([[3,4], [np.nan,1]])       # array([[False, False], [ True, False]])

# Sort along the last axis
np.sort([[1,4],[3,1]])  # array([[1, 4], [1, 3]])

# Check whether arrays are equal
np.array_equal(arr_1, arr_2)
# Convert array type

arr = np.array([1, 0])              # array([1, 0])
arr.astype(dtype='bool')            # array([ True, False])
```

- [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)
- [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)
- [ndarray.max](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html)
- [np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)
- [np.isnan](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html)
- [numpy sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)
- [np.array_equal](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html)

### Matrix functions

```
# Create identity (unit) matrix
np.identity(2)                      # array([[1., 0.], [0., 1.]])
np.eye(2)                           # array([[1., 0.], [0., 1.]])

# Get the main diagonal from a matrix
np.diag([[3,4], [2,1]])             # array([3, 1])

# Create matrix where diagonal from different matrix and 0s elsewhere
np.diag(np.diag([[3,4], [2,1]]))    # array([[3, 0], [0, 1]])

# Create matrix with lower triangle from different matrix and 0s elsewhere
np.tril([[3,4], [2,1]])             # array([[3, 0], [2, 1]])
# Shift the triangle one under the main diagonal
np.tril([[3,4], [2,1]], -1)         # array([[0, 0], [2, 0]])
```

- [np.identity](https://numpy.org/doc/stable/reference/generated/numpy.identity.html)
- [np.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html)
- [np.tril](https://numpy.org/doc/stable/reference/generated/numpy.tril.html)

## Linear Algebra

```py
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
v = np.array( [3, -1] )

# Addition of two matrices
A + B                   # array([[3, 1], [3, 5]])

# Multiply matrix with scalar
A * 3                   # array([[3, 3], [0, 3]])

# Elementwise product
A * B                   # array([[2, 0], [0, 4]])

# Matrix product
dot(A, B)               # array([[5, 4], [3, 4]])

# Multiply i-th row with i-th vector element
A * v[:, None]          # array([[ 3,  3], [ 0, -1]])
# Warning: following does the matrix product instead
A * v                   # array([[ 3, -1], [ 0, -1]])

# Calculate matrix or vector norm
np.linalg.norm(B)       # 5.385164807134504

# Check matrix symmetry
np.allclose(A, A.T, rtol=1e-05, atol=1e-08)

# Get inverse of a matrix
np.linalg.inv(B)        # array([[ 0.5  ,  0.   ], [-0.375,  0.25 ]])

# Compute matrix eigenvalues
np.linalg.eigvals(A)    # array([1., 5.])
```

- [Tentative_NumPy_Tutorial](https://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial)
- [i-th row by i-th element (stackoverflow)](https://stackoverflow.com/questions/18522216/multiplying-across-in-a-numpy-array)
- [np.linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
- [Symmetry check (stackoverflow)](https://stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy)
- [np.linalg.inv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)
- [np.linalg.eigvals](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html)

## Statistics

```py
# Correlation matrix for given arrays (Pearson)
np.corrcoef(np.arange(10), np.arange(10, 0, -1))    # array([[ 1., -1.], [-1.,  1.]])
```

- [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)

## Binary Operations

- [Binary operations (numpy.org)](https://numpy.org/doc/stable/reference/routines.bitwise.html)

```py
bool_arr = [ True,  True, False, False]
bool_2   = [ True, False,  True, False]
bin_arr  = [1, 1, 0, 0]
bin_2    = [1, 0, 1, 0]
int_arr  = [14, 12, 10,  9]
int_2    = [ 1,  3,  5,  6]

# Compute bitwise NOT operation for each element of given array
np.bitwise_not(bool_arr)            # array([False, False,  True,  True])
np.bitwise_not(bin_arr)             # array([-2, -2, -1, -1])
np.bitwise_not(int_arr)             # array([-15, -13, -11, -10])

# Compute bitwise OR operation on each two elements of given arrays
np.bitwise_or(bool_arr, bool_2)     # array([ True,  True,  True, False])
np.bitwise_or(bin_arr, bin_2)       # array([1, 1, 1, 0])
np.bitwise_or(int_arr, int_2)       # array([15, 15, 15, 15])

# Compute bitwise AND operation on each two elements of biven arrays
np.bitwise_and(bool_arr, bool_2)    # array([ True, False, False, False])
np.bitwise_and(bin_arr, bin_2)      # array([1, 0, 0, 0])
np.bitwise_and(int_arr, int_2)      # array([0, 0, 0, 0])
```

- [np.bitwise_not = np.bitwise_invert](https://numpy.org/doc/stable/reference/generated/numpy.invert.html)
- [np.bitwise_or](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_or.html)
- [np.bitwise_and](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html)

## Logic

- [logic functions (numpy.org)](https://numpy.org/doc/stable/reference/routines.logic.html)

