### Traj as POI ###

# This code generates POI walks
# for Null Model. Converts Random
# walks on cells into walks on POIS.


import pandas as pd

# cell_poi_ny contains cell ids and poi ids
# for the pois that are inside those cells.
df = pd.read_csv('cell_poi_ny.csv')


cell_id = df['cell_id']
poi_id = df['poi_enum']

output = []

# creating a list of distinct cell ids.
for x in cell_id:
    if x not in output:
        output.append(x)

# creating a dictionary with empty lists and unique cell_id's being keys.
new_dict = {new_list: [] for new_list in output}

for i in range(len(output)):

    for j in range(len(cell_id)):

        if (output[i] == cell_id[j]):

            # storing all poi id's as list against key value of cell id
            new_dict[output[i]].append(poi_id[j])



# stroing walks as pois
f_walk = open("null_walks_poi.txt", "w")


# reall null walks
with open("exp.txt") as file:

    walks = file.readlines()


for i in range(len(walks)):

    walk = walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n","").split(",")

    #print(walk)

    # for maintaining proper spacing in write file.
    x = 0

    for w in walk:

 
        if(int(w) in new_dict):

            x = x + 1
            #print(w, new_dict[int(w)])
            f_walk.write(str(new_dict[int(w)]))

    if x > 0:

        f_walk.write("\n")    

f_walk.close()