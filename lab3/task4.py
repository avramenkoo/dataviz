# 4. Побудуйте візуалізацію тензорного поля за допомогою еліпсоїдів,
# кубоїдів, циліндрів та будь-якого суперквадру.

import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab
import glyph_visualization_lib as gvl

start = 1
stop = 10
num = 6
x = np.linspace(start, stop, num, dtype=float, endpoint=True)
y = np.linspace(start, stop, num, dtype=float, endpoint=True)
z = np.linspace(start, stop, num, dtype=float, endpoint=True)
X, Y, Z = np.meshgrid(x, y, z)

stress_tensor = np.array([
    [X, np.log(X * Y), -np.log(X * Z)],
    [np.sin(X + Y), -Y, np.sin(Y + Z)],
    [-np.log(X * Z), np.sin(Y + Z), Z]
])

vm_stress = gvl.get_von_Mises_stress(stress_tensor)
glyph_radius = 0.25
limits = [np.min(vm_stress), np.max(vm_stress)]
colormap = plt.get_cmap('rainbow', 120)
fig = mlab.figure(bgcolor=(1, 1, 1))
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')

for i in range(x.size):
    for j in range(y.size):
        for k in range(z.size):
            center = [x[i], y[j], z[k]]
            data = stress_tensor[:, :, i, j, k]
            color = colormap(gvl.get_colormap_ratio_on_stress(vm_stress[i, j, k], limits))[:3]

            """
            glyph_type = {0: 'cuboid', 1: 'cylinder', 2: 'ellipsoid', 3: 'superquadric'}
            for glyph_type == 3 (superquadric), there are additional glyph shape types:
                0 - superquadrics,
                1 - Kindlmann_glyph,
                2 - Kindlmann_modified_glyph
            """
            x_g, y_g, z_g = gvl.get_glyph_data(center, data, limits,
                                               glyph_points=12,
                                               glyph_radius=glyph_radius,
                                               glyph_type=3,
                                               superquadrics_option=1)

            mlab.mesh(x_g, y_g, z_g, color=color)

mlab.show()
