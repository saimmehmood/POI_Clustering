# ids = {}
#
# val1 = 'C00'
# val2 = 'C01'
# ids['201'] = {val1, val2}
#
# #print (ids['201'])
#
# import networkx as nx
#
# G = nx.Graph()
#
# G.add_nodes_from([2,3])
# G.add_edge(2,3)
# G.add_edge(3,2)



list_of_lists = []
st_edge = []

st_edge.append("1, 2, 3")
st_edge.append("4, 5, 6")

list_of_lists.copy(st_edge)

del st_edge [:]

print(list_of_lists)