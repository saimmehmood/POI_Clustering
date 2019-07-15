import os, json


def getData():

	path_to_json = 'C:\\Users\\saim\\Documents\\POI_Clustering\\POI_datasets\\manhattan'
	json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
	#print(json_files)

	poi_x = []
	poi_y = []
	file_name = []

	f = open("poi_lat_long.csv", "w")
	f.write("p_id,point\n")
	for i in range(len(json_files)):
		file_name.append(str(json_files[i]).replace(".json", ""))
		with open(path_to_json + '/' + str(json_files[i])) as file:
			
			data = json.load(file)
			poi_x.append(float(data["geometry"]["location"]["lat"]))
			poi_y.append(float(data["geometry"]["location"]["lng"]))

		f.write(file_name[i] + ",POINT(" + str(poi_x[i]) + " " + str(poi_y[i]) + ")\n")

	f.close()

getData()