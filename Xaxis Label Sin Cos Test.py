import matplotlib.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 2, 5, 3])
ax.set_xticks([1,2,3,4])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr'])
plt.show()