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

		if (output[i] == traj_id[j]):
			temp.append(str(traj_id[j]) + "," + str(cell_id[j]))

s1 = []
s2 = []

for tmp in temp:
	t = tmp.split(",")
	s1.append(t[0])
	s2.append(t[1])

st_edge = []

for i in range(len(s1)):
	# print(s1[i], s2[i])
	try:
		if (s1[i] == s1[i + 1]):
			graph.add_edge(s2[i], s2[i + 1])
	except IndexError:
		print("")

# print(graph.edges())
list_of_edges = list(graph.edges)

nodes = []
for i in range(len(list_of_edges)):
	nodes.append(str(list_of_edges[i]).replace("(", "").replace(")", "").replace(", ", " ").replace("'", ""))


f = open("realm_nodes.edgelist", "w")

for i in range(len(nodes)):
	f.write(nodes[i] + "\n")