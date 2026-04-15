# PICTOGRAM
import matplotlib.pyplot as plt

labels = ['A','B','C','D','E']
data = [12, 10, 7, 5, 8]

plt.scatter(labels , data, marker="*")
plt.title('Scatter Plot')
plt.show()