import autograd.numpy as np
import matplotlib.pyplot as plt
from autograd import grad

noise = 0.5
x = []
y = []
# X values
for n in range(-5, 5):
    x.append(n + np.random.uniform(-noise, noise))
# Y
for n in range(len(x)):
    if x[n] >= 0.5:
        y.append(1)
    elif x[n] < 0.5:
        y.append(0)

w = np.array([3.0, 3.0])
alpha = 1
steps = 25

# Sigmoid function
def sigmoid(t):
    return 1/(1+np.exp(-t))

# Model(x.T * w)
def model(x, w):
    error = []
    for n in range(len(x)):
        xi = np.append(1, x[n])
        a = np.dot(xi, w)
        error.append(a)
    return error

# Cross entropy (simple)
def cross_entropy(w):
    cost = 0
    for n in range(len(x)):
        if y[n] == 1:
            a = -np.log(sigmoid(model(x, w)[n]))
            cost += a
        elif y[n] == 0:
            a = -np.log(1-sigmoid(model(x, w)[n]))
            cost += a

    return cost

# Moduar cross entropy
def modular_cross_entropy(w):
    cost = 0
    for n in range(len(x)):
        a = (y[n]*np.log(sigmoid(model(x, w)[n])) + (1-y[n])*np.log(1 - sigmoid(model(x, w)[n])))
        cost += a
    return -cost/len(x)

# Gradient descent
def descent(g, alpha, steps, w):
    gradient = grad(g)
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

a, b = descent(modular_cross_entropy, alpha, steps, w)

xx = np.arange(-5, 5, 0.1)

def f(t):
    return 1/(1+np.exp(-(t * a[25][1] + a[25][0])))

print(f"After 25 iterations, w = {a[25]}")
plt.plot(xx, f(xx), 'k')
plt.plot(x,y, 'o')
plt.show()
