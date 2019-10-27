### Real Model ###

# This code generates walks of trajectory paths based on cells ids. 
# It outputs trajectory paths as list of cell ids.

#import networkx as nx
import pandas as pd

df = pd.read_csv('traj_as_cells_ny_sample_1000.csv')

traj_id = df['traj_id']
cell_id = df['cell_id']

output = []

# Keeping distinct traj id's.
# As one traj ids appears multiple times.
# This helps us in storing all the cell id's
# against a single traj id i.e., the cells through
# which trajectory has passed.

for x in traj_id:
    if x not in output:
        output.append(x)


temp = []

# Making traj id and cell_id in order i.e.,
# putting same traj id's and cells through which it has passed.

for i in range(len(output)):

    for j in range(len(traj_id)):

        if (output[i] == traj_id[j]):
            temp.append(str(traj_id[j]) + "," + str(cell_id[j]))


#Splitting data into two lists.
s1 = [] # storing traj ids
s2 = [] # storing cell ids

for tmp in temp:
    t = tmp.split(",")
    s1.append(t[0])
    s2.append(t[1])


list_of_lists = [] # storing cell id's for each trajectory id as a list of lists
st_edge = [] # storing all the cell ids through which trajectory passed.

for i in range(len(s1)):
    
    try:
        if (s1[i] == s1[i + 1]):
        
         # connecting all cell id's that are part of the same traj.
            st_edge.append(s2[i])

        if (s1[i] != s1[i + 1]):
            st_edge.append(s2[i])
            list_of_lists.append(st_edge.copy())

            st_edge.clear() # making it clear for the cell id's of next trajectory

    except IndexError:

        # adding last element (cell id) belonging to the same trajectory. 
        st_edge.append(s2[i])
        list_of_lists.append(st_edge.copy())


# storing trajectory walks as cell ids as list on each line.
f_walk = open("walks.txt", "w")

ls = []

for i in range(len(list_of_lists)):

    ls = str(list_of_lists).split("], [")

# Converting list of lists into a single list each line

ls[0] = str(ls[0]).replace("[[", "")
ls[len(ls) - 1] = str(ls[len(ls) - 1]).replace("]]", "")

for i in range(len(ls)):
    
    f_walk.write(str("["+ls[i] + "]\n"))

f_walk.close()




