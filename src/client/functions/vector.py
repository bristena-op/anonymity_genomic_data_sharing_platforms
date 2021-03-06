import random


def _gen_random_vector(len_vector, lower_bound, upper_bound):
    return [
        random.randint(lower_bound, upper_bound)
        for _ in range(len_vector)
    ]


def gen_vectors(nb_nodes, len_vector, lower_bound, upper_bounds):
    output_vectors = [
        _gen_random_vector(len_vector, lower_bound, upper_bounds)
        for _ in range(nb_nodes - 1)
    ]
    normalizing_vector = [
        -sum(x[i] for x in output_vectors)
        for i in range(len(output_vectors[0]))
    ]

    output_vectors.append(normalizing_vector)

    return output_vectors
def _gen_rand_resp_vector(len_vector, lower_bound, upper_bound):
    vector = []
    for _ in range(len_vector):
        vector.append([random.randint(lower_bound, upper_bound), random.randint(lower_bound, upper_bound)])
    return vector

def gen_response_vectors(nb_nodes, len_vector, lower_bound, upper_bounds, collisions):
    output_vectors = [
        _gen_random_vector(len_vector*collisions, lower_bound, upper_bounds)
        for _ in range(nb_nodes - 1)
    ]
    normalizing_vector = [
        -sum(x[i] for x in output_vectors)
        for i in range(len(output_vectors[0]))
    ]

    return output_vectors
