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



# list_of_lists = []
# st_edge = []

# st_edge.append("1, 2, 3")
# st_edge.append("4, 5, 6")

# list_of_lists.copy(st_edge)

# del st_edge [:]

# print(list_of_lists)
# def learn_embeddings(walks):
#
#     walks = [map(str, walk) for walk in walks]
#     print(walks)
list_of_lists = []
walks = []
with open("walks.txt") as file:
    # walks.append(file.readline())
    # list_of_lists.append(walks.copy())
    for line in file:
        walks.append(line.replace("'", "").strip("\n"))
        #list_of_lists.append(walks)

# print(list_of_lists[0][0])
# print(type(list_of_lists[0][0]))
# print(type(list_of_lists[0]))
for walk in walks:
    list_of_lists.append(walk)

print(list_of_lists[0])
# print(list_of_lists)
# walk = []

# walk = walks.split("\n")
#
# for i in range(len(walk)):
#     print(walk[i])
#     walk = walks.split("\n")
#     try:
#         list_of_lists.append(walk[i])
#     except IndexError:
#         print(i)
#
#
# print(type(list_of_lists))
# print(list_of_lists)