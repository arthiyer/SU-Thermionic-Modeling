import numpy as np
import math
from oct2py import Oct2Py

oc = Oct2Py()
oc.graphics_toolkit('gnuplot')
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

material1 = raw_input('What cathode material are you using? Please capitalize the first letter of the material... ')
boltz = 1.3806488e-23
atsquare = np.multiply(materials[material][1], np.square(T))
kt = np.multiply(boltz, T)
WOverKt = np.divide(-materials[material][0], kt)
a = np.logaddexp(atsquare, np.exp(WOverKt))

oc.plot(xx, a, 'r')
oc.title('Current Thermionic Emission Density of ' + material + ' VS. Temperature')
oc.xlabel('Temperature')
oc.ylabel('Current Thermionic Emission Density')

raw_input(' ')
