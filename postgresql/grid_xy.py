import math

# Dividing geographical area into grids cells.
# grids: input taken from user to divide area into grids
def grid_trajectories(grid_x, grid_y, lat1, long1, lat2, long2):

    # Area Boundaries:
    top_left = lat1, long1

    height = lat2 - lat1
    width = long2 - long1

    cell_width = width/grid_x
    cell_height = height/grid_y


    f = open("area_cells.csv", "w")
    f.write("grid_id,name,coordinates\n")


    store_coordinate = []


    for row in range(grid_y):

        for col in range(grid_x):

            
            # new_lat_coord = top_left[0] + cell_height * row
            # new_long_coord = top_left[1] + cell_width * col


            cell_top_left = ( top_left[0] + cell_height * row, top_left[1] + cell_width * col )

            cell_top_right = ( top_left[0] + cell_height * row, top_left[1] + cell_width * (col + 1) )
            
            cell_bot_left = ( top_left[0] + cell_height * (row + 1), top_left[1] + cell_width * col )
            
            cell_bot_right = ( top_left[0] + cell_height * (row + 1), top_left[1] + cell_width * (col + 1) )

            f.write(str(grid_x * grid_y) + ",C" + str(row) + ":" + str(col) + ",\"POLYGON(" + str(cell_top_left) + str(cell_top_right) + str(cell_bot_right) + str(cell_bot_left) + str(cell_top_left) + ")\"\n")

           
    
    f.close()

    f = open("grid.csv", "w")
    f.write("grid_id, x_dim, y_dim\n")

    # generating grid id by taking power of prime numbers.
    f.write(str(grid_x * grid_y) + "," + str(grid_x) + "," + str(grid_y)) #(gird_id, rows, columns)
    f.close()



grid_trajectories(3, 4, 40.836064, -74.014138, 40.698068, -73.951576) # (no of rows, no of cols, lat1, long1, lat2, long2)


