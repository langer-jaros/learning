#!/bin/bash

if (($# < 1)); then echo "First argument is required, was not given."; exit 1; fi

source ~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02/compute/scripts/config.bash

for n in ${ns[@]}; do
    for ds in ${dataset[@]}; do
        for m in ${methods[@]}; do
            inst_file=${data_path}/${ds}/${ds^^}${n}_inst.dat
            sol_file=${data_path}/${ds}/${ds^^}${n}_sol.dat
            in_file=${ins_path}/${ds}/${ds^^}${n}_inst.dat
            out_file=${outs_path}/${ds}/${ds^^}${n}_sol.dat
            tmp_file=${tmp_path}/${ds}/${ds}_${m#*:}_${n}.csv
            case $1 in
            samples)
                shuf -n ${samples_num} ${inst_file} | sort -t ' ' -n > ${in_file}
                id_patt=$(cut -d ' ' -f 1 ${in_file} | tr '\n' '|')
                egrep "^(${id_patt:0:-1}) " ${sol_file} > ${out_file}
            ;;
            knapsack)
                $knapsack_cmd ${m%%:*} < $in_file > $tmp_file
                if (( ${m%%:*} == 6 )); then
                    for e in ${epsilons[@]}; do
                        tmp_file=${tmp_path}/${ds}/${ds}_${m#*:}_${n}_$(echo $e | tr -d "." ).csv
                        $knapsack_cmd ${m%%:*} ${e} < ${in_file} > ${tmp_file}
                    done
                fi
            ;;
            rp)     $rp_cmd ${m%%:*} < $in_file > $tmp_file     ;;
            bf)     $bf_cmd 1 < $in_file > $tmp_file            ;;
            dp)     $dp_cmd < $in_file > $tmp_file              ;;
            gh)     $gh_cmd < $in_file > $tmp_file              ;;
            fptas)  $fptas_cmd < $in_file > $tmp_file           ;;
            show)   echo ${dir_data}/${ds}/${ds^^}_${n}         ;;
            *)      echo "Desired action \"$1\" was not found." ;;
            esac
        done
    done
    echo "$(date +%T.%N) - Instances of size $n done."
done
