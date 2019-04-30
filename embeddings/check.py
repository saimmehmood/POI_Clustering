
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

f = open('check.txt', 'w')

f.write("\N{INFINITY}")


# import pandas as pd

# df = pd.read_csv("cos_sim_diff.csv")

# diff = df['cos_sim_diff']

# print(max(diff))