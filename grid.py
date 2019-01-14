
import imp

calculation = imp.load_source('calculation', 'trajectory_code/distance/calculation.py')

# Dividing geographical area into grids cells.
def GridTrajectories(grid, lat1, long1, lat2, long2):

	height = calculation.distanceLatLong(lat1, long1, lat2, long1)
	width = calculation.distanceLatLong(lat1, long1, lat1, long2)

	cell_height = height/grid
	cell_width = width/grid

	

GridTrajectories(2, 43.739829, -79.514102, 43.726355, -79.481279)