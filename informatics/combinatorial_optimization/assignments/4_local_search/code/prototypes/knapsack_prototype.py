#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knapsack 0/1 Tabu Search Prototype

Author:     Jaroslav Langer
Modified:   2021 Jan 23
"""

import sys
import math
import numpy as np
from collections import namedtuple


class Instance():
    """Knapsack 0/1 instance class."""

    id =    None             # id of the problem
    n =     None             # number of items
    cpty =  None             # weight capacity
    items = None             # items matrix [[weights], [values]]

    def __init__(self, inst_id, n, cpty, items):
        self.id = inst_id
        self.n = n
        self.cpty = cpty
        self.items = items

    def __repr__(self):
        return (f'<class Instance: '
                f'id={self.id}, n={self.n}, cpty={self.cpty},\n'
                f'items={self.items}>')

    @classmethod
    def read_instances(cls, lines=None):
        """Yield knapsack instances from standard input."""

        lines = sys.stdin if lines is None else lines       # lines or stdin
        for line in lines:
            numbers = [int(x) for x in line.split()]
            inst_id = numbers[0]                            # instance id
            n = numbers[1]                                  # number of items
            cpty = numbers[2]                               # capacity
            items = np.array([
                [numbers[i] for i in range(3, 3+2*n-1, 2)], # weights
                [numbers[i] for i in range(4, 3+2*n, 2)]    # values
            ])
            yield Instance(inst_id=inst_id, n=n, cpty=cpty, items=items)



class Solution():
    """Knapsack solution class.

    It should contain reference to the problem instance.
    Value represents the sum of item values.
    State vector represents what items are included into the solution.
    """

    inst = None
    state = None
    value = None

    def __init__(self, inst, state=None, value=None):
        self.inst = inst
        self.state = state
        self.value = value

    def __repr__(self):
        return (f'<class Solution: '
                f'inst.id={self.inst.id}, value={self.value},\n'
                f'state={self.state}>')

    @classmethod
    def get_random(cls, inst):

        total_weight = inst.items[0].sum()
        one_prob = min((inst.cpty / total_weight), 1)

        rand_gen = np.random.default_rng(42)
        # solution vector randomly initialized with an appropriate number of ones.
        state_rand = rand_gen.choice([0,1], size=inst.n, p=[1-one_prob, one_prob])
        soln_rand = Solution(inst=inst, state=state_rand)
        soln_rand.value = soln_rand.eval_state()

        return soln_rand

    def copy(self):
        """Return solution copy."""

        return Solution(inst=self.inst, value=self.value, state=self.state.copy())

    def assign(self, soln):
        self.inst = soln.inst
        self.state = soln.state.copy()
        self.value = soln.value

    def eval_state(self, inst=None):
        """Evaluate knapsack state.

        Return total value.
        Return -1 if the total weight exceeds knapsack's capacity.
        """
        inst = inst if (inst is not None) else self.inst

        weight, value = list(np.dot(inst.items, self.state))
        return value if (weight <= inst.cpty) else inst.cpty - weight

    def write_down(self):
        print(self.inst.id, self.inst.n, self.value, *self.state, end=' \n')


class Solver():
    """Knapsack 0/1 solver class."""

    @classmethod
    def tabu(cls, inst, tabu_period=3):
        """
        Solve knapsack instance using Tabu search.
        1) Randomly initialize first solution vector.
          - Number of ones is proportional to the average number of items that fits
        """

        tabu_dict = {}  #(swap_idx, swap_value, value_curr, soln_tmp.value):

        soln_best = Solution(inst=inst, value=0,
            state=np.zeros(inst.n, dtype='i4'))
        soln_tmp = Solution.get_random(inst) # First solution is randomized
        soln_next = soln_tmp.copy()
        key_next = None

        # max_iter = math.ceil(math.sqrt(inst.n))
        max_iter = inst.n
        for step in range(max_iter):        # Iterate until max_iteration
            value_curr = soln_tmp.value     # Current iteration value

            for swap_idx in range(inst.n):  # Iteration order can be randomized
                swap_value = soln_tmp.state[swap_idx]

                if (soln_tmp.state[swap_idx] == 0):
                    soln_tmp.state[swap_idx] = 1
                else:
                    soln_tmp.state[swap_idx] = 0

                soln_tmp.value = soln_tmp.eval_state()
                key_next = (swap_idx, swap_value, value_curr, soln_tmp.value)
                if (tabu_dict.get(key_next, step - 1) < step):  # Is tabu?
                    if (soln_tmp.value > soln_next.value):
                        soln_next.assign(soln_tmp)
                    if (soln_tmp.value > soln_best.value):
                        soln_best.assign(soln_tmp)
                soln_tmp.state[swap_idx] = swap_value
                soln_tmp.value = value_curr

            soln_tmp.assign(soln_next)
            tabu_dict[key_next] = step + tabu_period

        return soln_best


if __name__ == "__main__":
    import sys
    # sys.stdin = open('/dev/fd/3')
    # import pdb; pdb.Pdb(stdin=sys.__stdin__, stdout=sys.__stdout__).set_trace()

    if (len(sys.argv) > 1) and (sys.argv[1] == '-d'):
        lines = sys.stdin.readlines()
        sys.stdin = open('/dev/tty')
        import pdb
        pdb.set_trace()
    else:
        lines = None

    for inst in Instance.read_instances(lines):
        solution = Solver.tabu(inst)
        solution.write_down()

# import pdb; pdb.set_trace()
# breakpoint()

