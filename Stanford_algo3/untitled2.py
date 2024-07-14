#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 00:26:18 2023

@author: johnsonchan
"""
import numpy as np
import time

#%%
# get the file path
file_path = 'W2_clustering.txt'
# file_path = 'test 1.txt'
# convert text file to np.array type
clustering_data = np.loadtxt(file_path)
int_clustering_data = clustering_data.astype(int)
print('int_clustering_data: ')
print(int_clustering_data)
#%%

# clustering algorithm

# test1 can be found before
# Initially, each point in a separate cluster,we have 500 nodes
clusters = {}
for x in range(1,501):
    clusters[x] = [x]
print('clusters: ')
print(clusters)
# print('clusters: ')
# print(clusters)

# sort the distance of nodes
sorted_index = np.argsort(int_clustering_data[:,2], axis=0) 

# set the number of clusters 
k = 4

# def a function to get the key by value in dictionary
# d: dictionary
# k: key
def get_key_by_value(d, k):
    for leader, nodes in d.items():
        if k in nodes:
            return leader

# test2 can be found before
# c: dictionary. cluster 
# a: key. added value in dict
# d: key. deleted value in dict
def update_cluster(c, a, d):
    c[a].extend(c[d])
    del c[d]

# initialize number of iteration    
iteration = 0

# 
print('whole_edges: ')
print(len(sorted_index))

# core algorithm
start_time = time.time()
for i in sorted_index:
    # print('i: ')
    # print(i)
    
    #iteration = iteration + 1
    # print('iteration: ')
    # print(iteration)
    min_edge = int_clustering_data[i,:]
    key1 = get_key_by_value(clusters, min_edge[0])
    key2 = get_key_by_value(clusters, min_edge[1])
    if key1 == key2:
        continue
    elif len(clusters[key1]) >= len(clusters[key2]):
        update_cluster(clusters, key1, key2)
    else:
        update_cluster(clusters, key2, key1)

    # print('k: ')
    # print(len(clusters))
    if len(clusters) == k:
        break
        
end_time = time.time()
print('time: ' + str(end_time - start_time) + 's ')
print('time: ' + str((end_time - start_time) / 60) + 'min')
print('time: ' + str((end_time - start_time) / 3600) + 'h')
print('clusters: ')
print(clusters)

#%%
clusters_keys = list(clusters.keys()) # [102, 384, 414, 462]

# initialize 
spacing = []

distance=0
# set all spacing of k-clusters
for i in range(len(clusters_keys)-1):
    j = i+1
    for k in range(j, len(clusters_keys)):
        spacing.append([clusters_keys[i], clusters_keys[k], distance])
spacing = np.array(spacing)
print('spacing: ')
print(spacing)

#%%
def min_distance(int_clustering_data, clusters, cluster1, cluster2):
    minimum = int_clustering_data[:,2].max()
    # print('minimum: ')
    # print(minimum)
    for i in clusters[cluster1]:
        # print('i: ')
        # print(i)
        for j in clusters[cluster2]:
            # print('j: ')
            # print(j)
            if i < j:
                find_position = np.all([int_clustering_data[:,0]==i, int_clustering_data[:,1]==j], axis=0)
                find_edge = np.argwhere(find_position==True)
                actural_position = find_edge[0][0]
                distance = int_clustering_data[actural_position, 2]
                if minimum > distance:
                    minimum = distance
            else:
                find_position = np.all([int_clustering_data[:,0]==j, int_clustering_data[:,1]==i], axis=0)
                find_edge = np.argwhere(find_position==True)
                actural_position = find_edge[0][0]
                distance = int_clustering_data[actural_position, 2]
                if minimum > distance:
                    minimum = distance
            # print('minimum: ')
            # print(minimum)
    return minimum
            
#%%
for i in range(len(spacing)):
    spacing[i,2] = min_distance(int_clustering_data, clusters, spacing[i,0], spacing[i,1])
#%%
print('spacing: ')
print(spacing)
print('max distance clusters: ')
print(spacing[np.argmax(spacing[:,2]), :])
print('max distance: ')
print(np.amax(spacing[:,2]))

