# VERTICAL BAR CHART
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [15, 13, 18, 12, 15]

plt.bar(x, y)
plt.xlabel("x values")
plt.ylabel("y values")

plt.title("Bar Graph")
plt.show()