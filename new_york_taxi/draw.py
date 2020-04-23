from gmplot import gmplot
import pandas as pd

API_KEY = 'AIzaSyDbRSHdNyncQG1pqSgEWaI4RnfCp0wXMI4'

gmap = gmplot.GoogleMapPlotter(40.76781, -73.98228, 13, API_KEY)

def coordinates():


    df = pd.read_csv("slides_photo.csv")
    saved_col = df['coordinates']

    x = []
    y = []

    list_of_lists_x = []
    list_of_lists_y = []

    for item in saved_col:
        it = item[2:-2].split(')(')
        
        for item_0 in it:
            item_0 = item_0.split(', ')

            x.append(float(item_0[0]))
            y.append(float(item_0[1]))



        list_of_lists_x.append(x.copy())
        list_of_lists_y.append(y.copy())

        x.clear()
        y.clear()


    for i in range(len(list_of_lists_x)):

        gmap.plot(list_of_lists_x[i], list_of_lists_y[i], 'green', edge_width=3)


def trajectory():

    df = pd.read_csv("real_trajectory.csv")
    saved_col = df['trajectory']

    x = []
    y = []
    list_of_lists_x = []
    list_of_lists_y = []

    for item in saved_col:
        it = item[1:-1].split(',')
    

        for item_0 in it:
            item_0 = item_0.split(' ')

            x.append(float(item_0[0]))
            y.append(float(item_0[1]))

            # print(item_0[0], item_0[1])

        list_of_lists_x.append(x.copy())
        list_of_lists_y.append(y.copy())

        x.clear()
        y.clear()


    # for i in range(len(list_of_lists_x)):

    gmap.plot(list_of_lists_x[70], list_of_lists_y[70], 'red', edge_width=3)

coordinates()
trajectory()

# Draw
gmap.draw("my_map.html")
print("process completed")