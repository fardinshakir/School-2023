import autograd.numpy as np
import matplotlib.pyplot as plt
from autograd import grad

noise = 0.1
x = np.linspace(0, 1, 50).reshape(-1, 1)
y = []
w = np.array([1.0, 0.0])

for n in range(len(x)):
    what = x[n] + np.random.uniform(-noise, noise)
    y.append(what[0])

def f(x):
    return w[0]*x + w[1]

def model(x, w):
    error = []
    for n in range(len(x)):
        xi = np.append(1, x[n])
        a = np.dot(xi, w)
        error.append(a)
    return error


def least(w):
    least = 0
    for n in range(len(x)):
        a = (model(x, w)[n] - y[n])**2
        least += a
    return least/len(y)



def gradient(x, w):
    grad = []
    a = model(x, w)

    for n in range(len(x)):
        xdot = np.append(1, x[n])

        z = np.dot(xdot, a[n]-y[n])
        grad.append(z)

    return np.sum(grad) * (2/len(y))

def descent(g, alpha, steps, w):
    gradient = grad(least)
    for k in range(1, steps+1):
        if alpha == 'diminishing':
            alpha_n = 1/k
        else:
            alpha_n = alpha

    weight = [w]
    cost = [g(w)]
    for k in range(steps):
        check = gradient(w)
        w = w - alpha_n*check
        weight.append(w)
        cost.append(g(w))
    return weight,cost

a, b =descent(least, 0.5, 70, w)
plt.plot(np.arange(0, 71, 1), descent(least, 0.5, 70, w)[1])
plt.plot(np.arange(0, 71, 1), descent(least, 0.01, 70, w)[1])
plt.show()
'''
plt.plot(x, y, 'o')
plt.plot(x, f(x))
plt.show()
'''
