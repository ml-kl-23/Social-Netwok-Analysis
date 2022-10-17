# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:47:21 2022

We will use a SNAP public dataset Social circles: Facebook from Stanford 
University(https://snap.stanford.edu/data/ego-Facebook.html). 
This dataset consists of ‘circles’ (or ‘friends lists’) from Facebook. 
Facebook data was collected from survey participants. The dataset includes 
node features (profiles), circles, and ego networks. 


@author: manish
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


import networkx as nx
import matplotlib.pyplot as plt

G1 =nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype=int)

#nx.draw(G1)

'''
Degree centrality, betweenness centrality, closeness centrality
'''

pos = nx.spring_layout(G1)
betCent = nx.betweenness_centrality(G1, normalized=True, endpoints=True)
node_color = [20000.0 * G1.degree(v) for v in G1]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(G1, pos=pos, with_labels=False,
node_color=node_color,
node_size=node_size )
plt.axis('off')
sorted(betCent, key=betCent.get, reverse=True)[:5]


'''
Determine how Facebook friends are connected
'''

neigh = [1,30,70,100,200,350,500,750,900,1000,]
for i in range(len(neigh)):
    all_neighbors = list(nx.classes.function.all_neighbors(G1,neigh[i]))
    print('All neighbors for Node ', str(neigh[i]),' — -> ', str(all_neighbors))