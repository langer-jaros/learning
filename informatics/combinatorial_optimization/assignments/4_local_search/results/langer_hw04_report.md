# Local Search for Knapsack Problem

`2021 Jan 31, Jaroslav Langer`

## TODO

- Check tabu behaviour for miserable outcomes of easy problems (n=4,10).
- Rename `tabu_period` to `tabu_tenure`.
- Add `max_iter` to input parameters.
- Change `tabu_tenure` to function call of n.
- Argparser handle for debug, metadata.
- Metadata logging, solutions, number of evaluations, time.

## Contents

<!-- TOC GFM -->

* [Algorithm Choice and Description](#algorithm-choice-and-description)
* [Experimental Results](#experimental-results)
    * [Number of Iterations](#number-of-iterations)
    * [Tabu Period Impact](#tabu-period-impact)
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

### Tabu Period Impact

Experimentujte s různými nastaveními parametrů

## Conclusions

Pokuste se vyvodit nějaké závěry

## References

### Literature

- [tabu (mech.fsv.cvut.cz/~leps)](http://mech.fsv.cvut.cz/~leps/teaching/mmo/prednasky/prednaska05_Tabu.pdf)

### Examples

- [tabu knapsack](https://github.com/neemiasbsilva/knapsack-problem-using-dp-grasp-tabu/blob/master/TABU.py)
- [tabu sat](https://github.com/SamyMe/Tabu-Sat/blob/master/tabu.py)

