import numpy as np
from visual_kinematics.RobotSerial import *
from visual_kinematics.RobotTrajectory import *
import matplotlib.pyplot as plt
import random
import matplotlib as mpl
import time

mpl.use("agg")
alpha = 90
d = 0
plt.rcParams.update({'figure.max_open_warning': 16000})

trials = 16000
S0 = np.linspace(-97, 97, trials)
S1 = np.linspace(-123, 60, trials)
E0 = np.linspace(-175, 175, trials)
E1 = np.linspace(-3, 150, trials)
W0 = np.linspace(-175, 175, trials)
W1 = np.linspace(-90, 120, trials)
W2 = np.linspace(-175, 175, trials)
random.shuffle(S0)
random.shuffle(S1)
random.shuffle(E0)
random.shuffle(E1)
random.shuffle(W0)
random.shuffle(W1)
random.shuffle(W2)

theta = []
for n in range(len(S0)):
    q = [-np.radians(S0[n])/2, -np.radians(S1[n])/2, -np.radians(E0[n])/2, -np.radians(E1[n])/2, -np.radians(W0[n])/2, -np.radians(W1[n])/2, -np.radians(W2[n])/2]
    theta.append(q)

def Workspace():
    xpos = []
    ypos = []
    zpos = []
    for n in range(len(theta)):
        norm = 1000
        L1 = [d, 0, 0, theta[n][0]]
        L2 = [d, 273.35/norm, alpha, theta[n][1]]
        L3 = [d, 69/norm, alpha, theta[n][2]]
        L4 = [d, 364.35/norm, alpha, theta[n][3]]
        L5 = [d, 69/norm, alpha, theta[n][4]]
        L6 = [d, 374.24/norm, alpha, theta[n][5]]
        L7 = [d, 229.525/norm, 0, theta[n][6]]
        Links = [L1, L2, L3, L4, L5, L6, L7]
        dh_params = np.array([L1, L2, L3, L4, L5, L6, L7])
        robot = RobotSerial(dh_params)
        f = robot.forward(theta[n])
        robot.end_frame
        positions = f.t_3_1.reshape([3, ])
        xpos.append(positions[0])
        ypos.append(positions[1])
        zpos.append(positions[2])
    return xpos, ypos, zpos

def closePlots():
    plt.clf()
    plt.cla()
    plt.close("all")
    time.sleep(0.5)
x, y, z = forward()
#print(f"{x}\n{y}\n{z}")

plt.close("all")
fig = plt.figure(figsize = (12, 12))

ax = fig.add_subplot(projection='3d')

ax.scatter3D(x, y, z, 'bo')
plt.savefig('default.png')
ax.view_init(elev=90, azim=-90, roll=0)
plt.savefig('XY.png')
ax.view_init(elev=0, azim=-90, roll=0)
plt.savefig('ZX.png')
ax.view_init(elev=0, azim=0, roll=0)
plt.savefig('ZY.png')
closePlots()
