#FREQUENCY, RELATIVE FREQUENCY, CUMULATIVE FREQUENCY FOR CONTINUOUS DATA
import numpy as np

data = [12,15,17,19,21,23,25,27,29]
bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)

rel_freq = [f/sum(freq) for f in freq]

cf_lesser = []
s = 0
for f in freq:
    s += f
    cf_lesser.append(s)

cf_greater = []
s = sum(freq)
for f in freq:
    cf_greater.append(s)
    s -= f

print(f"{"Interval":<12}{"Freq":<8}{"Rel Freq":<12}{"CF lesser-than":<18}{"CF greater-than":<18}")
for i in range(len(freq)):
    interval = f"{edges[i]} - {edges[i+1]}"
    print(f"{interval:<12}{freq[i]:<8}{rel_freq[i]:<12.3f}{cf_lesser[i]:<18}{cf_greater[i]:<18}")

