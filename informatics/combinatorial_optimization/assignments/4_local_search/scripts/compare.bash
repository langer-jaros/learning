#!/bin/bash


base_path=~/Projects/learning/informatics/combinatorial_optimization/homeworks
outs=${base_path}/hw04/ins_and_outs/outs
solver=${base_path}/hw04/code/prototypes/knapsack_prototype.py

for dataset in ${base_path}/data/*; do
    for file in ${dataset}/*_{0,1}*soln*; do
        name=${file##*/}
        # diff --side-by-side --suppress-common-lines ${file} ${outs}/${file##*/}
        echo ${name} \
        $(diff -y --suppress-common-lines ${file} ${outs}/${file##*/} | wc -l)
        echo
        # out=${outs}/${name%%inst*}soln.csv
        # ${solver} < ${file} > ${out}
        # echo ${outs}/  ${file%%inst*}
    done;
done

