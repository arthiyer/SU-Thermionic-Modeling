# Necessary for plotting with Oct2Py
import numpy as np
# Necessary to perform mathematical functions
import math
# Implements Octave methods in python
from oct2py import Oct2Py

# Gives the user the option of whether to quit or continue at every stage in the program.
def userInput() :
    response = raw_input('Screenshot this image if you want it. Type the word yes into the terminal to continue. Type no to quit the program ... ')
    while True: 
        if response == 'yes':
            break
        elif response == 'no':
            exit(0)
        response = raw_input('Please enter a valid response (yes or no) ... ')

oc = Oct2Py()
oc.graphics_toolkit('gnuplot')

# This material is used for both Richardson-Dushman and Fermi-Dirac.
material = raw_input('What material are you using in your experiment? Please capitalize the first letter of the material ... ')

print('PART 1 --> Childs Law')

# Creates the x,y matrix using numpy
V = np.arange(1, 64, 1)
D = np.arange(1, 64, 1)

# Graphs Child's Law
oc.surf(np.divide.outer(np.multiply(8.8541871e-12,V**1.5),D**2))
oc.title('Childs law')
oc.xlabel('potential diff between anode & cathode (V)')
oc.ylabel('dist. between anode & cathode (mm)')
oc.zlabel('current density (mA mm-2)')

# Gives the user the option of whether or not to continue
userInput()

print('PART 2 --> Richardson Dushman Equation')

# Creates the x,y matrix using numpy
T = np.arange(1, 1000, 0.5)

# Dictionary catagorizing work functions and A correction factors by material.
# This is used for Part 2
materials = {'Molybdenum': [4.15, 55],
             'Nickel': [4.61, 30],
             'Tantalum': [4.12, 60],
             'Tungsten': [4.54, 60],
             'Cesium': [1.81, 160],
             'Iridium': [5.40, 160],
             'Platinum': [5.32, 32],
             'Rhenium': [4.84, 100],
             'Thorium': [3.38, 70],
             'Thoria': [2.54, 3],
             'Cs-Oxide': [0.75, 0.01],
             'default': [120.2, 1]
             }

# Boltzmann's constant
boltz = 1.3806488e-23

# Next three lines of code break up the equation into small parts to make debugging easier.
# This easier to follow for the reader.
atsquare = np.multiply(materials[material][1], np.square(T))
kt = np.multiply(boltz, T)
WOverKt = np.divide(-materials[material][0], kt)

# Overall function that puts the previous three lines of code together
function = np.logaddexp(atsquare, np.exp(WOverKt))

# Plots the function and appropriately labels the axes
oc.plot(T, function, 'r')
oc.title('Current Thermionic Emission Density of ' + material + ' VS. Temperature')
oc.xlabel('temperature (K)')
oc.ylabel('current density of the emission (mA/mm2)')

# Gives the user the option of whether or not to continue
userInput()

# Sets the ranges for the two variables in Part 3
T = np.arange(1, 64, 2)
E = np.arange(1, 64, 2)

# Dictionary categorizing the Ef of materials.
#This is used for Part 3.
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


# Next four lines of code break up the equation into small parts to make debugging easier.
# This easier to follow for the reader.
numerator = np.subtract(E, materials[material])
numerator = -numerator
denominator = np.multiply(boltz, T)
fraction = np.divide.outer(numerator, denominator)
# Plots the overall function, which puts the previous four lines of code together
oc.surf(fraction)

# Populates the plot with titles and labels
oc.title('Log of Fermi-Dirac Statistics for ' + material)
oc.xlabel('Temperature (K)')
oc.ylabel('Energy E (J)')
oc.zlabel('Fermi-Dirac Statistics')

# Stalls so that the plot does not disappear before the user wants it to.
raw_input(' ')
