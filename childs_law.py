import numpy as np
import math
from oct2py import Oct2Py
oc = Oct2Py()
oc.graphics_toolkit('gnuplot')
xx = np.arange(10, 11, 0.5)
oc.surf(np.divide.outer(np.multiply(8.8541871e-12,xx**1.5),xx**2))


