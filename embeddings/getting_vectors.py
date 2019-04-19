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

            labels_array.append(sr[0])
            numpy_arrays.append(np.array([float(i) for i in sr[1:]]))

    f = open("cos_sim.csv", "w")
    f.write("node1,node2,cosine_sim")


    for i in range(len(numpy_arrays)):

        for j in range(len(numpy_arrays)):

            try:
                print(str(labels_array[i + 1]) +","+ str(labels_array[j + 1]) + "," + str(cos_sim(numpy_arrays[i + 1], numpy_arrays[j + 1])))

            except IndexError:
                print("index error occured")

    # print("Cosine Similarity:")
    # print(cos_sim(numpy_arrays[1], numpy_arrays[2]))
    # print("Euclidean distance:")
    # print(LA.norm(numpy_arrays[1] - numpy_arrays[2]))

    #         if c == n_words:
    #             return np.array(numpy_arrays[1:]), np.array(labels_array[1:])
    # return np.array(numpy_arrays[1:]), np.array(labels_array[1:])

build_word_vector_matrix('prac_nodes.emb', 3)

