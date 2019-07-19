### Real Model ###

# This code generates edge list and walks of trajectory paths based on cells ids.
# 1st: it outputs a file that represents cell ids as edge lists in a format accepted by node2vec.
# 2nd: it outputs trajectory paths as list of cell ids.

import networkx as nx
import pandas as pd

df = pd.read_csv('traj_as_poi.csv')

traj_id = df['traj_id']
cell_id = df['poi_enum']


graph = nx.Graph()

# graph only stores distinct nodes.
for i in range(len(cell_id)):
    graph.add_node(cell_id[i])


output = []

# Keeping distinct traj id's.
# As one traj ids appears multiple times.
# This helps us in storing all the cell id's
# against a single traj id i.e., the cells through
# which trajectory has passed.

for x in traj_id:
    if x not in output:
        output.append(x)


temp = []

# Making traj id and cell_id in order i.e.,
# putting same traj id's and cells through which it has passed.

for i in range(len(output)):

    for j in range(len(traj_id)):

        if (output[i] == traj_id[j]):
            temp.append(str(traj_id[j]) + "," + str(cell_id[j]))



#Splitting data into two lists.
s1 = [] # storing traj ids
s2 = [] # storing cell ids

for tmp in temp:
    t = tmp.split(",")
    s1.append(t[0])
    s2.append(t[1])


list_of_lists = [] # storing cell id's for each trajectory id as a list of lists
st_edge = [] # storing all the cell ids through which trajectory passed.

for i in range(len(s1)):
    
    try:
        if (s1[i] == s1[i + 1]):
            graph.add_edge(s2[i], s2[i + 1])
            st_edge.append(s2[i])

        if (s1[i] != s1[i + 1]):
            st_edge.append(s2[i])
            list_of_lists.append(st_edge.copy())

            st_edge.clear() # making it clear for the cell id's of next trajectory

    except IndexError:
        st_edge.append(s2[i])
        list_of_lists.append(st_edge.copy())
       

list_of_edges = list(graph.edges)

nodes = []
for i in range(len(list_of_edges)):
    nodes.append(str(list_of_edges[i]).replace("(", "").replace(")", "").replace(", ", " ").replace("'", ""))


# Storing edge list for real model nodes.

f_edgelist = open("realm_nodes.edgelist", "w")

for i in range(len(nodes)):
   f_edgelist.write(nodes[i] + "\n")
f_edgelist.close()

# storing trajectory walks as cell ids as list on each line.
f_walk = open("walks.txt", "w")

ls = []

for i in range(len(list_of_lists)):

    ls = str(list_of_lists).split("], [")

# Converting list of lists into a single list each line

for i in range(len(ls)):

    str(ls[0]).replace("[[", "")
    str(ls[len(ls) - 1]).replace("]]", "")

    if(ls[i] != ls[0] and ls[i] != ls[len(ls) - 1]):
        f_walk.write(str("["+ls[i] + "]\n"))

f_walk.close()