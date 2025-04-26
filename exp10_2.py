#Histogram

import matplotlib.pyplot as plt

data = [1,7,3,5,8,3,4,2,1]
plt.hist(data,bins=6)
plt.title("Histogram")
plt.show()