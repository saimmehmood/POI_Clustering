# import warnings
# from text_unidecode import unidecode
# from collections import deque
# warnings.filterwarnings('ignore')


# import pandas as pd
# from sklearn.manifold import TSNE
# import numpy as np
import networkx as nx
import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# import seaborn as sns
# from node2vec import Node2Vec

# sns.set_style('whitegrid')



# df = pd.read_csv("trajascells.csv")
# col_traj_id = df['traj_id']


df = pd.read_csv('cell_names.csv')
saved_col = df['name']


G = nx.Graph()

for i in range(len(saved_col)):
	G.add_node(saved_col[i])



# G.add_nodes_from([2,3])
# G.add_edge(2,3)
# G.add_edge(3,2)

#print([n for n in G])

# Getting range of rows and columns from last node
list_of_nodes = list(G.nodes)
size = len(list_of_nodes)
last_node = list_of_nodes[int(size) - 1]

val = last_node.split(":")

row = val[0].replace("C", "")
col = val[1]


for i in range(int(row)):

	for j in range(int(col)):

		
