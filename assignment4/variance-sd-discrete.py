# VARIANCE, STANDARD DEVIATION FOR DISCRETE DATA
import numpy as np

data = [1,2,2,3,3,3,4,4,5]
mean = np.mean(data)

var = sum((data[i]-mean) ** 2 for i in range(len(data))) / len(data)
sd = var ** (1/2)

print("Variance:", var)
print("Standard Deviation:", sd)