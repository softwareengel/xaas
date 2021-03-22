from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0, 15)
y = np.exp(x/3.0)
f = interpolate.interp1d(x, y)
xnew = np.arange(0, 14, 0.1)
ynew = f(xnew)
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()