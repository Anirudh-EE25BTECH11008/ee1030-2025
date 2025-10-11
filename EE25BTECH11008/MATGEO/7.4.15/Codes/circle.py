# circle_plot.py
import ctypes
import math
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (compiled above)
lib = ctypes.CDLL("./circle.so")

# argtypes: a1,b1,c1,a2,b2,c2,area then pointers ux,uy,f,cc,r
lib.calc_circle.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

a1,b1,c1 = (2.0, -3.0, -5.0)
a2,b2,c2 = (3.0, -4.0, -7.0)

area = 154.0

# Prepare outputs
ux = ctypes.c_double()
uy = ctypes.c_double()
f_val = ctypes.c_double()
cc = ctypes.c_double()
r = ctypes.c_double()

# Call the C function
lib.calc_circle(a1, b1, c1, a2, b2, c2, area,
                ctypes.byref(ux), ctypes.byref(uy),
                ctypes.byref(f_val), ctypes.byref(cc), ctypes.byref(r))

u_vec = (ux.value, uy.value)
radius = r.value
circle_const = cc.value

# Centre (h,k) = -u
h, k = -u_vec[0], -u_vec[1]

# Print values
print("\nComputed circle parameters:")
print(f"u (vector) = ({u_vec[0]:.2f}, {u_vec[1]:.2f})")
print(f"f (scalar) = {f_val.value:.2f}")
print(f"circle constant (c) = {circle_const:.2f}")
print(f"r (radius) = {radius:.2f}")
print(f"centre = ({h:.2f}, {k:.2f})\n")

# Plotting extents
pad = 1.6
x_min = h - radius * pad
x_max = h + radius * pad
x_line = np.linspace(x_min, x_max, 800)

# Circle
theta = np.linspace(0, 2*math.pi, 400)
xc = h + radius * np.cos(theta)
yc = k + radius * np.sin(theta)
plt.plot(xc, yc, linewidth=2)          

# Centre
plt.scatter([h], [k], s=40)
plt.text(h + 0.03*radius, k + 0.03*radius, f"C({h:.2f},{k:.2f})", fontsize=9)

# Helper to plot a line ax + by + c = 0
def plot_line(a, b, c, x_vals, diff, label_text, style='--'):
    if abs(b) > 1e-12:
        y_vals = - (a * x_vals + c) / b
        plt.plot(x_vals, y_vals, style)
        x_text = h + 0.6 * radius
        y_text = - (a * x_text + c) / b
        plt.text(x_text, y_text+diff, label_text, fontsize=9)
        diff = 5
    else:
        x_vert = -c / a
        y_vals = np.linspace(k - radius*pad, k + radius*pad, 400)
        plt.plot([x_vert]*len(y_vals), y_vals, style)
        plt.text(x_vert + 0.02*radius, k, label_text, fontsize=9)

# Plot the two diameter lines
plot_line(a1, b1, c1, x_line, 0.5, f"{a1}x + {b1}y + {c1} = 0")
plot_line(a2, b2, c2, x_line, 1, f"{a2}x + {b2}y + {c2} = 0")

# Format plot
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle=':')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Circle from diameters and area")
plt.show()
