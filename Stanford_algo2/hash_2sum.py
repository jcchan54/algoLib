#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:23:52 2023

@author: johnsonchan
"""

def binary_search(ls:list[int], target:int):
    """ 
    ls must be sorted 
    1 if target in ls
    -1 if target not in ls
    -2 if target duplicates()
    """
    left = 0
    right = len(ls) -1
    while left <= right:
        mid = (left + right) //2
        if target > ls[mid]:
            left = mid+1
        elif target < ls[mid]:
            right = mid -1
        else:
            if mid > 0:
                if ls[mid-1] == target:
                    return -2
            if mid < len(ls)-1:
                if ls[mid+1] == target:
                    return -2
                
            return 1
    
    return -1

num_ls_1 = [1, 3,5,8, 2,3,4,7,8,9,1,2,1]

num_ls_1.sort()

with open("W4_data.txt") as file:
    ls = [int(e) for i,e in enumerate(file)]
    
hash_table ={}
for num in ls:
    hash_table[num] = True    
#%%
#ls = num_ls
#ls.sort()
distinct_pairs = 0
for t in range(-10000,10000):
    for s in ls:
        if (t-s) in hash_table:
            distinct_pairs += 1
            print(s,t)
            break

     
        
        




