#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 11:13:40 2023

@author: johnsonchan
"""

import numpy as np
W = 6
v = [3,2,4,4]
w = [4,3,2,3]


def knapsack(W,w,v):
    A = np.zeros((len(w)+1)*(W+1))
    A = A.reshape((len(w)+1,W+1))
    
    for i in range(1,len(w)+1):
        ind = i-1
        for x in range(W+1):
            if x >= w[ind]:
                A[i][x] = max(
                    A[i-1][x], 
                               A[i-1][x - w[ind]]+v[ind]
                    )
            else:
                A[i][x] = A[i-1][x]
    return A

        
B = knapsack(W, w, v)
w = []
v = []
with open("W4_knapsack.txt") as file:
    for i,ln in enumerate(file):
        if i ==0:
            W,n = ln.split()
            W, n = int(W), int(n)
            continue
        v_i, w_i = ln.split()
        #v_i, w_i = int(v_i), int(w_i)
        w += [int(w_i)]
        v += [int(v_i)]
        
A = knapsack(W, w, v)
            

            