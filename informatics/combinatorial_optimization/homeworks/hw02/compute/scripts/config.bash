#!/bin/bash

project_path=~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02

ins_path=${project_path}/compute/tests/ins
outs_path=${project_path}/compute/tests/outs
tmp_path=${project_path}/compute/tests/tmp
data_path=${project_path}/data

rp_cmd=${project_path}/compute/source/build/read_problem
dp_cmd=${project_path}/compute/source/build/dynamic_programming
gh_cmd=${project_path}/compute/source/build/greedy_heuristic
knapsack_dmd=${project_path}/compute/source/build/knapsack

dataset=(nk zkc zkw)
ns=(4 10 15) # (4 10 15 20 22 25 27 30 32 35 37 40)
methods=("3:dp" "4:gh" "5:redux") # ("3:dp" "4:gh" "5:redux") # ("1:bf" "2:bab" "3:dp" "4:gh" "5:redux" "6:fptas")

samples_num=100
