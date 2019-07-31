### Traj as POI ###

#-- Real Model --# # Using same as real_model_graph.py
# This model links (creates edges between them) POI's based on 
# if they are part of the same trajectory portion and cell



### Null Model ###
# This code generates a graph by adding edges between POI's inside grid cells.
# Each POI is considered as a node. 
# Each POI is picked from each cell and gets 
# connected to a POI from other adjacent cell.

import networkx as nx
import pandas as pd
import numpy as np
import random


df = pd.read_csv('cell_poi_ny.csv')


cell_id = df['cell_id']
poi_id = df['poi_enum']


# initializing graph
graph = nx.Graph()


for i in range(len(poi_id)):

    # adding poi ids as graph nodes. 
    graph.add_node(poi_id[i])


output = []

# Keeping distinct cell id's.
# As one cell id appears multiple times.
# This helps us in storing all the poi id's
# against a single cell id i.e., the cells through
# which poi has passed.

for x in cell_id:
    if x not in output:
        output.append(x)


temp = []


for i in range(len(output)):

    for j in range(len(cell_id)):

        if (output[i] == cell_id[j]):
            temp.append(str(cell_id[j]) + "," + str(poi_id[j]))



#Splitting data into two lists.
s1 = [] 
s2 = [] 

for tmp in temp:
    t = tmp.split(",")
    s1.append(t[0])
    s2.append(t[1])


list_of_lists = [] 
st_edge = [] 

for i in range(len(s1)):
    
    try:

        # if first and second element has same cell id, add their relevant poi's 
        if (s1[i] == s1[i + 1]):
            # graph.add_edge(s2[i], s2[i + 1])
            st_edge.append(s2[i])

        # if both are not the same, then the other is last one to be added
        if (s1[i] != s1[i + 1]):
            st_edge.append(s2[i])
            list_of_lists.append(st_edge.copy())

            st_edge.clear() # making it clear for the cell id's of next trajectory

    except IndexError:
        st_edge.append(s2[i])
        list_of_lists.append(st_edge.copy())


#print(list_of_lists)

# relating poi's from one cell to another cell randomly by creating edges between them.

for i in range(len(list_of_lists)): # i gives access to individual list 


    for j in range(len(list_of_lists[i])): # j gives access to individual element

        try: 
            
            for k in range(len(list_of_lists[i + 1])): # k gives access to individual elements of next list

                graph.add_edge(list_of_lists[i][j], list_of_lists[i+1][k]) # creating edge between adjacent cell poi's.

        except IndexError:
            print("reached end")



list_of_edges = list(graph.edges)

nodes = []
for i in range(len(list_of_edges)):
    nodes.append(str(list_of_edges[i]).replace("(", "").replace(")", "").replace(", ", " ").replace("'", ""))

f = open("nodes_traj.edgelist", "w")

for i in range(len(nodes)):
    f.write(nodes[i] + "\n")

f.close()
        