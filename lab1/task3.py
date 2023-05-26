# 3. Побудувати графіки у полярних координатах
# декартів лист

# Plot graphs in polar coordinates using the Cartesian letter representation
# Latex formula:
# \rho = \frac{3 * a * \cos \phi \sin \phi}{\cos^3 \phi + \sin^3 \phi}

import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 2*np.pi, 100)
a = 1

# по формулі вичисляємо значення ро
r = (3 * a * np.cos(phi) * np.sin(phi)) / (np.cos(phi)**3 + np.sin(phi)**3)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

ax.plot(phi, r, color='red')

ax.set_ylim(0, np.max(r))
ax.set_aspect('equal')
ax.set_title(r'$\rho = \frac{3 \cdot a \cdot \cos \phi \cdot \sin \phi}{\cos^3 \phi + \sin^3 \phi}$', fontsize=12)

plt.show()
