# ARITHMETIC MEAN, GEOMETRIC MEAN, HARMONIC MEAN FOR CONTINUOUS DATA
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)
cmarks = [(edges[i]+edges[i+1])/2 for i in range(len(edges)-1)]

am = sum([cmarks[i]*freq[i] for i in range(len(cmarks))]) / sum(freq)

#gm = np.power(np.prod([cmarks[i]**freq[i] for i in range(len(cmarks))]), 1/sum(freq))
gm = np.prod(np.power(cmarks, freq)) ** (1 / sum(freq))

hm = sum(freq) / sum([freq[i]/cmarks[i] for i in range(len(cmarks))])

print("Arithmetic Mean:", am)
print("Geometric Mean:", gm)
print("Harmonic Mean:", hm)