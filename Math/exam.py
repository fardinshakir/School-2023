import numpy as np
import matplotlib.pyplot as plt
x = np.arange(10, 201, 1)
#print(x)
def f(x):
    return (x * 0.06858)/(1.48*10**(-5))

#
def D(x, y):
    return (y*1.225*(x**(2))*(np.pi*(D/2)**2))/2

Re = f(x)
#print(Re)
D = (0.7 * 1.225 * (x**2) * (np.pi*(0.06858/2)))/2
print(D)

plt.plot(x, D)
plt.title('Drag vs Velocity')
plt.xlabel('Velicty (m/s)')
plt.ylabel('Drag (kg m/s)')
plt.show()
