# BAND CHART
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y_lower = [8, 11, 15, 10, 13]
y_upper = [15, 13, 18, 12, 15]

plt.plot(x, y_upper)
plt.plot(x, y_lower)
plt.fill_between(x, y_lower, y_upper, alpha=0.5)

plt.title("Band Chart")
plt.show()