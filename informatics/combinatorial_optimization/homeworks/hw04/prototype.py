#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knapsack Tabu Search Prototype

Author:     Jaroslav Langer
Modified:   2021 Jan 16
"""

import sys
import math
import numpy as np

class instance():
    id =    None             # id of the problem
    n =     None             # number of items
    cpty =  None             # weight capacity
    items = None             # items matrix [[weights], [values]]

    def __repr__(self):
        return (f'<class Instance: '
                f'id={self.id}, n={self.n}, cpty={self.cpty},\n'
                f'items={self.items}>')

def read_instance():
    inst = instance()
    for line in sys.stdin:                                  # standard input
        line_nums = [int(x) for x in line.split()]
        inst.id = line_nums[0]                              # instance id
        inst.n = line_nums[1]                               # number of items
        inst.cpty = line_nums[2]                               # capacity
        inst.items = np.array([
            [line_nums[i] for i in range(3, 3+2*inst.n-1, 2)],   # weights
            [line_nums[i] for i in range(4, 3+2*inst.n, 2)]      # values
        ])
        yield inst

def tabu(inst):
    '''
    Solve knapsack instance using Tabu search.
    1) Randomly initialize first solution vector.
      - Number of ones is proportional to the average number of items that fits
    '''
    tabu_dict = {} # {(idx, value): tabu_end}
    best = 0

    total_weight = inst.items[0].sum() # print(total_weight)
    one_prob = min((inst.cpty / total_weight), 1) # print(one_prob)

    rand_gen = np.random.default_rng(42)
    # solution vector randomly initialized with an appropriate number of ones.
    solution = rand_gen.choice([0,1], size=inst.n, p=[1-one_prob, one_prob])
    print(solution)
    '''

    for step in range(math.ceil(math.sqrt(inst.n))):
        for swap in range(inst.n):
            pass
    '''
    return None

def write_result(result):
    pass


if __name__ == "__main__":

    for inst in read_instance():
        print(inst, end='\n\n')

        result = tabu(inst)
        print(result)
        # write_result(result)

