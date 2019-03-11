#import uuid as unique_id
import math

# Dividing geographical area into grids cells.
# grids: input taken from user to divide area into grids
def grid_trajectories(grid_x, grid_y, lat1, long1, lat2, long2):

    # Area Boundaries:
    top_left = lat1, long1

    height = lat2 - lat1
    width = long2 - long1

    cell_width = width/grid_y
    cell_height = height/grid_x


    f = open("area_cells.csv", "w")
    f.write("grid_id,name,coordinates\n")


    store_coordinate = []
    store_coordinate.append(top_left)

    start = top_left
    tmp = top_left

    for i in range(grid_x + 1):

        for j in range(grid_y):

            start = start[0], start[1] + cell_width
            store_coordinate.append(start)

        # tmp variable to store starting value of row
        tmp = tmp[0] + cell_height, tmp[1]
        start = tmp
        store_coordinate.append(start)

    store_coordinate.pop()
    
    # for i in range(len(store_coordinate)):
    #     print(str(store_coordinate[i]))

	# storing grid points inside txt file as 
	# (Name: cell name, Coordinates: cell boundary coordinates)    
    
    for i in range(grid_x * grid_y):

    	if (i == 0):
    		row = 0
    		col = 0
    	else:
	    	row = int(i / grid_y) 
	    	col = int(i % grid_y) 

    	index_01 = int((grid_y + 1) * row + col)
    	coor_01 = store_coordinate[index_01]

    	index_02 = int((grid_y + 1) * row + col + 1)
    	coor_02 = store_coordinate[index_02]

    	index_03 = int((grid_y + 1) * (row + 1) + col)
    	coor_03 = store_coordinate[index_03]

    	index_04 = int((grid_y + 1) * (row + 1) + col + 1)
    	coor_04 = store_coordinate[index_04]

#        print("C" + str(row) + str(col) + ",\"[" + str(coor_01) + ", " + str(coor_02) + ", " + str(coor_03) + ", " + str(coor_04) + "]\"")

        # (grid_id, cell_no, coordinates)
    	f.write(str(math.pow(2, grid_x) * math.pow(3, grid_y)) + ",C" + str(row) + str(col) + ",\"POLYGON(" + str(coor_01) + str(coor_02) + str(coor_04) + str(coor_03) + str(coor_01) + ")\"\n")
    
    f.close()

    f = open("grid.csv", "w")
    f.write("grid_id, x_dim, y_dim\n")

    # generating grid id by taking power of prime numbers.
    f.write(str(math.pow(2, grid_x) * math.pow(3, grid_y)) + "," + str(grid_x) + "," + str(grid_y)) #(gird_id, rows, columns)
    f.close()



grid_trajectories(2, 5, 43.739829, -79.514102, 43.726355, -79.481279) # (no of rows, no of cols, lat1, long1, lat2, long2)


