# VARIANCE, STANDARD DEVIATION FOR CONTINOUOS DATA
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)
cmarks = [(edges[i]+edges[i+1])/2 for i in range(len(freq))]
mean = sum(freq[i]*cmarks[i] for i in range(len(cmarks))) / sum(freq)

var = sum(freq[i] * np.abs(cmarks[i]-mean) for i in range(len(cmarks))) / sum(freq)
sd = var ** (1/2)

print("Variance:", var)
print("Standard Deviation:", sd)