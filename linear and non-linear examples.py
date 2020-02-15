# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:38:04 2019

@author: thulfiqar
"""

import numpy as np
import matplotlib.pyplot as plt



# non linear
time = np.arange(0, 10, 0.1);
amplitude = 0.5 * time
plt.plot(time, amplitude)


time = np.arange(0, 10, 0.1);
amplitude = 3.5 + 0.5 * time
plt.plot(time, amplitude)


## non-linear
LN_amplitude   = np.log(time)

plt.plot(time, LN_amplitude)




