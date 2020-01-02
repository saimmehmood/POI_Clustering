### Traj as POI ###

# This code generates POI walks
# for Null Model. Converts Random
# walks on cells into walks on POIS.


import pandas as pd
import numpy as np
from collections import defaultdict

# cell_poi_ny contains cell ids and poi ids
# for the pois that are inside those cells.
df = pd.read_csv('cell_poi_ny.csv')


cell_id = df['cell_id']
poi_id = df['poi_enum']

output = []

# creating a list of distinct cell ids.
# for x in cell_id:
#     if x not in output:
#         output.append(x)
#
# # creating a dictionary with empty lists and unique cell_id's being keys.
# new_dict = {new_list: [] for new_list in output}
#
# for i in range(len(output)):
#
#     for j in range(len(cell_id)):
#
#         if (output[i] == cell_id[j]):
#
#             # storing all poi id's as list against key value of cell id
#             new_dict[output[i]].append(poi_id[j])
#
#
# print(new_dict)



data_dict = defaultdict(list)

for i in range(len(cell_id)):

    data_dict[int(cell_id[i])].append(int(poi_id[i]))

# print(data_dict)
# stroing walks as pois
f_walk = open("null_walks_poi.txt", "w")

# # real null walks
with open("random_walks.txt") as file:

    walks = file.readlines()

for i in range(len(walks)):

    # print(walks[0])
    # break
    walk = str(walks[i]).replace("[", "").replace("]", "").replace(" ", "").replace("\n","").replace("\'","").split(",")

    # print(walk)

    # break
    # for maintaining proper spacing in write file.
    x = 0

    for w in walk:
 
        if(int(w) in data_dict):

            x = x + 1
            print(w, data_dict[int(w)])
            f_walk.write(str(data_dict[int(w)]))

    if x > 0:
        f_walk.write("\n")

f_walk.close()