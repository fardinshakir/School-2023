import numpy as np
import matplotlib.pyplot as plt


# Analysis Criteria
type = 'Fins' # Choose Length, Width, Thickness, or Number of Fins (Thickness uses m^-1)
min = 1
max = 100


# Fin Properties
reference_N = 57 # Number of Fins
l = 116 # mm
w = 54.1 # mm
t = 0.4 # mm
h = 120 # mm

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
Pr = 0.707 # Prandtl Number



# Defining Fin Properties
def fin_array(l, w, t, h):
# Unit Conversion
    l = l/1000 # Length, m
    w = w/1000 # Width, m
    t = t/1000 # Thickness, m
    h = h/1000 # Height, m

    l_in = 56/1000 # Inner Length, m
    w_in = 34.1/1000 # Inner Width, m
    w_hp = 4.2625/1000 # Heat Pipe Length, m
    l_hp = 5/1000 # Heat Pipe Length, m

    L = 20/1000 # Annular Length, m

# Characteristic Dimension
    x = w # m

# Dimensionless Numbers
    Re_x = (v * x)/(visc) # Reynolds Number
    Nu_x = 0.332*(np.sqrt(Re_x))*(np.cbrt(Pr)) # Nusselt Number
    h_air = (Nu_x*k_water)/x # Convective Heat Transfer Coefficient, W/m^2K

    return l, w, t, h, l_in, w_hp, l_hp, w_in, L, h_air

# Fin Analysis Function
def fin_analysis(N, l, w, t, h, l_in, w_hp, l_hp, w_in, L, h_air):
# Temperature of base - Temperature of Fluid
    theta = T_copper-T_air

# Area of Fins
    A_f = 2*((w*l)-(w_in * l_in)) + 2*(l*t) + 2*(t*w) # Surface Area, m^2
    Lc = L + t/2 # Annular Length, m
    Ap = Lc*t # Annular Crossectional Area, m^2

# Area of Base and Total Area
    A_b = 4*(w_hp*h)+4*(l_hp*h) # Area of Base, m^2
    A_t = N*A_f + A_b # Total Area of Fins and Base, m^2

# Fin Efficiency
    annular_eff = np.sqrt(Lc**3) * np.sqrt(h_air/(k_aluminum*Ap)) # Reference Number for Figure 3

    m = np.sqrt((2*h_air)/(k_aluminum*t))
    n_f = (np.tanh(m*Lc))/(m*Lc)

# Finn Array Efficiency and Heat Rate
    q_t = h_air*A_t*(1 - ((N*A_f)/A_t)*(1-n_f))*theta # Heat Rate of Fin Array, W
    n_o = 1 - ((N*A_f)/A_t)*(1-n_f) # Total Fin Array Efficiency, %

    return n_o, q_t

'''
# Plotting Efficiency vs Number of Fins
def efficiency_plot(min, max, refN, reference_n_f):
# Range of Number of Fins
    N = np.arange(min, max, 1)
    full_efficiency_list = []
    efficiency_list = []
# Efficiency for Each Number of Fins
    for n in range(len(N)):
        eff, e = fin_analysis(N[n], l, w, t, h, l_in, w_hp, l_hp, w_in, L, h_air)
# Check if Efficiency is Better than Given by Manufacturer
        if eff > round(reference_n_f, 4):
            efficiency_list.append(eff)
        full_efficiency_list.append(eff)

# Plotting Full List and Cutoff List
    plt.ylabel('Fin Array Efficiency, n_f')
    plt.xlabel('Number of Fins, N')
    plt.title('Fin Array Efficiency vs Number of Fins')
    plt.plot(N, full_efficiency_list, 'r', linewidth=3)
    plt.plot(np.arange(min, len(efficiency_list), 1), efficiency_list, 'g', linewidth=5)
    plt.show()
'''

# Plotting Efficiency vs Interested Factor
def efficiency_plot(dimension, min, max, refN, reference_n_f, l, w, t):

    if dimension == 'Fins':
    # Range of Number of Fins
        x = np.arange(min, max, 1)
        full_efficiency_list = []
        efficiency_list = []
    # Efficiency for Each Number of Fins
        for n in range(len(x)):
            eff, q_rate = fin_analysis(x[n], l, w, t, h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Efficiency is Better than Given by Manufacturer
            if eff > round(reference_n_f, 4):
                efficiency_list.append(eff)
            full_efficiency_list.append(eff)

        if efficiency_list == []:
            print(f'Number of {dimension} do not significantly affect fin efficiency.')
        else:
            print(f'Number of {dimension} do significantly affect fin efficiency.')

    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Efficiency, n_f')
        plt.xlabel('Number of Fins, N')
        plt.title('Fin Array Efficiency vs Number of Fins')
        plt.plot(x, full_efficiency_list, 'r', linewidth=3)
        plt.plot(np.arange(min, len(efficiency_list)+1, 1), efficiency_list, 'g', linewidth=5)
        plt.plot(reference_N, reference_n_f, 'bo')
        plt.show()

    elif dimension == 'Length':
    # Range of Length
        x = np.arange(min, max, 1)/1000
        full_efficiency_list = []
        efficiency_list = []
    # Efficiency for Each Length
        for n in range(len(x)):
            eff, e = fin_analysis(refN, x[n], w, t, h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Efficiency is Better than Given by Manufacturer
            full_efficiency_list.append(eff)
            if eff < round(reference_n_f, 4):
                efficiency_list.append(eff)

        if efficiency_list == []:
            print(f'{dimension} factor does not significantly affect fin efficiency.')
        else:
            print(f'{dimension} factor does significantly affect fin efficiency.')
    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Efficiency, n_f')
        plt.xlabel('Length of Fin, m')
        plt.title('Fin Array Efficiency vs Length')
        plt.plot(x, full_efficiency_list, 'g', linewidth=5)

        if len(efficiency_list) == 1:
            index = full_efficiency_list.index(efficiency_list[0])
            plt.plot(x[index], efficiency_list, 'go', linewidth=5)
        else:
            plt.plot(np.arange(min, len(efficiency_list)+1, 1)/1000, efficiency_list, 'r', linewidth=3)
        plt.plot(l, reference_n_f, 'bo')

        plt.show()

    elif dimension == 'Width':
    # Range of Width
        x = np.arange(min, max, 1)/1000
        full_efficiency_list = []
        efficiency_list = []
    # Efficiency for Each Width
        for n in range(len(x)):
            eff, e = fin_analysis(refN, l, x[n], t, h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Efficiency is Better than Given by Manufacturer
            full_efficiency_list.append(eff)
            if eff < round(reference_n_f, 4):
                efficiency_list.append(eff)

        if efficiency_list == []:
            print(f'{dimension} factor does not significantly affect fin efficiency.')
        else:
            print(f'{dimension} factor does significantly affect fin efficiency.')
    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Efficiency, n_f')
        plt.xlabel('Width of Fin, m')
        plt.title('Fin Array Efficiency vs Width')
        plt.plot(x, full_efficiency_list, 'g', linewidth=5)

        if len(efficiency_list) == 1:
            index = full_efficiency_list.index(efficiency_list[0])
            plt.plot(x[index], efficiency_list, 'go', linewidth=5)
        else:
            plt.plot(np.arange(min, len(efficiency_list)+1, 1)/1000, efficiency_list, 'r', linewidth=3)
        plt.plot(w, reference_n_f, 'bo')

        plt.show()

    elif dimension == 'Thickness':
    # Range of Thickness
        x = np.arange(min, max, 1)/10000
        full_efficiency_list = []
        efficiency_list = []
    # Efficiency for Each Thickness
        for n in range(len(x)):
            eff, e = fin_analysis(refN, l, w, x[n], h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Efficiency is Better than Given by Manufacturer
            full_efficiency_list.append(eff)
            if eff < round(reference_n_f, 4):
                efficiency_list.append(eff)

        if efficiency_list == []:
            print(f'{dimension} factor does not significantly affect fin efficiency.')
        else:
            print(f'{dimension} factor does significantly affect fin efficiency.')
    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Efficiency, n_f')
        plt.xlabel('Thickness of Fin, m')
        plt.title('Fin Array Efficiency vs Thickness')
        plt.plot(x, full_efficiency_list, 'g', linewidth=5)

        if len(efficiency_list) == 1:
            index = full_efficiency_list.index(efficiency_list[0])
            plt.plot(x[index], efficiency_list, 'go', linewidth=5)
        else:
            plt.plot(np.arange(min, len(efficiency_list)+1, 1)/10000, efficiency_list, 'r', linewidth=3)
        plt.plot(t, reference_n_f, 'bo')

        plt.show()

    elif dimension not in ['Length', 'Width', 'Thickness', 'Fins']:
        print("Choose either 'Length', 'Width', 'Thickness', or 'Fins'.")



# Plotting Efficiency vs Interested Factor
def heat_rate_plot(dimension, min, max, refN, reference_heat_rate, l, w, t):

    if dimension == 'Fins':
    # Range of Number of Fins
        x = np.arange(min, max, 1)
        full_heat_list = []
        heat_list = []
    # Heat Rate for Each Number of Fins
        for n in range(len(x)):
            eff, q_rate = fin_analysis(x[n], l, w, t, h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Heat Rate is Better than Given by Manufacturer
            if q_rate < round(reference_heat_rate, 4):
                full_heat_list.append(q_rate)
            heat_list.append(q_rate)

        if heat_list == []:
            print(f'Number of {dimension} do not significantly affect fin heat.')
        else:
            print(f'Number of {dimension} do significantly affect fin heat.')

    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Heat Rate, q_t')
        plt.xlabel('Number of Fins, N')
        plt.title('Fin Array Heat Rate vs Number of Fins')

        plt.plot(x, heat_list, 'g', linewidth=3)
        plt.plot(np.arange(min, len(full_heat_list)+1, 1), full_heat_list, 'r', linewidth=5)
        plt.plot(reference_N, reference_heat_rate, 'bo')

        plt.show()



    elif dimension == 'Length':
    # Range of Lenth
        x = np.arange(min, max, 1)/1000
        full_heat_list = []
        heat_list = []
    # Heat Rate for Each Number Length
        for n in range(len(x)):
            eff, q_rate = fin_analysis(refN, x[n], w, t, h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Heat Rate is Better than Given by Manufacturer
            if q_rate < round(reference_heat_rate, 4):
                heat_list.append(q_rate)
            full_heat_list.append(q_rate)

        if heat_list == []:
            print(f'{dimension} factor does not significantly affect fin heat.')
        else:
            print(f'{dimension} factor does significantly affect fin heat.')

    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Heat Rate, q_t')
        plt.xlabel('Length, m')
        plt.title('Fin Array Heat Rate vs Length')

        plt.plot(x, full_heat_list, 'g', linewidth=3)
        plt.plot(np.arange(min, len(heat_list)+min, 1)/1000, heat_list, 'r', linewidth=5)

        plt.plot(l, reference_heat_rate, 'bo')

        plt.show()

    elif dimension == 'Width':
    # Range of Lenth
        x = np.arange(min, max, 1)/1000
        full_heat_list = []
        heat_list = []
    # Heat Rate for Each Number Width
        for n in range(len(x)):
            eff, q_rate = fin_analysis(refN, l, x[n], t, h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Heat Rate is Better than Given by Manufacturer
            if q_rate < round(reference_heat_rate, 4):
                heat_list.append(q_rate)
            full_heat_list.append(q_rate)

        if heat_list == []:
            print(f'{dimension} factor does not significantly affect fin heat.')
        else:
            print(f'{dimension} factor does significantly affect fin heat.')

    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Heat Rate, q_t')
        plt.xlabel('Width, m')
        plt.title('Fin Array Heat Rate vs Width')

        plt.plot(x, full_heat_list, 'g', linewidth=3)
        plt.plot(np.arange(min, len(heat_list)+min, 1)/1000, heat_list, 'r', linewidth=5)

        plt.plot(w, reference_heat_rate, 'bo')

        plt.show()

    elif dimension == 'Thickness':
    # Range of Lenth
        x = np.arange(min, max, 1)/10000
        full_heat_list = []
        heat_list = []
    # Heat Rate for Each Number Thickness
        for n in range(len(x)):
            eff, q_rate = fin_analysis(refN, l, w, x[n], h, l_in, w_hp, l_hp, w_in, L, h_air)
    # Check if Heat Rate is Better than Given by Manufacturer
            if q_rate < round(reference_heat_rate, 4):
                heat_list.append(q_rate)
            full_heat_list.append(q_rate)

        if heat_list == []:
            print(f'{dimension} factor does not significantly affect fin heat.')
        else:
            print(f'{dimension} factor does significantly affect fin heat.')

    # Plotting Full List and Cutoff List
        plt.ylabel('Fin Array Heat Rate, q_t')
        plt.xlabel('Thickness, m')
        plt.title('Fin Array Heat Rate vs Thickness')

        plt.plot(x, full_heat_list, 'g', linewidth=3)
        plt.plot(np.arange(min, len(heat_list)+min, 1)/10000, heat_list, 'r', linewidth=5)

        plt.plot(t, reference_heat_rate, 'bo')

        plt.show()

    elif dimension not in ['Length', 'Width', 'Thickness', 'Fins']:
        print("Choose either 'Length', 'Width', 'Thickness', or 'Fins'.")




l, w, t, h, l_in, w_hp, l_hp, w_in, L, h_air = fin_array(l, w, t , h)
efficiency, heat_rate = fin_analysis(reference_N, l, w, t, h, l_in, w_hp, l_hp, w_in, L, h_air)
print(f"Fin Array Efficiency, n_o = {round(efficiency, 2)*100} %\nFin Array Heat Rate, q_t = {round(heat_rate, 2)} W")
#fin_amount_plot(min_fins, max_fins, reference_N, efficiency)
efficiency_plot(type, min, max, reference_N, efficiency, l, w, t)
heat_rate_plot(type, min, max, reference_N, heat_rate, l, w, t)
