#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 00:53:38 2023

@author: johnsonchan
"""

vertices = ["".join(x.split(' ')) for x in open('W2_clustering2.txt', 'r').read().split('\n')[1:-1]]

def invert(bit):
    if bit != '0' and bit != '1':
        raise ValueError
    return '1' if bit == '0' else '0'

def similar(v):
    out = []
    for i in range(len(v)):
        out.append(v[:i]+invert(v[i]) + v[i+1:])
        for j in range(i+1, len(v)):
            out.append(v[:i]+invert(v[i])+v[i+1:j]+invert(v[j])+v[j+1:])
    return out
 
heads = {}
for v in vertices:
    heads[v] = v
clusters = len(heads) 
#print clusters
for v in vertices:
    v_head = heads[v]
    while heads[v_head] != v_head:
        v_head = heads[v_head]

    for friend in similar(v):
        if heads.get(friend):
            head = heads[friend]
            while heads[head] != head:
                head = heads[head]
            if v_head != head:
                heads[head] = v_head
                clusters -= 1
print(clusters)