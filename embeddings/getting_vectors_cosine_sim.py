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

def getting_vector_cosine_sim(vector_file_01, vector_file_02):

    #Return the vectors and labels for the first n_words in vector file.
    numpy_array_01 = []
    labels_array_01 = []

    numpy_array_02 = []
    labels_array_02 = []

    # first embedding file
    with open(vector_file_01, 'r') as f:
        for c, r in enumerate(f):
            sr = r.split()

            # storing all the labels
            labels_array_01.append(sr[0])

            # storing all the vectors
            numpy_array_01.append(np.array([float(i) for i in sr[1:]]))

    labels_array_01.pop(0)
    numpy_array_01.pop(0)

    with open(vector_file_02, 'r') as f:
        for c, r in enumerate(f):
            sr = r.split()

            # storing all the labels
            labels_array_02.append(sr[0])

            # storing all the vectors
            numpy_array_02.append(np.array([float(i) for i in sr[1:]]))

    labels_array_02.pop(0)
    numpy_array_02.pop(0)

    null_dict = {}

    for i in range(len(labels_array_01)):
        null_dict.update({labels_array_01[i]: numpy_array_01[i]})

    real_dict = {}

    for i in range(len(labels_array_02)):
        real_dict.update({labels_array_02[i]: numpy_array_02[i]})

    min_label = min(labels_array_01)
    max_label = max(labels_array_01)

    i = int(min_label)
    m = int(max_label)

    #print(null_dict)
    # if '3573' in null_dict:
    #print(null_dict[str(i)])
    f_cos_sim = open("cos_sim.csv", "w")
    f_cos_sim.write("node1,node2,null_cos_sim,real_cos_sim,diff\n")

    start = time.time()
    while i < m:

        j = i + 1

        while i < j <= m:

            f_cos_sim.write(str(i) + "," + str(j) + ",")
            if str(i) and str(j) in null_dict:
                f_cos_sim.write(str(cos_sim(null_dict[str(i)], null_dict[str(j)])) + ",")
                #print(str(i) + "," + str(null_dict[str(i)]))
                #print(str(i))
                #f_cos_sim.write(str(i) + "," + str(j) + "," + )

            j = j + 1

        i = i + 1

    end = time.time()

    print(end - start)






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
    #print(sorted(labels_array))

    # f_cos_sim = open("nullm_cos_sim.csv", "w")
    # f_cos_sim.write("node1,node2,cosine_sim\n")

    # As node (i, j) and (j, i) will have same consine similarity, so we are keeping one of them.
    cos_similarity = []

    start = time.time()
    # calculating and storing cosine similarity between every node.
    # for i in range(len(numpy_arrays)):
    #
    #     for j in range(len(numpy_arrays)):
    #
    #         # removing same pairs of nodes.
    #         if(labels_array[i] != labels_array[j]):
    #
    #             # keeping one pair from (i, j) and (j, i).
    #             if not (cos_similarity.__contains__(cos_sim(numpy_arrays[i], numpy_arrays[j]))):
    #
    #                 f_cos_sim.write(str(labels_array[i]) + "," + str(labels_array[j]) + "," +
    #                             str(cos_sim(numpy_arrays[i], numpy_arrays[j])) + "\n")
    #
    #             cos_similarity.append(cos_sim(numpy_arrays[i], numpy_arrays[j]))

    end = time.time()

    print(end - start)

#build_word_vector_matrix('nodes.emb', 25)

getting_vector_cosine_sim('nodes.emb', 'real_nodes.emb')

