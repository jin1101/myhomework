import numpy.random as nr
import numpy as np
import matplotlib.pyplot as plt
results = [np.mean(nr.binomial(1, 0.25, 30)) for _ in range(100)]
sample_mean = np.mean(results)
plt.hist(results)
plt.vlines(0.25, 0.0, 28.0, color = 'red')
plt.vlines(sample_mean, 0.0, 28.0, color = 'black')
plt.xlabel('Results')
plt.ylabel('Frequency')
plt.title('Histogram of results')
plt.show()