import numpy as np
import math
from oct2py import Oct2Py

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


material = raw_input('What material are you using in your experiment? Please capitalize the first letter of the material ... ')

print('PART 1 --> Childs Law')

xx = np.arange(1, 64, 1)
oc.surf(np.divide.outer(np.multiply(8.8541871e-12,xx**1.5),xx**2))


userInput()



print('PART 2 --> Richardson Dushman Equation')

T = np.arange(1, 1000, 0.5)

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

boltz = 1.3806488e-23
atsquare = np.multiply(materials[material][1], np.square(T))
kt = np.multiply(boltz, T)
WOverKt = np.divide(-materials[material][0], kt)
a = np.logaddexp(atsquare, np.exp(WOverKt))

oc.plot(T, a, 'r')
oc.title('Current Thermionic Emission Density of ' + material + ' VS. Temperature')
oc.xlabel('Temperature')
oc.ylabel('Current Thermionic Emission Density')

userInput()

    
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

numerator = np.subtract(E, materials[material])
numerator = -numerator
denominator = np.multiply(boltz, T)
fraction = np.divide.outer(numerator, denominator)
oc.surf(fraction)

oc.title('Log of Fermi-Dirac Statistics for ' + material)
oc.xlabel('Temperature (K)')
oc.ylabel('Energy E (J)')
oc.zlabel('Fermi-Dirac Statistics')

userInput()
