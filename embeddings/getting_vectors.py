import numpy as np
from numpy import linalg as LA

def distance(v1, v2):
    return np.sqrt(np.sum((v1 - v2) ** 2))

def build_word_vector_matrix(vector_file, n_words):
    #Return the vectors and labels for the first n_words in vector file
    numpy_arrays = []
    labels_array = []
    with open(vector_file, 'r') as f:
        for c, r in enumerate(f):
            sr = r.split()

            labels_array.append(sr[0])
            numpy_arrays.append(np.array([float(i) for i in sr[1:]]))

    #print(numpy_arrays[1])
    print(LA.norm(numpy_arrays[1] - numpy_arrays[2]))

    print(distance(numpy_arrays[1], numpy_arrays[2]))

    #         if c == n_words:
    #             return np.array(numpy_arrays[1:]), np.array(labels_array[1:])
    # return np.array(numpy_arrays[1:]), np.array(labels_array[1:])

build_word_vector_matrix('real_nodes.emb', 9)

