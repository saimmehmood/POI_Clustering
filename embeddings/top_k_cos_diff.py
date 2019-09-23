import numpy as np
import pandas as pd
import time

df = pd.read_csv('cos_sim_10_walks.csv')


diff = df['diff']
node1 = df['node1']
node2 = df['node2']

f = open("diff_10.txt", "w")

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
# #node_dict = {new_list: [] for new_list in cleaned}

#storing cosine similarity differences in numpy array.
# arr = np.array([float(i) for i in cleaned])



# arr = np.array(cleaned)

# out_arr = np.argsort(arr)

# for i in range(len(arr)):
# 	f.write(str(arr[out_arr]))


# k = 10

# top = (arr[np.argsort(arr)[-k:]])
# lowest = (arr[np.argsort(arr)[:k]])


# print(top)
# print(lowest)


# j = 0



# for i in range(len(diff)):
#     if(str(diff[i]) == str(top[j])):
#         print(node1[i], node2[i])
#         j = j + 1
#end = time.time()

#print(end - start)


