import numpy as np
import matplotlib.pyplot as plt

def g(w):
    return np.sin(2*w)

w = np.arange(-10, 10, 1)
def g(w):
    #return np.sin(3*w) + 0.1*w**2
    return w**2

def dg(x):
    h = 0.0000000000001
    for n in range(len(x)):
        a = (g(x[n]+h) - g(x[n]))/h

        if a == 0:
            print(x[n])
    return (g(x+h) - g(x))/h


fig = plt.figure()
ax = plt.axes()
plt.plot(w, g(w), 'r')
plt.plot(w, dg(w), 'b')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
plt.show()
