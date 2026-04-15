# PIE CHART
import matplotlib.pyplot as plt

shares = [20,31,45,23,11]
names = ['A','B','C','D','E']

plt.pie(shares, labels = names, autopct = "%1d%%")
plt.title("Pie Chart")
plt.show()