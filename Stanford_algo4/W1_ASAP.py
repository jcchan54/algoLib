#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:51:04 2023

@author: johnsonchan
"""
from numpy import inf, argmin
#%%

class Asap():
    def __init__(self, filename):
        self.graph = dict()
        self.weights = dict()
        nodes = set()
        self.inverse_graph = dict()
        with open(filename) as file:
            for i,ln in enumerate(file):
                if i ==0 :
                    continue
                u, v, w = ln.split()
                u, v, w = int(u), int(v), int(w)
                if u not in self.graph.keys():
                    self.graph[u] = [v]
                    self.weights[u] = {v:w}
                else:
                    self.graph[u].append(v)
                    self.weights[u][v] = w
                    
                if v not in self.inverse_graph.keys():
                    self.inverse_graph[v] = [u]
                else:
                    self.inverse_graph[v].append(u)
                    
                nodes.add(u)
                nodes.add(v)
            for v in nodes:
                if v not in self.graph:
                    self.graph[v] = []
                if v not in self.weights:
                    self.weights[v] = dict()
                if v not in self.inverse_graph:
                    self.inverse_graph[v] = []
            self.nodes = list(nodes)
            self.v_ind = {v:i for i,v in enumerate(nodes)}

    def add_node_zero(self):
        
        self.graph[0] = self.nodes
        self.weights[0] = {v:0 for v in self.nodes}
        self.inverse_graph = {u:[0]+self.inverse_graph[u] for u in self.inverse_graph.keys()}
        self.inverse_graph[0] = []
        self.nodes = [0]+self.nodes
        self.v_ind = {v:i for i,v in enumerate(self.nodes)}
        


    
    def remove_node_zero(self):
        self.graph.pop(0)
        self.weights.pop(0)
        self.nodes.pop(0)
        self.inverse_graph.pop(0)
        for u in self.inverse_graph.keys():
            self.inverse_graph[u].pop(0)
        self.v_ind = {v:i for i,v in enumerate(self.nodes)}
        return
    
    def BellmanFord(self,s):
        A_im1 = [inf if v != s else 0 for v in self.nodes] 
        A_i = [0]*len(self.nodes)
        
        
        for i in range(1,len(self.nodes)+1):
            for v in self.nodes:
                
                alt_v_weights = [A_im1[self.v_ind[u]] + self.weights[u][v] for u in self.inverse_graph[v]]
                
                A_i[self.v_ind[v]] = min([
                    A_im1[self.v_ind[v]],
                    min( alt_v_weights if len(alt_v_weights) >0 else [inf]
                        )
                    ])
            if A_im1 == A_i:
                break
            Ai0 = A_im1.copy()
            A_im1 = A_i.copy()
        if (i >= len(self.nodes)-1) & (A_im1 != Ai0): 
            raise Exception("Negative Cycle")
        return {v: A_i[self.v_ind[v]] for v in self.nodes}

    
    def transform_edge(self, edge_weight):
        for u in self.weights:
            for v in self.weights[u]:
                self.weights[u][v]+= edge_weight[u] - edge_weight[v]
        return
    
    def min_dist_in_Q(self,dist,Q):
        min_dist = inf
        min_i = 9e9
        for v in Q:
            if dist[self.v_ind[v]] <= min_dist:
                min_dist = dist[self.v_ind[v]]
                min_i = self.v_ind[v]
        return min_dist, min_i
    
    def Dijkstra(self,s):
        Q = set(self.nodes)
        dist = [inf  if v != s else 0 for v in self.nodes]
        prev = [0]*len(self.nodes)
    
        while len(Q) > 0:    
            min_dist, u_i = self.min_dist_in_Q(dist,Q)
            Q.remove(self.nodes[u_i])
            
            for v in self.graph[self.nodes[u_i]]:
                alt = dist[u_i] + self.weights[self.nodes[u_i]][v]
                if alt < dist[self.v_ind[v]]:
                    dist[self.v_ind[v]] = alt
                    prev[self.v_ind[v]] = self.nodes[u_i]
        stortest_paths = {v:dist[self.v_ind[v]] for v in self.nodes}
        return stortest_paths
    
    def reverse_transform(self,edge_weight, new_dist):
        for u in new_dist:
            for v in new_dist[u]:
                new_dist[u][v] = new_dist[u][v] - edge_weight[u] + edge_weight[v]
        return new_dist
        
    def Johnson(self):
        print('adding zero node')
        self.add_node_zero()
        print('BF')
        edge_weight = self.BellmanFord(0)
        print('remove node zero')
        self.remove_node_zero()
        print("tranform")
        self.transform_edge(edge_weight)
        print("Dijkstra")
        dist_ls = {u:self.Dijkstra(u) for i,u in enumerate(self.nodes)}
        print("reverse transform")
        dist_ls = self.reverse_transform(edge_weight,dist_ls)
        print("min dist")
        min_dist = min([dist_ls[u][v] for u in dist_ls for v in dist_ls[u]])
        return min_dist
#%%
#filename = "W1unittest2.txt"
filename = "W1g3.txt"
#filename = "W1unittest.txt"

A = Asap(filename)
min_d = A.Johnson()









    