import numpy as np
import math
from oct2py import Oct2Py

oc = Oct2Py()
oc.graphics_toolkit('gnuplot')
T = np.arange(1, 64, 2)
E = np.arange(1, 64, 2)

materials = {'Lithium': 4.74,
             'Sodium' : 3.24,
             'Potassium': 2.12,
             'Rubidium': 1.85,
             'Cesium': 1.59,
             'Copper': 7.00,
             'Silver': 5.49,
             'Gold': 5.53,
             'Berilium': 14.30,
             'Magnesium': 7.08,
             'Calcium': 4.69,
             'Strontium': 3.93,
             'Barium': 3.64,
             'Niobium': 5.32,
             'Iron': 11.10,
             'Manganese': 10.9,
             'Zinc': 9.47,
             'Cadmium': 7.47,
             'Mercury': 7.13,
             'Aluminum': 11.7,
             'Gallium': 10.40,
             'Indium': 8.63,
             'Thalium': 8.15,
             'Tin': 10.20,
             'Lead': 9.47,
             'Bismuth': 9.90,
             'Antimony': 10.90
}



material = raw_input('What material are you using? Please capitalize the first letter of the material... ')
#T = raw_input('What is the max temperature of your experiment? ')
boltz = 1.3806488e-23

numerator = np.subtract(E, materials[material])
numerator = -numerator
denominator = np.multiply(boltz, T)
fraction = np.divide.outer(numerator, denominator)
oc.surf(fraction)

oc.title('Log of Fermi-Dirac Statistics for ' + material)
oc.xlabel('Temperature (K)')
oc.ylabel('Energy E (J)')
oc.zlabel('Fermi-Dirac Statistics')

raw_input(' ')

