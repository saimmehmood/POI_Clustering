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

temp = []

for i in range(len(output)):
	
	for j in range(len(traj_id)):
		
		if(output[i] == traj_id[j]):

			temp.append(str(traj_id[j]) + "," + str(cell_id[j]))

s1 = []
s2 = []

for tmp in temp:
	t = tmp.split(",")
	s1.append(t[0])
	s2.append(t[1])

st_edge = []

for i in range(len(s1)):

	if (s1[i + 1] == s1[i]):
		st_edge.append(s2[i])



	
