#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python prototype solution to the first assignment from nonlinear optimization.
Author: Jaroslav Langer
Date:   2020, Dec. 14th
Desc.:  The code will be rewritten to the c/c++, so the code will not be pythonic, because it should not be.
"""

import sys
from math import sqrt

def read_matrix(matrix, m_file):
    """Read 1+n lines from given file, n is read from the first line.
    Write n rows of n floats to the matrix."""

    n = 0
    with open(m_file, "r") as f:
        first_line = f.readline()
        n = int(first_line); print(n)
        for i in range(n):
            line = f.readline()
            matrix.append([float(x) for x in line.split()])
            # print(line, end='')
    return n

def read_vector(vector, n, v_file):
    """Read vector of a length n from given file."""

    with open(v_file, "r") as f:
        for i, line in enumerate(f.readlines()):
            if (i == n): break
            vector.append(float(line))
    return None

def add_vector_vector(v_1, v_2):
    v = v_1.copy()
    for i in range(len(v_1)):
        v[i] = v_1[i] + v_2[i]
    return v

def subtract_vector_vector(v_1, v_2):
    v = v_1.copy()
    for i in range(len(v_1)):
        v[i] = v_1[i] - v_2[i]
    return v

def multiply_scalar_vector(s, v):
    x = v.copy()
    for i in range(len(v)):
        x[i] = s * v[i]
    return x

def multiply_vector_t_vector(x_1_t, x_2):
    x = 0
    for i in range(len(x_1_t)):
        x += x_1_t[i]*x_2[i]
    return x

# def multiply_vector_t_matrix(x_t, A):
#     x = [0 for x in x_t]
#     for i in range(len(x_t)):   # iterate over columns
#         for j in range(len(A)): # iterate over rows
#             x[i] += x_t[i] * A[j][i]
#     return x

def multiply_matrix_vector(m, v):
    x = [0 for row in m]            # shape (n,)
    for i in range(len(m)):         # iterate over rows
        for j in range(len(m[0])):  # iterate over columns
            x[i] += m[i][j] * v[j]
    return x

def norm(v):
    nn = 0
    for i in range(len(v)):
        nn += v[i]*v[i]
    return sqrt(nn)

def gradient_descent(A, b, x):
    i = 0 # step
    r = [x for x in b]
    while (True):
        print(f'STEP: {i: <4}')
        Ar   = multiply_matrix_vector(A, r)    # Helper
        rTr  = multiply_vector_t_vector(r, r)  # Helper
        rTAr = multiply_vector_t_vector(r, Ar) # Helper

        a =  rTr / rTAr

        ar   = multiply_scalar_vector(a, r)    # Helper
        aAr  = multiply_scalar_vector(a, Ar)   # Helper

        x = add_vector_vector(x, ar)
        r = subtract_vector_vector(r, aAr)

        nr = norm(r); print(nr)
        epsilon = 0.0001
        if (nr < epsilon): break
    return x


if __name__ == "__main__":
    method = "gd"       # gradient descent method
    saving = "full"     # saved as 2D array
    n = None            # number of entries
    A = matrix = None   # Matrix A initialization
    b = vector = []     # Vector b initialization
    x = []

    if len(sys.argv) < 4:
        print(f"Error: Three input parameters are required, {len(sys.argv)-1} were given.")
        sys.exit(1)                             # return 1
    f_matrix = sys.argv[1]
    f_vector = sys.argv[2]
    f_output = sys.argv[3]
    if len(sys.argv) > 4: method = sys.argv[4]  # set method
    if len(sys.argv) > 5: saving = sys.argv[5]  # set method

    if saving == "full":
        A = []
        n = read_matrix(A, sys.argv[1])
        read_vector(b, n, sys.argv[2])
    print(A, end='\n\n')
    print(b)


    if method == "gd":
        for i in range(n): x.append(0)  # Initialize vector x
        x = gradient_descent(A, b, x)

    print('\nsolution:', x)
    with open(f_output, mode="w") as f_out:
        f_out.write('\n'.join([str(xx) for xx in x]))
        f_out.write('\n')

    sys.exit(0) # return 0

