import networkx as nx
import pandas as pd
import numpy as np



df = pd.read_csv('cells.csv')

cell_names = df['cell_names']
grid_id = df['grid_id']

saved_col = []

for i in range(len(cell_names)):
    if grid_id[i] == 216:
        saved_col.append(cell_names[i])

graph = nx.Graph()

for i in range(len(saved_col)):
    graph.add_node(saved_col[i])

# Getting range of rows and columns from last node

list_of_nodes = list(graph.nodes)
size = len(list_of_nodes)
last_node = list_of_nodes[int(size) - 1]

val = last_node.split(":")

row = int(val[0].replace("C", "")) + 
col = int(val[1])

arr = np.array(list_of_nodes).reshape(row+1,col+1)

for i in range(row + 1):

    for j in range(col + 1):

        current_pos = i

        left_neighbor = max(0, current_pos - 1)
        right_neighbor = min(row, current_pos + 1)

        top_neighbor
        bottom_neighbor
