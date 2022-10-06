import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2 * np.pi, 2 * np.pi, 200) 
f1 = np.sin(x)
f2 = np.cos(x)
f3 = np.tan(x)
f4 = 1 / f3
f5=1/f2
f6=1/f1
#plt.plot(x, f1, label=r'$y=sin(x)$')
#plt.plot(x, f2, label=r'$y=cos(x)$')
#plt.plot(x, f3, label=r'$y=tan(x)$')
#plt.plot(x, f4, label=r'$y=cot(x)$')
plt.plot(x, f5, label=r'$y=sec(x)$', )
#plt.plot(x, f6, label=r'$y=csc(x)$', )

#ax = plt.gca()
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
#ax.spines['bottom'].set_position(('data', 0))
#ax.spines['left'].set_position(('data', 0))

plt.xlim(x.min() * 1.1, x.max() * 1.1)  # limit x range
plt.ylim(-4, 4)  # limit y range
#plt.xticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           #[r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
#plt.legend(loc='best')
plt.show()
