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
plt.rcParams.update({'figure.max_open_warning': 4000})

trials = 100
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

def forward():
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

def inverse(x, y, z):
    xyz = np.array([[x], [y], [z]])
    abc = np.array([0.5 * pi, 0., pi])
    end = Frame.from_euler_3(abc, xyz)
    robot.inverse(end)
    print("inverse is successful: {0}".format(robot.is_reachable_inverse))
    print("axis values: \n{0}".format(robot.axis_values))
    robot.show()

def trajectory(x1, y1, z1, x2, y2, z2):
    frames = [Frame.from_euler_3(np.array([0.5 * pi, 0., pi]), np.array([[x1], [y1], [z1]])),
              Frame.from_euler_3(np.array([0.5 * pi, 0., pi]), np.array([[x1], [y2], [z2]]))]
    #          Frame.from_euler_3(np.array([0, 0., pi]), np.array([[0.0], [0.], [0.0]]))]
    trajectory = RobotTrajectory(robot, frames)
    trajectory.show(motion="p2p")

def closePlots():
    plt.clf()
    plt.cla()
    plt.close("all")
    time.sleep(0.5)
x, y, z = forward()
#print(f"{x}\n{y}\n{z}")
#inverse(0.2, 0.3, 0.1)
#trajectory(0, 0, 0, 0.1, 0.5, 0.2)

def distance_list(xpos, ypos, zpos):
    tuple = [] # for 3 position vectors
    distance_list = [] # store distance values
    for x in xpos:
        for y in ypos:
            for z in zpos:
                tuple.append(x, y, z) # position vector
                distance = np.sqrt(x**2 + y**2 + z**2) # position distance from origin
                distance_list.append(distance) # add distance value
    print(distance_list)
    #dict = dict(tuple: distance_list) # link distance values with their corresponding 3 positions vectors
    return dict

def compare_dist(dict):
    np.sort(distance_list)
    top100distance = dict[-100:]
    return top100distance

distance_list(x, y, z)
