# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:17:37 2019

@author: thulfiqar
"""

import numpy as np
import matplotlib.pyplot as plt


# Get x values of the sine wave
time = np.arange(0, 10, 0.1);

# Amplitude of the sine wave is sine of a variable like time
#amplitude   = np.sin(time)
amplitude   = np.cos(time)
#amplitude   = np.exp(time)


# Plot a sine wave using time and amplitude obtained for the sine wave
plt.plot(time, amplitude)

# Give a title for the sine wave plot
plt.title('cosine wave')

# Give x axis label for the sine wave plot
plt.xlabel('Time')

# Give y axis label for the sine wave plot
plt.ylabel('Amplitude = sin(time)')

plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Display the sine wave
plt.show()

