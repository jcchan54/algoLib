#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:43:45 2023

@author: johnsonchan
"""
import numpy as np

def dist(x1,y1,x2,y2):
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

filename = "/Users/johnsonchan/Documents/CourseraCourseWorks/Stanford_algo4/W2.txt"
nodes = []
x_ls = []
y_ls = []
with open(filename) as f:
    for i, ln in enumerate(f):
        if i == 0:
            continue
        x, y = ln.split(' ')
        node, x, y = int(i)-1, float(x), float(y)
        nodes +=[node]
        x_ls += [x]
        y_ls += [y]
        
#%%
import matplotlib.pyplot as plt
plt.plot(x_ls, y_ls , 'bo', alpha = 0.3)
plt.show()


#%%
import itertools

def all_subsets(stuff):
    subsets = []
    subsets_ids = []
    cnt=0
    for L in range(1,len(stuff) + 1):
        for subset in itertools.combinations(stuff, L):
            subsets+=[subset]
            subsets_ids+=[cnt]
            cnt+=1
    return subsets, subsets_ids
#%%
S, S_ids =all_subsets(nodes)

inv_Set = {S[i]: S_ids[i] for i in range(len(S_ids))}

A = np.ones(( len(S), len(nodes)))*np.inf
A[inv_Set[(0,)],0] = 0.
j_ind = lambda x: x-1

#%%
for m in range(2,len(nodes)+1):
    for Si in S:
        if (0 not in Si) | (len(Si) !=m ):
            continue
        for j in Si:
            if j == 0:
                continue
            print(m,Si,j)
            new_set = tuple([i for i in Si if i != j])
            opt_ls = \
                [A[inv_Set[new_set], k] \
                 + dist(x_ls[k],y_ls[k],x_ls[j],y_ls[j]) \
                                                            for k in Si if k != j]
            print(opt_ls)
            A[inv_Set[Si],j] = min(opt_ls)
print([A[inv_Set[S[-1]],j_ind(k)] \
       + dist(x_ls[k],y_ls[k],x_ls[0],y_ls[0]) \
                                            for k in range(1,len(nodes))])
    
    
    
    
    
    
    
#%%

import numpy as np
from itertools import combinations

f = open(filename, 'r')
ls = f.readlines()[1:]
graph = [list(map(float, i.split(' '))) for i in ls]


def dis(i, j):
    return np.sqrt((graph[i][0]-graph[j][0])**2+(graph[i][1]-graph[j][1])**2)


N = len(graph)
dic1 = {frozenset([0]): {0: 0}}

for m in range(1, N):
    comb = list(combinations(range(1, N), m))
    dic2 = {frozenset(comb[i]): {list(comb[i])[j]: 0 for j in range(m)} for i in range(len(comb))}
    print(m, len(dic2))
    for s in dic2:
        for j in s:
            ans = []
            if m == 1:
                dic2[s][j] = dis(0, j)
            else:
                sj = set(s)
                sj.remove(j)
                dic2[s][j] = min([dic1[frozenset(sj)][k]+dis(k, j) for k in sj if k != j])
    dic1 = dic2.copy()

tsp = min([dic2[frozenset(comb[0])][j]+dis(0, j) for j in range(1, N)])
print(tsp)
            