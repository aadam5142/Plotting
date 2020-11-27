# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:57:56 2020

@author: anwar
"""

# Providing Labels

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
    
plt.figure('lin')
plt.title('Linear')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.title('Quadratic')
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)

plt.figure('cube')
plt.title('Cubic')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.title('Exponential')
plt.xlabel('sample points')
plt.ylabel('exponential function')
plt.plot(mySamples, myExponential)

# To clean windows and labels

# plt.clf()
