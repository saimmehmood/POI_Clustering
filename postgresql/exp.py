from gmplot import gmplot
import pandas as pd

API_KEY = 'AIzaSyCcFSRX4kExONVVB9cqQynjh7EXgZwcyaI'

gmap = gmplot.GoogleMapPlotter(43.739829, -79.514102, 13, API_KEY)

f = open('result.txt', 'r')
data = f.read()

tmp = str(data).split('\n')

tmp_0 = tmp[0:-1]

for tm in tmp_0:
	t = tm.split(' ')
	s1 = t[0]
	s2 = t[1]
	gmap.marker(float(s1), float(s2), 'cornflowerblue')

# Draw
gmap.draw("my_exp.html")
print("process completed")