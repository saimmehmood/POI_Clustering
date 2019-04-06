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
    if(grid_id[i] == 8.08281277465e+38):
        saved_col_id.append(cell_id[i])

for i in range(len(cell_names)):
    if grid_id[i] == 8.08281277465e+38:
        saved_col_name.append(cell_names[i])

graph = nx.Graph()

for i in range(len(saved_col_name)):
    graph.add_node(saved_col_id[i])

# Getting range of rows and columns from last node

list_of_names = list(saved_col_name)
size = len(list_of_names)
last_node = list_of_names[int(size) - 1]

val = last_node.split(":")

row = int(val[0].replace("C", ""))
col = int(val[1])

# print(row, col)

# reshaping 1D list into 2D array.
arr = np.array(saved_col_id).reshape(row+1,col+1)

for i in range(row + 1):

    for j in range(col + 1):

        row_pos = i
        col_pos = j

        left = max(0, col_pos - 1)
        right = min(col, col_pos + 1)

        top = max(0, row_pos - 1)
        bottom = min(row, row_pos + 1)

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

