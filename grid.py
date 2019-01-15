# coding=utf-8
import imp
import math

calculation = imp.load_source('calculation', 'trajectory_code/distance/calculation.py')

# Dividing geographical area into grids cells.
def GridTrajectories(grid, lat1, long1, lat2, long2):

    height = calculation.distanceLatLong(lat1, long1, lat2, long1)
    width = calculation.distanceLatLong(lat1, long1, lat1, long2)

    cell_height = height/grid
    cell_width = width/grid
 
 	# direction from one point towards another one
    bearing = calculation.calculateBearing(lat1, long1, lat2, long1)
  
    dia = math.pow(cell_height, 2) + math.pow(cell_width, 2)
    diagonal = math.sqrt(dia)

    cell_digonal_coordinate = calculation.calculateDestination(lat1, long1, bearing, cell_height)
    print(cell_digonal_coordinate)

GridTrajectories(2, 43.672545, -79.412068, 43.669763, -79.403223)
