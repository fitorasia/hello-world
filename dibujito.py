#!//Library/Frameworks/Python.framework/Versions/Current/bin/python

import sys
import numpy as np
from matplotlib import pyplot as pl

a=np.arange(1000)
b=np.cos(a/200)

pl.plot(a,b)
pl.show()
