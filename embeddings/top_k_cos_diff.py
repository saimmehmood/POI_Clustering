import numpy as np
import pandas as pd
import time

df = pd.read_csv('cos_sim_shuffle_walks.csv')


diff = df['diff']
node1 = df['node1']
node2 = df['node2']

f = open("diff_shuffle.txt", "w")

cleaned = []

#start = time.time()

for i in range(len(diff)):
    
    if(diff[i] != "infinite"):
    
        cleaned.append(float(diff[i]))
        #f.write(str(diff[i]) + "\n")


cleaned.sort()
# natsorted(cleaned)

for i in range(len(cleaned)):

	f.write(str(cleaned[i]) + "\n")

f.close()


