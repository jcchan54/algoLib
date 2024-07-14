#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 14:22:10 2023

@author: johnsonchan
"""

class Dijkstra(object):
    def __init__(self, filename:str):
        self._graph = dict()
        self._dist = dict()
        
        self.X = set()
        self.A = dict()
        self.B = []
        
        
        with open(filename) as file:
            for i,ln in enumerate(file):
                nodes = ln.split()
                self._graph[int(nodes[0])] = [int(ele.split(',')[0]) for ele in nodes[1:]]
                self._dist[int(nodes[0])] = [int(ele.split(',')[1]) for ele in nodes[1:]]
                self.A[int(nodes[0])] = float("inf")
                
        
        
    def shortest_path(self,start_node:int, end_node:int):
        self.A[start_node] = 0
        
        while True:
            self.X.add(start_node)
            for i, node in enumerate(self._graph[start_node]):
                if node in self.X:
                    continue
                alt = self.A[start_node] + self._dist[start_node][i]
                if alt < self.A[node]:
                    self.A[node] = alt
            d = {key: self.A[key] for key in self.A if key not in self.X}
            
            if start_node == end_node:
                break
            
            start_node = min(d, key=d.get)
                    
        return self.A[end_node]
        
        

d = Dijkstra("W2_graph.txt")
for num in [7,37,59,82,99,115,133,165,188,197]:
    d = Dijkstra("W2_graph.txt")
    print(d.shortest_path(1, num))











