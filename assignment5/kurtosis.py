# MEASURE OF KURTOSIS
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)
cmarks = [(edges[i] + edges[i+1])/2 for i in range(len(freq))]
mean = sum(freq[i]*cmarks[i] for i in range(len(freq))) / sum(freq)

cmu1 = sum(freq[i] * (cmarks[i] - mean) for i in range(len(cmarks))) / sum(freq)
cmu2 = sum(freq[i] * ((cmarks[i] - mean) ** 2) for i in range(len(cmarks))) / sum(freq)
cmu3 = sum(freq[i] * ((cmarks[i] - mean) ** 3) for i in range(len(cmarks))) / sum(freq)
cmu4 = sum(freq[i] * ((cmarks[i] - mean) ** 4) for i in range(len(cmarks))) / sum(freq)

beta2 = cmu4 / cmu2**2
gamma2 = beta2 - 3

print("Pearson's Kurtosis:", beta2)
print("Excess Kurtosis:", gamma2)

if gamma2 > 0:
    print("Leptokurtic - Sharp Peaked Graph")
elif gamma2 < 0:
    print("Platykuritc = Flat-topped Graph")
else:
    print("Normal Distribution - no kurtosis")
