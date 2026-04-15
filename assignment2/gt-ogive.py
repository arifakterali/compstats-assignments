# GREATER-THAN TYPE OGIVE FOR CONTINUOUS DATA
import matplotlib.pyplot as plt
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]
freq, edges = np.histogram(data, bins)

cf_greaterthan = []
s = sum(freq)
for f in freq:
    cf_greaterthan.append(s)
    s -= f

#x = [f"greater than {edges[i+1]}" for i in range(len(edges)-1)]

plt.plot(edges[1::], cf_greaterthan, marker="o")
plt.xlabel("x values")
plt.ylabel("greater-than cumulative frequency")
plt.title("Greater-than Type Ogive")
plt.show()