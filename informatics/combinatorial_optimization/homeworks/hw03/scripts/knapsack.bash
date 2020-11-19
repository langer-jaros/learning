#!/bin/bash

(( $# < 1 )) && echo "First argument is required, was not given." && exit 1
[[ $1 == gen ]] && (( $# < 2 )) && echo "Argument required by generator, was not given." && exit 1

source /home/langerjaros/Projects/learning/informatics/combinatorial_optimization/homeworks/hw03/scripts/config.bash

# kg2 -n inst-size -N inst-num -W num -C num [-a] [-I id] [-m rnum[,rnum]] [-w bal|light|heavy] [-c uni|corr|strong] [-k rnum][PRNG-control]

gen () {
    echo $1
    ${gen_cmd} -n $n -N $N -W $W -C $C -m $m -w $w > $1
}

case $1 in
create) # Create data directories
    cd ${data_path};    mkdir -p    ns ms Ws ws Cs cs ks;  cd ${scripts_path}  ;;
gen)    # Generate samples
    case $2 in
    ns) for n in ${ns[@]}; do gen ${data_path}/ns/n_${n}_inst.csv; done ;;
    ms) for m in ${ms[@]}; do gen ${data_path}/ms/n_${m}_inst.csv; done ;;
    Ws) for W in ${Ws[@]}; do gen ${data_path}/Ws/n_${W}_inst.csv; done ;;
    ws) for w in ${ws[@]}; do gen ${data_path}/ws/n_${w}_inst.csv; done ;;
    Cs) for C in ${Cs[@]}; do gen ${data_path}/Cs/n_${C}_inst.csv; done ;;
    cs) for c in ${cs[@]}; do gen ${data_path}/cs/n_${c}_inst.csv; done ;;
    ks) for w in light heavy; do
        for k in ${ks[@]}; do gen ${data_path}/ks/n_${w}_${k}_inst.csv; done;
        done    ;;
    *)  echo "Desired action \"$2\" was not found." ;;
    esac    ;;
compute)
    echo "$(date +%T.%N) - Computation started."
    for nm in ${methods[@]}; do
        # for n in ${ns[@]}; do ${knap} ${nm%:*} < ${data_path}/ns/n_${n}_inst.csv > ${data_path}/ns/n_${nm#*:}_${n}_sol.csv ; done
        for m in ${ms[@]}; do ${knap} ${nm%:*} < ${data_path}/ms/n_${m}_inst.csv > ${data_path}/ms/n_${nm#*:}_${m}_sol.csv ; done
        for W in ${Ws[@]}; do ${knap} ${nm%:*} < ${data_path}/Ws/n_${W}_inst.csv > ${data_path}/Ws/n_${nm#*:}_${W}_sol.csv ; done    
        for w in ${ws[@]}; do ${knap} ${nm%:*} < ${data_path}/ws/n_${w}_inst.csv > ${data_path}/ws/n_${nm#*:}_${w}_sol.csv ; done    
        for C in ${Cs[@]}; do ${knap} ${nm%:*} < ${data_path}/Cs/n_${C}_inst.csv > ${data_path}/Cs/n_${nm#*:}_${C}_sol.csv ; done    
        for c in ${cs[@]}; do ${knap} ${nm%:*} < ${data_path}/cs/n_${c}_inst.csv > ${data_path}/cs/n_${nm#*:}_${c}_sol.csv ; done    
        for w in light heavy; do
            for k in ${ks[@]}; do ${knap} ${nm%:*} < ${data_path}/ks/n_${w}_${k}_inst.csv > ${data_path}/ks/n_${nm#*:}_${w}_${k}_sol.csv; done;
        done
        echo "$(date +%T.%N) - Method ${nm#*:} done."
    done    ;;
delete) # Delete data directories
    cd ${data_path};    rm -r       ns ms Ws ws Cs cs ks;  cd ${scripts_path}   ;;
*)
    echo "Desired action \"$1\" was not found." ;;
esac


