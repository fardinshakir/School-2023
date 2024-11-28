import numpy as np
import matplotlib.pyplot as plt


# Fin Dimensions
l = 116/1000 # Length, m
w = 54.1/1000 # Width, m
t = 0.4/1000 # Thickness, m
h = 120/1000 # Height, m

l_in = 56/1000 # Inner Length, m
w_in = 34.1/1000 # Inner Width, m
w_hp = 4.2625/1000 # Heat Pipe Length, m
l_hp = 5/1000 # Heat Pipe Length, m

L = 20/1000 # Annular Length, m

# Temperatures
T_copper = 343 # Kelvin, 70c
T_water = 335.925 # Kelvin, 62.775c
T_air = 293.15 # Kelvin, 20c

# Thermal Conductivity
k_copper = 398 # W/mK
k_aluminum = 237 # W/mK
k_water = 26.3 * 10**(-3) # W/mK

# Air Properties
v = 6.911 # m/s
visc = 15.89 * (10**(-6)) # kg/m*s

# Dimensionless Numbers
Pr = 0.707 # Air

# Characteristic Dimension
x = w # m
Re_x = (v * x)/(visc) # Reynolds Number
Nu_x = 0.332*(np.sqrt(Re_x))*(np.cbrt(Pr)) # Nusselt Number
h_air = (Nu_x*k_water)/x # Convective Heat Transfer Coefficient, W/m^2K

# Fin Analysis Function
def fin_analysis(N, l, w, t, l_in, w_hp, l_hp, w_in, L, h):

    # Temperature of base - Temperature of Fluid
    theta = T_copper-T_air

    A_f = 2*((w*l)-(w_in * l_in)) + 2*(l*t) + 2*(t*w) # Surface Area, m^2
    Lc = L + t/2 # Annular Length, m
    Ap = Lc*t # Annular Crossectional Area, m^2

    A_b = 4*(w_hp*h)+4*(l_hp*h) # Area of Base, m^2
    A_t = N*A_f + A_b # Total Area of Fins and Base, m^2

    annular_eff = np.sqrt(Lc**3) * np.sqrt(h_air/(k_aluminum*Ap)) # Reference Number for Figure 3
    n_f = 0.82 # Single Annular Fin Efficiency, %

    q_t = h_air*A_t*(1 - ((N*A_f)/A_t)*(1-n_f))*theta # Heat Rate of Fin Array, W
    n_o = 1 - ((N*A_f)/A_t)*(1-n_f) # Total Fin Array Efficiency, %

    return n_o, q_t


# Plotting Efficiency vs Number of Fins
def fin_amount_plot(min, max, refN):
    N = np.arange(min, max, 1)
    full_efficiency_list = []
    efficiency_list = []
    for n in range(len(N)):
        eff, e = fin_analysis(N[n], l, w, t, l_in, w_hp, l_hp, w_in, L, h)
        if eff > fin_analysis(refN, l, w, t, l_in, w_hp, l_hp, w_in, L, h)[0]:
            plt.scatter(N[n], eff, color='red')
            plt.pause(0.01)
            plt.ylabel('Fin Array Efficiency n_f')
            plt.xlabel('Number of Fins N')

    #print(f"Fin Array Efficiency, n_o = {eff}\nFin Array Heat Rate, q_t = {e}")
    plt.show()



min_fin = 0
max_fin = 100
refN = 57
#fin_analysis(refN, l, w, t, l_in, w_hp, l_hp, w_in, L, h)
fin_amount_plot(min_fin, max_fin, 57)
