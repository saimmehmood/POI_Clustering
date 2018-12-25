import sophicated_generator as generator 
from gmplot import gmplot
import pandas as pd 

lat = 43.73254
lon = -79.30589
lists = generator.VALID_points(lat, lon, 0.001, .5)

generator.random_select(lists)

gmap = gmplot.GoogleMapPlotter(lat, lon, 14)

Lat, Long = zip(*lists)

#color the path with red
gmap.plot(Lat, Long, '#FF6666', edge_width=10)

#color the flags with green yellow
gmap.scatter(Lat, Long, 'ADFF2F', size=8, marker=True)

for i in lists: 
    gmap.marker(i[0], i[1], 'red')

#gmap.marker(routes[5][0], routes[5][1], 'yellow')

gmap.draw('../generator.html')
