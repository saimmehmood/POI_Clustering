from gmplot import gmplot

API_KEY = 'AIzaSyCcFSRX4kExONVVB9cqQynjh7EXgZwcyaI'

gmap = gmplot.GoogleMapPlotter(43.672545, -79.412068, 13, API_KEY)

f = open("grid_poi.txt", "r")
data = f.read()

tmp = str(data).split("\n")

tmp_0 = tmp[0:-1]
#print(tmp_0)

for tm in tmp_0:
	t = tm.split(",")
	s1 = t[0].replace("(","")
	s2 = t[1].replace(")","")
	

	gmap.marker(float(s1), float(s2), 'cornflowerblue')

# Draw
gmap.draw("my_map.html")
print("process completed")