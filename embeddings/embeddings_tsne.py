
### Null Model ###
# This code generates a graph by adding edges between grid cells.
# Each cell is considered as a node. 
# Each cell is connected to its adjacent cells i.e., (top, bottom, left & right)

import networkx as nx
import pandas as pd
import numpy as np



df = pd.read_csv('cells.csv')

cell_names = df['cell_names']
grid_id = df['grid_id']
cell_id = df['cell_id']

saved_col_name = []
saved_col_id = []

for i in range(len(cell_id)):
    if(grid_id[i] == 7776):
        saved_col_id.append(cell_id[i])

sorted_ids = sorted(saved_col_id)

# for i in range(len(sorted_ids)):
#     print(sorted_ids[i])

for i in range(len(cell_names)):
    if grid_id[i] == 7776:
        saved_col_name.append(cell_names[i])


graph = nx.Graph()

for i in range(len(sorted_ids)):
    #print(sorted_ids[i])
    graph.add_node(sorted_ids[i])

#print(graph.nodes())

# Getting range of rows and columns from last node

list_of_names = list(saved_col_name)
size = len(list_of_names)

max_row = 0
max_col = 0

for i in range(size):

    val = list_of_names[i].split(":")
    row = int(val[0].replace("C", ""))
    col = int(val[1])

    if(max_row < row):
        max_row = row
    if(max_col < col):
        max_col = col

#print(max_row, max_col)

# reshaping 1D list into 2D array.
arr = np.array(saved_col_id).reshape(max_row+1,max_col+1)

for i in range(max_row + 1):

    for j in range(max_col + 1):

        row_pos = i
        col_pos = j

        left = max(0, col_pos - 1)
        right = min(max_col, col_pos + 1)

        top = max(0, row_pos - 1)
        bottom = min(max_row, row_pos + 1)

        # Adding edges between grid cells.
        if (col_pos != left):
            graph.add_edge(arr[row_pos][col_pos], arr[row_pos][left])

        if (col_pos != right):
            graph.add_edge(arr[row_pos][col_pos], arr[row_pos][right])

        if (row_pos != top):
            graph.add_edge(arr[row_pos][col_pos], arr[top][col_pos])

        if (row_pos != bottom):
            graph.add_edge(arr[row_pos][col_pos], arr[bottom][col_pos])

list_of_edges = list(graph.edges)

nodes = []
for i in range(len(list_of_edges)):
    nodes.append(str(list_of_edges[i]).replace("(", "").replace(")", "").replace(", ", " "))

f = open("nodes.edgelist", "w")

for i in range(len(nodes)):
    f.write(nodes[i] + "\n")

f.close()

