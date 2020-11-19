# Experimental Measurements of Algorithms Quality

## Contents <!-- omit in toc -->
- [Algorithms Description](#algorithms-description)
  - [Brute Force](#brute-force)
  - [Branch and Bound](#branch-and-bound)
  - [Dynamic Progarmming](#dynamic-progarmming)
  - [Greedy Heuristic](#greedy-heuristic)
- [Robustness Meassurements](#robustness-meassurements)
- [Default other parameters](#default-other-parameters)
- [Capacity / Total Items Value](#capacity--total-items-value)
  - [Time Complexity](#time-complexity)
  - [Relative Error](#relative-error)
- [Value/Weight Correlation](#valueweight-correlation)
  - [Time Complexity](#time-complexity-1)
  - [Relative Error](#relative-error-1)
- [Weight distribution](#weight-distribution)
  - [Time Complexity](#time-complexity-2)
  - [Relative Error](#relative-error-2)
- [Granularity](#granularity)
  - [Time Complexity](#time-complexity-3)
  - [Relative Error](#relative-error-3)
- [number of items](#number-of-items)
- [max weight of an item](#max-weight-of-an-item)
- [max value of an item](#max-value-of-an-item)

## Algorithms Description

- Follows description of four methods that were put under analysis.

### Brute Force

- hrubá síla (pokud z implementace není evidentní úplná necitlivost na vlastnosti instancí)

### Branch and Bound

- metoda větví a hranic, případně ve více variantách

### Dynamic Progarmming

- dynamické programování (dekompozice podle ceny a/nebo hmotnosti). FPTAS algoritmus není nutné testovat, pouze pokud by bylo podezření na jiné chování, než DP

### Greedy Heuristic

- heuristika - poměr cena/váha

## Robustness Meassurements

- The meassurements were done for 7 instance parameters. Each was done separately. 
- For every non-categorical value, there were batches of 10 values. 
- In case of categorical parameters all posibilites were explored.
- For every method the relative error and time complexity were meassured.

## Default other parameters

| var | value | description                                             |
| --- | ---   | ---                                                     |
| n   | 16    | number of items                                         |
| N   | 50    | number of instances                                     |
| m   | 0.8   | ratio of capacity/total_weight                          |
| W   | 5000  | max weight of an item                                   |
| w   | bal   | preferable weight of an item (light, heavy or balanced) |
| C   | 5000  | max value of an item                                    |
| c   | uni   | weith,value correlation (uni, corr or strong)           |
| k   | 1     | granularity exponent                                    |

## Capacity / Total Items Value

Values are from range 0.1 to 1.

### Time Complexity

Brute force 
- The mean complexity is slowly rising
  - probably because, the heavier states are possible the more `max_items` are created.
- The poor performance of ratio 0.1 is probably caused by creating

Branch and bound
- Complexity rises with growing relative capacity of the knapsack
  - The mean and worst cases both saturates at ratio about 0.5
  - The robustness is worse with higher ratio, the complexity depends on the specific values

Dynamic programming
- The DP implementated as weight decomposition, so higher ratio means bigger capacitity i.e. more iterations.
- The decreasing rubustness is probably caused by creation of more possible states (that fit into knapsack).

Greedy heuristic and REDUX
- These methods does not show any significant dependencies on the capacity/total_value ratio.
- What they do show is the small robustness i.e. the big gap between mean and worst case.


![Time Complexity of capacity/total_value](figures/m_time.png)

### Relative Error

Greedy Heuristic and REDUX
- Both shows the same trend that the mean relative error is slowly decreasing with increasing ratio
- The worst case relative error decrease rapidly with increasing ratio.
  - It is probably because the fact that with increasing capacity more items can fit, so the potential error is lesser.

![capacity/total_value](figures/m_error.png)

## Value/Weight Correlation

### Time Complexity

![Time Complexity dependencies on items value/weight correlation](figures/c_time.png)

### Relative Error

![Relative error dependencies on items value/weight correlation](figures/c_error.png)

## Weight distribution

### Time Complexity

![Time Complexity dependencies on weight distribution](figures/w_time.png)

### Relative Error

![Relative error dependencies on weight distribution](figures/w_error.png)

## Granularity

### Time Complexity

![Time Complexity dependencies on items granularity](figures/k_time.png)

### Relative Error

![Relative error dependencies on items granularity](figures/k_error.png)

## number of items

## max weight of an item

## max value of an item