#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:43:05 2023

@author: johnsonchan
"""

from scheduling import split_sort


u_ls = [1,2,1,3, 4, 1]#,2,3,3,4]
v_ls = [2,3,3,4, 2, 4]#,1,2,1,3]
l_ls = [1,1,9,-8, -2, -3]#,1,1,9,-8]

def MST(u_ls, v_ls,l_ls):
    V = set(u_ls + v_ls)
    X = set()
    
    l_, ind = split_sort(l_ls, list(range(len(l_ls))))
    u_ = [u_ls[i] for i in ind]
    v_ = [v_ls[i] for i in ind]
    
    X.add(u_[0])
    MST_l = 0
    while len(V) > len(X):
        #print(X)
        u_new = []
        v_new = []
        l_new = []
        for i,u in enumerate(u_):
            if (u in X) & (v_[i] not in X):
                u_new += [u]
                v_new += [v_[i]]
                l_new += [l_[i]]
            elif (v_[i] in X) & (u not in X):
                u_new += [v_[i]] 
                v_new += [u]
                l_new += [l_[i]]
        MST_l += l_new[0]
        #print(MST_l)
        X.add(v_new[0])
        
    return MST_l
with open("W1_data2.txt") as file:
    u_ls = []
    v_ls = []
    l_ls = []
    for i, ln in enumerate(file):
        if i == 0:
            continue
        u, v, l = ln.split()
        u_ls += [int(u)]
        v_ls+= [int(v)]
        l_ls += [int(l)]
print(MST(u_ls, v_ls,l_ls))



            