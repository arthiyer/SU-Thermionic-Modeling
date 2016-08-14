import numpy as np
import math
from oct2py import Oct2Py

oc = Oct2Py()
oc.graphics_toolkit('gnuplot')
xx = np.arange(1, 1000, 0.5)

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
atsquare = np.multiply(materials[material1][1], np.square(xx))
kt = np.multiply(boltz, xx)
WOverKt = np.divide(-materials[material1][0], kt)
a = np.logaddexp(atsquare, np.exp(WOverKt))

oc.plot(xx, a, 'r')
oc.title('Current Thermionic Emission Density of ' + material1 + ' VS. Temperature')
oc.xlabel('Temperature')
oc.ylabel('Current Thermionic Emission Density')

raw_input(' ')
