import numpy as np
import math
from oct2py import Oct2Py
#from drawnow import drawnow

oc = Oct2Py()
oc.graphics_toolkit('gnuplot')
xx = np.arange(1, 1000, 0.5)

materials = {'molybdenum': [4.15, 55],
             'nickel': [4.61, 30],
             'tantalum': [4.12, 60],
             'tungsten': [4.54, 60],
             'cesium': [1.81, 160],
             'iridium': [5.40, 160],
             'platinum': [5.32, 32],
             'rhenium': [4.84, 100],
             'thorium': [3.38, 70],
             'thoria': [2.54, 3],
             'cs-oxide': [0.75, 0.01],
             'default': [120.2, 1]
    }

material1 = raw_input('What cathode material are you using?')
boltz = 1.3806488e-23
atsquare = np.multiply(materials[material1][1], np.square(xx))
kt = np.multiply(boltz, xx)
WOverKt = np.divide(-materials[material1][0], kt)
a = np.logaddexp(atsquare, np.exp(WOverKt))
question = raw_input('Would you like to plot the results for another cathode material? ')

if question == 'yes':
    material2 = raw_input('What is the second cathode material you are using?')
    atsquare2 = np.multiply(materials[material2][1], np.square(xx))
    kt2 = np.multiply(boltz, xx)
    WOverKt2 = np.divide(-materials[material2][0], kt2)
    b = np.logaddexp(atsquare2, np.exp(WOverKt2))
    question3 = raw_input('Would you like to plot the results for one last cathode material?')
    if question3 == 'yes':
       material3 = raw_input('What is the third cathode material you are using?')
       atsquare3 = np.multiply(materials[material3][1], np.square(xx))
       kt3 = np.multiply(boltz, xx)
       WOverKt3 = np.divide(-materials[material3][0], kt3)
       c = np.logaddexp(atsquare3, np.exp(WOverKt3))


#subplot(3, 1000, 1)
#fplot
#plot(x1, a, s1, x2, b, s2, x3, c, s3)
oc.plot(xx, a, 'r')
oc.title(material1)
oc.xlabel('Temperature')
oc.ylabel('Current Thermionic Emission Density')


#oc.plot(xx, b, 'b')
#oc.plot(xx, c, 'g')
#oc.show()

raw_input(' ')
