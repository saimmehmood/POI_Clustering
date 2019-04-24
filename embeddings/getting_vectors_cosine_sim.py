import numpy as np
from numpy import linalg as LA


def cos_sim(a, b):
    """Takes 2 vectors a, b and returns the cosine similarity according
    to the definition of the dot product
    """
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

def build_word_vector_matrix(vector_file, n_words):
    #Return the vectors and labels for the first n_words in vector file
    numpy_arrays = []
    labels_array = []

    with open(vector_file, 'r') as f:
        for c, r in enumerate(f):
            sr = r.split()

            # storing all the labels
            labels_array.append(sr[0])
            # storing all the vectors
            numpy_arrays.append(np.array([float(i) for i in sr[1:]]))

    f_cos_sim = open("nullm_cos_sim.csv", "w")
    f_cos_sim.write("node1,node2,cosine_sim\n")


    # calculating and storing cosine similarity between every node.
    for i in range(len(numpy_arrays)):
        #print(i)
        for j in range(len(numpy_arrays)):
            #print(i)
            try:
                if(labels_array[i+1] != labels_array[j+1]):

                    f_cos_sim.write(str(labels_array[i + 1]) +","+ str(labels_array[j + 1]) + "," + str(cos_sim(numpy_arrays[i + 1], numpy_arrays[j + 1])) + "\n")

            except IndexError:
                print("")

   

build_word_vector_matrix('nodes.emb', 25)

