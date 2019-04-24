import pandas as pd

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


for i in range(len(null_node1)):

    for j in range(len(real_node1)):

        if(null_node1[i] == real_node1[j] and null_node2[i] == real_node2[j]):
            f_cos_sim_diff.write(str(null_node1[i]) + "," + str(null_node2[i]) + "," + str(real_node1[j]) + "," + str(real_node2[j]) + "," + str(null_cos_sim[i] - real_cos_sim[j]) + "\n")

        # if(null_node1[i] != real_node1[j] and null_node2[i] != real_node2[j]):
        #     print(str(null_node1[i]) + "," + str(null_node2[i]) + "," + "\N{INFINITY}" + "\N{INFINITY}" + "\N{INFINITY}")
