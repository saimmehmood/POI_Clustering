# coding=utf-8
import imp
import math

calculation = imp.load_source('calculation', 'trajectory_code/distance/calculation.py')

def cell_boundary_coordinates(lat1, long1, bearing, distance):

    coordinate = calculation.calculateDestination(lat1, long1, bearing, distance)

    return coordinate

# Dividing geographical area into grids cells.
def grid_trajectories(grid, lat1, long1, lat2, long2):

    # Area Boundaries:
    top_left = lat1, long1
    bottom_left = lat2, long1

    top_right = lat1, long2
    bottom_right = lat2, long2

    # height & width of area
    height = calculation.distanceLatLong(top_left[0], top_left[1], bottom_left[0], bottom_left[1])
    width = calculation.distanceLatLong(top_left[0], top_left[1], top_right[0], top_right[1])

    # height and width of every cell
    cell_height = height/grid
    cell_width = width/grid
 
    # direction from one point towards another one
    bearing_left_to_right = calculation.calculateBearing(top_left[0], top_left[1], top_right[0], top_right[1])
    bearing_left_to_bottom = calculation.calculateBearing(top_left[0], top_left[1], bottom_left[0], bottom_left[1])
    bearing_towards_diagonal = calculation.calculateBearing(top_left[0], top_left[1], bottom_right[0], bottom_right[1])


    dia = math.pow(cell_height, 2) + math.pow(cell_width, 2)
    diagonal_distance = math.sqrt(dia)

    right = cell_boundary_coordinates(top_left[0], top_left[1], bearing_left_to_right, cell_width)
    bottom = cell_boundary_coordinates(top_left[0], top_left[1], bearing_left_to_bottom, cell_height)
    diagonal = cell_boundary_coordinates(top_left[0], top_left[1], bearing_towards_diagonal, diagonal_distance)

    f = open("area_cells.txt", "w")
    f.write("Rows Cells\n")
    f.close()

grid_trajectories(2, 43.672545, -79.412068, 43.669763, -79.403223)


