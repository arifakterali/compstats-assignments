# RAW MOMENTS FOR DISCRETE DATA
import numpy as np

data = [1,2,2,3,3,3,4,4,5]

rmu1 = sum(data[i] for i in range(len(data))) / len(data)
rmu2 = sum(data[i]**2 for i in range(len(data))) / len(data)
rmu3 = sum(data[i]**3 for i in range(len(data))) / len(data)
rmu4 = sum(data[i]**4 for i in range(len(data))) / len(data)

print("1st raw moment:", rmu1)
print("2nd raw moment:", rmu2)
print("3rd raw moment:", rmu3)
print("4th raw moment:", rmu4)
