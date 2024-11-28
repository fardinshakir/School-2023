import matplotlib.pyplot as plt
import autograd.numpy as np
from autograd import grad

# Function for gradient
g = lambda w: w[0]**2 + w[1]**2 + 2*np.sin(1.5*(w[0] + w[1])) + 2

# g and G will represent the same funciton***

# Function for plotting
G_func = lambda x, y: x**2 + y**2 + 2*np.sin(1.5*(x + y)) + 2

# Search parameters
alpha = 1
w = np.array([3.0, 3.0])
steps = 10
def descent(g,alpha,steps,w):
# Gradient computation
    gradient = grad(g)
    for k in range(1, steps+1):
        if alpha == 'diminishing':
            alpha_n = 1/k
        else:
            alpha_n = alpha

# Making a list to store our values for later
    weight = [w]
    cost = [g(w)]
    for k in range(steps):
# Checking the gradient
        check = gradient(w)

# Updating our weight and cost list including our original values
        w = w - alpha_n*check
        weight.append(w)
        cost.append(g(w))
    return weight,cost


def plot():
# Obtaining the search values
    a, b = descent(g, alpha, steps, w)
    aax = []
    aay = []
    for n in range(len(a)):
        aax.append(a[n][0])
        aay.append(a[n][1])

# GRADIENT DESCENT FUNCTION
# Initializing the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.arange(-5, 5, 0.1)
    m = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(u, u)
    G = G_func(X, Y)
# Creating plot and adjusting axis limits
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title('Gradient Descent Function')
    ax.contourf(X, Y, G)

# COST FUNCTION
    x = np.arange(0, len(b), 1)
    costplot = plt.figure(figsize=(10, 5))
    cost_ax = plt.axes()
# Creating plot and adjusting axis limits
    cost_ax.plot(x, b)
    cost_ax.set_xlim(0, steps)
    cost_ax.set_ylim(0, max(b)+5)
    cost_ax.set_title('Cost Function')

    print(f"w[X] coordinates: {aax}\nw[Y] coordinates: {aay}\n\ncost[X] coordinates: {x}\ncost[Y] coordinates: {b}")
    plt.show()
plot()
