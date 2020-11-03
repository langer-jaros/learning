#!/bin/bash

dir_data=../data
dataset=(NK ZKC ZKW)
ns=(4 10)

for ds in ${dataset[@]}; do
    for n in ${ns[@]}; do
        echo ${dir_data}/${ds}/${ds^^}_${n}
    done
done

# for n in ${ns[@]}; do
#     # runtime=$(./pipeline --threads $t)
#     # allRuntimes+=( $runtime )
# done

methods=(
    "1:bf"
    "2:bab"
    "3:dp"
    "4:gh"
    "5:redux"
    "6:fptas"
)

for m in ${methods[@]}; do
    m_key=${m%%:*}
    m_name=${m#*:}
    printf "{%s: %s}\n" "$m_key" "$m_name"
done
