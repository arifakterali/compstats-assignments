# CENTRAL MOMENT FOR DISCRETE DATA
import numpy as np

data = np.array([1,2,2,3,3,3,4,4,5])
mean = np.mean(data)

cmu1 = sum((data[i] - mean) for i in range(len(data))) / len(data)
cmu2 = sum((data[i] - mean) ** 2 for i in range(len(data))) / len(data)
cmu3 = sum((data[i] - mean) ** 3 for i in range(len(data))) / len(data)
cmu4 = sum((data[i] - mean) ** 4 for i in range(len(data))) / len(data)

print("1st central moment:", cmu1)
print("2nd central moment:", cmu2)
print("3rd central moment:", cmu3)
print("4th central moment:", cmu4)
