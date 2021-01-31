#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/assignments/4_local_search/config.bash

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

