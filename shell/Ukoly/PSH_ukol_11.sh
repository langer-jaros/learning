#!/bin/bash
#Jaroslav Langer
#09/05/2019

read -p "Zadejte hodnotu: "

if [[ $REPLY =~ ^(\+|-)?[[:digit:]]*$ ]]; then
        echo 'Vstup je cele cislo.'

        if (( REPLY > 0 )); then
                echo 'Cislo je kladne.'
        else
                echo 'Cislo je zaporne.'
        fi

        if (( REPLY%2 == 0 )); then
                echo 'Cislo je sude.'
        else
                echo 'Cislo je liche.'
        fi

        n=0
        while (( REPLY != 0 )); do
                REPLY=$(( REPLY/=10 ))
                n=$(( n+1 ))
        done
        echo "Pocet cislic: $n" 
        exit 0

elif [[ $REPLY =~ ^(\+|-)?[[:digit:]]+(\.|,)[[:digit:]]*$ ]]; then
        echo 'Vstup je desetinne cislo.'
        exit 0
fi

echo 'Nejedna se o ciselnou hodnotu'
exit 1
