# Sudoku

`2021 Feb 05, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Introduction and Problem Definition](#introduction-and-problem-definition)
    * [Sudoku Example](#sudoku-example)
* [Algorithms Description](#algorithms-description)
    * [Backtracking (BT)](#backtracking-bt)
    * [Maintaining Arc-Consistency (MAC-BT)](#maintaining-arc-consistency-mac-bt)
    * [Backjumping (BJ)](#backjumping-bj)
    * [Dynamic backtracking (DBT)](#dynamic-backtracking-dbt)
    * [Dependency Directed Backtracking (DDBT)](#dependency-directed-backtracking-ddbt)
* [Datasets](#datasets)

<!-- /TOC -->

## Introduction and Problem Definition

Sudoku is a number-placement puzzle. There are more versions of this game, here will be presented the most common one. You are given matrix $M$, $M \in \{0,1,2,3,4,5,6,7,8,9\}^{9,9}$ (the $0$ can be represented in various ways such as empty space, or any other symbol). The goal is to create matrix $M'$ where following rules are satisfied: 

1) $\forall i,j \in \{1,2, \dots, 9\},\quad M_{i,j} \neq 0 \iff M_{i,j} = M'_{i,j}$
2) $\forall i \in \{1,2, \dots, 9\},\quad |\{m: m \in M_{i,:}\}| = 9$
3) $\forall j \in \{1,2, \dots, 9\},\quad |\{m: m \in M_{:,j}\}| = 9$
4) $\forall k,l \in \{1,2,3\},\quad |\{m: m \in M_{k+3n,l+3o},\quad \forall n,o \in \{0,1,2\} \}| = 9$

The mathematical definition will be handy for the algorithm. More human-friendly definition offers perhaps [Wikipedia's sudoku](https://en.wikipedia.org/wiki/Sudoku).

The conditions about the number's "uniqueness" is most often defined using (a) binary conditions (b) allDifferent constraints. I defined the problem with set sizes and I believe all three definitions are indeed equivalent.

### Sudoku Example

Following is an example of a sudoku instance. Every number is followed with one filler symbol (can be anything). Zeros are represented with space character `' '`.

```txt
# Format description
# Lines starting with hash are ignored
# Odd columns are ignored (first column is even)
# Numbers are extracted from the even columns (here below hashes)
# Zeros can be denoted with 0 or with space character (' ')

# # # # # # # # #
5 3  |  7  |     |
6    |1 9 5|     |
  9 8|     |  6  |
#-----------------
8    |  6  |    3|
4    |8   3|    1|
7    |  2  |    6|
#-----------------
  6  |     |2 8  |
     |4 1 9|    5|
     |  8  |  7 9|
```

## Algorithms Description

### Backtracking (BT)

### Maintaining Arc-Consistency (MAC-BT)

### Backjumping (BJ)

### Dynamic backtracking (DBT)

### Dependency Directed Backtracking (DDBT)

## Datasets

* [Sudoku research page (Timo Mantere & Janne Koljonen, University of Vaasa](http://lipas.uwasa.fi/~timan/sudoku/)

