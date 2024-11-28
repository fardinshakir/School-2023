import numpy as np

l = 10
w = 5
t = 0.5
A_f = 2*(w*l) + 2*(l*t) + (t*w)
A_b = 5*5


T_cpui = 373 # Kelvin, 100c
T_water = 335.925 # Kelvin, 62.775c

k_copper = 398 # W/mK
k_aluminum = 237 # W/mK
h_air = 35 # W/m^2k (~ @ 8.168 m/s)

N = 57
A_t = N*A_f + A_b
Lc = l + (t/2)
m = np.sqrt((2*h_air)/(k_aluminum*t))
nf = (np.tanh(m*Lc))/(m*Lc)

no = 1-((N*A_f)/A_t)*(1-nf)
print(nf)
print(no)
