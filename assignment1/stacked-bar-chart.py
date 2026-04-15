# COMPOSITE (STACKED) BAR CHART
import matplotlib.pyplot as plt
import numpy as np

labels = ['A','B','C','D','E']
x = np.arange(len(labels))
part1 = [6,12,17,5,10]
part2 = [11,10,8,13,14]

plt.bar(x, part1, label="Part 1")
plt.bar(x, part2, bottom = part1, label="Part 2")
plt.xticks(x, labels)
plt.legend()

plt.title("Stacked-Bar Chart")
plt.show()
