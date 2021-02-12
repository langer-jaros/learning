# URL Traveler

Find a route between two URL sites just by following links form one to another.

`2021 Feb 10, Jaroslav Langer`

## Sample usage

```sh
# From fit.cvut.cz to mit.edu
./url_traveler.py -l

# From fit.cvut.cz to mit.edu
./url_traveler.py -s fit.cvut.cz -e mit.edu -o mit_route.txt -l mit_log.txt

# To see all the options
./url_traveler.py --help
```

## Contents

<!-- TOC GFM -->

* [Introduction](#introduction)
* [Algorithm Description](#algorithm-description)
* [Link Extraction](#link-extraction)
* [Search Algorithms](#search-algorithms)
    * [Breadth First Search (BFS)](#breadth-first-search-bfs)
    * [Depth First Search (DFS)](#depth-first-search-dfs)
    * [Iterative Depth First Search (IDS)](#iterative-depth-first-search-ids)
* [Heuristics](#heuristics)

<!-- /TOC -->

## Introduction

The goal is to create a program that upon two URL links given returns a sequence of links that leads from first site to the second one.

## Algorithm Description

I believe the easiest way to describe a program is to show the pseudocode first. Following example is a pseudocode of a BFS search algorithm, other search algorithms would differ in the way of how the `next_links` are stored and with the position of the recursion call.

```py
# Python URL Traveler pseudocode

def travel_rec(links, url_end, visited):
    next_links = set() # Structure to store new links to be visited

    for link in links:
        visited.add(link) # Storage of visited links, perhaps (link, prev_link)

        next_links.add(
                get_links_from_site(link) # Add newly read links to be visited
        )

        if (url_end in next_links):
            # If url_end is between next_links return path from start_url to
            # end_url, pehaps using the (link, perv_link) pairs in visited
            return create_path(url_end, next_links, links, visited)

    return travel_rec(next_links, url_end, visited)

def travel(url_start, url_end):
    return travel_rec(links={url_start}, url_end=url_end, visited={})
```

## Link Extraction

The sites are read with python library requests. Then the links are extracted from text of the response. The extraction is done by regular expressions via re python library. The query and fragment sections are forgotten. Links that are email addresses are not used.

Errors are ignored, namely SSL error, connection error, invalid URL error and unicode error.

## Search Algorithms

### Breadth First Search (BFS)

BFS will find the shortest path from start to end. It also will not repeat any site once it was visited. However its memory usage is exponential to the search depth, so it is ideal approach for searching a routes that are not too long, i.e. to be used for sites that are quite known such as `fit.cvut.cz -> mit.edu`.

### Depth First Search (DFS)

DFS's memory usage is linear to the length of the search depth. On the other hand the optimal solution is not guaranteed, and in open world such as internet links the search can be easily miss leaded by single link that points the search totally wrong direction. For this reasons the DFS is a viable solution if the end site is very popular and you can not afford to use the BFS, or there when the IDS is not implemented.

### Iterative Depth First Search (IDS)

IDS combines the advantages of BFS's optimality with DFS's low memory requirements. It performs multiple DFS's with set maximal depth limit and this limit is iteratively increased. It means, the algorithm visits the closed neighbors multiple times, however asymptotic complexity is still $\mathcal{O} (b^d)$, where $b$ is the branching factor and $d$ is the smallest depth with a solution. The memory usage is linear with the size of search depth. In cases where the BFS is not possible the IDS is the best option.

## Heuristics

Sites with the same domains as the final are prioritized i.e. in case of BFS for route to mit.edu, on level n, will be all sites with .edu visited before any others.

