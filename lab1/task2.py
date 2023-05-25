# 2. Побудувати поверхні
# Plot a surface
# z = x^2 \sin(x) - 2y^3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def surface_func(x, y):
    return x**2 * np.sin(x) - 2 * y**3

# Generate the x and y coordinates
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Compute the corresponding z values based on the formula
Z = surface_func(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'$z = x^2 \sin(x) - 2y^3$', fontsize=12)

# Show the plot
plt.show()
