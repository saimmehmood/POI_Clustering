

# print(list_of_lists)
# def learn_embeddings(walks):
#
#     walks = [map(str, walk) for walk in walks]
#     print(walks)
list_of_lists = []
walks = []
walk = []
with open("walks.txt") as file:

    for line in file:
        tmp = line.strip("\n").replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        t = tmp.split(" ")
        for i in range(len(t)):
            walk.append(t[i])
        walks.append(walk.copy())

for walk in walks:
    print(walk)
# print(walks[0][0])
# print(type(walks[0][0]))
# print(walks[0])
# print(type(walks[0]))
# print(walk)
# print(type(walk))
# for walk in walks:
#     list_of_lists.append(walk)
#
# print(type(list_of_lists[0][0]))
# print(type(list_of_lists[0]))
# print(type(list_of_lists))
#
# print(list_of_lists[0][0])
# print(list_of_lists[0])
# print(list_of_lists)