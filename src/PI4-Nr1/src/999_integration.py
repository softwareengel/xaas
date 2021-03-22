import matplotlib.pyplot as plt
x = np.linspace(-2, 2, num=30)
y = x
y_int = integrate.cumtrapz(y, x, initial=0)
plt.plot(x, y_int, 'ro', x, y[0] + 0.5 * x**2, 'b-')
plt.show()