#!/bin/bash

if (($# < 1)); then echo "First argument is required, was not given."; exit 1; fi

source ~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02/compute/scripts/config.bash

for ds in ${dataset[@]}; do
    for n in ${ns[@]}; do
        for m in ${methods[@]}; do
            inst_file=${data_path}/${ds}/${ds^^}${n}_inst.dat
            sol_file=${data_path}/${ds}/${ds^^}${n}_sol.dat
            in_file=${ins_path}/${ds}/${ds^^}${n}_inst.dat
            out_file=${outs_path}/${ds}/${ds^^}${n}_sol.dat
            tmp_file=${tmp_path}/${ds}/${ds^^}_${m#*:}_${n}.csv
            case $1 in
            samples)
                diff <(cut -d ' ' -f 1,2 ${in_file}) <(cut -d ' ' -f 1,2 ${out_file})
            ;;
            knapsack)
                    diff $out_file $tmp_file
            ;;
            rp)
                diff $in_file $tmp_file # diff -y --suppress-common-lines $file_in $file_out | wc -l
            ;;
            dp)
                diff $out_file $tmp_file # diff -y --suppress-common-lines $file_in $file_out | wc -l
            ;;
            show)
                echo ${dir_data}/${ds}/${ds^^}_${n}
            ;;
            *)
                echo "Desired action \"$1\" was not found."
            ;;
            esac
        done
    done
done
