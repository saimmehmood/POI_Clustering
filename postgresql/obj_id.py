import random
import pandas as pd

# f = open("obj_id.csv", "w")
# f.write("obj_id\n")
path = "C:\\Users\\saim\\Documents\\POI_clustering\\postgresql\\driving.csv"

df = pd.read_csv(path)

for x in range(len(df)):
	print(str(random.randint(1,len(df) + 1)))
# 	f.write(str(random.randint(0,99)) + "\n")
# f.close()

# for i in range(3 * 3):
        
#         if (i == 0):
#             row = 0
#             col = 0
#         else:
#             row = int(i / 3)
#             col = int(i % 3)

#         print(row, col)

# print(1 % 3)
# print(1 / 3)
# import math 

# print(math.pow(3, 10) * math.pow(2, 7))
