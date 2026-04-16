# MEAN DEVIATION FOR CONTINUOUS DATA
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)
cmarks = [(edges[i]+edges[i+1])/2 for i in range(len(edges)-1)]

mean = sum(cmarks[i]*freq[i] for i in range(len(cmarks))) / sum(freq)
A = 14

md_A = sum(freq[i] * np.abs(cmarks[i]-A) for i in range(len(cmarks))) / sum(freq)
md_mean = sum(freq[i] * np.abs(cmarks[i]-mean) for i in range(len(cmarks))) / sum(freq)

print("mean deviation about", A, "is:", md_A)
print("mean deviation about mean:", md_mean)