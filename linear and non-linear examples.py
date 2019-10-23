# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:38:04 2019

@author: thulfiqar
"""

import numpy as np
import matplotlib.pyplot as plot



# linear
time = np.arange(0, 10, 0.1);
amplitude = 0.5 * time
plot.plot(time, amplitude)

# the system should follow the rules of superposition
# if we have y1 = f(x1) and y2 = f(x2) then f(x1+x2) = y1 + y2


# and homogeneity if we have y = f(x) then Ay = f(Ax)



# non-linear
time = np.arange(0, 10, 0.1);
amplitude = 3.5 + 0.5 * time
plot.plot(time, amplitude)


# non-linear
LN_amplitude   = np.log(time)

plot.plot(time, LN_amplitude)




