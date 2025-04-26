import numpy as np

data = [10,12,9,13,16,30,45,50,60]

data.sort()

#quarrtile 1
Q1 = np.percentile(data,25)

#quartile 2
Q2 = np.percentile(data,50)

#quartile 3
Q3 = np.percentile(data,75)

bowley_skewness = (Q3 + Q1 - 2*Q2) / (Q3-Q1)

print("Bowley's coefficient of skewness:",bowley_skewness)
