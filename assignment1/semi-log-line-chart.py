# SEMI-LOGARITHMIC LINE CHART
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,34,99,250,889]

plt.semilogy(x, y)
plt.xlabel("x values")
plt.ylabel("y values scaled to log")

plt.title("Semi-logarithmic Chart")
plt.show()