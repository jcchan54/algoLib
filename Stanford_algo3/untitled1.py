#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:51:50 2023

@author: johnsonchan
"""

from scheduling import split_sort


def MST(graph,edge_l):
    u = list(graph.keys())[0]
    X = set([u])
    tot_l = 0
    cnt = 0
    while len(X) < len(graph):
        l_ls =[]
        v_ls = []
        print(graph[u])
        for i, v in enumerate(graph[u]):
            if v not in X:
                l_ls += [edge_l[u][i]]
                v_ls += [v]
        
        cnt+=1
        ind = list(range(len(l_ls)))
        l_ls_2, ind = split_sort(l_ls, ind)
        tot_l += l_ls_2[0]
        
        X.add(v_ls[ind[0]])
        u = v_ls[ind[0]]
        print(X)
    print(len(X))
    return tot_l



graph = {1: [2,3],
         2: [1,3,4],
         3: [1,2],
         4: [2]
         }

edge_l = {1: [1,9],
          2: [1,1,-8],
          3: [9,1],
          4: [-8]
    }


u_ls = [1,2,3,2]
v_ls = [2,3,4,3]
l_ls = [1,9,1,-8]


def MST2(u_ls,v_ls,l_ls):
    V = set(u_ls+v_ls)
    X = set([u_ls[0]])
    while len(X) < len(u_ls):
        for u in u_ls:
            if u in X:
                








print(MST(graph,edge_l))
graph = dict()
edge_l = dict()
with open("W1_data2.txt") as file:
    for i, ln in enumerate(file):
        if i ==0:
            continue
        u,v,l = ln.split()
        if int(u) not in graph:
            graph[int(u)] = []
            edge_l[int(u)] = []
        if int(v) not in graph:
            graph[int(v)] = []
            edge_l[int(v)] = []
        graph[int(u)] += [int(v)]
        edge_l[int(u)] += [int(l)]
        
        graph[int(v)] += [int(u)]
        edge_l[int(v)] += [int(l)]
#print(MST(graph,edge_l))
        



    