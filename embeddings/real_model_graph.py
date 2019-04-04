import networkx as nx
import pandas as pd


df = pd.read_csv('trajascells.csv')

traj_id = df['traj_id']
cell_id = df['cell_id']
cell_names = df['cell_names']

graph = nx.Graph()

print(len(traj_id))
print(len(cell_names))

for i in range(len(cell_names)):
	graph.add_node(cell_names[i])

# for i in range(len(traj_id)):

# 	for j in range(len(traj_id)):

# 		if(traj_id[i] == traj_id[j]):
# 			print(traj_id[j], cell_names[j])

print(graph.number_of_nodes())
print(graph.nodes())
