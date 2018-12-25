import imp
import numpy as np 
import pandas as pd
import random 

#use one trajectory path and generate many more trajectories
path = imp.load_source('path', '../trajectory/route.py')

calculation = imp.load_source('calculation', '../distance/calculation.py')

#create a list that store the VALID points around a specific coordinate
def VALID_points(lat, long, step, radius):
    generate_points = []
    
    top_bound = calculation.calculateDestination(lat, long, 45.0, 4.0)

    low_bound = calculation.calculateDestination(lat, long, 225, 4.0)

    top_bound_x = top_bound[0]
    top_bound_y = top_bound[1]

    low_bound_x = low_bound[0]
    low_bound_y = low_bound[1]

    x_points = np.arange(low_bound_x, top_bound_x, float(step))
    y_points = np.arange(low_bound_y, top_bound_y, float(step))

    for x in x_points:
        for y in y_points:
            coordinate = (x, y)
            generate_points.append(coordinate)

    return generate_points

#randomly select a coordinate from a list of valid points
def random_select(list):
    length = len(list)

    index =  random.randint(0, length - 1)

    return list[index]



    
