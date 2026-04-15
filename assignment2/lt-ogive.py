# LESS-THAN TYPE OGIVE FOR CONTINUOUS DATA
import matplotlib.pyplot as plt
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]
freq, edges = np.histogram(data, bins)

cf_lessthan = []
s = 0
for f in freq:
    s += f
    cf_lessthan.append(s)
# x = [f"less than {edges[i+1]}" for i in range(len(edges)-1)]

plt.plot(edges[1::], cf_lessthan, marker="o")
plt.xlabel("x values")
plt.ylabel("less-than cumulative frequency")
plt.title("Less-than Type Ogive")
plt.show()