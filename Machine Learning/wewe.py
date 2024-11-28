import autograd.numpy as np
import matplotlib.pyplot as plt
from autograd import grad
import ml_refi
g = lambda w: w[0]**2 + w[1]**2 + 2*np.sin(1.5*(w[0] + w[1])) + 2
G_func = lambda x, y: x**2 + y**2 + 2*np.sin(1.5*(x + y)) + 2

alpha = 10**(-2)
steps = 10
w = np.array([3, 3])
print(grad(w))

# gradient descent function - inputs: g (input function), alpha (steplength parameter), max_its (maximum number of iterations), w (initialization)
def gradient_descent(g,alpha,max_its,w):
    weight_history = [w]           # container for weight history
    cost_history = [g(w)]          # container for corresponding cost function history
    for k in range(max_its):

        w = w - alpha*gradient

        # record weight and cost
        weight_history.append(w)
        cost_history.append(g(w))
    return weight_history,cost_history




# Plotting functions
def plot():
# Obtaining the random search values
    a,b = random(g, alpha, steps, w)
# RANDOM SEARCH FUNCTION
# Initializing the figure
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    w1 = np.arange(-5, 5, .1)
    w2 = np.arange(-5, 5, .1)
    W1, W2 = np.meshgrid(w1, w2)
    G = G_func(W1, W2)

# Creating plot and adjusting axis limits
    ax.plot_surface(W1, W2, G)
    ax.set_title('Random Search Function')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

# Creating data points for the w values
    aax = []
    aay = []
    for n in range(0, len(a)):
        aax.append(a[n][0])
        aay.append(a[n][1])
    ax.plot(aax, aay, '-o')

# COST FUNCTION
# Initializing the figure
    cost_fig = plt.figure()
    cost_ax = plt.axes()

# Creating plot for the cost function and adjusting axis limits
    cost_ax.set_xlim(0, 6)
    cost_ax.set_ylim(0, 30)
    cost_ax.set_title('Cost Function')
    x = np.arange(0, len(b), 1)
    cost_ax.plot(x, b, '-o')
    print(f"w[X] coordinates: {aax}\nw[Y] coordinates: {aay}\n\ncost[X] coordinates: {x}\ncost[Y] coordinates: {b}")
    plt.show()

a, b = gradient_descent(g, alpha, steps, w)
print(b)

x = np.arange(0, len(b), 1)
'''
X, Y = np.meshgrid(x, y)
G = G_func(X, Y)
plt.figure()
plt.contourf(X, Y, G)
plt.show()
'''
plt.figure()
plt.plot(x, b)
plt.show()
