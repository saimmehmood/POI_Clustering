

# Dividing geographical area into grids cells.
# grids: input taken from user to divide area into grids
def grid_trajectories(grids, lat1, long1, lat2, long2):

    # Area Boundaries:
    top_left = lat1, long1

    height = lat2 - lat1
    width = long2 - long1

    cell_width = width/grids
    cell_height = height/grids


    f = open("area_cells.txt", "w")
    f.write("Name, Coordinates\n")


    store_coordinate = []
    store_coordinate.append(top_left)

    start = top_left
    tmp = top_left

    for i in range(grids + 1):

        for j in range(grids):

            start = start[0], start[1] + cell_width
            store_coordinate.append(start)

        # tmp variable to store starting value of row
        tmp = tmp[0] + cell_height, tmp[1]
        start = tmp
        store_coordinate.append(start)

    store_coordinate.pop()

	# storing grid points inside txt file as 
	# (Name: cell name, Coordinates: cell boundary coordinates)    
    for i in range(grids * grids):
    	if (i == 0):
    		row = 0
    		col = 0
    	else:
	    	row = int(i / grids)
	    	col = int(i % grids)

    	index_01 = int((grids + 1) * row + col)
    	coor_01 = store_coordinate[index_01]

    	index_02 = int((grids + 1) * row + col + 1)
    	coor_02 = store_coordinate[index_02]

    	index_03 = int((grids + 1) * (row + 1) + col)
    	coor_03 = store_coordinate[index_03]

    	index_04 = int((grids + 1) * (row + 1) + col + 1)
    	coor_04 = store_coordinate[index_04]

    	f.write("C" + str(row) + str(col) + "," + str(coor_01) + "," + str(coor_02) + "," + str(coor_03) + "," + str(coor_04) + "\n")
    
    f.close()


grid_trajectories(5, 43.672545, -79.412068, 43.669763, -79.403223)


