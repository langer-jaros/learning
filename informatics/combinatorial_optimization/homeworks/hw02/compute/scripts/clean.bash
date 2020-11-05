#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02/compute/scripts/config.bash

for ds in ${dataset[@]}; do rm ${outs_path}/${ds}/*; done
for ds in ${dataset[@]}; do rm ${ins_path}/${ds}/*; done
for ds in ${dataset[@]}; do rm ${tmp_path}/${ds}/*; done
