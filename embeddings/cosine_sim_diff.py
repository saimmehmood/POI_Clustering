import pandas as pd
import time



real_df = pd.read_csv("realm_cos_sim.csv")
real_node1 = real_df['node1']
real_node2 = real_df['node2']
real_cos_sim = real_df['cosine_sim']

null_df = pd.read_csv("nullm_cos_sim.csv")
null_node1 = null_df['node1']
null_node2 = null_df['node2']
null_cos_sim = null_df['cosine_sim']

f_cos_sim_diff = open("cos_sim_diff.csv", "w")
f_cos_sim_diff.write("null_node1,null_node2,real_node1,real_node2,cos_sim_diff\n")


# print(len(null_node1))
# print(len(real_node1))
f = open("work.txt", "w")

i = min(null_node1)
j = max(null_node1)
initial = i
start = time.time()



while (i <= j):
    k = initial
    while(k <= j):

        

        k = k + 1

    i = i + 1

# if (null_node1.__contains__(4186) and null_node2.__contains__(4185)):
#     print("yes")

end = time.time()

print(end - start)

# for i in range(len(null_node1)):
#
# 	count = 0
# 	for j in range(len(real_node1)):
# 		#print(j)
# 		if(null_node1[i] == real_node1[j] and null_node2[i] == real_node2[j]):
# 			f_cos_sim_diff.write(str(null_node1[i]) + "," + str(null_node2[i]) + "," + str(real_node1[j]) + "," + str(real_node2[j]) + "," + str((real_cos_sim[j]) - abs(null_cos_sim[i])) + "\n")
# 			count = count + 1
# 			break
#
# 	if(count == 0):
# 		f_cos_sim_diff.write(str(null_node1[i]) + "," + str(null_node2[i]) + "," + "infinite" + "," + "infinite" + "," + "infinite" + "\n")
#
#
#
#
#
# f_cos_sim_diff.close()