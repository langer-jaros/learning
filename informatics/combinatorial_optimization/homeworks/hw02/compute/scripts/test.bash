#!/bin/bash

if (($# < 1)); then echo "First argument is required, was not given."; exit 1; fi

project_path=~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02

ins_path=${project_path}/compute/tests/ins
outs_path=${project_path}/compute/tests/outs
tmp_path=${project_path}/compute/tests/tmp
data_path=${project_path}/data

rp_cmd=${project_path}/compute/source/build/read_problem
dp_cmd=${project_path}/compute/source/build/dynamic_programming

dataset=(nk zkc zkw)
ns=(4) # 10) # ns=(4 10 15 20 22 25 27 30 32 35 37 40)
methods=("1:bf" "2:bab" "3:dp" "4:gh" "5:redux" "6:fptas")

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
                shuf -n 5 ${inst_file} | sort -t ' ' -n > ${in_file}
                id_patt=$(cut -d ' ' -f 1 ${in_file} | tr '\n' '|')
                egrep "^(${id_patt:0:-1}) " ${sol_file} > ${out_file}
            ;;
            rp)
                $rp_cmd ${m%%:*} < $in_file > $tmp_file
            ;;
            dp)
                $dp_cmd < $in_file > $tmp_file
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
