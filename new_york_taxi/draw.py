from gmplot import gmplot
import pandas as pd

API_KEY = 'AIzaSyCcFSRX4kExONVVB9cqQynjh7EXgZwcyaI'

gmap = gmplot.GoogleMapPlotter(40.76781, -73.98228, 13, API_KEY)

#retrieving trajectories from the csv file.
# df = pd.read_csv("grid.csv")
# saved_col = df['coordinates']

# x = []
# y = []

# for item in saved_col:
#     it = item[2:-2].split(',')

#     for item_0 in it:
#         item_0 = item_0.split(' ')

#         x.append(float(item_0[0]))
#         y.append(float(item_0[1]))

#         # golden_gate_park_lats = x
#         # golden_gate_park_lons = y

#         gmap.marker(float(item_0[0]), float(item_0[1]), 'cornflowerblue')

df = pd.read_csv("real_trajectory.csv")
saved_col = df['trajectory']

x = []
y = []
list_of_lists_x = []
list_of_lists_y = []

for item in saved_col:
    it = item[2:-2].split('), (')

    for item_0 in it:
        item_0 = item_0.split(', ')

        x.append(float(item_0[0]))
        y.append(float(item_0[1]))

        #print(item_0[0], item_0[1])

    list_of_lists_x.append(x.copy())
    list_of_lists_y.append(y.copy())

    x.clear()
    y.clear()


for i in range(100):

	gmap.plot(list_of_lists_x[i], list_of_lists_y[i], 'red', edge_width=3)
	#gmap.heatmap(list_of_lists_x[i], list_of_lists_y[i])


# gmap.plot(x, y, 'red', edge_width=3)


#gmap.heatmap(list_of_lists_x, list_of_lists_y) #, 'red', edge_width=3)

# #gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'red', edge_width=3)

# Draw
gmap.draw("my_map.html")
print("process completed")