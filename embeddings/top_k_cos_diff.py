import numpy as np
import pandas as pd
import time

df = pd.read_csv('cos_sim.csv')

diff = df['diff']
node1 = df['node1']
node2 = df['node2']

f = open("top_k.csv", "w")

cleaned = []

#start = time.time()

for i in range(len(diff)):
    if(diff[i] != "infinite"):
        cleaned.append(diff[i])
        #f.write(str(diff[i]) + "\n")

# storing cosine similarity differences
arr = np.array([float(i) for i in cleaned])

k = 10

top = (arr[np.argsort(arr)[-k:]])
lowest = (arr[np.argsort(arr)[:k]])

j = 0



for i in range(len(diff)):
    if(str(diff[i]) == str(top[j])):
        print(node1[i], node2[i])
        j = j + 1
#end = time.time()

#print(end - start)


