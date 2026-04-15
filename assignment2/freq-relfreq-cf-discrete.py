# FREQUENCY, RELATIVE FREQUENCY, CUMULATIVE FREQUENCY FOR DISCRETE DATA + COLUMN DIAGRAM
from collections import Counter
import matplotlib.pyplot as plt

data = [1,2,2,3,3,3,4,4,5]
freq = Counter(data)

values = sorted(freq.keys())
frequencies = [freq[v] for v in values]
rel_frequencies = [f/sum(frequencies) for f in frequencies]

cum_freq_lesser = []
s = 0
for f in frequencies:
    s += f
    cum_freq_lesser.append(s)

cum_freq_greater = []
s = sum(frequencies)
for f in frequencies:
    cum_freq_greater.append(s)
    s -= f

print(f"{'values':<8}{'freq':<8}{'rel freq':<12}{'cf lesser-than':<18}{'cf greater-than':<18}")
for i in range(len(values)):
    print(f"{values[i]:<8}{frequencies[i]:<8}{rel_frequencies[i]:<12.3f}{cum_freq_lesser[i]:<18}{cum_freq_greater[i]:<18}")

plt.bar(values, freq)
plt.xlabel("values")
plt.ylabel("frequencies")
plt.title("Column Diagram")
plt.show()
