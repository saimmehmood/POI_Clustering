from googleplaces import GooglePlaces, types, lang
from decimal import Decimal
import os, json
import math
import numpy as np
import pandas as pd

calculation = imp.load_source('calculation', 'trajectory_code/distance/calculation.py')

# This function is needed to avoid json.dump decimal storage error 
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

# given the coordinates of two points, step value and your api key
# this function will calculate all the unique point of interests (POIs)
# in the rectangle defined by the two points
# step value denotes distance between POIs retrieval (must be given in float value). 
# format for values (lat & long (first point), lat & long (second point), step value (float), google places api key)
def scanAreaForPOIs(lat1, long1, lat2, long2, step, your_api):
	
	google_places = GooglePlaces(your_api)

	Id_of_places = {}
	place_details = []
	
	# sorting the given latitudes
	x_cords = [lat1, lat2]
	x_cords.sort()

	# sorting the given longitudes
	y_cords = [long1, long2]
	y_cords.sort()

    # storing all the latitude & longitude points 
	x_points = np.arange(x_cords[0], x_cords[1], float(step))
	y_points = np.arange(y_cords[0], y_cords[1], float(step))


	#k = 0 # to keep in check google api limit of 1000 requests per 24h (in case you need it)
	
	# traversing through all the latitude and longitude points
	for i in range(len(x_points)):
		x = x_points[i]		#lat
		for j in range(len(y_points)):
			y = y_points[j]		#long
			
			

			# querying google api
			query_result = google_places.nearby_search(
				location=str(x) + ',' + str(y), radius=30)


			# getting ID's from the specified location
			for place in query_result.places:

				plId = str(place.place_id)
				place.get_details()
				place_details.append(place.details)

				
				
				if plId not in Id_of_places:	
					# save place		
					Id_of_places[plId] = True
				
				
				else:	
					# store it as a false place
					Id_of_places[plId] = False
				

		# Breaking both loops to avoid reaching limit (in case you need it)		
		# 	k += 1
		# 	if (k == 100):
		# 		print("breaking loop")
		# 		break

		# if (k == 100):
		# 	print("breaking loop")
		# 	break

	Id_of_places = [key for key, value in Id_of_places.items() if value]
		
	# storing fetched POI detail from google api as a json file
	for i in range(len(place_details)):
		data = json.loads(json.dumps(place_details[i], default=decimal_default))

		# storing POI detail with ID as a file name.
		if str(data["place_id"]) in Id_of_places:
			print(str(data["place_id"]))
			with open('datasets\\upper_manhattan\\'+ str(data["place_id"]) +'.json', 'w') as outfile:
				json.dump(place_details[i], outfile, indent=4, default=decimal_default)

	
	# store Id_of_places (only) outside loop (in case you need them seperately)
	# with open('storing_all_ID.json', 'a') as outfile:
	# 	json.dump(Id_of_places, outfile, indent=2)



YOUR_API_KEY = 'AIzaSyDpADSuP30VRsIDPMc6orgqjej-v2AIaBc'

# (un-comment below function calling line to generate more data sets)
#scanAreaForPOIs(40.827943, -73.950741, 40.812798, -73.936505, 0.001, YOUR_API_KEY)  # upper manhattan

def getPOIAroundTrajectory(route): # using Euclidean distances
	path_to_json = 'C:\\Users\\saim\\Documents\\POI_clustering\\datasets\\new_north_york' # relative path to your stored data-sets
	json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
	
	threshold = 5

	route_x = []
	route_y = []

	for item in route:
    	it = item[2:-2].split('), (')

    for item_0 in it:
        item_0 = item_0.split(',')

        route_x.append(float(item_0[0]))
        route_y.append(float(item_0[1]))

    

	for i in range(len(json_files)):	
		with open(path_to_json + '\\' + str(json_files[i])) as file:
			data = json.load(file)
			data["geometry"]["location"]["lat"]
			data["geometry"]["location"]["lng"]
			
	
#getPOIAroundTrajectory(0)	


def fetchTrajectory():
	df = pd.read_csv("C:\\Users\\saim\\Documents\\POI_clustering\\trajectory_code\\trajectory_files\\random_100_driving_trajectories.csv") # relative path to your stored trajectories
	saved_col = df['trajectory']

	getPOIAroundTrajectory(saved_col[0])


fetchTrajectory()