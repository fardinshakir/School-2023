import numpy as np
from visual_kinematics.RobotSerial import *
from visual_kinematics.RobotTrajectory import *

alpha = 90
d = 0

# Define joint angle values (set 3rd element to 0 when doing inverse kinematics)
S0 = [-97.494, 97.494, 0]
S1 = [-123, 60, 0]
E0 = [-174.987, 174.987, 0]
E1 = [-2.864, 150, 0]
W0 = [-175.25, 175.25, 0]
W1 = [-90, 120, 0]
W2 = [-175.25, 175.25, 0]
# List of theta values
theta = [-np.radians(S0[2])/2, -np.radians(S1[2])/2, -np.radians(E0[2])/2, -np.radians(E1[2])/2, -np.radians(W0[2])/2, -np.radians(W1[2])/2, -np.radians(W2[2])/2]

# Normalizing link lengths and creating DH parameters
norm = 1000
L1 = [d, 0, 0, theta[0]]
L2 = [d, 273.35/norm, -alpha, theta[1]]
L3 = [d, 69/norm, alpha, theta[2]]
L4 = [d, 364.35/norm, -alpha, theta[3]]
L5 = [d, 69/norm, alpha, theta[4]]
L6 = [d, 374.24/norm, alpha, theta[5]]
L7 = [d, 229.525/norm, alpha, theta[6]]
Links = [L1, L2, L3, L4, L5, L6, L7]
dh_params = np.array([L1, L2, L3, L4, L5, L6, L7])

# Creating robot object from DH parameters
robot = RobotSerial(dh_params)

# Forward Kinematics (Using given joint angles @ line 8)
def forward():
    f = robot.forward(theta)
    robot.end_frame

    print("end frame t_4_4:")
    print(f.t_4_4)

    print("End Frame Position:")
    pos = f.t_3_1.reshape([3, ])
    print(pos)

    print("End Frame Angles:")
    print(f.euler_3)
    robot.show()

# Inverse Kinematics (give xyz and angles abc in rad)
def inverse(x, y, z, a, b, c):
    xyz = np.array([[x], [y], [z]])
    abc = np.array([a, b, c])
    end = Frame.from_euler_3(abc, xyz)
    robot.inverse(end)
    print("Inverse is successful: {0}".format(robot.is_reachable_inverse))
    print("Axis values: \n{0}".format(robot.axis_values))
    robot.show()

# Animation from going from one point to another given 2 frames
def trajectory(x1, y1, z1, x2, y2, z2):
    frames = [Frame.from_euler_3(np.array([0.5 * pi, 0., pi]), np.array([[x1], [y1], [z1]])),
              Frame.from_euler_3(np.array([0.5 * pi, 0., pi]), np.array([[x1], [y2], [z2]]))]
    trajectory = RobotTrajectory(robot, frames)
    trajectory.show(motion="p2p")


# Call for functions
#forward()
inverse(0.22661347, 0.55200808, 0.56230939, -1.2433447, 0.21086608, -0.51215784)
#trajectory(0, 0, 0, 0.1, 0.5, 0.2)


# link frames
# dh params
# all transformations
# total transformations
# forward kin
# inverse kin (2-3 examples)
# workspace
