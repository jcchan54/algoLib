#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:44:07 2023

@author: johnsonchan
"""

class Node(object):
    def __init__(self, 
                 left:object= None, 
                 right:object= None)-> None:
        self.left = left 
        self.right = right 
        
    def children(self)->tuple:
        return self.left, self.right 
    
    def __str__(self)->tuple:
        return self.left, self.right
    
def huffman_code_tree(node:object, binStr:str = '')-> dict:
    if type(node) ==str:
        return {node: binStr}
    l,r = node.children()
    d = dict()
    d.update(huffman_code_tree(l,binStr+'0'))
    d.update(huffman_code_tree(r,binStr+'1'))
    return d
def make_tree(nodes: list):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = Node(key1,key2)
        nodes.append((node,c1+c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]
weights = []
with open("W3_huffman.txt") as file:
    for i, ln in enumerate(file):
        if i == 0:
            continue
        weights+= [int(ln)]
#weights = [123,12,2,56,87,9,110,103]
freq = {f'{i}':e for i, e in enumerate(weights)}
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
node = make_tree(freq)
encoding = huffman_code_tree(node)

#%%
a = sorted(encoding.items(), key=lambda x: len(x[1]), reverse=True)