
                                          Trajectory Documentations 
Overview: The focus of the program is to generate several trajectories via a variety of travel modes. The program is divided into 5 different directories for which each concentrate on different concerns. At each directory, there is a test file to verify the correctness and completeness of the implementation. To provide a sample experiment for the location-based inference algorithm, we build a data set of trajectories from the Google Direction API.  The main file to generate all trajectories is inside the Trajectory_Files directory and data of the trajectories is stored in a file formatted in csv. 

Distance directory:

calculation.py
------ contains all necessary functions that calculate all simple mathematics formulas 

distanceLatLong(Lat1, Long1, Lat2, Long2)
------- this function calculates the distance between two Locations, given in term of Latitude-Longitude format. 
------- parameters: 
           Lat1 – the latitude of the first location 
           Long1 – the longitude of the first location
           Lat2 - the latitude of the second location
           Long2 – the longitude of the second location

calculateDestination(lat, long, bearing, distance)
------this function return a 2-tuple coordinate in latitude-longitude format given a location, direction of the given location, and distance
------ parameters:
         Lat –  the latitude of the location
         Long – the longitude of the location
         Bearing – the direction of the destination location in term of degree 
         Distance – the distance to the destination from the given location

calculateBearing(lat1, long1, lat2, long2)
------this function calculates the angle form from the first location to the second location 
----- parameters: 
            Lat1 – the latitude of the first location 
              Long1 – the longitude of the first location
              Lat2 - the latitude of the second location 
              Long2 – the longitude of the second location

generateRandom(lower_bound, upper_bound)
---- this function randomly generate a location given two boundary locations that limited the location to be within the boundary. 
---- parameters: 
             lower_bound – a location in 2-tuple coordinate formatted as latitude-longitude 
             upper_bound – a location in 2-tuple coordinate formatted as latitude-longitude 

Populate directory:
Sophicated_generator.py
  ---- this file is mainly focus on generating a list of locations for adding waypoints to the trajectory such that it’s more realistic in testing 

VALID_points(lat, long, step, radius)
 ---- return a list of locations where each location is represented in term of a 2-tuple Latitude-Longitude format. 
---- parameters: 
             lat – the latitude of the location 
             long – the longitude of the location
            step – the distance between each location to be generated 
            radius – the max distance around from the starting location to be generated 

random_select(list)
----- select a point RANDOMLY from the list returned from VALID_points function
----- parameters:
                list -  a list of all the coordinates return from VALID_points function

Trajectory directory
route.py
getPath(API_KEY, start, end, waypoints, traj_mode, index, threshold)
 ---- return a json file obtained from sending request to the Google Direction API
 ---- parameters: 
            API_KEY – a code represented as a string where it can be obtained from Google Console
            start – a 2-tuple coordinate that represent the starting location of the path 
            end – a 2-tuple coordinate that represent the ending location of the path
            waypoints – a list of waypoints where a user might stop by while going from start to 
                               end, it may be an empty list which means a direct path from start to end
            traj_mode – a string represents the way to travel from start to end
                              -it can be only 4 modes: bicycling, driving, walking, and transit
            index – an integer that represent the number of alternative path
                      -to avoid any confusion, set index equals to 0 to ensure no index out of bound 
           thershold – the approximate distance between each point from start to end

find_path_distance(path)
--- return the distance of the route from start to end
--- parameter: path – a json-formatted string            
           
find_path_time(path)
--- return the time it takes to travel on the route from start to end
--- parameter: path – a json-formatted string
find_polyline(path, step_num)
--- return a list of coordinates that are decoded from receiving polyline in the json-formatted string
--- parameters: 
            path – a json-formatted string
            step_num – the index that represents the direction instructions
_extract_polyline(start_location, end_location, radius_distance)
--- return a list of coordinates in the path that are manually generated to satisfy such that the distance between each coordinate are approximate the same distance 
--- parameters: 
            start_location – a 2-tuple coordinate that represent the starting position before change in 
                                     direction
            end_location – a 2-tuple coordinate that represent the ending position before change in
                                    direction 
            radius_distance -  the distance between each coordinate

findRoute(path, start, end, waypoints, traj_mode, index, thershold)
--- return a list of complete coordinates that represents the path from start to end
--- parameters: 
           path – a json-formatted string
           start – a 2-tuple coordinate that represent the starting location of the path 
            end – a 2-tuple coordinate that represent the ending location of the path
            waypoints – a list of waypoints where a user might stop by while going from start to 
                               end, it may be an empty list which means a direct path from start to end
            traj_mode – a string represents the way to travel from start to end
                              -it can be only 4 modes: bicycling, driving, walking, and transit
            index – an integer that represent the number of alternative path
                      -to avoid any confusion, set index equals to 0 to ensure no index out of bound 
           thershold – the approximate distance between each point from start to end
writeFiles directory:
----- this directory mainly focuses on writing n number of trajectories onto formatted csv files
writefile.py
geneate_Random_Waypoints(num, coordinate, step, radius)
--- return a list of waypoints given number of randomly waypoints to be generated
--- parameters: 
          num – the number of waypoints to be generated
          coordinate – a 2-tuple coordinate such that the waypoint is randomly generate within the 
                              the range
          step – the maximum distance between each point that form the routes 
          radius – the distance range within the coordinate 
generateTrajectory(API_KEY,  id, mode, thershold, waypoints)
---- return a trajectory with unique id and its properties such as distance, and time
--- parameters: 
            API_KEY - a code represented as a string where it can be obtained from Google Console
            id – an id, can be a string or an integer, is uniquely describe the trajectory 
            mode – travel mode 
           thershold - the maximum distance between each point that form the routes
           waypoints – a list of waypoints where a user might stop by while going from start to 
                               end, it may be an empty list which means a direct path from start to end
geneateStartEnd(mode, thershold)
--- return a pair of start, end coordinates that are randomly generated
--- parameters: 
           mode – travel mode
           thershold - the maximum distance between each point that form the routes
 

    
getTrajectory(API_KEY, mode, waypoints, thershold, number_of_trajectory, filename)
--- return a list of k trajectories given the number_of_trajectory to be generated and write to file_name.csv 
--- parameters: 
         API_KEY - a code represented as a string where it can be obtained from Google Console
        mode – travel mode 
        thershold - the maximum distance between each point that form the routes
        waypoints – a list of waypoints where a user might stop by while going from start to 
                               end, it may be an empty list which means a direct path from start to end
        number_of_trajectory – the number of trajectory to be generated 
        filename – a string that represents the name of the file to be written all trajectories

    




  
