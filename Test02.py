import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3.5, 3.5, 0.1)
y = 0
n = int(input("Please enter the highest power: "))
print("---"*10)

for i in range(0, n+1):
    a = int(input("Please enter the coefficient of this power({}): " .format(i)))
    y = y + a*x**i

plt.plot(x,y)
plt.axhline(y=0)#x軸
plt.axvline(x=0)#y軸
plt.show()
print("Done")