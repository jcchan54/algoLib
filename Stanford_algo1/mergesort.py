#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:03:48 2023

@author: johnsonchan
"""


#%%
def topdown_mergesort(ls1, ls2, n):
    #print(ls1,ls2)
    j = 0
    i = 0
    result = []
    
    for ele in range(len(ls1)+len(ls2)):
        if i >= len(ls1):
            result.append(ls2[j])
            j+=1
            #n+=len(ls1)
        elif j >= len(ls2):
            result.append(ls1[i])
            i+=1
        elif ls1[i] < ls2[j]:
            result.append(ls1[i])
            i+=1
        else:
            result.append(ls2[j])
            j+=1
            n+=len(ls1)-i
            #print('i>j', n)
            
    return result, n
print(topdown_mergesort([10,11,12],[1,2,5],0))
#%%
def merge_sort_with_n(ls:list, n:int)->list:    
    ls_len = len(ls)
    if ls_len <= 1:
        return ls, n
    
    upper_ls = ls[:int(ls_len/2)]
    lower_ls = ls[int(ls_len/2):]
    upper_ls, n = merge_sort_with_n(upper_ls, n)
    lower_ls, n = merge_sort_with_n(lower_ls, n)
    result, n = topdown_mergesort(upper_ls, lower_ls, n)
    return result, n
print(merge_sort_with_n([1,2,3,6,5,4],0))
#%%



#%%
import os
#print(os.getcwd())
f = open('/Users/johnsonchan/Documents/CourseraCourseWorks/Stanford_algo1/W2assignment.txt')
int_ls = []
for line in f.readlines():
    int_ls+=[int(line)]
    
f.close
#%%
sorted_ls,n = merge_sort_with_n(int_ls,0)

