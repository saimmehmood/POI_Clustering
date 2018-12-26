from gmplot import gmplot
import pandas as pd

API_KEY = 'AIzaSyCcFSRX4kExONVVB9cqQynjh7EXgZwcyaI'

gmap = gmplot.GoogleMapPlotter(43.739829, -79.514102, 13, API_KEY)

# retrieving trajectories from the csv file.
df = pd.read_csv("random_100_driving_trajectories.csv")
saved_col = df['trajectory']

x = []
y = []

for item in saved_col:
    it = item[2:-2].split('), (')
    print(it)
    for item_0 in it:
        item_0 = item_0.split(',')

        x.append(float(item_0[0]))
        y.append(float(item_0[1]))

golden_gate_park_lats = x
golden_gate_park_lons = y

gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=5)

# Draw
gmap.draw("my_map.html")
print("process completed")