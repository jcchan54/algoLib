#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:39:55 2023

@author: johnsonchan
"""

import numpy as np
#from itertools import combinations

filename = "/Users/johnsonchan/Documents/CourseraCourseWorks/Stanford_algo4/W3.txt"


f = open(filename, 'r')
ls = f.readlines()[1:]
graph = [list(map(float, i.split(' '))) for i in ls]

def sqr_dis(i, j):
    return (graph[i][1]-graph[j][1])**2+(graph[i][2]-graph[j][2])**2


def dis(i, j):
    return np.sqrt((graph[i][1]-graph[j][1])**2+(graph[i][2]-graph[j][2])**2)


N = len(graph)
dic1 = {frozenset([0]): {0: 0}}

#dist_matrix = [[dis(i, j) for i in range(len(graph))] for j in range(len(graph))]
def min_k(dist_ls):
    min_val,min_val_ls, min_k_ls = 9e9,[], []
    for item in dist_ls:
        dist, k = item
        if  dist < min_val:
            min_val = dist+0.0
            min_val_ls += [dist]
            min_k_ls += [k]

    #min_id = min([min_k_ls[i] for i,val in enumerate(min_val_ls) if abs(val-min_val) < 1e-8])
    return min_k_ls[-1], min_val#min_id, min_val
#print(min_k([[2132,0],[2312,1],[1e7,3], [2,4]]))
not_visited = set(range(N))
visited = set()
tot_dist = 0
tr = [0]
visited.add(tr[-1])
not_visited.remove(tr[-1])
#%%
for cnt in range(N-1):
    if cnt%1000 == 0:
        print("The index", tr[-1])
    dist_ls = [[sqr_dis(tr[-1],k),k] for k in not_visited]
    
    min_id, min_dist = min_k(dist_ls)
    tot_dist += np.sqrt(min_dist)
    
    tr+= [int(min_id)]
    visited.add(tr[-1])
    not_visited.remove(tr[-1])
tot_dist+= dis(0,tr[-1])
print(tot_dist)

##88625
#%%
import numpy as np

f = open(filename, 'r')
ls = f.readlines()[1:]
graph = [list(map(float, i.split(' ')))[1:] for i in ls]
graph = {i: graph[i] for i in range(len(graph))}

N = len(graph)


def dis(i, j):
    return (graph[i][0]-graph[j][0])**2+(graph[i][1]-graph[j][1])**2


tour = [0]
travel = 0
g = graph.copy()
g.pop(0)

while len(g) > 0:
    plan = 1e9
    for c in g:
        d = dis(tour[-1], c)
        if d < plan:
            plan = d
            city = c
    travel += np.sqrt(plan)
    tour += [city]
    g.pop(city)
    if len(g) % 1000 == 0:
        print('Travel %i, %i cities left' % (city, len(g)))

travel += np.sqrt(dis(0, tour[-1]))
print(travel)
# 1203406.5012708856
