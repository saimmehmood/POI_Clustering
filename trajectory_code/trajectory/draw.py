from gmplot import gmplot
import route
import imp 

calculation = imp.load_source('calculation', '../distance/calculation.py')

_lower_boundary_coordinate = (43.757643, -79.169527)
_upper_boundary_coordinate = (43.766771, -79.324935)

'''
point = calculation.generateRandom(_lower_boundary_coordinate, _upper_boundary_coordinate)

start = (point[0] , point[1])

point = calculation.generateRandom(_lower_boundary_coordinate, _upper_boundary_coordinate)

end =  (point[0] , point[1])

#start = '43.733700,-79.306929'
#end = '43.7255513,-79.2304354'
mode = 'transit'

waypoints = []

path = route.getPath(start, end, waypoints, mode, 0, 0.05)

routes = route.findRoute(path, start, end, waypoints, mode, 0, 0.05)

#print(route)

initial = routes[0]

initial_lat = initial[0]
initial_lng = initial[1]

gmap = gmplot.GoogleMapPlotter(initial_lat, initial_lng, 14)

Lat, Long = zip(*routes)

#color the path with red
gmap.plot(Lat, Long, '#FF6666', edge_width=10)

#color the flags with green yellow
#gmap.scatter(Lat, Long, 'ADFF2F', size=8, marker=True)

start_location = route.find_start_location(path)

for i in routes: 
    gmap.marker(i[0], i[1], 'red')

gmap.draw('../route.html')

distance = route.find_path_distance(path)
#print(distance)
'''

def draw(route, colour, file_name, scale):
    initial_lat = route[0][0]
    initial_long = route[0][1]

    gmap = gmplot.GoogleMapPlotter(initial_lat, initial_long, scale)

    #Lat, Long = zip(*route)

    #gmap.plot(Lat, Long, colour, edge_width=10)
    for i in route: 
        gmap.marker(i[0], i[1], 'red')

    gmap.draw(file_name + '.html')





