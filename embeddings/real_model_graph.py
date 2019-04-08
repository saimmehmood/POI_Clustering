import networkx as nx
import pandas as pd


df = pd.read_csv('check.csv')

traj_id = df['traj_id']
cell_id = df['cell_id']

graph = nx.Graph()

for i in range(len(cell_id)):
	graph.add_node(cell_id[i])

output = []

for x in traj_id:
    if x not in output:
        output.append(x)

for i in range(len(output)):
	
	for j in range(len(traj_id)):
		
		if(output[i] == traj_id[j]):

			print(traj_id[j], cell_id[j])
