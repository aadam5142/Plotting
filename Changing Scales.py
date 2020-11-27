# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:45:50 2020

@author: anwar
"""
# Changing Scales
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i*i*i)
    myExponential.append(1.5**i)
    
plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0 )
plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 4.0)
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')

plt.figure('cube exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 4.0)
plt.legend()
plt.title('Cubic vs. Exponential')
