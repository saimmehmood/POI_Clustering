ids = {}

val1 = 'C00'
val2 = 'C01'
ids['201'] = {val1, val2}

#print (ids['201'])

import networkx as nx

G = nx.Graph()

G.add_nodes_from([2,3])
G.add_edge(2,3)
G.add_edge(3,2)

