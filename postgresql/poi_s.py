import os, json

def getData():

	path_to_json = 'C:\\Users\\saim\\Documents\\POI_Clustering\\POI_datasets\\new_north_york'
	json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

	poi_x = []
	poi_y = []

	f = open("poi_lat_long.txt", "w")
	f.write("latitude longitude\n")
	for i in range(len(json_files)):
		#print(json_files[i])
		with open(path_to_json + '/' + str(json_files[i])) as file:
			data = json.load(file)
			poi_x.append(float(data["geometry"]["location"]["lat"]))
			poi_y.append(float(data["geometry"]["location"]["lng"]))

		f.write(str(poi_x[i]) + "," + str(poi_y[i]) + "\n")

	f.close()

getData()