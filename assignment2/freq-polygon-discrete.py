# FREQUENCY POLYGON FOR DISCRETE DATA
from collections import Counter
import matplotlib.pyplot as plt

data = [1,2,2,3,3,3,4,4,5]
freq = Counter(data)

values = sorted(freq.keys())
frequencies = [freq[v] for v in values]

plt.plot(values, frequencies, marker="o")
plt.xlabel("Values")
plt.ylabel("Frequencies")
plt.title("Frequency Polygon")
plt.show()