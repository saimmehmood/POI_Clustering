import googlemaps
import polyline
import imp 
import math

_path = imp.load_source('path', '../distance/calculation.py')

'''
   # return a path in formatted json file containing all import informations

   #parameter(s):
             start - an 2-tuple coordinate represents the starting point
             end - an 2- tuple coordinate represents the ending point
             waypoints - an list of locations to be alternated while remaining on the same path to destination
                       - there could be an empty list, which represents directed path from start to end
             traj_mode - a string that represents the path to travels by. i.e.: walking, driving, biking, transit 
             index - a number that represents the selective alternative paths to go 
             thershold - a number that represents the distance between each waypoints generated upon directions

'''
def getPath(API_KEY, start, end, waypoints, traj_mode, index, thershold):

    #connect to the google maps api via api key 
    _gmaps = googlemaps.Client(key=API_KEY)
    #allow convertion of an empty list
    if waypoints == []:
        waypoints == None

    _response = _gmaps.directions(start, end, waypoints=waypoints, mode=traj_mode, alternatives='true')
    
    #print(_response)
    if _response == []:
        return _response

    #print(_response[index])
    return _response[index]


#find the distance of a given path
def find_path_distance(path):
    distance = path['legs'][0]['distance']['text']
    return distance

#find the time of a given path
def find_path_time(path):
    time = path['legs'][0]['duration']['text']
    return time

#create a list in the form of (lat, lng) for start_location
def find_start_location(path):
    start_location = []

    print(path)
    steps = path['legs'][0]['steps']

    for i in steps:
        location = i['start_location']
        coordinate = (location['lat'], location['lng'])
        
        start_location.append(coordinate)
    
    return start_location

#extract reasonable constant K distance between two points
def _extract_polyline(start_location, end_location, radius_distance):
    new_points = [start_location]

    lat1 = start_location[0]
    lat2 = end_location[0]
    long1 = start_location[1]
    long2 = end_location[1]

    bearing = _path.calculateBearing(lat1, long1, lat2, long2)

    lat = lat1
    lon = long1

    point = _path.calculateDestination(lat, lon, bearing, radius_distance)
    
    distance = (_path.distanceLatLong(lat, lon, lat2, long2)) * 1000
    
    while distance > (radius_distance * 1000):

        point = _path.calculateDestination(lat, lon, bearing, radius_distance)
        new_points.append(point) 
        
        lat = point[0]
        lon = point[1]

        distance = (_path.distanceLatLong(lat, lon, lat2, long2))*1000
    
    return new_points
    
    
#return a list of decoded polyline coordinates given the index of the steps
def find_polylines(path, step_num):
    points_list = [] 
    steps = path['legs'][0]['steps']

    points = steps[step_num]['polyline']['points']
    points_list = polyline.decode(points)
    ''' 
    for s in range(0, len(steps)):
        points = steps[s]['polyline']['points']
        points_list = polyline.decode(points)

        location_list.append(points_list)
    '''

    return points_list

#create a list in the form of (lat, lng) for end_location
def find_end_location(path):
    end_location = []
    steps = path['legs'][0]['steps']

    for s in steps:
        location = s['end_location']
        coordinate = (location['lat'] , location['lng'])

        end_location.append(coordinate)

    return end_location


#given a list of steps, and the index of one path
#retrieve one trajectory/ path
def findRoute(path, start, end, waypoints, traj_mode, index, thershold):
    
    #initialized the values for the list(s)
    start_location = find_start_location(path)

    end_location = find_end_location(path)

    #concaternate in a parallel way
    route = []

    for i in range(0, len(start_location)):
        polyline = find_polylines(path, i)    

        length = len(polyline)
        for p in range(0, length - 1 ): 
            start = polyline[ p ]
            end = polyline[ p + 1 ]
            points = _extract_polyline(start, end, thershold)
            route += points

        route.append(polyline[ length - 1 ])

    return route









