# HORIZONTAL BAR CHART
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [15, 13, 18, 12, 15]

plt.barh(x, y)
plt.xlabel("x values")
plt.ylabel("y values")

plt.title("Horizontal Bar Graph")
plt.show()