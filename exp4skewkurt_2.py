import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

x = np.array([1,2,3,4,5,6,7,8,9,10])

#calculate mean and SD
mean = statistics.mean(x)
# Use NumPy's std function instead of statistics.stdev
sd = np.std(x) # Use NumPy's std function for NumPy arrays

plt.plot(x,norm.pdf(x,mean,sd)) # Also, 'xplth' was likely a typo and should be 'x'
plt.show()