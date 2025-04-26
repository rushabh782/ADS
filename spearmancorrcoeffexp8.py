import numpy as np

def spearman_corr(x, y):
    x_rank = np.argsort(np.argsort(x))
    y_rank = np.argsort(np.argsort(y))


    n = len(x)
    rho = 1 - 6 * np.sum((x_rank - y_rank)**2) / (n * (n**2 - 1))

    return rho

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Calculate Spearman's correlation
rho = spearman_corr(x, y)
print("Spearman's Correlation coefficient:", rho)
