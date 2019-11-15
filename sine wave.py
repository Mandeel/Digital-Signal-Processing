# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:42:28 2019

@author: thulfiqar
"""

import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
 
# frequency is the number of times a wave repeats a second
frequency = 1000
 
num_samples = 96000
 
# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
 
amplitude = 16000
 
# generating the sine wave
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]

# writing the sine wave into a file
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2

file = "test.wav"
wav_file=wave.open(file, 'w')
 
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))