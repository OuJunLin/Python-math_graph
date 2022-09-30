import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
y = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7])
y0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
x0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot(x, y0, color="lightgray")
plt.plot(x0, y, color="lightgray")
plt.plot(x, y)
plt.show()
