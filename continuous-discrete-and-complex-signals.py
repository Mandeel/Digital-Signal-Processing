# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.02, 0.05, 1000)
plt.plot(t, 325 * np.sin(2*np.pi*50*t));
plt.xlabel('t');
plt.ylabel('x(t)');
plt.title(r'Plot of CT signal $x(t)=325 \sin(2\pi 50 t)$');
plt.xlim([-0.02, 0.05]);
plt.show()


n = np.arange(50);
dt = 0.07/50
x = np.sin(2 * np.pi * 50 * n * dt)
plt.xlabel('n');
plt.ylabel('x[n]');
plt.title(r'Plot of DT signal $x[n] = 325 \sin(2\pi 50 n \Delta t)$');
plt.stem(n, x);


t = np.linspace(-0.02, 0.05, 1000)
plt.subplot(2,1,1); plt.plot(t, np.exp(2j*np.pi*50*t).real );
plt.xlabel('t');
plt.ylabel('Re x(t)');
plt.title(r'Real part of  $x(t)=e^{j 100 \pi t}$');
plt.xlim([-0.02, 0.05]);
plt.subplot(2,1,2); plt.plot(t, np.exp(2j*np.pi*50*t).imag );
plt.xlabel('t');
plt.ylabel('Im x(t)');
plt.title(r'Imaginary part of  $x(t)=e^{j 100 \pi t}$');
plt.xlim([-0.02, 0.05]);
plt.show()

