#!/bin/bash

base_path=~/Projects/learning/informatics/combinatorial_optimization/homeworks
outs=${base_path}/hw04/ins_and_outs/outs
solver=${base_path}/hw04/code/prototypes/knapsack_prototype.py

for dataset in ${base_path}/data/*; do
    for file in ${dataset}/*_{0,1}*inst*; do
        name=${file##*/}
        out=${outs}/${name%%inst*}soln.csv
        ${solver} < ${file} > ${out}
        # echo ${outs}/  ${file%%inst*}
    done;
done

