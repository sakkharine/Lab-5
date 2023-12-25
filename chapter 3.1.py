import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

z1 = x**0.25 + y**0.25
z2 = x**2 - y**2
z3 = 2*x + 3*y
z4 = x**2 + y**2
z5 = 2 + 2*x + 2*y - x**2 - y**2

fig = plt.figure(figsize=(15, 15))

ax1 = fig.add_subplot(321, projection='3d')
ax1.plot_surface(x, y, z1, cmap='viridis')
ax1.set_title('z = x^0.25 + y^0.25')

ax2 = fig.add_subplot(322, projection='3d')
ax2.plot_surface(x, y, z2, cmap='viridis')
ax2.set_title('z = x^2 - y^2')

ax3 = fig.add_subplot(323, projection='3d')
ax3.plot_surface(x, y, z3, cmap='viridis')
ax3.set_title('z = 2x + 3y')

ax4 = fig.add_subplot(324, projection='3d')
ax4.plot_surface(x, y, z4, cmap='viridis')
ax4.set_title('z = x^2 + y^2')

ax5 = fig.add_subplot(325, projection='3d')
ax5.plot_surface(x, y, z5, cmap='viridis')
ax5.set_title('z = 2 + 2x + 2y - x^2 - y^2')

plt.show()
