import numpy as np


# generate n numbers that round up to a total of M
def proportion(length, magnitude):
    raw_vector = np.random.rand(length)
    s = sum(raw_vector)
    return [(x / s) * magnitude for x in raw_vector]
