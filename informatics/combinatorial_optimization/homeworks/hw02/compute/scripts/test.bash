#!/bin/bash

project_path=~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02

dir_in=${project_path}/compute/tests/ins
dir_out=${project_path}/compute/tests/tmp

# execute=${project_path}/compute/source/build/read_problem
execute=${project_path}/compute/source/build/dynamic_programming

dataset=(nk zkc zkw)
ns=(4 10) # ns=(4 10 15 20 22 25 27 30 32 35 37 40)
methods=(
    "1:bf"
    "2:bab"
    "3:dp"
    "4:gh"
    "5:redux"
    "6:fptas"
)

for ds in ${dataset[@]}; do
    for n in ${ns[@]}; do
        for m in ${methods[@]}; do
            file_in=${dir_in}/${ds}/${ds^^}${n}_inst.dat
            file_out=${dir_out}/${ds}/${ds^^}${n}_inst.dat
            $execute ${m%%:*} < $file_in > $file_out
        done
    done
done
