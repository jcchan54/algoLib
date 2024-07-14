#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:19:27 2023

@author: johnsonchan
"""
import sys,threading
sys.setrecursionlimit(160900)
threading.stack_size(2**27)
print(sys.getrecursionlimit())

#%%

class KosarajuSCCs():
    def __init__(self,filename:str):
        self.graph = dict()
        self.rev_graph = dict()
        self.nodes = set()
        
        
        self.time = 0
        self.s = None
        self.function = dict()
        self.explored = []
        self.leaders = dict()
        
        
        with open(filename) as f:
            for i,ln in enumerate(f):
                h,t = ln.split()
                if int(h) not in self.graph:
                    self.graph[int(h)] = []
                    self.rev_graph[int(h)] = []
                if int(t) not in self.graph:
                    self.graph[int(t)] = []
                    self.rev_graph[int(t)] = []
                self.graph[int(h)].append(int(t))
                self.rev_graph[int(t)].append(int(h))
                
                self.nodes.add(int(h))
                self.nodes.add(int(t))
    def reset_global(self):
        self.time = 0
        self.s = None
        self.function = dict()
        self.explored = []
        self.leaders = dict()
        
                
    def DFS(self,G:dict,i:int):
        self.explored.append(i)
        if self.s not in self.leaders:
            self.leaders[self.s] = []
        self.leaders[self.s].append(i)
        
        for t in G[i]:
            if t not in self.explored:
                self.DFS(G,t)
                
        self.time = self.time+1
        self.function[i] = self.time
        return
    def fullDFS(self, G:dict):
        self.reset_global()
        for i in range(len(self.nodes),0,-1):
            
            if i not in self.explored:
                self.s = i
                self.DFS(G,i)
        return self.function, self.leaders
    def transform_graph(self,G:dict,f:dict):
        G_T = dict()
        for key in G:
            G_T[f[key]] = [f[e] for e in G[key]]
        return G_T
    def rev_transform_graph(self,G_T:dict,f:dict):
        G = dict()
        f_rev = {f[key]:key for key in f}
        for key in G_T:
            G[f_rev[key]] = [f_rev[e] for e in G_T[key]]
        return G
    def findFCCs(self):
        f1, l1 = self.fullDFS(self.rev_graph)
        G_T = self.transform_graph(self.graph, f1)
        f2, l2 = self.fullDFS(G_T)
        return self.rev_transform_graph(l2,f1)

#filename = "W1_graph.txt"
filename = "W1_unit_test4.txt"
a = KosarajuSCCs(filename)
l2 = a.findFCCs()
sizeOfSCCs = [len(l2[key]) for key in l2]
sizeOfSCCs.sort()
print("The largest size of SCCs: ", sizeOfSCCs[-5:])


#%%








