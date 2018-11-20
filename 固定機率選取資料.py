import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
prob = [0.1, 0.2, 0.3,
     0.1, 0.2, 0.1]

dice = list(range(1, 7))
samples = np.random.choice(dice, size=100000, p=prob)
tmp = Counter(samples)
print(tmp)
print(tmp.__class__)
X = sorted(tmp.keys())
Y = [tmp[x] for x in X]

plt.bar(X, Y)
plt.show()