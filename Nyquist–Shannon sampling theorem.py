# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:17:37 2019

@author: thulfiqar

If a function x(t) contains no frequencies higher than B hertz, it is completely determined by 
giving its ordinates at a series of points spaced 1/(2B) seconds apart.

"""

from numpy import linspace,cos,pi,ceil,floor,arange
from pylab import plot,show,axis

# sampling a signal badlimited to 40 Hz 
# with a sampling rate of 800 Hz
f = 40;  # Hz
tmin = -0.3;
tmax = 0.3;
t = linspace(tmin, tmax, 400);
signal_a = cos(2*pi*t);
signal_b = cos(2*pi*f*t);
x = signal_a + signal_b; # signal sampling
plot(t, x)

# sampling the signal with a sampling rate of 80 Hz
# in this case, we are using the Nyquist rate.
T = 1/80.0;
nmin = ceil(tmin / T);
nmax = floor(tmax / T);
n = arange(nmin,nmax);
x1 = cos(2*pi*n*T) + cos(2*pi*f*n*T);
plot(n*T, x1, 'ro')

# sampling the signal with a sampling rate of 35 Hz
# note that 35 Hz is under the Nyquist rate. (Aliasing)
#T = 1/35.0;
#nmin = ceil(tmin / T);
#nmax = floor(tmax / T);
#n = arange(nmin,nmax);
#x2 = cos(2*pi*n*T) + cos(2*pi*f*n*T);
#plot(n*T, x2, '-r.',markersize=8)

axis([-0.3, 0.3, -1.5, 2.3])
show()