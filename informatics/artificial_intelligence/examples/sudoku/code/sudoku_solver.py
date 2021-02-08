#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sudoku Solver Using Constraint Satisfaction Problem Approach

Author:     Jaroslav Langer
Modified:   2021 Feb 06
"""

import sys
import math
import numpy as np
import time
import copy

class Sudoku():
    """Reads sudoku file into matrix, writes sudoku matrix into file"""


    def __repr__(self):
        return (f"<class 'Sudoku':\n{self.matrix}\n>")


    @classmethod
    def read_instance(cls, input_iter, shape=(9,9)):
        """
        Return Sudoku instance, read iterable input into 2D array

        Format description:
        * Lines starting with hash and newlines are ignored
        * Odd columns are ignored (first column is even)
        * Numbers are extracted from the even columns
        * Zeros can be denoted with 0 or with space character ' '
        """

        sudoku = Sudoku()

        matrix_list = [int(n) if n != ' ' else 0
                for row, line in enumerate(input_iter)
                        if (line[0] not in ['#', '\r', '\n'])
                                for i, n in enumerate(list(line))
                                        if ((i % 2 == 0)
                                                and (i <= (shape[0] - 1) * 2))]
        matrix = np.reshape(matrix_list, shape)
        return matrix


    @classmethod
    def write_matrix(cls, matrix, file_out):
        """
        Writes matrix to given file_out.

        The format was copied to match http://lipas.uwasa.fi/~timan/sudoku/
        so the results would be possible to diff easily.
        """

        for row, line in enumerate(matrix):
            for col, elem in enumerate(line):
                print(f'{elem} ', file=file_out, end='')
                if (col in [2, 5]):
                    print('| ', file=file_out, end='')
                if (col == 8):
                    print(' = 0,45', file=file_out, end='')

            print(file=file_out, end='\r\n')
            if (row in [2, 5]):
                print('---------------------', file=file_out, end='\r\n')
            if (row == 8):
                print(file=file_out, end='\r\n')
                print('0 0 0 0 0 0 0 0 0 ', file=file_out, end='\r\n')
                print('45 45 45 45 45 45 45 45 45 ', file=file_out, end='\r\n')
                print('\r\n', file=file_out, end='\r\n')

class Solver():

    states_visited = 0

    @classmethod
    def is_consistent(cls, var, matrix):
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


    @classmethod
    def backtracking_rec(cls, unassigned, matrix):
        if (len(unassigned) == 0):
            return matrix
        var, work_domain = unassigned.popitem()
        for value in work_domain:
            cls.states_visited += 1
            matrix[var] = value
            if cls.is_consistent(var, matrix):
                result = cls.backtracking_rec(
                        unassigned=copy.deepcopy(unassigned), matrix=matrix
                )
                if (result is not None):
                    return result
            matrix[var] = 0
        return None


    @classmethod
    def backtracking(cls, matrix, file_meta, filter=True):
        """Solve sudoku matrix using backtracking"""
        start = time.process_time() # Measure CPU time

        unassigned = {
                (i,j): set(range(1, matrix.shape[0] + 1))
                        for i,j in np.argwhere(matrix == 0)
        }

        solution =  cls.backtracking_rec(unassigned, matrix)

        elapsed_cpu_time = time.process_time() - start
        if (file_meta is not None):
            print(f'# {cls.states_visited} {elapsed_cpu_time}', file=file_meta)
        return solution


if __name__ == '__main__':
    import argparse
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--debug', action='store_true',
            help='run in debug mode')
    parser.add_argument('-m', '--method', default='bt',
            choices=['bt', 'mac', 'bt', 'dbt', 'ddbt'],
            help=('solver method'))
    parser.add_argument('-w', '--metadata', nargs='?', const=sys.stdout,
            default=None, type=argparse.FileType('w'),
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
        solution = Solver.backtracking(matrix=instance,
                file_meta=args.metadata)
    else:
        raise NotImplementedError

    if (solution is not None):
        Sudoku.write_matrix(matrix=solution, file_out=args.output)

