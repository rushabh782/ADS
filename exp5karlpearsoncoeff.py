import numpy as np

data = [10,12,13,15,22,27,30,45,50,60]

#calculate mean
mean = np.mean(data)

#calculate median
median = np.median(data)

#Standard deviation
std_dev = np.std(data)

skewness = 3 * (mean - median) / std_dev

print("Karl Pearson coefficient of skewness:",skewness)