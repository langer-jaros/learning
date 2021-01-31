#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/assignments/4_local_search/config.bash

echo "$(date +%T.%N) - Computation started."
for dataset in ${base_path}/data/*; do
    for file in ${dataset}/*inst*; do #*_{0,1,2,3}*inst*
        name=${file##*/}
        out=${outs}/${name%%inst*}soln.csv
        ${solver} < ${file} > ${out}
        # echo ${outs}/  ${file%%inst*}
        echo "$(date +%T.%N) - File ${name} done."
    done;
done

