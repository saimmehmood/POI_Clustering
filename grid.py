# coding=utf-8
import imp
import math
import numpy as np

calculation = imp.load_source('calculation', 'trajectory_code/distance/calculation.py')

def cell_boundary_coordinates(lat1, long1, bearing, distance):

    coordinate = calculation.calculateDestination(lat1, long1, bearing, distance)

    return coordinate

def bearing(lat1, long1, lat2, long2):

    return calculation.calculateBearing(lat1, long1, lat2, long2)



# Dividing geographical area into grids cells.
def grid_trajectories(grids, lat1, long1, lat2, long2):

    # Area Boundaries:
    top_left = lat1, long1

    height = lat2 - lat1
    width = long2 - long1

    cell_width = width/grids
    cell_height = height/grids


    f = open("area_cells.txt", "w")
    f.write("Name Coordinates\n")


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



    # print(len(store_coordinate))

    # for i in range(len(store_coordinate)):
    # 	print(store_coordinate[i])
		# # f.write("C00," )
		# f.close()


grid_trajectories(3, 43.672545, -79.412068, 43.669763, -79.403223)


