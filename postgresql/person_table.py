import pandas as pd
import uuid as unique_id

path = "C:\\Users\\saim\\Documents\\POI_clustering\\postgresql\\driving.csv"

df = pd.read_csv(path)

file = open('unique_id.csv', 'w')
file.write("unique_id\n")

for i in range(len(df)):
	file.write(str(unique_id.uuid4()) + "\n")
file.close()