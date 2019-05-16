import imp

API_KEY = 'AIzaSyDpADSuP30VRsIDPMc6orgqjej-v2AIaBc'

write = imp.load_source('writeFile', '../writeFiles/writeFile.py')

coordinate = (43.739829, -79.514102)
#1000 trajectories without any waypoints
waypoints = write.generate_Random_Waypoints(30, coordinate, 0.05, .5)

for i in range(len(waypoints)):
	print(waypoints[i])

# coordinate_01 = (43.739829, -79.514102)
# coordinate_02 = (43.726355, -79.481279)

# driving_trajectories = write.getTrajectory(API_KEY, 'driving', waypoints, 0.05, 200, 'random_200_driving_trajectories', coordinate_01, coordinate_02)

#print(driving_trajectories)

#walking_trajectories = write.getTrajectory('walking', waypoints, 0.05, 1000, 'random_1000_walking_trajectories')

#transit_trajectories = write.getTrajectory('transit', waypoints, 0.05, 1000, 'random_1000_transit_trajectories')

#bicycling_trajectories = write.getTrajectory('bicycling', waypoints, 0.05, 1000, 'random_1000_bicycling_trajectories')


#--------------------------------------------------------------------------------------------------------------------------------------
#1000 trajectories with 1 waypoints

#waypoints = write.generate_Random_Waypoints(1, coordinate, 0.05, .5)

#walking_with_one_waypoint_trajectories = write.getTrajectory(API_KEY, 'walking', waypoints, 0.05, 1, 'random_1000_walking_with_one_waypoint_trajectories')






