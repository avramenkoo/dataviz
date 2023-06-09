# Побудувати поверхні 2-го порядку. a, b, c – константи
# Еліпсоїд

# Construct the surface of an ellipsoid using the equation:
# \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# a, b, c - константи
a = 2
b = 3
c = 1.5

# генеруємо theta і phi координати
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# вираховуємо координати x, y, z
x = a * np.sin(phi) * np.cos(theta)
y = b * np.sin(phi) * np.sin(theta)
z = c * np.cos(phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'Ellipsoid: $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$', fontsize=12)

# equal aspect ratio
ax.set_box_aspect([1, 1, 1])

plt.show()
