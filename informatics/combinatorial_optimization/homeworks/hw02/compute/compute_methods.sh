#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02/compute/scripts/config.bash


for n in ${ns[@]}; do
    for ds in ${dataset[@]}; do
        for m in ${methods[@]}; do
            inst_file=${data_path}/${ds}/${ds^^}${n}_inst.dat
            computed_file=${data_path}/computed/${ds}/${ds}_${m#*:}_${n}.csv
            $knapsack_cmd ${m%%:*} < $inst_file > $computed_file
        done
    done
    echo "$(date +%T.%N) - Instances of size $n done."
done
