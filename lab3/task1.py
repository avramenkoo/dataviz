# 1. Візуалізацію скалярного поля.
# Знайдіть його градієнт та візуалізуйте його як плоске векторне поле;

import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return 4 * np.log(x**2 + y**2) - 8 * x * y

min = -5
max = 3
n = 256

x = np.linspace(min, max, n)
y = np.linspace(min, max, n)
X, Y = np.meshgrid(x, y)

plt.pcolormesh(X, Y, u(X, Y))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Візуалізацію скалярного поля  $4\\ln(x^2 + y^2) - 8xy$')

xx, yy = np.meshgrid(np.linspace(min, max, 15), np.linspace(min, max, 15))
u_val = u(xx, yy)
u_dx, u_dy = np.gradient(u_val)

plt.quiver(xx, yy, u_dx, u_dy)
plt.title('Векторне поле ' + r'$u(x,y)=4\ln(x^2 + y^2) - 8xy$')

fig, ax = plt.subplots()
ax.streamplot(xx, yy, u_dx, u_dy, color=u_val, cmap='viridis')
plt.title('Градієнт ' + r'$4\ln(x^2 + y^2) - 8xy$')

plt.show()
