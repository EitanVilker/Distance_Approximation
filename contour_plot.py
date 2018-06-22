import matplotlib.pyplot as plt




import numpy as np
from math import pi
from time_cost import *

# keeping start and end position constant
xs = 0
ys = 0
xg = -1
yg = 1

# list of angle values
theta_s = np.arange(-180, 180, 1)
theta_g = np.arange(-180, 180, 1)

z = []
# creating list of time cost values
for angle_s in theta_s:
    for angle_g in theta_g:
        z.append(get_time_cost(xs,ys,xg,yg, angle_s, angle_g))

# reshaping timecost to be able to use a contour plot
z = np.array(z)
z = z.reshape(len(theta_s), len(theta_g))

# reshaping independent variables
x1, y1 = np.meshgrid(theta_s, theta_g)

# plotting the contour plot
plt.contour(x1, y1, z)
plt.show()