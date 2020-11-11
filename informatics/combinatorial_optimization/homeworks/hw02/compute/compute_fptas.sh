#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02/compute/scripts/config.bash

m="6:fptas"

for n in ${ns[@]}; do
    for e in ${epsilons[@]}; do
        for ds in ${dataset[@]}; do
            inst_file=${data_path}/${ds}/${ds^^}${n}_inst.dat
            computed_file=${data_path}/computed/${ds}/${ds}_${m#*:}_${n}_$(echo $e | tr -d "." ).csv
            $knapsack_cmd ${m%%:*} ${e} < ${inst_file} > ${computed_file}
        done
    done
    echo "$(date +%T.%N) - Instances of size $n done."
done
