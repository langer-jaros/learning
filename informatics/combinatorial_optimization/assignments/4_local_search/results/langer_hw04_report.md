# Local Search for Knapsack Problem

`2021 Feb 02, Jaroslav Langer`

## TODO

* Test bad examples with big max_iter and  tabu_tenure.
* Based on the max_iter analysis, choose `m` and test multiple `tabu_tenure`s.
* Evaluate rel_error, time and number of evaluations.

## Contents

<!-- TOC GFM -->

* [Algorithm Choice and Description](#algorithm-choice-and-description)
* [Experimental Results](#experimental-results)
    * [Number of Iterations](#number-of-iterations)
    * [Tabu Tenure Impact](#tabu-tenure-impact)
* [Conclusions](#conclusions)
* [References](#references)
    * [Literature](#literature)
    * [Examples](#examples)

<!-- /TOC -->

## Algorithm Choice and Description

Stručný popis zvoleného algoritmu

## Experimental Results

Výsledek měření = čas výpočtu a rel. chyba.
Pokud nejste schopni vypočítat rel. chybu, stačí uvést vývoj výsledné ceny (počáteční → koncová)

### Number of Iterations

Zkoušejte sledovat vývoj řešení (populace u GA) v průběhu běhu algoritmu. Graf potěší...

### Tabu Tenure Impact

Experimentujte s různými nastaveními parametrů

## Conclusions

Pokuste se vyvodit nějaké závěry

## References

### Literature

* [tabu (mech.fsv.cvut.cz/~leps)](http://mech.fsv.cvut.cz/~leps/teaching/mmo/prednasky/prednaska05_Tabu.pdf)

### Examples

* [tabu knapsack](https://github.com/neemiasbsilva/knapsack-problem-using-dp-grasp-tabu/blob/master/TABU.py)
* [tabu sat](https://github.com/SamyMe/Tabu-Sat/blob/master/tabu.py)

