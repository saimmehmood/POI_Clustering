import imp 
import writeFile 
drawer = imp.load_source('drawer', '../trajectory/draw.py')

API_KEY = 'AIzaSyBM2EVG_35lLPzdAPgNJu7YFjRNvTwEA_E'
coordinate = (43.73254, -79.30589)

#generate_Random_Waypoints(number_of_waypoints, coordinate, thershold, radius)
waypoints = writeFile.generate_Random_Waypoints(0, coordinate, 0.05, .5)

#getTrajectory(travel_mode, waypoints, thershold, number_of_trajectory, name_of_file)
one_element_trajectory = writeFile.getTrajectory(API_KEY, 'walking', waypoints, 0.05, 1, 'example')

#okay, the pin point is not draw yet, we can add the pinpoint
drawer.draw(one_element_trajectory[0], 'red', 'example', 10)

