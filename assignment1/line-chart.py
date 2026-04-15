# LINE CHART
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 23, 9, 16]

plt.plot(x, y, marker='o')
plt.xlabel("X")
plt.ylabel("Y")

plt.title("Line Chart")
plt.show()