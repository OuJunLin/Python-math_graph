import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3.5, 3.5, 0.1) #從-5到5，間隔是1，不含結束點5，
#且間隔可以實數
#print(x)
y = 0
y = y + 4*x
y = y - 3*x**2
#print(y)
plt.plot(x,y)
plt.axhline(y=0)#x軸
plt.axvline(x=0)#y軸
plt.show()
print("Done")