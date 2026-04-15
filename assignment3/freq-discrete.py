# FREQUENCY FOR DISCRETE DATA
from collections import Counter

data = [1,2,2,3,3,3,4,4,5]
freq_dict = Counter(data)

values = sorted(freq_dict.keys())
frequencies = [freq_dict[v] for v in values]

print(f"{"Values":<8}{"Freq":<8}")
for i in range(len(values)):
    print(f"{values[i]:<8}{frequencies[i]:<8}")