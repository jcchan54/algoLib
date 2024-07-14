#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:13:24 2023

@author: johnsonchan
"""

class MinHeap(object):
    def __init__(self):
        self.heap = [];
        
    def parent(self, index):
        return (index -1) // 2
    
    def left_child(self, index):
        return index * 2 + 1
    
    def right_child(self, index):
        return index * 2 + 2
    def size(self):
        return len(self.heap)
    
    def bubble_up(self,index):
        if index  == 0:
            return
        if self.heap[index] >= self.heap[self.parent(index)]:
            return
        self.heap[index],self.heap[self.parent(index)] = \
            self.heap[self.parent(index)], self.heap[index]
            
        self.bubble_up(self.parent(index))
    def bubble_down(self, index):
        
        if self.right_child(index) >= len(self.heap):
            return
        if (self.heap[index] <= self.heap[self.left_child(index)]) &\
            (self.heap[index] <= self.heap[self.right_child(index)]):
            return
        if self.heap[self.left_child(index)] < self.heap[self.right_child(index)]:
            # left child is smaller
            self.heap[index],self.heap[self.left_child(index)] = \
                self.heap[self.left_child(index)], self.heap[index]
            self.bubble_down(self.left_child(index))
        else:
            # right child is smaller
            self.heap[index],self.heap[self.right_child(index)] = \
                self.heap[self.right_child(index)], self.heap[index]
            self.bubble_down(self.right_child(index))
    
    def insert(self, ele):
        self.heap.append(ele)
        self.bubble_up(len(self.heap)-1)
    
    def extract_min(self):
        min_ele = self.heap[0]
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.bubble_down(0)
        return min_ele


class MaxHeap(object):
    def __init__(self):
        self.heap = [];
        
    def parent(self, index):
        return (index -1) // 2
    
    def left_child(self, index):
        return index * 2 + 1
    
    def right_child(self, index):
        return index * 2 + 2
    
    def size(self):
        return len(self.heap)
    
    def bubble_up(self,index):
        if index  == 0:
            return
        if self.heap[index] <= self.heap[self.parent(index)]:
            return
        self.heap[index],self.heap[self.parent(index)] = \
            self.heap[self.parent(index)], self.heap[index]
            
        self.bubble_up(self.parent(index))
    def bubble_down(self, index):
        
        if self.right_child(index) >= len(self.heap):
            return
        if (self.heap[index] >= self.heap[self.left_child(index)]) &\
            (self.heap[index] >= self.heap[self.right_child(index)]):
            return
        if self.heap[self.left_child(index)] > self.heap[self.right_child(index)]:
            # left child is larger
            self.heap[index],self.heap[self.left_child(index)] = \
                self.heap[self.left_child(index)], self.heap[index]
            self.bubble_down(self.left_child(index))
        else:
            # right child is smaller
            self.heap[index],self.heap[self.right_child(index)] = \
                self.heap[self.right_child(index)], self.heap[index]
            self.bubble_down(self.right_child(index))
    
    def insert(self, ele):
        self.heap.append(ele)
        self.bubble_up(len(self.heap)-1)
    
    def extract_max(self):
        min_ele = self.heap[0]
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.bubble_down(0)
        return min_ele



def MaintainMed(left_h, right_h, new_ele):
    if (left_h.size()==0):
        left_h.insert(new_ele)
        return left_h, right_h, new_ele
    elif (right_h.size()==0):
        if new_ele >= left_h.heap[0]:
            right_h.insert(new_ele)
        else:
            right_h.insert(left_h.extract_max())
            left_h.insert(new_ele)
        return left_h, right_h,left_h.heap[0] 
         
    left_h_max = left_h.heap[0]
    right_h_min = right_h.heap[0]
    
    if (new_ele) >= right_h_min:
        # new_ele is larger
        right_h.insert(new_ele)
    elif (new_ele) <= left_h_max:
        # new_ele is smalller
        left_h.insert(new_ele)
    else:
        left_h.insert(new_ele)
    
    if  right_h.size() >= (left_h.size() +2) :
        # right side has more
        right_min = right_h.extract_min()
        left_h.insert(right_min)
    elif left_h.size() >= (right_h.size() +2):
        # left side has more
        left_max = left_h.extract_max()
        right_h.insert(left_max)
    
    if right_h.size() > left_h.size():
        med = right_h.heap[0]
    else:
        med = left_h.heap[0]
    return left_h, right_h, med
    

with open("W3_data.txt") as file:
    num_ls = [int(ln) for i,ln in enumerate(file)]
        

rolling = [11,2,3,4,10,6,7,80,9]

left_h = MaxHeap()
right_h = MinHeap()
ans = 0
ls = []
for i,ele in enumerate(num_ls):
    
    """
    ls += [ele]
    ls.sort()
    med_i = (i+2)//2-1 if (i+1)%2 == 1 else (i+1)//2-1
    #print(med_i)
    print(ls)
    med = ls[med_i]
    """
    left_h, right_h,med = MaintainMed(left_h, right_h, ele)
    #print(left_h.heap,right_h.heap)
    #print(left_h.size() + right_h.size())
    
    #print(med)
    ans = (ans + med) %10000
    #print(ans, med)
    #print(ans)
    #if i == 15:
    #    break
    
        