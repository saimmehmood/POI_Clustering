
# walks = []
# walk = []
# with open("walks.txt") as file:

#     for line in file:
#         tmp = line.strip("\n").replace("[", "").replace("]", "").replace("'", "").replace(",", "")
#         t = tmp.split(" ")
#         for i in range(len(t)):
#             walk.append(t[i])

#         walks.append(walk.copy())

#         walk.clear()


# for walk in walks:
#     print(walk)
# print(walks[0][0])
# print(type(walks[0][0]))
# print(walks[0])
# print(type(walks[0]))
# print(walks)
# print(type(walks))

# f = open('check.txt', 'w')
#
# f.write("\N{INFINITY}")


# import pandas as pd

# df = pd.read_csv("cos_sim_diff.csv")

# diff = df['cos_sim_diff']

# print(max(diff))


# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
#
# common_num = [a for a in list_a for b in list_b if a == b]
#
# print(common_num)

# import pandas as pd
#
# df = pd.read_csv("nullm_cos_sim.csv")
#
# node1 = df['node1']
# node2 = df['node2']
#
# val1 = 3634
# val2 = 4089
#
# if(node1.__contains__(val1) and node2.__contains__(val2)):
#     print("it works")


# print(len(null_node1))
# print(len(real_node1))
# f = open("work.txt", "w")

# i = min(null_node1)
# j = max(null_node1)
# initial = i
# start = time.time()
#
# while (i <= j):
#     k = initial
#     while(k <= j):
#
#         print(i, k)
#
#         k = k + 1
#
#     i = i + 1

# # if (null_node1.__contains__(4186) and null_node2.__contains__(4185)):
# #     print("yes")
#

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# print( [[row[i] for row in matrix] for i in range(3)] )

import statistics

ar1 = [2, 3, 5, 8]
ar2 = [10, 12, 14, 16, 18, 20]

ar3 = []

for i in range(len(ar1)):
    ar3.append(ar1[i])

for j in range(len(ar2)):
    ar3.append(ar2[j])

print(statistics.median(ar3))