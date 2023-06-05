# 3. Побудуйте тривимірну візуалізацію векторного поля; За додатковий
# бал (не обов’язково) модернізуйте алгоритм побудови ліній току на
# випадок 3-вимірного поля.

import matplotlib.pyplot as plt
import numpy as np

x, y, z = np.meshgrid(np.arange(-5, 3, 0.6), np.arange(-5, 3, 0.6), np.arange(-5, 3, 2.4))

Fx = y / z + 2 * x
Fy = x / z
Fz = x * y / z**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(x, y, z, Fx, Fy, Fz, length=0.5, normalize=True, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'$F = (\frac{y}{z} + 2x; \frac{x}{z}; \frac{xy}{z^2})$')

plt.show()
