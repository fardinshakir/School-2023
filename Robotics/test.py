import numpy as np

alpha = 90
d = 0

S0 = 0
theta = [np.radians(0), np.radians(0), np.radians(0), np.radians(0), np.radians(0), np.radians(0), np.radians(0)]

norm = 1000
L1 = [0, 0, d, theta[0]]
L2 = [-alpha, 273.35/1000, d, theta[1]]
L3 = [alpha, 69/1000, d, theta[2]]
L4 = [-alpha, 364.35/1000, d, theta[3]]
L5 = [alpha, 69/1000, d, theta[4]]
L6 = [alpha, 374.24/1000, d, theta[5]]
L7 = [alpha, 229.525/1000, d, theta[6]]
Links = [L1, L2, L3, L4, L5, L6, L7]


def transform(Links):
    Transforms = []
    for n in range(len(Links)):
        T = np.array([
        [np.cos(Links[n][3]), -np.sin(Links[n][3]), 0, Links[n-1][1]],
        [np.sin(Links[n][3])*np.cos(Links[n-1][0]), np.cos(Links[n][3])*np.cos(Links[n-1][0]), -np.sin(Links[n-1][0]), -np.sin(Links[n-1][1])*Links[n][2]],
        [np.sin(Links[n][3])*np.sin(Links[n-1][0]), np.cos(Links[n][3])*np.sin(Links[n-1][0]), np.cos(Links[n-1][0]), np.cos(Links[n-1][1])*Links[n][2]],
        [0, 0, 0, 1]
        ])
        Transforms.append(T)
    return Transforms
T = transform(Links)

for n in range(len(T)):
    print(f"Transform of Link {n}\n{T[n]}\n")

z =((((T[0]*T[1])*T[2])*T[3])*T[4]*T[5]*T[6])
print(z)
