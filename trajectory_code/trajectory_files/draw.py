from gmplot import gmplot
import pandas as pd

API_KEY = 'AIzaSyCcFSRX4kExONVVB9cqQynjh7EXgZwcyaI'

gmap = gmplot.GoogleMapPlotter(52.517671, 13.377802, 13, API_KEY)

# retrieving trajectories from the csv file.
df = pd.read_csv("random_500_driving_trajectories.csv")
saved_col = df['trajectory']

x = []
y = []

list_of_lists_x = []
list_of_lists_y = []

for item in saved_col:
    it = item[2:-2].split('), (')
    
    for item_0 in it:
        item_0 = item_0.split(',')

        x.append(float(item_0[0]))
        y.append(float(item_0[1]))



    list_of_lists_x.append(x.copy())
    list_of_lists_y.append(y.copy())

    x.clear()
    y.clear()


for i in range(len(list_of_lists_x)):

	gmap.plot(list_of_lists_x[i], list_of_lists_y[i], 'red', edge_width=3)

#Draw
gmap.draw("my_map.html")
print("process completed")