import numpy as np
from math import pi
from matplotlib import pyplot as plt, pyplot


def scrape_web_data(url):
    import pandas as pd

    url_data = pd.read_html(url)
    return url_data


if __name__ == '__main__':
    gas_data_url = 'https://www.ohio.edu/mechanical/thermo/property_tables/gas/idealGas.html'
    gas_data = scrape_web_data(gas_data_url)[0]
    gas_names = gas_data[0]
    gas_ratios = gas_data[6]
    desired_gases = ['Hydrogen', 'Methane', 'Octane', 'Butane']
    gas_ratios_dictionary = {}
    for desired_gas in desired_gases:
        for index, row in gas_data.iterrows():
            if row[0] == desired_gas:
                gas_ratios_dictionary[row[0]] = row[6]

    gas_data = scrape_web_data(gas_data_url)[0]
    gas_names = gas_data[0]
    gas_ratios = gas_data[6]
    desired_gases = ['Hydrogen', 'Methane', 'Octane', 'Butane']
    gas_data_dictionary = {}
    for desired_gas in desired_gases:
        for index, row in gas_data.iterrows():
            if row[0] == desired_gas:
                gas_data_dictionary[row[0]] = {
                    'isochoric specific heat': row[5],
                    'specific heat ratio': row[6]
                }

    combustion_data_url = 'https://en.wikipedia.org/wiki/Heat_of_combustion'
    combustion_data = scrape_web_data(combustion_data_url)[3]
    for desired_gas in desired_gases:
        for index, row in combustion_data.iterrows():
            if row[0] == desired_gas:
                gas_data_dictionary[row[0]]['heat of combustion'] = row[4]

    print(gas_data_dictionary)

    # volume range to plot over -- use np.linspace()
    # define P(V) = k / V^γ + P_0
    # calculate ΔT at fixed V
    # define P2
#Hydrogen
γ = 1.405
V_1 = pi*(1/2 * 0.0995)**2*(79)
V_2 = 0.000100
#atmospheric pressure
T_2= 244 #still have to change
# heat of combustion?
T_1= 294
P_0 = 101352
k = P_0 * V_1**γ

def P(V_2): #psi
    return k / V_2**γ + P_0

#Bore of engine = 99.5mm, stroke of engine = 79mm
Volume_Range =np.linspace(V_2, V_1)
Pressure_Range =P(Volume_Range)
print(V_1)
print(P(V_2))
print(k)



plt.plot(Volume_Range, Pressure_Range)
plt.xlabel('volume (mm**3)')
plt.ylabel('pressure (psi)')
plt.show()

# # Draft code comments
#
# Does the code run without error?
# If any error occurs, can you suggest a potential fix?
#
# How understandable is the output of the code?
# Point out any parts you do not understand.
#
# How readable is the code itself?
# Say where formatting or commenting would make the code more readable or where PEP-8 is violated.
#
# How clearly do the code comments describe the problem it is trying to solve?
# Identify places that would benefit from a clearer comment.
#
# How clearly do the variable names relate to the concepts they concretize?
# Point out any variables you don't recognize, and/or suggest better names. Check for PEP-8 compliance.
#
# How well does the range of variables capture the problem described?
# Identify extraneous regions that could be left out or important regions that should be included.
#
# To what degree does the script follow a functional programming paradigm, packaging all major components of the script
# into separately defined functions that pass information among them in a small number of lines? Identify ways in which
# the functionalization of the code could be improved.
# How clearly do the visualizations show the solutions to the problem?
#
# Say if there is extraneous whitespace or the co-domain or domain of the data should be changed or any other ways the
# visualizations could be more effective
#