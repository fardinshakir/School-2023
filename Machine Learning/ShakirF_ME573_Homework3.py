import autograd.numpy as np
import matplotlib.pyplot as plt
from autograd import grad

# Parameters for our dataset
noise = 0.1
x = np.linspace(0, 1, 50).reshape(-1, 1)
y = []

# Initial conditions
w = np.array([2.0, 1.0])

# Adding Noise for our y values
for n in range(len(x)):
    what = x[n] + np.random.uniform(-noise, noise)
    y.append(what[0])

def model(x, w):
# This model function is simply a container for xdotT times w
    error = []

# Computing error at each interval
    for n in range(len(x)):
        xi = np.append(1, x[n])
        a = np.dot(xi, w)
        error.append(a)
    return error


def least(w):
# Container for the least square value
    least = 0
    for n in range(len(x)):

# Computing mean squared error
        a = (model(x, w)[n] - y[n])**2
        least += a
    return least/len(y)

def descent(g, alpha, steps, w):
# Gradient computation
    gradient = grad(least)
    for k in range(1, steps+1):
        if alpha == 'diminishing':
            alpha_n = 1/k
        else:
            alpha_n = alpha

# Making a list to store our values for later
    weight = [w]
    cost = [g(w)]

    for k in range(steps):
# Gradient is check
        check = gradient(w)

# Updating our weight and cost list including our original values
        w = w - alpha_n*check
        weight.append(w)
        cost.append(g(w))
    return weight,cost

# 0.5 alpha
a, b = descent(least, 0.5, 70, w)

# 0.01 alpha
c, d = descent(least, 0.01, 70, w)


# Printing the least square cost value
print(f"Least Square Cost Function Value = {least(w)}")
# Plotting the gradient descent of cost function history
xplot = np.arange(0, 71, 1)
ax = plt.axes()
ax.set_xlim(0, 70)
ax.set_ylim(0, 4)
plt.title('Red = 0.5 α , Blue = 0.01 α')
plt.plot(xplot, b, 'r')
plt.plot(xplot, d, 'b')
plt.show()
