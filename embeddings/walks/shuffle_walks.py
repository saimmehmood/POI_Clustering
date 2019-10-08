
import random
import pandas as pd

# Reading entire grid cells.
df = pd.read_csv('..\\cells_ny.csv')

cell_id = df['cell_id']


with open("..\\walks.txt") as file:

	walks = file.readlines()

# Creating walks for Intermediate Model which keeps
# first node same as real model and rest of the nodes
# are picked from all over the grid.
s_walk = open("..\\shuffled_walks.txt", "w")

walk = []
shuffle_all = []

for i in range(len(walks)):

	walk = list(walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n","").replace("'", "").split(","))

	first = walk.pop(0)

	shuffle_all.append(first)

	# taking 19 as the average of walks in real model is 20
	for j in range(19):

		shuffle_all.append(random.choice(cell_id))

	
	s_walk.write(str(shuffle_all) + "\n")

	# creating k perturbations every shuffled walk
	for k in range(9):

			random.shuffle(shuffle_all)

			s_walk.write(str(shuffle_all) + "\n")

	shuffle_all.clear()

s_walk.close()

# This function returns average of real walks.
def average_of_cell_walks():

	with open("..\\walks.txt") as file:

		walks = file.readlines()

	sum_of_walks_size = 0

	for i in range(len(walks)):

		walk = list(walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n","").replace("'", "").split(","))

		sum_of_walks_size = sum_of_walks_size + int((len(walk)))


	avg = sum_of_walks_size / int(len(walks))

	return avg


# We take real walks and add (k=9) perturbations for each walk.

def k_walk_perturbations():

	with open("..\\walks.txt") as file:

		walks = file.readlines()


	s_walk = open("shuffled_walks_10.txt", "w")

	walk = []

	for i in range(len(walks)):

		walk = list(walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n","").replace("'", "").split(","))

		s_walk.write(str(walk) + "\n")

		for k in range(9):

			random.shuffle(walk)

			s_walk.write(str(walk) + "\n")

	s_walk.close()