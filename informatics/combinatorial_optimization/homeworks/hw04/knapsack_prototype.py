#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Knapsack 0/1 Tabu Search Prototype

Author:     Jaroslav Langer
Modified:   2021 Jan 23
"""

import sys
import math
import numpy as np
from collections import namedtuple


# class instance():
#     """Knapsack 0/1 instance class."""
# 
#     id =    None             # id of the problem
#     n =     None             # number of items
#     cpty =  None             # weight capacity
#     items = None             # items matrix [[weights], [values]]
# 
#     def __init__(self, inst_id, n, cpty, items):
#         self.id = inst_id
#         self.n = n
#         self.cpty = cpty
#         self.items = items
# 
#     def __repr__(self):
#         return (f'<class Instance: '
#                 f'id={self.id}, n={self.n}, cpty={self.cpty},\n'
#                 f'items={self.items}>')
# 
#     @classmethod
#     def read_instances(cls):
#         """Yield knapsack instances from standard input."""
# 
#         for line in sys.stdin:                                  # standard input
#             line_nums = [int(x) for x in line.split()]
#             inst_id = line_nums[0]                              # instance id
#             n = line_nums[1]                               # number of items
#             cpty = line_nums[2]                               # capacity
#             items = np.array([
#                 [line_nums[i] for i in range(3, 3+2*inst.n-1, 2)],   # weights
#                 [line_nums[i] for i in range(4, 3+2*inst.n, 2)]      # values
#             ])
#             yield instance(inst_id=inst_id, n=n, cpty=cpty, items=items)
# 
# 
# 
# class solution():
#     """Knapsack solution class.
# 
#     It should contain reference to the problem instance.
#     Value represents the sum of item values.
#     State vector represents what items are included into the solution.
#     """
# 
#     inst = None
#     value = None
#     state = None
# 
#     def __init__(self, inst, value=None, state=None)
#         self.inst = inst
#         self.value = value
#         self.state = state
# 
#     def __repr__(self):
#         return (f'<class Solution: '
#                 f'inst.id={self.inst.id}, value={self.value},\n'
#                 f'state={self.state}>')
# 
#     @classmethod
#     def get_random(cls, inst):
#         
#         total_weight = inst.items[0].sum() # print(total_weight)
#         one_prob = min((inst.cpty / total_weight), 1) # print(one_prob)
# 
#         rand_gen = np.random.default_rng(42)
#         # solution vector randomly initialized with an appropriate number of ones.
#         state_rand = rand_gen.choice([0,1], size=inst.n, p=[1-one_prob, one_prob])
#         value = inst.eval_state(state_rand)
# 
#         return solution(inst, value, state_rand)
# 
#     def copy(self):
#         """Return solution copy."""
# 
#         return solution(inst=inst, value=value, state=state.copy())
# 
#     def eval_state(self, inst=self.inst):
#         """Evaluate knapsack state.
# 
#         Return total value.
#         Return -1 if the total weight exceeds knapsack's capacity.
#         """
# 
#         weight, value = *np.dot(self.state, inst.items)
#         return value if (weight <= inst.items.cpty) else -1
# 
#     def write_down(self):
#         return NotImplemented
# 
# 
# class solver():
#     """Knapsack 0/1 solver class."""
# 
#     @classmethod
#     def tabu(cls, inst):
#         """
#         Solve knapsack instance using Tabu search.
#         1) Randomly initialize first solution vector.
#           - Number of ones is proportional to the average number of items that fits
#         """
# 
#         tabu_dict = {} # {(idx, included, value): tabu_end}
# 
#         soln_best = solution(inst, 0, np.zeros(inst.n)) # ALSO TRY WITHOUT
#         soln_tmp = solution.get_random(inst)
#         soln_next = soln_curr.copy()
# 
#         max_iter = math.ceil(math.sqrt(inst.n)) # print(f'max_iter: {max_iter}')
#         for step in range(max_iter):
#             value_curr = soln_tmp.value
# 
#             for swap_idx in range(inst.n): # COULD BE RANDOMIZED
#                 present_curr = soln_tmp.state[swap_idx]
# 
#                 if (soln_tmp.state[swap_idx] == 0):
#                     soln_tmp.state[swap_idx] = 1
#                 else:
#                     soln_tmp.state[swap_idx] = 0
# 
#                 soln_tmp.value = soln_tmp.eval_state()
#                 if ((swap_idx, present_curr, value_curr, soln_tmp.value)
#                         in tabu_dict):
#                     soln_tmp.state[swap_idx] = present_curr
#                     soln_tmp.value = value_curr
#                     continue
# 
#                 if (soln_tmp.value > soln_next.value):
#                     soln_next.assign(soln_tmp)
#                 best_value = value
#                 best_solution = solution[:]
# 
#         return solution(inst, best_value, best_solution)


if __name__ == "__main__":
    import sys
    sys.stdin = open('/dev/fd/3')

    import pdb; pdb.Pdb(stdin=sys.__stdin__, stdout=sys.__stdout__).set_trace()

    for inst in instance.read_instances()
        print(inst, end='\n\n')
        
#         solution = solver.tabu(inst)
#         print(solution, end='\n\n')
#         write_result(result)

# import pdb; pdb.set_trace()
# breakpoint()

