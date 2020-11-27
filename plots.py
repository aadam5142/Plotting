# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:50:15 2020

@author: anwar
"""

# Plots

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
    myCubic.append(1**3)
    myExponential.append(1.5**i)
    
plt.figure('lin')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.plot(mySamples, myQuadratic)

plt.figure('cube')
plt.plot(mySamples, myCubic)

plt.figure('expoS')
plt.plot(mySamples, myExponential)