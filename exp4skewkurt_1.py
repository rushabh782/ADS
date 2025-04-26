import numpy as np
from scipy.stats import skew,kurtosis

data=[2,4,6,8,9,7,4,7,3]

skewness= skew(data)
print("Skewness:",skewness)

kurt = kurtosis(data)
print("Kurtosis:",kurt)