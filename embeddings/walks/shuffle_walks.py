import random

with open("walks.txt") as file:

    walks = file.readlines()


s_walk = open("shuffled_walks.txt", "w")

walk = []

for i in range(len(walks)):

	walk = list(walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n","").replace("'", "").split(","))

	#print(walk[i])
	# getting first element from walk and removing it
	first = walk.pop(0)

	random.shuffle(walk)

	walk.insert(0, first)

	s_walk.write(str(walk) + "\n")

s_walk.close()


def average_of_cell_walks():

	sum_of_walks_size = 0

	for i in range(len(walks)):

		walk = list(walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n","").replace("'", "").split(","))

		sum_of_walks_size = sum_of_walks_size + int((len(walk)))


	avg = sum_of_walks_size / int(len(walks))

	return avg