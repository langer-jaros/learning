#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sudoku Solver Using Constraint Satisfaction Problem Approach

Author:     Jaroslav Langer
Modified:   2021 Feb 06
"""

SHAPE = (9,9)

import sys
import math
import numpy as np
import time

class Sudoku():
    """Sudoku class ."""

    matrix = None


    def __init__(self, matrix=None):
        self.matrix = matrix if (matrix is not None) else np.zeros(SHAPE)


    def __repr__(self):
        return (f"<class 'Sudoku':\n{self.matrix}\n>")


    @classmethod
    def read_instance(cls, input_iter):
        """Return Sudoku instance, read iterable input into 2D array"""

        sudoku = Sudoku()

        matrix_list = [int(n) if n != ' ' else 0
                for row, line in enumerate(input_iter)
                        if (line[0] not in ['#', '\r'])
                                for i, n in enumerate(list(line))
                                        if ((i % 2 == 0)
                                                and (i <= (SHAPE[0] - 1) * 2))]
        matrix = np.reshape(matrix_list, SHAPE)
        return matrix


    @classmethod
    def write_matrix(cls, matrix, file_out):

        for line in matrix:
            for i, elem in enumerate(line):
                print(f'{elem} ', file=file_out, end='')
            print(file=file_out)


    def write_down(self, file_out):
        Sudoku.write_matrix(matrix=self.matrix, file_out=file_out)


def is_consistent(var, matrix):
    """Check whether the var's row, column and box have only unique values"""

    unique_row = np.unique(matrix[var[0], : ], return_counts=True)
    duplicated_row = any(unique_row[1][int(0 in unique_row[0]): ] > 1)

    unique_col = np.unique(matrix[ :, var[1]], return_counts=True)
    duplicated_col = any(unique_col[1][int(0 in unique_col[0]): ] > 1)

    unique_box = np.unique(
            matrix[
                    3 * (var[0] // 3) : 3 * (var[0] // 3) + 3,
                    3 * (var[1] // 3) : 3 * (var[1] // 3) + 3
            ], return_counts=True
    )
    duplicated_box = any(unique_box[1][int(0 in unique_box[0]): ] > 1)

    return (not (duplicated_row or duplicated_col or duplicated_box))


def backtracking_rec(unassigned, matrix):
    if (len(unassigned) == 0):
        return matrix
    var = unassigned.pop()
    for value in range(1, matrix.shape[0] + 1):
        matrix[var] = value
        if is_consistent(var, matrix):
            result = backtracking_rec(unassigned.copy(), matrix)
            if (result is not None):
                return result
        matrix[var] = 0
    return None
        

def backtracking(matrix):
    unassigned = {(i,j) for i,j in np.argwhere(matrix == 0)}
    return backtracking_rec(unassigned, matrix)


if __name__ == '__main__':
    import argparse
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--debug', action='store_true',
            help='run in debug mode')
    parser.add_argument('-m', '--method', default='bt',
            choices=['bt', 'mac', 'bt', 'dbt', 'ddbt'],
            help=('solver method'))
    parser.add_argument('-w', '--metadata', type=argparse.FileType('w'),
            help='optional file for metadata information')
    # Input/Outupt positional arguments
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'),
            default=sys.stdin,
            help='input file, if not given, stdin is used')
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'),
            default=sys.stdout,
            help='output file, if not given, stdout is used')
    args = parser.parse_args()

    if args.debug:
        input_iter = args.input.readlines()
        sys.stdin = open('/dev/tty')
        import pdb; pdb.set_trace()
    else:
        input_iter = args.input

    instance = Sudoku.read_instance(input_iter)

    if (args.method == 'bt'):
        solution = backtracking(matrix=instance)
    else:
        raise NotImplementedError

    if (solution is not None):
        Sudoku.write_matrix(matrix=solution, file_out=args.output)

