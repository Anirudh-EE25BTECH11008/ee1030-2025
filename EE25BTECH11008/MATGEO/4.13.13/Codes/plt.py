import numpy as np
import matplotlib.pyplot as plt

# Range for plotting
x = np.linspace(-10, 10, 400)

# Plot the pair of lines: x = 0 and y = 0
plt.plot([0, 0], [-10, 10], 'b', linewidth=2)   # x = 0
plt.plot([-10, 10], [0, 0], 'b', linewidth=2)   # y = 0

# Plot the bisectors: y = x and y = -x
plt.plot(x, x, 'r--', linewidth=1.5)
plt.plot(x, -x, 'g--', linewidth=1.5)

# Labels placed on the plot
plt.text(0.5, 9, 'y = 0', color='b', fontsize=10)
plt.text(8.5, 0.3, 'x = 0', color='b', fontsize=10)
plt.text(6, 6, 'y = x', color='r', fontsize=10)
plt.text(6, -6, 'y = -x', color='g', fontsize=10)

# Axes setup
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Pair of Lines: xy = 0 and Their Bisectors')
plt.axis('equal')
plt.grid(True, linestyle=':')
plt.show()
