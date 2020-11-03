#!/bin/bash

data_dir=../../data
out_dir=../tests/ins
n_lines=5

dataset=(nk zkc zkw)
ns=(4 10) # ns=(4 10 15 20 22 25 27 30 32 35 37 40)
methods=(
    "1:bf"
    "2:bab"
    "3:dp"
    "4:gh"
    "5:redux"
    "6:fptas"
)
compute=./knapsack

for ds in ${dataset[@]}; do
    for n in ${ns[@]}; do
        for m in ${methods[@]}; do
            file_in=${data_dir}/${ds}/${ds^^}${n}_inst.dat
            file_out=${out_dir}/${ds}/${ds^^}${n}_inst.dat
            shuf -n ${n_lines} ${file_in} > ${file_out}
        done
    done
done
