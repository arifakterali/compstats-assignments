# CUMULATIVE FREQUENCY DIAGRAM FOR DISCRETE DATA
import matplotlib.pyplot as plt
from collections import Counter

data = [1,2,2,3,3,3,4,4,5]
freq_dict = Counter(data)

values = sorted(freq_dict.keys())
frequencies = [freq_dict[v] for v in values]

cf_lesser = []
s = 0
for f in frequencies:
    s += f
    cf_lesser.append(s)

cf_greater = []
s = sum(frequencies)
for f in frequencies:
    cf_greater.append(s)
    s -= f

plt.plot(values, cf_lesser, marker="o", label="lesser-than cf")
plt.plot(values, cf_greater, marker="o", label="greater-than cf")
plt.legend()
plt.title("Cumulative Frequency Diagram")
plt.show()