# LOGARITHMIC LINE CHART
import matplotlib.pyplot as plt

x = [7,45,101,450,1254]
y = [2345, 999, 234, 20, 2]

plt.loglog(x,y, marker='o')
plt.xlabel("x values scaled to log")
plt.ylabel("y values scaled to log")

plt.title("Logarithmic Chart")
plt.show()