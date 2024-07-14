#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 21:01:23 2023

@author: johnsonchan
"""
import numpy as np
s = [1,4,2]
def med_index(s):
    return sorted(range(len(s)), key=lambda k: s[k])[1]
#%%
def swap(ls:list, i:int, j:int):
    ls[i], ls[j] = ls[j], ls[i]
    return ls

    
def pivot_swap(ls:list, tot_comparison:int = 0,
               first_i:int = 0, last_i:int = -999, 
               pivot_type:str="first"):
    
    last_i = len(ls)-1 if last_i == -999 else last_i
    if first_i >= last_i:
        print("black hole")
        return ls, first_i, tot_comparison
    #print(ls[first_i:last_i+1])
    if pivot_type =="first":
        None
    elif pivot_type == "last":
        ls = swap(ls,first_i,last_i)
    elif pivot_type =="med":
        mid_i = int((first_i+last_i)/2)
        s = [first_i,mid_i,last_i]
        
        p_i = med_index([ls[si] for si in s])
        p_i = s[p_i]
        ls = swap(ls,first_i,p_i)

    p = ls[first_i]
    #print(s, p_i,p)
    pivot_i = first_i + 0
    first_i += 1
    #print('first, last, p',first_i, last_i,p)    
    i =first_i+0;
    for j in range(first_i, last_i+1):
        tot_comparison += 1
        #print(i,j,ls)
        if p > ls[j]:
            #print("comparied")
            ls = swap(ls, i, j)
            i+=1
        
    #print(i,j,ls)  
    ls = swap(ls, pivot_i, i-1)
    
    #pivot_i = i-1 if i > 1 else pivot_i 
    return ls, i-1, tot_comparison
print(pivot_swap([3, 4, 9, 2,8], 0, 0,-999, 
                 pivot_type = "last"))

#%%
def pivot_sort(ls:list , tot_comparison:int = 0,
               first_i:int = 0, last_i:int = -999, 
               pivot_type:str = "first"):
    last_i = len(ls)-1 if last_i == -999 else last_i
    
    #print("main first last: ", first_i, last_i)
    if first_i >= (last_i):
        #print(ls)
        #print("skip")
        return ls, tot_comparison
    ls, p_i, tot_comparison = pivot_swap(ls, tot_comparison, first_i, last_i, 
                                         pivot_type=pivot_type)
    ls, tot_comparison = pivot_sort(ls,tot_comparison, first_i, p_i-1,
                                    pivot_type = pivot_type)
    ls , tot_comparison= pivot_sort(ls,tot_comparison, p_i+1, last_i,
                                    pivot_type=pivot_type)
    return ls, tot_comparison
    
print(pivot_sort([-100,3,8,1,5,2,4,7,0,23,-98], 0, pivot_type="med"))

#%%
import os
#print(os.getcwd())
f = open('/Users/johnsonchan/Documents/CourseraCourseWorks/Stanford_algo1/W3assignment.txt')
int_ls = []
for line in f.readlines():
    int_ls+=[int(line)]
    
f.close
#%%
sorted_ls, cnt = pivot_sort(int_ls, 0, pivot_type="med")
print(cnt)

