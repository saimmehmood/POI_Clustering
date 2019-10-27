import numpy as np
import pandas as pd
import time

df = pd.read_csv('cos_sim.csv')

# fetching all the columns from file.

diff = df['diff']
node1 = df['node1']
node2 = df['node2']

real_cos = df['real_cos_sim']
null_cos = df['null_cos_sim']

f = open("real_cos.txt", "w")

cleaned = []

# for i in range(len(null_cos)):
#
#     # if (null_cos[i] == "less"):
#     #     print(i)
#
#     if (null_cos[i] != "less") and (null_cos[i] != "infinite"):
#         cleaned.append(float(null_cos[i]))

# start = time.time()

# for i in range(len(diff)):
#
#     if (diff[i] != "less") and (diff[i] != "infinite"):
#         cleaned.append(float(diff[i]))

for i in range(len(real_cos)):

    if (real_cos[i] != "infinite") and (real_cos[i] != "less"):
        cleaned.append(float(real_cos[i]))

# reverse sorting to show the plot from highest to lowest. 
cleaned = sorted(cleaned, reverse=True)

for i in range(len(cleaned)):
    f.write(str(cleaned[i]) + "\n")

f.close()
