# 3D Reach bubble for robot
import numpy as np
import matplotlib.pyplot as plt

# Initialize figure and label axes
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

pi = np.pi
dr = pi/180 # Degree to radian multiple

# Define important robot dimensions and axis limits for GP8
z0 = 0.327  # Fixed height from base to A1
link1 = 0.28
link2 = 0.3
link3 = 0.064

a1, a2, a3 = np.mgrid[0:2*pi:15j, -115*dr:113*dr:13j, -205*dr:55*dr:17j]

r = link1*np.sin(a2) + link2*np.sin(pi/2+a2+a3)
Rx = r*np.cos(a1)
Ry = r*np.sin(a1)
Rz = z0 + link1*np.cos(a2) + link2*np.cos(pi/2+a2+a3)

# Plot reach points
ax.plot_surface(Rx, Ry, Rz, color = 'Red', alpha = 0.2)
ax.scatter(Rx, Ry, Rz, c='r', marker='o', alpha = 0.2)
