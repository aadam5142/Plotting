# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:16:29 2020

@author: anwar
"""
#Overlaying Plots

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
    
    
    
plt.figure('lin quad')
plt.clf()
# Adding Legends to the plot
plt.plot(mySamples, myLinear, label = 'linear') # Label for 'linear'
plt.plot(mySamples, myQuadratic, label = 'quadratic') # Label for 'quadratic'
plt.legend() # Legend for the plot
plt.title('Linear vs. Quadratic')

plt.figure('cube exp')
plt.clf()
# Adding Legends to the Plot
plt.plot(mySamples, myCubic, label = 'cubic') # Label for 'cubic'
plt.plot(mySamples, myExponential, label = 'exponential') # Label = 'exponential'
plt.legend() # Legend for the plot
plt.plot('lin quad')
plt.figure('Linear vs. Quadratic')
plt.figure('cube exp')
plt.title('Cubic vs. Exponential')