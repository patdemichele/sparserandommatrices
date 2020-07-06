import numpy as np


# try running this function on small values of t to understand its behavior
def gen_distinct(t): # generates distinct sequences of choosing t objects, some of which are distinct
    # here we consider the sequence (1,1,2) the same as (2,2,1). So only one of these is output
    if t == 1:
        return [[1]] # a single way to do so
    result = []
    sub = gen_distinct(t-1)
    for l in sub:
        for ending in range(1,max(l) + 2): # can go to the max+1 inclusive
            result.append(l + [ending])
    return result


def count_distinct_edges(left_choice, right_choice):
    if len(left_choice) != len(right_choice) + 1:
        error("improper input")
    t = len(right_choice)
    # always right left edge first
    edges = set([(left_choice[i],right_choice[i]) for i in range(t)] +
                [(left_choice[i+1], right_choice[i]) for i in range(t)])
    return len(edges)


def path_map(t): # paths from l to l of length 2t
    result = {}
    for left_choice in gen_distinct(t+1): # t+1 on the left
        for right_choice in gen_distinct(t):
            l_dist = len(set(left_choice)) # vertices used on left
            r_dist = len(set(right_choice)) # ... on right
            distinct_edges = count_distinct_edges(left_choice, right_choice)
            key = (l_dist, r_dist, distinct_edges)
            result[key] = result.get(key,0) + 1
    return result

def approx_where_r_equals_ck(pm, c): # given a path map and c
    # recall k on the left, r on the right
    # (a, b, c) approx k^a r^b (s/k)^c
    result = {} # will key by power of k, power of s
    for (x,y,z) in pm:
        result[(x-z+y, z)] = result.get((x-z+y, z), 0) + pm[(x,y,z)] * c**y
    return result
