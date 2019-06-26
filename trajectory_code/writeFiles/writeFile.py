#extract all data and write in all data to .csv files

import imp
from random import uniform
import gmplot
import csv 
import pandas as pd
route = imp.load_source('route', '../trajectory/route.py')
visual = imp.load_source('draw', '../trajectory/draw.py')
calculation = imp.load_source('calculation', '../distance/calculation.py')
generator = imp.load_source('generator', '../populate/sophicated_generator.py')

#_lower_boundary_coordinate = (43.757643, -79.169527)
#_upper_boundary_coordinate = (43.766771, -79.324935)

#populate trajectories
def getTrajectory(API_KEY, mode, waypoints, thershold, number_of_trajectory, filename, _upper_boundary_coordinate, _lower_boundary_coordinate):
    trajectories = []
    #open a text file formated in .csv 
    with open(filename + '.csv', 'w') as csvfile:
        fieldnames = ['distance', 'time', 'trajectory']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(0, number_of_trajectory):
            trajectory = generateTrajectory(API_KEY, mode, thershold, waypoints, _upper_boundary_coordinate, _lower_boundary_coordinate)
            trajectories.append(trajectory['trajectory'])
            writer.writerow(trajectory)

    return trajectories    

#generate start and end of the trajectory 
#AND ensure that start and end are not the same location
#ALSO check if there is a path exists from start to end
def generateStartEnd(mode, thershold, _upper_boundary_coordinate, _lower_boundary_coordinate):
    start = calculation.generateRandom(_upper_boundary_coordinate, _lower_boundary_coordinate)

    end = calculation.generateRandom(_upper_boundary_coordinate, _lower_boundary_coordinate)

    while (start[0] == end[0] or start[1] == end[0]):
        end = calculation.generateRandom(_upper_boundary_coordinate, _lower_boundary_coordinate)
    
    '''
    path = route.getPath(start, end, mode, 0, thershold)


    if path == []:
        return generateStartEnd(mode, thershold)
    ''' 

    return start, end

#produces a random trajectory with an input value representing id for each trajectory
def generateTrajectory(API_KEY, mode, thershold, waypoints, _upper_boundary_coordinate, _lower_boundary_coordinate):
    start, end = generateStartEnd(mode, thershold, _upper_boundary_coordinate, _lower_boundary_coordinate)
    path = route.getPath(API_KEY, start, end, waypoints, mode, 0, thershold)

    #error handling
    while path == []:
        start, end = generateStartEnd(mode, thershold, _upper_boundary_coordinate, _lower_boundary_coordinate)
        path = route.getPath(API_KEY, start, end, waypoints, mode, 0, thershold)
    
    trajectory = route.findRoute(path, start, waypoints, end, mode, 0, thershold)

    time = route.find_path_time(path)
    distance = route.find_path_distance(path)

    #construct a dictionary form name-value pair in json form 
    element = { 
            'distance' : distance,
            'time' : time, 
            'trajectory' : trajectory
            }
    
    #print(element)
    return element

#generate a random number of the waypoints according to the given parameter
def generate_Random_Waypoints(num, coordinate, step, radius):
    waypoints = []

    VALID_POINTS = generator.VALID_points(coordinate[0],coordinate[1], step, radius)

    for i in range(0, num):
        waypoint = generator.random_select(VALID_POINTS)
        waypoints.append(waypoint)

    return waypoints