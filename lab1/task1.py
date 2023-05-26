# Побудувати графіки функцій

import math
import numpy as np
import matplotlib.pyplot as plt


def y_f(x):
    return np.cos(x - 1) * math.e ** (6 * x)


def z_f(x):
    y = np.zeros_like(x)
    for idx, val in enumerate(x):
        if val <= 0:
            y[idx] = (1 + val ** 2) / ((1 + val ** 4) ** (-1 / 2))
        else:
            y[idx] = 2 * val + (np.sin(val) ** 2 / 2 + val)
    return y


x = np.arange(0, 2, 0.01)
y = y_f(x)
z = z_f(x)

fig1, ay = plt.subplots()
ay.plot(x, y)
ay.grid(True, linestyle='-.')
ay.set_xlabel('X')
ay.set_ylabel('Y')
ay.set_title(r'$\cos(x - 1) e^{6x}$', fontsize=12)
ay.tick_params(labelcolor='r', labelsize='medium', width=3)

fig2, az = plt.subplots()
az.plot(x, z)
az.grid(True, linestyle='-.')
az.set_xlabel('X')
az.set_ylabel('Y')
az.set_title(r'$\frac{1 + x^2}{\sqrt{1 + x^4}}, x \leq 0, \qquad 2x + \frac{\sin^2(x)}{2 + x}, x > 0$', fontsize=12)
az.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()

data = np.column_stack((x, y))
np.savetxt('./lab1/task1_1-data1.txt', data, delimiter='\t', header='X\tY')

data = np.column_stack((x, z))
np.savetxt('./lab1/task1_1-data2.txt', data, delimiter='\t', header='X\tZ')
