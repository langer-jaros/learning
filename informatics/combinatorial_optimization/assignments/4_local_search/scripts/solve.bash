#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/assignments/4_local_search/config.bash

m=n^2 # n
t=sqrt
tabu_m_t=${outs}/tabu_${m}_${t}
mkdir -p ${tabu_m_t}

echo "$(date +%T.%N) - Computation started."
for dataset in ${base_path}/data/*; do
    for inst in ${dataset}/*inst*; do #*_{0,1,2,3}*inst*
        name=${inst##*/}
        soln=${tabu_m_t}/${name%%inst*}soln.csv
        meta=${tabu_m_t}/${name%%inst*}meta.csv
        ${solver} -m ${m} -t ${t} -w ${meta} < ${inst} > ${soln}
        echo "$(date +%T.%N) - File ${name} done."
    done;
done

