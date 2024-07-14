#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 08:41:26 2023

@author: johnsonchan
"""


def td_merge_sort(ls1_l,ls1_r,ls2_l,ls2_r):
    #print(ls1_l,ls1_r,ls2_l,ls2_r)
    
    r1 = []
    r2 = []
    l_l = len(ls1_l)
    l_r = len(ls1_r)
    i = 0
    j = 0
    for k in range(len(ls1_l)+len(ls1_r)):
        if i>= l_l:
            r1.append(ls1_r[j])
            r2.append(ls2_r[j])
            
            j+=1
            
        elif j>= l_r:
            r1.append(ls1_l[i])
            r2.append(ls2_l[i])
            i+=1
        
        elif ls1_l[i]<ls1_r[j]:
            r1.append(ls1_l[i])
            r2.append(ls2_l[i])
            i+=1
        elif ls1_l[i]>ls1_r[j]:
            r1.append(ls1_r[j])
            r2.append(ls2_r[j])
            j+=1
        elif ls2_l[i] < ls2_r[j] :
            r1.append(ls1_l[i])
            r2.append(ls2_l[i])
            i+=1
        else:
            r1.append(ls1_r[j])
            r2.append(ls2_r[j])
            j+=1
        
    return r1, r2
    


def split_sort(ls1,ls2):
    if len(ls1) <= 1:
        return ls1, ls2
    i_m = len(ls1) //2
    ls1_l = ls1[:i_m]
    ls1_r = ls1[i_m:]
    
    ls2_l = ls2[:i_m]
    ls2_r = ls2[i_m:]
   
    ls1_l, ls2_l = split_sort(ls1_l, ls2_l)
    ls1_r, ls2_r = split_sort(ls1_r, ls2_r)
    r1,r2 = td_merge_sort(ls1_l,ls1_r,ls2_l,ls2_r)
    
    return r1, r2


diff = lambda w,l: w-l
diff_rev = lambda w_l,w: w-w_l
ratio = lambda w,l: w/l
ratio_rev = lambda w_l,w: w/w_l 



def greedy(l,w,w_l_f, w_l_f_rev):
    
    w_l = [w_l_f(w[i],l[i]) for i,e in enumerate(w) ]
    sch_w_l, sch_w = split_sort(w_l,w)
    sch_l = [w_l_f_rev(sch_w_l[i],sch_w[i]) for i,e in enumerate(sch_w)]
    sch_w_l = sch_w_l[::-1];
    sch_l = sch_l[::-1];
    sch_w = sch_w[::-1];
    from itertools import accumulate
    c = list(accumulate(sch_l))
    return sum([sch_w[i]*c[i] for i,e in enumerate(c) ])



#l = [4,1,4,2,3,4,6,4,2,2,2,2,2,2]
#w = [5,3,3,5,4,6,2,1,7,2,1,4,2,6]
l = []
w = []
with open("W1_data.txt") as file:
    for i,ln in enumerate(file):
        if i == 0:
            continue
        wl = ln.split()
        w+= [int(wl[0])]
        l+= [int(wl[1])]
print(greedy(l,w,diff, diff_rev))
print(greedy(l,w,ratio, ratio_rev))