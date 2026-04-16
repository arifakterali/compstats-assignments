# MEAN DEVIATION FOR DISCRETE DATA
import numpy as np

data = np.array([1,2,2,3,3,3,4,4,5])

am = np.mean(data)
A = 2

md_A = np.mean(np.abs(data - A))
md_mean = np.mean(np.abs(data - am))

print("mean deviation about", A, "is:", md_A)
print("mean deviation about mean:", md_mean)