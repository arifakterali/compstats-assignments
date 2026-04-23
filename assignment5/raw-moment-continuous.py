# RAW MOMENT FOR CONTINUOUS DATA
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)
cmarks = [(edges[i] + edges[i+1])/2 for i in range(len(freq))]

rmu1 = sum(cmarks[i]*freq[i] for i in range(len(cmarks))) / sum(freq)
rmu2 = sum(freq[i] * (cmarks[i] ** 2) for i in range(len(cmarks))) / sum(freq)
rmu3 = sum(freq[i] * (cmarks[i] ** 3) for i in range(len(cmarks))) / sum(freq)
rmu4 = sum(freq[i] * (cmarks[i] ** 4) for i in range(len(cmarks))) / sum(freq)

print("1st raw moment:", rmu1)
print("2nd raw moment:", rmu2)
print("3rd raw moment:", rmu3)
print("4th raw moment:", rmu4)

