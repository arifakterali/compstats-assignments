# CENTRAL MOMENT FOR CONTINUOUS DATA
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)
cmarks = [(edges[i] + edges[i+1])/2 for i in range(len(freq))]
mean = sum(freq[i]*cmarks[i] for i in range(len(freq))) / sum(freq)

cmu1 = sum(freq[i] * (cmarks[i] - mean) for i in range(len(cmarks))) / sum(freq)
cmu2 = sum(freq[i] * ((cmarks[i] - mean) ** 2) for i in range(len(cmarks))) / sum(freq)
cmu3 = sum(freq[i] * ((cmarks[i] - mean) ** 3) for i in range(len(cmarks))) / sum(freq)
cmu4 = sum(freq[i] * ((cmarks[i] - mean) ** 4) for i in range(len(cmarks))) 


print("1st central moment:", cmu1)
print("2nd central moment:", cmu2)
print("3rd central moment:", cmu3)
print("4th central moment:", cmu4)
