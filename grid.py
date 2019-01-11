
# Dividing geographical area into grids cells.
def GridTrajectories(grids, lat1, long1, lat2, long2):

	# sorting the given latitudes
	x_cords = [lat1, lat2]
	x_cords.sort()

	print(x_cords)
	
	# sorting the given longitudes
	y_cords = [long1, long2]
	y_cords.sort()
	print(y_cords)

GridTrajectories(0, 43.739829, -79.514102, 43.726355, -79.481279)