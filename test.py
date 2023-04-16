import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

n = 10
hilbert = np.zeros((10, 10))

for i in range(10):
    for j in range(10):
        hilbert[i][j] = 1/(i+1 + j+1 - 1)
hilbert = np.round(hilbert, 2)
print(hilbert)
sns.heatmap(hilbert)
plt.show()
