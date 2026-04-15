# ARITHMETIC MEAN, GEOMETRIC MEAN, HARMONIC MEAN FOR DISCRETE DATA
import numpy as np

data = np.array([1,2,2,3,3,3,4,4,5])

am = np.mean(data)
#gm = np.power(np.prod(data), 1/len(data))
gm2 = np.prod(data) ** (1/len(data))
#hm = 1 / np.mean([1/x for x in data])
h2m = 1 / np.mean(1/data)

print("Arithmetic Mean:", am)
print("Geometric Mean:", gm2)
print("Harmonic Mean:", h2m)