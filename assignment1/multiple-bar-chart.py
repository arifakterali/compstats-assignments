# MULTIPLE BAR CHART
import matplotlib.pyplot as plt
import numpy as np

labels = ['A','B','C','D','E']
x = np.arange(len(labels))
data1 = [6,12,17,5,10]
data2 = [11,10,8,13,14]

width = 0.3
plt.bar(x-width/2, data1, width, label="Data 1")
plt.bar(x+width/2, data2, width, label="Data 2")
plt.xticks(x, labels)
plt.legend()

plt.title("Multiple-Bar Chart")
plt.show()