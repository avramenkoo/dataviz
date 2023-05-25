# Побудувати графіки у полярних координатах
# декартов лист

# Plot graphs in polar coordinates using the Cartesian letter representation
# Latex formula:
# \rho = \frac{3 * a * \cos \phi \sin \phi}{\cos^3 \phi + \sin^3 \phi}

import numpy as np
import matplotlib.pyplot as plt

# Define the phi values
phi = np.linspace(0, 2*np.pi, 100)

# Define the parameter 'a'
a = 1

# Calculate the r values based on the formula
r = (3 * a * np.cos(phi) * np.sin(phi)) / (np.cos(phi)**3 + np.sin(phi)**3)

# Create a polar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Plot the graph
ax.plot(phi, r, color='red')

# Set the plot limits and aspect ratio
ax.set_ylim(0, np.max(r))
ax.set_aspect('equal')

# Set the title
ax.set_title(r'$\rho = \frac{3 \cdot a \cdot \cos \phi \cdot \sin \phi}{\cos^3 \phi + \sin^3 \phi}$', fontsize=12)

# Show the plot
plt.show()
