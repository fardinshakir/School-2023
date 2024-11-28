'''
Fardin Shakir
MAT 460 Numerical Differential Equations
Project
5/6/2022
'''
# Importing necessary libraries

import numpy as np
import matplotlib.pyplot as pl
import matplotlib.animation as animation


# Gravitational constant
gamma = 1
# Iterations (higher for smoother plotting and further range of data)
n = 10000
# Masses 1 and 2
m1 = 50
m2 = 1

# Main function which runs program
def main():
    my_animation(runge(y0))  



def my_animation(Y):
# Generating figure for plotting
    fig, ax = pl.subplots()
# Setting my data points
    dots, = pl.plot([], [], 'ro',)
# Plot configuration (title, grid, x, and y limits)
    pl.title("Two Masses Planetary Motion")
    ax.grid()
    ax.set_xlim(-10, 20)
    ax.set_ylim(-10, 10)

# Setting up my update frame function
    def update_frame(i):
        dots.set_data([ Y[i][0,0], Y[i][1,0] ], [ Y[i][0, 1], Y[i][1, 1] ])
        return dots,
# Defining how my animation is function (1ms intervals and n frames)
    anim = animation.FuncAnimation(fig, update_frame,  interval=1,
                        frames=n, blit=True, save_count=100)
    pl.show()



# Force attraction system of equations
def f(y):
    F1 = ((gamma*m1*m2)/(np.linalg.norm(y[1]-y[0])**3))*(y[1] - y[0])
    # Setting up my system of differential equations
    return np.array([y[2], y[3], F1/m1, -F1/m2])



# Runge Kutta Function
def runge(y0):
    # Step size
    h = 0.1
    # Initial positions
    y = y0
    # Initial values
    yin = y0
    # Empty solution box for solutions
    ysolve = []

    # For loop for 4th Order RK
    for i in range(1, n + 1):
        # Runge Kutta takes initial cooridinates and determines next in sequence of a first order differential equation
        k1 = h * f(y)
        k2 = h * f(y + 0.5 * h * k1)
        k3 = h * f(y + 0.5 * h * k2)
        k4 = h * f(y + h* k3)
        # Next y value
        y = y + (h / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        # Combing my empty solutions box and solutions
        ysolve.append(y)
    # My final solution box which contains initial and n iterations of solutions
    return np.concatenate([yin[None, ...], ysolve], axis=0)



# ALL MY INITIAL CONDITIONS 
# Positions of mass 1 and 2
x1 = np.array([0, 0])   
x2 = np.array([10, 0])

# Velocity of masses 1 and 2
p = 1
v1 = np.array([0, p/m1])
v2 = np.array([0, p/m2])

# Setting up my initial system
y0 = np.array([x1, x2, v1, v2])

if __name__ == "__main__":
    main()