import numpy as np
import time


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


    labels_array.pop(0)
    numpy_arrays.pop(0)

    # print(len(numpy_arrays))
    # print(len(labels_array))

    f_cos_sim = open("realm_cos_sim.csv", "w")
    f_cos_sim.write("node1,node2,cosine_sim\n")

    cos_similarity = []

    start = time.time()
    # calculating and storing cosine similarity between every node.
    for i in range(len(numpy_arrays)):

        for j in range(len(numpy_arrays)):

            if(labels_array[i] != labels_array[j]):

                if not (cos_similarity.__contains__(cos_sim(numpy_arrays[i], numpy_arrays[j]))):

                    f_cos_sim.write(str(labels_array[i]) + "," + str(labels_array[j]) + "," +
                                str(cos_sim(numpy_arrays[i], numpy_arrays[j])) + "\n")

                cos_similarity.append(cos_sim(numpy_arrays[i], numpy_arrays[j]))

    end = time.time()

    print(end - start)

build_word_vector_matrix('real_nodes.emb', 422)

