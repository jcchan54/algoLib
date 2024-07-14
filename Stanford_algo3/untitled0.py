#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:00:03 2023

@author: johnsonchan
"""
from scheduling import split_sort



def add_new_group(v1,v2,groups):
    return groups + [[v1,v2]]
def add_to_group(new, old, groups):
    for i,grp in enumerate(groups):
        if old in grp:
            break
    groups[i] += [new]
    return groups + []
def merge_groups(v1,v2,groups):
    found = 0
    grp1 = -1
    groups = groups + []
    for i,grp in enumerate(groups):
        if v1 in grp:
            grp1 = i + 0
            found+=1
        if v2 in grp:
            grp2 = i + 0
            found+=1
            
        if found >=2:
            break
        
    if grp1 <0:
        print(v1, v2, groups)
        raise("error")
    
    #groups[grp1] = groups[grp1]+ groups[grp2] + []    
    new_grp = groups[grp1]+ groups[grp2] + []
    #groups = [(new_grp if i == grp1 else grp) 
    #          for i,grp in enumerate(groups)]
    groups = [grp for i,grp in enumerate(groups) if (i!= grp2) and i!= (grp1)] 
    groups += [new_grp]
    
    


    #groups = [grp if i != grp1 else new_grp 
    #         for i,grp in enumerate(groups) if i!= grp2]
    return groups +[]

def clustering(from_v_p,to_v_p,group_exp = 2 ):
    V = set(from_v+to_v)
    tot = len(V)
    S = set()
    
    groups = []
    
    cnt = 0
    while (len(S) < tot) | (len(groups) > group_exp):
        v1, v2 = from_v_p[cnt],to_v_p[cnt]
        
        if (v1 in S) and (v2 in S):
            groups = merge_groups(v1, v2, groups)
        elif (v1 not in S) & (v2 in S):
            groups = add_to_group(v1, v2, groups)
        elif (v1 in S) & (v2 not in S):
            groups = add_to_group(v2, v1, groups)
        else:
            groups = add_new_group(v1, v2, groups)
       
        S.add(v1)
        S.add(v2)
        cnt+=1
        
        
    return groups

def spacings(groups, dist_dict):
    l_g = len(groups)
    spacing = []
    for i in range(l_g):
        for j in range(i+1,l_g):
            ds = [dist_dict[f"{e_i}_{e_j}"] \
                  if e_i < e_j else dist_dict[f"{e_j}_{e_i}"] \
                  for e_i in groups[i] for e_j in groups[j]]
            spacing+=[min(ds)]
    return spacing
                    




from_v = []
to_v = []
dist = []
dist_dict=dict()
with open("W2_clustering.txt") as file:
    for i,ln in enumerate(file):
        if i == 0:
            continue
        v1, v2, d = ln.split()
        v1, v2, d = int(v1), int(v2), int(d)
        from_v += [v1]
        to_v += [v2]
        dist += [d]
        dist_dict[f"{v1}_{v2}"] = d
        
dist_p, order = split_sort(dist, list(range(len(dist))))
to_v_p = [to_v[i] for i in order]
from_v_p = [from_v[i] for i in order]


groups = clustering(from_v_p, to_v_p, group_exp = 4)
spacing = spacings(groups, dist_dict)
        
    