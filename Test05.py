import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 200) 
f1 = np.sin(x)
f6=1/f1
plt.plot(x, f6, label='$y=sec(x)$')
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(-4, 4)
plt.show()