from gmplot import gmplot
import pandas as pd

API_KEY = 'AIzaSyCcFSRX4kExONVVB9cqQynjh7EXgZwcyaI'

gmap = gmplot.GoogleMapPlotter(43.739829, -79.514102, 13, API_KEY)

f = open("grid_poi.txt", "r")
data = f.read()

tmp = str(data).split("\n")

tmp_0 = tmp[0:-1]
#print(tmp_0)

for tm in tmp_0:
	t = tm.split(" ")
	s1 = t[0].replace("(","")
	s2 = t[1].replace(")","")
	

	gmap.marker(float(s1), float(s2), 'cornflowerblue')
	#gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

df = pd.read_csv("grid.csv")
saved_col = df['coordinates']

x = []
y = []

for item in saved_col:
    it = item[2:-2].split(',')

    for item_0 in it:
        item_0 = item_0.split(' ')

        x.append(float(item_0[0]))
        y.append(float(item_0[1]))


        #gmap.marker(float(item_0[0]), float(item_0[1]), 'cornflowerblue')

golden_gate_park_lats = x
golden_gate_park_lons = y

gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'red', edge_width=3)
# Draw
gmap.draw("my_map.html")
print("process completed")